"""OCR existing scanned PDFs only; preserve original files and API credentials."""
import hashlib,io,json,time,zipfile,sys,subprocess
from pathlib import Path
import requests,fitz
from inventory import ROOT

sys.stdout.reconfigure(encoding='utf-8')
BASE='https://mineru.net/api/v4'

def request_retry(session,method,url,**kwargs):
    for attempt in range(4):
        try:return session.request(method,url,**kwargs)
        except requests.exceptions.RequestException:
            if attempt==3:raise
            time.sleep(3*(attempt+1))

def run(record):
    path=Path(record['main_pdf'])
    with fitz.open(path) as doc:
        page_count=len(doc)
    if not page_count:
        print(json.dumps({'key':record['key'],'status':'corrupt-zero-page-PDF'},ensure_ascii=False),flush=True)
        return None
    directory=ROOT/'sources'/record['key'];directory.mkdir(parents=True,exist_ok=True)
    cfg=json.loads(Path(r'C:\Users\lhc\.agents\skills\paper-interpret\config.json').read_text(encoding='utf-8'))
    session=requests.Session();session.trust_env=False
    headers={'Authorization':'Bearer '+cfg['mineru_token'],'Content-Type':'application/json'}
    state=directory/'ocr-state.json';archive=directory/'ocr-result.zip'
    if not archive.exists():
        if state.exists():batch=json.loads(state.read_text(encoding='utf-8'))['batch_id']
        else:
            response=session.post(BASE+'/file-urls/batch',json={'files':[{'name':record['key']+'.pdf'}],'model_version':'vlm'},headers=headers,timeout=60)
            response.raise_for_status();data=response.json()
            if data.get('code')!=0:raise RuntimeError('OCR upload link failed: '+str(data.get('msg',''))[:160])
            batch=data['data']['batch_id']
            upload=session.put(data['data']['file_urls'][0],data=path.read_bytes(),timeout=180);upload.raise_for_status()
            state.write_text(json.dumps({'batch_id':batch,'original_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}),encoding='utf-8')
        deadline=time.monotonic()+1200
        while time.monotonic()<deadline:
            response=request_retry(session,'GET',BASE+'/extract-results/batch/'+batch,headers=headers,timeout=60);response.raise_for_status();data=response.json()
            if data.get('code')!=0:raise RuntimeError('OCR status failed')
            item=data['data']['extract_result'][0]
            print(json.dumps({'key':record['key'],'ocr_status':item['state']},ensure_ascii=False),flush=True)
            if item['state']=='failed':raise RuntimeError('OCR parse failed: '+str(item.get('err_msg',''))[:150])
            if item['state']=='done':
                try:
                    download=request_retry(session,'GET',item['full_zip_url'],timeout=180);download.raise_for_status();archive.write_bytes(download.content)
                except requests.exceptions.SSLError:
                    # Windows curl uses the OS certificate store; TLS verification stays on.
                    fetched=subprocess.run(['curl.exe','--fail','--location','--max-time','180','--output',str(archive),item['full_zip_url']],capture_output=True)
                    if fetched.returncode:raise RuntimeError('OCR archive TLS verification failed with both Python and Windows curl')
                break
            time.sleep(15)
        else:raise RuntimeError('OCR timeout; batch state preserved')
    with zipfile.ZipFile(archive) as result:
        md_name=next((n for n in result.namelist() if n.endswith('full.md')),None)
        if not md_name:raise RuntimeError('OCR full text absent')
        text=result.read(md_name).decode('utf-8')
        (directory/'ocr-full.md').write_text(text,encoding='utf-8')
        page_text=[]
        for name in result.namelist():
            if name.endswith('content_list.json'):
                entries=json.loads(result.read(name))
                for e in entries:
                    if not isinstance(e,dict):continue
                    content=e.get('text') or '\n'.join(e.get('image_caption',[])) or '\n'.join(e.get('table_caption',[]))
                    if content:page_text.append('[PDF physical page '+str(int(e.get('page_idx',0))+1)+']\n'+str(content))
                break
        source='OCR 转写；原文扫描图像优先，不能把 OCR 字符识别当作已核实科学事实。\n\n'+'\n\n'.join(page_text or [text])
        if len(source)<2500:raise RuntimeError('OCR text too short')
        (directory/'main-text.txt').write_text(source,encoding='utf-8')
    attachment=record['pdf_attachments'][0]['key']
    prepared=dict(record,status='ready',main_attachment_key=attachment,main_pdf_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pdf_pages=page_count,source_text=str(directory/'main-text.txt'),supplements=[],figure_candidates=[],pdf_identity={'ocr_requires_visual_confirmation':True},source_text_method='MinerU scanned-PDF OCR')
    (directory/'prepared.json').write_text(json.dumps(prepared,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'key':record['key'],'status':'OCR-ready','pages':page_count,'source_chars':len(source)},ensure_ascii=False),flush=True)
    return prepared

def main():
    inventory=ROOT/'prepared-inventory.json';data=json.loads(inventory.read_text(encoding='utf-8'))
    for record in data['records']:
        if record['status']!='blocked-text-extraction':continue
        try:
            prepared=run(record)
            if prepared:
                latest=json.loads(inventory.read_text(encoding='utf-8'))
                latest['records']=[prepared if r['key']==prepared['key'] else r for r in latest['records']]
                temp=inventory.with_suffix('.json.tmp');temp.write_text(json.dumps(latest,ensure_ascii=False,indent=2),encoding='utf-8');temp.replace(inventory)
        except Exception as error:print(json.dumps({'key':record['key'],'status':'OCR-blocked','error':str(error)[:200]},ensure_ascii=False),flush=True)

if __name__=='__main__':main()

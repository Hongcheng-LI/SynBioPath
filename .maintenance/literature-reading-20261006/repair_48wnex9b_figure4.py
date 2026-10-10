from pathlib import Path
import fitz,hashlib,json,requests,datetime
root=Path(r'C:\Software\Data\05-Obsidian\SynBioPath\.maintenance\literature-reading-20261006'); key='48WNEX9B'; directory=root/'sources'/key
pdf=Path(r'C:\Software\Data\02-Zotero\storage\BJRV3QBX\2026-Science Advances-A minimal transcription factor network is sufficient to drive paclitaxel biosynthesis.pdf')
expected='718c1a125836f2f592ca154fb969244a31cc148073f5811e5c7baf840c6b8586'
h=lambda b:hashlib.sha256(b).hexdigest()
source_sha=h(pdf.read_bytes())
if source_sha!=expected: raise RuntimeError('source PDF hash mismatch')
with fitz.open(pdf) as doc:
 page=doc[5]; bbox=(15,295,582,720); rect=fitz.Rect(*bbox)
 pix=page.get_pixmap(matrix=fitz.Matrix(3,3),clip=rect,alpha=False); data=pix.tobytes('png'); digest=h(data)
 out=directory/f'{key}-Figure-4-p6-manual-{digest[:16]}.png'; out.write_bytes(data)
pubp=directory/'publication.json'; pub=json.loads(pubp.read_text(encoding='utf-8'))
image=next(i for i in pub['images'] if i['label']=='Figure 4' and i['page']==6)
old_url=image['url']; old_sha=image['sha256']
cachep=directory/'uploads.json'; cache=json.loads(cachep.read_text(encoding='utf-8')) if cachep.exists() else {}
if digest in cache: url=cache[digest]
else:
 s=requests.Session(); s.trust_env=False
 response=s.post('http://127.0.0.1:36677/upload',json={'list':[str(out)]},timeout=180); response.raise_for_status(); result=response.json()
 if not result.get('success') or len(result.get('result',[]))!=1: raise RuntimeError('PicGo upload failed')
 url=result['result'][0]
remote=requests.get(url,timeout=90); remote.raise_for_status(); remote_sha=h(remote.content)
if remote_sha!=digest: raise RuntimeError('remote crop hash mismatch')
note=Path(pub['note']); content=note.read_text(encoding='utf-8')
if content.count(old_url)!=1: raise RuntimeError('old URL count unexpected')
note.write_text(content.replace(old_url,url),encoding='utf-8')
image.update({'file':str(out),'bbox':list(bbox),'sha256':digest,'url':url})
# Update the corresponding normalized crop in published and source drafts.
part=next(p for fig in pub['draft_metadata']['figures'] if fig['label']=='Figure 4' for p in fig['pages'] if p['page']==6)
part['bbox']=[bbox[0]/page.rect.width,bbox[1]/page.rect.height,bbox[2]/page.rect.width,bbox[3]/page.rect.height]
for draft_name in ['normalized-draft.json','repaired-draft.json']:
 path=directory/draft_name
 if path.exists():
  obj=json.loads(path.read_text(encoding='utf-8')); d=obj.get('draft',obj)
  for fig in d.get('figures',[]):
   if fig.get('label')=='Figure 4':
    for p in fig.get('pages',[]):
     if p.get('page')==6: p['bbox']=[bbox[0]/page.rect.width,bbox[1]/page.rect.height,bbox[2]/page.rect.width,bbox[3]/page.rect.height]
  path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
cache[digest]=url; cachep.write_text(json.dumps(cache,ensure_ascii=False,indent=2),encoding='utf-8')
entry={'key':key,'label':'Figure 4','page':6,'bbox':list(bbox),'dimensions':[pix.width,pix.height],'sha256':digest,'remote_sha256':remote_sha,'url':url,'previous_url':old_url,'previous_sha256':old_sha,'file':str(out),'reason':'exclude preceding body text while preserving all panels and complete caption'}
pub.setdefault('manual_crop_audit',[]).append({'timestamp':datetime.datetime.now().astimezone().isoformat(),'source_pdf':str(pdf),'source_pdf_sha256_before_and_after':source_sha,'crops':[entry]})
pubp.write_text(json.dumps(pub,ensure_ascii=False,indent=2),encoding='utf-8')
auditp=root/'manual-crop-repair-audit-20261010.json'; audit=json.loads(auditp.read_text(encoding='utf-8')); audit['items'].append(entry); audit['updated']=datetime.datetime.now().astimezone().isoformat(); auditp.write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
if note.read_text(encoding='utf-8').count(url)!=1: raise RuntimeError('note URL verification failed')
print(json.dumps(entry,ensure_ascii=False))

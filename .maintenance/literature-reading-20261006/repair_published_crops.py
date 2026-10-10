from pathlib import Path
import fitz, hashlib, json, requests, datetime, sys

ROOT = Path(r'C:\Software\Data\05-Obsidian\SynBioPath\.maintenance\literature-reading-20261006')
VAULT = Path(r'C:\Software\Data\05-Obsidian\SynBioPath')
CASES = {
 'EYHR26TJ': {
  'pdf': Path(r'C:\Software\Data\02-Zotero\storage\H8WG5INA\2026-FoTO1 orchestrates taxol biosynthesis through catalytic and non-catalytic mechanisms.pdf'),
  'sha256': '09d16d4dd6ed76f7fd686344e03ee77000bffc43cac0e79c52c548872f9035a3',
  'crops': [
   ('Figure 2',15,(66,65,550,264),'remove full-page continuation; keep caption continuation'),
   ('Figure 3',17,(66,65,548,518),'remove full-page continuation; keep caption continuation'),
   ('Figure 4',19,(66,65,550,222),'remove full-page continuation; keep caption continuation'),
  ]},
 '48WNEX9B': {
  'pdf': Path(r'C:\Software\Data\02-Zotero\storage\BJRV3QBX\2026-Science Advances-A minimal transcription factor network is sufficient to drive paclitaxel biosynthesis.pdf'),
  'sha256': '718c1a125836f2f592ca154fb969244a31cc148073f5811e5c7baf840c6b8586',
  'crops': [
   ('Figure 1',2,(30,45,582,620),'include full figure and complete caption; exclude following body text'),
   ('Figure 3',5,(30,45,582,470),'include full figure and complete caption; exclude following body text'),
   ('Figure 4',6,(15,285,582,720),'include all panels and complete caption'),
  ]}
}

def sha(data): return hashlib.sha256(data).hexdigest()
def write_json(path,data): path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def patch_draft_file(path, updates, sizes):
 if not path.exists(): return
 obj=json.loads(path.read_text(encoding='utf-8')); draft=obj.get('draft',obj)
 for fig in draft.get('figures',[]):
  for part in fig.get('pages',[]):
   item=updates.get((fig.get('label'),int(part.get('page',-1))))
   if item:
    w,h=sizes[int(part['page'])]
    x0,y0,x1,y1=item['bbox']
    part['bbox']=[x0/w,y0/h,x1/w,y1/h]
 if 'draft' in obj: obj['draft']=draft
 write_json(path,obj)

local=requests.Session(); local.trust_env=False
remote=requests.Session()
all_audit=[]
for key,case in CASES.items():
 pdf=case['pdf']; pdf_bytes=pdf.read_bytes(); source_sha=sha(pdf_bytes)
 if source_sha != case['sha256']: raise RuntimeError(f'{key}: source PDF hash changed: {source_sha}')
 directory=ROOT/'sources'/key
 pub_path=directory/'publication.json'; pub=json.loads(pub_path.read_text(encoding='utf-8'))
 note=Path(pub['note']); note_text=note.read_text(encoding='utf-8')
 cache_path=directory/'uploads.json'; cache=json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}
 updates={}; sizes={}; entries=[]
 with fitz.open(pdf) as doc:
  for label,page_no,bbox,reason in case['crops']:
   page=doc[page_no-1]; rect=fitz.Rect(*bbox)
   if not page.rect.contains(rect): raise RuntimeError(f'{key}/{label}/p{page_no}: crop outside page {page.rect}: {rect}')
   pix=page.get_pixmap(matrix=fitz.Matrix(3.0,3.0),clip=rect,alpha=False)
   image_bytes=pix.tobytes('png'); digest=sha(image_bytes)
   out=directory/f'{key}-{label.replace(" ","-")}-p{page_no}-manual-{digest[:16]}.png'
   out.write_bytes(image_bytes)
   image=next((im for im in pub['images'] if im['label']==label and int(im['page'])==page_no),None)
   if image is None: raise RuntimeError(f'{key}: publication image missing for {label} p{page_no}')
   old_url=image['url']; old_sha=image['sha256']
   if digest in cache:
    url=cache[digest]
   else:
    response=local.post('http://127.0.0.1:36677/upload',json={'list':[str(out)]},timeout=180)
    response.raise_for_status(); result=response.json()
    if not result.get('success') or len(result.get('result',[]))!=1: raise RuntimeError(f'{key}/{label}: PicGo upload failed: {result}')
    url=result['result'][0]
    if not isinstance(url,str) or not url.startswith(('https://','http://')): raise RuntimeError(f'{key}/{label}: invalid PicGo URL {url!r}')
   fetched=remote.get(url,timeout=90); fetched.raise_for_status(); remote_sha=sha(fetched.content)
   if remote_sha!=digest: raise RuntimeError(f'{key}/{label}: uploaded hash mismatch {remote_sha} != {digest}')
   cache[digest]=url
   image.update({'file':str(out),'bbox':list(bbox),'sha256':digest,'url':url})
   count=note_text.count(old_url)
   if count != 1: raise RuntimeError(f'{key}: expected one note URL for {old_url}, got {count}')
   note_text=note_text.replace(old_url,url)
   updates[(label,page_no)]={'bbox':list(bbox),'url':url,'sha256':digest,'old_url':old_url,'old_sha256':old_sha,'file':str(out),'page':page_no,'label':label,'reason':reason,'dimensions':[pix.width,pix.height]}
   sizes[page_no]=(page.rect.width,page.rect.height)
   entries.append({'key':key,'label':label,'page':page_no,'bbox':list(bbox),'dimensions':[pix.width,pix.height],'sha256':digest,'remote_sha256':remote_sha,'url':url,'previous_url':old_url,'previous_sha256':old_sha,'file':str(out),'reason':reason})
 # Reflect the revised source crops in the saved metadata/drafts.
 patch_draft_file(directory/'normalized-draft.json',updates,sizes)
 patch_draft_file(directory/'repaired-draft.json',updates,sizes)
 for fig in pub.get('draft_metadata',{}).get('figures',[]):
  for part in fig.get('pages',[]):
   item=updates.get((fig.get('label'),int(part.get('page',-1))))
   if item:
    w,h=sizes[int(part['page'])]; x0,y0,x1,y1=item['bbox']
    part['bbox']=[x0/w,y0/h,x1/w,y1/h]
 if key=='48WNEX9B':
  review=pub.get('source_review',{})
  if 'minor_issues' in review:
   review['manual_crop_resolved_issues']=review['minor_issues']
   review['minor_issues']=[]
  review['crop_complete']=True
 if key=='EYHR26TJ':
  gaps=pub.get('draft_metadata',{}).get('source_gaps',[])
  pub['draft_metadata']['source_gaps']=[g for g in gaps if 'screenshots use full original pages' not in g and 'screenshots use original full pages' not in g and 'screenshots are full pages' not in g and 'screenshots use the full original page' not in g and '截图采用原文整页' not in g]
  note_text=note_text.replace('；为保留全部图版与图注，截图采用原文整页。','。').replace('为保留全部图版与图注，截图采用原文整页。','')
 audit={'timestamp':datetime.datetime.now().astimezone().isoformat(),'source_pdf':str(pdf),'source_pdf_sha256_before_and_after':source_sha,'crops':entries}
 pub['manual_crop_audit']=pub.get('manual_crop_audit',[])+[audit]
 note.write_text(note_text,encoding='utf-8')
 write_json(cache_path,cache); write_json(pub_path,pub)
 # Verify the written note points to each new crop exactly once.
 saved=note.read_text(encoding='utf-8')
 for item in entries:
  if saved.count(item['url'])!=1: raise RuntimeError(f'{key}: updated note link not verified for {item["label"]}')
 all_audit.extend(entries)
 print(json.dumps({'key':key,'note':str(note),'replaced_crops':len(entries),'urls_sha_verified':len(entries)},ensure_ascii=False),flush=True)

write_json(ROOT/'manual-crop-repair-audit-20261010.json',{'updated':datetime.datetime.now().astimezone().isoformat(),'items':all_audit})
print(json.dumps({'total_replaced_crops':len(all_audit),'audit':str(ROOT/'manual-crop-repair-audit-20261010.json')},ensure_ascii=False))

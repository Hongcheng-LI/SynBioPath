import json,hashlib,re,datetime
from pathlib import Path
import worker as w
rows=[]
for key in ['D2T4CM4K','E4HTE8GN','AK9B4YFU']:
    d=w.ROOT/'sources'/key
    rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
    pub=json.loads((d/'publication.json').read_text(encoding='utf-8'))
    draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
    note=Path(pub['note']);body=note.read_text(encoding='utf-8')
    w.validate_structure(draft)
    expected=len(pub['images'])
    checks={'source_pdf_unchanged':hashlib.sha256(Path(rec['main_pdf']).read_bytes()).hexdigest()==rec['main_pdf_sha256'],'eight_main_chapters':len(re.findall(r'^# ',body,re.M))==8,'no_unresolved_figure_markers':'<!--FIGURE:' not in body,'all_image_urls_embedded':all(x['url'] in body for x in pub['images']),'all_local_crops_intact':all(hashlib.sha256(Path(x['file']).read_bytes()).hexdigest()==x['sha256'] for x in pub['images']),'actual_image_embed_count':len(re.findall(r'!\[[^\]]*\]\(https://',body))==expected,'source_review_pass':pub['source_review']['pass'],'deferred_directory':'文献笔记待归类' in str(note)}
    if not all(checks.values()):raise RuntimeError((key,checks))
    rows.append({'key':key,'note':str(note),'images':expected,'checks':checks})
baseline=json.loads((w.ROOT/'existing-note-hashes.json').read_text(encoding='utf-8'))
unchanged=[];changed=[]
for item in baseline:
    p=w.VAULT/item['path']
    (unchanged if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'] else changed).append(item['path'])
result={'time':datetime.datetime.now().isoformat(),'new_notes':rows,'existing_baseline_files':len(baseline),'existing_baseline_unchanged':len(unchanged),'existing_baseline_changed':changed,'remote_verification':'publish uses PicGo and GET content SHA256 per image; no redundant remote download in this audit'}
w.write_json(w.ROOT/'codex-three-paper-integrity-d2-e4-ak-20261007.json',result)
print(json.dumps(result,ensure_ascii=False))


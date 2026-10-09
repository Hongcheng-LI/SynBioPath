import json,hashlib,re,datetime
from pathlib import Path
import worker as w
rows=[]
for key in ['DW2KXVKT']:
    d=w.ROOT/'sources'/key;rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));pub=json.loads((d/'publication.json').read_text(encoding='utf-8'));draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft'];note=Path(pub['note']);body=note.read_text(encoding='utf-8');w.validate_structure(draft);expected=len(pub['images'])
    checks={'source_pdf_unchanged':hashlib.sha256(Path(rec['main_pdf']).read_bytes()).hexdigest()==rec['main_pdf_sha256'],'eight_research_chapters':len(re.findall(r'^# ',body,re.M))==8,'no_unresolved_figure_markers':'<!--FIGURE:' not in body,'all_image_urls_embedded':all(x['url'] in body for x in pub['images']),'all_local_crops_intact':all(hashlib.sha256(Path(x['file']).read_bytes()).hexdigest()==x['sha256'] for x in pub['images']),'actual_image_embed_count':len(re.findall(r'!\[[^\]]*\]\(https://',body))==expected,'source_review_pass':pub['source_review']['pass'],'deferred_directory':'文献笔记待归类' in str(note)}
    if key=='unused':
        checks['Table1_both_pages_embedded']=sorted(x['page'] for x in pub['images'] if x['label']=='Table 1')==[3,4]
        checks['Table2_both_pages_embedded']=sorted(x['page'] for x in pub['images'] if x['label']=='Table 2')==[5,6]
        checks['module2_not_invented']='第 2 模块下方没有给出底物名称' in body
    if not all(checks.values()):raise RuntimeError((key,checks))
    rows.append({'key':key,'note':str(note),'images':expected,'checks':checks})
baseline=json.loads((w.ROOT/'existing-note-hashes.json').read_text(encoding='utf-8'));changed=[]
for item in baseline:
    p=w.VAULT/item['path']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:changed.append(item['path'])
pubs=[json.loads(p.read_text(encoding='utf-8')) for p in (w.ROOT/'sources').glob('*/publication.json')]
inv=json.loads((w.ROOT/'prepared-inventory.json').read_text(encoding='utf-8'))
result={'time':datetime.datetime.now().isoformat(),'new_notes':rows,'existing_baseline_files':len(baseline),'existing_baseline_unchanged':len(baseline)-len(changed),'existing_baseline_changed':changed,'remote_verification':'publish uses PicGo and GET content SHA256 per image','excluded_heptose_paper_has_no_publication':not(w.ROOT/'sources'/'2E5UEWNP'/'publication.json').exists(),'published_notes_total':len(pubs),'images_total':sum(len(x['images']) for x in pubs),'remaining_ready':sum(x.get('status')=='ready' and not(w.ROOT/'sources'/x['key']/'publication.json').exists() for x in inv['records'])}
if changed or not result['excluded_heptose_paper_has_no_publication']:raise RuntimeError(result)
w.write_json(w.ROOT/'codex-paper-integrity-dw-20261009.json',result);print(json.dumps(result,ensure_ascii=False))

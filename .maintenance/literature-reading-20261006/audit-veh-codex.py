import json,hashlib,re,datetime
from pathlib import Path
import worker as w
d=w.ROOT/'sources'/'VEHEPT5K';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));pub=json.loads((d/'publication.json').read_text(encoding='utf-8'));draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft'];note=Path(pub['note']);body=note.read_text(encoding='utf-8');w.validate_structure(draft)
checks={'source_pdf_unchanged':hashlib.sha256(Path(rec['main_pdf']).read_bytes()).hexdigest()==rec['main_pdf_sha256'],'eight_research_chapters':len(re.findall(r'^# ',body,re.M))==8,'no_unresolved_figure_markers':'<!--FIGURE:' not in body,'all_image_urls_embedded':all(x['url'] in body for x in pub['images']),'all_local_crops_intact':all(hashlib.sha256(Path(x['file']).read_bytes()).hexdigest()==x['sha256'] for x in pub['images']),'actual_image_embed_count':len(re.findall(r'!\[[^\]]*\]\(https://',body))==5,'all_main_figures_tables':sorted(x['label'] for x in pub['images'])==['Figure 1','Figure 2','Figure 3','Figure 4','Table 1'],'source_review_pass':pub['source_review']['pass'],'deferred_directory':'文献笔记待归类' in str(note),'microgram_units_correct':'204 ± 1 μg/L' in body and '306 ± 3 μg/L' in body,'UPC_attribution_correct':'CEN5 到 CEN7' in body and '均值相同' in body,'GGOH_not_direct_GGPP':'GGOH 是已经离开带二磷酸前体状态' in body,'fold_change_baselines_explicit':'27.2、38.2' in body,'all_raw_not_claimed':'未取得原始 GC-MS' in body}
assert all(checks.values()),checks
baseline=json.loads((w.ROOT/'existing-note-hashes.json').read_text(encoding='utf-8'));changed=[]
for item in baseline:
 p=w.VAULT/item['path']
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:changed.append(item['path'])
pubs=[json.loads(p.read_text(encoding='utf-8')) for p in (w.ROOT/'sources').glob('*/publication.json')];inv=json.loads((w.ROOT/'prepared-inventory.json').read_text(encoding='utf-8'))
result={'time':datetime.datetime.now().isoformat(),'new_notes':[{'key':rec['key'],'note':str(note),'images':len(pub['images']),'checks':checks}],'existing_baseline_files':len(baseline),'existing_baseline_unchanged':len(baseline)-len(changed),'existing_baseline_changed':changed,'remote_verification':'publish uses PicGo and GET content SHA256 per image','excluded_heptose_paper_has_no_publication':not(w.ROOT/'sources'/'2E5UEWNP'/'publication.json').exists(),'published_notes_total':len(pubs),'images_total':sum(len(x['images']) for x in pubs),'remaining_ready':sum(x.get('status')=='ready' and not(w.ROOT/'sources'/x['key']/'publication.json').exists() for x in inv['records'])}
assert not changed and result['excluded_heptose_paper_has_no_publication'],result
w.write_json(w.ROOT/'codex-paper-integrity-veh-20261009.json',result);print(json.dumps(result,ensure_ascii=False))

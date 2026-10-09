import json,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'A4UKNEHC';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));packet=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'));draft=packet['draft'];draft['report']=(d/'codex-report.md').read_text(encoding='utf-8');draft['source_gaps'].append('Table2 entry5 65percent9c versus body13a to9b; discrepancy retained')
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'));pdf=fitz.open(rec['main_pdf']);bbox=[305,495,546,608];p=pdf[1]
for x in images:
 if x['label']=='Figure 3':
  out=d/'A4UKNEHC-Figure-3-p2-complete-refined.png';p.get_pixmap(dpi=300,clip=fitz.Rect(bbox)).save(out);sha=hashlib.sha256(out.read_bytes()).hexdigest();out2=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(out2);x.update(file=str(out2),bbox=bbox,sha256=sha);print(str(out2))
for f in draft['figures']:
 if f['label']=='Figure 3':f['pages'][0]['bbox']=[bbox[0]/p.rect.width,bbox[1]/p.rect.height,bbox[2]/p.rect.width,bbox[3]/p.rect.height]
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',packet);w.write_json(d/'codex-crops.json',images)

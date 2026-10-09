from pathlib import Path
import fitz,json
d=Path(__file__).parent/'sources'/'JJ77V5A7';r=json.loads((d/'prepared.json').read_text(encoding='utf-8'));pdf=fitz.open(r['main_pdf']);out=d/'codex-pages';out.mkdir(exist_ok=True)
for i,p in enumerate(pdf):
 p.get_pixmap(dpi=120).save(str(out/f'p{i+1:02}.png'));(d/f'page-{i+1:02}.txt').write_text(p.get_text(sort=True),encoding='utf-8')
print('Rendered ten original pages')

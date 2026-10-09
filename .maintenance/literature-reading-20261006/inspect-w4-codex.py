from pathlib import Path
import fitz,json
d=Path(__file__).parent/'sources'/'W4IHDLC6';r=json.loads((d/'prepared.json').read_text(encoding='utf-8'));pdf=fitz.open(r['main_pdf']);out=d/'codex-pages';out.mkdir(exist_ok=True)
for i,p in enumerate(pdf):
 p.get_pixmap(dpi=110).save(str(out/f'p{i+1:02}.png'));(d/f'page-{i+1:02}.txt').write_text(p.get_text(sort=True),encoding='utf-8')
print('Rendered three main pages',pdf[0].rect)

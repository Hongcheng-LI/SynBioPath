from pathlib import Path
import fitz,json
d=Path(__file__).parent/'sources'/'A2J2FZZU';r=json.loads((d/'prepared.json').read_text(encoding='utf-8'));pdf=fitz.open(r['main_pdf']);out=d/'codex-pages';out.mkdir(exist_ok=True)
for i,p in enumerate(pdf):p.get_pixmap(dpi=150).save(str(out/f'p{i+1:02}.png'))
print('Rendered four main pages')

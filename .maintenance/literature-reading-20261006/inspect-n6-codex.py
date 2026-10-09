import json,fitz
import worker as w
d=w.ROOT/'sources'/'N6EIP5DM';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));doc=fitz.open(rec['main_pdf'])
for i in [1,4,5,7,8,9,10,16]:
 p=doc[i];p.get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(d/f'codex-page-{i+1:03}.png')
 print(i+1,tuple(p.rect),[(tuple(round(v,1) for v in x['bbox'])) for x in p.get_image_info() if fitz.Rect(x['bbox']).get_area()>3000])
for i in range(13,19):
 print('\nPAGE',i+1)
 for b in doc[i].get_text('blocks'):print(' '.join(b[4].split()))

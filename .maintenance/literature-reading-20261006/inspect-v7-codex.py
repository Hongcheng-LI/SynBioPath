import fitz,json,hashlib
import worker as w
d=w.ROOT/'sources'/'V7XAHPMQ'
p=w.Path(r'C:\Software\Data\02-Zotero\storage\6L9NBJ3Z\s41586-025-09697-2.pdf')
doc=fitz.open(p)
for i in [0,1,2,3,5,6,12,13,14,15,16]:
 page=doc[i];page.get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(d/f'final-page-{i+1:03}.png')
 print(i+1,tuple(page.rect),[(tuple(round(v,1) for v in im['bbox'])) for im in page.get_image_info()])
print('final_source_sha256',hashlib.sha256(p.read_bytes()).hexdigest())

import json,hashlib,re
import fitz
from PIL import Image
import worker as w
d=w.ROOT/'sources'/'KHP3QFIE'
rec=json.loads((d/'prepared.json').read_text(encoding='utf8'))
doc=fitz.open(rec['main_pdf'])
specs=[('Figure 1',[(3,[43,46,553,702]),(4,[43,46,553,655])],list('ABCDEFGHIJ'),'原文 Figure 1：天然 IDR、异戊烯基吲哚反应与 TS 功能，跨页全部 A–J 子图及完整原图注'),('Figure 2',[(5,[43,46,553,721])],list('ABCDEFGHI'),'原文 Figure 2：IDR 相互作用、凝聚体及级联催化，全部 A–I 子图与完整原图注')]
images=[];figures=[]
for label,parts,panels,caption in specs:
 rasters=[];sources=[]
 for page,bbox in parts:
  pg=doc[page-1];pix=pg.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=fitz.Rect(bbox),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);rasters.append(im)
  sources.append({'page':page,'bbox':[bbox[0]/pg.rect.width,bbox[1]/pg.rect.height,bbox[2]/pg.rect.width,bbox[3]/pg.rect.height],'dpi':300})
 if len(rasters)>1:
  combined=Image.new('RGB',(max(x.width for x in rasters),sum(x.height for x in rasters)+12),'white');offset=0
  for im in rasters:combined.paste(im,(0,offset));offset+=im.height+12
 else:combined=rasters[0]
 file=d/('KHP3QFIE-'+label.replace(' ','-')+'-complete.png');combined.save(file)
 images.append({'label':label,'caption':caption,'page':parts[0][0],'file':str(file),'bbox':parts[0][1],'source_parts':sources,'panels':panels,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
 figures.append({'label':label,'caption':caption,'panels':panels,'pages':sources})
draft={'identity_matches':True,'identity_reason':'Printed main PDF and current live Zotero title, all ten authors and DOI match; Quick Report; 2026 online date; nine physical pages read and viewed','paper_type':'research','source_article_type':'Quick Report','title_zh':'天然IDR相分离与萜类级联催化','filename_title':'天然IDR相分离与萜类级联催化','journal_short':'Sci China Life Sci','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':['本地无补充文件，Figure S1–S70、补表及详细结构谱图未独立复核','Figure 2C 图注与图内标签、正文不一致；Figure 1E 图注包含自指表述，保留来源问题','主文提供相对产物量，缺完整绝对产率、动力学、置信区间与多重比较说明','酵母 FPP 萃取与测定身份需补充材料核查；机制中水排除和碳正离子稳定属解释'],'report':(d/'codex-report.md').read_text(encoding='utf8'),'figures':figures}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft});w.write_json(d/'codex-crops.json',images)
print(json.dumps({'cjk':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

import json,hashlib,re,fitz
from PIL import Image
import worker as w
d=w.ROOT/'sources'/'RTPSCVUP';rec=json.loads((d/'prepared.json').read_text(encoding='utf8'));doc=fitz.open(rec['main_pdf']);scale=300/72
specs=[('Figure 1',3,[[305,63,558,561]],list('ABCDEF'),'single'),('Figure 2',4,[[60,63,310,735],[318,630,568,735]],list('ABCDEFGHIJKLMN'),'caption-continuation-below'),('Figure 3',5,[[48,63,378,511],[385,63,556,317]],list('ABCDEF'),'side-caption'),('Figure 4',6,[[60,63,389,300],[396,63,568,258]],list('ABCDEFGHIJK'),'side-caption'),('Figure 5',7,[[48,63,557,357]],list('ABCDEFG'),'single'),('Figure 6',8,[[60,63,568,438]],[],'single')]
images=[];figures=[]
for label,page,boxes,panels,mode in specs:
 pg=doc[page-1];parts=[]
 for b in boxes:
  pix=pg.get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(b),alpha=False);parts.append(Image.frombytes('RGB',[pix.width,pix.height],pix.samples))
 if mode=='caption-continuation-below':
  canvas=Image.new('RGB',(max(p.width for p in parts),sum(p.height for p in parts)+25),'white');y=0
  for part in parts:canvas.paste(part,(0,y));y+=part.height+25
 elif mode=='side-caption':
  canvas=Image.new('RGB',(sum(p.width for p in parts)+29,max(p.height for p in parts)),'white');x=0
  for part in parts:canvas.paste(part,(x,0));x+=part.width+29
 else:canvas=parts[0]
 file=d/('RTPSCVUP-'+label.replace(' ','-')+'-complete.png');canvas.save(file)
 caption=next(x['caption'] for x in rec['figure_candidates'] if x['label']==label)
 if label=='Figure 2':
  caption+='\n'+next(b[4] for b in pg.get_text('blocks') if b[4].startswith('(L) Biomass'))
 normalized=[{'page':page,'bbox':[b[0]/pg.rect.width,b[1]/pg.rect.height,b[2]/pg.rect.width,b[3]/pg.rect.height],'dpi':300} for b in boxes]
 figures.append({'label':label,'caption':caption,'panels':panels,'pages':normalized,'original_crop_parts':normalized,'composition':mode})
 images.append({'label':label,'caption':caption,'page':page,'bbox':boxes[0],'crop_parts':boxes,'composition':mode,'panels':panels,'file':str(file),'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
draft={'identity_matches':True,'identity_reason':'PDF title 13authors DOI PlantCommunications7 101830 and liveZotero match. Published19March2026 distinct May11volume date.','paper_type':'research','source_article_type':'Resource article','title_zh':'丹参毛状根的萜类前体合成与放大边界','filename_title':'丹参毛状根的萜类前体合成与放大边界','journal_short':'Plant Commun','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':['本地未附补充文件和Source data，PPD、5L反应器、部分表达及生物量辅助证据只按主文转述','GC-MS方法paclitaxel用词、Figure2I生长引用及WRKY61/ERF106参考文献存在不一致','前体池与转录不是直接通量或靶启动子结合证明，组合路线未作完整因子交互检验','taxadiene专用标准品/响应因子/校准详情主文不足；全紫杉醇/全皂苷与优化株系放大未验证','精确P值、置信区间、多重比较、放大误差与总体独立性尚未充分报告'],'report':(d/'codex-report.md').read_text(encoding='utf8'),'figures':figures}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft});w.write_json(d/'codex-crops.json',images)
w.write_json(d/'codex-arithmetic.json',{'W61_1_to_TS1':45.53/3.02,'W61_3_to_TS1':41.84/3.02,'W61_1_to_directparent':45.53/7.69,'W61_3_to_directparent':41.84/7.69,'final_to_TS1':65.17/3.02,'final_to_TS8_Figure6_baseline':65.17/4.29,'final_to_same_W61_uninduced':65.17/45.53,'scale_to_same_shake_line':8.52/7.69,'taxadiene_unit':'mg/kg fresh weight','PPD_unit':'mg/kg dry weight','scale_up_line':'CPS(-)/TS(+)#3','scale_up_mgkgFW':8.52,'highest_optimized_line_mgkgFW':65.17,'FW_DW_conversion_performed':False,'scale_significance_unreported':True,'fold_changes_multiplied':False,'SI_read':False})
print(json.dumps({'CJK':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[i['file'] for i in images]},ensure_ascii=False))

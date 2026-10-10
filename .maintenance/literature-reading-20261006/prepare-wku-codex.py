import json,hashlib,re,fitz
import worker as w
d=w.ROOT/'sources'/'WKUSI2EY';rec=json.loads((d/'prepared.json').read_text(encoding='utf8'));doc=fitz.open(rec['main_pdf'])
specs=[('Graphical Abstract',1,[200,319,465,450],[]),('Figure 1',2,[36,313,562,747],list('abcdefg')),('Figure 2',5,[36,53,562,519],list('abcdefghijkl')),('Figure 3',6,[36,53,562,544],list('abcdefgh')),('Figure 4',7,[36,53,562,640],list('abcdefghijklmnopqrs')),('Figure 5',9,[36,53,562,348],list('abcdef')),('Figure 6',10,[36,323,562,747],list('abc'))]
images=[];figures=[];extra=[]
for label,page,bbox,panels in specs:
 pg=doc[page-1];file=d/('WKUSI2EY-'+label.replace(' ','-')+'-complete.png');pg.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=fitz.Rect(bbox),alpha=False).save(str(file));caption=next((x['caption'] for x in rec['figure_candidates'] if x['label']==label),'Graphical Abstract：原文首页完整图形摘要，MVA 到萜类的多酶组装示意')
 meta={'label':label,'caption':caption,'panels':panels,'pages':[{'page':page,'bbox':[bbox[0]/pg.rect.width,bbox[1]/pg.rect.height,bbox[2]/pg.rect.width,bbox[3]/pg.rect.height],'dpi':300}]}
 (extra if label=='Graphical Abstract' else figures).append(meta)
 images.append({'label':label,'caption':caption,'page':page,'bbox':bbox,'panels':panels,'file':str(file),'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
draft={'identity_matches':True,'identity_reason':'Printed title ten authors DOI BioresourceTechnology459135232 online24June2026 matches current Zotero; date2026-11 is volume date not first online','paper_type':'research','source_article_type':'Research article','title_zh':'生物正交多酶组装与萜类体外合成','filename_title':'生物正交多酶组装与萜类体外合成','journal_short':'Bioresour Technol','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':['补充文件未在本地，随机交联流程、序列、FTIR、电镜与标准曲线未独立复核','Figure3构建命名、Figure5非等摩尔对象与引用图号、taxadiene融合端向存在来源不一致','主文n=3未充分交代独立性质与误差类型；未报告全部检验、精确P、置信区间','溶液组装拓扑及直接通道化尚未建立；taxadiene为初步定性而非绝对滴度'],'report':(d/'codex-report.md').read_text(encoding='utf8'),'figures':figures,'additional_original_graphics':extra}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft});w.write_json(d/'codex-crops.json',images);print(json.dumps({'cjk':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[i['file'] for i in images]},ensure_ascii=False))

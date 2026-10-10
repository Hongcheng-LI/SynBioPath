import json,hashlib,re,fitz
import worker as w
d=w.ROOT/'sources'/'BZQCBN7N';rec=json.loads((d/'prepared.json').read_text(encoding='utf8'));doc=fitz.open(rec['main_pdf'])
specs=[('Figure 1',3,[43,61,553,514],[]),('Table 1',5,[43,60,553,697],[]),('Table 2',7,[43,60,553,664],[]),('Figure 2',9,[43,61,553,503],list('ABC')),('Figure 3',10,[43,61,553,514],list('AB'))]
images=[];figures=[]
for label,page,bbox,panels in specs:
 pg=doc[page-1];file=d/('BZQCBN7N-'+label.replace(' ','-')+'-complete.png');pg.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=fitz.Rect(bbox),alpha=False).save(str(file));caption=next(x['caption'] for x in rec['figure_candidates'] if x['label']==label)
 figures.append({'label':label,'caption':caption,'panels':panels,'pages':[{'page':page,'bbox':[bbox[0]/pg.rect.width,bbox[1]/pg.rect.height,bbox[2]/pg.rect.width,bbox[3]/pg.rect.height],'dpi':300}]})
 images.append({'label':label,'caption':caption,'page':page,'bbox':bbox,'panels':panels,'file':str(file),'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
draft={'identity_matches':True,'identity_reason':'Printed Review four authors FrontBioengBiotechnol9 article632269 DOI10.3389/fbioe.2021.632269 date05Feb2021 matches current live Zotero; all15pages read/viewed','paper_type':'review','source_article_type':'Review','title_zh':'紫杉醇工程瓶颈与转录组候选综述','filename_title':'紫杉醇工程瓶颈与转录组候选综述','journal_short':'Front Bioeng Biotechnol','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':['未逐篇独立复核所有引文原始数据与测序序列；本文为2021叙述性综述','Table2重复S713T及Y835F、R63H/R363H、D380R/D390R、Q609G/Y609G存在冲突，未静默修正','BDP50/60倍、Y688L2.4/2.5倍为本文内部差异；Glasscock2019在本文为预印本','跨宿主终点单位不同；总氧化taxanes不是完整紫杉醇滴度，未补造统计或统一折算'],'report':(d/'codex-report.md').read_text(encoding='utf8'),'figures':figures}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft});w.write_json(d/'codex-crops.json',images);print(json.dumps({'cjk':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[i['file'] for i in images]},ensure_ascii=False))

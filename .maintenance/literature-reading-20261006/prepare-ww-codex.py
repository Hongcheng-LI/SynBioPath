import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'WWVFPY84';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.535,.297,.922,.467],[]),('Unnumbered Structure Graphic',2,[.075,.074,.491,.808],list('123456789')),('Figure 1',3,[.075,.081,.922,.353],['A','B']),('Table 1',4,[.075,.078,.491,.726],[]),('Figure 2',5,[.075,.081,.922,.252],['A','B'])]
figs=[{'label':l,'caption':'原文图表：肽结构、构型比较、NMR与体外蛋白酶读数','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地无SI，NP-MRD未独立读取，本文首次不作当前检索保证','单次混合水华Microcystis优势群落非所有化合物生产者归属','2Ser与Htyr共同改变非单变量Ser比较','2结果m1005.700与方法1005.4700差异，采用方法并保留冲突','8结果1806.8310 vs方法computed1806.8310found1806.8333','Table1主文只ValNMePhePheAhpTyr，无完整ThrGlnBTA数据且无续表','Marfey水解Gln转Glu，原肽Gln靠结构组合','LFDVA分辨Thr构型，LFD AA分辨不足非证实','SI碎片可能归属非独立确认全部碎裂路径','1vs3同时Thr与Gln构型不同，不能唯一归因Thr','4vs996p.4679未检出差异非严格等效','蛋白酶误差种类完整nCI未报告不按图估数','6酰基2Sstar3Rstar仅相对不能升绝对，HMBC强度趋势不是精确异核J','8/9作者推测分离伪产物未验证原样和时间，8构型依类比','7/8分子式deltaCH4O不应写只甲基化，9另有Glu4Ser4与开环','DTrpferintoic编号原文4而实际5，不归给活性4','7–9多结构共变不可用曲线证明水解无影响','无该材料BGC或A/E/反式酶验证','无本研究人体生态毒性/环境浓度，分离回收不是暴露或滴度']
draft={'identity_matches':True,'identity_reason':'Formal8pageJNP88 1950–1957 titleauthorsDOImatch, notSI','paper_type':'research','title_zh':'蓝细菌肽的组成构型与注释证据','filename_title':'蓝细菌肽构型变化的结构注释与活性归因边界','journal_short':'J Nat Prod','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex originalPDFreading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    for index,page,box,name in [(0,0,fitz.Rect(329.3859,238.11,555.421,372.019),'Abstract'),(1,1,fitz.Rect(48.47,52.95,294.46,649.186),'Structures'),(2,2,fitz.Rect(38,55.46,567.89,285),'Figure1')]:
        out=d/('WWVFPY84-'+name+'-clean.png')
        doc[page].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
        sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
        images[index].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

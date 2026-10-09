import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'E4HTE8GN';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[315,237,556,373]),('Unnumbered Structure Graphic',1,[51,538,292,682]),('Table 1',2,[51,58,556,426]),('Figure 1',2,[51,429,556,645]),('Figure 2',3,[51,59,556,334]),('Figure 3',3,[51,342,556,511]),('Figure 4',3,[315,620,556,756]),('Figure 5',4,[51,59,556,265]),('Table 2',5,[51,58,292,507]),('Table 3',5,[315,58,556,499]),('Figure 6',5,[51,511,292,637]),('Table 4',6,[51,104,292,289])]
with fitz.open(rec['main_pdf']) as doc:
    figs=[{'label':l,'caption':'原文图表：HPPO杂萜结构、核磁及细胞活性证据','panels':[],'pages':[{'page':p,'bbox':[b[0]/doc[p-1].rect.width,b[1]/doc[p-1].rect.height,b[2]/doc[p-1].rect.width,b[3]/doc[p-1].rect.height],'dpi':300}]} for l,p,b in spec]
gaps=['本地无SI，CCDC与NP-MRD原始数据未独立读取，ECD未重算','菌株保持Penicillium sp.属级，ITS99%不能改成确定种名','甲基迁移为结构比较未直接验证生源反应','1Flack0.18(7)，3为0.03(5)，不混淆','2部分构型依赖推定共同生源，4/5依赖ECD类比，6S60未读取，7NOE相对差向关系','主文全部无明显H1975毒性与Table4中9IC5015uM不一致','25uM单点与IC50剂量参数分开，斜杠脚注未测试非无效','重复数误差类型精确统计和活性细节需SI','5数值21±1与吲哚美辛24±2不能称显著更强','RAW264.7CC50与H1975不同细胞指标不可替代','分离mg非发酵滴度，未提供基因/靶点/动物证据','3晶体C54H64O16不改写单分子组成C27H32O8','epoxy名称含氧桥不统一当三元环']
draft={'identity_matches':True,'identity_reason':'Formal8pageJNP87 1209–1216 titleauthorsDOImatch','paper_type':'research','title_zh':'海洋青霉HPPO杂萜的结构与细胞表型证据','filename_title':'HPPO杂萜的氧桥构型与NO抑制证据','journal_short':'J Nat Prod','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex mainPDFsource reading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    for i,(l,p,b) in enumerate(spec):
        box=fitz.Rect(b);out=d/('E4HTE8GN-'+l.replace(' ','-')+'-complete.png');doc[p-1].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
        sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
        images[i].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

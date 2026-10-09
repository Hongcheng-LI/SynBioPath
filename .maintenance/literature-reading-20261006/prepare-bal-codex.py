import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'BALTX27W';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.511,.337,.922,.501],[]),('Unnumbered Structure Graphic',1,[.54,.73,.90,.841],[]),('Table 1',2,[.075,.078,.922,.471],[]),('Figure 1',2,[.511,.484,.922,.619],[]),('Figure 2',3,[.075,.13,.491,.259],[]),('Table 2',3,[.075,.443,.491,.647],[]),('Figure 3',4,[.075,.082,.922,.367],['compound 1','compound 2'])]
figs=[{'label':l,'caption':'原文图表：结构确证、生成抑制与细胞信号证据','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地未提供SI、原始NMR和CIF，未重跑DP4+或晶体精修','Chalinidae为科级来源，Pestalotiopsis仅属级鉴定','OSMAC优选无完整正文定量比较矩阵','分离回收量不是发酵滴度，方法摇速原文120ppm单位待核','正文H7至C6相关未列于Table1对应行，需原始NMR核查','DP4+100percent仅限候选比较，不是绝对构型独立证明','CCDC2160284/2160285未独立读取','BMM48hMTT与5day分化时间不同，CC50及选择性指数为下界','Table2n3独立动物与技术重复未明确，完整曲线与精确统计未报告','compound3量不足未测试，并非无活性','Figure3RAW264.7而表型BMM，未闭合跨模型因果','p65图注pP65与条带和坐标p65标注不同，不据此写磷酸化','信号变化非直接结合或酶靶点证明，无动物疗效','结构生源关系为推测，无BGC、酶学、同位素','作者当时SciFinder相似性检索不是当前全库新颖性复核']
draft={'identity_matches':True,'identity_reason':'Formal6pageJNP87 160–165, titleauthorsDOImatch; attachment supplement flag incorrect','paper_type':'research','title_zh':'Pestanoid A的结构确证与破骨细胞生成抑制','filename_title':'PestanoidA的结构确证与破骨细胞生成抑制边界','journal_short':'J Nat Prod','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex originalPDFreading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    box=fitz.Rect(317.59,270.14,555.42,399.23)
    out=d/'BALTX27W-Graphical-Abstract-clean.png'
    doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
    sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
    images[0].update(file=str(target),sha256=sha,bbox=list(box))
    box=fitz.Rect(330,585,545,673)
    out=d/'BALTX27W-Structures-clean.png'
    doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
    sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
    images[1].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'76I5KWYI';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.511,.298,.922,.414],[]),('Figure 1',1,[.511,.469,.922,.851],list('abc')),('Figure 2',2,[.075,.082,.922,.456],list('abc')),('Scheme 1',3,[.511,.078,.922,.483],[]),('Table 1',3,[.511,.508,.922,.897],[])]
figs=[{'label':l,'caption':'原文图：cnn预测筛选、设计结构、化学合成或活性面板','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地无SI，未读原始合成物NMR/HRMS、详细方法与cnn预测表','synBNP为基因簇启发合成物，天然分离异源表达或KO身份未验证','192候选预测不是192实验验证，图示约200为概数','允许最多3个Acode有>3差异位点，非每个code至多3位点','正文Cnn27–29与图中蓝色27/29/30编号差异需SI和序列核查','A6/A9StachelhausLeuvsSANDPUMAOrn人工选择，未实测底物活化','60–85percent基因同源不是相同天然产物证明','Gly无DL不能因E结构域写Dgly','cinnamoylACP/CoA术语混用，载体转换未实测','化学结构和成环按目标合成，不能验证天然路线','表1MICugmL与细胞IC50uM不同，Bsub64和BAS8498并非全无抗菌','细胞4–21uM健康分类Vero4HEK6不显示肿瘤选择性','正文额外13微生物9细胞与表15微生物9细胞总计范围不完全对应','C6活性降低无完整IC50倍数和靶点，不能推全部类似物必需性','未报告全文独立重复置信区间统计','在线May20与ZoteroMay31区分']
draft={'identity_matches':True,'identity_reason':'Actual5pageformalOrgLett26 4433–4437 titleauthors DOI match, notSI','paper_type':'research','title_zh':'Cinnamosyn的预测设计合成与细胞毒性','filename_title':'Cinnamosyn的预测结构与合成活性证据','journal_short':'Org Lett','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex originalPDFreading with figure/tablevisualQA; no externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
 box=fitz.Rect(315.44,238.11,555.42,329.78)
 out=d/'76I5KWYI-Graphical-Abstract-clean.png'
 doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
 sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
 images[0].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

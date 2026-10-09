import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'3DVJBS6C';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.601,.336,.919,.507],[]),('Figure 1',1,[.511,.533,.922,.699],[]),('Table 1',2,[.075,.078,.491,.666],[]),('Figure 2',2,[.511,.082,.922,.409],[]),('Figure 3',2,[.511,.549,.922,.752],[]),('Figure 4',3,[.075,.082,.491,.350],[]),('Scheme 1',3,[.075,.802,.922,.940],[]),('Figure 5',3,[.511,.082,.922,.607],list('ABCDEF')),('Figure 6',4,[.075,.082,.491,.603],list('ABCDEF'))]
figs=[{'label':l,'caption':'原文图：杂合结构、波谱、生物合成假说或铁死亡相关测定','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['正文5页已读，SI缺失，未读完整培养分离/量子计算/生物方法与原始谱图','CCDC2226694仅正文确认，未下载精修，ECD未复算','NOE段落C7prime与表1甲基及最终C5prime手性列表不一致，标明疑似编号笔误未擅改','Scheme1为提出路径，无本菌株基因簇酶或同位素证据','15.4uM是A375RSL3细胞保护EC50非HMOX1酶IC50','多诱导剂多细胞系保护范围有限，不是所有铁死亡模型或体内药效','DPPH/铁相关阴性限定检测，不排除所有细胞环境作用','HMOX1表达下降与ZnPP保护是关联，不是直接唯一靶点证明','误差线n统计检验精确P及拟合CI正文不足，Figure6FP<.01照录','肿瘤细胞保护不是抗肿瘤杀伤，其他化合物背景细胞毒性不能转借','HOMX/RLS名称笔误结合图文识别，未建错误实体','在线日期June24与ZoteroJuly12区分']
draft={'identity_matches':True,'identity_reason':'Actual5pageformalOrgLett26 5695–5699 DOI titleauthors match, mainarticle notSI','paper_type':'research','title_zh':'Stephaochratidin A杂合结构与铁死亡抑制证据','filename_title':'StephaochratidinA的结构与铁死亡保护机制边界','journal_short':'Org Lett','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex localoriginalPDFreading and visuallycheckedmainfigures, no externalmodel'})
images=w.crops(rec,draft,d)
# Preserve the complete original graphical-abstract bitmap while excluding
# fragments of the adjoining abstract text captured by the generic margin.
with fitz.open(rec['main_pdf']) as doc:
 box=fitz.Rect(367.53997802734375,270.1399841308594,555.4199829101562,405.0099792480469)
 out=d/'3DVJBS6C-Graphical-Abstract-clean.png'
 doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
 sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
 images[0].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

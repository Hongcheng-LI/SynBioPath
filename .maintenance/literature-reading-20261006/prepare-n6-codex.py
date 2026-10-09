import json,re
import worker as w
d=w.ROOT/'sources'/'N6EIP5DM'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',2,[.085,.135,.68,.474],[]),('Figure 2',5,[.085,.135,.701,.759],[]),('Figure 3',6,[.085,.135,.701,.66],[]),('Figure 4',17,[.085,.451,.701,.916],list('ABC'))]
figs=[{'label':l,'caption':'原文图：紫杉醇生产路线、反应网络或工程方法','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
figs.append({'label':'Table 1','caption':'异源紫杉烷生产系统；四页完整续表，旋转至可读方向','panels':[],'pages':[{'page':p,'bbox':[0,0,1,1],'dpi':300,'rotation':90} for p in [8,9,10,11]]})
gaps=['叙述性综述，未提供系统检索纳入流程，未对99篇引用逐篇复核','仅Jiang2024Science在同批任务中直接核查，其他滴度保留综述转述层级','表1四页全部覆盖，但不同产物单位底物培养统计口径不可直接排名','酵母0.97ug/L紫杉醇是从baccatinIII开始的转化','烟草64.29ng/gFW终产物条目起始底物需原始MolPlant2023核查','表1Science2024约50ng/g没有注明干鲜重，原始论文核实为干重','总氧化紫杉烷不能等同单一5alphaol或紫杉醇','Synechocystis羟基化产品条目摘要未列出完整氧化酶构成','约2000倍化学生物增益对应产物和基线需原始研究核查','天然真菌生产争议不否定工程真菌taxadiene证据','ABCG2候选转运功能未验证，图4紫杉烷传感器与AI闭环是路线框架','不同体系AI案例如EPA27.5g/L不是紫杉醇滴度','无生命周期成本及同条件宿主比较，无法证明工业最优路线']
draft={'identity_matches':True,'identity_reason':'21page formalPDF title DOI authors and2026volumeissue match; 2025copyright and DOI distinguished','paper_type':'review','title_zh':'紫杉醇可持续生产的合成生物学路线图','filename_title':'紫杉醇生产路线的产物边界与工程证据','journal_short':'Trends in Biotechnology','category':None,'related_categories':[],'classification_reason':'全部文献笔记完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex local originalPDF fulltext, table and figure reading; no external model'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

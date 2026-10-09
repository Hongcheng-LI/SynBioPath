import json,re,hashlib,fitz
import worker as w
d=w.ROOT/'sources'/'V7XAHPMQ';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
p=w.Path(r'C:\Software\Data\02-Zotero\storage\6L9NBJ3Z\s41586-025-09697-2.pdf')
rec.update(main_pdf=str(p),main_attachment_key='6L9NBJ3Z',main_pdf_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pdf_pages=17)
w.write_json(d/'codex-prepared.json',rec)
spec=[('Figure 1',2,[.05,.045,.95,.453],[]),('Figure 2',3,[.05,.045,.95,.88],['a','b']),('Figure 3',4,[.05,.045,.95,.61],list('abcde')),('Figure 4',6,[.05,.045,.95,.58],list('abcd')),('Figure 5',7,[.05,.045,.95,.88],list('abcdef')),('Extended Data Figure 1',13,[.05,.04,.95,.75],['a','b']),('Extended Data Figure 2',14,[.05,.04,.95,.75],['a','b'])]
figs=[{'label':l,'caption':'正式版本原文：模型、数据、验证或候选检索','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['正式17页版本替代33页提前预览作为阅读截图来源，原附件保留','第二附件是同篇正式论文而非独立SI，完整Supplementary及原始色谱矩阵缺失','未下载训练数据代码和权重，未复现模型，链接仅由正文确认','正例部分随机EC物种匹配序列；负例由替换生成，未当作全部实测标签','三维复合物主要由预测和对接生成而非实验实测','ESP最终模型未同数据重训，整体差异不能全归因架构','双未知是作者对象划分，序列骨架聚类隔离未独立核查','91.7percent为12新底物Top1，不是624组合整体准确率','Topk图非单调，具体分母成功定义需SI核查','Reporting Summary研究设计replication等no，统计勾选不代替每组实际误差','PltM和ThHal同Q4KCZ3编号、表达段落漏一酶需序列核对','20Angstrom cube及radius、缺活性位点筛除及中心对接描述不一致，未擅定代码实现','ESM2具体版本权重待源码核查','没有可靠化学区域立体选择性预测，BGC案例为已知路径检索非新通路实证']
report=re.sub(r'\{\{FIGURE:([^}]+)\}\}',r'<!--FIGURE:\1-->',(d/'codex-report.md').read_text(encoding='utf-8'))
draft={'identity_matches':True,'identity_reason':'Both versions same DOI; formal17pagePDF titleauthors DOI match; inspected original main figures extended data and reporting summary','paper_type':'research','title_zh':'交叉注意力图神经网络预测酶底物特异性','filename_title':'EZSpecificity酶底物预测的数据标签与验证边界','journal_short':'Nature','category':None,'related_categories':[],'classification_reason':'全库笔记完成后归类','source_gaps':gaps,'figures':figs,'report':report}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex original preview plus formalPDF reading, no external model'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

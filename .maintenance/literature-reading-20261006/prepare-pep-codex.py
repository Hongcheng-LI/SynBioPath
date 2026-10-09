import json,re
import worker as w
d=w.ROOT/'sources'/'PEP725R8'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Scheme 1',2,[.06,.065,.93,.438],'Gö40/10 的多家族代谢物与异构体'),('Scheme 2',2,[.06,.443,.495,.667],'S1013 的四个产物及三种生源池'),('Figure 1',3,[.06,.065,.50,.246],'影响次级代谢的 DNA、RNA、蛋白与产物层级框架'),('Scheme 3',4,[.06,.064,.93,.416],'A. ochraceus DSM7428 的聚酮及含氮代谢家族'),('Scheme 4',5,[.06,.07,.495,.604],'F-24′707 的螺双萘、双萘与 mutolide 成员'),('Scheme 5',5,[.51,.07,.925,.573],'Gö40/14 的培养依赖结构谱'),('Scheme 6',6,[.06,.067,.93,.487],'Tü64 的 manumycin 侧链与装配差异'),('Scheme 7',7,[.06,.068,.495,.55],'A1 的 pH 相关结构家族概括'),('Scheme 8',7,[.51,.085,.93,.469],'Tü3634 的前体兼容与非预期诱导产物')]
figs=[{'label':l,'caption':c,'panels':[],'pages':[{'page':p,'bbox':b}]} for l,p,b,c in spec]
draft={'identity_matches':True,'identity_reason':'Original title authors journal MINIREVIEWS label and2002 3 619–627 match Zotero metadata; long-form DOI taken from Zotero not printed inPDF','paper_type':'review','title_zh':'OSMAC 框架与环境依赖的天然产物化学多样性','filename_title':'OSMAC 框架的案例证据与机制边界','journal_short':'ChemBioChem','category':None,'related_categories':[],'classification_reason':'待全部笔记完成后统一分类','source_gaps':['综述所引原始研究、学位论文和未发表结果未逐篇独立核查','案例产量缺少统一实验设计、归一化和原始统计数据','多种生源与调控解释在本文仍属假说','正文 DOI 未印出，长格式 DOI 来自 Zotero 元数据'],'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex reads all9 original pages and manually checks8schemes andfigure against page images; no paid model used'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[{'label':i['label'],'file':i['file']} for i in images]},ensure_ascii=False))

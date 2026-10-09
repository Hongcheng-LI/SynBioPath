import json,re,fitz
import worker as w
d=w.ROOT/'sources'/'XDR3W689';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',3,[.13,.213,.95,.884],['A','B']),('Figure 2',4,[.06,.267,.95,.43],[]),('Figure 3',6,[.26,.08,.95,.22],['1','2']),('Figure 4',7,[.13,.22,.95,.55],[]),('Table 1',5,[.04,.08,.95,.91],[]),('Table 2',8,[.26,.08,.95,.26],[])]
figs=[{'label':l,'caption':'原文七肽结构、基因簇、谱学数据或活性结果','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地无SI，Marfey、完整NMR、MSMS及相关菌株材料未独立重核','nblBS缺少敲除互补、异源合成或酶学因果验证','整体水解不能独立确认两Phe的位置构型，作者归属待位置证据核实','第三模块无E的D-Phe来源及Thr脱水酶尚未实证','Figure4图注3与部分正文指向1不一致','正文碳类型总计41与分子总碳42不符，芳香碳分类及部分位移与Table1冲突','Table1化合物2 Ala alpha-C40.0异常，未代改','NH9.52到9.32实际高场，正文方向表述冲突','MIC3.25与方法3.125及摘要6.5与主表6.25冲突','菌株列表漏A.baumannii，K.pneumoniae前筛编号与Table2不同','缺少独立重复误差及匹配溶剂对照说明，未补造显著性','未独立确认所有菌株MDR表型，无MBC靶点毒性体内药效数据','GenBank登录号仅核对正文，未下载序列验证']
draft={'identity_matches':True,'identity_reason':'Original12pagePDF title authors DOI10.3390/molecules31030547 match Zotero','paper_type':'research','title_zh':'基因组驱动发现冷泉来源Bacillus抗菌七肽','filename_title':'冷泉芽孢杆菌七肽的构型差异与活性证据','journal_short':'Molecules','category':None,'related_categories':[],'classification_reason':'全库笔记完成后统一归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
draft['report']=re.sub(r'\{\{FIGURE:([^}]+)\}\}',r'<!--FIGURE:\1-->',draft['report'])
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex original PDF reading without external model'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

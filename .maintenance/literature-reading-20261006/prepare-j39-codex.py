import json,re
import worker as w
d=w.ROOT/'sources'/'J39PT6YP'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',2,[.27,.35,.95,.806],'三十二种聚酮结构与异构体'),('Table 1',3,[.27,.29,.95,.622],'1、3、5 的核磁位移与耦合'),('Figure 2',4,[.27,.385,.95,.705],'COSY 与关键 HMBC 连接'),('Figure 3',4,[.27,.725,.95,.9],'2、11、13、14 的单晶结构'),('Figure 4',5,[.27,.098,.95,.612],'实验与计算 ECD 对比'),('Figure 5',5,[.27,.625,.95,.844],'NOESY 空间关系'),('Table 2',6,[.27,.10,.95,.35],'11 的核磁数据'),('Table 3',6,[.045,.613,.95,.879],'13–15 的核磁比较'),('Figure 6',7,[.27,.387,.95,.56],'15 的两种 DP4+ 候选'),('Table 4',8,[.27,.149,.95,.438],'25/26 的核磁数据'),('Figure 7',8,[.27,.697,.95,.866],'MTPA 酯的局部位移差'),('Table 5',9,[.27,.25,.95,.65],'27–29 的核磁数据与缺失信号脚注'),('Figure 8',10,[.27,.159,.84,.5],'29 的 NOESY、ECD 与 DP4+ 候选'),('Figure 9',11,[.045,.098,.95,.537],'作者提出的1–24可能生源网络'),('Table 6',12,[.045,.172,.95,.427],'逐菌种 MIC、阳性对照与符号定义')]
figs=[{'label':l,'caption':c,'panels':(['A','B','C','D','E','F'] if l=='Figure 4' else ['A','B','C'] if l=='Figure 8' else []),'pages':[{'page':p,'bbox':b,'dpi':240}]} for l,p,b,c in spec]
draft={'identity_matches':True,'identity_reason':'OriginalPDF title authors journal2024 and DOI10.3390/md22050204 match Zotero','paper_type':'research','title_zh':'冷泉来源 Talaromyces CS-258 的聚酮结构与抗菌谱','filename_title':'冷泉真菌聚酮的立体鉴定与抗菌证据','journal_short':'Mar Drugs','category':None,'related_categories':[],'classification_reason':'待全部笔记完成后统一分类','source_gaps':['本地未提供SI，全部原始谱图、手性分离和计算输出未独立复核','3的芳香氢与离子标签、11立体中心标号、25/26甲基号存在主文内部冲突','27命名羟基及中性式/离子式不一致，29命名有两种写法','Figure6候选15b构型标签异常，保留原图','主文抗菌对照概括不完全符合Table6逐菌种值','生源网络和抗菌靶点未获本篇直接功能验证','三次测量独立性未说明，MIC不确定性未报告'],'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex source-grounded reading, no external-model call'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[{'label':i['label'],'file':i['file']} for i in images]},ensure_ascii=False))

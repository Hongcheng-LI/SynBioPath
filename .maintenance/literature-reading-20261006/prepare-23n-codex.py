import json,re
import worker as w
d=w.ROOT/'sources'/'23NGHBLY'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[(1,3,[.075,.06,.935,.966],['A','B','C','D','E']),(2,4,[.06,.065,.94,.955],['A','B','C','D']),(3,6,[.07,.06,.945,.80],[]),(4,7,[.07,.06,.94,.72],['A','B','C']),(5,8,[.07,.06,.94,.974],['A','B']),(6,9,[.075,.215,.945,.947],['A','B','C'])]
caps=['CSMD 的采样、构建、质量、映射覆盖与基因稀释曲线','contig 分类与 OTU 的冷泉类型共享','物种代表的系统发育与预测代谢模块','候选 BGC 类别、数据库匹配与 GCF 稀释曲线','古菌及细菌 BGC 负担的系统发育分布','门、冷泉类型及样本间 GCF 共享']
figs=[{'label':f'Figure {n}','caption':caps[n-1],'panels':panels,'pages':[{'page':p,'bbox':b,'dpi':300}]} for n,p,b,panels in spec]
gaps=['本地未提供 Supporting Information，补图表的精确数值及个体记录未核查','未下载原始 reads、MAG、簇记录或重跑算法，仓库可用性未在线验证','预测功能与 BGC 不等同于代谢表型、产物结构或生物活性实验证实','Figure3的370+1527为1897，与1895标题不一致，门计数及百分比也有冲突','正文407属与960潜在新属口径不清，有氧候选跨44/55门不一致','非冗余contig正文56Gb与数据可用性54Gb不一致','Figure1的65%fromthisstudy与讨论65%increase定义不可混用','Figure6C图注Log10-normalized与色标z-score不一致','相同样本映射比较采用Welch而非配对检验，未重算；跨地点类型比较存在混杂','新颖性依赖历史数据库和阈值；组合判定逻辑、组样本数、误差定义及多重比较仍需补表脚本']
draft={'identity_matches':True,'identity_reason':'Original15physicalpages titleauthors DOI10.1093/gpbjnl/qzad006 matchZotero','paper_type':'research','title_zh':'全球海洋冷泉宏基因组的分类、功能及天然产物多样性','filename_title':'全球冷泉宏基因组的资源构建与生物合成预测','journal_short':'GPB','category':None,'related_categories':[],'classification_reason':'全部笔记完成后统一归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex source maintext methods andfigure reading; no external-model call'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images)},ensure_ascii=False))

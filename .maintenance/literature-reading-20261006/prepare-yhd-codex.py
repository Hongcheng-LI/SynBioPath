import json,re
import worker as w
d=w.ROOT/'sources'/'YHD6KJUF';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',2,[.075,.075,.93,.603],['A','B','C']),('Figure 2',3,[.075,.076,.93,.421],[]),('Figure 3',3,[.075,.443,.93,.951],['A','B']),('Figure 4',4,[.075,.075,.487,.48],['A','B','C']),('Figure 5',5,[.075,.075,.93,.944],['A','B','C']),('Figure 6',6,[.075,.579,.487,.951],['A','B']),('Figure 7',7,[.075,.075,.93,.94],['A','B']),('Figure 8',8,[.075,.075,.93,.753],['A','B']),('Graphical Abstract',1,[.548,.275,.918,.446],[])]
figs=[{'label':label,'caption':{'Graphical Abstract':'首页图形摘要：天然 GGPP 与几何探针的不同催化终点'}.get(label,'原文底物、产物或机制图'),'panels':panels,'pages':[{'page':p,'bbox':b,'dpi':300}]} for label,p,b,panels in spec]
gaps=['本地无 SI：反应条件、色谱、完整 NMR、氘谱图及 DFT 坐标未独立重核','PDF 含XXXX卷页和A–J页码，为提前发表版本；未补造正式卷页','18测试14成功，不存在统一成功阈值、精确酶动力学及产物比例可核数据','多数绝对构型依赖生物合成类比，GC/MS不能确定相同对映体','48为被氘标记排除的候选结构，不是第15个分离新产物','正文最高8.2kcal/mol与Figure5的8.6黑框不一致','PmS产物归属在正文和Figure7紫色符号间有冲突','Figure7蓝框x占位及45.2符号待SI核查；不补造数字或负号','Figure7/8 O8相对能量参照不同，未合并成统一曲线','氘标记限制部分迁移，未直接捕获全部碳正离子；DFT不等于完整酶内实测路径']
draft={'identity_matches':True,'identity_reason':'Original10pagePDF titleauthors DOI10.1021/acscatal.6c01805 matchZotero; maintext despite automated supplementflag','paper_type':'research','title_zh':'双键几何构型控制二萜合酶催化','filename_title':'双键几何探针对二萜催化路径的约束','journal_short':'ACS Catal','category':None,'related_categories':[],'classification_reason':'全部笔记完成后统一归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex originalPDF reading no external-model call'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images)},ensure_ascii=False))

import json,re
from pathlib import Path
import worker as w
d=w.ROOT/'sources'/'PMQWGNMV'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
figs=[
 {'label':'Chart 1','caption':'商业大黄提取分配和九个分离物的完整流程；横向原图转正','panels':[],'pages':[{'page':2,'bbox':[.10,.11,.89,.95],'rotation':90}]},
 {'label':'Table I','caption':'I、III、IV、V、VI 的碳核磁数据及可互换归属脚注','panels':[],'pages':[{'page':3,'bbox':[.18,.55,.83,.947]}]},
 {'label':'Figure 1','caption':'modified Horeau 衍生物气相色谱；A、B 为峰标识','panels':[],'pages':[{'page':4,'bbox':[.19,.105,.84,.486]}]},
 {'label':'Figure 2','caption':'I–VI 的六个结构；原图左下对应 IV 的结构误印为 VI','panels':[],'pages':[{'page':5,'bbox':[.19,.102,.81,.389]}]},
 {'label':'Chart 2','caption':'作者提出的大黄酚性成分可能多酮生源模型','panels':[],'pages':[{'page':6,'bbox':[.14,.102,.85,.744]}]},
]
draft={'identity_matches':True,'identity_reason':'Scanned original title authors and CPB 32(9)3493–3500 match Zotero DOI10.1248/cpb.32.3493','paper_type':'research','title_zh':'大黄色原酮和色满酮衍生物的分离与结构鉴定','filename_title':'大黄色原酮与色满酮的结构证据和生源假说','journal_short':'Chem Pharm Bull','category':None,'related_categories':[],'classification_reason':'待全部笔记完成后统一分类','source_gaps':['商业药材缺少明确植物学鉴定和凭证标本','部分碳谱归属可互换，未提供完整原始波谱与衍生物积分数据','Figure 2 左下 IV 的原图编号误印为 VI','主文未报告独立确定糖 D/L 的手性分析','生源图是结构推断模型，未经示踪或酶学验证'],'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex directly reads all8 original scanned pages and crosschecks OCR against original images; no external paid-model call'})
images=w.crops(rec,draft,d)
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

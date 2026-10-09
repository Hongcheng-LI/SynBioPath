import json,re,fitz
import worker as w
d=w.ROOT/'sources'/'CTJPEHPH'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
ranges=['1–19','20–29','30–54','55–92','93–118','119–130','131–136','137–146','147–160','161–171','172–200','201–242','243–267','268–293','294–319','320–341','342–364','365–388','389–413','414–430','431–453','454–480','481–501']
figs=[];groups=[]
with fitz.open(rec['main_pdf']) as doc:
 for n,p in enumerate(doc):
  boxes=[fitz.Rect(i['bbox']) for i in p.get_image_info() if fitz.Rect(i['bbox']).get_area()>3000]
  boxes.sort(key=lambda b:(round(b.x0/100),b.y0))
  merged=[]
  for box in boxes:
   if merged and abs(merged[-1].x0-box.x0)<1 and abs(merged[-1].x1-box.x1)<1 and 0<=box.y0-merged[-1].y1<=2:
    merged[-1]|=box
   else:merged.append(box)
  for box in merged:groups.append((n+1,[box.x0/p.rect.width,box.y0/p.rect.height,box.x1/p.rect.width,box.y1/p.rect.height]))
assert len(groups)==len(ranges)==23
for k,((p,b),c) in enumerate(zip(groups,ranges),1):
 figs.append({'label':f'Unnumbered Structure Graphic {k}','caption':f'未编号结构图版 {k}：原文 PDF 第 {p} 页，化合物 {c}；定位编号由本笔记设置，非原刊图号','panels':[],'pages':[{'page':p,'bbox':b,'dpi':300}]})
draft={'identity_matches':True,'identity_reason':'Title authors DOI10.3389/fmicb.2019.00294 andREVIEW2019 match originalPDF','paper_type':'review','title_zh':'OSMAC 策略探索微生物结构多样性的案例综述','filename_title':'OSMAC 结构多样性综述的案例地图与证据边界','journal_short':'Front Microbiol','category':None,'related_categories':[],'classification_reason':'待全部笔记完成后统一分类','source_gaps':['综述引用的原始论文未全面逐篇复核，活性与产量为二手转述','原文存在编号、数量、单位和菌名的局部冲突，相关例子待原始来源核对','共培养生产者及沉默基因簇激活在多例中未被直接验证','原文关于 nicotinamide 抑制剂类型和组蛋白乙酰化静电方向的表述经补充来源纠错','结构图版无原刊图号，笔记采用页码与化合物范围建立23个定位标识'],'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex reads original main text pages1–14 and checks structure plates pages2–13, selected reference entries and primary source clarifications; no external paid-modelcall'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[{'label':i['label'],'page':i['page'],'file':i['file']} for i in images]},ensure_ascii=False))

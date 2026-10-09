import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'Z6YUHKGS';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',2,[.04,.05,.95,.955],list('ABCDE')),('Figure 2',3,[.04,.05,.95,.458],list('ABC')),('Figure 3',4,[.04,.05,.95,.465],[]),('Figure 4',5,[.04,.05,.95,.70],list('ABC')),('Figure 5',6,[.04,.05,.95,.867],list('ABCDEFGH'))]
figs=[{'label':l,'caption':'原文：候选功能筛选、机制模型与baccatin III重构','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['无完整SI S1–S16 TablesS1/S2 DataS1，NMR原谱动力学拟合计算坐标未重核','Km14.14±3.15微摩尔，底物50微摩尔及环氧4.5微摩尔，MeJA100微摩尔与标尺5微米按原PDF图像确认，文本单位抽取错误已纠正','未检出游离环氧3转2，不能穷尽全部短寿命酶内中间体','DFT为酶自由截短铁卟啉模型而非完整蛋白QM/MM或实测中间体','Figure5A为异源组合逐一省去，不是九个原生基因敲除','九基因组合产物检出不唯一确定C1/C10酶功能与顺序或全部宿主贡献','RNAi方向来自正文，SI具体效果特异性未核查','组织共表达及ER定位不等于物理复合物或底物通道化证明','Figure5D n3 SE双侧t，精确P置信区间多重校正未逐项报告','CK归一化及处理对照细节待SI核查','产量约50ng/g干重低水平，不等于mg/L工业滴度或紫杉醇全合成','2024研究状态不当作2026全领域更新；参考论文未全部逐篇阅读']
report=re.sub(r'\{\{FIGURE:([^}]+)\}\}',r'<!--FIGURE:\1-->',(d/'codex-report.md').read_text(encoding='utf-8'))
draft={'identity_matches':True,'identity_reason':'Original8pagePDF title authors Science383622–629 DOI match Zotero','paper_type':'research','title_zh':'红豆杉酶鉴定与baccatin III异源重构','filename_title':'baccatinIII重构的酶功能与网络证据','journal_short':'Science','category':None,'related_categories':[],'classification_reason':'全库笔记完成后归类','source_gaps':gaps,'figures':figs,'report':report}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex original8pagePDF read and originalunits verified, no external model'})
# This publisher embeds tall monochrome column rules as image objects.
# Crop directly to reviewed bounds rather than unioning those page dividers.
images=[]
with fitz.open(rec['main_pdf']) as doc:
 for graphic in figs:
  part=graphic['pages'][0];p=doc[part['page']-1];b=part['bbox']
  box=fitz.Rect((b[0]-.008)*p.rect.width,(b[1]-.008)*p.rect.height,(b[2]+.008)*p.rect.width,(b[3]+.008)*p.rect.height)
  for info in p.get_image_info():
   r=fitz.Rect(info['bbox'])
   if info.get('bpc',8)>1 and r.intersects(box) and 3000<r.get_area()<.9*p.rect.get_area():box|=r
  for block in p.get_text('blocks'):
   if w.caption_graphic(block[4].strip())==graphic['label']:box|=fitz.Rect(block[:4])
  box=(box+(-3,-3,3,3))&p.rect
  pix=p.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False);raw=pix.tobytes('png');digest=hashlib.sha256(raw).hexdigest()
  out=d/(rec['key']+'-'+graphic['label'].replace(' ','-')+f'-p{part["page"]}-1-'+digest[:16]+'.png');out.write_bytes(raw)
  images.append({'label':graphic['label'],'caption':graphic['caption'],'page':part['page'],'file':str(out),'bbox':list(box),'panels':graphic['panels'],'sha256':digest})
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

import json,re
import worker as w
d=w.ROOT/'sources'/'FCM54K4J'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'repaired-draft.json').read_text(encoding='utf-8'))['draft']
draft.update(report=(d/'codex-report.md').read_text(encoding='utf-8'),filename_title='含卤细胞松弛素的 OSMAC 发现与结构证据',classification_reason='待全部笔记完成后统一分类',category=None,related_categories=[])
draft['source_gaps']=['实际 SI 未提供，S85–S87 与完整原始波谱未独立复核','主文 Table 4 的 12/14 的 C12 氢信号与正文及碳谱冲突','部分图表引用及 HMBC 描述有笔误','原文部分同分子式的精确质量计算值不一致，未静默修正','具体卤化酶及沉默基因簇激活未经直接验证','细胞系身份认证与完整剂量反应原始数据未在主文提供']
locations={'Chart 1':(2,[.08,.075,.925,.438]),'Table 1':(2,[.08,.443,.925,.86]),'Table 2':(3,[.08,.075,.925,.50]),'Figure 1':(3,[.08,.50,.925,.86]),'Figure 2':(4,[.08,.073,.925,.423]),'Figure 3':(4,[.08,.434,.485,.682]),'Figure 4':(5,[.08,.123,.485,.4]),'Figure 5':(5,[.08,.525,.485,.79]),'Table 3':(6,[.08,.074,.925,.504]),'Table 4':(6,[.08,.504,.925,.91]),'Table 5':(7,[.08,.073,.925,.504]),'Figure 6':(7,[.08,.505,.485,.755]),'Figure 7':(7,[.515,.505,.925,.78]),'Figure 8':(8,[.08,.073,.485,.35]),'Table 6':(8,[.08,.612,.925,.945])}
locations['Table 5']=(7,[.08,.073,.925,.496])
for g in draft['figures']:
 p,b=locations[g['label']];g['pages']=[{'page':p,'bbox':b}]
draft['figures'].insert(0,{'label':'Graphical Abstract','caption':'首页图文摘要：培养外观、代谢谱与含卤成员；峰高并非绝对产率','panels':[],'pages':[{'page':1,'bbox':[.518,.316,.921,.489]}]})
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex directly read all10 original pages and replaced cached report after source checking; no external-model call'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':[{'label':i['label'],'file':i['file']} for i in images]},ensure_ascii=False))

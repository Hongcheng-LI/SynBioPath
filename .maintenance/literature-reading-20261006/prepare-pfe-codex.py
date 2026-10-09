import json,re
import worker as w
d=w.ROOT/'sources'/'PFEFMY85';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[(1,2,[.12,.48,.91,.863]),(2,3,[.27,.319,.95,.511]),(3,4,[.11,.098,.95,.484]),(4,5,[.12,.102,.95,.458]),(5,6,[.18,.145,.87,.884]),(6,7,[.10,.272,.91,.472]),(7,7,[.27,.666,.80,.9]),(8,8,[.12,.366,.95,.779]),(9,9,[.14,.226,.92,.921]),(10,11,[.27,.104,.95,.305]),(11,11,[.055,.456,.95,.657]),(12,12,[.12,.154,.95,.594]),(13,13,[.07,.109,.95,.571]),(14,14,[.11,.10,.95,.638]),(15,15,[.09,.185,.95,.507]),(16,16,[.09,.102,.95,.415]),(17,16,[.11,.59,.95,.918]),(18,17,[.27,.232,.85,.407]),(19,17,[.12,.664,.87,.929]),(20,18,[.16,.294,.90,.697]),(21,19,[.13,.294,.90,.606]),(22,19,[.27,.628,.93,.918]),(23,20,[.27,.24,.95,.5])]
ranges=['1–18','19–21','22–32','33–41','42–55','56–60','61–62','63–71','72–79','84–86','87–89','90–104','105–122','123–136','137–144','145–153','154–164','165–166','167–172','174–182']
figs=[{'label':f'Figure {n}','caption':('原文结构图：'+ranges[n-1] if n<=20 else {21:'冷泉资料的来源报道构成',22:'热液资料的来源报道构成',23:'冷泉与热液资料的活性报道计数'}[n]),'panels':[],'pages':[{'page':p,'bbox':b,'dpi':240}]} for n,p,b in spec]
draft={'identity_matches':True,'identity_reason':'Original26pagePDF title authors REVIEW andDOI10.3390/md20060404 matchZotero','paper_type':'review','title_zh':'冷泉与热液喷口的深海天然产物','filename_title':'冷泉与热液天然产物的来源地图和证据边界','journal_short':'Mar Drugs','category':None,'related_categories':[],'classification_reason':'待全部笔记完成后统一分类','source_gaps':['引用原始研究未全面逐篇重读，来源与活性经常来自不同论文','未提供完整检索筛选流程和逐项统计清单，比例不可解释为生态丰度或发现效率','图文编号冲突含89糖苷、134–136图号、132/142名称','采样海域与坐标冲突，Vibrio/Bacillus误称fungus，古菌置于细菌章节','25mg/mL、0.13±0.4μg/mL及mM等异常单位需原始文献核查','180名称与膜脂结构对应待原始来源核查','132相关引用为in silico，本文未提供直接结合或抗病毒实验','80–83和173在原文仅文字描述，没有补造结构截图'],'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft)
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex reads source maintext originalfigurepages andselectedreferences, no external-model call'})
images=w.crops(rec,draft,d);w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images)},ensure_ascii=False))


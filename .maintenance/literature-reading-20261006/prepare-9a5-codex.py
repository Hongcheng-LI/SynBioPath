import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'9A5TMMLF';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));doc=fitz.open(rec['main_pdf'])
spec=[('Figure 1',2,[49,70,553,392])]
gaps=['Spotlight commentary two pages no new Methods Results or quantitative yields cited primary papers not independently read','18 genes author summary not all host absolute minimum low yield prevents full single module reconstruction','C4beta C20 epoxidase versus CYP725A4 sequential epoxidation alternative interpretations natural order unresolved','T2prime alpha OH extraction T20aOH not skeletal C20 hydroxylation preserve original figure','Microorganism seems inactive unspecified host n expression detection limits not absolute absence','Metabolon and substrate channeling future directions not direct demonstrated complexes','Sustainability future claim no LCA TEA industrial data human review false classification deferred']
figs=[{'label':l,'caption':('原文 Movie 1 静态海报及图注（内部索引 Chart 1，视频未读取）' if l=='Chart 1' else '原文 '+l+'：完整图表及图注'),'panels':[],'pages':[{'page':p,'bbox':[b[0]/doc[p-1].rect.width,b[1]/doc[p-1].rect.height,b[2]/doc[p-1].rect.width,b[3]/doc[p-1].rect.height],'dpi':300}]} for l,p,b in spec]
draft={'identity_matches':True,'identity_reason':'2pages4authorsMolPlant17:370371DOI liveZotero verified Spotlight','paper_type':'review','source_article_type':'Spotlight','title_zh':'紫杉醇路线新阶段短评中的最小集合与重构边界','filename_title':'紫杉醇路线新阶段短评中的最小集合与重构边界','journal_short':'Mol Plant','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodexsourcegrounded2pages'})
images=[]
for fig,(l,p,b) in zip(figs,spec):
 out=d/('9A5TMMLF-'+l.replace(' ','-')+'-p'+str(p)+'-complete.png');doc[p-1].get_pixmap(dpi=300,clip=fitz.Rect(b),alpha=False).save(out);sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target);images.append({'label':l,'caption':fig['caption'],'page':p,'file':str(target),'bbox':b,'panels':[],'sha256':sha})
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'CJK':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images),'files':[x['file'] for x in images]},ensure_ascii=False))

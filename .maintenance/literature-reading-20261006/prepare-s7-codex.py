import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'S7AVSQZL';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));doc=fitz.open(rec['main_pdf'])
spec=[('Figure 1',2,[39,112,562,695])]
gaps=['NewsViews3pages commentary no new experiments original Liang2025 DOI800z unread this DOI801y distinct','Visible PDF3 published30April2025 textlayer placeholder xx xx xxxx stale use visible page','Externally fed baccatinIII beta phenylalanine yeast conversion not full de novo single strain','Morethan60percent baccatinIII to third intermediate in tobacco not final Taxol yeast yield','280fold T3NBT versus DBTNBT efficiency metric unspecified not overall yield n P CI unreported','Over40P45025BAHD candidate counts not biological n negative host results limited','Metabolicgrid lowtiter could be explanation not determined direct flux fourenzyme benzoylCoA module distinct sidechainCoA','minute amount no quantitative titer no LCA TEA future consortium not actual Taxolconsortium human review false classification deferred']
figs=[{'label':l,'caption':('原文 Movie 1 静态海报及图注（内部索引 Chart 1，视频未读取）' if l=='Chart 1' else '原文 '+l+'：完整图表及图注'),'panels':[],'pages':[{'page':p,'bbox':[b[0]/doc[p-1].rect.width,b[1]/doc[p-1].rect.height,b[2]/doc[p-1].rect.width,b[3]/doc[p-1].rect.height],'dpi':300}]} for l,p,b in spec]
draft={'identity_matches':True,'identity_reason':'3pages2authorsNatureSynthesisDOI liveZotero verified NewsViews','paper_type':'review','source_article_type':'News & Views','title_zh':'紫杉醇末端生物转化评论的代谢网格与供料边界','filename_title':'紫杉醇末端生物转化评论的代谢网格与供料边界','journal_short':'Nat Synth','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodexsourcegrounded3pages'})
images=[]
for fig,(l,p,b) in zip(figs,spec):
 out=d/('S7AVSQZL-'+l.replace(' ','-')+'-p'+str(p)+'-complete.png');doc[p-1].get_pixmap(dpi=300,clip=fitz.Rect(b),alpha=False).save(out);sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target);images.append({'label':l,'caption':fig['caption'],'page':p,'file':str(target),'bbox':b,'panels':[],'sha256':sha})
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'CJK':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images),'files':[x['file'] for x in images]},ensure_ascii=False))

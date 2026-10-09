import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'MQZQ29BH';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));doc=fitz.open(rec['main_pdf'])
spec=[('Figure 1',4,[40,65,545,382]),('Table 1',5,[40,68,545,310]),('Figure 2',9,[40,65,545,570]),('Figure 3',10,[40,54,375,728]),('Figure 3',11,[40,69,375,136]),('Figure 4',12,[40,409,545,740]),('Figure 5',13,[40,67,545,489]),('Table 2',14,[40,68,545,190]),('Figure 6',15,[40,67,545,374]),('Table 3',16,[40,530,545,746]),('Figure 7',18,[40,410,545,741]),('Table 4',19,[40,552,377,689])]
gaps=['Narrative review23mainpages read and originalpages viewed; references metadata read not115primarypapers independentlyverified; noSIprovided','Seven numberedFigures three numberedscientificTables; Figure3captioncontinuesp11; Table4internalcropindex fororiginalunnumberedFundingadministrativetable explicitlydisclosednotinventedscientificresult','Published31March2026 issueJune2026 Zotero20260611 retained','AuthorpatentCuratixCOIdisclosed; clinical/regulatorydatesasreviewreportednotlivestatusverified','Scecore5CoAsynthesissteps acetylCoAACSdownstreamextension PCAumbrella notexclusiveallacetylCoAroute; compartmentpoolnotwholecelltotal','Scesalvageanddenovo notuniversalallfungi; genomecopynumbernotessentiality experiment','Figure4ATP/MgcoordinatesborrowedhumanPANK3notfungalATPcomplex; PDB6UJ56B3V; Tyr221bodyvsTyr197Figure4DTable2unresolved; RMSD1.40unitnotexplicitcaption','Sequence36identity53similarity localstructureandglobalconservationnotprovenselectivity; humanmultipleisoformsnotexemptiontoxicity','Table3PTZKi50/160/217/106nMAfPanK notCandidaMIC; keyfeaturesIC50wordingnotinterchangeable; alphaPanAm100nMPfvs17.6ugmlSceendpointsnotcompared','MNS1.953.9uMMIC50sourceonly animalnrawdataCIPvaluesnotreportedhere hostNLRP3effects notclinicaltherapeuticproof','Figure7proposedmodel varyingcausalstrength speciescontextsdistinct no suppliedFICImatrixorclinicaldose/outcomeproof','Oldstrainbackgroundconfoundingretained withoutactionablepathogenresistanceengineering; noteseducationalmechanisms nooperationalpathogenoptimization']
figs=[]
for label in dict.fromkeys(l for l,p,b in spec):
 pages=[]
 for l,p,b in spec:
  if l==label:
   r=doc[p-1].rect;pages.append({'page':p,'bbox':[b[0]/r.width,b[1]/r.height,b[2]/r.width,b[3]/r.height],'dpi':300})
 caption='原文 '+label+'：完整图表及图注' if label!='Table 4' else '原文未编号 Funding 表；Table 4 仅为本笔记截图索引'
 figs.append({'label':label,'caption':caption,'panels':[],'pages':pages})
draft={'identity_matches':True,'identity_reason':'PDFtitle3authorsCMR39issue2DOI verified23pages','paper_type':'review','title_zh':'真菌辅酶A代谢与抗真菌靶点的证据边界','filename_title':'真菌辅酶A代谢与抗真菌靶点的证据边界','journal_short':'Clin Microbiol Rev','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodexsourcegroundedreview23pages'})
images=[]
for l,p,b in spec:
 out=d/('MQZQ29BH-'+l.replace(' ','-')+'-p'+str(p)+'-complete.png');doc[p-1].get_pixmap(dpi=300,clip=fitz.Rect(b),alpha=False).save(out);sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
 caption=next(f['caption'] for f in figs if f['label']==l);images.append({'label':l,'caption':caption,'page':p,'file':str(target),'bbox':b,'panels':[],'sha256':sha})
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'rect':list(doc[0].rect),'images':[x['file'] for x in images]},ensure_ascii=False))


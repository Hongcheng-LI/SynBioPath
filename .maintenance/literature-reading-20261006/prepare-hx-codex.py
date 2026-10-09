import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'HX6HEZ5C';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'));doc=fitz.open(rec['main_pdf'])
spec=[('Figure 1',p,[60,45,558,650]) for p in range(6,11)]+[('Figure 2',11,[78,45,560,477]),('Figure 3',12,[150,45,558,558]),('Table 1',12,[150,575,540,643]),('Figure 4',13,[150,45,558,440]),('Figure 5',13,[65,457,558,708]),('Figure 6',14,[55,45,560,620]),('Figure 6',15,[150,45,560,205]),('Figure 7',15,[116,222,560,718]),('Figure 8',16,[65,334,560,738]),('Figure 9',17,[150,105,560,738]),('Figure 10',18,[65,45,560,274])]
gaps=['22mainpagesreadviewed; referencesmetadatareadnot98originalpapers; SI S1S2TablesS1S6unavailablelocallyunread; GenBankMW030627notindependentlydownloaded','TenFiguresoneTable16complete300dpicrops Figure1p6to10 Figure6imagep14captionp15','TmLOX13sequence2676bp891aa enzyme102kDa; TMabsencepredictionnotexperimentlocalization; Sceorpathogenresultsnottransferredhere','Table1Vmaxunitnmolminus1minminus1sourceproblemnotcorrectedinvented; nofitCIskcat; Km29.6vs24.7C18:3notlower','210/31specificactivitymeansratio6.774193548;201.4/44.6Vmax4.515695067;6.8/1.8ratio3.777777778 notrawreplicatestatistics','MediumPTXnotcelltotalflux; internalstandardusesPTXsameanalyte deductionunclear no reportedrecoveryLODLOQcalibrationfullvalidation','Figure6DimagechromatogramEbar vscaptionDbarEchromatogram; targetindependentsecondsiRNAgenerescuenotshown','NDGA98notabsolute100%; p14textcontrol24mgL vsFigure7Baxis5/control~4.2 sourceconflict no30foldinvented; planttreatmentnotpureenzymeconcentration','Figure8colorbarminus40plus40vscaptionminus20plus20; Figure9lastrowrepeatedMixEOE vsMixDHOEMixHOEothercontexts','n9combines3independentsamples3technicalmeasurementsnot9biological; ANOVAP<.05 noexactPposthocCIorrawrefit','JApartial58%; oxylipin3.6/4.1/4.0over4.2=85.71497.61995.238 notformalequivalence; nooverexpressionindustrialclaim','BackgroundDBAThydroxylatedincorrectnotrepeated;Figure10simplifiedschemenotallfluxmeasured; fungusAfPXGproductionprotocolnotreproduced']
figs=[]
for label in dict.fromkeys(l for l,p,b in spec):
 pages=[]
 for l,p,b in spec:
  if l==label:
   r=doc[p-1].rect;pages.append({'page':p,'bbox':[b[0]/r.width,b[1]/r.height,b[2]/r.width,b[3]/r.height],'dpi':300})
 figs.append({'label':label,'caption':'原文 '+label+'：完整图表及图注','panels':[],'pages':pages})
draft={'identity_matches':True,'identity_reason':'22pages title3authorsSciRep1542330DOI verified','paper_type':'research','title_zh':'Taxus media脂氧合酶TmLOX13与紫杉醇积累的功能证据','filename_title':'Taxus media脂氧合酶TmLOX13与紫杉醇积累的功能证据','journal_short':'Sci Rep','category':None,'related_categories':[],'classification_reason':'全部文献解读完成后统一分类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodexsourcegrounded22pages'})
images=[]
for l,p,b in spec:
 out=d/('HX6HEZ5C-'+l.replace(' ','-')+'-p'+str(p)+'-complete.png');doc[p-1].get_pixmap(dpi=300,clip=fitz.Rect(b),alpha=False).save(out);sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target);images.append({'label':l,'caption':'原文 '+l+'：完整图表及图注','page':p,'file':str(target),'bbox':b,'panels':[],'sha256':sha})
w.write_json(d/'codex-crops.json',images);w.write_json(d/'codex-arithmetic.json',{'activity_ratio':210/31,'Vmax_ratio':201.4/44.6,'Vmax_Km_ratio':6.8/1.8,'silenced_retained_percent':100/2.3,'silenced_decline_percent':100-100/2.3,'oxylipin_recovery_percent':[100*x/4.2 for x in [3.6,4.1,4.0]],'method':'Actuallycomputed source reportedmeanratios notrawstats'})
print(json.dumps({'CJK':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':len(images),'rect':list(doc[0].rect)},ensure_ascii=False))


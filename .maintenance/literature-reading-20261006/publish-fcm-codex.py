import json,time
import worker as w
d=w.ROOT/'sources'/'FCM54K4J'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read full10-page main text and viewed original pages1–9, checked tables/structure diagrams and visually inspected16 actual crop screenshots. Corrected cached draft mechanism inflation, invented iodine isotope pattern, SAR pairing and Table4 data conflict. No independent second-model review','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[
 {'claim':'12new and6known compounds;1–3,5–12,14new','source_locator':'PDF1 abstract, PDF2 Chart1, PDF5 knowncompounds','evidence':'Numbered structure families match list'},
 {'claim':'2 contains1Br with1:1 peaks556.20593/558.20386;3 iodineC14 and6 iodineC20','source_locator':'PDF4 results andTables1/2','evidence':'Br isotopepair and local C14/C20 chemical shifts; no claimed iodine doublet'},
 {'claim':'NaBr andKI isolationroutes separately list9 compounds each,5/6notbothgroups','source_locator':'PDF8–9 experimental','evidence':'NaBr1 2 4 7 9 12 13 17 18;KI3 5 6 8 10 11 14 15 16'},
 {'claim':'CalculatedECD6/7/10/11 with separate functionals;Xray18asreference','source_locator':'PDF5,PDF7–9 figures4/5/7/8 andmethods','evidence':'CAM-B3LYP RBVP86 B3LYP WB97XD respectively;S87andFlack−0.09(9) for18'},
 {'claim':'Table4 C12proton12/14 conflicts withbodyChart1Table5','source_locator':'PDF5paragraph,PDF6Table4,PDF7Table5','evidence':'Table4shows12=4.10s14=1.71s;carbon12=20.0 14=63.5'},
 {'claim':'Haloperoxidase not identified;negativeincubation only constrains testedreaction','source_locator':'PDF4 paragraph,PDF8conclusion,PDF9incubationmethods','evidence':'No gene protein enzymatic assay reported in fullpaper'},
 {'claim':'Table6unitsμM meanSD n3 independentexperiments;no Pvalues','source_locator':'PDF8Table6footnote','evidence':'1 45±3;2 7.4±1.5;3 47±1;18 .2±.1;Vero2 18±2'},
 {'claim':'Matchedacetylpairs4/5 12/13 14/15 17/18;17R=H18R=Ac','source_locator':'PDF2Chart1','evidence':'SharedstructureR substitutions in originalchart'},
 {'claim':'SameformulaC30H37NO4 calculatedmass variesin5/7/8 printeddata','source_locator':'PDF9experimental','evidence':'476.27121 476.27683 476.27912 printed for same[M+H]assignment'}
 ],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked);w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

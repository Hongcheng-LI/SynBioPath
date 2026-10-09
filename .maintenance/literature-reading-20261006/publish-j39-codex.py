import json,time
import worker as w
d=w.ROOT/'sources'/'J39PT6YP'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read original main text and methods pages1–16 and inspected all original graphic pages2–12 plus15 actual crops. Figure2 recropped to avoid intersecting nextFigure3. Supporting information and full reference list not independently reread; no external-model call.','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[
 {'claim':'32 numbered compounds include11new plus1first-natural knownsynthetic28','source_locator':'PDF1–2 Figure1 andPDF16conclusion','evidence':'1,3,5,11,13–15,25–27,29 vs28 distinguished'},
 {'claim':'3 aromatic protons and ionlabel conflict retained','source_locator':'PDF3Table1 andtext;PDF13spectroscopic data','evidence':'6.44/6.98 versus3.26/2.94;261.0398[M-H]- versus[M+H]+'},
 {'claim':'11 relativeconfiguration pluschiral separation/ECD,atom9a/9b conflict','source_locator':'PDF6Table2 Figure4D','evidence':'9a133.3quaternary vs9b76.9oxymethine;ECDlabel9b'},
 {'claim':'13–15 absolute assignmentsECD,15DP4candidateprobabilitynotuniversalcertainty','source_locator':'PDF7 Figure6;Figure4E','evidence':'13 8R9R10aR,14 8R9R10aS,15 8R9S10aR;15a100percent reportedSI notrerun'},
 {'claim':'25/26C10MosherS/R distinguishedfromsharedcoreECD','source_locator':'PDF8Table4 Figure7;Figure4F','evidence':'C10S25/C10R26;core7S8R8aR;H3-10 typo vsH3-12'},
 {'claim':'27formulaandname discrepancies preserved','source_locator':'PDF8–9 andFigure1–2','evidence':'m/z316.9668 ioncompositionC11H10O3I+,drawnOH omitted fromtrivialname'},
 {'claim':'29DP4relative29b99.12percent plusECD5R3primeS;nameconflict','source_locator':'PDF10Figure8,PDF14','evidence':'talarofuranone vs talarofurolactone same29'},
 {'claim':'Figure9 possiblebiosynthesisnotgeneorenzymeproof','source_locator':'PDF10–11Figure9 caption','evidence':'possible routes basedon references andstructure,notfunctionalexperiments'},
 {'claim':'10EcoliMIC0.5 vscontrol0.25 notbetterorequal','source_locator':'PDF12Table6','evidence':'10 AH0.5 VP1 VH0.5 correspondingcontrols0.5 1 2;18EC0.5 VP2 vs0.25 1'},
 {'claim':'30/31acetylassociationstrain dependent,triplicateundefinedindependence','source_locator':'PDF12Table6,PDF15assay','evidence':'EC4vs64 PA32vs32 VP32vs32;triplicate stated withoutindependence'}
 ],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked);w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

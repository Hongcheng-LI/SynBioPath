import json,time
import worker as w
d=w.ROOT/'sources'/'PEP725R8'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read full9-page minireview, viewed original illustration pages and visually checked all9 actual screenshots; primary references not independently reread; no external-model call','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[
 {'claim':'Review publicationChemBioChem2002 3 619–627,not newuniformexperiment','source_locator':'PDF1 journaltitleMINIREVIEWS and alltext','evidence':'Cases fromgroup and literature; no uniformprimarymethodssection'},
 {'claim':'Scheme1 13/14reported1:3cis-trans mixture;oneculturediversitynot16clusters','source_locator':'PDF1 intro andPDF2Scheme1','evidence':'ansamycins macrolides collinolactones butyrolactones'},
 {'claim':'Scheme2 fourmetabolites3biogeneticpools;19yield13foldNaBr withoutBrin19','source_locator':'PDF1–2introScheme2','evidence':'Gabosines/sugar hexacyclinicacid/PKSI angustmycinderivative'},
 {'claim':'Aochraceus previous21max8mg/L versus15additionalcompoundsmax94mg/L','source_locator':'PDF3section2.1 andPDF4Scheme3','evidence':'Differentcompounds yield maxima notpairedsameproductincrease'},
 {'claim':'F24707Scheme4someproductsmax2.6g/L;55max70mg/L;ancymidoleunexpectedthreefold37','source_locator':'PDF4section2.2 andPDF5Scheme4','evidence':'Explicitunclearmechanism andsolidculture40–42,44–46'},
 {'claim':'Scheme6differentPKSexpressionversusstuttering/skipping alternatives unresolved','source_locator':'PDF6section3.2','evidence':'Two competing biosynthesis explanations explicitly given'},
 {'claim':'Scheme7pHranges5–6.5/6.5–8 butbodycaseharvest8.2','source_locator':'PDF6section3.3 andPDF7Scheme7','evidence':'Schematicranges are summary notstrictthreshold'},
 {'claim':'Scheme8standard93/94 11/6mgL;nonprecursorinduction95/96supportsalternativeexplanations','source_locator':'PDF7Scheme8andsection3.4','evidence':'Signal/cofactoranddetoxification hypotheses given'},
 {'claim':'Conclusion >100compounds >25classes6microorganisms;notuniversalprediction','source_locator':'PDF7conclusion','evidence':'Authors state no commonrules for allmicroorganisms'}
 ],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked);w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

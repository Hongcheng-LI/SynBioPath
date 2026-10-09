import json,time
import worker as w
d=w.ROOT/'sources'/'CTJPEHPH'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
images[21]['caption']=images[21]['caption'].replace('454–480','453–480（453 在前页也出现）')
draft['report']=draft['report'].replace('组合干预相关的 **454–480**','组合干预相关的 **453–480**（**453** 在前页也出现）')
w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex source-grounded reading'})
(d/'codex-report.md').write_text(draft['report'],encoding='utf-8')
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read main text pages1–14, inspected original illustration pages2–13 and all23 actual300dpi crops; selected reference entries compared; cited primary studies not all independently reread. RSC author accepted manuscript checked; NAR publisher-indexed primary summary checked, landing page unavailable. No external-model call.','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[
 {'claim':'Narrative review not uniform primary experiment; own23 locators not author figure numbers','source_locator':'PDF1–14 and actual graphical pages2–13','evidence':'Continuous compound numbers across unnumbered plates'},
 {'claim':'501 highest compound number not501 globally new molecules','source_locator':'PDF2 graph1 and PDF13 graph23','evidence':'Isotopic members, conformer depictions and known compounds also included'},
 {'claim':'Culture state examples span12 genera without uniform factorial design','source_locator':'PDF5–9 culture state section','evidence':'Medium/state/oxygen vary jointly across studies'},
 {'claim':'Count/range inconsistencies48–49 and153–157 retained','source_locator':'PDF3 and6','evidence':'four versus two and five numbered compounds'},
 {'claim':'Spicaria activity references235 outside275–293 range','source_locator':'PDF8 text and both graphic plates','evidence':'235 lies in preceding Penicillium plate'},
 {'claim':'349–354 co-culture statement differs from cited autoclaved bacteria reference','source_locator':'PDF10 and selected Ancheeva2017 reference','evidence':'Reference title specifies autoclaved Pseudomonas aeruginosa'},
 {'claim':'Nicotinamide NAD-dependent HDAC correction based on primary author manuscript','source_locator':'PDF12 and RSC c5ob01595b authorversion abstract','evidence':'Review ZnII-type label conflicts with primary abstract'},
 {'claim':'Histone acetylation electrostatic direction corrected with primary indexed summary','source_locator':'PDF11 and NAR47(16)8470 indexed primary summary','evidence':'Neutralized lysine charge reduces corresponding electrostatic attraction; full NAR landing unavailable'},
 {'claim':'Precursor activity wrong498 reference not assigned to499–501','source_locator':'PDF13–14','evidence':'498 belongs preceding Penicillium example'},
 {'claim':'Plate22 repeats453 before454–480','source_locator':'PDF12–13 actual crops21–22','evidence':'453 explicitly appears on both pages'}
 ],'unresolved_source_issues':draft['source_gaps']+['Original embedded structure plates contain a few clipped tiny atom-label glyphs, also visible in full original page8; screenshots preserve source content without redrawing.']}
w.write_json(d/'codex-source-review.json',checked)
w.write_json(d/'codex-crops.json',images)
w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

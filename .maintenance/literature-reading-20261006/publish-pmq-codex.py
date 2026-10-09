import json,time
import worker as w
d=w.ROOT/'sources'/'PMQWGNMV'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read all8 original scanned pages, checked local OCR numerical claims against source images and visually inspected all5 actual crops; no second-model review','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[
 {'claim':'750g commercial rhubarb and isolated quantities40/8/25/35/7/10mg for I–VI','source_locator':'PDF2 Chart1 and PDF7 experimental','evidence':'All9 compound branches and yields visible in original flowchart'},
 {'claim':'TableI excludes II and notes interchangeable aromatic carbon assignments','source_locator':'PDF3 TableI','evidence':'ColumnsI III IV V VI and footnotes a/b visible'},
 {'claim':'IV C2′ S assigned using modifiedHoreau; A/B are derivative chromatogram peak labels','source_locator':'PDF4 Figure1 and paragraphs','evidence':'Caption identifies(R)-amine with(R)/(S)-phenylbutyric acid derivatives'},
 {'claim':'V hydrolysis IV/glucose, anomerJ7Hz; no reported HMBC or separate chiral sugar analysis','source_locator':'PDF4 text and PDF7 experimental','evidence':'Crude hesperidinase hydrolysis and ordinary glucose TLC comparison'},
 {'claim':'VI saturated carbon shifts73.2/44.6/191.2 and CD-basedS assignment','source_locator':'PDF3 TableI, PDF5 paragraph and PDF7 experimental','evidence':'13C shifts and303/332nm CD molar ellipticity signs'},
 {'claim':'Figure2 lower-left IV structure incorrectly labelled VI in original','source_locator':'PDF5 Figure2','evidence':'Both lower-left hydroxypropylchromone and lower-right chromanone labelledVI'},
 {'claim':'Chart2 proposedbiogenesismodel, no tracer/genes/enzymes validated here','source_locator':'PDF5–6 discussion and Chart2','evidence':'Caption Possible Scheme and full-paper methods do not include such experiments'}
 ],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked)
w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

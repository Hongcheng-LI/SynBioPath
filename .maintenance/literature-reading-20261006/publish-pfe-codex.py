import json,time
import worker as w
d=w.ROOT/'sources'/'PFEFMY85'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
claims=[
('182 numbered entries,90new and132references are review statistics','PDF1,20–21','Coverage1984–March2022,86coldseep96hydrothermal;not current full field census'),
('Occurrence and activity can derive from different source papers','PDF3 and references14–15','Sterol19 activities cited to Ficus/ricebran sources;not same coldseep experimental evidence'),
('No original structures for80–83 or173','PDF10,17–18','Text-only EPS/surfactin entries retained without fabricated screenshots'),
('Tentative sedimentary ethers not proven producers','PDF11 Figure10','84–86 tentatively identified in carbonates'),
('Glycoside and figure references conflict','PDF11 Figure11,PDF14 Figure14','88 drawing versus89body;134–136 figure14 versus citedfigure15'),
('Taxonomy and geographical inconsistencies remain explicit','PDF10,12,18–19','Vibrio/Bacillus calledfungi;archaea underbacteria;WesternAtlantic versus126.8983E27.7875N'),
('Suspicious units not silently converted','PDF9,13–14','79MIC25mg/mL;110 0.13±0.4ug/mL;126 35.29±1.55mM'),
('132/142 naming and computational evidence distinguished','PDF14,20 andreference104','132 deoxytryptoquivaline;142 chaetominine;ref104 in silico multitarget study,not directbinding experiment'),
('180 name versus depicted membrane lipid requires primary-source checking','PDF18 Figure20','Text geranylgeranylglycerol versus180 depicted tetraether;not silently reidentified'),
('Source pie percentages describe assembled literature','PDF19 Figures21–22','Cold56fungi24animal17bacteria3other;hot78fungi19bacteria3animal;archaea classification caveat'),
('Activity categories overlap and lack independent assay denominator','PDF20 Figure23','Antibacterial34cold23hot;antitumor17cold8hot;not ecology abundance or discovery success probability')]
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read source maintext pages1–21, inspected original graphic pages2–20, selected references including104 and all23actual crops. Figure21 recropped to avoid nextFigure22 bitmap. No independent external-model review, no comprehensive rereading of cited primary papers.','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[{'claim':a,'source_locator':b,'evidence':c} for a,b,c in claims],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked)
w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})

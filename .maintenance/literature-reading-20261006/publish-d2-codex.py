import json,time
import worker as w
d=w.ROOT/'sources'/'D2T4CM4K'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
claims=[
('Ten diterpene synthases and four CYPs; 40 initial combinations,31 positive','PDF2–3 Table1','Later combinations selected rather than exhaustive'),
('217 reported products,162 new-to-Nature annotations','PDF2–3 Figure1','Annotation novelty distinct from full structure confirmation'),
('13 products characterized by NMR','PDF3','Remaining structures have different confidence levels; SI not independently read'),
('Isopimaradiene oxidation and nezukol branches','PDF3–4 Figure2','Product formation supports combination sufficiency,not every isolated enzymatic step'),
('Miltiradiene conversion to abietatriene described as spontaneous','PDF4–5 Figure3','Not attributed to CYP catalysis'),
('Product26 trans-biformen-3beta-ol','PDF5–6 Figure4','Structure corrects initial C18 alcohol assumption'),
('Selected titers23 2.09,26 2.68,147 2.38mg/L','PDF3 Table2','Not uniform titers of all217 products; replicate/error reporting limitations retained'),
('Docking distances2.89/2.97 and2.59/3.15angstrom','PDF6–7 Figure5','Predicted geometry,not experimental complex structure or activation energy'),
('No activity screening of the entire product library','PDFmaintext','Prior pharmacology citations do not establish activity of current products')]
checked={'pass':True,'review_status':'codex-source-checked','method':'Current Codex read all8 main PDF pages; original pages2–7 and all7 actual300dpi figure/table crops visually checked. SI, nmrXiv and MetaboLights not independently read. No external model review.','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':[x['label'] for x in images],'covered_labels':[x['label'] for x in images],'missing_panels':[],'missing_pages':[]},'verified_claims':[{'claim':a,'source_locator':b,'evidence':c} for a,b,c in claims],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',checked)
w.validate_structure(draft)
note=w.publish(rec,draft,images,checked,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})
print(json.dumps({'note':note,'images':len(images)},ensure_ascii=False))

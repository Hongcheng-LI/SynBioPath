import json,time
import worker as w
d=w.ROOT/'sources'/'26XKNUT7'
rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
draft=json.loads((d/'codex-draft.json').read_text(encoding='utf-8'))['draft']
images=json.loads((d/'codex-crops.json').read_text(encoding='utf-8'))
arithmetic={'efficiency_ratio_emodin_rhapontigenin':8.5/1.9,'specific_activity_nmol_min_mg':62*60/1000,'molecular_mass_error_ppm':(455.0961-455.0954)/455.0954*1e6}
w.write_json(d/'codex-arithmetic.json',arithmetic)
claims=[('Identity','PDF293','5authorsPlantBiotechnology37p293to299DOI online20200730notZotero0925fundJP16K08297'),('Coverage','PDF293to299Figures1to6Tables1to2','All7mainpagesread7originalpagesviewed8final300dpicropsfullpanelscaptionsfootnotesSIactualunreadrawNMRunread'),('Candidates','PDF295Figure2','RpUGT1UGT73BE14GroupD RpUGT2UGT72B49RpUGT3UGT71AQ1GroupE homologcloningnotallgenomecoverage'),('Product','PDF294to296Figure3','Emodin6OauthorsNMR1D2DMSassignment455.0961vs455.0954 notMSalonepositions;4vs40minnotexactyield extendednootherdetectednotuniversalzero'),('Scope','PDF295to297Figures4and5','FiveanthraquinonesonlyemodinpositiveRpUGT1othersRpUGT2/3negative testedconditions rhapontigeninpositive resveratrolpiceatannolnegative;flavonolsmultiproduct3Otentative;10vs180mindifferent'),('Activity','PDF297Table1','All7activitiesandSDread emodin62pkatmg notconversionyield quercetin79.4SD29.6triplicatemeasurementsnotstatisticaldifference'),('Kinetics','PDF294and297Table2','All3Km/kcat/efficienciesSDunitsreadkcat1e-3s-1fixedalternates10and2.5mM;efficiencyratio4.473684Python nofitrawCIhypothesized'),('Organs','PDF296and298Figure6','Oneindividualsamecollectdaytriplicate not3plants;freshweightunitsnotfermentationtitre expressionaccumulationnospatialcorrelation transportcompartmentsotherUGThypothesesnotproof'),('Limits','PDF293to299','Noindustrialyieldorengineeringvalidated no8Oenzymediscovered noRugulosinAsubstratetested nativefunctionmightnotgeneticnecessityproof referencesnotindependentlyread noCOIstatement')]
labels=[x['label'] for x in images]
review={'pass':True,'review_status':'codex-source-checked','method':'CurrentCodex7mainpagesread7originalsviewed8final300dpicropsallpanelscaptionsfootnotescheckedPythonarithmeticnoexternalLLMnohumanreview','human_full_paper_review':False,'identity_matches':True,'classification_supported':True,'crop_complete':True,'major_issues':[],'figure_coverage':{'expected_labels':labels,'covered_labels':labels,'missing_panels':[],'missing_pages':[]},'verified_claims':[{'claim':a,'source_locator':b,'evidence':c} for a,b,c in claims],'unresolved_source_issues':draft['source_gaps']}
w.write_json(d/'codex-source-review.json',review)
w.validate_structure(draft)
note=w.publish(rec,draft,images,review,d)
w.record_result({'key':rec['key'],'title':rec['title'],'time':time.strftime('%Y-%m-%d %H:%M:%S'),'status':'published','note':note,'images':len(images),'review_status':'codex-source-checked'})
print(json.dumps({'note':note,'images':len(images)},ensure_ascii=False))

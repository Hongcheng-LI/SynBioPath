import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'9HACLINL';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.511,.318,.922,.475],[]),('Figure 1',2,[.075,.077,.491,.389],['A','B']),('Figure 2',2,[.075,.637,.491,.936],[]),('Figure 3',2,[.511,.17,.922,.378],['1','2','3']),('Scheme 1',3,[.511,.20,.922,.514],[]),('Figure 4',4,[.075,.081,.922,.599],list('ABCDEFGHI'))]
figs=[{'label':l,'caption':'原文图：新骨架、结构证据、生源假说与AKR1B1相互作用','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地无SI与CIF2126704，未重跑ECD/DP4或晶体精修','标题steroidanalogues非经典甾醇途径证明','1先Xray补关键NMR缺失，2/3无主文单晶','正文fourmethines列出五个碳项','C20去屏蔽文字但两处65.5，需SI同溶剂核对','NOE缺失有检测边界，Z/E位移规则限同类和溶剂','DP4+100percent候选比较非全结构确定性','生源Scheme仅假说，无前体/中间体检测示踪基因酶证据，生产者未定位','酶A图IC50plusminus1.04误差类型未报告，完整方法在SI','2/3在20uM筛选阴性非全部浓度无活性','SPR2 Kd43.16原图S7未提供，1 Kd3.40直接体外结合支持','IC50不能等于Kd或由比值推Ki竞争机制','CETSAHepG2C/Dn3，无完整原条带及统计，不能估细胞Tm','蛋白CD53.9plusminus.6至57.6plusminus.4误差类型未说明，不是体内药稳','beta-angle术语含混不扩写二级结构转变','405nm为激发观察条件非发射峰，HepG2I仅分布，HeLa双标共定位在未读SI','无靶点位点/同家族选择性/动物疾病疗效','在线June27与ZoteroJuly12区分']
draft={'identity_matches':True,'identity_reason':'Formal5pageOL26 5794–5798 titleauthorsDOImatch, notSI','paper_type':'research','title_zh':'Tagpyrrollins与Tagpyrrollidone的结构及AKR1B1结合','filename_title':'Tagpyrrollins的结构生源假说与AKR1B1证据','journal_short':'Org Lett','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex originalPDFreading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    box=fitz.Rect(315.44,255,555.42,379)
    out=d/'9HACLINL-Graphical-Abstract-clean.png'
    doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
    sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
    images[0].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

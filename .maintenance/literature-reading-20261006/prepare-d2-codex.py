import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'D2T4CM4K';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Figure 1',2,[303,50,563,687],['A','B']),('Table 1',3,[34,50,294,405],[]),('Table 2',3,[34,586,563,744],[]),('Figure 2',4,[34,304,563,748],list('ABCDEFG')),('Figure 3',5,[34,267,563,748],list('ABCDEFG')),('Figure 4',6,[34,485,563,748],list('ABC')),('Figure 5',7,[34,52,563,265],list('AB'))]
with fitz.open(rec['main_pdf']) as doc:
    figs=[{'label':l,'caption':'原文图表：二萜组合产物、分级结构信息、定量与对接模型','panels':a,'pages':[{'page':p,'bbox':[b[0]/doc[p-1].rect.width,b[1]/doc[p-1].rect.height,b[2]/doc[p-1].rect.width,b[3]/doc[p-1].rect.height],'dpi':300}]} for l,p,b,a in spec]
gaps=['本地无SI，nmrXiv和MetaboLights未独立读取，对接未重跑','217统计产物非全部完整结构确证，162数据库未记录判断非162全NMR新化合物','主文13NMR、36已述18MS与后文38MS各口径关系需SI','11087和10阶段产物非直接独立相加，190氧化汇总需全表去重','40单CYP31阳性，双CYP21选择性后续非穷尽全子集','新酵母产物充分性不是原生途径必要性，背景非酶贡献未完全排除','醛36likelyintermediate非纯化酶逐步确证','miltiradiene至abietatriene自发不能归CYP','cisabienol醇3beta或18未唯一指定','26结构C3beta纠正原C18假说，对接非实验结构势垒或精确比例','Table2定量n3至5，误差种类/重复类型主文未完整，未复现方法','Table2部分enz栏148/152/210不完整不能代表全表达','qNMR支持选定GC/LC定量，未知标准产物不估精确滴度','MGperL非全217通用产量无工业性能','正文药理为引用未做本产物活性筛选','主文RoMiS交叉引Fig2E/F但对应Fig3E/F，按实际图核查','13NMR里作者列四候选新结构22/120/134/147，26已有类同报道']
draft={'identity_matches':True,'identity_reason':'Formal8pageMetabEng82 193–200, titleauthorsDOImatch','paper_type':'research','title_zh':'酵母二萜组合生物合成的产物与选择性证据','filename_title':'酵母二萜组合生物合成的结构鉴定与选择性边界','journal_short':'Metab Eng','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex originalPDFreading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    for i,(l,p,b,a) in enumerate(spec):
        box=fitz.Rect(b);out=d/('D2T4CM4K-'+l.replace(' ','-')+'-complete.png')
        doc[p-1].get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
        sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
        images[i].update(file=str(target),sha256=sha,bbox=list(box))
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

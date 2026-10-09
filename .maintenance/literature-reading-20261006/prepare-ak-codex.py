import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'AK9B4YFU';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[328,270,556,374],[],0),('Unnumbered Structure Graphic',2,[51,58,293,216],[],0),('Table 1',3,[55,59,401,754],[],90),('Table 2',4,[51,58,556,417],[],0),('Figure 1',4,[51,424,556,727],[],0),('Figure 2',5,[51,59,556,424],[],0),('Figure 3',6,[51,68,292,491],list('ABC'),0),('Figure 4',7,[51,65,556,667],list('ABCD'),0)]
with fitz.open(rec['main_pdf']) as doc:
    figs=[{'label':l,'caption':'原文图表：Maydistacins连接、构型及计算比较','panels':a,'pages':[{'page':p,'bbox':[b[0]/doc[p-1].rect.width,b[1]/doc[p-1].rect.height,b[2]/doc[p-1].rect.width,b[3]/doc[p-1].rect.height],'dpi':300}]} for l,p,b,a,rot in spec]
gaps=['无本地SI，NP-MRD及被引原文未独立读取，计算未重跑','在线2023与卷年2024分开','正文DEPT1非质子化碳概括与Table2逐位CH归属不一致','Table1与Table2的4/5溶剂脚注不同按各表保存','3正文NOE把H2a列入两面存在内部不一致','3与2总DBE均8，开桥与乙酰羰基变化不简写只乙酰化','DP4+100%仅指定候选和模型条件概率非全部结构无条件正确','1–3计算ECD，4–7类比和化学关联不全独立计算，无单晶','4质量结果441.2599与实验441.2602不一致','Figure4C图内5含11Sstar图注候选省略该位点','S68水解叠谱S70类比ECD未读取','阳性对照摘要6.7±.6正文6.9±.7，1为19±2uM','MTT50uM存活>90非其他体系或长期安全','NO活性重复数误差种类检验主文未明确','首次类活性为作者查新判断未独立全量检索','无活性图表不能添加虚构曲线，无基因或靶点验证']
draft={'identity_matches':True,'identity_reason':'Formal9pageJNP87 68–76,titleauthorsDOImatch','paper_type':'research','title_zh':'Maydistacins的连接构型与NO抑制证据','filename_title':'Maydistacins的构型计算与NO抑制证据','journal_short':'J Nat Prod','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'CurrentCodex mainPDFsource reading without externalmodel'})
images=w.crops(rec,draft,d)
with fitz.open(rec['main_pdf']) as doc:
    for i,(l,p,b,a,rot) in enumerate(spec):
        box=fitz.Rect(b);out=d/('AK9B4YFU-'+l.replace(' ','-')+'-complete.png');doc[p-1].get_pixmap(matrix=fitz.Matrix(300/72,300/72).prerotate(rot),clip=box,alpha=False).save(out)
        sha=hashlib.sha256(out.read_bytes()).hexdigest();target=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(target)
        images[i].update(file=str(target),sha256=sha,bbox=list(box),rotation_degrees=rot)
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

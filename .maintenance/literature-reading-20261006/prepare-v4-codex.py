import json,re,fitz,hashlib
import worker as w
d=w.ROOT/'sources'/'V4DNVIRB';rec=json.loads((d/'prepared.json').read_text(encoding='utf-8'))
spec=[('Graphical Abstract',1,[.519,.294,.916,.407],[]),('Figure 1',2,[.075,.085,.491,.439],list('ab')),('Unnumbered Structure Graphic',2,[.075,.462,.491,.711],[]),('Figure 2',3,[.511,.085,.922,.404],list('ab')),('Figure 3',4,[.075,.082,.922,.502],[])]
figs=[{'label':l,'caption':'原文图：tpt基因簇、产物结构或建议生物合成路径','panels':a,'pages':[{'page':p,'bbox':b,'dpi':300}]} for l,p,b,a in spec]
gaps=['本地没有SI，未读原始NMR/ECD和构建回补补充图','1/6/7打印分子式氢数与所列计算质量不一致，原图确认并本地实际计算，无擅自更正','骨架绝对构型包含同类生物合成和ECD类比，未独立重新解析','tpt14遗传必要性，不等于已完成纯酶糖供体底物谱测定','tpt12缺失株产物变化回补不恢复，不能当作直接因果工程规律','缩减约52kb簇与62402bp完整构建体范围不同','异源4由保留时间和UV匹配，未报告独立分离完整结构与滴度','非酶促成环为probably假设，宿主内源酶和提取阶段作用未排除','建议中间体I–IV不是全已分离，未知C17氧化酶未定位','分离回收mg不是校正滴度；无完整独立重复和统计','纸片阴性不提供MIC，50uM两细胞系阴性不是全药理结论','未测试引言所述大豆脂氧合酶活性','在线发布日期原文January3与ZoteroJanuary26区分']
draft={'identity_matches':True,'identity_reason':'ActualsixpagePDF title DOI authorsJNP2024 87 98–103 match, main article notSI despitepreparedcheckflag','paper_type':'research','title_zh':'Tetrapetalones发现与异源生产及四环形成线索','filename_title':'Tetrapetalones基因簇与非酶促成环的证据边界','journal_short':'J Nat Prod','category':None,'related_categories':[],'classification_reason':'全库完成后归类','source_gaps':gaps,'figures':figs,'report':(d/'codex-report.md').read_text(encoding='utf-8')}
w.normalize_format(draft);w.validate_structure(draft);w.write_json(d/'codex-draft.json',{'draft':draft,'method':'Current Codex actual mainPDFreading and formulaarithmetic; no externalmodel'})
images=[]
with fitz.open(rec['main_pdf']) as doc:
 for g in draft['figures']:
  part=g['pages'][0];p=doc[part['page']-1];b=part['bbox']
  # Graphical abstract is made from transformed/clipped raster tiles whose
  # reported bboxes extend into the surrounding prose. Use visually checked
  # page coordinates, preserving the actual rendered graphic instead.
  if g['label']=='Graphical Abstract':box=fitz.Rect(315,234,557,326)
  else:
   box=fitz.Rect(max(0,b[0]-.008)*p.rect.width,max(0,b[1]-.008)*p.rect.height,min(1,b[2]+.008)*p.rect.width,min(1,b[3]+.008)*p.rect.height)
   for x in p.get_text('blocks'):
    if w.caption_graphic(x[4].strip())==g['label']:box |= fitz.Rect(x[:4])
   box=(box+(-3,-3,3,3))&p.rect
  out=d/(rec['key']+'-'+g['label'].replace(' ','-')+f'-p{part["page"]}.png')
  p.get_pixmap(matrix=fitz.Matrix(300/72,300/72),clip=box,alpha=False).save(out)
  sha=hashlib.sha256(out.read_bytes()).hexdigest();unique=out.with_name(out.stem+'-'+sha[:16]+'.png');out.replace(unique)
  images.append({'label':g['label'],'caption':g['caption'],'page':part['page'],'file':str(unique),'bbox':list(box),'panels':g['panels'],'sha256':sha})
w.write_json(d/'codex-crops.json',images)
print(json.dumps({'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',draft['report'])),'images':images},ensure_ascii=False))

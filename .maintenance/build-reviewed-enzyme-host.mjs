// Deterministic compiler of human-reviewed, body-line decisions. No title/keyword classifier.
// node .maintenance/build-reviewed-enzyme-host.mjs [--check]
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = p => fs.readFileSync(path.join(root,p),'utf8').replace(/^\uFEFF/,'');
const json = p => JSON.parse(read(p));
const digest = p => crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex').toUpperCase();
const plan = json('.maintenance/三框架迁移清单.json');
if (path.resolve(plan.root)!==root) throw Error('Wrong workspace');
const manifest = new Map(plan.files.map(f=>[f.id,f]));
for (const f of plan.files) if(digest(f.target)!==f.sha256.toUpperCase()) throw Error(`Original note changed: ${f.id}`);
const decisions=json('.maintenance/enzyme-host-body-review.json');
const baselinePath='.maintenance/enzyme-host-before-body-review.json';
const ep='酶工程/酶索引清单.json', hp='细胞工厂/细胞工厂索引清单.json';
const existing=fs.existsSync(path.join(root,baselinePath));
const baseline=existing?json(baselinePath):{enzyme:json(ep),host:json(hp),pages:{}};
if(!existing){
  for(const framework of ['酶工程','细胞工厂']){
    for(const d of fs.readdirSync(path.join(root,framework),{withFileTypes:true})){
      const p=`${framework}/${d.name}/00. 类别导航.md`;
      if(d.isDirectory() && fs.existsSync(path.join(root,p))) baseline.pages[p]=read(p);
    }
    const p=`${framework}/00. ${framework}导航.md`; baseline.pages[p]=read(p);
  }
}
const e=structuredClone(baseline.enzyme), h=structuredClone(baseline.host);
function evidence(rows,ids){
  const out=new Map();
  for(const row of rows){
    const [id,lines]=row, f=manifest.get(id);
    if(!f||out.has(id)) throw Error(`Invalid/duplicate decision ${id}`);
    const body=read(f.target).split(/\r?\n/);
    const quotes=lines.map(n=>{
      const quote=body[n-1];
      if(!Number.isInteger(n)||n<15||!quote?.trim()||/^#|^!\[|文章题目|文章标题/.test(quote)) throw Error(`Not body evidence ${id}:L${n}`);
      return {line:n,quote};
    });
    out.set(id,{review_date:decisions.date,reading_status:'classification-relevant note body reviewed; original paper/SI not reverified',source_sha256:f.sha256,study_type:row.length===4?row[2]:undefined,judgment:row.at(-1),evidence:quotes});
  }
  if(out.size!==ids.length||ids.some(id=>!out.has(id))) throw Error('Review coverage mismatch');
  return out;
}
const er=evidence(decisions.enzyme,e.files.map(f=>f.literature_id));
const hr=evidence(decisions.host,h.files.map(f=>f.id));
const changes=[];
function enzymePage(number){return Object.keys(baseline.pages).find(p=>p.startsWith(`酶工程/${number}.`)&&p.endsWith('类别导航.md'));}
function em(id,number){return e.files.find(f=>f.literature_id===id).memberships.find(m=>m.page===enzymePage(number));}
function setRole(id,number,role,why){const m=em(id,number); if(!m)throw Error('Missing enzyme membership'); const before=m.role;m.role=role;m.theme=why;changes.push({framework:'酶工程',id,category:number,before,after:role,reason:why});}
function addEnzyme(id,number,role,why){const f=e.files.find(f=>f.literature_id===id);if(em(id,number))throw Error('Duplicate membership');f.memberships.push({page:enzymePage(number),role,section:'正文复核补充',label:`文献 ${id}`,theme:why});changes.push({framework:'酶工程',id,category:number,before:null,after:role,reason:why});}
function removeEnzyme(id,number,why){const f=e.files.find(f=>f.literature_id===id),m=em(id,number);if(!m)throw Error('Missing membership');f.memberships=f.memberships.filter(x=>x!==m);changes.push({framework:'酶工程',id,category:number,before:m.role,after:null,reason:why});}
setRole(16,'12','related_context','KYNA酰胺经NRPS/P450及自发开环形成，仅作替代酰胺生成路线比较。');
addEnzyme(16,'01','core_enzyme_study','KazC P450氧化触发DKP开环。');
addEnzyme(16,'07','core_enzyme_study','KazA NRPS参与DKP骨架装配。');
setRole(24,'13','cascade_component','商用PLE提供原位脱保护底物，非本研究核心酶发现/工程。');
setRole(111,'07','general_method','DeepAden是NRPS底物预测方法。');
setRole(113,'02','general_method','Glydentify是GT功能识别计算方法。');
setRole(116,'01','core_enzyme_study','正文明确包括T1OH/T5OH产物选择性改造。');
removeEnzyme(166,'13','氧化肽骨架切割不是TE、酯酶或环氧水解酶反应。');
removeEnzyme(243,'13','NTF2-like大环化不等于硫酯酶/水解酶。');
addEnzyme(247,'04','core_enzyme_study','AspX等候选存在实验卤化证据，不只是通用挖掘方法。');
addEnzyme(247,'08','core_enzyme_study','AspX属于Fe(II)/αKG依赖卤化体系。');
addEnzyme(206,'14','cascade_component','光驱动黄素依赖ER参与E. coli非天然合成。');
for(const f of e.files){f.body_review=er.get(f.literature_id);f.evidence_basis='分类相关正文段落人工复核；精确行号及引文见body_review；未重核原论文/SI';}
e.core_notes_unique=e.files.filter(f=>f.memberships.some(m=>m.role==='core_enzyme_study')).length;
e.general_methods_unique=e.files.filter(f=>f.memberships.some(m=>m.role==='general_method')).length;
e.all_linked_notes_unique=e.files.length;e.body_reviewed_notes=er.size;e.schema_version=2;
e.note='按笔记文件计数；研究类型与酶类别是两个维度。core_enzyme_study表示核心研究对象，不等于已工程改造。物理主归档不自动代表酶本体类别。';
function assignment(id,group){return h.files.find(f=>f.id===id).assignments.find(a=>a.group===group);}
function hostChange(id,group,fields){const a=assignment(id,group);if(!a)throw Error('Missing host assignment');changes.push({framework:'细胞工厂',id,category:group,before:structuredClone(a),after:fields,reason:hr.get(id).judgment});Object.assign(a,fields);}
function hostAdd(id,group,role,mode){const f=h.files.find(f=>f.id===id),g=h.groups.find(g=>g.key===group);if(assignment(id,group))throw Error('Duplicate host membership');const a={group,index:g.index,role,mode,note:hr.get(id).judgment};f.assignments.push(a);changes.push({framework:'细胞工厂',id,category:group,before:null,after:a,reason:a.note});}
hostChange(194,'kp',{role:'生产体系',mode:'木糖利用/ALE底盘工程＋游离脂肪酸生产'});
hostChange(263,'bc',{role:'底盘/遗传工具',mode:'RNP-CRISPR、前体池表征和报告基因整合；未验证异源目标萜类生产'});
hostChange(264,'general',{role:'计算/设计方法',mode:'D2Cell原始方法研究；含酵母香叶醇湿实验，不是综述'});
hostAdd(264,'sc','生产体系','计算指导的香叶醇生产靶点实验验证');
hostChange(208,'sc',{role:'计算/设计方法',mode:'酵母地下代谢计算模型与部分验证'});
hostChange(208,'general',{role:'计算/设计方法',mode:'逆合成与深度学习代谢网络设计'});
hostChange(53,'ec',{mode:'正文记载从葡萄糖从头合成卤代香豆素'});
hostChange(147,'ec',{mode:'全细胞模块＋末端加热化学氧化；非纯生物从头生产小檗碱'});
hostAdd(147,'cf','生产体系','全细胞转化接末端化学氧化的混合体系');
hostChange(95,'strep',{mode:'S. albidoflavus原生簇激活＋S. coelicolor模块验证'});
hostChange(199,'bc',{mode:'原生ABA路径改造积累ABA-diol，非异源完整路径'});
hostChange(225,'ec',{mode:'体内氧化紫杉烷衍生物合成；外加H2O2，不是紫杉醇'});
for(const f of h.files){f.body_review=hr.get(f.id);f.reading_status='classification-relevant note body reviewed; original paper/SI not reverified';for(const a of f.assignments)a.body_review_note=hr.get(f.id).judgment;}
h.roles=[...new Set(h.files.flatMap(f=>f.assignments.map(a=>a.role)))];
h.schema_version=2;h.classification_basis='Manual review of classification-relevant local note body passages with exact line quotes; no title inference; not original-paper/SI verification';
h.body_reviewed_notes=hr.size;h.indexed_unique_notes=h.files.length;h.production_unique_notes=h.files.filter(f=>f.assignments.some(a=>a.role==='生产体系')).length;
h.page_associations=h.files.reduce((n,f)=>n+f.assignments.length,0);
for(const g of h.groups){const ff=h.files.filter(f=>f.assignments.some(a=>a.group===g.key));g.notes=ff.length;g.production=ff.filter(f=>f.assignments.some(a=>a.group===g.key&&a.role==='生产体系')).length;}
const writes=new Map();
const pretty=o=>JSON.stringify(o,null,2)+'\n';
if(!existing)writes.set(baselinePath,pretty(baseline));
writes.set(ep,pretty(e));writes.set(hp,pretty(h));
const noext=s=>s.replace(/\.md$/,'');
const wiki=(p,label)=>`[[${noext(p)}|${label}]]`;
const link=id=>wiki(manifest.get(id).target,`文献 ${id}：${path.basename(manifest.get(id).target,'.md')}`);
const compact=s=>s.replace(/[\r\n]+/g,' ').replace(/\|/g,'／');
const caution='本轮阅读本地笔记中与分类相关的正文，不代表原论文、SI或笔记中全部数据/机制解释已经核实。计数单位为笔记文件，不是去重论文。';
const roleLabels={core_enzyme_study:'核心酶研究',general_method:'计算、综述与通用方法',cascade_component:'级联组件与应用',related_context:'关联背景与边界比较'};
const enzymePages=Object.keys(baseline.pages).filter(p=>p.startsWith('酶工程/')&&p.endsWith('类别导航.md')).sort();
for(const p of enzymePages){
  const category=p.split('/')[1];const members=e.files.flatMap(f=>f.memberships.filter(m=>m.page===p).map(m=>({f,m})));
  const original=baseline.pages[p];const summary=original.match(/## 已有资料的归纳\n([\s\S]*?)(?=\n## )/)?.[1];
  const lines=['---','type: enzyme-index',`updated: ${decisions.date}`,'evidence_basis: reviewed-local-note-body','---','',`# ${category}`,'',wiki('酶工程/00. 酶工程导航.md','返回酶工程导航')+' · '+wiki('酶工程/分类正文复核.md','正文复核记录'),'',`关联 ${members.length} 份笔记；其中核心酶研究 ${members.filter(x=>x.m.role==='core_enzyme_study').length} 份。核心研究包含发现和机制，不等于工程改造。`,'',caution,'','酶类入口与物理存放位置分离；同一原笔记不复制、不移动。下列研究类型为整篇笔记标签，具体酶在本文的角色以分区为准。'];
  for(const [role,label] of Object.entries(roleLabels)){
    const subset=members.filter(x=>x.m.role===role);if(!subset.length)continue;
    lines.push('',`## ${label}`,'');
    for(const {f,m} of subset){const r=f.body_review;lines.push(`- ${link(f.literature_id)} — **${r.study_type}**。`, `  - 本页关联：${m.theme}。`,`  - 正文判断：${r.judgment}`,`  - 依据：L${r.evidence.map(q=>q.line).join('、L')}；完整引文和SHA256见酶索引清单。`);}
  }
  if(summary)lines.push('','## 保留的专题归纳','', '> 以下为原导航的专题解释，不替代上方复核角色；原导航完整快照保存在 .maintenance/enzyme-host-before-body-review.json。','',summary.trim());
  lines.push('','## 物理主归档','', '这里仅列本文件夹原有正文，不作为核心酶类别判据。','',...plan.files.filter(f=>f.framework==='酶工程'&&f.category===category).map(f=>`- ${link(f.id)}`),'');
  writes.set(p,lines.join('\n'));
}
for(const g of h.groups){
  const members=h.files.flatMap(f=>f.assignments.filter(a=>a.group===g.key).map(a=>({f,a})));
  const lines=['---','type: cell-factory-index',`updated: ${decisions.date}`,'source_basis: reviewed-local-note-body','---','',`# ${g.name}`,'',wiki('细胞工厂/00. 细胞工厂导航.md','返回细胞工厂导航')+' · '+wiki('细胞工厂/分类正文复核.md','正文复核记录'),'',g.scope,'',`关联 ${g.notes} 份笔记；${g.production} 份含生产/全细胞转化角色。包括实验级生产与混合体系，不代表完整从头合成或成熟工艺。`,'',caution,''];
  for(const role of h.roles){const subset=members.filter(x=>x.a.role===role);if(!subset.length)continue;lines.push(`## ${role}`,'');for(const {f,a} of subset)lines.push(`- ${link(f.id)}`,`  - 模式：${a.mode}。`,`  - 正文判断：${f.body_review.judgment}`,`  - 原索引补充：${a.note}`,`  - 依据：L${f.body_review.evidence.map(q=>q.line).join('、L')}；完整引文及SHA256见细胞工厂索引清单。`);lines.push('');}
  lines.push('## 使用边界','','基因来源、克隆/蛋白表达宿主、途径验证宿主与生产宿主分开记录；未列宿主不代表论文中不存在该物种。','本轮不修改原始笔记里的数据或译名，也不将原笔记中的推测、未来工作或宣传性结论提升为已验证事实。','');
  writes.set(g.index,lines.join('\n'));
}
for(const [framework,index,rows] of [['酶工程',e,enzymePages.map(p=>({p,category:p.split('/')[1],count:e.files.filter(f=>f.memberships.some(m=>m.page===p)).length}))],['细胞工厂',h,h.groups.map(g=>({p:g.index,category:g.name,count:g.notes}))]]){
  const n=plan.files.filter(f=>f.framework===framework).length;
  const text=['---','type: framework-index',`updated: ${decisions.date}`,'---','',`# ${framework}导航`,'',wiki('00. 知识库导航.md','返回三框架总导航')+' · '+wiki(`${framework}/分类正文复核.md`,'本轮正文复核与修正'),''];
  text.push(framework==='酶工程'?'分类顺序：酶类别 → 在本文中的角色 → 研究类型（发现与机制、工程改造、计算方法、综述、多酶体系等）。不要把所有酶学研究都理解为工程改造。':'分类顺序：实际宿主/体系 → 研究角色（生产、途径验证、工具、计算设计、机制背景、综述）→ 生产模式。基因来源不作为宿主分类依据。','',`原文主归档 ${n} 份；正文分类复核 ${index.body_reviewed_notes} 份关联笔记。保留物理文件路径，跨框架通过链接连接。`, '',caution,'','| 类别 | 物理主归档 | 关联阅读 |','| --- | ---: | ---: |');
  for(const r of rows)text.push(`| ${wiki(r.p,r.category).replace('|','\\|')} | ${plan.files.filter(f=>f.framework===framework&&f.category===r.category).length} | ${r.count} |`);
  text.push('','## 统计与证据边界','','- 一篇笔记可有多个酶类或宿主入口，关联数不能相加当论文数。','- 发现与机制包含用于检验机制的突变；“工程改造”还须有功能、选择性、表达/稳定性或模块设计依据。','- 投料全细胞转化、从头合成、中间体供给、体外级联和化学终步分别标注。','- 预印本、重复版本、二手解读和研究记录仍保留，未新增独立论文身份确认。','- 本轮仅复核已有两份索引及明确修正，不声称穷尽所有笔记的潜在交叉关系。','');
  writes.set(`${framework}/00. ${framework}导航.md`,text.join('\n'));
}
for(const [framework,reviewMap] of [['酶工程',er],['细胞工厂',hr]]){
  const text=[`# ${framework}分类正文复核`,'',wiki(`${framework}/00. ${framework}导航.md`,'返回分类导航'),'',`日期：${decisions.date}。本轮 ${reviewMap.size} 份笔记的分类相关正文已审阅；并非逐篇原论文全文/SI核验。`,'','## 重要修正',''];
  for(const c of changes.filter(c=>c.framework===framework))text.push(`- ${link(c.id)}：${c.reason}`);
  text.push('','## 逐条依据','','以下摘录来自本地笔记，保留原文措辞不表示认可其所有推论。超长段落仅显示前220字符，完整原句、行号和文件SHA256存于本框架JSON索引的 body_review。','');
  for(const [id,r] of reviewMap){text.push(`### 文献 ${id}`,'',link(id),'',`${r.study_type?'研究类型：'+r.study_type+'。':''}${r.judgment}`,'');for(const q of r.evidence){text.push(`- L${q.line} 摘录：${compact(q.quote.slice(0,220))}${q.quote.length>220?'……（摘录，非全文）':''}`);}text.push('');}
  text.push('## 可重复性','','人工判断输入：.maintenance/enzyme-host-body-review.json；生成器：.maintenance/build-reviewed-enzyme-host.mjs。','原导航与原索引备份：.maintenance/enzyme-host-before-body-review.json。运行生成器的 --check 选项可校验原笔记哈希、精确正文行、审阅覆盖和输出一致性。','分类相关段落可支持初步归类；原笔记有错译、夸大或遗漏时，本轮保留疑点，不自动纠正文献数据。','');
  writes.set(`${framework}/分类正文复核.md`,text.join('\n'));
}
const unique=new Set([...er.keys(),...hr.keys()]);
const regressions=[
  ['KYNA不是独立酰胺化酶',em(16,'12').role==='related_context'&&em(16,'01').role==='core_enzyme_study'&&em(16,'07').role==='core_enzyme_study'],
  ['商用PLE是辅助组件',em(24,'13').role==='cascade_component'],
  ['NRPS预测不等于工程实验',em(111,'07').role==='general_method'],
  ['GT预测不等于工程实验',em(113,'02').role==='general_method'],
  ['氧化断肽不是水解酶',!em(166,'13')],
  ['NTF2宏环化不是TE',!em(243,'13')],
  ['实验铁卤化酶有两类入口',em(247,'04').role==='core_enzyme_study'&&em(247,'08').role==='core_enzyme_study'],
  ['RNP报告基因不等于目标萜生产',assignment(263,'bc').role==='底盘/遗传工具'],
  ['木糖研究包含FFA生产',assignment(194,'kp').role==='生产体系'],
  ['D2Cell方法与湿实验分开',assignment(264,'general').role==='计算/设计方法'&&assignment(264,'sc').role==='生产体系'],
  ['保留未确定酵母种属',assignment(181,'pending').role==='待核实'&&!assignment(181,'sc')],
  ['小檗碱末端化学步骤显式标记',!!assignment(147,'cf')&&assignment(147,'ec').mode.includes('化学')],
  ['UPO仍归非P450',em(225,'15').role==='core_enzyme_study'&&em(225,'01').role==='related_context'],
  ['没有漏掉主归档',plan.files.filter(f=>f.framework==='酶工程').every(f=>er.has(f.id))&&plan.files.filter(f=>f.framework==='细胞工厂').every(f=>hr.has(f.id))]
];
for(const [name,pass]of regressions)if(!pass)throw Error(`Regression failed: ${name}`);
for(const f of e.files)if(new Set(f.memberships.map(m=>m.page)).size!==f.memberships.length)throw Error('Duplicate enzyme membership');
for(const f of h.files)if(new Set(f.assignments.map(a=>a.group)).size!==f.assignments.length)throw Error('Duplicate host membership');
const exactQuotes=[...er.values(),...hr.values()].reduce((n,r)=>n+r.evidence.length,0);
const report={date:decisions.date,scope:decisions.scope,enzyme_reviewed:er.size,host_reviewed:hr.size,unique_notes_reviewed:unique.size,original_notes_hash_checked:plan.files.length,exact_body_quotes:exactQuotes,regression_cases:regressions.length,enzyme_changes:changes.filter(c=>c.framework==='酶工程').length,host_changes:changes.filter(c=>c.framework==='细胞工厂').length,production_unique_notes:h.production_unique_notes,changes};
writes.set('.maintenance/enzyme-host-body-review-report.json',pretty(report));
if(process.argv.includes('--check')){
  if(!existing)throw Error('Baseline missing');
  for(const [p,body]of writes)if(read(p)!==body)throw Error(`Generated output drift: ${p}`);
  for(const index of [json(ep),json(hp)])for(const f of index.files){const r=f.body_review;const target=f.source||f.target;if(digest(target)!==r.source_sha256.toUpperCase())throw Error('Hash changed');const body=read(target).split(/\r?\n/);for(const q of r.evidence)if(body[q.line-1]!==q.quote)throw Error('Quote drift');}
  console.log(JSON.stringify({...report,changes:undefined,passed:true,outputs_checked:writes.size},null,2));
}else{
  // All source/coverage checks run before creating any output.
  for(const [p,body]of writes)fs.writeFileSync(path.join(root,p),body,'utf8');
  console.log(JSON.stringify({...report,changes:undefined,outputs_written:writes.size},null,2));
}

// Read-only compiler. Emits planned moves and file contents; does not write or move files.
// Usage: node .maintenance/build-knowledge-base.mjs --part=moves|metadata|navigation|links|snapshot
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
if (fs.existsSync(path.join(root, '.maintenance/enzyme-host-body-review.json'))) {
  throw Error('Legacy migration compiler retired after body review. Use build-reviewed-enzyme-host.mjs and build-reviewed-biosynthesis-sources.ps1; do not regenerate from old classification rules.');
}
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const json = p => JSON.parse(read(p));
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(path.join(root, p))).digest('hex').toUpperCase();
const old = json('.maintenance/三框架迁移清单.json');
const review = json('.maintenance/来源分类审阅规则.json');
const enzyme = json('酶工程/酶索引清单.json');
const factory = json('细胞工厂/细胞工厂索引清单.json');
if (path.resolve(old.root) !== root) throw Error('Wrong workspace.');
const moves = [], writes = new Map(), rename = new Map();
const categories = [
  ['01. 萜类与甾体','萜类与甾体','按骨架专题区分单萜、倍半萜、二萜、三萜、四萜与甾体；糖基化等修饰另记。'],
  ['03. 聚酮类','聚酮类','芳香聚酮、蒽醌、大环内酯等用专题与属性区分，不再叠加深层文件夹。'],
  ['04. 肽类天然产物','肽类天然产物','NRP、RiPP、环二肽和其他肽统一入口；结构与装配方式分别记录，NRPS-like 非肽产物不强行归肽。'],
  ['07. 生物碱','生物碱','按具体骨架建专题；与肽类或杂合途径重叠时用交叉链接，不复制正文。'],
  ['08. 苯丙素、黄酮与相关多酚','苯丙素、黄酮与相关多酚','植物和真菌来源分别阅读；含糖修饰不自动改归糖类。'],
  ['09. 糖类、核苷与核碱基衍生物','糖类、核苷与核碱基衍生物','保留糖骨架、核苷和核碱基衍生物的区别；通路中的 PKS 不自动改变整分子主类别。'],
  ['10. 脂肪酸衍生天然产物','脂肪酸衍生天然产物','当前是 FAS/脂肪酰基相关条目的阅读入口；不再将所有其他小分子混入本类。'],
  ['11. 杂合天然产物','杂合天然产物','PKS–NRPS、聚酮–萜及其他明确杂合体系；具体装配模式另记。'],
  ['12. 其他特化代谢物与前体','其他特化代谢物与前体','暂容纳氨基酸衍生小分子、NRPS-like 非肽骨架、其他前体及功能背景；不是统一生物合成起源。'],
  ['90. 跨类别综述与通用方法','跨类别综述与通用方法','跨化合物综述、基因组/宏基因组挖掘、鉴定和计算方法；不伪装成单条天然通路。'],
  ['99. 待核实类别与文献清单','待核实类别与文献清单','化合物类别未确定、文献清单或资料不足；保持待核实，不凭题名补齐。']
];
const sourceGroups = {
  fungi: ['01. 真菌来源','真菌来源','酵母属于真菌；按本研究天然通路/母体对象，而不是异源验证宿主归类。'],
  bacteria: ['02. 细菌来源','细菌来源','蓝细菌归细菌；宏基因组预测与化学合成条目须保留原生合成者未确定的边界。'],
  plants: ['03. 植物来源','植物来源','植物通路在酵母、细菌或曲霉重构时，生产宿主另记，不改变天然来源。'],
  animals: ['04. 动物来源与母体启发','动物来源与母体启发','动物分离材料、母体来源和实际合成者分开；人工衍生物不代表动物天然通路。'],
  archaea: ['05. 古菌来源','古菌来源','古菌单列，不与细菌合并。'],
  algae: ['06. 藻类及其他真核来源','藻类及其他真核来源','仅用于明确真核藻类线索；蓝细菌不放这里，海洋来源只是生态信息。'],
  cross: ['90. 跨来源综述与工程应用','跨来源综述与工程应用','例外入口：跨来源方法、人工通路、生物催化应用或合成/活性背景，不宣称存在单一已验证天然来源。'],
  pending: ['99. 来源待核实','来源待核实','本地材料不足以确定研究通路或母体来源；不得把表达宿主、作用对象或一般背景菌作为来源。']
};
const chemical = oldCategory => ({
  '01. 萜类':'01. 萜类与甾体','02. 甾体类':'01. 萜类与甾体',
  '04. 非核糖体肽':'04. 肽类天然产物','05. 核糖体肽与 RiPPs':'04. 肽类天然产物',
  '06. 环二肽与其他肽类':'04. 肽类天然产物',
  '08. 苯丙素、黄酮与植物多酚':'08. 苯丙素、黄酮与相关多酚',
  '10. 脂肪酸与其他小分子':'12. 其他特化代谢物与前体'
}[oldCategory] ?? oldCategory);
const originById = new Map();
for (const field of ['primary_origin_groups','linked_origin_groups']) {
  for (const [group, ids] of Object.entries(review[field])) {
    for (const id of ids) {
      if (originById.has(id) && originById.get(id) !== group) throw Error(`Conflicting origin: ${id}`);
      originById.set(id, group);
    }
  }
}
const hostFolders = {
  sc:'02. 酵母底盘/01. 酿酒酵母', kp:'02. 酵母底盘/02. 毕赤酵母与 Komagataella',
  otheryeast:'02. 酵母底盘/03. 非传统酵母与黑酵母',
  ec:'01. 细菌底盘/01. 大肠杆菌', strep:'01. 细菌底盘/02. 链霉菌与其他细菌',
  asp:'03. 丝状真菌底盘/01. 曲霉', pen:'03. 丝状真菌底盘/02. 青霉与木霉',
  bc:'03. 丝状真菌底盘/03. 灰葡萄孢霉', otherfung:'03. 丝状真菌底盘/04. 其他丝状真菌',
  plant:'04. 植物与植物细胞体系/01. 植物异源表达与生产体系',
  cons:'91. 生产组织与混合体系/01. 共培养与串联生产',
  cf:'91. 生产组织与混合体系/02. 无细胞与化学生物混合体系',
  general:'90. 跨宿主综述与通用设计方法', pending:'99. 宿主与生产模式待核实'
};
const oldHostFolder = new Map(factory.groups.map(g => [g.name,hostFolders[g.key]]));
const base = p => path.posix.basename(p, '.md');
const stem = p => p.endsWith('.md') ? p.slice(0,-3) : p;
const wiki = (p,label,table=false) => `[[${stem(p)}${table ? '\\|' : '|'}${label ?? base(p)}]]`;
const page = (type,title,body) => `---\ntype: ${type}\nupdated: 2026-10-04\nevidence_status: local-note-based\n---\n\n# ${title}\n\n${body.trim()}\n`;
const put = (p,content,part='navigation') => {
  const movedSource = [...rename].find(([,to])=>to===p)?.[0];
  const baseline = movedSource ?? (fs.existsSync(path.join(root,p)) ? p : null);
  const before = baseline ? read(baseline) : null;
  writes.set(p,{path:p,before,content,part,expected_sha256:baseline ? hash(baseline) : null});
};
const move = (from,to,kind) => {
  if (from === to) return;
  if (!fs.existsSync(path.join(root,from))) throw Error(`Missing source ${from}`);
  if (fs.existsSync(path.join(root,to))) throw Error(`Existing target ${to}`);
  moves.push({source:from,target:to,sha256:hash(from),kind});
  rename.set(from,to);
};
const walk = (dir='') => fs.readdirSync(path.join(root,dir),{withFileTypes:true}).flatMap(e => {
  if (e.name === '.git') return [];
  const p = dir ? `${dir}/${e.name}` : e.name;
  return e.isDirectory() ? walk(p) : [p];
});
const allFiles = walk();
const snapshot = allFiles.map(p => ({path:p,sha256:hash(p)}));
const notes = old.files.map(f => {
  if (hash(f.target) !== f.sha256) throw Error(`Original note changed before planning: ${f.id}`);
  const body = read(f.target), title = base(f.target), override = review.overrides[f.id] ?? {};
  let compoundClass = chemical(f.chemical_category);
  if ([131,214].includes(f.id)) compoundClass = '10. 脂肪酸衍生天然产物';
  let group = originById.get(f.id);
  if (!group) group = compoundClass.startsWith('90.') ? 'cross' : 'pending';
  if (f.framework === '生物合成' && !originById.has(f.id)) throw Error(`Primary biosynthesis origin was not reviewed: ${f.id}`);
  let target = f.target;
  if (f.framework === '生物合成') target = `生物合成/${compoundClass}/${sourceGroups[group][0]}/${path.posix.basename(f.target)}`;
  if (f.framework === '细胞工厂') {
    const folder = oldHostFolder.get(f.category);
    if (!folder) throw Error(`Unmapped host ${f.id}`);
    target = `细胞工厂/${folder}/${path.posix.basename(f.target)}`;
  }
  move(f.target,target,'literature');
  const lines = body.split(/\r?\n/);
  const patterns = {
    fungi:/真菌|Aspergillus|Penicillium|Fusarium|Botrytis|Amanita|Stachybotrys|Allantophomopsis|Cortinarius|Thermomyces|Acaulium|曲霉|青霉|皮肤癣菌|蘑菇|Myrothecium/i,
    bacteria:/Streptomyces|Micromonospora|Burkholderia|Photorhabdus|Nocardia|Kutzneria|Actinomadura|Amycolatopsis|Limnoraphis|Fischerella|细菌|链霉菌|放线菌/i,
    plants:/植物|Taxus|Withania|Nicotiana|Glycyrrhiza|Andrographis|Cephalotaxus|Tripterygium|Paeonia|Arabidopsis|Marchantia|Asclepias|Cannabis|红豆杉|雷公藤|穿心莲|苦皮藤|金鸡纳/i,
    animals:/蛙皮|动物|metazoan/i, archaea:/古菌|archaea/i,
    algae:/藻|alga|Phaeodactylum|kain|KabC|DabC/i,
    cross:/本研究|综述|研究背景|研究对象|人工|工程|合成|宏基因组/,
    pending:/研究背景|本研究|核心科学问题|研究对象/
  };
  const species = review.source_species[f.id] ?? null;
  const speciesNeedle = species?.split(/[ ;；/]/)[0];
  const lineIndex = lines.findIndex(l => speciesNeedle && l.includes(speciesNeedle) && !/大学|工作单位|研究所/.test(l));
  const fallback = lines.findIndex(l => patterns[group].test(l) && !/大学|研究所|科学院|工作单位|University|College of|School of/.test(l));
  const evidenceLine = lineIndex >= 0 ? lineIndex : fallback;
  const doi = body.slice(0,4000).match(/10\.\d{4,9}\/[^\s\])<>"，；]+/)?.[0]?.replace(/[.*。,;]+$/,'') ?? null;
  return {
    id:f.id, title, previous_path:f.target, path:target, framework:f.framework,
    category:target.split('/')[1], chemical_category:compoundClass,
    chemical_subtype:f.chemical_category.replace(/^\d+\. /,''),
    source_group:group, source_group_name:sourceGroups[group][1], source_species:species,
    source_scope:override.scope ?? (group === 'cross' ? '跨来源方法、综述或工程应用' : group === 'pending' ? '来源待核实' : '本地笔记中的通路/母体研究对象'),
    source_note:override.note ?? '',
    source_evidence: evidenceLine < 0 ? null : {file:target,line:evidenceLine+1,excerpt:lines[evidenceLine].slice(0,240)},
    source_evidence_status:'local-note-based; original paper/SI and taxonomy not comprehensively reverified',
    doi_from_local_note:doi, sha256:f.sha256, primary_focus:f.reason,
    enzyme_memberships:enzyme.files.find(e=>e.literature_id===f.id)?.memberships ?? [],
    host_assignments:factory.files.find(e=>e.id===f.id)?.assignments ?? []
  };
});
const byId = new Map(notes.map(n=>[n.id,n]));
const oldCategoryPages = {
  '01. 萜类':'生物合成/01. 萜类与甾体/00. 类别导航.md',
  '02. 甾体类':'生物合成/知识专题/甾体类阅读索引.md',
  '04. 非核糖体肽':'生物合成/知识专题/肽类-非核糖体肽阅读索引.md',
  '05. 核糖体肽与 RiPPs':'生物合成/知识专题/肽类-RiPPs 阅读索引.md',
  '06. 环二肽与其他肽类':'生物合成/知识专题/肽类-环二肽与其他肽阅读索引.md',
  '08. 苯丙素、黄酮与植物多酚':'生物合成/08. 苯丙素、黄酮与相关多酚/00. 类别导航.md',
  '10. 脂肪酸与其他小分子':'生物合成/12. 其他特化代谢物与前体/00. 类别导航.md'
};
for (const [folder,to] of Object.entries(oldCategoryPages)) move(`生物合成/${folder}/00. 类别导航.md`,to,'category-index');
for (const group of factory.groups) {
  const oldFolder = `细胞工厂/${group.name}`, newFolder = `细胞工厂/${hostFolders[group.key]}`;
  for (const p of allFiles.filter(p=>p.startsWith(`${oldFolder}/`))) {
    if (!rename.has(p)) move(p,`${newFolder}/${p.slice(oldFolder.length+1)}`,'host-index');
  }
}
const replacements = [...rename].flatMap(([from,to])=>[[from,to],[stem(from),stem(to)]])
  .sort((a,b)=>b[0].length-a[0].length);
// Exact wiki targets only. Protect historical paths, external URLs and scientific prose.
const rewriteLinks = text => text.replace(/\[\[([^\]|]+)(\|[^\]]*)?\]\]/g,(whole,target,alias='')=>{
  const escaped = target.endsWith('\\'), clean = escaped ? target.slice(0,-1) : target;
  const [name,...anchor] = clean.split('#');
  const mapped = rename.get(name) ?? rename.get(`${name}.md`);
  if (!mapped) return whole;
  return `[[${name.endsWith('.md') ? mapped : stem(mapped)}${anchor.length ? '#'+anchor.join('#') : ''}${escaped ? '\\' : ''}${alias}]]`;
});
for (const p of allFiles.filter(p=>p.endsWith('.md'))) {
  if (old.files.some(f=>f.target===p)) continue; // All original literature notes have no wiki targets to rewrite.
  const before = read(p), content = rewriteLinks(before), target = rename.get(p) ?? p;
  if (content !== before || target !== p) {
    // At move time the destination will contain the original bytes; patch against those bytes.
    writes.set(target,{path:target,before,content,part:'links',expected_sha256:hash(p)});
  }
}
for (const file of enzyme.files) {
  const n = byId.get(file.literature_id);
  file.source = n.path; file.primary_category = n.category;
}
enzyme.updated = '2026-10-04';
enzyme.source_preservation = '正文内容不变；source 指向当前归档，previous_source 是历史路径。';
for (const group of factory.groups) {
  group.previous_index = group.index;
  group.index = `细胞工厂/${hostFolders[group.key]}/00. 类别导航.md`;
  group.host_class = hostFolders[group.key].split('/')[0];
}
for (const file of factory.files) {
  const n = byId.get(file.id); file.target=n.path; file.primary_category=n.category;
  for (const a of file.assignments) a.index=factory.groups.find(g=>g.key===a.group).index;
}
factory.source_preservation='正文内容不变；target/index 为当前路径，previous_target/previous_index 保留历史。';
for (const n of notes) n.host_assignments = factory.files.find(f=>f.id===n.id)?.assignments ?? [];
const serialize = obj => JSON.stringify(obj,null,2)+'\n';
put('酶工程/酶索引清单.json',serialize(enzyme),'metadata');
put('细胞工厂/细胞工厂索引清单.json',serialize(factory),'metadata');
const current = {
  schema_version:2,root,date:'2026-10-04',original_manifest:'.maintenance/三框架迁移清单.json',
  original_literature_notes:old.original_literature_notes, additional_interpretation_notes:1,
  evidence_basis:review.basis,
  counts:Object.fromEntries(['生物合成','酶工程','细胞工厂'].map(f=>[f,notes.filter(n=>n.framework===f).length])),
  files:notes.map(n=>({id:n.id,previous_target:n.previous_path,target:n.path,framework:n.framework,
    category:n.category,chemical_category:n.chemical_category,source_group:n.source_group,sha256:n.sha256,reason:n.primary_focus}))
};
put('.maintenance/知识库当前归档清单.json',serialize(current),'metadata');
put('.maintenance/知识库重构迁移清单.json',serialize({schema_version:1,root,date:'2026-10-04',moves}),'metadata');
put('.maintenance/知识库重构前快照.json',serialize({root,date:'2026-10-04',files:snapshot}),'snapshot');
put('生物合成/生物合成分类索引.json',serialize({schema_version:1,date:'2026-10-04',basis:review.basis,
  count_unit:'note files, not unique publications or fully verified papers',categories,source_groups:sourceGroups,files:notes}),'metadata');

const caution = '> 分类依据本地笔记的初步整理，不等于原始论文全文/SI 精读或通路已完整验证。综述、预印本、二手解读、人工衍生物和活性背景按原性质保留。';
const relation = n => {
  const enz = n.enzyme_memberships.filter(m=>m.role==='core_enzyme_study').map(m=>wiki(m.page,path.posix.basename(path.posix.dirname(m.page))));
  const hosts = n.host_assignments.map(a=>`${wiki(a.index,path.posix.basename(path.posix.dirname(a.index)))}（${a.role}）`);
  const bits=[];
  if (enz.length) bits.push('酶：'+[...new Set(enz)].join('、'));
  if (hosts.length) bits.push('宿主/体系：'+[...new Set(hosts)].join('、'));
  return bits.length ? '\n  - '+bits.join('；')+'。' : '';
};
const item = n => `- ${wiki(n.path,n.title)} — ${n.chemical_subtype}；${n.source_scope}。${n.source_note ? ' '+n.source_note : ''}${relation(n)}`;
const lists = (rows,framework) => {
  const primary=rows.filter(n=>n.framework===framework), other=rows.filter(n=>n.framework!==framework);
  return `## 本框架主归档\n\n${primary.length ? primary.map(item).join('\n') : '正文主归其他框架，本页不复制。'}\n\n## 跨框架关联阅读\n\n${other.length ? other.map(item).join('\n') : '当前无跨框架条目。'}`;
};
const categorySummary=[];
for (const [folder,label,scope] of categories) {
  const members=notes.filter(n=>n.chemical_category===folder);
  if (!members.length) continue;
  const primary=members.filter(n=>n.framework==='生物合成');
  const sourceRows=[];
  for (const [key,[sourceFolder,sourceLabel,sourceScope]] of Object.entries(sourceGroups)) {
    const rows=members.filter(n=>n.source_group===key);
    if (!rows.length) continue;
    const index=`生物合成/${folder}/${sourceFolder}/00. 来源导航.md`;
    put(index,page('biosynthesis-source-index',`${label} · ${sourceLabel}`,
      `${wiki(`生物合成/${folder}/00. 类别导航.md`,'返回化合物类别')} · ${wiki('生物合成/00. 生物合成导航.md','生物合成总导航')}\n\n${sourceScope}\n\n主归档 ${rows.filter(n=>n.framework==='生物合成').length} 个笔记，关联 ${rows.length} 个笔记（含主归档，不能跨页相加当作论文总数）。\n\n${caution}\n\n${lists(rows,'生物合成')}\n\n## 分类证据与下一步\n\n详细来源范围、具体物种（有记录者）、原文行号、DOI 候选与宿主角色见 ${wiki('生物合成/生物合成分类索引.json','分类索引清单')}。原笔记中的强结论未在本轮重新背书；先核查天然来源/原生证据，再分析反应顺序与瓶颈。`));
    sourceRows.push(`| ${wiki(index,sourceLabel,true)} | ${rows.filter(n=>n.framework==='生物合成').length} | ${rows.length} |`);
  }
  const subtypeRows = [...new Set(members.map(n=>n.chemical_subtype))].map(sub=>{
    const rows=members.filter(n=>n.chemical_subtype===sub);
    return `### ${sub}\n\n${rows.map(n=>`- ${wiki(n.path,n.title)} — ${n.source_group_name}；主归 ${n.framework}。`).join('\n')}`;
  });
  put(`生物合成/${folder}/00. 类别导航.md`,page('biosynthesis-category',label,
    `${wiki('生物合成/00. 生物合成导航.md','返回生物合成')} · ${wiki('00. 知识库导航.md','三框架总导航')}\n\n${scope}\n\n本类主归档 ${primary.length} 个，关联 ${members.length} 个笔记（含主归档）；每篇正文只有一个存放位置。\n\n${caution}\n\n## 按天然来源/研究范围浏览\n\n| 来源入口 | 主归档 | 关联笔记（含主归档） |\n| --- | ---: | ---: |\n${sourceRows.join('\n')}\n\n## 跨来源的骨架/装配专题阅读\n\n下列名称沿用历史化合物索引，仅作阅读筛选；肽类的结构和装配方式、杂合来源仍需分别记录。\n\n${subtypeRows.join('\n\n')}\n\n## 连接通路、酶与宿主\n\n来源子页已链接相关酶页与实际宿主/体系页，并保留“生产、工具、途径验证、背景”等角色。${wiki('00. 知识连接工作台.md','知识连接工作台')}提供全库交叉检索。`));
  categorySummary.push(`| ${wiki(`生物合成/${folder}/00. 类别导航.md`,label,true)} | ${primary.length} | ${members.length} |`);
}
put('生物合成/00. 生物合成导航.md',page('framework-index','生物合成导航',
  `${wiki('00. 知识库导航.md','返回总导航')}\n\n目录按 **化合物类别 → 天然来源类群 → 文献** 组织。亚类、骨架和具体物种通过专题与分类属性检索，不再叠加深目录。主归档 108 个笔记；以下关联阅读覆盖另外两个框架，正文不重复。\n\n| 化合物类别 | 主归档 | 关联笔记（含主归档） |\n| --- | ---: | ---: |\n${categorySummary.join('\n')}\n\n## 来源规则\n\n- 天然通路来源、分离材料、酶来源、表达宿主、生产宿主各是不同信息。\n- 跨来源综述、人工通路和合成/活性背景用例外入口；不强行指定天然来源。\n- 真菌黄酮保留真菌来源，不因“黄酮”默认归植物；蓝细菌属于细菌，古菌单列。\n- 来源未知进入待核实；已识别类群但未确认具体物种时，物种字段留空/待核对。\n\n${caution}\n\n## 已有专题与维护\n\n${allFiles.filter(p=>p.startsWith('生物合成/知识专题/')&&p.endsWith('.md')).map(p=>'- '+wiki(p)).join('\n')}\n- ${wiki('生物合成/知识专题/甾体类阅读索引.md','甾体类阅读索引')}\n- ${wiki('生物合成/知识专题/肽类-非核糖体肽阅读索引.md','非核糖体肽阅读索引')}\n- ${wiki('生物合成/知识专题/肽类-RiPPs 阅读索引.md','RiPPs 阅读索引')}\n- ${wiki('生物合成/知识专题/肽类-环二肽与其他肽阅读索引.md','环二肽与其他肽阅读索引')}\n- ${wiki('生物合成/生物合成分类索引.json','来源、骨架与证据分类索引')}\n- ${wiki('00. 待核实与阅读队列.md','待核实与阅读队列')}\n- ${wiki('00. 知识库使用与维护.md','使用与维护规则')}\n\n旧专题的 11 个未创建概念链接保持原状，不以未经核查的概念补写制造完成假象。`));

const hostParents=[...new Set(Object.values(hostFolders).map(f=>f.split('/')[0]))];
const hostSummary=[];
for (const parent of hostParents) {
  const groups=factory.groups.filter(g=>g.host_class===parent);
  if (!groups.some(g=>g.index.includes('/'+parent+'/'))) continue;
  const rows=groups.map(g=>`| ${wiki(g.index,path.posix.basename(path.posix.dirname(g.index)),true)} | ${g.primary_notes} | ${g.notes} |`);
  put(`细胞工厂/${parent}/00. 底盘导航.md`,page('host-class-index',parent.replace(/^\d+\. /,''),
    `${wiki('细胞工厂/00. 细胞工厂导航.md','返回细胞工厂')}\n\n${parent.startsWith('91.') ? '此处按生产组织方式分类，不是宿主类群；各实际宿主仍有交叉入口。' : '按实际生产/转化或底盘研究对象分类；天然通路和酶来源不替代生产宿主身份。'}\n\n| 入口 | 主归档 | 关联笔记（含主归档） |\n| --- | ---: | ---: |\n${rows.join('\n')}\n\n${wiki('细胞工厂/专题导航/00. 按工程问题阅读.md','按工程问题阅读')}\n\n${caution}`));
  hostSummary.push(`- ${wiki(`细胞工厂/${parent}/00. 底盘导航.md`,parent.replace(/^\d+\. /,''))}`);
}
const allHostRows=factory.groups.map(g=>`| ${wiki(g.index,hostFolders[g.key],true)} | ${g.primary_notes} | ${g.notes} |`);
put('细胞工厂/00. 细胞工厂导航.md',page('framework-index','细胞工厂导航',
  `${wiki('00. 知识库导航.md','返回总导航')}\n\n按 **生产底盘类群 → 具体宿主** 分类，主归档 42 个笔记。酵母和丝状真菌是工程底盘导航分组，不是宣称两者构成完整系统发育树。\n\n## 底盘与补充体系\n\n${hostSummary.join('\n')}\n- ${wiki(factory.groups.find(g=>g.key==='general').index,'跨宿主综述与通用设计方法')}\n- ${wiki(factory.groups.find(g=>g.key==='pending').index,'宿主与生产模式待核实')}\n\n| 具体入口 | 主归档 | 关联笔记（含主归档） |\n| --- | ---: | ---: |\n${allHostRows.join('\n')}\n\n## 工程问题与证据边界\n\n${wiki('细胞工厂/专题导航/00. 按工程问题阅读.md','底盘工具、通路重构、前体辅因子、表达区室化、运输耐受与培养放大')}\n\n- 来源生物、表达宿主、生产宿主、物种/菌株分别记录；表达纯化酶不算该化合物的生产工厂。\n- 从头合成、喂前体转化、途径验证和宿主工具分别标记；中间体不等于完整终产物。\n- 共培养、同种多菌株、串联和无细胞混合是组织方式，不与菌种处于同一分类轴。\n- Pichia pastoris 旧名不无条件等同任一 Komagataella 物种；按原论文菌株核对。\n\n${caution}\n\n## 调研报告与追溯\n\n${allFiles.filter(p=>p.startsWith('细胞工厂/调研报告/')&&p.endsWith('.md')).map(p=>'- '+wiki(p)).join('\n')}\n\n报告中的滴度、底盘优劣与知识产权判断未在本轮重新核查。\n\n${wiki('细胞工厂/细胞工厂索引清单.json','宿主与生产角色索引')} · ${wiki('00. 知识连接工作台.md','知识连接工作台')}`));

const enzymeQuestions=[
  ['酶发现与功能线索',/发现|挖掘|表征|鉴定|功能|筛选|预测/],
  ['催化机制与选择性',/机制|机理|结构|选择性|立体|催化|构象/],
  ['工程改造与设计',/工程|改造|定向进化|设计|突变|重设计|重定位|交换/],
  ['生物催化应用与级联',/应用|酶法合成|酶促合成|化学酶|级联|一锅|全条外|全条外|无细胞/]
];
const enzymeSections=enzymeQuestions.map(([label,rx])=>{
  const rows=notes.filter(n=>n.enzyme_memberships.length && rx.test(n.title));
  return `## ${label}\n\n题名线索匹配 ${rows.length} 个笔记，允许一文多入口；是否实际完成改造/验证需读正文和原文。\n\n${rows.map(n=>`- ${wiki(n.path,n.title)} — ${n.enzyme_memberships.map(m=>wiki(m.page,path.posix.basename(path.posix.dirname(m.page)))+'（'+m.role+'）').join('；')}。`).join('\n') || '当前未匹配，后续人工补充。'}`;
});
put('酶工程/专题导航/00. 按研究问题阅读.md',page('enzyme-question-index','按酶研究问题阅读',
  `${wiki('酶工程/00. 酶工程导航.md','返回酶工程')}\n\n这是题名筛选生成的阅读入口，不是科学结论或研究阶段的人工定论。酶发现、功能机制和应用不自动算酶工程；source/role 与原有酶清单保留。\n\n${enzymeSections.join('\n\n')}`));
const enzymeNav=read('酶工程/00. 酶工程导航.md');
put('酶工程/00. 酶工程导航.md',rewriteLinks(enzymeNav)+`\n## 按研究问题与来源阅读\n\n- ${wiki('酶工程/专题导航/00. 按研究问题阅读.md','发现与功能、机制、工程改造、应用与级联')}\n- ${wiki('00. 知识连接工作台.md','化合物—来源—酶—宿主连接工作台')}\n\n酶类别保持主要入口，不按来源再复制一套目录。天然通路来源、酶来源与表达宿主不同；来源属性需核对具体酶/序列，不能从产物或测试菌反推。本框架名称沿用“酶工程”，收录范围包括酶发现、机制与生物催化。\n`);
const hostQuestions=[
  ['底盘工具与遗传操作',/CRISPR|Cre-lox|基因组编辑|表达载体|启动子|重组技术|平台/],
  ['通路重构与模块组织',/重构|途径|通路|从头|多酶|共培养|联合体|模块|生物合成/],
  ['前体、碳源与辅因子',/前体|辅因子|碳源|甲醇|木糖|辅酶|硫同化|β-氧化|代谢工程/],
  ['表达、区室化与调控',/表达|调控|转录|蛋白|启动子|区室|定位|伴侣/],
  ['运输、耐受与培养放大',/运输|转运|耐受|毒性|培养|发酵|规模|高产|高效|生产/]
];
put('细胞工厂/专题导航/00. 按工程问题阅读.md',page('host-question-index','按细胞工厂工程问题阅读',
  `${wiki('细胞工厂/00. 细胞工厂导航.md','返回细胞工厂')}\n\n题名关键词只筛选阅读线索，不保证论文已解决该工程问题。生产角色沿用已有人工作用标记；各组不可相加当作独立论文数。\n\n${hostQuestions.map(([label,rx])=>{
    const rows=notes.filter(n=>n.host_assignments.length && rx.test(n.title));
    return `## ${label}\n\n${rows.map(n=>'- '+wiki(n.path,n.title)+' — '+n.host_assignments.map(a=>wiki(a.index,path.posix.basename(path.posix.dirname(a.index)))+'（'+a.role+'；'+a.mode+'）').join('；')+'。').join('\n') || '当前未匹配，不填空白案例。'}`;
  }).join('\n\n')}`));

const pending=notes.filter(n=>n.source_group==='pending');
put('00. 待核实与阅读队列.md',page('verification-queue','待核实与阅读队列',
  `${wiki('00. 知识库导航.md','返回总导航')}\n\n以下 ${pending.length} 个笔记的天然通路/母体来源还不足以确定。不是无效文献，也不代表已经完整精读；原归档与其他索引仍可使用。\n\n${lists(pending,'生物合成')}\n\n## 核查顺序\n\n1. 先读原论文的研究对象和产生菌/植物材料，区分分离来源、实际合成者与表达宿主。\n2. 找到原生遗传/代谢物证据，记录 DOI、物种/菌株、图号和来源段落。\n3. 区分纯酶、异源验证、全细胞转化和从头生产；未验证不补齐。\n4. 更新分类索引，再更新导航；不能仅凭关键词把资料提升为通路证明。`));
put('00. 知识连接工作台.md',page('cross-framework-workbench','知识连接工作台',
  `${wiki('00. 知识库导航.md','返回总导航')}\n\n**化合物/骨架 → 天然来源与通路 → 反应/酶 → 实际生产宿主 → 工程问题 → 实验证据**。本页只连接已存在资料，不新写未经核查的机理结论。\n\n## 从不同问题进入\n\n- 查某类化合物如何形成：${wiki('生物合成/00. 生物合成导航.md','化合物与来源导航')}。\n- 查酶如何催化或改造：${wiki('酶工程/00. 酶工程导航.md','酶体系导航')}、${wiki('酶工程/专题导航/00. 按研究问题阅读.md','酶研究问题导航')}。\n- 选底盘/比较模块：${wiki('细胞工厂/00. 细胞工厂导航.md','生产宿主导航')}、${wiki('细胞工厂/专题导航/00. 按工程问题阅读.md','工程问题导航')}。\n- 先补证据：${wiki('00. 待核实与阅读队列.md','来源待核实队列')}。\n\n## 全库关联记录\n\n${notes.map(n=>`- ${wiki(n.path,n.title)} — ${wiki(`生物合成/${n.chemical_category}/00. 类别导航.md`,n.chemical_category.replace(/^\d+\. /,''))} / ${wiki(`生物合成/${n.chemical_category}/${sourceGroups[n.source_group][0]}/00. 来源导航.md`,n.source_group_name)}；主归 ${n.framework}。${relation(n)}`).join('\n')}\n\n## 核查而非推断\n\n证据状态、来源引用行、DOI 候选、具体物种（有记录者）、酶关联角色及生产方式在 ${wiki('生物合成/生物合成分类索引.json','结构化分类清单')} 中保存。一个链接不等于通路已全解析；一个生产宿主关联不等于完整终产物从头生产。`));
put('00. 知识库使用与维护.md',page('knowledge-base-maintenance','知识库使用与维护',
  `${wiki('00. 知识库导航.md','返回首页')}\n\n## 三个稳定入口\n\n- 生物合成：化合物类别 → 天然来源类群；骨架/装配方式用专题，不把糖苷全部归糖类。\n- 酶工程：酶体系与研究问题；包括发现和机制，只有明确改造证据才称工程。\n- 细胞工厂：生产底盘类群 → 具体宿主；培养组织方式另列补充入口。\n\n每篇正文只放一处。多类别、多酶、多宿主用链接和属性，不复制正文。主归档以论文主要问题为依据，可以人工调整。原始笔记、文件名、DOI 文本与图片地址本轮保持不变。\n\n## 记录字段\n\n化合物类别与骨架、天然通路来源、分离材料、实际合成者、酶来源/序列、表达宿主、生产宿主/菌株、生产方式、研究重点、DOI/来源位置与阅读状态。未知留空或待核实；不得将来源、宿主和作用对象混用。\n\n## 新增文献\n\n1. 用 ${wiki('生物合成/模板/文献笔记模板.md','文献笔记模板')} 建立笔记，写明来源类型与阅读边界。\n2. 按主要问题选择唯一主归档；生物合成资料再按化合物类别和天然来源选择目录。跨来源/人工应用用例外入口。\n3. 在已有专题页增加链接，记录参与反应的酶和实际生产宿主，区分背景/验证/生产。\n4. 更新当前归档清单和结构化分类索引；JSON 不是自动动态检索插件，不会自行吸收新笔记。\n5. 运行 \`.maintenance/validate-three-frameworks.ps1\` 和 \`.maintenance/validate-knowledge-base.ps1\`，查看 hash、覆盖和链接结果。增加/改写文献时须明确更新相应基线。\n\n## 本轮可重复性与历史\n\n- \`.maintenance/来源分类审阅规则.json\` 保存人工来源初筛与例外规则。\n- \`.maintenance/build-knowledge-base.mjs\` 是本轮从旧三框架快照编译迁移计划的只读脚本，不是可以在完成后盲目重跑的同步器。\n- \`.maintenance/知识库重构迁移清单.json\` 保存每次移动的明确路径和 SHA-256；移动脚本先校验范围与冲突。\n- \`.maintenance/知识库当前归档清单.json\` 指向当前位置；旧三框架清单和历史化合物清单保持历史快照，不应作为当前路径使用。\n- \`.maintenance/知识库重构前快照.json\` 用于检查范围外文件、原始专题和报告未受意外修改。\n\n本轮没有新增插件、Git 提交或推送，也没有逐篇重新精读原论文/SI。`));
put('生物合成/模板/文献笔记模板.md',`---\ntype: literature-note\ntitle: ""\ndoi: ""\nsource_type: "待核实：原始研究/综述/预印本/二手解读"\nreading_status: "未读原文"\nprimary_framework: "待选择"\ncompound_class: "待核实"\nscaffold: "待核实"\nnatural_pathway_origin: []\nisolation_source: "待核实"\nactual_producer: "待核实"\nenzyme_source: []\nenzyme_system: []\nexpression_host: []\nproduction_host: []\nstrain: []\nproduction_mode: "待核实：从头/喂前体/验证/无细胞/混合"\nresearch_focus: []\nevidence_status: "待核实"\n---\n\n# 文献标题\n\n## 原始来源\n\nDOI、原文/附件位置；具体页码、图号或表号。\n\n## 研究问题与分类依据\n\n说明主归档理由。区分天然来源、酶来源、表达宿主和生产宿主。\n\n## 已确认 Observation\n\n仅记录材料支持的观察。写明纯酶/原生/异源证据、产物身份和检测方法；缺信息不编造。\n\n## Interpretation 与局限\n\n解释与观察分开；标明推断、假设、尚缺的原文或 SI。\n\n## 与已有知识的连接\n\n链接具体化合物/通路专题、酶页、宿主页；不复制文献。\n\n## 下一步核查或分析\n\n列最小必要核查，不把生成笔记等同完成精读。\n`);
put('00. 知识库导航.md',page('knowledge-base-home','SynBioPath：天然产物研究知识库',
  `三个研究框架、一份文献正文、多维交叉阅读。\n\n| 框架 | 主归档笔记 | 分类依据 |\n| --- | ---: | --- |\n| ${wiki('生物合成/00. 生物合成导航.md','生物合成',true)} | 108 | 化合物类别 → 天然来源类群 |\n| ${wiki('酶工程/00. 酶工程导航.md','酶工程',true)} | 117 | 酶体系/家族 → 功能机制与工程专题 |\n| ${wiki('细胞工厂/00. 细胞工厂导航.md','细胞工厂',true)} | 42 | 生产底盘类群 → 具体宿主 |\n\n合计 **267 个文献相关笔记文件**，包括综述、预印本、二手解读、疑似重复版本和文献清单，不等于 267 篇去重的原始论文。原有知识专题与两份调研报告另行保留。\n\n## 常用入口\n\n- ${wiki('00. 知识连接工作台.md','化合物—来源—酶—宿主连接工作台')}\n- ${wiki('00. 待核实与阅读队列.md','待核实与阅读队列')}\n- ${wiki('00. 知识库使用与维护.md','使用、分类与维护规则')}\n- ${wiki('生物合成/模板/文献笔记模板.md','新增文献模板')}\n\n## 目录示意\n\n\`\`\`text\n生物合成/化合物类别/天然来源类群/文献笔记.md\n酶工程/酶体系类别/文献笔记.md\n酶工程/专题导航/按研究问题阅读.md\n细胞工厂/生产底盘类群/具体宿主/文献笔记.md\n细胞工厂/生产组织与混合体系/共培养或无细胞等/\n\`\`\`\n\n不同框架之间用链接连接，不复制正文。来源子页保留在其他框架存放的相关酶/生产文献。\n\n## 证据与本轮范围\n\n${caution}\n\n原始 267 个笔记正文不改写，文件名、引用和图片地址保留。来源分类是本地材料支持的初筛，未逐篇核查原论文/SI；未知不补齐。原萜专题 11 个未创建概念链接保留。软件教程、实验细节与科研网址等非文献资料仍在原位置。\n\n## 当前清单与历史\n\n- ${wiki('生物合成/生物合成分类索引.json','当前化合物、来源、酶与宿主关联清单')}\n- ${wiki('.maintenance/知识库当前归档清单.json','当前正文归档与 SHA-256 清单')}\n- ${wiki('.maintenance/知识库重构迁移清单.json','本轮移动记录')}\n- ${wiki('.maintenance/三框架迁移清单.json','旧三框架历史快照')}\n\n旧清单中的路径是历史状态，不代表当前位置。仅本地整理，没有 Git 提交或推送。`));

const workspacePath='.obsidian/workspace.json';
if (fs.existsSync(path.join(root,workspacePath))) {
  const visit = value => {
    if (typeof value === 'string') return rename.get(value) ?? value;
    if (Array.isArray(value)) return value.map(visit);
    if (value && typeof value === 'object') return Object.fromEntries(Object.entries(value).map(([k,v])=>[k,visit(v)]));
    return value;
  };
  put(workspacePath,serialize(visit(json(workspacePath))),'metadata');
}
if (new Set(moves.map(m=>m.target.toLowerCase())).size !== moves.length) throw Error('Duplicate move targets.');
if (notes.length !== 267) throw Error('Unexpected corpus count.');
const part=process.argv.find(a=>a.startsWith('--part='))?.slice(7) ?? 'summary';
const summary={root,literature:notes.length,primary_counts:current.counts,moves:moves.length,
  pending_primary_biosynthesis:pending.filter(n=>n.framework==='生物合成').map(n=>n.id),
  source_counts:Object.fromEntries(Object.keys(sourceGroups).map(g=>[g,notes.filter(n=>n.source_group===g).length])),
  writes:writes.size,parts:['moves','metadata','navigation','links','snapshot']};
if (part === 'summary') process.stdout.write(serialize(summary));
else if (part === 'moves') process.stdout.write(serialize({summary,moves}));
else process.stdout.write(serialize({summary,writes:[...writes.values()].filter(w=>w.part===part)}));

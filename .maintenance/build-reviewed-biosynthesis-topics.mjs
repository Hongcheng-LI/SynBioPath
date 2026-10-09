import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const check = process.argv.includes('--check');
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const json = p => JSON.parse(read(p).replace(/^\uFEFF/, ''));
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex').toUpperCase();
const plan = json('.maintenance/三框架迁移清单.json');
if (path.resolve(plan.root).toLowerCase() !== root.toLowerCase()) throw Error('Wrong vault');
const sourceIndex = json('生物合成/来源分类索引清单.json');
const review = json('.maintenance/biosynthesis-topic-body-review.json');
const enzyme = json('酶工程/酶索引清单.json');
const factory = json('细胞工厂/细胞工厂索引清单.json');
const topics = [
  { id: 1, name: '发现与途径定位', question: '如何找到分子、BGC 或非成簇基因，并定位真实中间体与步骤？', boundary: '包括基因组挖掘、组学、化学捕获和结构鉴定；计算预测、关联与实验重构分别标注。' },
  { id: 2, name: '前体供给与骨架构建', question: '从哪些构件出发，如何延伸、缩合、环化、释放并决定骨架立体化学？', boundary: '包括 TPS、PKS、NRPS、CDPS、NRPS-like 和 RiPP 前体组织；前体甲基化不自动归为后修饰。' },
  { id: 3, name: '后修饰与骨架重塑', question: '骨架形成后如何氧化、还原、糖基化、甲基化、卤化、交联、重排或裂解？', boundary: '包括装配线加工与成熟反应；明确酶促、自发反应和尚未确证的生物发生。' },
  { id: 4, name: '多单元组装与路径分支', question: '多个构件如何拼接，共同中间体如何分流，不同来源的路径如何比较？', boundary: '讨论化学组装、代谢网络与分支；不把药物联合协同当作分子拼接，也不把旁路自动称为转录调控。' },
  { id: 5, name: '调控与生理生态功能', question: '何时、何地、为何产生这些分子，如何组织反应并参与适应、防御和相互作用？', boundary: '包括转录、酶抑制、支架/区室化、环境与生态；预测、关联和直接因果证据分开。' },
  { id: 6, name: '活性、靶标与应用', question: '分子作用于什么靶标，结构差异如何影响效应，可用于什么应用？', boundary: '活性测试不自动等于阳性，靶标研究不自动等于途径解析，天然与化学合成类似物分开。' }
];
const topicById = new Map(topics.map(t => [t.id, t]));
const sourceById = new Map(sourceIndex.records.map(r => [r.id, r]));
const bios = plan.files.filter(f => f.framework === '生物合成');
const reviewed = new Map();
for (const row of review.rows) {
  if (row.length !== 8 || reviewed.has(row[0])) throw Error(`Invalid/duplicate review row ${row[0]}`);
  reviewed.set(row[0], row);
}
if (reviewed.size !== bios.length) throw Error('Review coverage mismatch');
// Check every original file before any output, including the two untouched frameworks.
for (const f of plan.files) {
  if (hash(fs.readFileSync(path.join(root, f.target))) !== f.sha256) throw Error(`Original note changed: ${f.id}`);
}
const records = bios.map(f => {
  const row = reviewed.get(f.id), s = sourceById.get(f.id);
  if (!row || !s || s.note_sha256 !== f.sha256) throw Error(`Missing/stale decision ${f.id}`);
  const [id, primary, secondary, evidenceLines, focus, judgment, studyRole, caution] = row;
  const memberships = primary ? [primary, ...secondary] : [];
  if ((primary === 0 && (id !== 158 || secondary.length)) || new Set(memberships).size !== memberships.length || memberships.some(t => !topicById.has(t))) throw Error(`Invalid topics ${id}`);
  const lines = read(f.target).split(/\r?\n/);
  const evidence = evidenceLines.map(line => {
    const quote = lines[line - 1];
    if (!Number.isInteger(line) || !quote?.trim() || /^\s*(#|!\[)/.test(quote)) throw Error(`Invalid body evidence ${id}:${line}`);
    return { line, quote };
  });
  if (!evidence.length) throw Error(`No body evidence ${id}`);
  return {
    id, target: f.target, title: path.basename(f.target, '.md'), category: f.category,
    source_group: s.source_group, source_taxon_or_scope: s.source_taxon_or_scope,
    source_role: s.source_role, source_caution: s.review_flag,
    primary_topic: primary, secondary_topics: secondary, topics: memberships,
    focus, judgment, study_role: studyRole, caution,
    evidence_level: 'local-note-body; original-paper-not-verified',
    note_sha256: f.sha256, evidence,
    enzyme_links: (enzyme.files.find(e => e.literature_id === id)?.memberships ?? []).map(m => ({ page: m.page, role: m.role })),
    factory_links: (factory.files.find(e => e.id === id)?.assignments ?? []).map(a => ({ page: a.index, role: a.role, note: a.note }))
  };
});
const categories = [...new Set(records.map(r => r.category))].sort();
const sources = ['真菌来源', '细菌来源', '植物来源', '动物来源', '古菌来源', '宏基因组来源（产生者未定）', '多来源或生态体系', '跨来源与通用方法', '来源待核实'];
if (records.some(r => !sources.includes(r.source_group))) throw Error('Unknown source group');
const topicPath = t => `生物合成/研究专题/${String(t.id).padStart(2, '0')}. ${t.name}.md`;
const categoryPath = c => `生物合成/${c}/00. 研究专题导航.md`;
const wiki = (p, label) => `[[${p.replace(/\.md$/, '')}|${label}]]`;
const escapeCell = s => String(s).replaceAll('|', '／').replaceAll('\n', ' ');
const counts = t => ({ primary: records.filter(r => r.primary_topic === t).length, linked: records.filter(r => r.topics.includes(t)).length });
const outputs = new Map();
const add = (p, type, text) => {
  if (fs.existsSync(path.join(root, p)) && !read(p).includes(`type: ${type}\n`)) throw Error(`Unrecognized generated page ${p}`);
  outputs.set(p, `---\ntype: ${type}\nupdated: ${review.date}\n---\n\n${text.trim()}\n`);
};
const scope = '> 分类依据本地文献笔记的相关正文，而不是标题；未逐篇核查原始论文/SI。这里是文献导航，不是已经综合验证的机制结论。主专题表示阅读重点，其他专题表示正文支持的关联；同一原文不复制。';
function item(r, topic) {
  const tag = r.primary_topic === topic ? '主专题' : '关联专题';
  const evidence = r.evidence.map(e => `L${e.line}`).join('、');
  const result = [`- ${wiki(r.target, r.focus)} — ${tag}；${r.study_role}；ID ${r.id}。`, `  - 正文判断：${r.judgment}（笔记 ${evidence}）`, `  - 来源：${r.source_taxon_or_scope}；角色：${r.source_role}。`];
  if (r.caution || r.source_caution) result.push(`  - 边界：${[r.caution, r.source_caution].filter(Boolean).join('；')}`);
  const enzymeLinks = [...new Map(r.enzyme_links.map(e => [e.page, e])).values()].slice(0, 2);
  const hostLinks = [...new Map(r.factory_links.map(e => [e.page, e])).values()].slice(0, 2);
  const bridges = [...enzymeLinks.map(e => wiki(e.page, `酶索引：${path.basename(path.dirname(e.page))}`)), ...hostLinks.map(h => wiki(h.page, `体系索引：${h.role}（${h.note}）`))];
  if (bridges.length) result.push(`  - 跨框架：${bridges.join(' · ')}。`);
  return result.join('\n');
}
for (const c of categories) {
  const rs = records.filter(r => r.category === c);
  let text = `# ${c}：研究专题导航\n\n${wiki(`生物合成/${c}/00. 类别导航.md`, '类别与全部跨框架文献')} · ${wiki(`生物合成/${c}/00. 来源导航.md`, '来源复核')} · ${wiki('生物合成/研究专题导航.md', '跨化合物研究专题')}\n\n${scope}\n\n本页覆盖本类别 ${rs.length} 个主归档笔记。其他两框架的同类文献保留在原类别导航的交叉引用区；本轮未重新为这些文献分配生物合成专题。来源是天然产生者或研究通路来源，不是异源表达宿主或靶标。\n\n## 专题概览\n\n| 研究问题 | 主专题笔记 | 含关联专题 |\n| --- | ---: | ---: |\n`;
  for (const t of topics) text += `| ${t.name} | ${rs.filter(r => r.primary_topic === t.id).length} | ${rs.filter(r => r.topics.includes(t.id)).length} |\n`;
  text += '\n先按天然来源分组，再按研究问题阅读；没有正文证据的栏目不强行填充。\n';
  for (const s of sources) {
    const group = rs.filter(r => r.source_group === s && r.topics.length);
    if (!group.length) continue;
    text += `\n## ${s}\n`;
    for (const t of topics) {
      const matches = group.filter(r => r.topics.includes(t.id)).sort((a, b) => Number(b.primary_topic === t.id) - Number(a.primary_topic === t.id) || a.id - b.id);
      if (!matches.length) continue;
      text += `\n### ${String(t.id).padStart(2, '0')}. ${t.name}\n\n${t.question}\n\n${matches.map(r => item(r, t.id)).join('\n\n')}\n`;
    }
  }
  const excluded = rs.filter(r => !r.topics.length);
  if (excluded.length) text += '\n## 资料清单与待补证据\n\n' + excluded.map(r => `- ${wiki(r.target, r.focus)}：${r.judgment}（笔记 ${r.evidence.map(e => `L${e.line}`).join('、')}）`).join('\n') + '\n';
  add(categoryPath(c), 'biosynthesis-topic-category', text);
}
for (const t of topics) {
  let text = `# ${t.name}\n\n${wiki('生物合成/研究专题导航.md', '研究专题总入口')} · ${wiki('生物合成/00. 生物合成导航.md', '化合物类别入口')}\n\n${scope}\n\n${t.question}\n\n分类边界：${t.boundary}\n\n本专题包含 ${counts(t.id).linked} 个笔记，其中 ${counts(t.id).primary} 个以此为主专题；跨专题计数不可相加当作论文总数。\n`;
  for (const c of categories) {
    const group = records.filter(r => r.category === c && r.topics.includes(t.id));
    if (!group.length) continue;
    text += `\n## ${c}\n\n${wiki(categoryPath(c), '本类来源 → 专题导航')}\n`;
    for (const s of sources) {
      const matches = group.filter(r => r.source_group === s).sort((a, b) => Number(b.primary_topic === t.id) - Number(a.primary_topic === t.id) || a.id - b.id);
      if (matches.length) text += `\n### ${s}\n\n${matches.map(r => item(r, t.id)).join('\n\n')}\n`;
    }
  }
  add(topicPath(t), 'biosynthesis-research-topic', text);
}
let overview = `# 生物合成：研究专题导航\n\n${wiki('1. 通往合成生物学之路/00. 知识库导航.md', '三框架总导航')} · ${wiki('生物合成/00. 生物合成导航.md', '生物合成框架')} · ${wiki('生物合成/来源导航.md', '全部来源')} · ${wiki('生物合成/研究专题分类复核.md', '正文分类与验收')}\n\n${scope}\n\n## 两种阅读路线\n\n研究某类分子：化合物类别 → 天然来源 → 研究问题 → 文献正文。\n比较通用规律：研究问题 → 化合物类别 → 天然来源 → 文献正文。\n需要酶机制或生产体系时，沿文献条目的酶/体系索引链接进入另两框架，不另建一份原文。\n\n## 六个研究问题\n\n| 专题 | 回答的问题 | 主专题笔记 | 含关联专题 |\n| --- | --- | ---: | ---: |\n`;
for (const t of topics) overview += `| ${wiki(topicPath(t), t.name).replaceAll('|', '\\|')} | ${t.question} | ${counts(t.id).primary} | ${counts(t.id).linked} |\n`;
overview += '\n## 按化合物类别进入\n\n';
overview += categories.map(c => `- ${wiki(categoryPath(c), c)}：${records.filter(r => r.category === c).length} 个主归档笔记。`).join('\n');
overview += '\n\n## 使用与证据边界\n\n107 个笔记关联至少一个研究专题，1 个年度文献链接清单单列；108 是笔记数，不是去重后的原始论文数。方法、综述、预测指导化学合成、活性研究分别标注，不把标题中的“生物合成”当作完整途径证据。\n\n其他两框架的 159 个主归档笔记及既有跨框架索引保留，本轮不宣称已为其完成六专题正文复核。疑似重复解读不删除、不充当独立重复验证。原笔记、图片链接与 Git 远程配置不修改。\n\n后续新增笔记时，先判定主要研究问题及证据类型，再补来源和次专题；未读正文的记录先留待核实，不用关键词自动确认机制。\n';
add('生物合成/研究专题导航.md', 'biosynthesis-topic-index', overview);
let report = `# 生物合成研究专题：正文分类复核\n\n${wiki('生物合成/研究专题导航.md', '返回专题导航')}\n\n审阅范围：108 个生物合成主归档笔记的分类相关正文。逐条人工决定主/次专题；原始论文、SI、图片内容未在本轮逐项核验。267 个原笔记 SHA256 必须保持迁移清单基线不变。完整正文引文、哈希、来源和交叉链接保存于同目录的研究专题索引清单.json；人工决策在 .maintenance/biosynthesis-topic-body-review.json。\n\n专题代码：${topics.map(t => `${t.id}=${t.name}`).join('；')}；0=资料清单不分配科研专题。\n\n## 分类记录\n\n| ID | 化合物类别 | 主 / 次专题 | 研究重点与正文判断 | 正文行号 | 类型与边界 |\n| ---: | --- | --- | --- | --- | --- |\n`;
for (const r of records) report += `| ${r.id} | ${r.category} | ${r.primary_topic} / ${r.secondary_topics.join('、') || '无'} | ${wiki(r.target, r.focus).replaceAll('|', '\\|')}：${escapeCell(r.judgment)} | ${r.evidence.map(e => `L${e.line}`).join('、')} | ${escapeCell(r.study_role + (r.caution ? '；' + r.caution : ''))} |\n`;
report += '\n## 验收与再生成\n\n原文不移动、不复制、不修改；导航采用可识别的局部块更新，保留总导航搬迁和用户已有链接修改。来源维度沿用已正文复核的来源索引，不拿生产宿主充当天然产生者。\n\n可复核命令：\n\n```powershell\nnode .maintenance/build-reviewed-biosynthesis-topics.mjs --check\n& .maintenance/validate-three-frameworks.ps1\n& .maintenance/validate-biosynthesis-sources.ps1\n```\n\n原笔记内容若发生变化，再生成会停止，需重新审阅相关分类。旧萜专题的 11 个尚未建立概念链接单独保留，不在本轮捏造内容来补齐。\n';
add('生物合成/研究专题分类复核.md', 'biosynthesis-topic-review', report);
outputs.set('生物合成/研究专题索引清单.json', JSON.stringify({ schema: 1, date: review.date, method: '人工回读本地笔记相关正文；禁止标题/关键词自动分类', scope: review.scope, single_copy: true, topics, counts: { reviewed_notes: records.length, assigned_notes: records.filter(r => r.topics.length).length, unassigned_lists: records.filter(r => !r.topics.length).length }, records }, null, 2) + '\n');

const begin = '<!-- research-topics:start -->', end = '<!-- research-topics:end -->';
const blockPattern = /<!-- research-topics:start -->[\s\S]*?<!-- research-topics:end -->\n\n/g;
const navigationBefore = new Map();
const baselineFile = '.maintenance/biosynthesis-topics-navigation-baseline.json';
const baseline = fs.existsSync(path.join(root, baselineFile)) ? json(baselineFile) : { date: review.date, files: {} };
function bridge(p, content) {
  const body = read(p);
  const clean = body.replace(blockPattern, '');
  navigationBefore.set(p, hash(Buffer.from(clean)));
  if (clean.includes(begin) || clean.includes(end)) throw Error(`Malformed topic block ${p}`);
  if (!baseline.files[p]) baseline.files[p] = { sha256: hash(Buffer.from(clean)), content: clean };
  const match = /^## /m.exec(clean);
  const offset = match?.index ?? clean.length;
  const block = `${begin}\n## 按研究问题阅读\n\n${content}\n${end}\n\n`;
  outputs.set(p, clean.slice(0, offset) + block + clean.slice(offset));
}
for (const c of categories) {
  const content = `${wiki(categoryPath(c), '本类：天然来源 → 六个研究专题')}。主/次专题依据笔记正文；原文只有一份，完整的跨框架文献仍保留在类别导航。`;
  bridge(`生物合成/${c}/00. 类别导航.md`, content);
  bridge(`生物合成/${c}/00. 来源导航.md`, content);
}
for (const p of ['1. 通往合成生物学之路/00. 知识库导航.md', '生物合成/00. 生物合成导航.md', '生物合成/来源导航.md']) {
  bridge(p, `${wiki('生物合成/研究专题导航.md', '生物合成研究专题总入口')}：发现与途径定位、前体与骨架、后修饰、多单元与分支、调控与生态、活性与靶标。\n\n保留化合物类别 → 天然来源，再增加研究问题导航；108 个主归档笔记完成正文分类，其中 1 个资料清单单列。`);
}
for (const p of ['酶工程/00. 酶工程导航.md', '细胞工厂/00. 细胞工厂导航.md']) bridge(p, `${wiki('生物合成/研究专题导航.md', '从化合物与研究问题返回生物合成')}。本框架继续按酶类别或实际体系组织，不以宿主替代天然来源；既有正文复核索引保留。`);
if (!fs.existsSync(path.join(root, baselineFile))) {
  if (check) throw Error('Missing navigation baseline; generate before checking');
  outputs.set(baselineFile, JSON.stringify(baseline, null, 2) + '\n');
}
const changed = [...outputs].filter(([p, text]) => !fs.existsSync(path.join(root, p)) || read(p) !== text);
if (check) {
  if (changed.length) throw Error(`Stale topic outputs: ${changed.map(([p]) => p).join(', ')}`);
} else {
  for (const [p, text] of changed) {
    const full = path.resolve(root, p);
    if (!full.startsWith(root + path.sep)) throw Error('Path outside vault');
    fs.mkdirSync(path.dirname(full), { recursive: true });
    fs.writeFileSync(full, text, 'utf8');
  }
}
const preservation = [...navigationBefore].filter(([p, sha256]) => hash(Buffer.from(read(p).replace(blockPattern, ''))) !== sha256).map(([p]) => p);
if (preservation.length) throw Error(`Changed existing navigation outside topic blocks: ${preservation.join(', ')}`);
console.log(JSON.stringify({ passed: true, mode: check ? 'check-no-writes' : 'generate', bodyReviewedNotes: records.length, assignedNotes: records.filter(r => r.topics.length).length, originalHashesVerified: plan.files.length, categories: categories.length, topicPages: topics.length, preservedNavigationPages: Object.keys(baseline.files).length, changedFiles: changed.length, primaryTopicCounts: Object.fromEntries(topics.map(t => [t.name, counts(t.id).primary])) }, null, 2));

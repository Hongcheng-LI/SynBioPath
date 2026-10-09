import hashlib,json,re,os
from collections import Counter,defaultdict
from pathlib import Path
from datetime import datetime,timezone,timedelta
from inventory import ROOT,VAULT

def navigation_block(path,content):
    if not path.exists():return
    original=path.read_text(encoding='utf-8-sig')
    start='<!-- literature-reading-20261006:start -->'
    end='<!-- literature-reading-20261006:end -->'
    block=start+'\n'+content.strip()+'\n'+end
    if start in original:
        revised=re.sub(re.escape(start)+r'[\s\S]*?'+re.escape(end),lambda _:block,original)
    else:
        backup=ROOT/'navigation-backups'/path.relative_to(VAULT)
        backup.parent.mkdir(parents=True,exist_ok=True)
        if not backup.exists():backup.write_bytes(path.read_bytes())
        revised=original.rstrip()+'\n\n'+block+'\n'
    if revised!=original:path.write_text(revised,encoding='utf-8')

def update():
    path=ROOT/'prepared-inventory.json'
    data=json.loads(path.read_text(encoding='utf-8')) if path.exists() else json.loads((ROOT/'inventory.json').read_text(encoding='utf-8'))
    progress={}
    if (ROOT/'progress.jsonl').exists():
        for line in (ROOT/'progress.jsonl').read_text(encoding='utf-8').splitlines():
            if line.strip():
                try:r=json.loads(line);progress[r['key']]=r
                except json.JSONDecodeError:pass
    published=[]
    for p in (ROOT/'sources').glob('*/publication.json'):
        r=json.loads(p.read_text(encoding='utf-8'))
        if Path(r['note']).exists():published.append(r)
    counts=Counter(r['status'] for r in data['records'])
    failures=[r for r in progress.values() if r['status']=='blocked']
    summary={'updated':datetime.now(timezone(timedelta(hours=8))).isoformat(),'vault':str(VAULT),
             'inventory':dict(counts),'published_notes':len(published),
             'uploaded_images':sum(len(r['images']) for r in published),
             'attempted_unique_records':len(progress),'attempt_failures':len(failures),
             'remaining_local_ready':counts.get('ready',0)-len(published)}
    (ROOT/'status.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    title='2026-10-06 Zotero 全库文献解读进度'
    md=f'# {title}\n\n更新时间：{summary["updated"]}。目标库：`{VAULT}`。\n\n范围：Zotero 整个个人文库；排除学位论文、中文文献和糖免疫相关文献（2026-10-08 用户追加），跳过已有实质解读及重复条目。\n\n'
    md+=f'已完成笔记 **{len(published)} 篇**，已上传并校验 **{summary["uploaded_images"]} 张原文截图**；本地主文可读队列尚余 **{summary["remaining_local_ready"]} 篇**。\n\n当前阶段：先整理全部笔记，新增笔记统一暂存于 `00. 文献笔记待归类/2026-10 全库解读`；完成后再分类。前轮已归档的 4 篇保留原位，分类导航本阶段暂停更新。\n\n'
    md+='本阶段优先处理已有且可读的 PDF，无 PDF 或文件不可用的条目暂不处理。笔记分别记录外部模型交叉核对或当前 Codex 原文核对方式，均与人工逐项复核分开；受阻条目不能算作已完成。已有论文笔记和原始 PDF 保持原样。\n\n'
    md+='## 库存核对\n\n| 状态 | 条目数 |\n| --- | ---: |\n'
    names={'ready':'本地主文可读（含已处理）','already-interpreted':'已匹配实质解读','duplicate-record':'重复记录','blocked-no-pdf':'无 PDF 附件记录','blocked-pdf-unavailable':'PDF 记录存在，但本地文件不可用','blocked-main-pdf-identity':'未取得可确认的主文，通常仅有 SI','blocked-text-extraction':'全文提取受阻','blocked-corrupt-pdf':'PDF 文件损坏，无法读取页面','excluded-thesis':'排除学位论文','excluded-chinese':'排除中文文献','excluded-chinese-pdf':'PDF 确认为中文，排除','excluded-non-paper':'排除非论文条目'}
    for status,n in counts.items():md+=f'| {names.get(status,status)} | {n} |\n'
    md+='\n## 本次新增笔记\n\n'
    groups=defaultdict(list);related_groups=defaultdict(list)
    for entry in published:
        note=Path(entry['note']);rel=note.relative_to(VAULT).as_posix();groups[str(note.parent.relative_to(VAULT)).replace('\\','/')].append(rel)
        for other in entry.get('draft_metadata',{}).get('related_categories',[]):
            if (VAULT/other).is_dir() and other!=str(note.parent.relative_to(VAULT)).replace('\\','/'):
                related_groups[other].append(rel)
        md+=f'- [[{rel[:-3]}|{note.stem}]]\n'
    if not published:md+='尚无笔记通过全部归档步骤。\n'
    md+='\n## 生成或核对受阻\n\n'
    for r in failures:md+=f'- `{r["key"]}` {r["title"]}：{r.get("stage","")} / {r.get("error","")}。\n'
    if not failures:md+='当前无生成失败记录。\n'
    md+='\n## 本地附件受阻清单\n\n'
    for r in data['records']:
        if r['status'].startswith('blocked-'):
            md+=f'- `{r["key"]}` {r["title"]}；DOI：{r["doi"] or "未记录"}；{names.get(r["status"],r["status"])}。\n'
    # Status is derived data and does not edit any original literature note.
    (VAULT/(title+'.md')).write_text(md,encoding='utf-8')
    return summary
    for category in set(groups)|set(related_groups):
        notes=groups.get(category,[])
        p=VAULT/category/'00. 本次批量新增文献.md'
        content='# 本次批量新增文献\n\n[[2026-10-06 Zotero 全库文献解读进度|返回全库任务进度]]\n\n'
        content+=f'## 主归档（{len(notes)} 篇）\n\n'
        content+='\n'.join(f'- [[{x[:-3]}|{Path(x).stem}]]' for x in sorted(notes))+'\n'
        others=related_groups.get(category,[])
        if others:content+=f'\n## 关联阅读（{len(others)} 篇，正文位于其他类别）\n\n'+'\n'.join(f'- [[{x[:-3]}|{Path(x).stem}]]' for x in sorted(others))+'\n'
        p.write_text(content,encoding='utf-8')
        navigation_block(VAULT/category/'00. 类别导航.md',f'## 本次新增阅读\n\n[[{category}/00. 本次批量新增文献|2026-10-06 批量解读：主归档 {len(notes)} 篇，关联阅读 {len(others)} 篇]]。原表计数保留为 2026-10-04 整理基线。')
    navigation_block(VAULT/'1. 通往合成生物学之路'/'00. 知识库导航.md','## Zotero 全库解读\n\n[[2026-10-06 Zotero 全库文献解读进度|查看本次新增笔记、全库进度与附件受阻清单]]。以上三框架计数为 2026-10-04 整理基线；本次新增单独登记，各类别导航中保留入口。')
    return summary

if __name__=='__main__':
    import sys;sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(update(),ensure_ascii=False,indent=2))

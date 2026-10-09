# Zotero 全库解读任务

目标知识库：`C:\Software\Data\05-Obsidian\SynBioPath`。

用户范围：整个 Zotero 个人文库，排除学位论文及中文论文。实质解读通过 DOI、准确题名与阅读内容匹配；导航、索引或只有摘要的条目不等同已经解读。重复 Zotero 记录共用一个正文身份。

`prompts/research.md` 与 `prompts/review.md` 保存本次用户提示词的原样快照；没有更改桌面原始文件。

处理步骤：本地 PDF 身份/语言检查 → 全文及图表原页 → 对应提示词生成 → 格式检查 → 来源与裁剪核对 → 必要时按原文修正并重审 → PicGo 上传 → 实际图片内容哈希校验 → 统一暂存待归类目录（全部笔记完成后再分类）。

使用本机 paper-interpret 已配置的模型接口；凭据仅从现有配置读取，不在任务文件中存储。不使用摘要冒充全文。无法覆盖图表或无法读取主文的条目保持受阻，不标记完成。模型核对结果不等同人工逐项复核。

`inventory.json` 是起始全库核对；`prepared-inventory.json` 包含附件检查及排除结果。`progress.jsonl` 为追加记录，`status.json` 为最新汇总。每篇的 `sources/<Zotero-key>/` 保存主文提取文本、原始页面、草稿、来源核对、截图和 PicGo URL；原始 Zotero PDF 与已有论文笔记只读。

重新开始已有队列：

```powershell
python -X utf8 -u "C:\Software\Data\05-Obsidian\SynBioPath\.maintenance\literature-reading-20261006\worker.py" --all --workers 4
```

已成功归档的条目不会再次生成或上传。运行锁中的 PID 必须先核实，不能在已有进程运行时启动第二份任务。连续模型接口错误会停止新请求，保留已经完成的结果及来源核对记录。

查看进度：打开知识库根目录的 `2026-10-06 Zotero 全库文献解读进度.md`。每个已有分类下新增 `00. 本次批量新增文献.md`，正文各放一个主位置，其他框架保留关联链接。

不适合既有三框架的论文进入“99. 跨学科文献与待分类”，明确分类限制，不伪称已完成专业归类。


2026-10-07 续跑调整：按用户要求先笔记后分类；截图名包含 Zotero key 和内容哈希，避免图床同名覆盖；生成/修复/核对预算提高至 48000 tokens，输出截断作为单篇失败，不当作模型服务整体断线；事实错误不得作为 minor issue 放行。


当前用户优先级：只处理已有可读主文 PDF，暂停缺失全文下载；全部笔记整理完之前不分类。两份历史扫描件经 Windows 本地 OCR 恢复，并保留全部原始页面供生成与核对。queue_guard.py 在主队列结束后接续 OCR 新增与失败重试；guard.lock / worker.lock 表示独立控制器与工作进程，不能重复启动。

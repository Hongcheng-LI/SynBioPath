param([switch]$ValidateOnly)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$plan = Get-Content -LiteralPath (Join-Path $PSScriptRoot '三框架迁移清单.json') -Raw -Encoding utf8 | ConvertFrom-Json
if ([IO.Path]::GetFullPath($plan.root) -ne $root) { throw 'Wrong workspace.' }
$bios = @($plan.files | Where-Object framework -eq '生物合成')
$review = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'biosynthesis-source-body-review.json') -Raw -Encoding utf8 | ConvertFrom-Json
$groupNames = @('真菌来源','细菌来源','植物来源','动物来源','古菌来源','宏基因组来源（产生者未定）','多来源或生态体系','跨来源与通用方法','来源待核实')
$decisions = @{}
foreach ($row in $review.rows) {
    if ($row.Count -ne 7 -or $decisions.ContainsKey([int]$row[0])) { throw 'Malformed or duplicate review row.' }
    $decisions[[int]$row[0]] = $row
}
if ($decisions.Count -ne $bios.Count) { throw 'Review coverage does not match biosynthesis inventory.' }

# No title or keyword classifier: classification is an explicitly reviewed decision.
# Verify ALL inputs before writing any output. A changed note requires another review.
$records = [Collections.Generic.List[object]]::new()
foreach ($item in $bios) {
    if (-not $decisions.ContainsKey([int]$item.id)) { throw "Missing body review: $($item.id)" }
    $d = $decisions[[int]$item.id]
    if ($d[1] -notin $groupNames -or @($d[4]).Count -eq 0) { throw "Invalid source/evidence: $($item.id)" }
    $path = [IO.Path]::GetFullPath((Join-Path $root $item.target))
    if (-not $path.StartsWith($root + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Path outside vault.' }
    $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
    if ($hash -ne $item.sha256) { throw "Note changed; re-review evidence before rebuilding: $($item.target)" }
    $body = @(Get-Content -LiteralPath $path -Encoding utf8)
    $evidence = @(foreach ($line in $d[4]) {
        $n = [int]$line
        if ($n -lt 1 -or $n -gt $body.Count -or [string]::IsNullOrWhiteSpace($body[$n-1]) -or $body[$n-1] -match '^\s*(#|!\[)') { throw "Invalid body evidence: $($item.id):$n" }
        [pscustomobject]@{ line = $n; quote = $body[$n-1] }
    })
    $records.Add([pscustomobject][ordered]@{
        id = [int]$item.id
        category = [string]$item.category
        source_group = [string]$d[1]
        source_taxon_or_scope = [string]$d[2]
        source_role = [string]$d[3]
        title = [IO.Path]::GetFileNameWithoutExtension($item.target)
        target = [string]$item.target
        basis = [string]$d[5]
        review_flag = [string]$d[6]
        review_status = $(if ($d[1] -eq '来源待核实') { 'body-reviewed-source-unresolved' } else { 'body-reviewed' })
        evidence_level = 'local-note-body; original-paper-not-verified'
        note_sha256 = $hash
        evidence = $evidence
    })
}
if ($ValidateOnly) { Write-Output "PASS: $($records.Count) body decisions, hashes and evidence lines verified; no writes."; return }

function Write-GeneratedText([string]$Path, [string]$Text) {
    $normalized = $Text.Replace("`r`n", "`n").TrimEnd() + "`n"
    if ((Test-Path -LiteralPath $Path) -and [IO.File]::ReadAllText($Path) -ceq $normalized) { return }
    [IO.File]::WriteAllText($Path, $normalized, [Text.UTF8Encoding]::new($false))
}
function Assert-GeneratedPage([string]$Path, [string]$Type) {
    if ((Test-Path -LiteralPath $Path) -and -not ((Get-Content -LiteralPath $Path -TotalCount 4 -Encoding utf8) -contains ('type: ' + $Type))) { throw "Refusing to overwrite unrecognized page: $Path" }
}
function NoteLink($Record) { return '[[' + $Record.target.Substring(0, $Record.target.Length - 3) + '|' + $Record.title + ']]' }

$manifestPath = Join-Path $root '生物合成/来源分类索引清单.json'
$baselinePath = Join-Path $PSScriptRoot 'biosynthesis-source-title-baseline.json'
if (-not (Test-Path -LiteralPath $baselinePath)) {
    $old = Get-Content -LiteralPath $manifestPath -Raw -Encoding utf8 | ConvertFrom-Json
    if ($old.method -notmatch '标题') { throw 'Expected the original title-based baseline; refusing to invent a comparison.' }
    Copy-Item -LiteralPath $manifestPath -Destination $baselinePath
}
$baseline = Get-Content -LiteralPath $baselinePath -Raw -Encoding utf8 | ConvertFrom-Json
$oldGroups = @{}
foreach ($entry in $baseline.records) { $oldGroups[[int]$entry.id] = $entry.source_group }
$categories = @($records.category | Sort-Object -Unique)
foreach ($category in $categories) { Assert-GeneratedPage (Join-Path $root ('生物合成/' + $category + '/00. 来源导航.md')) 'source-index' }
Assert-GeneratedPage (Join-Path $root '生物合成/来源导航.md') 'biosynthesis-source-index'
$reportPath = Join-Path $root '生物合成/来源分类正文复核.md'
Assert-GeneratedPage $reportPath 'source-review-report'

$manifest = [ordered]@{
    schema = 2
    date = $review.review_date
    method = '逐条回读本地笔记的来源相关正文，人工判断产生者、通路来源、异源宿主及靶标关系；不按标题或物种关键词自动归类'
    scope = $review.scope
    single_copy = $true
    records = @($records)
}
Write-GeneratedText $manifestPath ($manifest | ConvertTo-Json -Depth 8)
foreach ($category in $categories) {
    $members = @($records | Where-Object category -eq $category)
    $lines = [Collections.Generic.List[string]]::new()
    @('---','type: source-index',('updated: ' + $review.review_date),'---','',('# ' + $category + '：按来源浏览'),'',
      ('[[' + ('生物合成/' + $category + '/00. 类别导航') + '|返回本化合物类别]] · [[生物合成/来源导航|全部来源分类]] · [[生物合成/来源分类正文复核|正文复核记录]]'),'',
      '分组依据本地文献笔记的正文。来源指天然产生者、研究通路或明确标注的天然模板，不是异源表达宿主、活性靶标或采样环境。每条显示判断及正文行号；完整原句和文件哈希保存在生物合成/来源分类索引清单.json。未核查原始论文全文。','') | ForEach-Object { $lines.Add($_) }
    foreach ($group in $groupNames) {
        $subset = @($members | Where-Object source_group -eq $group)
        if ($subset.Count -eq 0) { continue }
        $lines.Add('## ' + $group + '（' + $subset.Count + '）'); $lines.Add('')
        foreach ($r in $subset) {
            $lines.Add('- ' + (NoteLink $r))
            $lines.Add('  - 来源：' + $r.source_taxon_or_scope + '；角色：' + $r.source_role + '。')
            $lines.Add('  - 正文判断：' + $r.basis + '（笔记 ' + (($r.evidence | ForEach-Object { 'L' + $_.line }) -join '、') + '）')
            if ($r.review_flag) { $lines.Add('  - 边界：' + $r.review_flag + '。') }
        }
        $lines.Add('')
    }
    Write-GeneratedText (Join-Path $root ('生物合成/' + $category + '/00. 来源导航.md')) ($lines -join "`n")
    $categoryIndex = Join-Path $root ('生物合成/' + $category + '/00. 类别导航.md')
    $body = Get-Content -LiteralPath $categoryIndex -Raw -Encoding utf8
    $link = '[[生物合成/' + $category + '/00. 来源导航|按天然来源浏览]]'
    $body = $body.Replace(' · [[00. 来源导航|按天然来源浏览]]', '')
    if (-not $body.Contains($link)) {
        $anchor = '[[00. 知识库导航|三框架总导航]]'
        if (-not $body.Contains($anchor)) { throw "Missing navigation anchor: $categoryIndex" }
        $body = $body.Replace($anchor, $anchor + ' · ' + $link)
    }
    Write-GeneratedText $categoryIndex $body
}

$lines = [Collections.Generic.List[string]]::new()
@('---','type: biosynthesis-source-index',('updated: ' + $review.review_date),'---','','# 生物合成：按化合物类别 → 来源浏览','',
  '[[00. 生物合成导航|返回生物合成导航]] · [[00. 知识库导航|返回总导航]] · [[生物合成/来源分类正文复核|正文复核记录]]','',
  '本轮逐条核对了 108 篇生物合成主归档笔记的来源相关正文，替换原来的标题初筛。文献仍保持单份，化合物类别沿用现有一级分类；此处不是对其余框架、全部化合物类别或原始论文的完整复审。','',
  '“动物来源”等分组可包含天然模板的合成衍生物，具体角色在条目下单列。宏基因组来源不等于已确定产生菌；方法论文按实际研究对象或跨来源范围归类。','') | ForEach-Object { $lines.Add($_) }
foreach ($category in $categories) {
    $count = @($records | Where-Object category -eq $category).Count
    $lines.Add('- [[生物合成/' + $category + '/00. 来源导航|' + $category + ']] — ' + $count + ' 篇主归档笔记')
}
$lines.Add(''); $lines.Add('## 正文复核后的来源分组'); $lines.Add('')
foreach ($group in $groupNames) {
    $count = @($records | Where-Object source_group -eq $group).Count
    if ($count) { $lines.Add('- ' + $group + '：' + $count) }
}
$lines.Add(''); $lines.Add('计数单位是笔记文件，不是去重后的独立论文。综述、文献汇总及不同版本未擅自合并。证据层级为本地笔记正文，不等于原始文献已验证。')
Write-GeneratedText (Join-Path $root '生物合成/来源导航.md') ($lines -join "`n")

$changed = @($records | Where-Object { $oldGroups[$_.id] -ne $_.source_group })
$lines = [Collections.Generic.List[string]]::new()
@('---','type: source-review-report',('updated: ' + $review.review_date),'---','','# 来源分类：正文复核记录','',
  '[[生物合成/来源导航|返回来源导航]]','',
  '## 本轮覆盖与证据边界','',
  '- 已逐条回读 108 篇生物合成主归档笔记的来源相关正文，不仅复查原待核实条目，也复查原已分类条目。',
  '- 分类依据是本地笔记的背景、方法、结果等正文中产生菌、基因簇来源及宿主关系。没有把标题正则改成正文关键词自动判定。',
  '- 未打开和核查每篇原始论文全文、图内文字或 SI；笔记中的科学断言不因被摘录而获得独立验证。',
  '- 这份来源报告只覆盖生物合成来源维度；其他两框架的后续正文复核见 [[酶工程/分类正文复核|酶工程复核]] 与 [[细胞工厂/分类正文复核|细胞工厂复核]]。化合物类别未在来源复核中全部重判。',
  '- 文献正文不改写、不复制、不重新移动；索引可交叉引用。',
  '- 判定输入：.maintenance/biosynthesis-source-body-review.json；输出：生物合成/来源分类索引清单.json。输出逐条记录原句、行号、SHA256 和解释。',
  '- 原标题初筛清单留存于 .maintenance/biosynthesis-source-title-baseline.json，仅供追溯，不再驱动分类。','',
  '## 来源改变','',('相对标题初筛，共 ' + $changed.Count + ' 条来源分组发生改变；其余条目也补充了正文证据。'),'') | ForEach-Object { $lines.Add($_) }
foreach ($r in $changed) { $lines.Add('- ' + (NoteLink $r) + '：' + $oldGroups[$r.id] + ' → ' + $r.source_group + '。' + $r.basis) }
$lines.Add(''); $lines.Add('## 仍无法确认来源的条目'); $lines.Add('')
foreach ($r in @($records | Where-Object source_group -eq '来源待核实')) { $lines.Add('- ' + (NoteLink $r) + '：' + $r.review_flag + '。') }
$lines.Add(''); $lines.Add('## 需要保留的限定与后续复核'); $lines.Add('')
foreach ($r in @($records | Where-Object { $_.review_flag -and $_.source_group -ne '来源待核实' })) { $lines.Add('- ' + (NoteLink $r) + '：' + $r.review_flag + '。') }
$lines.Add(''); $lines.Add('## 后续入库规则'); $lines.Add('')
@('- 生物合成：先看实际研究的通路与化合物骨架，再记录天然产生者或通路来源；杂合骨架、未知来源不硬塞进单一类别。',
  '- 酶工程：按被实际研究或改造的酶类别分类；只在背景中提到 P450、糖基转移酶等，不足以建立该类别关系。纯酶功能发现与工程改造应分开标注。',
  '- 细胞工厂：按实际生产体系的宿主分类；仅用于表达纯化酶的大肠杆菌、用于克隆的酵母、疾病模型或未来展望不自动计为细胞工厂。',
  '- 交叉研究保留一个正文文件，可在多个入口建立索引；每个分类关系分别记录正文依据。',
  '- 未知、推测、异源重构、天然分离、化学合成和基因进化来源分别记录。不得把预测、重构或药效实验升级为天然存在证据。',
  '- 更改文献笔记后必须重新核对行号与依据；构建脚本会因文件哈希变化停止，避免旧证据悄然失效。') | ForEach-Object { $lines.Add($_) }
Write-GeneratedText $reportPath ($lines -join "`n")
Write-Output "Indexed notes: $($records.Count); changed source groups: $($changed.Count)"
$records | Group-Object source_group | Sort-Object Name | ForEach-Object { Write-Output ($_.Name + ': ' + $_.Count) }

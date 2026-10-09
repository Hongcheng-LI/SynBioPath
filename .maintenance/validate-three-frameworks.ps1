$ErrorActionPreference = 'Stop'
$repoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$plan = Get-Content -LiteralPath (Join-Path $PSScriptRoot '三框架迁移清单.json') -Raw | ConvertFrom-Json
if ($repoRoot -ne [IO.Path]::GetFullPath($plan.root)) { throw 'Wrong workspace.' }
$failures = @()
if (@($plan.files.id | Sort-Object -Unique).Count -ne $plan.files.Count) { $failures += 'Duplicate literature IDs.' }
if (@($plan.files.target | Sort-Object -Unique).Count -ne $plan.files.Count) { $failures += 'Duplicate literature targets.' }
$byId = @{}
foreach ($file in $plan.files) {
    $byId[[int]$file.id] = $file
    $target = Join-Path $repoRoot $file.target
    if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
        $failures += ('Missing literature: ' + $file.target)
    } elseif ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash -ne $file.sha256) {
        $failures += ('Changed literature content: ' + $file.target)
    }
    if ($file.target.Split('/')[0] -ne $file.framework -or $file.target.Split('/')[1] -ne $file.category) {
        $failures += ('Framework/category mismatch: ' + $file.target)
    }
}
$counts = [ordered]@{}
foreach ($framework in @('生物合成','酶工程','细胞工厂')) {
    $expected = @($plan.files | Where-Object framework -eq $framework).Count
    $counts[$framework] = $expected
    $actual = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot $framework) -Filter '*.md' -File -Recurse | Where-Object {
        $_.Name -notin @('00. 类别导航.md','00. 来源导航.md','00. 研究专题导航.md') -and $_.Directory.Name -match '^\d\d\.'
    }).Count
    if ($expected -ne $actual) { $failures += ('Physical note count mismatch: ' + $framework) }
}
$enzyme = Get-Content -LiteralPath (Join-Path $repoRoot '酶工程/酶索引清单.json') -Raw | ConvertFrom-Json
$factoryIndex = Get-Content -LiteralPath (Join-Path $repoRoot '细胞工厂/细胞工厂索引清单.json') -Raw | ConvertFrom-Json
foreach ($file in $enzyme.files) {
    if ($file.source -ne $byId[[int]$file.literature_id].target) { $failures += 'Enzyme source path mismatch.' }
    foreach ($membership in $file.memberships) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $membership.page))) { $failures += 'Missing enzyme index.' }
    }
}
foreach ($file in $factoryIndex.files) {
    if ($file.target -ne $byId[[int]$file.id].target) { $failures += 'Host source path mismatch.' }
    foreach ($assignment in $file.assignments) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $assignment.index))) { $failures += 'Missing host index.' }
    }
}
foreach ($group in $factoryIndex.groups) {
    $actual = @($factoryIndex.files | Where-Object { $_.assignments.group -contains $group.key }).Count
    if ($group.notes -ne $actual) { $failures += ('Host group count mismatch: ' + $group.key) }
}
if (@($plan.files | Where-Object { $_.framework -eq '酶工程' -and $_.id -notin $enzyme.files.literature_id }).Count) { $failures += 'Primary enzyme notes missing from index.' }
if (@($plan.files | Where-Object { $_.framework -eq '细胞工厂' -and $_.id -notin $factoryIndex.files.id }).Count) { $failures += 'Primary host notes missing from index.' }

$markdown = @(Get-ChildItem -LiteralPath $repoRoot -Filter '*.md' -File -Recurse | Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' })
$oldConcepts = @('MVA 途径','MEP 途径','IPP 与 DMAPP','异戊烯基二磷酸合酶','萜类合酶','碳正离子级联环化','P450 后修饰','2-酮戊二酸依赖型双加氧酶','真菌萜类细胞工厂','酵母萜类细胞工厂','无细胞萜类生物合成')
$preexistingPlaceholders = @()
$newBrokenLinks = @()
$linkCount = 0
foreach ($file in $markdown) {
    $relative = [IO.Path]::GetRelativePath($repoRoot, $file.FullName).Replace('\','/')
    $body = [string](Get-Content -LiteralPath $file.FullName -Raw)
    foreach ($match in [regex]::Matches($body, '\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')) {
        $linkCount++
        $target = $match.Groups[1].Value.TrimEnd([char]92).Split('#')[0]
        if (-not $target) { continue }
        $exists = (Test-Path -LiteralPath (Join-Path $repoRoot $target)) -or (Test-Path -LiteralPath (Join-Path $repoRoot ($target + '.md')))
        # Obsidian supports links relative to the page as well as vault-root paths.
        if (-not $exists) {
            $pageRelativeTarget = Join-Path $file.DirectoryName $target
            $exists = (Test-Path -LiteralPath $pageRelativeTarget) -or (Test-Path -LiteralPath ($pageRelativeTarget + '.md'))
        }
        if (-not $exists) { $exists = @($markdown | Where-Object { $_.BaseName -eq $target -or $_.Name -eq $target }).Count -gt 0 }
        if (-not $exists) {
            $item = [pscustomobject]@{File=$relative; Target=$target}
            if ($relative -eq '生物合成/知识专题/6. 萜.md' -and $target -in $oldConcepts) {
                $preexistingPlaceholders += $item
            } else { $newBrokenLinks += $item }
        }
    }
}
if ($newBrokenLinks.Count) { $failures += 'New broken wikilinks.' }
$result = [ordered]@{
    Date='2026-10-04'; Passed=($failures.Count -eq 0); LiteratureNotes=$plan.files.Count
    MainFrameworkCounts=$counts; LiteratureContentHashesPassed=($plan.files.Count - @($failures | Where-Object { $_ -match '^Missing literature:|^Changed literature content:' }).Count)
    EnzymeLinkedNotes=$enzyme.files.Count; HostLinkedNotes=$factoryIndex.files.Count; Wikilinks=$linkCount
    NewBrokenWikilinks=$newBrokenLinks.Count; PreexistingUncreatedConceptLinks=$preexistingPlaceholders.Count
    PreservedConceptPlaceholders=$preexistingPlaceholders; Failures=$failures; NewBrokenLinkDetails=$newBrokenLinks
}
$result | ConvertTo-Json -Depth 6
if ($failures.Count) { throw 'Three-framework validation failed. See output.' }

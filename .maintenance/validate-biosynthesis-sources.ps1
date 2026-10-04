$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
& (Join-Path $PSScriptRoot 'build-reviewed-biosynthesis-sources.ps1') -ValidateOnly
$review = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'biosynthesis-source-body-review.json') -Raw -Encoding utf8 | ConvertFrom-Json
$manifest = Get-Content -LiteralPath (Join-Path $root '生物合成/来源分类索引清单.json') -Raw -Encoding utf8 | ConvertFrom-Json
$decisions = @{}
foreach ($row in $review.rows) { $decisions[[int]$row[0]] = $row }
$seen = @{}
$evidenceCount = 0
foreach ($r in $manifest.records) {
    if ($seen.ContainsKey([int]$r.id)) { throw "Duplicate generated record: $($r.id)" }
    $seen[[int]$r.id] = $true
    $d = $decisions[[int]$r.id]
    if (-not $d -or $d[1] -cne $r.source_group -or $d[2] -cne $r.source_taxon_or_scope -or $d[3] -cne $r.source_role -or $d[5] -cne $r.basis -or $d[6] -cne $r.review_flag) { throw "Output diverges from reviewed decision: $($r.id)" }
    if (@($r.evidence).Count -ne @($d[4]).Count) { throw "Evidence count differs: $($r.id)" }
    $path = Join-Path $root $r.target
    if ((Get-FileHash -LiteralPath $path).Hash -ne $r.note_sha256) { throw "Stale evidence hash: $($r.id)" }
    $body = @(Get-Content -LiteralPath $path -Encoding utf8)
    for ($i = 0; $i -lt $r.evidence.Count; $i++) {
        $e = $r.evidence[$i]
        if ($e.line -ne $d[4][$i] -or $body[$e.line-1] -cne $e.quote) { throw "Evidence quote/line mismatch: $($r.id)" }
        $evidenceCount++
    }
    $nav = Get-Content -LiteralPath (Join-Path $root ('生物合成/' + $r.category + '/00. 来源导航.md')) -Raw -Encoding utf8
    $expectedLink = '[[' + $r.target.Substring(0, $r.target.Length - 3) + '|'
    if (-not $nav.Contains($expectedLink) -or -not $nav.Contains($r.basis)) { throw "Missing navigation entry or explanation: $($r.id)" }
}
if ($seen.Count -ne $decisions.Count) { throw 'Generated output does not cover all reviewed records.' }
# Guard representative failure modes: target vs producer, host vs source,
# fungal flavonoids, animal-template derivatives, HGT, and unresolved origin.
$expected = @{28='真菌来源';64='真菌来源';82='真菌来源';96='来源待核实';99='动物来源';127='细菌来源';149='真菌来源';180='真菌来源';233='来源待核实';245='细菌来源';258='植物来源'}
foreach ($id in $expected.Keys) {
    $r = $manifest.records | Where-Object id -eq $id
    if ($r.source_group -ne $expected[$id]) { throw "Classification regression: $id" }
}
[ordered]@{
    Passed = $true
    BodyReviewedNotes = $seen.Count
    ExactBodyEvidenceQuotes = $evidenceCount
    SourceUnresolved = @($manifest.records | Where-Object source_group -eq '来源待核实').Count
    RegressionCases = $expected.Count
    OriginalPapersVerified = $false
} | ConvertTo-Json

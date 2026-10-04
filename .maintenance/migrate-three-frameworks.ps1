param([switch]$Execute)

$ErrorActionPreference = 'Stop'
$repoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$planPath = Join-Path $PSScriptRoot '三框架迁移清单.json'
$plan = Get-Content -LiteralPath $planPath -Raw | ConvertFrom-Json
if ($repoRoot -ne [IO.Path]::GetFullPath($plan.root)) {
    throw 'Manifest root does not match the script workspace.'
}
$boundary = $repoRoot.TrimEnd([char]92, [char]47) + [IO.Path]::DirectorySeparatorChar
$resolved = @()
foreach ($move in $plan.moves) {
    $sourcePath = [IO.Path]::GetFullPath((Join-Path $repoRoot $move.source))
    $targetPath = [IO.Path]::GetFullPath((Join-Path $repoRoot $move.target))
    if (-not $sourcePath.StartsWith($boundary, [StringComparison]::OrdinalIgnoreCase) -or
        -not $targetPath.StartsWith($boundary, [StringComparison]::OrdinalIgnoreCase)) {
        throw ('Path outside workspace: ' + $move.source)
    }
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw ('Missing source; migration is not safe to rerun: ' + $sourcePath)
    }
    if (Test-Path -LiteralPath $targetPath) { throw ('Target exists: ' + $targetPath) }
    $beforeHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
    if ($move.sha256 -and $beforeHash -ne $move.sha256) {
        throw ('Source changed since planning: ' + $sourcePath)
    }
    $resolved += [pscustomobject]@{Source=$sourcePath; Target=$targetPath; Hash=$beforeHash; Kind=$move.kind}
}
if (@($resolved.Target | Sort-Object -Unique).Count -ne $resolved.Count) {
    throw 'Duplicate targets in migration plan.'
}
if (-not $Execute) {
    [pscustomobject]@{Mode='DryRun'; Files=$resolved.Count; Literature=@($resolved | Where-Object Kind -eq 'literature').Count; Overwrites=0} | ConvertTo-Json
    return
}

foreach ($move in $resolved) {
    $parentPath = Split-Path -Parent $move.Target
    if (-not (Test-Path -LiteralPath $parentPath)) {
        New-Item -ItemType Directory -Path $parentPath -Force | Out-Null
    }
    Move-Item -LiteralPath $move.Source -Destination $move.Target -ErrorAction Stop
    if ((Get-FileHash -LiteralPath $move.Target -Algorithm SHA256).Hash -ne $move.Hash) {
        throw ('Post-move hash mismatch: ' + $move.Target)
    }
}

# Remove only verified empty legacy directories; never recursively delete files.
$emptyDirectoriesRemoved = 0
foreach ($legacyName in @('2. 文献库','4. 天然产物生物合成','6. 酶与生物催化','7. 细胞工厂','文献调研','公众号他人投稿')) {
    $legacyPath = [IO.Path]::GetFullPath((Join-Path $repoRoot $legacyName))
    if (-not $legacyPath.StartsWith($boundary, [StringComparison]::OrdinalIgnoreCase)) { throw 'Unsafe cleanup path.' }
    if (-not (Test-Path -LiteralPath $legacyPath)) { continue }
    $directories = @(Get-ChildItem -LiteralPath $legacyPath -Directory -Force -Recurse | Sort-Object { $_.FullName.Length } -Descending)
    $directories += Get-Item -LiteralPath $legacyPath
    foreach ($directory in $directories) {
        $absoluteDirectory = [IO.Path]::GetFullPath($directory.FullName)
        if (-not $absoluteDirectory.StartsWith($boundary, [StringComparison]::OrdinalIgnoreCase)) { throw 'Unsafe empty directory path.' }
        if (@(Get-ChildItem -LiteralPath $absoluteDirectory -Force).Count -eq 0) {
            Remove-Item -LiteralPath $absoluteDirectory -Force -ErrorAction Stop
            $emptyDirectoriesRemoved++
        }
    }
}
[pscustomobject]@{Mode='Executed'; Moved=$resolved.Count; Literature=@($resolved | Where-Object Kind -eq 'literature').Count; HashesPassed=$resolved.Count; EmptyLegacyDirectoriesRemoved=$emptyDirectoriesRemoved} | ConvertTo-Json

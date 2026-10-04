param([string]$Framework = '酶工程', [int]$Skip = 0, [int]$Count = 20, [int[]]$Ids, [string]$Pattern = '', [int]$Limit = 3, [int]$Width = 480)
$root = Split-Path -Parent $PSScriptRoot
$p = Get-Content (Join-Path $PSScriptRoot '三框架迁移清单.json') -Raw -Encoding utf8 | ConvertFrom-Json
$e = Get-Content (Join-Path $root '酶工程/酶索引清单.json') -Raw -Encoding utf8 | ConvertFrom-Json
$h = Get-Content (Join-Path $root '细胞工厂/细胞工厂索引清单.json') -Raw -Encoding utf8 | ConvertFrom-Json
$items = if ($Ids) { @($p.files | Where-Object { $_.id -in $Ids }) } else { @($p.files | Where-Object framework -eq $Framework | Select-Object -Skip $Skip -First $Count) }
foreach ($f in $items) {
    $a = @(Get-Content -LiteralPath (Join-Path $root $f.target) -Encoding utf8)
    Write-Output "`nID $($f.id) $($f.category)"
    $em = @($e.files | Where-Object literature_id -eq $f.id).memberships
    if ($em) { Write-Output ('E: ' + (($em | ForEach-Object { ($_.page.Split('/')[1]) + ':' + $_.role }) -join '; ')) }
    $hm = @($h.files | Where-Object id -eq $f.id).assignments
    if ($hm) { Write-Output ('H: ' + (($hm | ForEach-Object { $_.group + ':' + $_.role + ':' + $_.mode }) -join '; ')) }
    $hits = [Collections.Generic.List[int]]::new()
    if ($Pattern) {
        for ($i=0; $i -lt $a.Count; $i++) { if ($a[$i] -match $Pattern -and $a[$i].Length -gt 45 -and $a[$i] -notmatch '^#|^!\[') { $hits.Add($i) } }
    } else {
        for ($i=0; $i -lt $a.Count; $i++) {
            if ($a[$i] -match '^#+.*(突破|研究结论|研究总结|结论总结|整体研究思路)') {
                for ($j=$i+1; $j -lt [Math]::Min($i+14,$a.Count);$j++) { if ($a[$j].Length -gt 60 -and $a[$j] -notmatch '^!\[|^#') { $hits.Add($j); if ($hits.Count -ge $Limit) { break } } }
            }
            if ($hits.Count -ge $Limit) { break }
        }
        if (-not $hits.Count) { for ($i=14; $i -lt $a.Count; $i++) { if ($a[$i] -match '本研究|研究团队|作者.*(发现|鉴定|开发)|成功.*(生产|合成)' -and $a[$i].Length -gt 60 -and $a[$i] -notmatch '^#|^!\[') { $hits.Add($i) } } }
    }
    foreach ($i in @($hits | Select-Object -Unique | Select-Object -First $Limit)) { $v=$a[$i]; if($v.Length -gt $Width){$v=$v.Substring(0,$Width)+' [后文省略]'}; Write-Output "L$($i+1): $v" }
}

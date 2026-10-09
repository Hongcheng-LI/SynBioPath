param([Parameter(Mandatory=$true)][string]$PageDirectory)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrResult, Windows.Media.Ocr, ContentType=WindowsRuntime]
$null = [Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime]
$taskMethod = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetGenericArguments().Count -eq 1 -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
} | Select-Object -First 1
function Wait-OcrOperation($Operation, [Type]$ResultType) {
    $converted = $taskMethod.MakeGenericMethod($ResultType).Invoke($null, @($Operation))
    $converted.Wait()
    return $converted.Result
}
$language = [Windows.Globalization.Language]::new('en-US')
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($language)
if (-not $engine) { throw 'English Windows OCR language is unavailable' }
$results = @()
foreach ($imageFile in (Get-ChildItem -LiteralPath $PageDirectory -Filter 'page-*.png' | Sort-Object Name)) {
    $file = Wait-OcrOperation ([Windows.Storage.StorageFile]::GetFileFromPathAsync($imageFile.FullName)) ([Windows.Storage.StorageFile])
    $stream = Wait-OcrOperation ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Wait-OcrOperation ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Wait-OcrOperation ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $ocr = Wait-OcrOperation ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $results += [pscustomobject]@{page=[int]($imageFile.BaseName -replace '^page-', ''); text=($ocr.Lines | ForEach-Object {$_.Text}) -join "`n"}
    $bitmap.Dispose()
    $stream.Dispose()
    Write-Output ('OCR page ' + $imageFile.BaseName + ' complete')
}
$outputPath = Join-Path $PageDirectory 'windows-ocr.json'
[System.IO.File]::WriteAllText($outputPath, ($results | ConvertTo-Json -Depth 6), [System.Text.UTF8Encoding]::new($false))
Write-Output ('Saved ' + $results.Count + ' pages')

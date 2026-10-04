param([switch]$ValidateOnly)
# Compatibility entry point. Title-based classification has been retired.
& (Join-Path $PSScriptRoot 'build-reviewed-biosynthesis-sources.ps1') -ValidateOnly:$ValidateOnly

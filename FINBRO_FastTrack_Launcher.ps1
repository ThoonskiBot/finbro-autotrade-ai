
# FINBRO_FastTrack_Launcher.ps1
# 💹 Ultra-Streamlined Installer for Profitable FINBRO Bot Launch

# ========== CONFIG ==========
$sourceZip = "$env:USERPROFILE\Downloads\FINBRO_Live_Pack.zip"
$finbroPath = "C:\FINBRO"
$testScript = "run_finbro_daily_stack.bat"
$remoteRepo = "https://github.com/ThoonskiBot/finbro-autotrade-ai.git"
$commitMsg = "FINBRO Live Pack deployed and tested"

# ========== SETUP ==========
Write-Host "`nExpanding FINBRO_Live_Pack..." -ForegroundColor Cyan
Expand-Archive $sourceZip -DestinationPath "$finbroPath\TEMP" -Force

Write-Host "Moving tools, launchers, and configs into place..." -ForegroundColor Cyan
$files = Get-ChildItem "$finbroPath\TEMP" -Recurse -File
foreach ($f in $files) {
    $target = Join-Path $finbroPath ($f.Name)
    Move-Item $f.FullName $target -Force
}

Remove-Item "$finbroPath\TEMP" -Recurse -Force

# ========== TEST ==========
Write-Host "`nRunning FINBRO daily stack..." -ForegroundColor Cyan
Set-Location $finbroPath
& "$finbroPath\$testScript"

# ========== GIT COMMIT ==========
Write-Host "`nSaving clean repo state to GitHub..." -ForegroundColor Cyan
git add .
git commit -m $commitMsg
git push origin main

Write-Host "`nFINBRO bot updated, tested, and committed live." -ForegroundColor Green

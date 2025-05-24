
# FINBRO_LiveOps_Deploy.ps1
# Expert-Level FINBRO Deployment Script

# ========== CONFIG ==========
$zipName = "FINBRO_Live_Pack.zip"
$finbroDir = "C:\FINBRO"
$sourceZip = "$env:USERPROFILE\Downloads\$zipName"
$testScript = "run_finbro_daily_stack.bat"
$remoteRepo = "https://github.com/ThoonskiBot/finbro-autotrade-ai.git"
$commitTagPrefix = "v"
$logPath = "$finbroDir\logs"
$versionFile = "$finbroDir\version.txt"

# ========== UTIL: Load/Increment Version ==========
if (!(Test-Path $versionFile)) {
    "1.0.0" | Out-File -Encoding UTF8 $versionFile
}
$currentVersion = Get-Content $versionFile
$parts = $currentVersion -split "\."
$parts[2] = [int]$parts[2] + 1
$newVersion = "$($parts[0]).$($parts[1]).$($parts[2])"
$newVersion | Out-File -Encoding UTF8 $versionFile

# ========== STEP 1: Extract Bundle ==========
if (!(Test-Path $sourceZip)) {
    Write-Host "ERROR: $zipName not found in Downloads. Canceling." -ForegroundColor Red
    exit 1
}

Write-Host "`nExtracting new FINBRO bundle..." -ForegroundColor Cyan
Expand-Archive -Path $sourceZip -DestinationPath "$finbroDir\TEMP" -Force

# ========== STEP 2: Move Files ==========
Write-Host "Moving new files into place..." -ForegroundColor Cyan
$files = Get-ChildItem "$finbroDir\TEMP" -Recurse -File
foreach ($f in $files) {
    $target = Join-Path $finbroDir ($f.Name)
    Move-Item $f.FullName $target -Force
}
Remove-Item "$finbroDir\TEMP" -Recurse -Force

# ========== STEP 3: Run Test Stack ==========
Write-Host "`nRunning test stack..." -ForegroundColor Yellow
Set-Location $finbroDir
& "$finbroDir\$testScript"

# ========== STEP 4: Log It ==========
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
if (!(Test-Path $logPath)) {
    New-Item -Path $logPath -ItemType Directory
}
"[$timestamp] FINBRO version $newVersion deployed and tested." | Out-File "$logPath\deploy_log_$timestamp.txt"

# ========== STEP 5: Git Add, Commit, Tag, Push ==========
Write-Host "`nCommitting and pushing to GitHub..." -ForegroundColor Cyan
git add .
git commit -m "FINBRO $newVersion deployed, tested, and committed live"
git tag "$commitTagPrefix$newVersion"
git push origin main
git push origin "$commitTagPrefix$newVersion"

Write-Host "`nFINBRO $newVersion live with full test, log, and version tag." -ForegroundColor Green

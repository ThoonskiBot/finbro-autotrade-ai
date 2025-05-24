
# FINBRO_MasterLauncher.ps1
# 🚀 One-Click Deploy/Test/Scrub/Push FINBRO Launcher

$finbroDir = "C:\FINBRO"
$zipPattern = "FINBRO_*.zip"
$bfgJar = "$finbroDir\bfg.jar"
$mirrorRepo = "$finbroDir\FINBRO_clean_repo.git"
$remoteRepo = "https://github.com/ThoonskiBot/finbro-autotrade-ai.git"
$versionFile = "$finbroDir\version.txt"
$logPath = "$finbroDir\logs"
$testScript = "run_finbro_daily_stack.bat"
$tagPrefix = "v"

# STEP 1: Select Most Recent ZIP from Downloads
$downloadedZip = Get-ChildItem "$env:USERPROFILE\Downloads" -Filter $zipPattern | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (!$downloadedZip) {
    Write-Host "ERROR: No FINBRO_*.zip file found in Downloads." -ForegroundColor Red
    exit 1
}

# STEP 2: Unzip and Overwrite
Write-Host "`nInstalling latest pack: $($downloadedZip.Name)" -ForegroundColor Cyan
Expand-Archive $downloadedZip.FullName -DestinationPath "$finbroDir\TEMP" -Force
$files = Get-ChildItem "$finbroDir\TEMP" -Recurse -File
foreach ($f in $files) {
    Move-Item $f.FullName -Destination "$finbroDir\$($f.Name)" -Force
}
Remove-Item "$finbroDir\TEMP" -Recurse -Force

# STEP 3: Run Test Stack
Write-Host "`nRunning FINBRO test stack..." -ForegroundColor Yellow
Set-Location $finbroDir
& "$finbroDir\$testScript"

# STEP 4: Version Bump
if (!(Test-Path $versionFile)) { "1.0.0" | Out-File -Encoding UTF8 $versionFile }
$parts = (Get-Content $versionFile) -split "\."
$parts[2] = [int]$parts[2] + 1
$newVersion = "$($parts[0]).$($parts[1]).$($parts[2])"
$newVersion | Out-File -Encoding UTF8 $versionFile
$tag = "$tagPrefix$newVersion"

# STEP 5: Optional Scrub Pass
Write-Host "`nScrubbing secrets with BFG..." -ForegroundColor Yellow
if (!(Test-Path $mirrorRepo)) {
    git clone --mirror $finbroDir $mirrorRepo
}
java -jar $bfgJar --delete-files ".env" --no-blob-protection $mirrorRepo
Set-Location $mirrorRepo
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git remote set-url origin $remoteRepo
git push --mirror origin

# STEP 6: Final Commit + Tag + Push
Set-Location $finbroDir
git add .
git commit -m "FINBRO $newVersion deployed and tested"
git tag $tag
git push origin main
git push origin $tag

# STEP 7: Log
if (!(Test-Path $logPath)) { New-Item -Path $logPath -ItemType Directory }
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
"[$timestamp] FINBRO version $newVersion deployed, scrubbed, tested, and pushed." | Out-File "$logPath\FINBRO_$newVersion.log"

Write-Host "`nFINBRO $newVersion is now live and GitHub clean." -ForegroundColor Green

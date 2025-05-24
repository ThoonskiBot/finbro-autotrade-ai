
# FINBRO_git_cleanse_launcher.ps1
# 🔐 Cleans .env and sensitive files from Git history using BFG and pushes clean repo to GitHub

$repoPath = "C:\FINBRO"
$mirrorPath = "$repoPath\FINBRO_clean_repo.git"
$bfgJar = "$repoPath\bfg.jar"
$sensitiveFile = ".env"
$remoteUrl = "https://github.com/ThoonskiBot/finbro-autotrade-ai.git"

Write-Host "✅ Step 1: Cloning mirror of repo..." -ForegroundColor Cyan
git clone --mirror $repoPath $mirrorPath

Write-Host "✅ Step 2: Running BFG to delete $sensitiveFile from all history..." -ForegroundColor Cyan
java -jar $bfgJar --delete-files $sensitiveFile --no-blob-protection $mirrorPath

Write-Host "✅ Step 3: Pruning history and cleaning up..." -ForegroundColor Cyan
Set-Location $mirrorPath
git reflog expire --expire=now --all
git gc --prune=now --aggressive

Write-Host "✅ Step 4: Resetting remote to GitHub and force pushing clean repo..." -ForegroundColor Cyan
git remote set-url origin $remoteUrl
git push --mirror origin

Write-Host "`n🎉 FINBRO Git history successfully cleaned and pushed. You're safe to commit again." -ForegroundColor Green

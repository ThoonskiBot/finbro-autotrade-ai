
# FINBRO_SecretScrubber.ps1
# 🔐 Full Secret Scrubber for GitHub Push Protection

$finbroPath = "C:\FINBRO"
$mirrorRepo = "$finbroPath\FINBRO_clean_repo.git"
$bfgJar = "$finbroPath\bfg.jar"
$secretsFile = "$finbroPath\secrets.txt"
$remoteRepo = "https://github.com/ThoonskiBot/finbro-autotrade-ai.git"

# Step 1: Build secrets.txt if missing
if (!(Test-Path $secretsFile)) {
    Write-Host "⚙️  Creating default secrets.txt..." -ForegroundColor Yellow
    @"
# Replace OpenAI keys (sample)
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ==> REMOVED_OPENAI_KEY
"@ | Set-Content -Encoding UTF8 $secretsFile
    Write-Host "✍️  Edit secrets.txt to include all redaction patterns before continuing." -ForegroundColor Cyan
    notepad $secretsFile
    pause
}

# Step 2: Clone mirror if missing
if (!(Test-Path $mirrorRepo)) {
    Write-Host "🧱 Cloning clean mirror repo..." -ForegroundColor Cyan
    git clone --mirror $finbroPath $mirrorRepo
}

# Step 3: Run BFG
Write-Host "`n🧼 Scrubbing secrets from history with BFG..." -ForegroundColor Cyan
java -jar $bfgJar --replace-text $secretsFile $mirrorRepo

# Step 4: Prune reflogs and garbage collect
Set-Location $mirrorRepo
Write-Host "`n🧹 Cleaning Git objects..." -ForegroundColor Yellow
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Step 5: Push mirror to GitHub
Write-Host "`n🚀 Pushing scrubbed repo to GitHub (force overwrite)..." -ForegroundColor Green
git remote set-url origin $remoteRepo
git push --mirror origin

Write-Host "`n✅ FINBRO repo successfully sanitized and force-pushed to GitHub." -ForegroundColor Green

# Auto Git Commit Script for FINBRO
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$commitMessage = "✅ FINBRO Auto-Save at $timestamp"

Set-Location "C:\FINBRO"
git add .
git commit -m $commitMessage

Move-Item "$PSScriptRoot\..\tools\*" "C:\FINBRO\tools\" -Force -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\launchers\*" "C:\FINBRO\launchers\" -Force -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\scripts\*" "C:\FINBRO\scripts\" -Force -ErrorAction SilentlyContinue
Remove-Item "C:\FINBRO\launchers\test_run_*.bat" -Force -ErrorAction SilentlyContinue
Remove-Item "C:\FINBRO\scripts\upgrade_git_commit_*.bat" -Force -ErrorAction SilentlyContinue
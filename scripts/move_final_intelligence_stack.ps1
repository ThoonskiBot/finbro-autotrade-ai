Move-Item "$PSScriptRoot\..\tools\*" "C:\FINBRO\tools\" -Force -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\ui\*" "C:\FINBRO\ui\" -Force -Recurse -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\launchers\*" "C:\FINBRO\launchers\" -Force -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\scripts\*" "C:\FINBRO\scripts\" -Force -ErrorAction SilentlyContinue
Move-Item "$PSScriptRoot\..\docs\*" "C:\FINBRO\docs\" -Force -ErrorAction SilentlyContinue
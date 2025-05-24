$block = "Elite_Upgrade"
$extractPath = "$env:USERPROFILE\Downloads\FINBRO_$block"
$tools = Get-ChildItem "$extractPath\tools" -Filter *.py
foreach ($t in $tools) {
    Move-Item $t.FullName "C:\FINBRO\tools\$($t.Name)" -Force
}
Move-Item "$extractPath\run_elite_upgrade.bat" "C:\FINBRO\run_elite_upgrade.bat" -Force
Start-Process "C:\FINBRO\run_elite_upgrade.bat"
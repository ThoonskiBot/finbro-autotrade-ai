$timestamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$logFile = "C:\FINBRO\logs\finbro_output_$timestamp.txt"

if (!(Test-Path -Path "C:\FINBRO\logs")) {
    New-Item -ItemType Directory -Path "C:\FINBRO\logs"
}

Start-Transcript -Path $logFile -Append
cd "C:\FINBRO\FINBRO_Phase_16_Complete"
python finbro_runner.py
Stop-Transcript

Write-Host "✅ FINBRO run complete. Log saved to $logFile"
pause

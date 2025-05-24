$Action = New-ScheduledTaskAction -Execute "C:\FINBRO\tools\run_evening_summary.bat"
$Trigger = New-ScheduledTaskTrigger -Daily -At 6pm
Register-ScheduledTask -Action $Action -Trigger $Trigger -TaskName "FINBRO 6PM Report Push" -Description "Delivers GPT summary and PnL via email and Telegram daily" -User "SYSTEM"
@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "
\ = Get-ChildItem 'C:\FINBRO\logs\order_log_*.txt' | Sort-Object LastWriteTime -Descending | Select-Object -First 1; 
if (\.Name -ne 'order_log_latest.txt') { Copy-Item \.FullName 'C:\FINBRO\logs\order_log_latest.txt' -Force }"

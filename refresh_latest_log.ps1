$log = Get-ChildItem "C:\FINBRO\logs\order_log_*.txt" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($log.Name -ne "order_log_latest.txt") {
    Copy-Item $log.FullName "C:\FINBRO\logs\order_log_latest.txt" -Force
}

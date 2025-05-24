
# FINBRO Setup Script for PowerShell
$root = "C:\Users\Matthew\OneDrive\Desktop\FINBRO"

# Create necessary directories
$folders = @("core", "executors", "reports", "signals", "logs", "runners")
foreach ($folder in $folders) {
    $path = Join-Path $root $folder
    if (-Not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Output "✅ Created: $path"
    }
    $init = Join-Path $path "__init__.py"
    if (-Not (Test-Path $init)) {
        New-Item -ItemType File -Path $init | Out-Null
    }
}

# Create PowerShell aliases for daily tasks
$profilePath = $PROFILE
if (-Not (Test-Path $profilePath)) {
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
}

Add-Content -Path $profilePath -Value @'
function finbro-run { python "C:\Users\Matthew\OneDrive\Desktop\FINBRO\runners\daily_finbro_runner.py" }
function finbro-log { notepad "C:\Users\Matthew\OneDrive\Desktop\FINBRO\logs\trade_log.csv" }
function finbro-sig { explorer "C:\Users\Matthew\OneDrive\Desktop\FINBRO\signals" }
function finbro-summary { python "C:\Users\Matthew\OneDrive\Desktop\FINBRO\reports\trade_performance_summary.py" }
function finbro-digest { python "C:\Users\Matthew\OneDrive\Desktop\FINBRO\reports\daily_trade_digest_generator.py" }
'@

Write-Output "✅ FINBRO aliases added to PowerShell profile."
Write-Output "Please restart your PowerShell terminal to use the aliases."

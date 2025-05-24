
from tools.saf_summary_analyzer import analyze_saf_logs

def get_saf_dashboard_html():
    executed, skipped, reasons = analyze_saf_logs()
    output = "<h3>🧠 Strategy Execution Summary</h3><ul>"
    for strat in set(executed.keys()).union(skipped.keys()):
        output += f"<li><b>{strat}:</b> {executed[strat]} executed / {skipped[strat]} skipped<ul>"
        for reason, count in reasons[strat].items():
            output += f"<li>{count} skipped due to {reason}</li>"
        output += "</ul></li>"
    output += "</ul>"
    return output


from tools.feature_alpha_analyzer import analyze_feature_alpha

def get_alpha_summary_html():
    alpha = analyze_feature_alpha()
    html = "<h3>📈 Alpha by Strategy</h3><ul>"
    for k, v in alpha.items():
        html += f"<li><b>{k.title()}:</b> {v} net trades</li>"
    html += "</ul>"
    return html

# FINBRO Preview Auto-Run Snippet
try:
    from reports.preview_exporter import export_previews
    export_previews()
    print("🖼️ Preview image generated.")
except Exception as e:
    print(f"⚠️ Preview generation failed: {e}")

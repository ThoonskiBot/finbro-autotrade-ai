
def append_to_summary_journal(content, path):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n\n--- GPT Reflection ---\n")
        f.write(content)

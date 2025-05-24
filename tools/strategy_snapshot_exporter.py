# Phase 94 – Strategy Snapshot Exporter

import json
from datetime import datetime
from pathlib import Path

def export_snapshot(snapshot, out_dir="snapshots"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    filename = f"{out_dir}/snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(snapshot, f, indent=4)
    return filename
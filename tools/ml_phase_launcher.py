import importlib.util
import time
import sys
import os
from pathlib import Path

# Parse CLI args
start_phase = int(sys.argv[1]) if len(sys.argv) > 1 else 601
end_phase = int(sys.argv[2]) if len(sys.argv) > 2 else 700

print(f" Launching FINBRO ML Phases {start_phase} to {end_phase}...\n")

success = []
failed = []

# Get absolute path to the tools directory
tools_dir = Path(__file__).parent.resolve()

for i in range(start_phase, end_phase + 1):
    filename = f"phase_{i:03d}_ml_module.py"
    file_path = tools_dir / filename

    if not file_path.exists():
        print(f" Phase {i} FAILED: File not found: {file_path}\n")
        failed.append(i)
        continue

    try:
        start = time.time()
        print(f"- Running {filename}...")

        spec = importlib.util.spec_from_file_location(f"phase_{i}", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        run_fn = getattr(module, f"run_phase_{i}")
        run_fn()

        duration = round(time.time() - start, 2)
        print(f" Phase {i} completed in {duration}s\n")
        success.append(i)
    except Exception as e:
        print(f" Phase {i} FAILED: {e}\n")
        failed.append(i)

print(" All Done.")
print(f" Success: {len(success)} |  Failed: {len(failed)}")
if failed:
    print(" Failed Phases:", failed)
# === AUTOSAVE GIT COMMIT ===
import subprocess
phase_range = f"{start_phase}-{end_phase}"
try:
    subprocess.run(["powershell", "./autosave_git_commit.ps1", "-phaseRange", phase_range], check=True)
except Exception as e:
    print(f"?? Git autosave failed: {e}")
# === AUTOSAVE GIT COMMIT ===
import subprocess
phase_range = f"{start_phase}-{end_phase}"
try:
    subprocess.run(["powershell", "./autosave_git_commit.ps1", "-phaseRange", phase_range], check=True)
except Exception as e:
    print(f"?? Git autosave failed: {e}")



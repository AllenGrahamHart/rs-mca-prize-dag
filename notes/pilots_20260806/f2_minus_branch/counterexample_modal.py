#!/usr/bin/env python3
"""Run the F2 omitted-minus-branch audit in Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-f2-minus-branch-counterexample"
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[3] if len(SOURCE.parents) > 3 else Path("/repo")
OUTPUT = SOURCE.parent / "counterexample_result.json"
REMOTE_ROOT = Path("/repo")
SCRIPT = "notes/pilots_20260806/f2_minus_branch/verify_counterexample.py"
MANIFEST = "background/nodes/f2_admissible_direct_sum_grs_reduction/node.json"

image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(ROOT / SCRIPT, str(REMOTE_ROOT / SCRIPT), copy=True)
    .add_local_file(ROOT / MANIFEST, str(REMOTE_ROOT / MANIFEST), copy=True)
)
app = modal.App(APP_NAME)


@app.function(
    image=image,
    cpu=1,
    memory=1024,
    timeout=120,
    max_containers=1,
    retries=0,
)
def verify() -> dict[str, object]:
    process = subprocess.run(
        ["python3", str(REMOTE_ROOT / SCRIPT)],
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    result = {
        "schema": "f2-minus-branch-counterexample-v1",
        "app": APP_NAME,
        "status": "PASS" if process.returncode == 0 else "FAIL",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    print("F2_MINUS_BRANCH_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = verify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("F2_MINUS_BRANCH_LOCAL_RESULT " + json.dumps(result, sort_keys=True))

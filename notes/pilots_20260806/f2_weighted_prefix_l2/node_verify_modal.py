#!/usr/bin/env python3
"""Run the F2 weighted-prefix L2 node verifier in Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-f2-weighted-prefix-l2-verify"
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[3] if len(SOURCE.parents) > 3 else Path("/repo")
OUTPUT = SOURCE.parent / "node_verify_result.json"
REMOTE_ROOT = Path("/repo")
NODE = "background/nodes/f2_admissible_weighted_prefix_l2_identity"

image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_dir(ROOT / NODE, str(REMOTE_ROOT / NODE), copy=True)
    .add_local_file(ROOT / "dag.json", str(REMOTE_ROOT / "dag.json"), copy=True)
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
        ["python3", str(REMOTE_ROOT / NODE / "verify.py")],
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    result = {
        "schema": "f2-weighted-prefix-l2-verify-v1",
        "app": APP_NAME,
        "status": "PASS" if process.returncode == 0 else "FAIL",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    print("F2_WEIGHTED_PREFIX_L2_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = verify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("F2_WEIGHTED_PREFIX_L2_LOCAL_RESULT " + json.dumps(result, sort_keys=True))

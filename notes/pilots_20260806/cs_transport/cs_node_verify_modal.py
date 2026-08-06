#!/usr/bin/env python3
"""Run both candidate CS node verifiers in one bounded Modal worker."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-cs-proved-node-verification"
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[3] if len(SOURCE.parents) > 3 else Path("/repo")
NODE_ID = "rate_half_crossing_ideal_galois_multiplicity_exclusion"
NODE_DIR = ROOT / "background/nodes" / NODE_ID
PILOT_DIR = SOURCE.parent
OUTPUT = PILOT_DIR / "cs_node_verify_final_result.json"

image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_dir(NODE_DIR, f"/repo/background/nodes/{NODE_ID}", copy=True)
    .add_local_dir(
        PILOT_DIR,
        "/repo/notes/pilots_20260806/cs_transport",
        copy=True,
    )
    .add_local_file(ROOT / "dag.json", "/repo/dag.json", copy=True)
)
app = modal.App(APP_NAME)


@app.function(image=image, cpu=1, memory=1024, timeout=120, max_containers=1)
def verify() -> dict[str, object]:
    records = []
    for verifier in ("verify.py", "verify_audit.py"):
        process = subprocess.run(
            ["python3", f"/repo/background/nodes/{NODE_ID}/{verifier}"],
            text=True,
            capture_output=True,
            timeout=90,
            check=False,
        )
        records.append(
            {
                "verifier": verifier,
                "returncode": process.returncode,
                "stdout": process.stdout[-4000:],
                "stderr": process.stderr[-4000:],
            }
        )
        if process.returncode:
            break
    result = {
        "schema": "cs-proved-node-verification-v1",
        "app": APP_NAME,
        "status": "PASS" if len(records) == 2 and all(
            record["returncode"] == 0 for record in records
        ) else "FAIL",
        "records": records,
    }
    print("CS_NODE_VERIFY_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = verify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("CS_NODE_VERIFY_LOCAL_RESULT " + json.dumps(result, sort_keys=True))

#!/usr/bin/env python3
"""Replay the F2 collision-floor and minus-kernel nodes in Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


APP_NAME = "rs-mca-f2-minus-coupled-kernel"
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[3] if len(SOURCE.parents) > 3 else Path("/repo")
OUTPUT = SOURCE.parent / "coupled_kernel_result.json"
REMOTE_ROOT = Path("/repo")
NODE_PATHS = (
    "background/nodes/f2_weighted_kernel_collision_floor",
    "background/nodes/f2_minus_branch_coupled_negacyclic_reduction",
    "critical/nodes/f2_conditional_close",
)

image = modal.Image.debian_slim(python_version="3.12")
for relative in NODE_PATHS:
    image = image.add_local_dir(ROOT / relative, str(REMOTE_ROOT / relative), copy=True)
image = image.add_local_file(ROOT / "dag.json", str(REMOTE_ROOT / "dag.json"), copy=True)
image = image.add_local_file(
    ROOT / "notes/pilots_20260806/f2_minus_branch/counterexample_result.json",
    str(REMOTE_ROOT / "notes/pilots_20260806/f2_minus_branch/counterexample_result.json"),
    copy=True,
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
    records = []
    for relative in NODE_PATHS:
        process = subprocess.run(
            ["python3", str(REMOTE_ROOT / relative / "verify.py")],
            text=True,
            capture_output=True,
            timeout=90,
            check=False,
        )
        records.append(
            {
                "node": Path(relative).name,
                "returncode": process.returncode,
                "stdout": process.stdout[-4000:],
                "stderr": process.stderr[-4000:],
            }
        )
        if process.returncode:
            break
    result = {
        "schema": "f2-minus-coupled-kernel-v1",
        "app": APP_NAME,
        "status": "PASS"
        if len(records) == len(NODE_PATHS)
        and all(record["returncode"] == 0 for record in records)
        else "FAIL",
        "records": records,
    }
    print("F2_MINUS_COUPLED_KERNEL_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    result = verify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("F2_MINUS_COUPLED_KERNEL_LOCAL_RESULT " + json.dumps(result, sort_keys=True))

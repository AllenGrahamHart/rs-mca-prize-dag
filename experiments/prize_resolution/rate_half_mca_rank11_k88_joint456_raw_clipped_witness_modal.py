#!/usr/bin/env python3
"""Run the K'=88 joint 4/5/6 witness route probe on Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
NAMES = (
    "rate_half_mca_rank11_k88_joint456_raw_clipped_witness_probe.py",
    "rate_half_mca_rank11_k88_clipped_domination_falsifier_cached.py",
    "rate_half_mca_rank11_k88_clipped_scan_core.py",
    "rate_half_mca_rank11_k87_clipped_domination_falsifier_cached.py",
    "rate_half_mca_rank11_k87_clipped_domination_falsifier.py",
    "rate_half_mca_rank11_k87_clipped_scan_core.py",
    "rate_half_mca_raw_clipped_adjacent_support.py",
    "rate_half_mca_rank11_k87_best_single_domination_falsifier.py",
    "rate_half_mca_rank11_k87_best_single_scan_core.py",
    "rate_half_mca_rank11_k85_best_single_domination_falsifier.py",
    "rate_half_mca_rank11_k85_edge4_domination_falsifier.py",
)
SOURCES = tuple(DIRECTORY / name for name in NAMES)
PROBE = SOURCES[0]
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (*SOURCES, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)

app = modal.App("rate-half-mca-rank11-k88-joint456-witness")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("time")
    .pip_install("scipy==1.14.1")
)
for path in SOURCES:
    image = image.add_local_file(path, f"/root/{path.name}")
image = image.add_local_file(CODE, str(CODE)).add_local_file(DEPS, str(DEPS))


@app.function(image=image, cpu=1, memory=512, timeout=120)
def run_probe() -> dict[str, object]:
    completed = subprocess.run(
        ["/usr/bin/time", "-v", "python3", str(PROBE)],
        cwd="/tmp",
        capture_output=True,
        text=True,
        timeout=105,
    )
    rows = [
        json.loads(line)
        for line in completed.stdout.splitlines()
        if line.startswith("{")
    ]
    return {
        "event": "JOB_RESULT",
        "exit": completed.returncode,
        "result": rows[-1] if rows else None,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


@app.local_entrypoint()
def main() -> None:
    row = run_probe.remote()
    print(json.dumps(row, sort_keys=True), flush=True)
    if row["exit"] != 0 or row["result"] is None:
        raise RuntimeError("probe failed")

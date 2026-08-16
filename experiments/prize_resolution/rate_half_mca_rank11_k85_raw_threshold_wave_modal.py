#!/usr/bin/env python3
"""Bounded paired Modal dispatcher for the K'=85 raw-threshold wave."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


ROOT = Path(__file__).resolve().parents[2]
PRIMARY = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_k85_raw_threshold_offset_probe.py"
AUDIT = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_k85_raw_threshold_offset_audit.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (PRIMARY, AUDIT, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k85-raw-threshold-wave")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("time")
    .add_local_file(PRIMARY, "/root/primary.py")
    .add_local_file(AUDIT, "/root/audit.py")
    .add_local_file(CODE, "/root/code.tar.gz")
    .add_local_file(DEPS, "/root/deps.tar.gz")
)


def peak_mb(stderr: str) -> int:
    for line in stderr.splitlines():
        if "Maximum resident set size" in line:
            return (int(line.rsplit(":", 1)[1].strip()) + 1023) // 1024
    return -1


@app.function(image=image, cpu=1, memory=256, timeout=180)
def run_job(implementation: str, offset: int) -> dict[str, object]:
    script = "/root/primary.py" if implementation == "primary" else "/root/audit.py"
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-v", "python3", script, str(offset)],
            cwd="/root",
            capture_output=True,
            text=True,
            timeout=165,
        )
        return {
            "event": "JOB_RESULT",
            "job": f"{implementation}:offset{offset}",
            "exit": completed.returncode,
            "timed_out": False,
            "peak_mb": peak_mb(completed.stderr),
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "event": "JOB_RESULT",
            "job": f"{implementation}:offset{offset}",
            "exit": None,
            "timed_out": True,
            "peak_mb": -1,
            "stdout": exc.stdout or "",
            "stderr": exc.stderr or "",
        }


@app.local_entrypoint()
def main() -> None:
    jobs = [
        (implementation, offset)
        for implementation in ("primary", "audit")
        for offset in range(1, 75)
    ]
    completed = failures = 0
    for row in run_job.starmap(jobs, order_outputs=False):
        print(json.dumps(row, sort_keys=True), flush=True)
        completed += 1
        failures += int(
            row["timed_out"]
            or row["exit"] != 0
            or not (0 < int(row["peak_mb"]) <= 128)
        )
    event = "BATCH_PASS" if completed == len(jobs) and failures == 0 else "BATCH_INCOMPLETE"
    print(json.dumps({
        "event": event,
        "completed": completed,
        "expected": len(jobs),
        "failures": failures,
    }, sort_keys=True), flush=True)
    if event != "BATCH_PASS":
        raise RuntimeError(event)

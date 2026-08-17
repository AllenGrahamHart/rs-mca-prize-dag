#!/usr/bin/env python3
"""Bounded paired Modal dispatcher for the K'=85 raw-threshold wave."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
PRIMARY = DIRECTORY / "rate_half_mca_rank11_k85_raw_threshold_offset_probe.py"
AUDIT = DIRECTORY / "rate_half_mca_rank11_k85_raw_threshold_offset_audit.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (PRIMARY, AUDIT, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k85-raw-threshold-wave")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("time")
    .add_local_file(PRIMARY, f"/root/{PRIMARY.name}")
    .add_local_file(AUDIT, f"/root/{AUDIT.name}")
    .add_local_file(CODE, str(CODE))
    .add_local_file(DEPS, str(DEPS))
)


def peak_mb(stderr: str) -> int:
    for line in stderr.splitlines():
        if "Maximum resident set size" in line:
            return (int(line.rsplit(":", 1)[1].strip()) + 1023) // 1024
    return -1


@app.function(image=image, cpu=1, memory=256, timeout=180)
def run_job(implementation: str, offset: int) -> dict[str, object]:
    script = str(PRIMARY if implementation == "primary" else AUDIT)
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-v", "python3", script, str(offset)],
            cwd="/tmp",
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
def main(smoke: bool = False) -> None:
    offsets = (1, 74) if smoke else range(1, 75)
    jobs = [
        (implementation, offset)
        for implementation in ("primary", "audit")
        for offset in offsets
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

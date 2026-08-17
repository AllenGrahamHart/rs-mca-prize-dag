#!/usr/bin/env python3
"""Bounded paired Modal dispatcher for the K'=88 raw-threshold probe."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PROBE = HERE / "rate_half_mca_rank11_k88_raw_threshold_offset_probe.py"
PRIMARY_BASE = HERE / "rate_half_mca_rank11_k85_raw_threshold_offset_probe.py"
AUDIT_BASE = HERE / "rate_half_mca_rank11_k85_raw_threshold_offset_audit.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (PROBE, PRIMARY_BASE, AUDIT_BASE, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)

app = modal.App("rate-half-mca-rank11-k88-raw-threshold-wave")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("time")
    .add_local_file(PROBE, f"/root/{PROBE.name}")
    .add_local_file(PRIMARY_BASE, f"/root/{PRIMARY_BASE.name}")
    .add_local_file(AUDIT_BASE, f"/root/{AUDIT_BASE.name}")
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
    try:
        completed = subprocess.run(
            [
                "/usr/bin/time", "-v", "python3", f"/root/{PROBE.name}",
                implementation, str(offset),
            ],
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
    offsets = (1, 77) if smoke else range(1, 78)
    jobs = [
        (implementation, offset)
        for implementation in ("primary", "audit")
        for offset in offsets
    ]
    failures = 0
    completed = 0
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
        "smoke": smoke,
    }, sort_keys=True), flush=True)
    if event != "BATCH_PASS":
        raise RuntimeError(event)

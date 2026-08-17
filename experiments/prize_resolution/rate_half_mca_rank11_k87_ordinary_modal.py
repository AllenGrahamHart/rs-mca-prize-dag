#!/usr/bin/env python3
"""Run the paired K'=87 ordinary lane through one remote Modal call."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
PRIMARY = DIRECTORY / "rate_half_mca_rank11_k87_threshold_frontier_replay.py"
AUDIT = DIRECTORY / "rate_half_mca_rank11_k87_threshold_frontier_audit.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (PRIMARY, AUDIT, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k87-ordinary")
image = modal.Image.debian_slim(python_version="3.12").apt_install("time")
for path in (PRIMARY, AUDIT):
    image = image.add_local_file(path, f"/root/{path.name}")
image = image.add_local_file(CODE, str(CODE)).add_local_file(DEPS, str(DEPS))


def peak_mb(stderr: str) -> int:
    for line in stderr.splitlines():
        if "Maximum resident set size" in line:
            return (int(line.rsplit(":", 1)[1].strip()) + 1023) // 1024
    return -1


def run_child(implementation: str) -> dict[str, object]:
    script = PRIMARY.name if implementation == "primary" else AUDIT.name
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-v", "python3", f"/root/{script}"],
            cwd="/tmp",
            capture_output=True,
            text=True,
            timeout=900,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        return {
            "event": "JOB_RESULT",
            "job": f"{implementation}:ordinary",
            "exit": None,
            "timed_out": True,
            "peak_mb": -1,
            "partial_stdout": stdout,
        }
    return {
        "event": "JOB_RESULT",
        "job": f"{implementation}:ordinary",
        "exit": completed.returncode,
        "timed_out": False,
        "peak_mb": peak_mb(completed.stderr),
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout": completed.stdout,
        "stderr": completed.stderr if completed.returncode else "",
    }


@app.function(image=image, cpu=1, memory=1024, timeout=1815)
def run_pair() -> list[dict[str, object]]:
    return [run_child(implementation) for implementation in ("primary", "audit")]


@app.local_entrypoint()
def main() -> None:
    rows = run_pair.remote()
    failures = 0
    for row in rows:
        print(json.dumps(row, sort_keys=True), flush=True)
        failures += int(
            row["timed_out"]
            or row["exit"] != 0
            or not (0 < int(row["peak_mb"]) <= 128)
        )
    event = "BATCH_COMPLETE" if len(rows) == 2 and failures == 0 else "BATCH_INCOMPLETE"
    print(json.dumps({
        "event": event,
        "completed": len(rows),
        "expected": 2,
        "infrastructure_failures": failures,
    }, sort_keys=True), flush=True)
    if event != "BATCH_COMPLETE":
        raise RuntimeError(event)

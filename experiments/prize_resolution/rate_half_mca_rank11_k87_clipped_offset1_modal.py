#!/usr/bin/env python3
"""Paired exhaustive K'=87 raw-clipped stress on offset 1."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
NAMES = (
    "rate_half_mca_rank11_k87_clipped_domination_falsifier.py",
    "rate_half_mca_rank11_k87_clipped_domination_audit.py",
    "rate_half_mca_rank11_k87_clipped_scan_core.py",
    "rate_half_mca_raw_clipped_adjacent_support.py",
    "rate_half_mca_rank11_k87_best_single_domination_falsifier.py",
    "rate_half_mca_rank11_k87_best_single_domination_audit.py",
    "rate_half_mca_rank11_k87_best_single_scan_core.py",
    "rate_half_mca_rank11_k85_best_single_domination_falsifier.py",
    "rate_half_mca_rank11_k85_best_single_domination_audit.py",
    "rate_half_mca_rank11_k85_edge4_domination_falsifier.py",
)
SOURCES = tuple(DIRECTORY / name for name in NAMES)
PRIMARY, AUDIT = SOURCES[0], SOURCES[1]
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (*SOURCES, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k87-clipped-offset1")
image = modal.Image.debian_slim(python_version="3.12").apt_install("time")
for path in SOURCES:
    image = image.add_local_file(path, f"/root/{path.name}")
image = image.add_local_file(CODE, str(CODE)).add_local_file(DEPS, str(DEPS))


def peak_mb(stderr: str) -> int:
    for line in stderr.splitlines():
        if "Maximum resident set size" in line:
            return (int(line.rsplit(":", 1)[1].strip()) + 1023) // 1024
    return -1


def json_rows(output: str):
    for line in output.splitlines():
        if line.startswith("{"):
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


@app.function(image=image, cpu=1, memory=256, timeout=735)
def run_job(implementation: str) -> dict[str, object]:
    script = PRIMARY if implementation == "primary" else AUDIT
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-v", "python3", str(script), "1"],
            cwd="/tmp",
            capture_output=True,
            text=True,
            timeout=720,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        return {
            "event": "JOB_RESULT",
            "job": implementation,
            "exit": None,
            "timed_out": True,
            "peak_mb": -1,
            "partial_stdout": stdout,
        }
    rows = list(json_rows(completed.stdout))
    terminal = [
        row for row in rows if row.get("event") in {"FALSIFIED", "SURVIVED"}
    ]
    return {
        "event": "JOB_RESULT",
        "job": implementation,
        "exit": completed.returncode,
        "timed_out": False,
        "peak_mb": peak_mb(completed.stderr),
        "progress_rows": sum(row.get("event") == "PROGRESS" for row in rows),
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "result": terminal[0] if len(terminal) == 1 else None,
        "stderr": completed.stderr if completed.returncode else "",
    }


@app.local_entrypoint()
def main() -> None:
    jobs = (("primary",), ("audit",))
    completed = failures = 0
    for row in run_job.starmap(jobs, order_outputs=False):
        print(json.dumps(row, sort_keys=True), flush=True)
        completed += 1
        failures += int(
            row["timed_out"]
            or row["exit"] != 0
            or not (0 < int(row["peak_mb"]) <= 128)
            or row["result"] is None
        )
    event = (
        "BATCH_COMPLETE"
        if completed == 2 and failures == 0
        else "BATCH_INCOMPLETE"
    )
    print(json.dumps({
        "event": event,
        "completed": completed,
        "expected": 2,
        "infrastructure_failures": failures,
    }, sort_keys=True), flush=True)
    if event != "BATCH_COMPLETE":
        raise RuntimeError(event)

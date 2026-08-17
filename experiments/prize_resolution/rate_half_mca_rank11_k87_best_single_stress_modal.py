#!/usr/bin/env python3
"""Paired bounded stress wave for K'=87 best-single domination."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
PRIMARY = DIRECTORY / "rate_half_mca_rank11_k87_best_single_domination_falsifier.py"
AUDIT = DIRECTORY / "rate_half_mca_rank11_k87_best_single_domination_audit.py"
CORE = DIRECTORY / "rate_half_mca_rank11_k87_best_single_scan_core.py"
K85_PRIMARY = DIRECTORY / "rate_half_mca_rank11_k85_best_single_domination_falsifier.py"
K85_AUDIT = DIRECTORY / "rate_half_mca_rank11_k85_best_single_domination_audit.py"
K85_BASE = DIRECTORY / "rate_half_mca_rank11_k85_edge4_domination_falsifier.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
SOURCES = (PRIMARY, AUDIT, CORE, K85_PRIMARY, K85_AUDIT, K85_BASE, CODE, DEPS)
for path in SOURCES:
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k87-best-single-stress")
image = modal.Image.debian_slim(python_version="3.12").apt_install("time")
for path in SOURCES[:-2]:
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


@app.function(image=image, cpu=1, memory=256, timeout=375)
def run_job(implementation: str, offset: int) -> dict[str, object]:
    script = PRIMARY if implementation == "primary" else AUDIT
    try:
        completed = subprocess.run(
            ["/usr/bin/time", "-v", "python3", str(script), str(offset)],
            cwd="/tmp",
            capture_output=True,
            text=True,
            timeout=360,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        return {
            "event": "JOB_RESULT",
            "job": f"{implementation}:offset{offset}",
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
        "job": f"{implementation}:offset{offset}",
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
    offsets = (1, 9, 23, 43)
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
            or row["result"] is None
        )
    event = (
        "BATCH_COMPLETE"
        if completed == len(jobs) and failures == 0
        else "BATCH_INCOMPLETE"
    )
    print(json.dumps({
        "event": event,
        "completed": completed,
        "expected": len(jobs),
        "infrastructure_failures": failures,
    }, sort_keys=True), flush=True)
    if event != "BATCH_COMPLETE":
        raise RuntimeError(event)

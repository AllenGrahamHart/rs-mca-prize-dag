#!/usr/bin/env python3
"""Run a K'=87 clipped-wave range in two sequential remote workers."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
NAMES = (
    "rate_half_mca_rank11_k87_clipped_domination_falsifier_cached.py",
    "rate_half_mca_rank11_k87_clipped_domination_audit_cached.py",
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


app = modal.App("rate-half-mca-rank11-k87-clipped-wave-range")
image = modal.Image.debian_slim(python_version="3.12").apt_install("time")
for path in SOURCES:
    image = image.add_local_file(path, f"/root/{path.name}")
image = image.add_local_file(CODE, str(CODE)).add_local_file(DEPS, str(DEPS))


def peak_mb(stderr: str) -> int:
    for line in stderr.splitlines():
        if "Maximum resident set size" in line:
            return (int(line.rsplit(":", 1)[1].strip()) + 1023) // 1024
    return -1


@app.function(image=image, cpu=1, memory=256, timeout=7215)
def run_range(implementation: str, start: int, end: int):
    script = PRIMARY if implementation == "primary" else AUDIT
    results = []
    for offset in range(start, end + 1):
        try:
            completed = subprocess.run(
                ["/usr/bin/time", "-v", "python3", str(script), str(offset)],
                cwd="/tmp",
                capture_output=True,
                text=True,
                timeout=900,
            )
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode(errors="replace")
            results.append({
                "event": "JOB_RESULT",
                "job": f"{implementation}:offset{offset}",
                "exit": None,
                "timed_out": True,
                "peak_mb": -1,
                "partial_stdout": stdout,
            })
            continue
        rows = []
        for line in completed.stdout.splitlines():
            if line.startswith("{"):
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        terminal = [
            row for row in rows
            if row.get("event") in {"FALSIFIED", "SURVIVED"}
        ]
        results.append({
            "event": "JOB_RESULT",
            "job": f"{implementation}:offset{offset}",
            "exit": completed.returncode,
            "timed_out": False,
            "peak_mb": peak_mb(completed.stderr),
            "progress_rows": sum(
                row.get("event") == "PROGRESS" for row in rows
            ),
            "stdout_sha256": hashlib.sha256(
                completed.stdout.encode()
            ).hexdigest(),
            "result": terminal[0] if len(terminal) == 1 else None,
            "stderr": completed.stderr if completed.returncode else "",
        })
    return results


@app.local_entrypoint()
def main(start: int, end: int) -> None:
    if not (1 <= start <= end <= 43):
        raise ValueError((start, end))
    completed = failures = 0
    remote_jobs = (
        ("primary", start, end),
        ("audit", start, end),
    )
    for batch in run_range.starmap(remote_jobs, order_outputs=False):
        for row in batch:
            print(json.dumps(row, sort_keys=True), flush=True)
            completed += 1
            failures += int(
                row["timed_out"]
                or row["exit"] != 0
                or not (0 < int(row["peak_mb"]) <= 128)
                or row.get("result") is None
            )
    expected = 2 * (end - start + 1)
    event = (
        "BATCH_COMPLETE"
        if completed == expected and failures == 0
        else "BATCH_INCOMPLETE"
    )
    print(json.dumps({
        "event": event,
        "completed": completed,
        "expected": expected,
        "infrastructure_failures": failures,
        "start": start,
        "end": end,
    }, sort_keys=True), flush=True)
    if event != "BATCH_COMPLETE":
        raise RuntimeError(event)

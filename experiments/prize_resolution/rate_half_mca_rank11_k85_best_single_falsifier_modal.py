#!/usr/bin/env python3
"""Run one K'=85 best-single-edge falsifier with witness audit."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
SCAN = DIRECTORY / "rate_half_mca_rank11_k85_best_single_domination_falsifier.py"
BASE = DIRECTORY / "rate_half_mca_rank11_k85_edge4_domination_falsifier.py"
AUDIT = DIRECTORY / "rate_half_mca_rank11_k85_best_single_witness_audit.py"
CODE = Path("/tmp/k83-threshold-frontier-adjacent-code.tar.gz")
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (SCAN, BASE, AUDIT, CODE, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k85-best-single-falsifier")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(SCAN, f"/root/{SCAN.name}")
    .add_local_file(BASE, f"/root/{BASE.name}")
    .add_local_file(AUDIT, f"/root/{AUDIT.name}")
    .add_local_file(CODE, str(CODE))
    .add_local_file(DEPS, str(DEPS))
)


def rows(text: str):
    return [json.loads(line) for line in text.splitlines() if line.startswith("{")]


@app.function(image=image, cpu=1, memory=256, timeout=240)
def run(offset: int) -> dict[str, object]:
    scan = subprocess.run(
        ["python3", str(SCAN), str(offset)],
        cwd="/tmp",
        capture_output=True,
        text=True,
        timeout=215,
    )
    terminal = [
        row for row in rows(scan.stdout)
        if row.get("event") in {"FALSIFIED", "SURVIVED"}
    ]
    if scan.returncode != 0 or len(terminal) != 1:
        return {
            "event": "INCOMPLETE",
            "scan_exit": scan.returncode,
            "scan_stdout": scan.stdout,
            "scan_stderr": scan.stderr,
        }
    result = terminal[0]
    audit_payload = None
    if result["event"] == "FALSIFIED":
        audit = subprocess.run(
            [
                "python3", str(AUDIT), str(offset), str(result["m2"]),
                str(result["s4"]), str(result["s5"]), str(result["case"]),
            ],
            cwd="/tmp",
            capture_output=True,
            text=True,
            timeout=15,
        )
        payload = rows(audit.stdout)
        if audit.returncode != 0 or len(payload) != 1:
            return {
                "event": "INCOMPLETE",
                "scan": result,
                "audit_exit": audit.returncode,
                "audit_stdout": audit.stdout,
                "audit_stderr": audit.stderr,
            }
        audit_payload = payload[0]
        keys = (
            "offset", "m2", "s2", "s3", "s4", "s5", "case", "charges",
            "single_edges", "raw_before", "raw_before_high", "single_after",
            "single_high", "leader", "excess_over_leader",
        )
        assert all(result[key] == audit_payload[key] for key in keys)
    return {"event": "PASS", "scan": result, "audit": audit_payload}


@app.local_entrypoint()
def main(offset: int = 11) -> None:
    result = run.remote(offset)
    print(json.dumps(result, sort_keys=True), flush=True)
    if result.get("event") != "PASS":
        raise RuntimeError("INCOMPLETE")

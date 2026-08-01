#!/usr/bin/env python3
"""Cheap Modal replay of residual sum failures in the F29 cell-5 lane."""

import itertools
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
TRACE = DIRECTORY / "rate_half_kb_positive_433_1a_sum_failure_trace.c"
BASE = DIRECTORY / "rate_half_kb_positive_433_1a_common_chart_probe.c"
REMOTE_TRACE = "/root/rate_half_kb_positive_433_1a_sum_failure_trace.c"
REMOTE_BASE = "/root/rate_half_kb_positive_433_1a_common_chart_probe.c"
REMOTE_BINARY = "/tmp/sum-failure-trace"

app = modal.App("rs-mca-positive-433-1a-sum-failure-trace")
image = (
    modal.Image.debian_slim()
    .apt_install("gcc")
    .add_local_file(TRACE, REMOTE_TRACE)
    .add_local_file(BASE, REMOTE_BASE)
)


@app.function(image=image, cpu=0.5, memory=256, timeout=60, max_containers=8)
def trace_case(case):
    epsilon_1, epsilon_2, alignment = case
    compiler = subprocess.run(
        ["gcc", "-O3", "-std=c11", REMOTE_TRACE, "-o", REMOTE_BINARY],
        capture_output=True, text=True, timeout=15,
    )
    if compiler.returncode:
        return {"status": "COMPILE_ERROR", "case": case,
                "stderr": compiler.stderr}
    try:
        process = subprocess.run(
            [REMOTE_BINARY, "29", "5", str(epsilon_1), str(epsilon_2),
             "1", str(alignment)],
            capture_output=True, text=True, timeout=40,
        )
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "case": case}
    if process.returncode:
        return {"status": "ERROR", "case": case,
                "stdout": process.stdout, "stderr": process.stderr}
    return {"status": "COMPLETE", "trace": process.stderr.splitlines(),
            **json.loads(process.stdout)}


@app.local_entrypoint()
def main():
    cases = ((-1, -1, 0), (-1, -1, 1))
    print(json.dumps({
        "scope": (
            "F29 cell 5 cycle +1 diagnostic only; maximum residual squared-"
            "sum rows among product-compatible lifts; no deployed-field claim"
        ),
        "results": list(trace_case.map(cases)),
    }, sort_keys=True))

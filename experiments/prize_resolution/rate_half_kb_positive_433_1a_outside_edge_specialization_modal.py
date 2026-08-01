#!/usr/bin/env python3
"""Bounded Modal pilot for specialized positive 433-1a edge cuts."""

import itertools
import json
from pathlib import Path
import subprocess

import modal


APP_NAME = "rs-mca-positive-433-1a-edge-specialization"
DIRECTORY = Path(__file__).parent
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
BASE = DIRECTORY / "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
REMOTE_PROBE = "/root/probe.py"
REMOTE_BASE = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROBE, REMOTE_PROBE)
    .add_local_file(BASE, REMOTE_BASE)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=90, max_containers=4)
def compile_case(case):
    cell, epsilon_1, epsilon_2, cycle_sign, edge = case
    command = [
        "python3", REMOTE_PROBE,
        "--cell", str(cell),
        "--epsilon-1", str(epsilon_1),
        "--epsilon-2", str(epsilon_2),
        "--cycle-sign", str(cycle_sign),
        "--edge", edge,
    ]
    try:
        process = subprocess.run(
            command, capture_output=True, text=True, timeout=75
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "case": case,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr),
        }
    lines = [json.loads(line) for line in process.stdout.splitlines() if line]
    return {
        "case": case,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "records": lines,
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main(cell: int = 5, cycle_sign: int = 1, edge: str = "ef"):
    cases = tuple(
        (cell, epsilon_1, epsilon_2, cycle_sign, edge)
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2)
    )
    print(json.dumps({
        "app": APP_NAME,
        "scope": "one-cell one-edge symbolic size pilot; no route conclusion",
        "results": list(compile_case.map(cases)),
    }, sort_keys=True))

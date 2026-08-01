#!/usr/bin/env python3
"""Bounded Modal pilot for the sparse positive 433-1a cell-5 edge cut."""

import json
from pathlib import Path
import subprocess

import modal


APP_NAME = "rs-mca-positive-433-1a-cell5-sparse-edge"
DIRECTORY = Path(__file__).parent
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_PROBE = "/root/probe.py"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROBE, REMOTE_PROBE)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=100)
def compile_case(cycle_sign, edge):
    command = [
        "python3", REMOTE_PROBE,
        "--cycle-sign", str(cycle_sign),
        "--edge", edge,
    ]
    try:
        process = subprocess.run(
            command, capture_output=True, text=True, timeout=85
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr),
        }
    return {
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main(cycle_sign: int = 1, edge: str = "ef"):
    print(json.dumps({
        "app": APP_NAME,
        "scope": "one exact sparse-normalization size pilot; no route conclusion",
        "result": compile_case.remote(cycle_sign, edge),
    }, sort_keys=True))

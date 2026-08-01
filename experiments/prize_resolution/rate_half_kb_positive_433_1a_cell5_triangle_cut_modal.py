#!/usr/bin/env python3
"""Bounded Modal compilation of target-free cell-5 triangle cuts."""

import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_triangle_cut_probe.py"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_PROBE = "/root/probe.py"
REMOTE_KERNEL = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"

app = modal.App("rs-mca-positive-433-1a-cell5-triangle-cut")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PROBE, REMOTE_PROBE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=100, max_containers=2)
def compile_cut(template):
    try:
        process = subprocess.run(
            ["python3", REMOTE_PROBE, "--template", template],
            capture_output=True, text=True, timeout=85,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "template": template,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr),
        }
    return {
        "template": template,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main():
    print(json.dumps({
        "scope": (
            "two exact target-free cell-5 triangle cut size pilots; "
            "no route or deployed-field conclusion"
        ),
        "results": list(compile_cut.map(("A", "B"))),
    }, sort_keys=True))

#!/usr/bin/env python3
"""Run the deployed-field cell-5 ratio compiler on Modal."""

import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_ratio_compiler.py"
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_ratio_result.json"
REMOTE_SCRIPT = "/root/rate_half_kb_positive_433_1a_cell5_ratio_compiler.py"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_RESULT = "/root/rate_half_kb_positive_433_1a_cell5_ratio_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-ratio-compiler")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SCRIPT, REMOTE_SCRIPT)
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(RESULT, REMOTE_RESULT)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=120)
def compile_ratio():
    process = subprocess.run(
        ["python", REMOTE_SCRIPT], capture_output=True, text=True, timeout=105
    )
    return {
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    print(json.dumps({
        "scope": (
            "exact deployed-field cell-5 ratio compiler; no denominator-"
            "branch, outside-system, route, row, or Prize conclusion"
        ),
        "result": compile_ratio.remote(),
    }, sort_keys=True))

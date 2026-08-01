#!/usr/bin/env python3
"""Replay the deployed cell-5 ratio exceptional branch on Modal."""

import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMPILER = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_ratio_exceptional_compiler.py"
)
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
REMOTE_COMPILER = "/root/ratio_exceptional_compiler.py"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"

app = modal.App("rs-mca-positive-433-1a-cell5-ratio-exceptional")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(COMMON, REMOTE_COMMON)
)


@app.function(image=image, cpu=1.0, memory=1536, timeout=150)
def test_exceptional():
    import importlib.util

    specification = importlib.util.spec_from_file_location(
        "compiler", REMOTE_COMPILER
    )
    compiler = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(compiler)
    compiled = compiler.compile_program()
    program = compiled.pop("program")
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=125,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **compiled,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr),
        }
    return {
        **compiled,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    print(json.dumps({
        "scope": (
            "one exact deployed-field guarded ratio-chart exceptional "
            "branch; no generic, outside, route, row, or Prize conclusion"
        ),
        "result": test_exceptional.remote(),
    }, sort_keys=True))

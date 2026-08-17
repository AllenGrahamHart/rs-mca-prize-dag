#!/usr/bin/env python3
"""Run the rank-11 factor-flag recursion probe on one small Modal worker."""

from __future__ import annotations

import subprocess
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PROBE = HERE / "rate_half_mca_rank11_factor_flag_recursion_probe.py"

app = modal.App("rate-half-mca-rank11-factor-flag-recursion-probe")
image = modal.Image.debian_slim(python_version="3.12").add_local_file(
    PROBE, f"/root/{PROBE.name}"
)


@app.function(image=image, cpu=1, memory=256, timeout=60)
def run() -> tuple[int, str, str]:
    completed = subprocess.run(
        ["python3", f"/root/{PROBE.name}"],
        capture_output=True,
        text=True,
        timeout=45,
    )
    return completed.returncode, completed.stdout, completed.stderr


@app.local_entrypoint()
def main() -> None:
    code, stdout, stderr = run.remote()
    print(stdout, end="")
    if stderr:
        print(stderr, end="")
    if code:
        raise SystemExit(code)

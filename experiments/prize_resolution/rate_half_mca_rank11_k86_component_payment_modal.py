#!/usr/bin/env python3
"""Run the exact K'=86 component payment on Modal."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


DIRECTORY = Path(__file__).resolve().parent
PAYMENT = DIRECTORY / "rate_half_mca_rank11_k86_component_payment.py"
DEPS = Path("/tmp/k72-deps.tar.gz")
for path in (PAYMENT, DEPS):
    if not path.is_file():
        raise FileNotFoundError(path)


app = modal.App("rate-half-mca-rank11-k86-component-payment")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(PAYMENT, f"/root/{PAYMENT.name}")
    .add_local_file(DEPS, str(DEPS))
)


@app.function(image=image, cpu=1, memory=256, timeout=30)
def run() -> dict[str, object]:
    completed = subprocess.run(
        ["python3", str(PAYMENT)],
        cwd="/tmp",
        capture_output=True,
        text=True,
        timeout=20,
    )
    rows = [
        json.loads(line)
        for line in completed.stdout.splitlines()
        if line.startswith("{")
    ]
    if completed.returncode != 0 or len(rows) != 1:
        return {
            "event": "INCOMPLETE",
            "exit": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
    return rows[0]


@app.local_entrypoint()
def main() -> None:
    result = run.remote()
    print(json.dumps(result, sort_keys=True), flush=True)
    if result.get("status") != "PASS":
        raise RuntimeError("INCOMPLETE")

#!/usr/bin/env python3
"""Run the weight-six certificate verifier on Modal with a diagnostic timeout."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[4]
RELATIVE = (
    "background/nodes/dli_wcl_ell2_weight6_recursive_norm_exclusion/verify.py"
)
app = modal.App("rs-mca-dli-wcl-weight6-certificate-verify")
image = modal.Image.debian_slim().add_local_dir(
    str(ROOT), remote_path="/repo", copy=True
)


@app.function(image=image, cpu=1, memory=2048, timeout=900)
def verify_remote() -> dict[str, object]:
    started = time.monotonic()
    completed = subprocess.run(
        ["python3", RELATIVE],
        cwd="/repo",
        capture_output=True,
        text=True,
        timeout=840,
    )
    return {
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


@app.local_entrypoint()
def main() -> None:
    print(verify_remote.remote())

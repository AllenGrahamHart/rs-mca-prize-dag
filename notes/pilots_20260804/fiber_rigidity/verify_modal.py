#!/usr/bin/env python3
"""One-container Modal launcher for the independent full fixture audit."""

from __future__ import annotations

from pathlib import Path

import modal


REMOTE_VERIFY = "/repo/notes/pilots_20260804/fiber_rigidity/verify.py"
REMOTE_CERTIFICATE = "/repo/notes/pilots_20260804/fiber_rigidity/fixture.json"
HERE = Path(__file__).resolve().parent
if Path(REMOTE_VERIFY).exists():
    VERIFY = Path(REMOTE_VERIFY)
    CERTIFICATE = Path(REMOTE_CERTIFICATE)
else:
    VERIFY = HERE / "verify.py"
    CERTIFICATE = HERE / "fixture.json"

app = modal.App("rs-mca-xr-fiber-rigidity-boundary-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(str(VERIFY), REMOTE_VERIFY, copy=True)
    .add_local_file(str(CERTIFICATE), REMOTE_CERTIFICATE, copy=True)
)


@app.function(image=image, cpu=2.0, memory=1024, timeout=280, max_containers=1)
def run_audit() -> dict:
    import subprocess

    completed = subprocess.run(
        [
            "python3",
            REMOTE_VERIFY,
            REMOTE_CERTIFICATE,
            "--full-scan",
            "--tamper-selftest",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=270,
        check=False,
    )
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout[-20000:],
    }


@app.local_entrypoint()
def main() -> None:
    result = run_audit.remote()
    print(result["stdout"], end="")
    if result["returncode"] != 0:
        raise RuntimeError(f"remote audit failed: returncode={result['returncode']}")
    if "XR_FIBER_RIGIDITY_INDEPENDENT_AUDIT_PASS" not in result["stdout"]:
        raise RuntimeError("remote audit marker missing")

#!/usr/bin/env python3
"""One-container Modal launcher for the exact fiber-rigidity fixture."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


REMOTE_FIXTURE = "/repo/notes/pilots_20260804/fiber_rigidity/fixture.py"
REMOTE_ALGEBRA = "/repo/notes/pilots_20260803/sl2_unstructured/algebra.py"

HERE = Path(__file__).resolve().parent
if Path(REMOTE_FIXTURE).exists():
    # Modal imports the launcher from /root; the packaged sources already
    # live at their remote paths at that point.
    FIXTURE = Path(REMOTE_FIXTURE)
    ALGEBRA = Path(REMOTE_ALGEBRA)
else:
    FIXTURE = HERE / "fixture.py"
    ALGEBRA = HERE.parents[1] / "pilots_20260803/sl2_unstructured/algebra.py"
OUTPUT = HERE / "fixture.json"

app = modal.App("rs-mca-xr-fiber-rigidity-boundary-fixture")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .add_local_file(str(FIXTURE), REMOTE_FIXTURE, copy=True)
    .add_local_file(str(ALGEBRA), REMOTE_ALGEBRA, copy=True)
)


@app.function(image=image, cpu=2.0, memory=1024, timeout=280, max_containers=1)
def run_fixture(seed: int) -> dict:
    import subprocess

    output = "/tmp/fiber_rigidity_fixture.json"
    completed = subprocess.run(
        [
            "python3",
            REMOTE_FIXTURE,
            "--seed",
            str(seed),
            "--max-seeds",
            "1",
            "--output",
            output,
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=270,
        check=False,
    )
    result_path = Path(output)
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout[-20000:],
        "complete": completed.returncode == 0 and result_path.exists(),
        "certificate": result_path.read_text(encoding="ascii")
        if result_path.exists()
        else None,
    }


@app.local_entrypoint()
def main(seed: int = 20260806, output: str = str(OUTPUT)) -> None:
    result = run_fixture.remote(seed)
    print(result["stdout"], end="")
    if not result["complete"]:
        raise RuntimeError(
            f"remote fixture incomplete: returncode={result['returncode']}"
        )
    encoded = result["certificate"]
    payload = json.loads(encoded)
    if payload.get("verdict") != "COUNTEREXAMPLE_TO_FIELD_INDEPENDENT_FR":
        raise RuntimeError("unexpected remote verdict")
    Path(output).write_text(encoded, encoding="ascii")
    print(
        "XR_FIBER_RIGIDITY_MODAL_PASS "
        f"sha256={hashlib.sha256(encoded.encode('ascii')).hexdigest()} "
        f"output={output}"
    )

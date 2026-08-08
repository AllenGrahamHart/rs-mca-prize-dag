#!/usr/bin/env python3
"""Run independent direct-cell Rabinowitsch audits on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "direct_residual_cell_audit.sage"
BASE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
    / "near_literal_assignment_transport_audit.sage"
)
app = modal.App("rs-mca-k3-near-literal-direct-cell-audit")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/direct_residual_cell_audit.sage", copy=True)
    .add_local_file(BASE, "/near_literal_assignment_transport_audit.sage", copy=True)
)


@app.function(image=image, cpu=4, memory=8192, timeout=630)
def audit(cell: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["DIRECT_CELL"] = cell
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/direct_residual_cell_audit.sage"],
            env=environment,
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
        stdout, stderr = completed.stdout, completed.stderr
        returncode = completed.returncode
        timed_out = False
    except subprocess.TimeoutExpired as error:
        stdout, stderr = error.stdout or "", error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        returncode, timed_out = None, True
    payloads = []
    for line in stdout.splitlines():
        if line.startswith("DIRECT_CELL_AUDIT_JSON "):
            payloads.append(json.loads(line.split(" ", 1)[1]))
    return {
        "status": "TIMEOUT" if timed_out else (
            "PASS" if returncode == 0 and payloads else "FAIL"
        ),
        "returncode": returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payloads[-1] if payloads else None,
        "partial_payloads": payloads,
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-20000:],
        "stderr_tail": stderr[-20000:],
    }


@app.local_entrypoint()
def main() -> None:
    cells = ("F02-A-RX", "F02-A-RL", "F02-OB-RX", "F02-OB-RL")
    calls = {cell: audit.spawn(cell) for cell in cells}
    results = {cell: calls[cell].get() for cell in cells}
    output = {
        "schema": "kb-c2-112-near-literal-direct-cell-audit-modal-v1",
        "results": results,
    }
    output_path = HERE / "direct_residual_f02_square_audit_output.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        cell: {
            "status": row["status"],
            "terminal": (row["payload"] or {}).get("terminal"),
            "seconds": row["seconds"],
        }
        for cell, row in results.items()
    }, sort_keys=True))
    print(f"wrote {output_path}")

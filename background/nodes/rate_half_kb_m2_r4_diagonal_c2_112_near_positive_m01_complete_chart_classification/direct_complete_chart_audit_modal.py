#!/usr/bin/env python3
"""Run independent complete-chart M01 audits on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "direct_complete_chart_audit.sage"
BASE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
    / "near_literal_assignment_transport_audit.sage"
)
app = modal.App("rs-mca-k3-near-positive-m01-complete-chart-audit")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/direct_complete_chart_audit.sage", copy=True)
    .add_local_file(BASE, "/near_literal_assignment_transport_audit.sage", copy=True)
)


@app.function(image=image, cpu=4, memory=8192, timeout=930)
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
    completed = subprocess.run(
        ["sage", "/direct_complete_chart_audit.sage"],
        env=environment,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )
    payloads = []
    for line in completed.stdout.splitlines():
        if line.startswith("DIRECT_COMPLETE_CHART_AUDIT_JSON "):
            payloads.append(json.loads(line.split(" ", 1)[1]))
    return {
        "status": "PASS" if completed.returncode == 0 and payloads else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payloads[-1] if payloads else None,
        "partial_payloads": payloads,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout_tail": completed.stdout[-20000:],
        "stderr_tail": completed.stderr[-20000:],
    }


@app.local_entrypoint()
def main() -> None:
    cells = tuple(
        f"M01-{root}-{allocation}"
        for root in ("A", "OB")
        for allocation in ("RX", "RL", "RM")
    )
    calls = {cell: audit.spawn(cell) for cell in cells}
    results = {cell: calls[cell].get() for cell in cells}
    output = {
        "schema": "kb-c2-112-near-positive-m01-complete-chart-audit-modal-v1",
        "results": results,
    }
    output_path = HERE / "direct_complete_chart_audit_output.json"
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

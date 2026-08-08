#!/usr/bin/env python3
"""Run all 48 literal positive projective-boundary cells on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "literal_boundary_classify.sage"
app = modal.App("rs-mca-k3-near-positive-projective-boundary-literal")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/literal_boundary_classify.sage", copy=True)
)


@app.function(image=image, cpu=2, memory=4096, timeout=360)
def classify(cell: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["BOUNDARY_CELL"] = cell
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    completed = subprocess.run(
        ["sage", "/literal_boundary_classify.sage"],
        env=environment,
        capture_output=True,
        text=True,
        timeout=330,
        check=False,
    )
    payloads = []
    for line in completed.stdout.splitlines():
        if line.startswith("LITERAL_BOUNDARY_JSON "):
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
def main(cell: str = "") -> None:
    assignments = (
        "F00", "F01", "F02", "F03", "F04", "F05",
        "F06", "F07", "M00", "M01", "M02", "M03",
    )
    cells = (
        (cell,)
        if cell
        else tuple(
            f"{assignment}-{root}"
            for assignment in assignments
            for root in ("A", "TA", "OB", "OI")
        )
    )
    calls = {cell: classify.spawn(cell) for cell in cells}
    results = {cell: calls[cell].get() for cell in cells}
    output = {
        "schema": "kb-c2-112-near-positive-projective-boundary-literal-modal-v1",
        "results": results,
    }
    output_path = HERE / "literal_boundary_classification_output.json"
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

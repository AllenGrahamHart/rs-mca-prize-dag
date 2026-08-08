#!/usr/bin/env python3
"""Run the aligned-negative literal identity checks on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "aligned_negative_literal_identity.sage"
app = modal.App("rs-mca-k3-aligned-negative-literal-identity")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/aligned_negative_literal_identity.sage", copy=True)
)


@app.function(image=image, cpu=2, memory=2048, timeout=930)
def audit(assignment: str, chart: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["NEGATIVE_ASSIGNMENT"] = assignment
    environment["NEGATIVE_CHART"] = chart
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/aligned_negative_literal_identity.sage"],
            env=environment,
            capture_output=True,
            text=True,
            timeout=900,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else (error.stdout or "")
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else (error.stderr or "")
        return {
            "status": "TIMEOUT",
            "returncode": None,
            "seconds": round(time.monotonic() - started, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "payload": None,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stdout_tail": stdout[-20000:],
            "stderr_tail": stderr[-20000:],
        }
    payloads = []
    for line in completed.stdout.splitlines():
        if line.startswith("ALIGNED_NEGATIVE_LITERAL_JSON "):
            payloads.append(json.loads(line.split(" ", 1)[1]))
    return {
        "status": "PASS" if completed.returncode == 0 and payloads else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payloads[-1] if payloads else None,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout_tail": completed.stdout[-20000:],
        "stderr_tail": completed.stderr[-20000:],
    }


@app.local_entrypoint()
def main(assignment: str = "", chart: str = "") -> None:
    assignments = (
        tuple(assignment.split(","))
        if assignment
        else (
            "F00", "F01", "F02", "F03", "F04", "F05",
            "F06", "F07", "M00", "M01", "M02", "M03",
        )
    )
    keys = tuple(
        (name, chart_name)
        for name in assignments
        for chart_name in ((chart,) if chart else ("generic", "sum-zero"))
    )
    calls = {
        f"{name}:{chart}": audit.spawn(name, chart)
        for name, chart in keys
    }
    results = {key: call.get() for key, call in calls.items()}
    output = {
        "schema": "kb-c2-112-aligned-negative-literal-identity-modal-v2",
        "results": results,
    }
    suffix = assignment.lower().replace(",", "_") if assignment else "all"
    if chart:
        suffix = f"{suffix}_{chart}"
    output_path = HERE / f"aligned_negative_literal_identity_{suffix}_output.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        key: {
            "status": row["status"],
            "terminal": (row["payload"] or {}).get("terminal"),
            "seconds": row["seconds"],
        }
        for key, row in results.items()
    }, sort_keys=True))
    print(f"wrote {output_path}")

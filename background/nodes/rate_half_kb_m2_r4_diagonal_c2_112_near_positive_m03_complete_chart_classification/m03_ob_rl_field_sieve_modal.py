#!/usr/bin/env python3
"""Run the M03-OB-RL exact field sieve on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "m03_ob_rl_field_sieve.sage"
BASE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
    / "near_literal_assignment_transport_audit.sage"
)
app = modal.App("rs-mca-k3-near-positive-m03-ob-rl-field-sieve")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/m03_ob_rl_field_sieve.sage", copy=True)
    .add_local_file(BASE, "/near_literal_assignment_transport_audit.sage", copy=True)
)


@app.function(image=image, cpu=4, memory=8192, timeout=930)
def sieve() -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    completed = subprocess.run(
        ["sage", "/m03_ob_rl_field_sieve.sage"],
        env=environment,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )
    payloads = []
    for line in completed.stdout.splitlines():
        if line.startswith("M03_OB_RL_FIELD_SIEVE_JSON "):
            payloads.append(json.loads(line.split(" ", 1)[1]))
    return {
        "status": "PASS" if completed.returncode == 0 and payloads else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payloads[-1] if payloads else None,
        "partial_payloads": payloads,
        "stdout_tail": completed.stdout[-20000:],
        "stderr_tail": completed.stderr[-20000:],
    }


@app.local_entrypoint()
def main() -> None:
    result = sieve.remote()
    output = {
        "schema": "kb-c2-112-near-positive-m03-ob-rl-field-sieve-modal-v1",
        "result": result,
    }
    output_path = HERE / "m03_ob_rl_field_sieve_output.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "terminal": (result["payload"] or {}).get("terminal"),
        "seconds": result["seconds"],
    }, sort_keys=True))
    print(f"wrote {output_path}")

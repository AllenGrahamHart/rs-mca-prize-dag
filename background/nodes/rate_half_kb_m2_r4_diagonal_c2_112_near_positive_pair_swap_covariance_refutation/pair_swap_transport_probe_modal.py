#!/usr/bin/env python3
"""Run the exact reciprocal-pair-swap transport probe on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
PROBE = HERE / "pair_swap_transport_probe.sage"
BASE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
    / "near_literal_assignment_transport_audit.sage"
)
OUTPUT = HERE / "pair_swap_transport_probe_output.json"
app = modal.App("rs-mca-k3-near-literal-pair-swap-probe")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(PROBE, "/pair_swap_transport_probe.sage", copy=True)
    .add_local_file(BASE, "/near_literal_assignment_transport_audit.sage", copy=True)
)


@app.function(image=image, cpu=4, memory=8192, timeout=300)
def run_probe(
    assignment: str = "",
    localizers: bool = False,
    search: bool = False,
) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PAIR_SWAP_ASSIGNMENT"] = assignment
    environment["PAIR_SWAP_LOCALIZERS"] = "1" if localizers else "0"
    environment["PAIR_SWAP_SEARCH"] = "1" if search else "0"
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/pair_swap_transport_probe.sage"],
            env=environment,
            capture_output=True,
            text=True,
            timeout=270,
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
    payload = None
    for line in stdout.splitlines():
        if line.startswith("PAIR_SWAP_PROBE_JSON "):
            payload = json.loads(line.split(" ", 1)[1])
    return {
        "status": "TIMEOUT" if timed_out else (
            "PASS" if returncode == 0 and payload is not None else "FAIL"
        ),
        "returncode": returncode,
        "seconds": round(time.monotonic() - started, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "payload": payload,
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr_tail": stderr[-20000:],
    }


@app.local_entrypoint()
def main(
    assignment: str = "",
    localizers: bool = False,
    all_assignments: bool = False,
    search: bool = False,
) -> None:
    if all_assignments:
        assignments = (
            "F00", "F01", "F02", "F03", "F04", "F05",
            "F06", "F07", "M00", "M01", "M02", "M03",
        )
        calls = {
            item: run_probe.spawn(item, localizers, False)
            for item in assignments
        }
        results = {item: calls[item].get() for item in assignments}
        output = {
            "schema": "kb-c2-112-near-literal-pair-swap-shards-modal-v1",
            "localizers": localizers,
            "results": results,
        }
        output_path = HERE / (
            "pair_swap_transport_localizer_shards_output.json"
            if localizers
            else "pair_swap_transport_core_shards_output.json"
        )
        output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
        print(json.dumps({
            "statuses": {item: row["status"] for item, row in results.items()},
            "terminals": {
                item: (row["payload"] or {}).get("terminal")
                for item, row in results.items()
            },
        }, sort_keys=True))
        print(f"wrote {output_path}")
        return

    result = run_probe.remote(assignment, localizers, search)
    output = {
        "schema": "kb-c2-112-near-literal-pair-swap-modal-v1",
        "result": result,
    }
    output_path = (
        HERE / "pair_swap_transport_destination_search_output.json"
        if search
        else (
            OUTPUT if not assignment else HERE / (
                f"pair_swap_transport_probe_{assignment.lower()}_output.json"
            )
        )
    )
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "seconds": result["seconds"],
        "terminal": (result["payload"] or {}).get("terminal"),
    }, sort_keys=True))
    print(f"wrote {output_path}")

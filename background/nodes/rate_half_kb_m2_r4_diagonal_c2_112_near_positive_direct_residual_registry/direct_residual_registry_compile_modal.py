#!/usr/bin/env python3
"""Compile the 30-cell direct residual registry on Modal."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "direct_residual_registry_compile.sage"
BASE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
    / "near_literal_assignment_transport_audit.sage"
)
OUTPUT = HERE / "direct_residual_registry_output.json"
app = modal.App("rs-mca-k3-near-literal-direct-residual-registry")
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("python3", "python-is-python3")
    .add_local_file(SOURCE, "/direct_residual_registry_compile.sage", copy=True)
    .add_local_file(BASE, "/near_literal_assignment_transport_audit.sage", copy=True)
)


@app.function(image=image, cpu=4, memory=8192, timeout=360)
def compile_registry() -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/direct_residual_registry_compile.sage"],
            env=environment,
            capture_output=True,
            text=True,
            timeout=330,
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
        if line.startswith("DIRECT_RESIDUAL_REGISTRY_JSON "):
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
        "stdout_tail": stdout[-20000:],
        "stderr_tail": stderr[-20000:],
    }


@app.local_entrypoint()
def main() -> None:
    result = compile_registry.remote()
    OUTPUT.write_text(json.dumps({
        "schema": "kb-c2-112-near-literal-direct-residual-registry-modal-v1",
        "result": result,
    }, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "seconds": result["seconds"],
        "cells": (result["payload"] or {}).get("cell_count"),
        "max_terms": (result["payload"] or {}).get("max_terms"),
        "max_total_degree": (result["payload"] or {}).get("max_total_degree"),
    }, sort_keys=True))
    print(f"wrote {OUTPUT}")

#!/usr/bin/env python3
"""Run the balanced fixed structural probe in bounded Modal containers."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


MODE = os.environ.get("FIXED_PROBE_MODE", "balanced")
APP_NAME = f"rs-mca-k3-fixed-branch-probe-{MODE}"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
PROBE = HERE / "probe.sage"
LIBRARY = HERE / "branch_core.sage"
OUTPUT = HERE / (
    "modal_remaining_representative_probe_output.json"
    if MODE == "remaining_representatives"
    else "modal_probe_output.json"
)
CELLS = (
    ("F04-R02", "F05-R02", "F04-R20", "F05-R20")
    if MODE == "remaining_representatives"
    else ("F04-R11", "F05-R11")
)

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin "
        "pull/1149/head:refs/remotes/origin/pr1149",
        "git -C /repo checkout --detach refs/remotes/origin/pr1149",
    )
    .add_local_file(PROBE, "/probe.sage")
    .add_local_file(LIBRARY, "/branch_core.sage")
)


@app.function(image=image, cpu=2, memory=16384, timeout=780, max_containers=2)
def probe(cell: str) -> dict[str, object]:
    import hashlib
    import os
    import resource
    import subprocess
    import time

    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    try:
        completed = subprocess.run(
            ["sage", "/probe.sage", "--cell", cell],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=720,
            check=False,
        )
        lines = [line for line in completed.stdout.splitlines() if line.startswith("{")]
        record = json.loads(lines[-1]) if lines else None
        status = (
            "PASS"
            if completed.returncode == 0
            and record
            and record.get("terminal")
            == "EXACT_FACTORED_BRANCH_DATA_NO_EMPTINESS_CLAIM"
            else "FAIL"
        )
        return {
            "cell": cell,
            "status": status,
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "record": record,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stdout_tail": completed.stdout[-2000:],
            "stderr_tail": completed.stderr[-4000:],
        }
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "error": str(error),
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(probe.map(CELLS, return_exceptions=True))
    normalized = []
    for cell, row in zip(CELLS, rows):
        if isinstance(row, BaseException):
            normalized.append({"cell": cell, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-fixed-balanced-quadratic-branch-modal-probe-v1",
        "app": APP_NAME,
        "mode": MODE,
        "upstream_commit": COMMIT,
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")

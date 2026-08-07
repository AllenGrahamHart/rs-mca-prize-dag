#!/usr/bin/env python3
"""Run bounded modular Groebner probes for the balanced generic cores."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


MODE = os.environ.get("GROEBNER_MODE", "full")
APP_NAME = f"rs-mca-k3-fixed-balanced-core-groebner-{MODE}"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
LIBRARY = HERE / "branch_core.sage"
SCRIPT = HERE / "groebner_probe.sage"
OUTPUT = HERE / (
    "modal_groebner_deployed_output.json"
    if MODE == "deployed"
    else "modal_groebner_probe_output.json"
)
PRIMES = (2130706433,) if MODE == "deployed" else (1009, 2130706433)
CASES = tuple(
    {"cell": cell, "prime": prime}
    for cell in ("F04-R11", "F05-R11", "F06-R11", "F07-R11")
    for prime in PRIMES
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
    .add_local_file(LIBRARY, "/branch_core.sage")
    .add_local_file(SCRIPT, "/groebner_probe.sage")
)


@app.function(image=image, cpu=2, memory=16384, timeout=420, max_containers=4)
def run_case(case: dict[str, object]) -> dict[str, object]:
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
    command = [
        "sage",
        "/groebner_probe.sage",
        "--cell",
        str(case["cell"]),
        "--prime",
        str(case["prime"]),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=360,
            check=False,
        )
        records = []
        for line in completed.stdout.splitlines():
            if line.startswith("{"):
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        done = next((row for row in records if row.get("phase") == "DONE"), None)
        status = "PASS" if completed.returncode == 0 and done else "FAIL"
        return {
            **case,
            "status": status,
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stdout_tail": completed.stdout[-4000:],
            "stderr_tail": completed.stderr[-4000:],
        }
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        records = []
        for line in stdout.splitlines():
            if line.startswith("{"):
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return {
            **case,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(run_case.map(CASES, return_exceptions=True))
    normalized = []
    for case, row in zip(CASES, rows):
        if isinstance(row, BaseException):
            normalized.append({**case, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-fixed-balanced-core-groebner-modal-v1",
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

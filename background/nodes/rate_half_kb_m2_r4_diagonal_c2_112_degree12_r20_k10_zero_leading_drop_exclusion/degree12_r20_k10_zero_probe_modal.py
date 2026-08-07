#!/usr/bin/env python3
"""Run R20 degree-12 K10-zero leading-drop probes on Modal."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


MODE = os.environ.get("DEGREE12_R20_K10_MODE", "broad")
APP_NAME = f"rs-mca-k3-degree12-r20-k10-zero-leading-drop-{MODE}"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
BALANCED = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
)
LIBRARY = BALANCED / "branch_core.sage"
SCRIPT = HERE / "degree12_r20_k10_zero_probe.sage"
HELPER = HERE / "generic_block_analysis.sage"
OUTPUT = HERE / f"modal_degree12_r20_k10_zero_{MODE}_output.json"
if MODE == "broad":
    CASES = tuple({"cell": cell} for cell in ("F04-R20", "F06-R20"))
elif MODE == "generic_f04":
    CASES = ({"cell": "F04-R20", "generic_block": True},)
elif MODE == "linear_drop":
    CASES = tuple(
        {"cell": cell, "linear_drop": True}
        for cell in ("F04-R20", "F06-R20")
    )
elif MODE == "linear_source_f04":
    CASES = ({"cell": "F04-R20", "linear_source": True},)
elif MODE == "linear_source_f06":
    CASES = ({"cell": "F06-R20", "linear_source": True},)
elif MODE == "linear_source":
    CASES = tuple(
        {"cell": cell, "linear_source": True}
        for cell in ("F04-R20", "F06-R20")
    )
else:
    raise ValueError(f"unsupported DEGREE12_R20_K10_MODE={MODE!r}")

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
    .add_local_file(SCRIPT, "/degree12_r20_k10_zero_probe.sage")
    .add_local_file(HELPER, "/generic_block_analysis.sage")
)


@app.function(
    image=image,
    cpu=4,
    memory=32768,
    timeout=1800 if MODE == "generic_f04" else 900,
    max_containers=2,
)
def run_case(case: dict[str, str]) -> dict[str, object]:
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
        "/degree12_r20_k10_zero_probe.sage",
        "--cell",
        case["cell"],
    ]
    if case.get("generic_block"):
        command.append("--generic-block")
    if case.get("linear_drop"):
        command.append("--linear-drop")
    if case.get("linear_source"):
        command.append("--linear-source")
    try:
        completed = subprocess.run(
            command,
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=1680 if case.get("generic_block") else 780,
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
        return {
            **case,
            "status": "PASS" if completed.returncode == 0 and done else "FAIL",
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "records": records,
            "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
            "stdout_tail": completed.stdout[-10000:],
            "stderr_tail": completed.stderr[-10000:],
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
            "stdout_tail": stdout[-10000:],
            "stderr_tail": stderr[-10000:],
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
        "schema": "kb-c2-112-fixed-degree12-r20-k10-zero-modal-v1",
        "app": APP_NAME,
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

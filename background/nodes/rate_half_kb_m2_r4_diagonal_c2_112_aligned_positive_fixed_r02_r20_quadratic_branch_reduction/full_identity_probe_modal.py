#!/usr/bin/env python3
"""Run bounded full-identity coefficient compilers for fixed assignments."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


MODE = os.environ.get("FULL_IDENTITY_MODE", "representatives")
COEFFICIENT_INDEX = int(os.environ.get("FULL_IDENTITY_COEFF", "0"))
IDENTITY = os.environ.get("FULL_IDENTITY_KIND", "J")
APP_NAME = f"rs-mca-k3-fixed-full-identity-{MODE}-{IDENTITY.lower()}-c{COEFFICIENT_INDEX}"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
LIBRARY = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
    / "branch_core.sage"
)
SCRIPT = HERE / "full_identity_probe.sage"
OUTPUT = HERE / (
    f"modal_full_identity_{MODE}_c{COEFFICIENT_INDEX}_output.json"
    if IDENTITY == "J"
    else f"modal_full_identity_{MODE}_{IDENTITY.lower()}_c{COEFFICIENT_INDEX}_output.json"
)
ASSIGNMENTS = (
    ("F04",)
    if MODE == "single"
    else (("F04", "F05") if MODE == "representatives" else ("F04", "F05", "F06", "F07"))
)
CASES = tuple(
    {
        "assignment": assignment,
        "coefficient_index": COEFFICIENT_INDEX,
        "identity": IDENTITY,
    }
    for assignment in ASSIGNMENTS
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
    .add_local_file(SCRIPT, "/full_identity_probe.sage")
)


@app.function(image=image, cpu=2, memory=16384, timeout=480, max_containers=4)
def run_assignment(case: dict[str, object]) -> dict[str, object]:
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
    assignment = str(case["assignment"])
    coefficient_index = int(case["coefficient_index"])
    identity = str(case["identity"])
    try:
        completed = subprocess.run(
            [
                "sage",
                "/full_identity_probe.sage",
                "--assignment",
                assignment,
                "--identity",
                identity,
                "--coefficient-index",
                str(coefficient_index),
            ],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=420,
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
            "assignment": assignment,
            "coefficient_index": coefficient_index,
            "identity": identity,
            "status": "PASS" if completed.returncode == 0 and done else "FAIL",
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
        return {
            "assignment": assignment,
            "coefficient_index": coefficient_index,
            "identity": identity,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(run_assignment.map(CASES, return_exceptions=True))
    normalized = []
    for case, row in zip(CASES, rows):
        if isinstance(row, BaseException):
            normalized.append(
                {**case, "status": "REMOTE_ERROR", "error": repr(row)}
            )
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-fixed-full-identity-coefficients-modal-v1",
        "app": APP_NAME,
        "mode": MODE,
        "coefficient_index": COEFFICIENT_INDEX,
        "identity": IDENTITY,
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

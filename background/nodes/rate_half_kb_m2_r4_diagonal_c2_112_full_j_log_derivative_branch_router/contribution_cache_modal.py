#!/usr/bin/env python3
"""Cache the thirteen R02 logarithmic contributions in parallel on Modal."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-f04-r02-full-j-log-contribution-cache"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
ROUTE = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_quadratic_branch_reduction"
)
BALANCED = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
)
LIBRARY = BALANCED / "branch_core.sage"
FULL_IDENTITY = ROUTE / "modal_full_identity_single_c0_output.json"
SCRIPT = ROUTE / "quadratic_quotient_full_j_probe.sage"
SCOPE = os.environ.get("LOG_CACHE_SCOPE", "all")
if SCOPE == "observed":
    indices = range(6)
elif SCOPE == "slow":
    indices = (0, 1, 4, 5)
else:
    indices = range(13)
REMOTE_TIMEOUT = 960 if SCOPE == "slow" else 480
PROCESS_TIMEOUT = 900 if SCOPE == "slow" else 420
OUTPUT = HERE / f"modal_contribution_cache_r02_{SCOPE}_output.json"
CASES = tuple(
    {
        "contribution_index": index,
        "process_timeout": PROCESS_TIMEOUT,
    }
    for index in indices
)

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("sagemath/sagemath:10.9")
    .apt_install("git", "python3", "python-is-python3")
    .run_commands(
        "git init /repo",
        f"git -C /repo remote add origin {UPSTREAM}",
        "git -C /repo fetch --depth=1 origin pull/1149/head:refs/remotes/origin/pr1149",
        "git -C /repo checkout --detach refs/remotes/origin/pr1149",
    )
    .add_local_file(LIBRARY, "/branch_core.sage")
    .add_local_file(FULL_IDENTITY, "/full_identity.json")
    .add_local_file(SCRIPT, "/quadratic_quotient_full_j_probe.sage")
)


@app.function(
    image=image,
    cpu=2,
    memory=16384,
    timeout=REMOTE_TIMEOUT,
    max_containers=13,
)
def run_case(case: dict[str, int]) -> dict[str, object]:
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
            [
                "sage",
                "/quadratic_quotient_full_j_probe.sage",
                "--target",
                "R02",
                "--cache-contribution-index",
                str(case["contribution_index"]),
            ],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=case["process_timeout"],
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
            **case,
            "status": "TIMEOUT",
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
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
        "schema": "kb-c2-112-f04-r02-full-j-log-contribution-cache-modal-v1",
        "app": APP_NAME,
        "scope": SCOPE,
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

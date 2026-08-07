#!/usr/bin/env python3
"""Replay full-J coefficient zero and its logarithmic router literally."""

from __future__ import annotations

import json
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-fixed-literal-full-j-log-router-source-replay"
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
FULL_SCRIPT = ROUTE / "full_identity_probe.sage"
LOG_SCRIPT = ROUTE / "log_derivative_j_probe.sage"
FULL_OUTPUT = HERE / "modal_full_identity_literal_replay_output.json"
LOG_OUTPUT = HERE / "modal_log_derivative_literal_replay_output.json"
CASES = tuple({"assignment": assignment} for assignment in ("F05", "F06", "F07"))

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
    .add_local_file(FULL_SCRIPT, "/full_identity_probe.sage")
    .add_local_file(LOG_SCRIPT, "/log_derivative_j_probe.sage")
)


def normalize_completed(completed, seconds: float, peak_kb: int) -> dict[str, object]:
    import hashlib

    records = []
    for line in completed.stdout.splitlines():
        if line.startswith("{"):
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    done = next((row for row in records if row.get("phase") == "DONE"), None)
    return {
        "status": "PASS" if completed.returncode == 0 and done else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(seconds, 6),
        "peak_kb": peak_kb,
        "records": records,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout_tail": completed.stdout[-10000:],
        "stderr_tail": completed.stderr[-10000:],
    }


@app.function(image=image, cpu=2, memory=16384, timeout=1620, max_containers=3)
def run_assignment(case: dict[str, object]) -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    assignment = str(case["assignment"])
    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)

    def run(command: list[str]) -> dict[str, object]:
        began = time.monotonic()
        try:
            completed = subprocess.run(
                command,
                cwd="/repo",
                env=environment,
                capture_output=True,
                text=True,
                timeout=720,
                check=False,
            )
            return normalize_completed(
                completed,
                time.monotonic() - began,
                resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            )
        except subprocess.TimeoutExpired as error:
            stdout = error.stdout or ""
            stderr = error.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode(errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode(errors="replace")
            return {
                "status": "TIMEOUT",
                "seconds": round(time.monotonic() - began, 6),
                "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                "stdout_tail": stdout[-10000:],
                "stderr_tail": stderr[-10000:],
            }

    full = run(
        [
            "sage",
            "/full_identity_probe.sage",
            "--assignment",
            assignment,
            "--identity",
            "J",
            "--coefficient-index",
            "0",
        ]
    )
    log = run(
        [
            "sage",
            "/log_derivative_j_probe.sage",
            "--assignment",
            assignment,
        ]
    )
    return {"assignment": assignment, "full": full, "log": log}


def payload(kind: str, rows: list[dict[str, object]]) -> dict[str, object]:
    normalized = [
        {"assignment": row["assignment"], **row[kind]}
        if kind in row
        else {"assignment": row["assignment"], "status": "REMOTE_ERROR", "error": row["error"]}
        for row in rows
    ]
    return {
        "schema": f"kb-c2-112-fixed-literal-{kind}-source-replay-modal-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in ("PASS", "FAIL", "TIMEOUT", "REMOTE_ERROR")
        },
        "results": normalized,
    }


@app.local_entrypoint()
def main() -> None:
    raw_rows = list(run_assignment.map(CASES, return_exceptions=True))
    rows = []
    for case, row in zip(CASES, raw_rows):
        if isinstance(row, BaseException):
            rows.append({**case, "error": repr(row)})
        else:
            rows.append(row)
    full = payload("full", rows)
    log = payload("log", rows)
    FULL_OUTPUT.write_text(json.dumps(full, indent=2, sort_keys=True) + "\n")
    LOG_OUTPUT.write_text(json.dumps(log, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"full": full["counts"], "log": log["counts"]}, sort_keys=True))
    print(f"wrote {FULL_OUTPUT}")
    print(f"wrote {LOG_OUTPUT}")

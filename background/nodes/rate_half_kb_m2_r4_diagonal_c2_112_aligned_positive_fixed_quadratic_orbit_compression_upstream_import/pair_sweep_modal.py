#!/usr/bin/env python3
"""Sweep all quadratic row pairs for the two balanced fixed orbits."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import modal


APP_NAME = "rs-mca-k3-pr1149-balanced-pair-sweep"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
SCRIPT = (
    "/repo/experimental/scripts/"
    "compile_kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.sage"
)
OUTPUT = Path(__file__).resolve().parent / "modal_pair_sweep_output.json"
CASES = tuple(
    {"cell": cell, "pair": pair}
    for cell in ("F04-R11", "F05-R11")
    for pair in combinations(range(4), 2)
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
)


@app.function(
    image=image,
    cpu=1,
    memory=8192,
    timeout=240,
    max_containers=12,
)
def sweep(case: dict[str, object]) -> dict[str, object]:
    import os
    import resource
    import subprocess
    import time

    cell = str(case["cell"])
    pair = [int(value) for value in case["pair"]]
    environment = dict(os.environ)
    environment["HOME"] = "/tmp/sage-home"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    os.makedirs(environment["HOME"], exist_ok=True)
    began = time.monotonic()
    try:
        completed = subprocess.run(
            [
                "sage",
                SCRIPT,
                "--cell",
                cell,
                "--quadratic-compress",
                str(pair[0]),
                str(pair[1]),
                "--check",
                "--summary",
            ],
            cwd="/repo",
            env=environment,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        lines = [
            line for line in completed.stdout.splitlines() if line.startswith("{")
        ]
        summary = json.loads(lines[0]) if len(lines) == 1 else None
        expected_quadratic = pair == [0, 1]
        if completed.returncode == 0 and summary and expected_quadratic:
            status = "PASS"
        elif (
            not expected_quadratic
            and completed.returncode != 0
            and "assert first.degree() == second.degree()" in completed.stderr
        ):
            status = "EXPECTED_REJECT"
        else:
            status = "FAIL"
        return {
            "cell": cell,
            "pair": pair,
            "status": status,
            "returncode": completed.returncode,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "summary": summary,
            "stderr_tail": completed.stderr[-2000:],
        }
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "pair": pair,
            "status": "TIMEOUT",
            "returncode": None,
            "seconds": round(time.monotonic() - began, 6),
            "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
            "summary": None,
            "stderr_tail": str(error),
        }


@app.local_entrypoint()
def main() -> None:
    rows = list(sweep.map(CASES, return_exceptions=True))
    normalized = []
    for case, row in zip(CASES, rows):
        if isinstance(row, BaseException):
            normalized.append({**case, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    output = {
        "schema": "kb-c2-112-pr1149-balanced-pair-sweep-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "case_count": len(CASES),
        "counts": {
            status: sum(row["status"] == status for row in normalized)
            for status in (
                "PASS",
                "EXPECTED_REJECT",
                "FAIL",
                "TIMEOUT",
                "REMOTE_ERROR",
            )
        },
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")

#!/usr/bin/env python3
"""Replay both generic cubic factors for one selected literal fixed cell."""

from __future__ import annotations

import json
import os
from pathlib import Path

import modal


CELL = os.environ.get("LITERAL_CUBIC_CELL", "F07-R02")
assert CELL in ("F07-R02", "F06-R20")
APP_NAME = f"rs-mca-k3-fixed-{CELL.lower()}-generic-cubic-replay"
UPSTREAM = "https://github.com/przchojecki/rs-mca.git"
COMMIT = "55ac3e07477bd7a768190a3e755f22b0d44354b0"
HERE = Path(__file__).resolve().parent
NODES = HERE.parent
LIBRARY = (
    NODES
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
    / "branch_core.sage"
)
SCRIPT = (
    NODES
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_quadratic_branch_reduction"
    / "generic_factor_probe.sage"
)
OUTPUT = HERE / (
    "modal_literal_r02_cubic_factor_replay_output.json"
    if CELL == "F07-R02"
    else "modal_literal_f06_r20_cubic_factor_replay_output.json"
)
CASES = tuple(
    {"cell": CELL, "factor_index": index, "prime": 2130706433}
    for index in (0, 1)
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
    .add_local_file(SCRIPT, "/generic_factor_probe.sage")
)


@app.function(image=image, cpu=2, memory=16384, timeout=300, max_containers=2)
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
    completed = subprocess.run(
        [
            "sage",
            "/generic_factor_probe.sage",
            "--cell",
            str(case["cell"]),
            "--factor-index",
            str(case["factor_index"]),
            "--prime",
            str(case["prime"]),
        ],
        cwd="/repo",
        env=environment,
        capture_output=True,
        text=True,
        timeout=240,
        check=False,
    )
    records = []
    for line in completed.stdout.splitlines():
        if line.startswith("{"):
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    done = next((record for record in records if record.get("phase") == "DONE"), None)
    return {
        **case,
        "status": "PASS" if completed.returncode == 0 and done else "FAIL",
        "returncode": completed.returncode,
        "seconds": round(time.monotonic() - began, 6),
        "peak_kb": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "records": records,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode()).hexdigest(),
        "stdout_tail": completed.stdout[-6000:],
        "stderr_tail": completed.stderr[-6000:],
    }


@app.local_entrypoint()
def main() -> None:
    raw_rows = list(run_case.map(CASES, return_exceptions=True))
    rows = []
    for case, row in zip(CASES, raw_rows):
        if isinstance(row, BaseException):
            rows.append({**case, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "kb-c2-112-fixed-literal-r02-cubic-factor-replay-modal-v1",
        "app": APP_NAME,
        "upstream_commit": COMMIT,
        "counts": {
            status: sum(row["status"] == status for row in rows)
            for status in ("PASS", "FAIL", "REMOTE_ERROR")
        },
        "results": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["counts"], sort_keys=True))
    print(f"wrote {OUTPUT}")

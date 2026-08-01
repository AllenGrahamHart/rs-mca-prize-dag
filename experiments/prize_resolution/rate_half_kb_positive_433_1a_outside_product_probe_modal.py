#!/usr/bin/env python3
"""Capped Modal paired-product probe for positive 433-1a/O0b."""

import itertools
import json
from pathlib import Path
import subprocess
from collections import Counter

import modal


APP_NAME = "rs-mca-positive-433-1a-outside-product-probe"
SOURCE = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_common_chart_probe.c"
)
REMOTE_SOURCE = "/root/rate_half_kb_positive_433_1a_common_chart_probe.c"
REMOTE_BINARY = "/tmp/outside-product-probe"
CELL_ORBIT_REPRESENTATIVES = (0, 1, 3, 4, 5, 9, 11, 12, 14)

app = modal.App(APP_NAME)
image = modal.Image.debian_slim().apt_install("gcc").add_local_file(
    SOURCE, REMOTE_SOURCE
)


@app.function(image=image, cpu=0.5, memory=256, timeout=60, max_containers=72)
def probe_case(case):
    prime, cell, epsilon_1, epsilon_2, cycle_sign = case
    compiler = subprocess.run(
        ["gcc", "-O3", "-std=c11", REMOTE_SOURCE, "-o", REMOTE_BINARY],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if compiler.returncode:
        return {"status": "COMPILE_ERROR", "case": case,
                "stderr": compiler.stderr}
    try:
        process = subprocess.run(
            [REMOTE_BINARY, str(prime), str(cell), str(epsilon_1),
             str(epsilon_2), str(cycle_sign)],
            capture_output=True,
            text=True,
            timeout=40,
        )
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "case": case}
    if process.returncode:
        return {"status": "ERROR", "case": case,
                "stdout": process.stdout, "stderr": process.stderr}
    return {"status": "COMPLETE", **json.loads(process.stdout)}


@app.local_entrypoint()
def main(prime: int = 29):
    cases = tuple(itertools.product(
        (prime,), CELL_ORBIT_REPRESENTATIVES, (-1, 1), (-1, 1), (-1, 1)
    ))
    results = list(probe_case.map(cases))
    completed = [row for row in results if row["status"] == "COMPLETE"]
    summaries = []
    for cell, cycle_sign in itertools.product(
        CELL_ORBIT_REPRESENTATIVES, (-1, 1)
    ):
        rows = [row for row in completed
                if row["cell"] == cell and row["cycle_sign"] == cycle_sign]
        summaries.append({
            "cell": cell,
            "cycle_sign": cycle_sign,
            "completed_root_sign_rows": len(rows),
            "common_support_survivors": sum(
                row["support_survivors"] for row in rows
            ),
            "common_points_with_outside": sum(
                row["common_points_with_outside"] for row in rows
            ),
            "outside_target_completions": sum(
                row["outside_target_completions"] for row in rows
            ),
            "first_example": next(
                (row["outside_example"] for row in rows
                 if row["outside_example"][0] >= 0), None
            ),
        })
    print(json.dumps({
        "app": APP_NAME,
        "prime": prime,
        "case_count": len(results),
        "status_counts": dict(Counter(row["status"] for row in results)),
        "total_common_support_survivors": sum(
            row["support_survivors"] for row in completed
        ),
        "total_common_points_with_outside": sum(
            row["common_points_with_outside"] for row in completed
        ),
        "total_outside_target_completions": sum(
            row["outside_target_completions"] for row in completed
        ),
        "summaries": summaries,
        "noncomplete": [row for row in results if row["status"] != "COMPLETE"],
        "scope": (
            f"F{prime} aligned xi=eta necessary quadratic paired-product "
            "completion only; target/source choices are finite-field "
            "relaxations; no outside sum, deployed-field, route, K3, or "
            "Prize conclusion"
        ),
    }, sort_keys=True))

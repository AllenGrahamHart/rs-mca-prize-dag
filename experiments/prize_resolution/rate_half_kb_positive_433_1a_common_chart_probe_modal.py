#!/usr/bin/env python3
"""Capped Modal point counts for positive 433-1a common pivot charts."""

import itertools
import json
from pathlib import Path
import subprocess
from collections import Counter

import modal


APP_NAME = "rs-mca-positive-433-1a-common-chart-probe"
SOURCE = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_common_chart_probe.c"
)
REMOTE_SOURCE = "/root/rate_half_kb_positive_433_1a_common_chart_probe.c"
REMOTE_BINARY = "/tmp/common-chart-probe"
PRIMES = (13, 17, 29)
CELL_ORBIT_REPRESENTATIVES = (0, 1, 3, 4, 5, 9, 11, 12, 14)

app = modal.App(APP_NAME)
image = modal.Image.debian_slim().apt_install("gcc").add_local_file(
    SOURCE, REMOTE_SOURCE
)


@app.function(image=image, cpu=0.5, memory=256, timeout=60, max_containers=64)
def probe_case(case):
    prime, cell, epsilon_1, epsilon_2 = case
    compile_process = subprocess.run(
        ["gcc", "-O3", "-std=c11", REMOTE_SOURCE, "-o", REMOTE_BINARY],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if compile_process.returncode:
        return {
            "status": "COMPILE_ERROR", "case": case,
            "stderr": compile_process.stderr,
        }
    try:
        process = subprocess.run(
            [REMOTE_BINARY, str(prime), str(cell), str(epsilon_1), str(epsilon_2)],
            capture_output=True,
            text=True,
            timeout=40,
        )
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "case": case}
    if process.returncode:
        return {
            "status": "ERROR", "case": case,
            "stdout": process.stdout, "stderr": process.stderr,
        }
    return {"status": "COMPLETE", **json.loads(process.stdout)}


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product(
        PRIMES, CELL_ORBIT_REPRESENTATIVES, (-1, 1), (-1, 1)
    ))
    results = list(probe_case.map(cases))
    completed = [row for row in results if row["status"] == "COMPLETE"]
    prime_summary = {}
    for prime in PRIMES:
        rows = [row for row in completed if row["prime"] == prime]
        prime_summary[str(prime)] = {
            "completed_cases": len(rows),
            "total_admissible": sum(row["admissible"] for row in rows),
            "total_base_rank_six": sum(row["base_rank_six"] for row in rows),
            "total_rank_survivors": sum(row["rank_survivors"] for row in rows),
            "total_support_survivors": sum(row["support_survivors"] for row in rows),
            "total_zero_branch": sum(row["zero_branch"] for row in rows),
            "cases_with_support_survivors": sum(
                row["support_survivors"] > 0 for row in rows
            ),
            "maximum_support_survivors": max(
                (row["support_survivors"] for row in rows), default=None
            ),
        }
    cell_summary = []
    for prime, cell in itertools.product(PRIMES, CELL_ORBIT_REPRESENTATIVES):
        rows = [
            row for row in completed
            if row["prime"] == prime and row["cell"] == cell
        ]
        cell_summary.append({
            "prime": prime,
            "cell": cell,
            "completed_sign_rows": len(rows),
            "support_survivors": sum(row["support_survivors"] for row in rows),
            "sign_rows_with_survivors": sum(
                row["support_survivors"] > 0 for row in rows
            ),
            "minimum_per_sign_row": min(
                (row["support_survivors"] for row in rows), default=None
            ),
            "maximum_per_sign_row": max(
                (row["support_survivors"] for row in rows), default=None
            ),
            "zero_branch": sum(row["zero_branch"] for row in rows),
            "pivot_counts": [
                sum(row["pivot_counts"][index] for row in rows)
                for index in range(4)
            ],
        })
    print(json.dumps({
        "app": APP_NAME,
        "case_count": len(results),
        "status_counts": dict(Counter(row["status"] for row in results)),
        "prime_summary": prime_summary,
        "cell_summary": cell_summary,
        "noncomplete": [row for row in results if row["status"] != "COMPLETE"],
        "scope": (
            "small-prime common-stage point counts only; no deployed-field, "
            "outside-row, route-deletion, K3, or Prize conclusion"
        ),
    }, sort_keys=True))

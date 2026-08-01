#!/usr/bin/env python3
"""Capped Modal summaries for the positive 433-1a common Vieta atlas."""

import itertools
import json
from pathlib import Path
import subprocess
from collections import Counter

import modal


APP_NAME = "rs-mca-positive-433-1a-common-vieta-compiler"
SOURCE = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
)
REMOTE_SOURCE = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=0.5, memory=768, timeout=240, max_containers=100)
def compile_case(case):
    mode, cell, epsilon_1, epsilon_2 = case
    command = [
        "python3", REMOTE_SOURCE, "--cell", str(cell),
        "--epsilon-1", str(epsilon_1), "--epsilon-2", str(epsilon_2),
    ]
    if mode in ("stripped", "gcd"):
        command.append("--strip-fast")
    if mode == "gcd":
        command.append("--gcd-summary")
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=220,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "mode": mode,
            "status": "TIMEOUT",
            "stdout": error.stdout or "",
            "stderr": error.stderr or "",
        }
    if process.returncode:
        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "mode": mode,
            "status": "ERROR",
            "stdout": process.stdout,
            "stderr": process.stderr,
        }
    result = json.loads(process.stdout)
    result["mode"] = mode
    return {"status": "COMPLETE", **result}


@app.local_entrypoint()
def main(remaining_only: bool = False):
    if remaining_only:
        cases = tuple(itertools.product(("gcd",), range(3, 12), (-1, 1), (-1, 1)))
    else:
        cases = tuple(itertools.product(("raw", "stripped"), range(15), (-1, 1), (-1, 1)))
    results = list(compile_case.map(cases))
    mode_summaries = {}
    for mode in ("raw", "stripped", "gcd"):
        completed = [
            row for row in results
            if row["status"] == "COMPLETE" and row["mode"] == mode
        ]
        summaries = [
            summary
            for row in completed
            for summary in row["minor_summaries"]
        ]
        row_unique_histogram = Counter(
            str(len({summary["sha256"] for summary in row["minor_summaries"]}))
            for row in completed
        )
        gcd_summaries = [
            row["joint_gcd_summary"]
            for row in completed
            if row.get("joint_gcd_summary") is not None
        ]
        mode_summaries[mode] = {
            "completed_cases": len(completed),
            "minor_count": len(summaries),
            "minor_degree_histogram": dict(Counter(
                str(summary["total_degree"]) for summary in summaries
            )),
            "minimum_terms": min((summary["terms"] for summary in summaries), default=None),
            "maximum_terms": max((summary["terms"] for summary in summaries), default=None),
            "unique_minor_digests": len({summary["sha256"] for summary in summaries}),
            "within_row_unique_histogram": dict(row_unique_histogram),
            "joint_gcd_degree_histogram": dict(Counter(
                str(summary["total_degree"]) for summary in gcd_summaries
            )),
            "joint_gcd_maximum_terms": max(
                (summary["terms"] for summary in gcd_summaries), default=None
            ),
        }
    completed = [row for row in results if row["status"] == "COMPLETE"]
    print(json.dumps({
        "app": APP_NAME,
        "case_count": len(results),
        "status_counts": dict(Counter(row["status"] for row in results)),
        "cell_orbits": completed[0]["cell_orbits"] if completed else [],
        "modes": mode_summaries,
        "noncomplete_cases": [
            {key: row.get(key) for key in ("cell", "epsilon", "status", "stderr")}
            for row in results if row["status"] != "COMPLETE"
        ],
    }, indent=2, sort_keys=True))

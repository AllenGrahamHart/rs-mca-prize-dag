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


@app.function(image=image, cpu=0.5, memory=768, timeout=60, max_containers=60)
def compile_case(case):
    cell, epsilon_1, epsilon_2 = case
    try:
        process = subprocess.run(
            ["python3", REMOTE_SOURCE, "--cell", str(cell),
             "--epsilon-1", str(epsilon_1), "--epsilon-2", str(epsilon_2)],
            capture_output=True,
            text=True,
            timeout=50,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "status": "TIMEOUT",
            "stdout": error.stdout or "",
            "stderr": error.stderr or "",
        }
    if process.returncode:
        return {
            "cell": cell,
            "epsilon": [epsilon_1, epsilon_2],
            "status": "ERROR",
            "stdout": process.stdout,
            "stderr": process.stderr,
        }
    return {"status": "COMPLETE", **json.loads(process.stdout)}


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product(range(15), (-1, 1), (-1, 1)))
    results = list(compile_case.map(cases))
    completed = [row for row in results if row["status"] == "COMPLETE"]
    summaries = [
        summary
        for row in completed
        for summary in row["minor_summaries"]
    ]
    print(json.dumps({
        "app": APP_NAME,
        "case_count": len(results),
        "status_counts": dict(Counter(row["status"] for row in results)),
        "cell_orbits": completed[0]["cell_orbits"] if completed else [],
        "minor_count": len(summaries),
        "minor_degree_histogram": dict(Counter(
            str(summary["total_degree"]) for summary in summaries
        )),
        "minimum_terms": min((summary["terms"] for summary in summaries), default=None),
        "maximum_terms": max((summary["terms"] for summary in summaries), default=None),
        "unique_minor_digests": len({summary["sha256"] for summary in summaries}),
        "noncomplete_cases": [
            {key: row.get(key) for key in ("cell", "epsilon", "status", "stderr")}
            for row in results if row["status"] != "COMPLETE"
        ],
    }, indent=2, sort_keys=True))

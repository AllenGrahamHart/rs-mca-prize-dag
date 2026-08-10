#!/usr/bin/env python3
"""Bounded Modal compilation of the repeated-BC 433-1b/O0b atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler_result.json"
REMOTE_SOURCE = "/root/rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
APP_NAME = "rs-mca-positive-433-1b-o0b-common-repeat-vieta"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=0.5, memory=768, timeout=240, max_containers=60)
def compile_case(case):
    mode, cell, epsilon_1, epsilon_2, bc_sign = case
    command = [
        "python3", REMOTE_SOURCE, "--cell", str(cell),
        "--epsilon-1", str(epsilon_1), "--epsilon-2", str(epsilon_2),
        "--bc-sign", str(bc_sign),
    ]
    if mode == "stripped":
        command.append("--strip-fast")
    try:
        process = subprocess.run(
            command, capture_output=True, text=True, timeout=220,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell, "epsilon": [epsilon_1, epsilon_2],
            "bc_sign": bc_sign, "mode": mode, "status": "TIMEOUT",
            "stdout": error.stdout or "", "stderr": error.stderr or "",
        }
    if process.returncode:
        return {
            "cell": cell, "epsilon": [epsilon_1, epsilon_2],
            "bc_sign": bc_sign, "mode": mode, "status": "ERROR",
            "stdout": process.stdout, "stderr": process.stderr,
        }
    return {"status": "COMPLETE", **json.loads(process.stdout)}


def summarize(rows, mode, bc_sign):
    completed = [
        row for row in rows
        if row["status"] == "COMPLETE"
        and row["mode"] == mode
        and row["bc_sign"] == bc_sign
    ]
    minors = [
        summary for row in completed for summary in row["minor_summaries"]
    ]
    return {
        "completed_cases": len(completed),
        "minor_count": len(minors),
        "minor_degree_histogram": dict(sorted(Counter(
            str(summary["total_degree"]) for summary in minors
        ).items())),
        "minimum_terms": min((summary["terms"] for summary in minors), default=None),
        "maximum_terms": max((summary["terms"] for summary in minors), default=None),
        "unique_minor_digests": len({summary["sha256"] for summary in minors}),
        "within_row_unique_histogram": dict(sorted(Counter(
            str(len({summary["sha256"] for summary in row["minor_summaries"]}))
            for row in completed
        ).items())),
    }


@app.local_entrypoint()
def main():
    source_bytes = SOURCE.read_bytes()
    cases = tuple(itertools.product(
        ("raw", "stripped"), range(15), (-1, 1), (-1, 1), (-1, 1),
    ))
    rows = list(compile_case.map(cases, order_outputs=True))
    rows.sort(key=lambda row: (
        row.get("mode", ""), row.get("bc_sign", 0),
        row.get("cell", -1), row.get("epsilon", []),
    ))
    summaries = {
        mode: {
            str(bc_sign): summarize(rows, mode, bc_sign)
            for bc_sign in (-1, 1)
        }
        for mode in ("raw", "stripped")
    }
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-common-repeat-vieta-v1",
        "scope": (
            "Exact raw and guard-stripped common Vieta minor summaries for "
            "all 120 repeated-BC matching/root-sign/BC-sign rows; no route claim."
        ),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "app": APP_NAME,
        "case_count": len(rows),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "summaries": summaries,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": len(rows),
        "status_counts": output["status_counts"],
        "summaries": summaries,
    }, sort_keys=True))


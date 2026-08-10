#!/usr/bin/env python3
"""Bounded Modal driver for repeated-BC 433-1b/O0b product-rank minors."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler.py"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler_result.json"
)
REMOTE_SOURCE = "/root/repeat_product_rank.py"
APP_NAME = "rs-mca-positive-433-1b-o0b-repeat-product-rank"

app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=0.5, memory=768, timeout=75, max_containers=15)
def compile_case(case):
    cell, bc_sign = case
    try:
        process = subprocess.run(
            ["python3", REMOTE_SOURCE, "--cell", str(cell),
             "--bc-sign", str(bc_sign), "--dump"],
            capture_output=True, text=True, timeout=65,
        )
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "cell": cell, "bc_sign": bc_sign}
    if process.returncode:
        return {
            "status": "ERROR", "cell": cell, "bc_sign": bc_sign,
            "stdout": process.stdout, "stderr": process.stderr,
        }
    return {"status": "COMPLETE", **json.loads(process.stdout)}


@app.local_entrypoint()
def main():
    source_bytes = SOURCE.read_bytes()
    cases = tuple((cell, bc_sign)
                  for cell in range(15) for bc_sign in (-1, 1))
    rows = list(compile_case.map(cases, order_outputs=True))
    completed = [row for row in rows if row["status"] == "COMPLETE"]
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-repeat-product-rank-v1",
        "scope": (
            "Exact guard-stripped repeated-BC product-block maximal minors "
            "in all thirty cell/sign rows; no route conclusion."
        ),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "app": APP_NAME,
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "guard_only_cells": {
            f"{row['cell']}:{row['bc_sign']}": row["guard_only_minor_columns"]
            for row in completed if row["guard_only_minor_columns"]
        },
        "stripped_degree_histogram": dict(sorted(Counter(
            str(minor["degree"])
            for row in completed for minor in row["stripped"]
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": output["status_counts"],
        "guard_only_cells": output["guard_only_cells"],
        "stripped_degree_histogram": output["stripped_degree_histogram"],
    }, sort_keys=True))

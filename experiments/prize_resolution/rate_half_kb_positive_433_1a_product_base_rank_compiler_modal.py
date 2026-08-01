#!/usr/bin/env python3
"""Capped Modal driver for positive 433-1a product-block rank minors."""

import json
from pathlib import Path
import subprocess
from collections import Counter

import modal


APP_NAME = "rs-mca-positive-433-1a-product-base-rank"
SOURCE = Path(__file__).with_name(
    "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
)
REMOTE_SOURCE = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
app = modal.App(APP_NAME)
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=0.5, memory=768, timeout=60, max_containers=15)
def compile_cell(case):
    cell, dump = case
    command = ["python3", REMOTE_SOURCE, "--cell", str(cell)]
    if dump:
        command.append("--dump")
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=50,
        )
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "cell": cell}
    if process.returncode:
        return {
            "status": "ERROR", "cell": cell,
            "stdout": process.stdout, "stderr": process.stderr,
        }
    return {"status": "COMPLETE", **json.loads(process.stdout)}


@app.local_entrypoint()
def main(dump_cell: int = -1):
    cells = (dump_cell,) if dump_cell >= 0 else tuple(range(15))
    results = list(compile_cell.map((cell, dump_cell >= 0) for cell in cells))
    completed = [row for row in results if row["status"] == "COMPLETE"]
    print(json.dumps({
        "app": APP_NAME,
        "status_counts": dict(Counter(row["status"] for row in results)),
        "guard_only_cells": {
            str(row["cell"]): row["guard_only_minor_columns"]
            for row in completed if row["guard_only_minor_columns"]
        },
        "stripped_degree_histogram": dict(Counter(
            str(minor["degree"])
            for row in completed for minor in row["stripped"]
        )),
        "cells": [
            {
                "cell": row["cell"],
                "singleton": row["singleton"],
                "matching": row["matching"],
                "guard_only_minor_columns": row["guard_only_minor_columns"],
                "stripped": row["stripped"],
                "stripped_expressions": row.get("stripped_expressions"),
                "stripped_ledgers": row.get("stripped_ledgers"),
                "rank_drop_substitution": row.get("rank_drop_substitution"),
                "rank_drop_specialized": row.get("rank_drop_specialized"),
                "rank_drop_guard_only_minor_columns": row.get(
                    "rank_drop_guard_only_minor_columns"
                ),
                "rank_drop_specialized_expressions": row.get(
                    "rank_drop_specialized_expressions"
                ),
                "rank_drop_specialized_ledgers": row.get(
                    "rank_drop_specialized_ledgers"
                ),
            }
            for row in completed
        ],
        "noncomplete": [row for row in results if row["status"] != "COMPLETE"],
    }, sort_keys=True))

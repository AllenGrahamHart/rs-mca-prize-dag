#!/usr/bin/env python3
"""Hostile controls for the 433-1b/O0b residual partition."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("partition_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(payload):
    try:
        VERIFY.validate(payload)
    except RuntimeError:
        return
    raise RuntimeError("mutation survived")


def main():
    dag = json.loads((VERIFY.ROOT / "dag.json").read_text())
    VERIFY.validate(dag)
    for parent in VERIFY.PARENTS:
        mutation = copy.deepcopy(dag)
        next(row for row in mutation["nodes"]
             if row["id"] == parent)["status"] = "TARGET"
        reject(mutation)
    mutation = copy.deepcopy(dag)
    mutation["edges"] = [
        row for row in mutation["edges"]
        if not (row["from"] == VERIFY.PARENTS[-1]
                and row["to"] == VERIFY.NODE_ID)
    ]
    reject(mutation)
    mutation = copy.deepcopy(dag)
    next(row for row in mutation["nodes"]
         if row["id"] == VERIFY.NODE_ID)["closure"] = "wrong census"
    reject(mutation)
    print("PASS positive 433-1b/O0b residual partition hostile audit: 9/9")


if __name__ == "__main__":
    main()

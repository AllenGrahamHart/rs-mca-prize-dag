#!/usr/bin/env python3
"""Hostile controls for the complete BC- cells-3/6 aggregate."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("aggregate_verify", NODE / "verify.py")
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
    by_id = {row["id"]: row for row in dag["nodes"]}
    for parent in (VERIFY.COLORED, VERIFY.UNCOLORED, VERIFY.TRANSPORT):
        mutation = copy.deepcopy(dag)
        next(row for row in mutation["nodes"] if row["id"] == parent)["status"] = "TARGET"
        reject(mutation)
    mutation = copy.deepcopy(dag)
    mutation["edges"] = [
        row for row in mutation["edges"]
        if not (row["from"] == VERIFY.COLORED and row["to"] == VERIFY.NODE_ID)
    ]
    reject(mutation)
    mutation = copy.deepcopy(dag)
    next(row for row in mutation["nodes"]
         if row["id"] == VERIFY.NODE_ID)["closure"] = "incorrect census"
    reject(mutation)
    print("PASS repeated-BC cells3/6 BC- aggregate hostile audit: 5/5")


if __name__ == "__main__":
    main()

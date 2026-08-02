#!/usr/bin/env python3
"""Mutation controls for the cell-4 exceptional-chart verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell4_exception_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payload, label):
    try:
        VERIFY.verify_payload(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads((VERIFY.EXPERIMENTS / VERIFY.FACTOR_FILE).read_text())
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["result"]["linear_roots"].pop()
    must_fail(mutation, "root coverage")

    mutation = copy.deepcopy(payload)
    cubic = next(factor for row in mutation["result"]["rows"]
                 for factor in row["factorization"]
                 if factor["total_degree"] == 3)
    cubic["total_degree"] = 2
    must_fail(mutation, "cubic factor class")

    mutation = copy.deepcopy(payload)
    mutation["result"]["linear_roots"][0]["t"] = 2
    must_fail(mutation, "guard root")
    print("positive 433-1a cell-4 exceptional-chart audit verified")


if __name__ == "__main__":
    main()

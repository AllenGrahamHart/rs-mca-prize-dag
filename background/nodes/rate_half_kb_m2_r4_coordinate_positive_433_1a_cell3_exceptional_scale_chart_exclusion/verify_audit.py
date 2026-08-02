#!/usr/bin/env python3
"""Mutation controls for the cell-3 exceptional-chart verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell3_exception_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payloads, label):
    try:
        VERIFY.verify_payloads(payloads)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payloads = {
        name: json.loads((VERIFY.EXPERIMENTS / filename).read_text())
        for name, filename in VERIFY.FILES.items()
    }
    VERIFY.verify_payloads(payloads)

    mutation = copy.deepcopy(payloads)
    mutation["factor"]["result"]["linear_roots"].pop()
    must_fail(mutation, "exceptional root coverage")

    mutation = copy.deepcopy(payloads)
    mutation["charts"]["rows"][0]["unit"] = False
    must_fail(mutation, "common chart unit pattern")

    mutation = copy.deepcopy(payloads)
    mutation["points"]["result"]["b_roots"][0] += 1
    must_fail(mutation, "quadratic lift")

    mutation = copy.deepcopy(payloads)
    mutation["outside"]["rows"][0]["pair"]["unit"] = False
    must_fail(mutation, "signed-pair unit")
    print("positive 433-1a cell-3 exceptional-chart audit verified")


if __name__ == "__main__":
    main()

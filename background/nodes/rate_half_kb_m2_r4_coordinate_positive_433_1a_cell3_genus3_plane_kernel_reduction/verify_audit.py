#!/usr/bin/env python3
"""Mutation controls for the cell-3 genus-three reduction verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell3_verify", NODE / "verify.py")
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
    mutation["profile"]["result"]["reconstruction_equal"] = False
    must_fail(mutation, "quotient reconstruction")

    mutation = copy.deepcopy(payloads)
    mutation["cover"]["result"]["numerator_factorization"]["factors"][0][
        "multiplicity"
    ] = 2
    must_fail(mutation, "square-free cover")

    mutation = copy.deepcopy(payloads)
    mutation["plane"]["result"]["b1_opposite"] = False
    must_fail(mutation, "B1 opposition")

    mutation = copy.deepcopy(payloads)
    mutation["target"]["result"]["status"] = "COMPLETE"
    must_fail(mutation, "timeout fence")
    print("positive 433-1a cell-3 genus-three reduction audit verified")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mutation controls for the cell-4 signed-pair verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell4_pair_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payloads, label):
    try:
        VERIFY.verify_payloads(payloads["projection"], payloads["factor"],
                               payloads["reconstruction"])
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payloads = {
        name: json.loads((VERIFY.EXPERIMENTS / filename).read_text())
        for name, filename in VERIFY.FILES.items()
    }
    VERIFY.verify_payloads(payloads["projection"], payloads["factor"],
                           payloads["reconstruction"])

    mutation = copy.deepcopy(payloads)
    mutation["factor"]["result"]["factors"].pop()
    must_fail(mutation, "live factor coverage")

    mutation = copy.deepcopy(payloads)
    mutation["reconstruction"]["result"]["resultant_identity"][
        "leading_exponent"
    ] = 6
    must_fail(mutation, "resultant normalization")

    mutation = copy.deepcopy(payloads)
    mutation["reconstruction"]["result"]["plane_reduction"][
        "discarded_factors"
    ]["plane_content"]["factors"][2]["multiplicity"] = 44
    must_fail(mutation, "discarded scale ledger")
    print("positive 433-1a cell-4 signed-pair audit verified")


if __name__ == "__main__":
    main()

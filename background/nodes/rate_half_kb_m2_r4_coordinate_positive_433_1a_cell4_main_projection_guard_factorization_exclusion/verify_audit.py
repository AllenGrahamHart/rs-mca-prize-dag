#!/usr/bin/env python3
"""Mutation controls for the cell-4 guard-factorization verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell4_guard_verify",
                                              NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payload, label):
    try:
        VERIFY.verify_payload(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads((VERIFY.EXPERIMENTS / VERIFY.RESULT_FILE).read_text())
    VERIFY.verify_payload(payload)

    mutation = copy.deepcopy(payload)
    mutation["result"]["plane_leading_exponent"] = 20
    must_fail(mutation, "plane scale")

    mutation = copy.deepcopy(payload)
    mutation["result"]["quotient_ring_cross_identity"]["verified"] = False
    must_fail(mutation, "cross identity")

    mutation = copy.deepcopy(payload)
    mutation["result"]["f_leading_norm"]["factors"][3]["text"] = "t + 2"
    must_fail(mutation, "norm factor")

    mutation = copy.deepcopy(payload)
    mutation["artifact_sha256"][
        "rate_half_kb_positive_433_1a_cell4_pair_resultant_factor_2.txt"
    ] = "0"*64
    must_fail(mutation, "input custody")
    print("positive 433-1a cell-4 main guard factorization audit verified")


if __name__ == "__main__":
    main()

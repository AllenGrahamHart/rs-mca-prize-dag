#!/usr/bin/env python3
"""Mutation controls for the exceptional coefficient projection verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell4_exception_projection_verify",
                                              NODE / "verify.py")
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
    mutation["ledger"]["evaluation_rank"] = 14
    must_fail(mutation, "interpolation rank")

    mutation = copy.deepcopy(payloads)
    mutation["gcd"]["result"]["common"]["factors"].pop()
    must_fail(mutation, "H factor coverage")

    mutation = copy.deepcopy(payloads)
    mutation["factor"]["result"]["factors"][3]["root"] = 2
    must_fail(mutation, "residual root census")

    mutation = copy.deepcopy(payloads)
    mutation["lift"]["result"]["divisibility"]["live"]["coefficients"][0][
        "zero_mod_h"
    ] = False
    must_fail(mutation, "H quotient divisibility")
    print("positive 433-1a cell-4 exceptional coefficient audit verified")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mutation controls for the cell-3 guard-factorization verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell3_guard_verify",
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
    mutation["result"]["projected_sha256"] = "0"*64
    must_fail(mutation, "projected resultant")

    mutation = copy.deepcopy(payload)
    mutation["result"]["quotient_ring_cross_identity"]["verified"] = False
    must_fail(mutation, "cross identity")

    mutation = copy.deepcopy(payload)
    mutation["result"]["leading_exception_atlas"][
        "all_uncovered_deployed_roots_guarded"
    ] = False
    must_fail(mutation, "exception atlas")

    mutation = copy.deepcopy(payload)
    mutation["result"]["leading_exception_atlas"]["rows"][3][
        "b_rows"
    ][0]["common_guards"] = []
    must_fail(mutation, "b+1 guard")

    mutation = copy.deepcopy(payload)
    mutation["source_plane_sha256"] = "0"*64
    must_fail(mutation, "input custody")
    print("positive 433-1a cell-3 guard factorization audit verified")


if __name__ == "__main__":
    main()

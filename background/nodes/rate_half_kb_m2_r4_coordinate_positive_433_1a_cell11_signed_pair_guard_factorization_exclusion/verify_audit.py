#!/usr/bin/env python3
"""Mutation controls for the cell-11 guard-factorization verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_guard_verify",
                                              NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def must_fail(payloads, label):
    try:
        VERIFY.verify_payloads(*payloads)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    keys = ("kernel_result", "plane_result", "main_result", "scale_result",
            "charts_result")
    originals = [
        json.loads((VERIFY.EXPERIMENTS / VERIFY.FILES[key][0]).read_text())
        for key in keys
    ]
    VERIFY.verify_payloads(*originals)

    mutation = copy.deepcopy(originals)
    mutation[0]["result"]["basis_size"] = 9
    must_fail(mutation, "kernel basis")

    mutation = copy.deepcopy(originals)
    mutation[1]["result"]["b1_opposite"] = False
    must_fail(mutation, "B1 opposition")

    mutation = copy.deepcopy(originals)
    mutation[2]["result"]["quotient_ring_cross_identity"]["verified"] = False
    must_fail(mutation, "cross identity")

    mutation = copy.deepcopy(originals)
    mutation[2]["result"]["leading_exception_atlas"]["rows"][5][
        "b_rows"
    ][0]["deployed_w0_roots"][0]["guards"] = []
    must_fail(mutation, "finite guard")

    mutation = copy.deepcopy(originals)
    mutation[3]["result"]["linear_roots"].pop()
    must_fail(mutation, "scale root")

    mutation = copy.deepcopy(originals)
    mutation[4]["rows"][3]["unit"] = False
    must_fail(mutation, "scale unit")
    print("positive 433-1a cell-11 guard factorization audit verified")


if __name__ == "__main__":
    main()

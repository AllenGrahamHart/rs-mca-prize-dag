#!/usr/bin/env python3
"""Mutation controls for the exceptional reconstruction verifier."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell4_h_exclusion_verify",
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
    mutation["frobenius"]["result"]["base_field_root_gcd"]["degree"] = 14
    must_fail(mutation, "Frobenius degree")

    mutation = copy.deepcopy(payloads)
    for row in mutation["atlas"]["result"]["rows"]:
        candidates = [item for item in row["w0_rows"] if "b" in item]
        if candidates:
            candidates[0]["d0_zero"] = False
            break
    must_fail(mutation, "generic denominator guard")

    mutation = copy.deepcopy(payloads)
    mutation["content"]["result"]["rows"][0]["w0_rows"].append({"w0": 1})
    must_fail(mutation, "content fiber point")

    mutation = copy.deepcopy(payloads)
    for row in mutation["scales"]["result"]["replay_rows"]:
        if not row["t_guard"] and row["b_rows"]:
            row["b_rows"][0]["d0_zero"] = False
            break
    must_fail(mutation, "scale denominator guard")
    print("positive 433-1a cell-4 exceptional reconstruction audit verified")


if __name__ == "__main__":
    main()

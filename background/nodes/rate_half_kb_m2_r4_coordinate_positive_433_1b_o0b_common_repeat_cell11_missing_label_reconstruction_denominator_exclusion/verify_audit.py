#!/usr/bin/env python3
"""Hostile controls for the cell-11 reconstruction-boundary verifier."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("reconstruction_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(mutation, label):
    payload = copy.deepcopy(VERIFY.load(VERIFY.RESULT))
    mutation(payload)
    try:
        VERIFY.validate_payload(payload, VERIFY.load(VERIFY.TOWER))
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    reject(lambda value: value.__setitem__("case_count", 7), "row census")
    reject(lambda value: value["rows"][0].__setitem__(
        "tower_valid", False), "tower validity")
    reject(lambda value: value["rows"][0][
        "norm_numerator_factorization"
    ][0].__setitem__("degree", 2), "factor profile")
    reject(lambda value: value["rows"][1]["base_field_roots"][0].__setitem__(
        "tower_chart_guards_nonzero", False), "root classification")
    reject(lambda value: value["rows"][1]["root_fiber_census"][0].__setitem__(
        "source_candidate_count", 1), "lift census")
    reject(lambda value: value["rows"][1]["boundary_points"][0].__setitem__(
        "common_equations_zero", False), "equation replay")
    reject(lambda value: value["rows"][1]["boundary_points"][0].__setitem__(
        "common_guard_nonzero", True), "guard replay")
    reject(lambda value: value["rows"][0].__setitem__(
        "status", "GUARDED_RECONSTRUCTION_BOUNDARY_PRESENT"), "status")
    print("PASS cell11 reconstruction boundary hostile audit: 8/8")


if __name__ == "__main__":
    main()

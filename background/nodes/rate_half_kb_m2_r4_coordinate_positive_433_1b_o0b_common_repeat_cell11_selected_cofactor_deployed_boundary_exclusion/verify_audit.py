#!/usr/bin/env python3
"""Hostile controls for the cell-11 selected-cofactor boundary verifier."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("boundary_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def reject(mutation, label):
    payload = copy.deepcopy(VERIFY.load(VERIFY.RESULT))
    mutation(payload)
    try:
        VERIFY.validate_payload(
            payload, VERIFY.load(VERIFY.TOWER), VERIFY.load(VERIFY.INPUT)
        )
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    reject(lambda value: value.__setitem__("case_count", 7), "row census")
    reject(lambda value: value["rows"][0].__setitem__("tower_valid", False),
           "tower validity")
    reject(lambda value: value["rows"][0].__setitem__(
        "selected_rank_minor_sha256", "0" * 64), "cofactor identity")
    reject(lambda value: value["rows"][0][
        "norm_numerator_factorization"
    ][0].__setitem__("degree", 1), "factor profile")
    reject(lambda value: value["rows"][0]["base_field_roots"][0].__setitem__(
        "x", 2), "base-field root")
    reject(lambda value: value["rows"][0]["base_field_roots"][0].__setitem__(
        "pre_cofactor_guards_nonzero", True), "guard witness")
    reject(lambda value: value.__setitem__(
        "deployed_boundary_root_occurrences", 1), "deployed roots")
    reject(lambda value: value["rows"][0].__setitem__(
        "status", "DEPLOYED_FIELD_BOUNDARY_PRESENT"), "status")
    print("PASS cell11 selected-cofactor boundary hostile audit: 8/8")


if __name__ == "__main__":
    main()

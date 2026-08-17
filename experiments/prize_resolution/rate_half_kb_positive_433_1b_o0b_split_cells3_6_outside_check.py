#!/usr/bin/env python3
"""Check the preregistered O0b split cells-3/6 outside pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRODUCT = HERE / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
KERNEL = HERE / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
MANIFEST = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
CORE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_outside_core.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_outside_pilot_result.json"
PRODUCT_SHA256 = "ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293"
KERNEL_SHA256 = "e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"
CORE_SHA256 = "07d371aaf2beee7c3182e3ae2f65e0e3844a74e8730850d1d764714b07dfa46b"
REPRESENTATIVES_SHA256 = "39fb277a94d8ee3a24e3a8f9e1f0bb50014665ca7c151659d4dc8fcd912392d6"
PILOT_SHA256 = "a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def row_key(row):
    return (
        row["cell"],
        row["lane"],
        row["sigma_o"],
        *row["epsilon"],
        row["xi_index"],
        row["pairing_index"],
    )


def verify(payload=None, manifest=None):
    require(hashlib.sha256(PRODUCT.read_bytes()).hexdigest() == PRODUCT_SHA256,
            "product custody")
    require(hashlib.sha256(KERNEL.read_bytes()).hexdigest() == KERNEL_SHA256,
            "kernel custody")
    require(hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == MANIFEST_SHA256,
            "manifest custody")
    require(hashlib.sha256(CORE.read_bytes()).hexdigest() == CORE_SHA256,
            "core custody")
    manifest = manifest or json.loads(MANIFEST.read_text())
    payload = payload or json.loads(RESULT.read_text())
    expected = tuple(tuple(row) for row in manifest["pilot_representatives"])
    require(len(expected) == 24 and manifest["pilot_stratum_count"] == 56,
            "pilot manifest census")
    require(manifest["representatives_sha256"] == REPRESENTATIVES_SHA256,
            "complete representative hash")
    require(manifest["pilot_representatives_sha256"] == PILOT_SHA256,
            "pilot representative hash")
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cells3-6-outside-pilot-v1",
            "result schema")
    require(payload["scope"] == "pilot" and payload["field"] == 2130706433,
            "result scope")
    require(payload["source_product_sha256"] == PRODUCT_SHA256 and
            payload["source_kernel_sha256"] == KERNEL_SHA256 and
            payload["source_manifest_sha256"] == MANIFEST_SHA256 and
            payload["source_core_sha256"] == CORE_SHA256,
            "source custody fields")
    require(payload["representatives_sha256"] == REPRESENTATIVES_SHA256 and
            payload["selected_cases_sha256"] == PILOT_SHA256,
            "selected case custody")
    require(payload["complete"] is True, "complete checkpoint")
    require(payload["expected_case_count"] == 24 and
            payload["processed_case_count"] == 24 and len(payload["rows"]) == 24,
            "result census")
    require(payload["status_counts"] == {"COMPLETE": 24} and
            payload["unit_count"] == 24, "all-unit summary")
    rows = payload["rows"]
    require(tuple(row_key(row) for row in rows) == expected,
            "ordered pilot case cover")
    require(len({row["program_sha256"] for row in rows}) == 24,
            "distinct case programs")
    for row in rows:
        require(row["status"] == "COMPLETE" and row["unit"] is True,
                "unit row")
        require(row["dimension"] == -1 and row["basis_size"] == 1,
                "unit ideal shape")
        require(row["common_equation_count"] == 3 and
                row["outside_equation_count"] == 5,
                "equation ledger")
        require(row["rank_cofactor_count"] == 6 and row["guard_count"] > 30,
                "guard/rank ledger")
        require(row["input_polynomials"] == [] and
                row["guard_factors"] == [] and row["rank_cofactors"] == [],
                "unit compact output")
        stdout = row["stdout"]
        require("COFACTOR_DIM=-1,COFACTOR_SIZE=1" in stdout and
                "BEGIN\nDIM=-1\nSIZE=1\nUNIT=1\nEND" in stdout and
                "?" not in stdout,
                "saturation transcript")
        require(row["stderr"] == "", "clean Singular stderr")
    return {"rows": 24, "unit": 24, "programs": 24}


def expect_rejected(payload, label):
    try:
        verify(payload=payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutation = deepcopy(payload)
    mutation["complete"] = False
    expect_rejected(mutation, "incomplete checkpoint")
    mutation = deepcopy(payload)
    mutation["rows"][0]["rank_cofactor_count"] = 5
    expect_rejected(mutation, "missing rank chart")
    mutation = deepcopy(payload)
    mutation["rows"][0]["unit"] = False
    expect_rejected(mutation, "nonunit row")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_OUTSIDE_PILOT_CHECK_PASS "
        f"rows={result['rows']} unit={result['unit']} programs={result['programs']} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()

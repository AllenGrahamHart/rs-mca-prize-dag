#!/usr/bin/env python3
"""Outcome-neutral checker for the seven remaining O0b charts."""

import argparse
from copy import deepcopy
import hashlib
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_projective_chart_program.py"
ALL_INFINITY = HERE / "rate_half_kb_positive_433_1b_o0b_chart_all_infinity_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
PROGRAM_SHA256 = "277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5"
ALL_INFINITY_SHA256 = "545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf"
CASE = [3, "S0", -1, -1, -1, 2, 0]
ALL_INFINITY_MASK = ("infinity", "infinity", "infinity")
MASKS = tuple(
    mask for mask in product(("finite", "infinity"), repeat=3)
    if mask != ALL_INFINITY_MASK
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(PROGRAM.read_bytes()).hexdigest() == PROGRAM_SHA256,
            "program custody")
    require(hashlib.sha256(ALL_INFINITY.read_bytes()).hexdigest() ==
            ALL_INFINITY_SHA256, "closed-chart custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-chart-remaining-pilot-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE,
            "scope")
    require(payload["chart_masks"] == [list(mask) for mask in MASKS] and
            payload["excluded_closed_mask"] == list(ALL_INFINITY_MASK),
            "chart scope")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_program_sha256"] == PROGRAM_SHA256 and
            payload["source_all_infinity_sha256"] == ALL_INFINITY_SHA256,
            "source fields")
    rows = payload["rows"]
    require(payload["expected_row_count"] == 7 and
            payload["processed_row_count"] == 7 and
            payload["remote_errors"] == [] and len(rows) == 7,
            "complete collection")
    require([row["index"] for row in rows] == list(range(7)) and
            [tuple(row["chart_mask"]) for row in rows] == list(MASKS),
            "ordered chart cover")
    require(len({row["program_sha256"] for row in rows}) == 7,
            "distinct chart programs")
    unit_count = 0
    timeout_count = 0
    nonunit_count = 0
    for row in rows:
        finite_count = tuple(row["chart_mask"]).count("finite")
        require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
        require(row["variable_count"] == 7 + finite_count and
                row["finite_root_count"] == finite_count and
                row["common_basis_size"] == 21 and
                row["outside_equation_count"] == 8 and
                row["matching_chart_equation_count"] == 6 and
                row["guard_count"] == 40 and row["rank_cofactor_count"] == 6,
                "input ledger")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str),
                    "timeout transcript")
            timeout_count += 1
            continue
        require(row["stderr"] == "" and "END" in row["stdout"] and
                "?" not in row["stdout"], "complete transcript")
        if row["unit"]:
            require(row["dimension"] == -1 and row["basis_size"] == 1 and
                    row["input_program"] == "" and "UNIT=1" in row["stdout"],
                    "unit result")
            unit_count += 1
        else:
            require(row["input_program"] != "" and "UNIT=0" in row["stdout"],
                    "retained nonunit result")
            nonunit_count += 1
    require(payload["unit_count"] == unit_count, "unit summary")
    return {
        "rows": 7, "unit": unit_count, "nonunit": nonunit_count,
        "timeout": timeout_count,
    }


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutation = deepcopy(payload)
    mutation["collection_complete"] = False
    expect_rejected(mutation, "incomplete collection")
    mutation = deepcopy(payload)
    mutation["rows"][0]["index"] = 6
    expect_rejected(mutation, "wrong order")
    mutation = deepcopy(payload)
    mutation["rows"][0]["matching_chart_equation_count"] = 5
    expect_rejected(mutation, "missing chart equation")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_CHART_REMAINING_PILOT_CHECK_PASS "
          f"rows={result['rows']} unit={result['unit']} "
          f"nonunit={result['nonunit']} timeout={result['timeout']} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

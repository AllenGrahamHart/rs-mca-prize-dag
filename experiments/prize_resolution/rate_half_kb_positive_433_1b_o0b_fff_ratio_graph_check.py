#!/usr/bin/env python3
"""Outcome-neutral checker for the exact FFF ratio-graph subsystem."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_program.py"
SOURCE_TIMEOUT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_reduced_square_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
PROGRAM_SHA256 = "4375aa57ad1b1ec1aa85afd323e6bed5d4e6b7bd1c33e4ab15492a623a443898"
SOURCE_TIMEOUT_SHA256 = "c4406f815ddbcc33618a91ddce56b8a51c4f2c541f746d28f2873df377d0f7ba"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_prefix(values, expected, label):
    actual = [row["equation"] for row in values]
    require(actual == expected[:len(actual)], label)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(PROGRAM.read_bytes()).hexdigest() == PROGRAM_SHA256,
            "program custody")
    require(hashlib.sha256(SOURCE_TIMEOUT.read_bytes()).hexdigest() ==
            SOURCE_TIMEOUT_SHA256, "source-timeout custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-ratio-graph-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_program_sha256"] == PROGRAM_SHA256 and
            payload["source_timeout_sha256"] == SOURCE_TIMEOUT_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] ==
            "necessary FFF ratio-graph subsystem superset" and
            row["omitted_finite_pair"] == "q4" and
            row["variable_count"] == 7 and
            row["variables"] == ["E", "s", "x", "t", "r", "c", "b"] and
            row["graph_relation"] == "a2m*x-a0m" and
            row["q5_removed_factor"] == "a2m^4" and
            row["q6_removed_factor"] == "a2m^2" and
            row["common_basis_size"] == 21 and
            row["outside_equation_order"] == [5, 7, 6] and
            row["normal_form_order"] == [5, 7, 6] and
            row["route_guard_count"] == 16 and
            row["extra_guards"] == ["E", "s", "x", "a0m", "a2m"] and
            row["rank_cofactor_count"] == 6,
            "input ledger")
    require(row["graph_dimension"] is None or
            (row["graph_dimension"] >= 0 and row["graph_basis_size"] > 0),
            "graph stage")
    verify_prefix(row["normal_stages"], [5, 7, 6], "normal prefix")
    verify_prefix(row["equation_stages"], [5, 7, 6], "equation prefix")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "" and
            row["graph_dimension"] >= 0 and
            len(row["normal_stages"]) == 3 and
            len(row["equation_stages"]) == 3 and
            len(row["route_stages"]) == 16 and
            len(row["extra_stages"]) == 5,
            "complete stage ledger")
    if row["unit"]:
        require(row["dimension"] == -1 and row["basis_size"] == 1 and
                row["cofactor_dimension"] == -1 and
                row["cofactor_basis_size"] == 1 and "UNIT=1" in row["stdout"],
                "unit result")
    else:
        require(row["dimension"] >= 0 and row["basis_size"] > 0 and
                "UNIT=0" in row["stdout"], "nonunit result")
    return {"status": "COMPLETE", "unit": row["unit"]}


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
    mutation["row"]["graph_relation"] = "a2m*x+a0m"
    expect_rejected(mutation, "wrong graph relation")
    mutation = deepcopy(payload)
    mutation["row"]["q5_removed_factor"] = "a2m^2"
    expect_rejected(mutation, "wrong removed factor")
    mutation = deepcopy(payload)
    mutation["row"]["omitted_finite_pair"] = None
    expect_rejected(mutation, "overstated full chart")
    return 4


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_RATIO_GRAPH_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

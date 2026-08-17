#!/usr/bin/env python3
"""Outcome-neutral checker for the canonical O0b FFF ratio reduction."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_ratio_reduction_program.py"
IFF_UNIT = HERE / "rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_ratio_reduction_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
IFF_UNIT_SHA256 = "5485816c745c18d1514200cc1bba057662c03319f7820883e7010ecb723b93c3"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(IFF_UNIT.read_bytes()).hexdigest() == IFF_UNIT_SHA256,
            "IFF-unit custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-ratio-reduction-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_iff_unit_sha256"] == IFF_UNIT_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "necessary FFF ratio-reduction superset" and
            row["variable_count"] == 6 and
            row["block_order"] == ["dp(2)", "dp(4)"] and
            row["common_basis_size"] == 21 and
            row["outside_equation_order"] == [7, 5, 4, 6] and
            row["route_guard_count"] == 16 and
            row["extra_guards"] == ["e", "s", "a0m", "a2m"] and
            row["rank_cofactor_count"] == 6,
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "" and
            [stage["equation"] for stage in row["equation_stages"]] ==
            [7, 5, 4, 6] and len(row["route_stages"]) == 16 and
            len(row["extra_stages"]) == 4,
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
    mutation["row"]["outside_equation_order"] = [7, 5, 4]
    expect_rejected(mutation, "missing q6")
    mutation = deepcopy(payload)
    mutation["row"]["extra_guards"] = ["e", "a0m", "a2m"]
    expect_rejected(mutation, "missing ratio guard")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_RATIO_REDUCTION_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

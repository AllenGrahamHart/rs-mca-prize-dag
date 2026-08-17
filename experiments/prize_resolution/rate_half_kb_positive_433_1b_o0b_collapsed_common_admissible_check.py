#!/usr/bin/env python3
"""Outcome-neutral checker for exact collapsed-common admissibility."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
FGLM = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_result.json"
FACTOR = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_eliminant_factor.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_result.json"
SOURCE_SHA256 = "01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
FGLM_SHA256 = "a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f"
FACTOR_SHA256 = "8d0c74703d84ff3eebaf43e5c867fc23ed6ea387a05497f8acc7fafed2a570e1"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source-basis custody")
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(FGLM.read_bytes()).hexdigest() == FGLM_SHA256,
            "FGLM custody")
    require(hashlib.sha256(FACTOR.read_bytes()).hexdigest() == FACTOR_SHA256,
            "factor custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-collapsed-common-admissible-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_basis_sha256"] == SOURCE_SHA256 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_fglm_sha256"] == FGLM_SHA256 and
            payload["source_factor_sha256"] == FACTOR_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "exact admissible collapsed common locus" and
            row["variable_count"] == 4 and row["source_dimension"] == 0 and
            row["source_basis_size"] == 43 and row["source_vdim"] == 65 and
            row["route_guard_count"] == 16 and
            row["rank_cofactor_count"] == 6,
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "" and
            row["initial_dimension"] == 0 and
            row["initial_basis_size"] == 43 and row["initial_vdim"] == 65 and
            len(row["stages"]) == 16 and
            [stage["guard_index"] for stage in row["stages"]] == list(range(16)),
            "complete stage ledger")
    if row["unit"]:
        require(row["dimension"] == -1 and row["basis_size"] == 1 and
                row["cofactor_dimension"] == -1 and
                row["cofactor_basis_size"] == 1 and "UNIT=1" in row["stdout"],
                "unit result")
    else:
        require(row["dimension"] == 0 and row["basis_size"] > 0 and
                row["cofactor_dimension"] == 0 and "UNIT=0" in row["stdout"],
                "nonunit result")
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
    mutation["row"]["route_guard_count"] = 15
    expect_rejected(mutation, "missing route guard")
    mutation = deepcopy(payload)
    mutation["row"]["rank_cofactor_count"] = 5
    expect_rejected(mutation, "missing rank cofactor")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_ADMISSIBLE_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

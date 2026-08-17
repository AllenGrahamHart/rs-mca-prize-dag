#!/usr/bin/env python3
"""Outcome-neutral checker for the O0b collapsed common basis."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_program.py"
COLLAPSE_PROOF = HERE / "rate_half_kb_positive_433_1b_o0b_multifinite_infinity_collapse.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COLLAPSE_PROOF_SHA256 = "ed7a70cee69571b946ceef6a2c60e1c9f50438d2fb4dab37d19094265fa102a0"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COLLAPSE_PROOF.read_bytes()).hexdigest() ==
            COLLAPSE_PROOF_SHA256, "collapse-proof custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-collapsed-common-basis-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["source_collapse_proof_sha256"] == COLLAPSE_PROOF_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "necessary collapsed common superset" and
            row["variable_count"] == 4 and
            row["common_basis_size"] == 21 and
            row["collapsed_kernel_indices"] == [2, 5] and
            row["collapse_equation_count"] == 2 and
            row["generator_count"] == 23,
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "",
            "complete transcript")
    if row["unit"]:
        require(row["dimension"] == -1 and row["basis_size"] == 1 and
                row["basis"] == [] and "UNIT=1" in row["stdout"],
                "unit result")
    else:
        require(row["dimension"] >= 0 and
                row["basis_size"] == len(row["basis"]) and
                row["basis_size"] > 0 and "UNIT=0" in row["stdout"],
                "nonunit basis")
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
    mutation["row"]["collapsed_kernel_indices"] = [2]
    expect_rejected(mutation, "missing collapse equation")
    mutation = deepcopy(payload)
    mutation["row"]["relation"] = "exact admissible collapsed locus"
    expect_rejected(mutation, "overstated exactness")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_BASIS_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

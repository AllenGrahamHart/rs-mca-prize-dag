#!/usr/bin/env python3
"""Outcome-neutral checker for the O0b collapsed common FGLM audit."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_result.json"
SOURCE_SHA256 = "01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source-basis custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-collapsed-common-fglm-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_basis_sha256"] == SOURCE_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "exact basis-order conversion" and
            row["variable_count"] == 4 and
            row["source_dimension"] == 0 and
            row["source_basis_size"] == 43,
            "input ledger")
    require(row["dp_dimension"] == 0 and row["dp_basis_size"] == 43 and
            isinstance(row["dp_vdim"], int) and row["dp_vdim"] > 0,
            "degree ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "vdim": row["dp_vdim"]}
    require(row["stderr"] == "" and "LEX_END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "" and
            row["lex_dimension"] == 0 and
            row["lex_vdim"] == row["dp_vdim"] and
            row["lex_basis_size"] == len(row["lex_basis"]) and
            row["lex_basis_size"] > 0,
            "complete FGLM ledger")
    return {"status": "COMPLETE", "vdim": row["dp_vdim"]}


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
    mutation["row"]["dp_dimension"] = 1
    expect_rejected(mutation, "positive-dimensional source")
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["lex_vdim"] += 1
        expect_rejected(mutation, "degree mismatch")
    else:
        mutation = deepcopy(payload)
        mutation["row"]["dp_vdim"] = 0
        expect_rejected(mutation, "zero degree")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_COMMON_FGLM_CHECK_PASS "
          f"status={result['status']} vdim={result['vdim']} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

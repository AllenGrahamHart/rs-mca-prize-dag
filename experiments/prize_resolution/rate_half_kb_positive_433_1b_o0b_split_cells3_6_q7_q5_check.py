#!/usr/bin/env python3
"""Outcome-neutral checker for the O0b q3 -> q7 -> q5 diagnostic."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
SOURCE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_q7_q5_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
SOURCE_SHA256 = "ce0396a9f6d951270a5ec3ba9b8371919020dcac75ca11af488d9fabc5e0edb9"
SOURCE_BASIS_SHA256 = "679c448e3587f4bb11f39a6742aa7439d9b909ad68cf19834ca463d634c5aceb"
CASE = [3, "S0", -1, -1, -1, 2, 0]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cells3-6-q7-q5-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE,
            "scope")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_single_extensions_sha256"] == SOURCE_SHA256,
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["source_equations"] == ["q3", "q7"] and
            row["added_equation"] == "q5" and
            row["source_basis_size"] == 128 and
            row["source_basis_sha256"] == SOURCE_BASIS_SHA256 and
            row["standard_basis_attribute_set"] is True,
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT"}
    encoded = json.dumps(row["basis"], separators=(",", ":"))
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and
            "not a standard basis" not in row["stdout"] and
            isinstance(row["normal_form_degree"], int) and
            isinstance(row["normal_form_terms"], int) and
            row["basis_size"] == len(row["basis"]) and
            row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
            "complete basis")
    return {"status": "COMPLETE"}


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
    mutation["row"]["added_equation"] = "q4"
    expect_rejected(mutation, "wrong equation")
    mutation = deepcopy(payload)
    mutation["row"]["source_basis_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong source basis")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_Q7_Q5_CHECK_PASS "
          f"status={result['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

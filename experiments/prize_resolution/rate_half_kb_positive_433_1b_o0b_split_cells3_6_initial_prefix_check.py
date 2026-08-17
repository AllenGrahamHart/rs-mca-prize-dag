#!/usr/bin/env python3
"""Outcome-neutral checker for the O0b initial-prefix diagnostic."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
CASE = [3, "S0", -1, -1, -1, 2, 0]
PREFIX_COUNTS = [1, 2, 3, 4, 5]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "global-basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cells3-6-initial-prefix-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE,
            "scope")
    require(payload["prefix_counts"] == PREFIX_COUNTS and
            payload["expected_row_count"] == 5 and
            payload["processed_row_count"] == 5 and
            payload["remote_errors"] == [] and len(payload["rows"]) == 5,
            "complete collection")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_global_basis_sha256"] == BASIS_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256,
            "source fields")
    rows = payload["rows"]
    require([row["prefix_count"] for row in rows] == PREFIX_COUNTS,
            "ordered prefix cover")
    require(len({row["program_sha256"] for row in rows}) == 5,
            "distinct programs")
    basis_payload = json.loads(BASIS.read_text())
    source_row = next(row for row in basis_payload["rows"] if row["epsilon"] == [-1, -1])
    completed = 0
    timed = 0
    for row in rows:
        prefix_count = row["prefix_count"]
        require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
        require(row["common_basis_size"] == 21 and
                len(row["outside_equations"]) == prefix_count and
                row["source_basis_sha256"] == source_row["basis_sha256"],
                "input ledger")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str),
                    "timeout transcript")
            timed += 1
            continue
        encoded = json.dumps(row["basis"], separators=(",", ":"))
        require(row["stderr"] == "" and "END" in row["stdout"] and
                "?" not in row["stdout"] and
                row["basis_size"] == len(row["basis"]) and
                row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
                "complete basis")
        completed += 1
    return {"rows": 5, "complete": completed, "timeout": timed}


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
    mutation["rows"][0]["prefix_count"] = 5
    expect_rejected(mutation, "wrong order")
    mutation = deepcopy(payload)
    mutation["rows"][0]["source_basis_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong source basis")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_INITIAL_PREFIX_CHECK_PASS "
          f"rows={result['rows']} complete={result['complete']} "
          f"timeout={result['timeout']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Outcome-neutral checker for O0b single-equation extensions."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PREFIX = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
PREFIX_SHA256 = "486c36b63335f0b30aa17008481df341869f5d37b32456d58fc40438deb7daa6"
CASE = [3, "S0", -1, -1, -1, 2, 0]
EQUATION_INDICES = [4, 5, 6, 7]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(PREFIX.read_bytes()).hexdigest() == PREFIX_SHA256,
            "prefix custody")
    prefix_payload = json.loads(PREFIX.read_text())
    source = next(row for row in prefix_payload["rows"] if row["prefix_count"] == 1)
    require(source["status"] == "COMPLETE" and source["basis_size"] == 51,
            "source prefix")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cells3-6-single-extensions-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["case"] == CASE,
            "scope")
    require(payload["equation_indices"] == EQUATION_INDICES and
            payload["expected_row_count"] == 4 and
            payload["processed_row_count"] == 4 and
            payload["remote_errors"] == [] and len(payload["rows"]) == 4,
            "complete collection")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_compiler_sha256"] == COMPILER_SHA256 and
            payload["source_prefix_sha256"] == PREFIX_SHA256,
            "source fields")
    rows = payload["rows"]
    require([row["equation_index"] for row in rows] == EQUATION_INDICES and
            [row["equation_name"] for row in rows] == ["q4", "q5", "q6", "q7"],
            "ordered equation cover")
    require(len({row["program_sha256"] for row in rows}) == 4,
            "distinct programs")
    completed = 0
    timed = 0
    for row in rows:
        require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
        require(row["source_prefix_count"] == 1 and
                row["source_prefix_basis_size"] == 51 and
                row["source_prefix_basis_sha256"] == source["basis_sha256"],
                "source basis ledger")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str),
                    "timeout transcript")
            timed += 1
            continue
        encoded = json.dumps(row["basis"], separators=(",", ":"))
        require(row["stderr"] == "" and "END" in row["stdout"] and
                "?" not in row["stdout"] and
                isinstance(row["normal_form_degree"], int) and
                isinstance(row["normal_form_terms"], int) and
                row["basis_size"] == len(row["basis"]) and
                row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
                "complete basis")
        completed += 1
    return {"rows": 4, "complete": completed, "timeout": timed}


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
    mutation["rows"][0]["equation_index"] = 7
    expect_rejected(mutation, "wrong order")
    mutation = deepcopy(payload)
    mutation["rows"][0]["source_prefix_basis_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong source basis")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_SINGLE_EXTENSIONS_CHECK_PASS "
          f"rows={result['rows']} complete={result['complete']} "
          f"timeout={result['timeout']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

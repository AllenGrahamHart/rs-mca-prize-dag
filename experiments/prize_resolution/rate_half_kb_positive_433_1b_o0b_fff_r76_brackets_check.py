#!/usr/bin/env python3
"""Outcome-neutral checker for the exact FFF R76 bracket bank."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GRAPH = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
RAW_CORE = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_program.py"
PROGRESSIVE = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_program.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_program.py"
SOURCE_TIMEOUT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
RAW_CORE_SHA256 = "7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6"
PROGRESSIVE_SHA256 = "b73c4e888dc69353bc823c787babdf7c4b8b5d2a4c7efe708ffef16604f045ca"
SOURCE_TIMEOUT_SHA256 = "0a2173e080a4a5029713aa8fa8feea73056a5e84b8139bc780684d5545117d95"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def expected_keys():
    return [
        (family, index)
        for family, count in (("M0", 5), ("M1", 5), ("M2", 4))
        for index in range(count)
    ]


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    require(hashlib.sha256(RAW_CORE.read_bytes()).hexdigest() == RAW_CORE_SHA256,
            "raw-core custody")
    require(hashlib.sha256(PROGRESSIVE.read_bytes()).hexdigest() ==
            PROGRESSIVE_SHA256, "progressive-core custody")
    require(hashlib.sha256(SOURCE_TIMEOUT.read_bytes()).hexdigest() ==
            SOURCE_TIMEOUT_SHA256, "timeout custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-brackets-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_graph_sha256"] == GRAPH_SHA256 and
            payload["source_raw_core_sha256"] == RAW_CORE_SHA256 and
            payload["source_progressive_sha256"] == PROGRESSIVE_SHA256 and
            payload["source_timeout_sha256"] == SOURCE_TIMEOUT_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "exact reduced R76 bracket bank" and
            row["source_progressive_relation"] ==
            "exact progressive R76 coefficients on admissible FFF base graph" and
            row["bracket_layout"] == [
                {"family": "M0", "count": 5},
                {"family": "M1", "count": 5},
                {"family": "M2", "count": 4},
            ] and row["bracket_count"] == 14 and
            row["expected_zero_brackets"] == [
                {"family": "M0", "index": 2},
                {"family": "M1", "index": 0},
            ] and row["intermediate_reduction_count"] == 61 and
            row["graph_basis_sha256"] ==
            "7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e",
            "input ledger")
    require(len(row["intermediate_stages"]) <= 61, "intermediate prefix")
    stage_keys = [(value["family"], value["index"])
                  for value in row["bracket_stages"]]
    value_keys = [(value["family"], value["index"]) for value in row["brackets"]]
    keys = expected_keys()
    require(stage_keys == keys[:len(stage_keys)] and
            value_keys == keys[:len(value_keys)], "bracket prefixes")
    for value in row["brackets"]:
        require(value["polynomial_sha256"] ==
                hashlib.sha256(value["polynomial"].encode()).hexdigest(),
                "bracket hash")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "bracket_count": len(row["brackets"])}
    require(row["stderr"] == "" and row["input_program"] == "" and
            len(row["intermediate_stages"]) == 61 and
            len(row["bracket_stages"]) == 14 and len(row["brackets"]) == 14,
            "complete bracket ledger")
    lookup = {
        (value["family"], value["index"]): value["polynomial"]
        for value in row["brackets"]
    }
    require(lookup[("M0", 2)] == "0" and lookup[("M1", 0)] == "0" and
            all(value != "0" for key, value in lookup.items()
                if key not in {("M0", 2), ("M1", 0)}),
            "exact zero pattern")
    return {"status": "COMPLETE", "bracket_count": 14}


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
    mutation["row"]["bracket_count"] = 13
    expect_rejected(mutation, "wrong bracket count")
    mutation = deepcopy(payload)
    mutation["row"]["expected_zero_brackets"] = []
    expect_rejected(mutation, "lost zero pattern")
    if payload["row"]["brackets"]:
        mutation = deepcopy(payload)
        mutation["row"]["brackets"][0]["polynomial"] += "+1"
        expect_rejected(mutation, "bracket mutation")
        return 4
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_BRACKETS_CHECK_PASS "
          f"status={result['status']} brackets={result['bracket_count']} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

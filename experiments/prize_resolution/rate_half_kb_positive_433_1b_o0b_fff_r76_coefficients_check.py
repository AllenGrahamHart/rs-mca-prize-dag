#!/usr/bin/env python3
"""Outcome-neutral checker for the FFF R76 coefficient reductions."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GRAPH = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-coefficients-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_graph_sha256"] == GRAPH_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] ==
            "exact R76 coefficients on admissible FFF base graph" and
            row["resultant_variable"] == "E" and
            row["variable_count"] == 5 and
            row["variables"] == ["x", "t", "r", "c", "b"] and
            row["coefficient_order"] == list(range(9)) and
            row["maximum_s_degree"] == 8 and
            row["q7_E_degree"] == 2 and row["q6_E_degree"] == 2 and
            row["graph_basis_size"] == 48 and
            row["graph_basis_sha256"] ==
            "7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e",
            "input ledger")
    stage_indices = [stage["coefficient"] for stage in row["coefficient_stages"]]
    value_indices = [value["coefficient"] for value in row["coefficients"]]
    require(stage_indices == list(range(9))[:len(stage_indices)] and
            value_indices == list(range(9))[:len(value_indices)],
            "coefficient prefixes")
    for value in row["coefficients"]:
        require(value["polynomial_sha256"] ==
                hashlib.sha256(value["polynomial"].encode()).hexdigest(),
                "coefficient hash")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "coefficient_count": len(row["coefficients"])}
    require(row["stderr"] == "" and row["input_program"] == "" and
            len(row["coefficient_stages"]) == 9 and
            len(row["coefficients"]) == 9 and
            all(stage["term_count"] >= 0 and stage["degree"] >= -1
                for stage in row["coefficient_stages"]) and
            any(stage["term_count"] > 0 for stage in row["coefficient_stages"]),
            "complete coefficient ledger")
    return {"status": "COMPLETE", "coefficient_count": 9}


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
    mutation["row"]["maximum_s_degree"] = 7
    expect_rejected(mutation, "wrong s degree")
    mutation = deepcopy(payload)
    mutation["row"]["resultant_variable"] = "s"
    expect_rejected(mutation, "wrong resultant variable")
    if payload["row"]["coefficients"]:
        mutation = deepcopy(payload)
        mutation["row"]["coefficients"][0]["polynomial"] += "+1"
        expect_rejected(mutation, "coefficient mutation")
        return 4
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_COEFFICIENTS_CHECK_PASS "
          f"status={result['status']} coefficients={result['coefficient_count']} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

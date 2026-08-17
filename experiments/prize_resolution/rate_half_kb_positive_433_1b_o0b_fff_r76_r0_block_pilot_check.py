#!/usr/bin/env python3
"""Outcome-neutral checker for the R76[0] block-square pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
GRAPH = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
BRACKETS = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_result.json"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
BRACKETS_SHA256 = "08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    require(hashlib.sha256(BRACKETS.read_bytes()).hexdigest() == BRACKETS_SHA256,
            "bracket custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-r76-r0-block-pilot-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_graph_sha256"] == GRAPH_SHA256 and
            payload["source_brackets_sha256"] == BRACKETS_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "exact R76[0] block-square pilot" and
            row["target_coefficient"] == 0 and
            row["source_family"] == "M0" and row["source_index"] == 0 and
            row["source_polynomial_sha256"] ==
            "4dc6a43d99611455c3ffadf53c2f2489f0e252371c280c138377ecc2b0a44839" and
            row["source_term_count"] == 1152 and row["block_size"] == 128 and
            row["block_index"] == 0 and row["term_start"] == 0 and
            row["term_end"] == 128 and row["input_term_count"] == 128 and
            row["product_multiplier"] == 1 and row["graph_basis_size"] == 48 and
            row["graph_basis_sha256"] ==
            "7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e",
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT"}
    require(row["stderr"] == "" and row["input_program"] == "" and
            row["observed_input_terms"] == 128 and row["raw_term_count"] > 0 and
            row["normal_term_count"] > 0 and row["normal_polynomial"] and
            row["normal_sha256"] ==
            hashlib.sha256(row["normal_polynomial"].encode()).hexdigest(),
            "complete product ledger")
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
    mutation["row"]["term_end"] = 127
    expect_rejected(mutation, "wrong block boundary")
    mutation = deepcopy(payload)
    mutation["row"]["product_multiplier"] = 2
    expect_rejected(mutation, "wrong square multiplier")
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["normal_polynomial"] += "+1"
        expect_rejected(mutation, "normal mutation")
        return 4
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_R0_BLOCK_PILOT_CHECK_PASS "
          f"status={result['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

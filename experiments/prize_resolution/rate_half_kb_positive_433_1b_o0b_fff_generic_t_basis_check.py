#!/usr/bin/env python3
"""Outcome-neutral checker for the generic-t FFF graph basis."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
GRAPH = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_result.json"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-generic-t-basis-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_graph_sha256"] == GRAPH_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] ==
            "exact admissible FFF ratio graph over F_p(t)" and
            row["coefficient_field"] == "F_2130706433(t)" and
            row["parameter"] == "t" and
            row["fiber_variables"] == ["x", "r", "c", "b"] and
            row["source_dimension"] == 1 and row["source_basis_size"] == 48 and
            row["source_basis_sha256"] ==
            "7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e" and
            row["denominator_exceptions_open"] is True,
            "input ledger")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT"}
    encoded = json.dumps(row["basis"], separators=(",", ":"))
    require(row["stderr"] == "" and row["input_program"] == "" and
            row["dimension"] == 0 and row["basis_size"] > 0 and
            row["vector_space_dimension"] > 0 and
            len(row["basis"]) == row["basis_size"] and
            row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
            "complete generic basis")
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
    mutation["row"]["parameter"] = "b"
    expect_rejected(mutation, "wrong parameter")
    mutation = deepcopy(payload)
    mutation["row"]["denominator_exceptions_open"] = False
    expect_rejected(mutation, "hidden exceptions")
    if payload["row"]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["row"]["basis"][0] += "+1"
        expect_rejected(mutation, "basis mutation")
        return 4
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_GENERIC_T_BASIS_CHECK_PASS "
          f"status={result['status']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

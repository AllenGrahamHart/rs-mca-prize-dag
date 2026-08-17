#!/usr/bin/env python3
"""Outcome-neutral checker for the six-case basis-fed cross pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
CASES = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_cases.json"
COMPILER = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_outside_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
CASES_SHA256 = "2e1eea3589e0737e9efa7a3a49a0492d6fece4577b93a36eb1f6badf0b499b42"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def row_case(row):
    return (
        row["cell"], row["lane"], row["sigma_o"], *row["epsilon"],
        row["xi_index"], row["pairing_index"],
    )


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    case_payload = json.loads(CASES.read_text())
    cases = tuple(tuple(row) for row in case_payload["cases"])
    encoded = json.dumps(cases, separators=(",", ":"))
    require(case_payload["cases_sha256"] == CASES_SHA256 and
            hashlib.sha256(encoded.encode()).hexdigest() == CASES_SHA256,
            "case custody")
    cache = json.loads(CACHE.read_text())
    basis = json.loads(BASIS.read_text())
    packet_hashes = {
        tuple(row["epsilon"]): row["packet_sha256"] for row in cache["rows"]
    }
    basis_hashes = {
        tuple(row["epsilon"]): row["basis_sha256"] for row in basis["rows"]
    }
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cells3-6-basis-cross-pilot-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and payload["remote_errors"] == [],
            "complete collection")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_cases_sha256"] == hashlib.sha256(CASES.read_bytes()).hexdigest() and
            payload["source_compiler_sha256"] == hashlib.sha256(COMPILER.read_bytes()).hexdigest() and
            payload["source_program_sha256"] == hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["selected_cases_sha256"] == CASES_SHA256,
            "source fields")
    require(payload["expected_case_count"] == 6 and
            payload["processed_case_count"] == 6 and len(payload["rows"]) == 6,
            "row census")
    rows = payload["rows"]
    require([row["index"] for row in rows] == list(range(6)) and
            tuple(row_case(row) for row in rows) == cases, "ordered case cover")
    require(len({row["program_sha256"] for row in rows}) == 6,
            "distinct programs")
    unit_count = 0
    nonunit_count = 0
    timeout_count = 0
    for row in rows:
        require(row["status"] in {"COMPLETE", "TIMEOUT"}, "accepted row status")
        require(row["common_basis_size"] == 21 and
                row["outside_equation_count"] == 5 and
                row["guard_count"] == 40 and row["rank_cofactor_count"] == 6,
                "input ledger")
        signs = tuple(row["epsilon"])
        require(row["packet_sha256"] == packet_hashes[signs] and
                row["basis_sha256"] == basis_hashes[signs], "sign source custody")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str), "timeout transcript")
            timeout_count += 1
            continue
        require(row["stderr"] == "" and "END" in row["stdout"] and
                "?" not in row["stdout"], "complete transcript")
        if row["unit"]:
            require(row["dimension"] == -1 and row["basis_size"] == 1 and
                    row["input_program"] == "" and "UNIT=1" in row["stdout"],
                    "unit row")
            unit_count += 1
        else:
            require(row["input_program"] != "" and "UNIT=0" in row["stdout"],
                    "retained nonunit row")
            nonunit_count += 1
    require(payload["unit_count"] == unit_count, "unit summary")
    return {
        "rows": 6,
        "unit": unit_count,
        "nonunit": nonunit_count,
        "timeout": timeout_count,
    }


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
    mutation["rows"][0]["index"] = 5
    expect_rejected(mutation, "wrong order")
    mutation = deepcopy(payload)
    mutation["rows"][0]["basis_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong basis")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_BASIS_CROSS_CHECK_PASS "
          f"rows={result['rows']} unit={result['unit']} nonunit={result['nonunit']} "
          f"timeout={result['timeout']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

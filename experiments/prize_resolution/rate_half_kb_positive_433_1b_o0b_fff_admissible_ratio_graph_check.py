#!/usr/bin/env python3
"""Outcome-neutral checker for the guarded FFF base ratio graph."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_program.py"
SOURCE_TIMEOUT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
SOURCE_TIMEOUT_SHA256 = "9992611165f31733a3c497b27b93c39f65b621f9e3acc1489ab46c3d78e7096e"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(SOURCE_TIMEOUT.read_bytes()).hexdigest() ==
            SOURCE_TIMEOUT_SHA256, "source-timeout custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-admissible-ratio-graph-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_timeout_sha256"] == SOURCE_TIMEOUT_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
            "source fields")
    row = payload["row"]
    require(row["status"] in {"COMPLETE", "TIMEOUT"}, "row status")
    require(row["relation"] == "necessary admissible FFF base ratio graph" and
            row["variable_count"] == 5 and
            row["variables"] == ["x", "t", "r", "c", "b"] and
            row["graph_relation"] == "a2m*x-a0m" and
            row["common_basis_size"] == 21 and
            row["common_basis_dimension"] == 1 and
            row["inherited_route_guard_count"] == 16 and
            row["inherited_rank_cofactor_count"] == 6 and
            row["base_guards"] == ["x", "a0m", "a2m"],
            "input ledger")
    require(row["graph_dimension"] is None or
            (row["graph_dimension"] == 1 and row["graph_basis_size"] > 0),
            "graph stage")
    actual = [stage["guard_index"] for stage in row["base_guard_stages"]]
    require(actual == [0, 1, 2][:len(actual)], "guard prefix")
    if row["status"] == "TIMEOUT":
        require(isinstance(row["partial_stdout"], str) and
                isinstance(row["partial_stderr"], str), "timeout transcript")
        return {"status": "TIMEOUT", "unit": False}
    require(row["stderr"] == "" and "END" in row["stdout"] and
            "?" not in row["stdout"] and row["input_program"] == "" and
            row["graph_dimension"] == 1 and
            len(row["base_guard_stages"]) == 3,
            "complete stage ledger")
    encoded = json.dumps(row["basis"], separators=(",", ":"))
    require(row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
            "basis hash")
    if row["unit"]:
        require(row["dimension"] == -1 and row["basis_size"] == 1 and
                row["basis"] == [] and "UNIT=1" in row["stdout"],
                "unit result")
    else:
        require(row["dimension"] == 1 and row["basis_size"] > 1 and
                len(row["basis"]) == row["basis_size"] and
                "UNIT=0" in row["stdout"], "nonunit result")
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
    mutation["row"]["base_guards"] = ["x", "a2m"]
    expect_rejected(mutation, "missing base guard")
    mutation = deepcopy(payload)
    mutation["row"]["inherited_route_guard_count"] = 0
    expect_rejected(mutation, "lost inherited guards")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_ADMISSIBLE_RATIO_GRAPH_CHECK_PASS "
          f"status={result['status']} unit={int(result['unit'])} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

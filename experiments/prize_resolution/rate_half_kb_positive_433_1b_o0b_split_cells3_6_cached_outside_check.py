#!/usr/bin/env python3
"""Check the repaired cached-input O0b split cells-3/6 pilot."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
MANIFEST = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
CORE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_pilot_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"
REPRESENTATIVES_SHA256 = "39fb277a94d8ee3a24e3a8f9e1f0bb50014665ca7c151659d4dc8fcd912392d6"
PILOT_SHA256 = "a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def row_key(row):
    return (
        row["cell"], row["lane"], row["sigma_o"], *row["epsilon"],
        row["xi_index"], row["pairing_index"],
    )


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == MANIFEST_SHA256,
            "manifest custody")
    manifest = json.loads(MANIFEST.read_text())
    cache = json.loads(CACHE.read_text())
    payload = payload or json.loads(RESULT.read_text())
    expected = tuple(tuple(row) for row in manifest["pilot_representatives"])
    packet_hashes = {
        tuple(row["epsilon"]): row["packet_sha256"] for row in cache["rows"]
    }
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cells3-6-cached-pilot-v1",
            "schema")
    require(payload["complete"] is True and payload["field"] == 2130706433,
            "complete field result")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_manifest_sha256"] == MANIFEST_SHA256 and
            payload["source_core_sha256"] ==
            hashlib.sha256(CORE.read_bytes()).hexdigest(), "source fields")
    require(payload["representatives_sha256"] == REPRESENTATIVES_SHA256 and
            payload["selected_cases_sha256"] == PILOT_SHA256,
            "case custody")
    require(payload["expected_case_count"] == 24 and
            payload["processed_case_count"] == 24 and len(payload["rows"]) == 24,
            "row census")
    require(payload["status_counts"] == {"COMPLETE": 24} and
            payload["unit_count"] == 24, "all-unit summary")
    rows = payload["rows"]
    require(tuple(row_key(row) for row in rows) == expected, "ordered case cover")
    require(len({row["program_sha256"] for row in rows}) == 24,
            "distinct programs")
    for row in rows:
        require(row["status"] == "COMPLETE" and row["unit"] is True,
                "unit row")
        require(row["dimension"] == -1 and row["basis_size"] == 1,
                "unit ideal shape")
        require(row["common_equation_count"] == 3 and
                row["outside_equation_count"] == 5 and
                row["rank_cofactor_count"] == 6 and row["guard_count"] > 30,
                "equation/guard ledger")
        require(row["packet_sha256"] == packet_hashes[tuple(row["epsilon"])],
                "sign-packet custody")
        require(row["input_program"] == "" and row["stderr"] == "",
                "compact clean output")
        require("COFACTOR_DIM=-1,COFACTOR_SIZE=1" in row["stdout"] and
                "BEGIN\nDIM=-1\nSIZE=1\nUNIT=1\nEND" in row["stdout"] and
                "?" not in row["stdout"], "saturation transcript")
    return {"rows": 24, "unit": 24, "programs": 24}


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutation = deepcopy(payload)
    mutation["complete"] = False
    expect_rejected(mutation, "incomplete checkpoint")
    mutation = deepcopy(payload)
    mutation["rows"][0]["packet_sha256"] = "0" * 64
    expect_rejected(mutation, "wrong sign packet")
    mutation = deepcopy(payload)
    mutation["rows"][0]["rank_cofactor_count"] = 5
    expect_rejected(mutation, "missing rank chart")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_CACHED_CHECK_PASS "
          f"rows={result['rows']} unit={result['unit']} programs={result['programs']} "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

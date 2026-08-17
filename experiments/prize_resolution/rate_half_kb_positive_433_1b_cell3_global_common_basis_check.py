#!/usr/bin/env python3
"""Check the guarded global cell-3 common Groebner bases."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    cache = json.loads(CACHE.read_text())
    payload = payload or json.loads(RESULT.read_text())
    packet_hashes = {
        tuple(row["epsilon"]): row["packet_sha256"] for row in cache["rows"]
    }
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-global-common-basis-v1",
            "schema")
    require(payload["complete"] is True and payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256,
            "complete source result")
    require(payload["expected_row_count"] == 4 and
            payload["processed_row_count"] == 4 and len(payload["rows"]) == 4,
            "row census")
    require([row["epsilon"] for row in payload["rows"]] ==
            [[-1, -1], [-1, 1], [1, -1], [1, 1]], "ordered sign cover")
    program_hashes = set()
    basis_hashes = set()
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["dimension"] == 1,
                "complete common curve")
        require(row["basis_size"] == len(row["basis"]) and row["basis_size"] > 0,
                "basis census")
        encoded = json.dumps(row["basis"], separators=(",", ":"))
        require(row["basis_sha256"] == hashlib.sha256(encoded.encode()).hexdigest(),
                "basis hash")
        require(row["packet_sha256"] == packet_hashes[tuple(row["epsilon"])],
                "sign packet custody")
        require("BEGIN\nDIM=1\nSIZE=" in row["stdout"] and
                "BASIS_BEGIN" in row["stdout"] and "BASIS_END" in row["stdout"] and
                "?" not in row["stdout"] and row["stderr"] == "",
                "complete transcript")
        program_hashes.add(row["program_sha256"])
        basis_hashes.add(row["basis_sha256"])
    require(len(program_hashes) == 4 and len(basis_hashes) == 4,
            "distinct sign programs and bases")
    return {"rows": 4, "programs": 4, "bases": 4}


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
    expect_rejected(mutation, "incomplete result")
    mutation = deepcopy(payload)
    mutation["rows"][0]["dimension"] = 2
    expect_rejected(mutation, "wrong dimension")
    mutation = deepcopy(payload)
    mutation["rows"][0]["basis"].pop()
    expect_rejected(mutation, "truncated basis")
    return 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    result = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_CELL3_GLOBAL_COMMON_BASIS_CHECK_PASS "
          f"rows={result['rows']} programs={result['programs']} "
          f"bases={result['bases']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

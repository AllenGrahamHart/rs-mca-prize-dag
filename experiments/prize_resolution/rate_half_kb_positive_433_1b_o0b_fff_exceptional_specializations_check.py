#!/usr/bin/env python3
"""Checker for the original-system FFF exceptional specializations."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GRAPH = HERE / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
ROOTS = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
ROOTS_SHA256 = "e845607b89e7d21159bd308cbf00f9a3fd74a25120bc4d479a607f7e9d8751a7"
ROOT_VALUES = [
    0, 1, 16711679, 47655010, 451278922, 465887767, 666570304,
    676802667, 1036595577, 1141382033, 1629292471, 1893783428,
    2113994754, 2130706432,
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in ((CACHE, CACHE_SHA256), (GRAPH, GRAPH_SHA256),
                         (ROOTS, ROOTS_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-exceptional-specializations-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_graph_sha256"] == GRAPH_SHA256 and
            payload["source_roots_sha256"] == ROOTS_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["roots"] == ROOT_VALUES and len(payload["rows"]) == 14 and
            [row["root"] for row in payload["rows"]] == ROOT_VALUES, "envelope")
    for row in payload["rows"]:
        require(row["status"] in {"COMPLETE", "TIMEOUT"} and
                row["relation"] ==
                "original guarded FFF q5-q7-q6 exceptional specialization" and
                row["engine"] == "Singular slimgb" and
                row["field"] == 2130706433 and
                row["variables"] == ["E", "s", "x", "t", "r", "c", "b"] and
                row["source_graph_basis_size"] == 48 and
                row["source_graph_basis_sha256"] ==
                "7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e" and
                row["source_graph_dimension"] == 1 and
                row["equation_order"] == ["base", "q5", "q7", "q6"] and
                row["omitted_finite_pair"] == "q4" and
                row["uses_generic_rational_basis"] is False and
                row["root_polynomial_sha256"] ==
                "3589dc59d90716f76248f83b667411527fda6ceaff5b845b9dc673afbc5d4592",
                "row input")
        require([stage["stage"] for stage in row["stages"]] ==
                ["base", "q5", "q7", "q6"][:len(row["stages"])], "stages")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str), "timeout")
        else:
            require(row["input_program"] == "" and len(row["stages"]) == 4 and
                    isinstance(row["unit"], bool) and row["basis_size"] >= 1 and
                    (row["unit"] is False or
                     (row["dimension"] == -1 and row["basis_size"] == 1)) and
                    ((row["unit"] and row["basis"] == []) or
                     (not row["unit"] and
                      len(row["basis"]) == row["basis_size"])) and
                    row["basis_sha256"] == hashlib.sha256(
                        json.dumps(row["basis"], separators=(",", ":")).encode()
                    ).hexdigest(), "complete row")
    return payload["rows"]


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutations = []
    mutation = deepcopy(payload)
    mutation["source_roots_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["roots"] = list(reversed(ROOT_VALUES))
    mutations.append((mutation, "roots"))
    mutation = deepcopy(payload)
    mutation["rows"][0]["uses_generic_rational_basis"] = True
    mutations.append((mutation, "basis boundary"))
    if payload["rows"] and payload["rows"][0]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["rows"][0]["basis_sha256"] = "0" * 64
        mutations.append((mutation, "basis"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    rows = verify()
    mutations = hostile_audit() if args.hostile else 0
    closed = sum(row["status"] == "COMPLETE" and row["unit"] for row in rows)
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_EXCEPTIONAL_"
          f"SPECIALIZATIONS_CHECK_PASS closed={closed}/14 "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

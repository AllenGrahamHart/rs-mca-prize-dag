#!/usr/bin/env python3
"""Checker for guarded q4 replays on the exceptional FFF survivors."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
SURVIVORS = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_result.json"
PROGRAM = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_program.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
SURVIVORS_SHA256 = "c066bb4f5813be4915e40a51225287cfde11284b3b3df4cabdae889778a97b88"
ROOT_VALUES = [
    0, 1, 16711679, 47655010, 451278922, 1629292471, 1893783428,
    2113994754, 2130706432,
]
EXPECTED_STAGES = (
    ["lift"] + [f"route:{index}" for index in range(16)] +
    [f"extra:{index}" for index in range(5)] + ["cofactor", "q4"]
)
ROUTE_GUARDS = [
    "b", "c", "r", "t", "b - 1", "b + 1", "c - 1", "c + 1",
    "b - c", "b + c", "r^2 - 1", "r^2 + 1", "t^2 - 1",
    "t^2 + 1", "-r^2 + t^2", "r^2 + t^2",
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify(payload=None):
    for path, digest in ((CACHE, CACHE_SHA256), (SURVIVORS, SURVIVORS_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-exceptional-admissibility-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == 2130706433 and
            payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_survivors_sha256"] == SURVIVORS_SHA256 and
            payload["source_program_sha256"] ==
            hashlib.sha256(PROGRAM.read_bytes()).hexdigest() and
            payload["roots"] == ROOT_VALUES and len(payload["rows"]) == 9 and
            [row["root"] for row in payload["rows"]] == ROOT_VALUES, "envelope")
    for row in payload["rows"]:
        require(row["status"] in {"COMPLETE", "TIMEOUT"} and
                row["relation"] ==
                "guarded lifted q4 replay on exceptional FFF survivor" and
                row["engine"] == "Singular slimgb and saturation" and
                row["field"] == 2130706433 and
                row["variables"] == ["e", "E", "s", "x", "t", "r", "c", "b"] and
                row["lift_relation"] == "e^2-E" and
                row["route_guards"] == ROUTE_GUARDS and
                row["extra_guards"] == ["e", "s", "x", "a0m", "a2m"] and
                row["rank_cofactor_count"] == 6 and
                row["equation"] == "original finite-pair q4 resultant" and
                row["expected_stages"] == EXPECTED_STAGES and
                row["packet_sha256"] ==
                "fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9",
                "row input")
        require([stage["stage"] for stage in row["stages"]] ==
                EXPECTED_STAGES[:len(row["stages"])], "stages")
        if row["status"] == "TIMEOUT":
            require(isinstance(row["partial_stdout"], str) and
                    isinstance(row["partial_stderr"], str), "timeout")
        else:
            expected_first = next(
                (stage["stage"] for stage in row["stages"]
                 if stage["dimension"] == -1 and stage["basis_size"] == 1), None
            )
            require(row["input_program"] == "" and len(row["stages"]) == 24 and
                    row["first_unit_stage"] == expected_first and
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
    mutation["source_survivors_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["roots"] = list(reversed(ROOT_VALUES))
    mutations.append((mutation, "roots"))
    mutation = deepcopy(payload)
    mutation["rows"][0]["route_guards"] = []
    mutations.append((mutation, "guards"))
    if payload["rows"] and payload["rows"][0]["status"] == "COMPLETE":
        mutation = deepcopy(payload)
        mutation["rows"][0]["first_unit_stage"] = "q4"
        mutations.append((mutation, "first unit"))
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
          f"ADMISSIBILITY_CHECK_PASS closed={closed}/9 "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit the incomplete cached-input cells-3/6 pilot."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_pilot_result.json"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"
RESULT_SHA256 = "4d2471d23f0ac04f5e049b6a84cd08152f85911f5cb72b0b5ae3a436d414accf"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def row_key(row):
    return (
        row["cell"], row["lane"], row["sigma_o"], *row["epsilon"],
        row["xi_index"], row["pairing_index"],
    )


def main():
    require(hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == MANIFEST_SHA256,
            "manifest custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    manifest = json.loads(MANIFEST.read_text())
    payload = json.loads(RESULT.read_text())
    expected = tuple(tuple(row) for row in manifest["pilot_representatives"])
    require(payload["complete"] is False, "incomplete checkpoint")
    require(payload["expected_case_count"] == 24 and
            payload["processed_case_count"] == 23 and len(payload["rows"]) == 23,
            "partial checkpoint census")
    require(payload["status_counts"] == {"TIMEOUT": 23} and
            payload["unit_count"] == 0, "timeout census")
    require(tuple(row_key(row) for row in payload["rows"]) == expected[:23],
            "ordered partial cover")
    require(len({row["program_sha256"] for row in payload["rows"]}) == 23,
            "distinct timed programs")
    for row in payload["rows"]:
        require(row["status"] == "TIMEOUT", "timeout row")
        require(row["partial_stdout"] == "" and row["partial_stderr"] == "",
                "no initial Groebner transcript")
        require("unit" not in row and len(row["program_sha256"]) == 64,
                "no mathematical result")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_CACHED_INCOMPLETE_PASS "
          "processed=23 timeouts=23 missing=1 mathematical_rows=0")


if __name__ == "__main__":
    main()

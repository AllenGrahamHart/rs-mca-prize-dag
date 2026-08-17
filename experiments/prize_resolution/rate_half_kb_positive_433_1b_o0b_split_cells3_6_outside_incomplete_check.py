#!/usr/bin/env python3
"""Audit the bounded incomplete cells-3/6 outside pilot checkpoint."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_outside_pilot_result.json"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"
RESULT_SHA256 = "2a48b176a5c7a60f6a32ce9b234d18af57aa7b283142f4e1533065af0eb1d8fa"


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
            payload["processed_case_count"] == 24 and len(payload["rows"]) == 24,
            "checkpoint census")
    require(payload["status_counts"] == {"REMOTE_ERROR": 24} and
            payload["unit_count"] == 0, "timeout status census")
    require(tuple(row_key(row) for row in payload["rows"]) == expected,
            "ordered pilot cover")
    for row in payload["rows"]:
        require(row["status"] == "REMOTE_ERROR" and
                "FunctionTimeoutError" in row["error"] and
                "timeout of 300s" in row["error"], "remote timeout row")
        require("unit" not in row and "program_sha256" not in row,
                "no mathematical transcript")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_OUTSIDE_INCOMPLETE_PASS "
          "rows=24 timeouts=24 mathematical_rows=0")


if __name__ == "__main__":
    main()

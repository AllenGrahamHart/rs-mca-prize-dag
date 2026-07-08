#!/usr/bin/env python3
"""Integrity check for the banked A=[0,1,50] census JSON."""

from __future__ import annotations

import json
from pathlib import Path


RESULT_PATH = Path(
    "critical/nodes/u1_x4_direct_column_budget/notes/"
    "f3_h3_core_0150_census_results.json"
)


def main() -> None:
    data = json.loads(RESULT_PATH.read_text())
    if data["core"] != [0, 1, 50]:
        raise AssertionError(data["core"])
    if data["total_shapes"] != 129766:
        raise AssertionError(data["total_shapes"])
    if data["norm_exception_count"] != 1152:
        raise AssertionError(data["norm_exception_count"])
    if data["activation_exception_count"] != 0:
        raise AssertionError(data["activation_exception_count"])
    if data["activation_exceptions"] != []:
        raise AssertionError(data["activation_exceptions"])
    print("H3_CORE_0150_CENSUS_CHECK_PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the exact cells-3/6 quotient and committed manifest."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_split_cells3_6_quotient.py"
)
MANIFEST = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
)
SCRIPT_SHA256 = "0b9d3c7a785f07e3469f9305be81b3d9f7c3f572f3b969f81ba7281636b892fd"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "quotient compiler custody")
    require(hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == MANIFEST_SHA256,
            "manifest custody")
    spec = importlib.util.spec_from_file_location("cells3_6_quotient", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generated = module.representative_manifest()
    payload = json.loads(MANIFEST.read_text())
    require(payload["raw_cases"] == 5040, "raw census")
    require(payload["representative_count"] == 1416, "representative census")
    require(payload["s0_profile"] == {"2": 72, "4": 384}, "S0 profile")
    require(payload["repeated_profile"] == {"2": 240, "4": 720},
            "repeated profile")
    require(payload["pilot_stratum_count"] == 56 and
            payload["pilot_representative_count"] == 24, "pilot census")
    require(payload["representatives"] == [list(row) for row in generated["representatives"]],
            "ordered representatives")
    require(payload["pilot_representatives"] ==
            [list(row) for row in generated["pilot_representatives"]],
            "ordered pilot representatives")
    require(payload["representatives_sha256"] ==
            "39fb277a94d8ee3a24e3a8f9e1f0bb50014665ca7c151659d4dc8fcd912392d6",
            "representative hash")
    require(payload["pilot_representatives_sha256"] ==
            "a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96",
            "pilot hash")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_QUOTIENT_VERIFY_PASS "
          "raw=5040 reps=1416 pilot=24/56")


if __name__ == "__main__":
    main()

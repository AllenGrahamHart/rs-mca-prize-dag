#!/usr/bin/env python3
"""Verify the exact O0b FFI/FIF collapsed-common exclusions."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CHECK = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_check.py"
)
RESULT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_result.json"
)
FACTOR = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_collapsed_common_eliminant_factor.py"
)
CHECK_SHA256 = "ff9e43a54913a0d7d69b5ffdd4abf9bf06a3fd921a4361b144b98a804b089538"
RESULT_SHA256 = "38a44a30aa3421a67161acf5268d4bbfbe9e33903547e50259fc3f0da77efd03"
FACTOR_SHA256 = "8d0c74703d84ff3eebaf43e5c867fc23ed6ea387a05497f8acc7fafed2a570e1"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    require(hashlib.sha256(CHECK.read_bytes()).hexdigest() == CHECK_SHA256,
            "checker custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    require(hashlib.sha256(FACTOR.read_bytes()).hexdigest() == FACTOR_SHA256,
            "factor custody")
    checker = load("admissible_check", CHECK)
    factor = load("eliminant_factor", FACTOR)
    checked = checker.verify()
    degree, guarded = factor.verify_factorization()
    payload = json.loads(RESULT.read_text())
    row = payload["row"]
    require(checked == {"status": "COMPLETE", "unit": True} and
            degree == 14 and len(guarded) == 2 and
            row["stages"][4] == {
                "guard_index": 4, "dimension": 0, "basis_size": 22
            } and
            row["stages"][5] == {
                "guard_index": 5, "dimension": -1, "basis_size": 1
            }, "exclusion ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFI_FIF_COLLAPSED_COMMON_EXCLUSIONS_VERIFY_PASS "
          "charts=2 unit_guard=b+1")


if __name__ == "__main__":
    main()

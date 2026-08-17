#!/usr/bin/env python3
"""Verify the exact O0b IFF rational-branch exclusion."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CHECK = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_check.py"
)
CORE = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_program.py"
)
RESULT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_iff_rational_reduction_result.json"
)
CHECK_SHA256 = "e6b895464bb43663ba0428a949eacd57628d1329ffdd12eda6ccb6221d12de54"
CORE_SHA256 = "ce5ef23fee81c3065dbf66c35298abaa799198a4756ae1869a19b2382263d2ad"
RESULT_SHA256 = "5485816c745c18d1514200cc1bba057662c03319f7820883e7010ecb723b93c3"


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
    require(hashlib.sha256(CORE.read_bytes()).hexdigest() == CORE_SHA256,
            "core custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    checker = load("iff_check", CHECK)
    core = load("iff_core", CORE)
    checked = checker.verify()
    substitutions, records, numerator = core.verify_rational_reduction()
    row = json.loads(RESULT.read_text())["row"]
    require(checked == {"status": "COMPLETE", "unit": True} and
            len(substitutions) == 3 and len(records) == 4 and
            numerator != 0 and
            row["equation_stages"] == [
                {"equation": 7, "dimension": 0, "basis_size": 42},
                {"equation": 5, "dimension": 0, "basis_size": 44},
                {"equation": 6, "dimension": 0, "basis_size": 44},
            ] and
            row["route_stages"][5] == {
                "guard_index": 5, "dimension": -1, "basis_size": 1
            }, "IFF exclusion ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_IFF_RATIONAL_BRANCH_EXCLUSION_VERIFY_PASS "
          "branches=2 unit_guard=b+1")


if __name__ == "__main__":
    main()

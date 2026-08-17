#!/usr/bin/env python3
"""Verify the four global common bases and their custody."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CHECKER = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_cell3_global_common_basis_check.py"
)
RESULT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
)
RESULT_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"


def main():
    if hashlib.sha256(RESULT.read_bytes()).hexdigest() != RESULT_SHA256:
        raise RuntimeError("global-basis result custody")
    spec = importlib.util.spec_from_file_location("global_basis_check", CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.verify()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_GLOBAL_BASIS_VERIFY_PASS "
          f"rows={result['rows']} programs={result['programs']} bases={result['bases']}")


if __name__ == "__main__":
    main()

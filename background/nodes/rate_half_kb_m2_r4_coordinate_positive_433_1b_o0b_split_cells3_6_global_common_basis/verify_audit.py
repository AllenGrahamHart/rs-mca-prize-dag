#!/usr/bin/env python3
"""Run the hostile audit for the global common bases."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CHECKER = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_cell3_global_common_basis_check.py"
)


def main():
    spec = importlib.util.spec_from_file_location("global_basis_check", CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    mutations = module.hostile_audit()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_GLOBAL_BASIS_AUDIT_PASS "
          f"mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()

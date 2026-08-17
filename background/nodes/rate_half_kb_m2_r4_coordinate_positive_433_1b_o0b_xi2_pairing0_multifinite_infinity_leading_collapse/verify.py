#!/usr/bin/env python3
"""Verify the exact FFI/FIF infinity leading-coefficient collapse."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_multifinite_infinity_collapse.py"
)
SCRIPT_SHA256 = "ed7a70cee69571b946ceef6a2c60e1c9f50438d2fb4dab37d19094265fa102a0"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_script():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "collapse-script custody")
    spec = importlib.util.spec_from_file_location("infinity_collapse", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    module = load_script()
    records, pairs = module.verify_pair_ledger()
    collapses = module.verify_collapses()
    guards = module.verify_guards()
    require(len(records) == 7 and len(pairs) == 3 and
            set(collapses) == {"FFI", "FIF"} and guards == 4,
            "collapse census")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_MULTIFINITE_INFINITY_COLLAPSE_VERIFY_PASS "
          "masks=2 guards=4")


if __name__ == "__main__":
    main()

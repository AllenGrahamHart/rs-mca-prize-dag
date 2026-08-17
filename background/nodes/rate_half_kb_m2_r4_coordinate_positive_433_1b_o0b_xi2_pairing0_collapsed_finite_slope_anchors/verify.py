#!/usr/bin/env python3
"""Verify collapsed finite-slope anchors for O0b FFI/FIF."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_collapsed_finite_slope_anchors.py"
)
SCRIPT_SHA256 = "1059e49271b06104353ad61c2e3c766c56e253ae3480c0410fb6afa08802ac99"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_script():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "slope-anchor script custody")
    spec = importlib.util.spec_from_file_location("slope_anchors", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    module = load_script()
    expected = module.verify_generic_anchor()
    separations = module.verify_record_separations()
    masks = module.verify_scope()
    require(str(expected) == "(-anchor + y)*(lam*z1 + z0)" and
            set(separations) == {"q4", "q5", "q6"} and
            masks == {"FFI": ("q4", "q5"), "FIF": ("q4", "q6")},
            "anchor ledger")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_FINITE_SLOPE_ANCHORS_VERIFY_PASS "
          "masks=2 records=3")


if __name__ == "__main__":
    main()

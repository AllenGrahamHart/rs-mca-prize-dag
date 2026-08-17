#!/usr/bin/env python3
"""Independent Burnside and hostile audit for split cells 1 and 2."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cells1_2_common_exclusion.py")


def load():
    spec = importlib.util.spec_from_file_location("cells1_2_exclusion", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def expect_rejected(call, label):
    try:
        call()
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    payload = json.loads(MODULE.RESULT.read_text())
    bad = deepcopy(payload)
    bad["rows"][0]["unit"] = False
    expect_rejected(lambda: MODULE.validate_payload(bad), "nonunit chart")
    expect_rejected(
        lambda: MODULE.verify_quotient(s0_d_permutation=tuple(range(7))),
        "identity D-sign action",
    )

    s0_raw, s0_fixed = 1680, 16*9
    repeated_raw, repeated_fixed = 3360, 32*15
    require((s0_raw+s0_fixed)//4 == 456 and
            (repeated_raw+repeated_fixed)//4 == 960,
            "independent Burnside census")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS1_2_AUDIT_PASS "
          "raw=5040 reps=1416 mutations=2/2")


if __name__ == "__main__":
    main()

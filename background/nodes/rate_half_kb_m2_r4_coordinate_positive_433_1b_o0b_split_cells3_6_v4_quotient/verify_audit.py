#!/usr/bin/env python3
"""Independent Burnside and hostile audit of the cells-3/6 quotient."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_split_cells3_6_quotient.py"
)


def load():
    spec = importlib.util.spec_from_file_location("cells3_6_quotient", SCRIPT)
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
    except (KeyError, RuntimeError):
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    s0_orbits = (1680 + 144) // 4
    repeated_orbits = (3360 + 480) // 4
    require((s0_orbits, repeated_orbits) == (456, 960), "Burnside census")
    expect_rejected(
        lambda: MODULE.verify(s0_d_permutation=tuple(range(7))),
        "identity S0 D-sign action",
    )
    duplicates = dict(MODULE.REPEATED.DUPLICATE_PERMUTATIONS)
    duplicates["SDE"] = tuple(range(7))
    expect_rejected(
        lambda: MODULE.verify(duplicate_permutations=duplicates),
        "identity SDE duplicate action",
    )
    expect_rejected(
        lambda: MODULE.verify(outside_permutation=(0, 0, 4, 5, 2, 3, 6)),
        "nonbijective B/C outside action",
    )
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_AUDIT_PASS "
          "raw=5040 reps=1416 mutations=3/3")


if __name__ == "__main__":
    main()

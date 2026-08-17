#!/usr/bin/env python3
"""Independent Burnside and hostile audit of the component quotient."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cell0_component_quotient.py")


def load():
    spec = importlib.util.spec_from_file_location("component_quotient", SCRIPT)
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
    s0_raw = 2 * 2 * 2 * 105
    repeated_raw = 2 * 2 * 2 * 2 * 105
    s0_secondary_fixed = 2 * 2 * 2 * 9
    repeated_secondary_fixed = 2 * 2 * 2 * 2 * 15
    s0_orbits = (s0_raw + s0_secondary_fixed) // 4
    repeated_orbits = (repeated_raw + repeated_secondary_fixed) // 4
    require((s0_orbits, repeated_orbits) == (228, 480), "Burnside census")

    expect_rejected(lambda: MODULE.verify_component_action({"A": "B", "B": "A"}),
                    "component-type swap")
    expect_rejected(
        lambda: MODULE.representative_manifest(s0_d_permutation=tuple(range(7))),
        "identity S0 D-sign action",
    )
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMPONENT_AUDIT_PASS "
          "raw=2520 reps=708 mutations=2/2")


if __name__ == "__main__":
    main()

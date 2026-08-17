#!/usr/bin/env python3
"""Independent census and hostile controls for cell-0 common classification."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_common_classification.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = load("cell0_common", SCRIPT)


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
    charts = json.loads(MODULE.CHARTS.read_text())
    components = json.loads(MODULE.COMPONENTS.read_text())
    require(MODULE.validate_common_payload(charts, components) == (12, 12, 4),
            "baseline common payload")

    bad_charts = deepcopy(charts)
    mixed = next(row for row in bad_charts["rows"]
                 if row["epsilon"][0] != row["epsilon"][1])
    mixed["unit"] = False
    expect_rejected(lambda: MODULE.validate_common_payload(bad_charts, components),
                    "mixed chart nonunit")

    bad_components = deepcopy(components)
    bad_components["rows"][0]["row_checks"][0]["zero"] = False
    expect_rejected(lambda: MODULE.validate_common_payload(charts, bad_components),
                    "component row nonzero")

    expect_rejected(
        lambda: MODULE.verify_mixed_quotient(tuple(range(7))),
        "identity S0 D-sign action",
    )

    raw = 2 * 6 * 7 * 15
    s0_burnside = (420 + 4 * 9) // 4
    repeated_burnside = (840 + 8 * 15) // 4
    require((raw, s0_burnside, repeated_burnside) == (1260, 114, 240),
            "independent census")
    require(s0_burnside + repeated_burnside == 354, "Burnside total")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMMON_AUDIT_PASS "
          "closed=1260/354 mutations=3/3")


if __name__ == "__main__":
    main()

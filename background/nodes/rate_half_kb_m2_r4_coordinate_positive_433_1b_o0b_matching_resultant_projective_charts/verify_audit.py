#!/usr/bin/env python3
"""Hostile audit for the O0b projective-chart split."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
VERIFY = NODE / "verify.py"


def expect_rejected(call, label):
    try:
        call()
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    spec = importlib.util.spec_from_file_location("node_verify", VERIFY)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    module = verifier.load_script()
    expect_rejected(lambda: module.verify_resultant_identity(sign=1),
                    "wrong resultant sign")
    expect_rejected(lambda: module.verify_chart_cover(module.chart_masks()[:-1]),
                    "missing chart")
    symbols, _, _, formula = module.symbols_and_resultant()
    p2 = symbols[2]
    expect_rejected(
        lambda: module.require(
            module.sp.expand(formula.subs({p2: 0})) == 0,
            "one-sided infinity chart",
        ),
        "one-sided infinity chart",
    )
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_RESULTANT_PROJECTIVE_CHARTS_AUDIT_PASS "
          "mutations=3/3")


if __name__ == "__main__":
    main()

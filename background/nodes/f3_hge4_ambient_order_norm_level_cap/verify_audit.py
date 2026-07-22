#!/usr/bin/env python3
"""Mutation audit for the HGE4 ambient-order norm level cap."""

from __future__ import annotations

import importlib.util
from decimal import Decimal, getcontext
from pathlib import Path


VERIFY = Path(__file__).with_name("verify.py")
SPEC = importlib.util.spec_from_file_location("ambient_cap_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> None:
    correct = MODULE.ambient_cap(41, 40)
    order = 1 << 40

    # Mutation 1: weakening the ambient exponent s to the level exponent a
    # loses every proper-level gain and returns only the old quarter cap.
    weakened = min(
        order // 4 - 1,
        2 * MODULE.ceil_div(order * 40, 8 * 40) - 1,
    )
    assert correct == 268_173_567_751
    assert weakened == order // 4 - 1
    assert weakened > correct

    # Mutation 2: floor is one unit too aggressive whenever the ratio is not
    # integral, and is not licensed by r < ma/(8s).
    floor_mutation = 2 * ((order * 40) // (8 * 41)) - 1
    assert (order * 40) % (8 * 41)
    assert floor_mutation == correct - 2

    # Mutation 3: dropping the final -1 fails the exact top-level regression.
    top_order = 1 << 41
    missing_strictness = 2 * MODULE.ceil_div(top_order * 41, 8 * 41)
    assert missing_strictness == top_order // 4
    assert MODULE.ambient_cap(41, 41) == top_order // 4 - 1

    # Mutation 4: the tempting exponent 3/2 is too large. Its claimed local
    # contraction already fails at x=1/100.
    getcontext().prec = 60
    x_value = Decimal(1) / 100
    assert (Decimal(1) - x_value).ln() > -(Decimal(3) / 2) * x_value * Decimal(2).ln()

    # The proved parity gate has the pinned odd one-factor loss.
    first_live = MODULE.first_sharp_live_defect(41, 40)
    assert first_live == 6_948_379_851
    assert not MODULE.sharp_deleted(41, 40, first_live)
    assert MODULE.sharp_deleted(41, 40, first_live - 1)

    print(
        "F3_HGE4_AMBIENT_ORDER_NORM_LEVEL_CAP_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()

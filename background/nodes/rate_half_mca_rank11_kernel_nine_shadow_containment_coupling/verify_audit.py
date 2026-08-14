#!/usr/bin/env python3
"""Independent algebra audit for full nine-shadow containment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    require(comb(p["component_subset_size"], p["shadow_subset_size"]) == 55, "55 shadows")
    require(comb(3, 2) == p["rank9_spanning_shadow_minimum"], "three spanning")
    checked = 0
    for kprime in (12, 4599, 11773, 15446, 15670, 15671):
        mprime = kprime + 67472
        e_large = comb(mprime - 9, 2)
        e_small = comb(kprime - 10, 2)
        require(e_large > e_small, f"sign {kprime}")

        # Reconstruct the coefficient by eliminating J_1 from
        # 55 I <= E_0 B-(E_0-E_1)J_1 and 3 I_1 <= E_1 J_1.
        eliminated = 55 + Fraction(3 * (e_large - e_small), e_small)
        printed = 52 + Fraction(3 * e_large, e_small)
        require(eliminated == printed, f"elimination {kprime}")
        checked += 1
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_COUPLING_AUDIT_PASS "
        f"rows={checked} coefficient_base=52 lower_coefficient=55"
    )


if __name__ == "__main__":
    main()

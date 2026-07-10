#!/usr/bin/env python3
"""Replay exact arithmetic for the official rich-coset K=6 theorem."""

from __future__ import annotations

from fractions import Fraction

from f3_h2_hbk_conditional_compiler import energy_constant, h_floor_threshold


K = Fraction(6, 1)


def main() -> None:
    linear_supply = Fraction(35, 36) * Fraction(5, 6) ** 2
    linear_demand = Fraction(2, 5) * Fraction(7, 5)
    if linear_supply != Fraction(875, 1296):
        raise AssertionError(linear_supply)
    if linear_demand != Fraction(14, 25):
        raise AssertionError(linear_demand)
    if linear_supply <= linear_demand:
        raise AssertionError((linear_supply, linear_demand))

    degree_constant = Fraction(360, 67) + Fraction(180, 67 * 36)
    if degree_constant >= K:
        raise AssertionError(degree_constant)

    h2_energy = energy_constant(K)
    if h2_energy != 211:
        raise AssertionError(h2_energy)
    threshold = h_floor_threshold(K)
    if threshold != Fraction(44_521, 64) or threshold >= 1 << 13:
        raise AssertionError(threshold)

    print(f"F3_OFFICIAL_RICH_COSET_K6_PASS K={K} h2_energy={h2_energy}")


if __name__ == "__main__":
    main()


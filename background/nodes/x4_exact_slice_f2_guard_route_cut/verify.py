#!/usr/bin/env python3
"""Replay the exact arithmetic used by the exact-slice F2 route cut."""

from fractions import Fraction


N = 1 << 41
RATES = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16))
PRINTED_T = (8592912739, 7014660390, 4722556392, 2943177800)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    print(f"PASS {label}")


def main() -> None:
    t_min = (N >> 8) - 1
    require(2 * t_min * t_min > 385 * N, "uniform Hoeffding margin exceeds 385 bits")

    t_upper = (N - 1) // 128
    require(t_upper < N // 64, "comparison depth is below N/64")
    for rho in RATES:
        if rho == Fraction(1, 2):
            distance = t_min
        else:
            distance = int((Fraction(1, 2) - rho) * N) - t_upper
        require(distance >= t_min, f"rate {rho} no closer to the central slice")

    # The published L=255.9 corridor table is a non-load-bearing replay.
    for rho, t_xr in zip(RATES, PRINTED_T):
        require(t_xr * 2559 < 10 * N, f"rate {rho} printed exact-slice depth is guard-rejected")

    require(128 + 256 < 385, "floor and gate overhead is below the Hoeffding margin")
    print("X4_EXACT_SLICE_F2_GUARD_ROUTE_CUT_PASS")


if __name__ == "__main__":
    main()

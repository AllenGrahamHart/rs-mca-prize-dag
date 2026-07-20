#!/usr/bin/env python3
"""Verify background-surplus Plotkin distance and effective excess."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path


RATES = (2, 4, 8, 16)
F23_PATH = (
    Path(__file__).resolve().parents[1]
    / "l1_cross_quotient_split_descent_obstruction"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_background_surplus_f23", F23_PATH)
assert SPEC is not None and SPEC.loader is not None
F23 = module_from_spec(SPEC)
SPEC.loader.exec_module(F23)


def surplus_boundary_code() -> tuple[int, int, int]:
    universe = tuple(range(8))
    family = [frozenset((2 * i, 2 * i + 1)) for i in range(4)]
    ell = 1
    surplus = 1
    effective = len(universe) - 4 * (ell + surplus)
    assert effective == 0
    assert all(
        len(left ^ right) >= 2 * (ell + surplus)
        for left, right in combinations(family, 2)
    )
    assert len(family) <= 2 * len(universe)
    return len(family), surplus, effective


def f23_control() -> tuple[int, int, int]:
    F23.check_pair(F23.D0, F23.F0, F23.W0)
    F23.check_pair(F23.D1, F23.F1, F23.W1)
    d = len(F23.D0)
    h = len(F23.SUPPORT)
    minimum = F23.ELL - (h - d)
    exact = len(F23.BACKGROUND)
    surplus = exact - minimum
    universe = len(F23.CORE) + len(F23.BACKGROUND)
    effective = universe - 4 * (F23.ELL + surplus)
    assert (minimum, surplus, effective) == (1, 0, 1)
    return minimum, surplus, effective


def arithmetic_audit() -> tuple[int, int]:
    checked = 0
    bounded = 0
    for rate in RATES:
        for k in range(2, 81):
            total = (rate - 1) * k + 1
            for ell in range(1, total + 1):
                petals, background = divmod(total, ell)
                if petals == 0:
                    continue
                gap = ell - background
                plotkin = (k - 1) + background - 4 * ell
                for surplus in sorted({0, background // 2, background}):
                    effective = plotkin - 4 * surplus
                    numerator = (
                        (petals - 3 * (rate - 1) + 1) * ell
                        - rate * (gap + 1)
                        - 4 * (rate - 1) * surplus
                    )
                    assert (rate - 1) * effective == numerator
                    checked += 1
                    if effective <= 3:
                        bounded += 1
    return checked, bounded


def logarithmic_cap_audit() -> int:
    checked = 0
    for log_n in range(1, 13):
        n = 1 << log_n
        for cap in range(5):
            for effective in range(cap * log_n + 1):
                assert (1 << (effective + 1)) * n <= 2 * n ** (cap + 1)
                checked += 1
    return checked


def main() -> None:
    family, surplus, effective = surplus_boundary_code()
    minimum, f23_surplus, f23_effective = f23_control()
    checked, bounded = arithmetic_audit()
    logarithmic = logarithmic_cap_audit()
    assert checked > 0 and bounded > 0 and logarithmic > 0
    print(
        "L1_BACKGROUND_SURPLUS_PLOTKIN_PASS "
        f"family={family} z={surplus} E_z={effective} "
        f"f23=u{minimum}:z{f23_surplus}:E{f23_effective} "
        f"checked={checked} bounded={bounded} logarithmic={logarithmic}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify bounded Plotkin-excess puncturing and official slack arithmetic."""

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
SPEC = spec_from_file_location("l1_plotkin_excess_f23", F23_PATH)
assert SPEC is not None and SPEC.loader is not None
F23 = module_from_spec(SPEC)
SPEC.loader.exec_module(F23)


def excess_one_code() -> tuple[int, int, tuple[int, int]]:
    universe = tuple(range(5))
    family = [frozenset(pair) for pair in combinations(universe, 2)]
    ell = 1
    excess = len(universe) - 4 * ell
    assert excess == 1
    assert all(
        len(left ^ right) >= 2 * ell
        for left, right in combinations(family, 2)
    )

    class_sizes = []
    for bit in (0, 1):
        cell = [member for member in family if int(0 in member) == bit]
        punctured = [frozenset(x for x in member if x != 0) for member in cell]
        assert all(
            len(left ^ right) >= 2 * ell
            for left, right in combinations(punctured, 2)
        )
        assert len(cell) <= 2 * 4 * ell
        class_sizes.append(len(cell))
    bound = 2 ** (excess + 1) * 4 * ell
    assert len(family) == 10 <= bound == 16
    return len(family), bound, tuple(class_sizes)


def f23_excess_one() -> tuple[int, int, int]:
    F23.check_pair(F23.D0, F23.F0, F23.W0)
    F23.check_pair(F23.D1, F23.F1, F23.W1)
    universe = len(F23.CORE) + len(F23.BACKGROUND)
    excess = universe - 4 * F23.ELL
    bound = 2 ** (excess + 1) * (universe - excess)
    assert (universe, excess, bound) == (9, 1, 32)
    return universe, excess, bound


def official_identity() -> tuple[int, int]:
    checked = 0
    bounded = 0
    for rate in RATES:
        for k in range(2, 201):
            total = (rate - 1) * k + 1
            for ell in range(1, total + 1):
                petals, background = divmod(total, ell)
                if petals == 0:
                    continue
                gap = ell - background
                excess = (k - 1) + background - 4 * ell
                numerator = (
                    (petals - 3 * (rate - 1) + 1) * ell
                    - rate * (gap + 1)
                )
                assert (rate - 1) * excess == numerator
                checked += 1
                if 0 <= excess <= 4:
                    bounded += 1
    return checked, bounded


def main() -> None:
    family, bound, classes = excess_one_code()
    universe, excess, f23_bound = f23_excess_one()
    checked, bounded = official_identity()
    assert checked > 0 and bounded > 0
    print(
        "L1_BOUNDED_PLOTKIN_EXCESS_PASS "
        f"family={family}/{bound} classes={classes} "
        f"f23=V{universe}:E{excess}/{f23_bound} "
        f"official={checked} bounded={bounded}"
    )


if __name__ == "__main__":
    main()

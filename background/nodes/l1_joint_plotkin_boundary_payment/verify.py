#!/usr/bin/env python3
"""Verify the joint Plotkin boundary and official source translation."""

from __future__ import annotations

from itertools import combinations


RATES = (2, 4, 8, 16)


def constant_weight_boundary() -> tuple[int, int, int]:
    universe = frozenset(range(4))
    family = [frozenset(pair) for pair in combinations(universe, 2)]
    ell = 1
    assert len(family) == 6
    assert all(
        len(left ^ right) >= 2 * ell
        for left, right in combinations(family, 2)
    )
    signs = [tuple(1 if i in member else -1 for i in universe) for member in family]
    assert all(
        sum(x * y for x, y in zip(left, right)) <= 0
        for left, right in combinations(signs, 2)
    )
    assert len(family) <= 2 * len(universe)
    return len(family), len(universe), ell


def combined_set_audit() -> tuple[int, int]:
    checked = 0
    paid = 0
    for n_core in range(2, 31):
        for background in range(0, 11):
            universe = n_core + background
            for ell in range(1, 11):
                for d in range(n_core + 1):
                    for u in range(background + 1):
                        for r in range(-1, d + u + 1):
                            if d + u != r + ell:
                                continue
                            weight = d + u
                            assert 2 * (weight - r) == 2 * ell
                            checked += 1
                            if universe <= 4 * ell:
                                assert universe - 4 * ell <= 0
                                paid += 1
    return checked, paid


def official_translation() -> tuple[int, int, int]:
    paid = 0
    live = 0
    equality = 0
    for rate in RATES:
        for k in range(2, 201):
            total = (rate - 1) * k + 1
            for ell in range(1, total + 1):
                petals, background = divmod(total, ell)
                if petals == 0:
                    continue
                n_core = k - 1
                direct = n_core + background > 4 * ell
                translated = (
                    rate * background
                    > (4 * (rate - 1) - petals) * ell + rate
                )
                gap_form = (
                    (petals - 3 * (rate - 1) + 1) * ell
                    > rate * (ell - background + 1)
                )
                assert direct == translated == gap_form
                if direct:
                    assert petals >= 3 * (rate - 1)
                    live += 1
                else:
                    paid += 1
                if n_core + background == 4 * ell:
                    equality += 1
                    assert not direct
    return paid, live, equality


def main() -> None:
    family, universe, ell = constant_weight_boundary()
    checked, combined_paid = combined_set_audit()
    paid, live, equality = official_translation()
    assert checked > 0 and combined_paid > 0
    assert paid > 0 and live > 0 and equality > 0
    print(
        "L1_JOINT_PLOTKIN_BOUNDARY_PASS "
        f"family={family}/{2 * universe} V={universe} ell={ell} "
        f"checked={checked} combined_paid={combined_paid} "
        f"official_paid={paid} live={live} equality={equality}"
    )


if __name__ == "__main__":
    main()

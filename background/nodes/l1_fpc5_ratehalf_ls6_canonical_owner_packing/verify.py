#!/usr/bin/env python3
"""Exact regression checks for the LS6 canonical-owner theorem."""

from __future__ import annotations

from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHART = (
    ROOT
    / "background/nodes/l1_fpc5_ratehalf_ls6_determinant_coordinate_chart/verify.py"
)
SPEC = spec_from_file_location("ls6_chart_verify", CHART)
assert SPEC is not None and SPEC.loader is not None
poly = module_from_spec(SPEC)
SPEC.loader.exec_module(poly)


def exact_quotient(numerator: list[int], denominator: list[int]) -> list[int]:
    quotient, remainder = poly.divmod_poly(numerator, denominator)
    assert remainder == [0]
    return quotient


def locator(points: range) -> list[int]:
    value = [1]
    for point in points:
        value = poly.mul(value, [(-point) % poly.MOD, 1])
    return value


def main() -> None:
    # This exact chart has D_H=D_0-H and Q_H=1. Exhausting all linear H
    # supplies many fully split points while keeping the replay tiny.
    ell, a = 3, 1
    j, h, s = 2 * ell - a, ell - 2 * a, ell - a
    d0 = locator(range(j))
    q0 = [1]
    multiplier = [7, 1]
    v0 = [1]
    modulus = poly.sub(poly.mul(d0, multiplier), v0)
    q0_inverse = [1]
    base_roots = frozenset(poly.roots(d0))
    assert len(base_roots) == j

    owners: dict[tuple[int, ...], list[tuple[frozenset[int], list[int]]]]
    owners = defaultdict(list)
    split_points = 0
    algebra_checks = 0

    for coefficients in product(range(poly.MOD), repeat=h + 1):
        coordinate = poly.trim(list(coefficients))
        dh, qh, vh = poly.chart_inverse(
            coordinate, modulus, d0, q0, v0, q0_inverse
        )
        assert qh == [1]
        assert poly.degree(vh) <= s
        assert poly.mul(dh, multiplier) == poly.add(poly.mul(modulus, qh), vh)
        if coordinate == [0]:
            assert dh == d0
            continue

        roots_h = frozenset(poly.roots(dh))
        if len(roots_h) != j:
            continue
        split_points += 1

        owner = poly.gcd_poly(d0, coordinate)
        assert owner == poly.gcd_poly(d0, dh)
        g = poly.degree(owner)
        assert 0 <= g <= h
        aa = exact_quotient(d0, owner)
        bb = exact_quotient(dh, owner)
        kk = exact_quotient(coordinate, owner)
        assert poly.gcd_poly(owner, aa) == [1]
        assert poly.gcd_poly(owner, bb) == [1]
        assert poly.gcd_poly(aa, bb) == [1]
        assert poly.degree(aa) == poly.degree(bb) == j - g
        assert poly.degree(kk) <= h - g
        assert kk == poly.sub(poly.mul(aa, qh), poly.mul(bb, q0))
        assert poly.gcd_poly(kk, aa) == [1]
        assert poly.gcd_poly(kk, bb) == [1]
        assert poly.gcd_poly(owner, qh) == [1]
        assert roots_h - base_roots == frozenset(poly.roots(bb))
        owners[tuple(owner)].append((roots_h - base_roots, dh))
        algebra_checks += 1

    assert split_points >= 100
    assert len(owners) >= 2

    pair_checks = 0
    packing_checks = 0
    universe_size = poly.MOD - j
    for owner_key, family in owners.items():
        owner = list(owner_key)
        g = poly.degree(owner)
        width = j - g
        choose_size = h - g + 1
        bound = comb(universe_size, choose_size) // comb(width, choose_size)
        assert len(family) <= bound
        packing_checks += 1
        for left_index, (left_roots, left_locator) in enumerate(family):
            for right_roots, right_locator in family[left_index + 1 :]:
                assert len(left_roots & right_roots) <= h - g
                cross = poly.sub(left_locator, right_locator)
                reduced = exact_quotient(cross, owner)
                assert poly.degree(reduced) <= h - g
                pair_checks += 1

    arithmetic_checks = 0
    for ell_value in range(4, 40):
        for a_value in range(1, max(2, ell_value // 3)):
            h_value = ell_value - 2 * a_value
            if h_value < 0:
                continue
            for b_value in range(0, ell_value):
                v = 2 * ell_value + a_value + b_value - 2
                for c_value in range(0, h_value + 1):
                    width = ell_value + a_value + c_value
                    size = c_value + 1
                    if size > width or size > v:
                        continue
                    numerator = comb(v, size)
                    denominator = comb(width, size)
                    assert numerator < (3**size) * denominator
                    arithmetic_checks += 1

    print(
        "PASS: LS6 canonical-owner packing "
        f"split_points={split_points} owners={len(owners)} "
        f"algebra_checks={algebra_checks} pair_checks={pair_checks} "
        f"packing_checks={packing_checks} arithmetic_checks={arithmetic_checks}"
    )


if __name__ == "__main__":
    main()

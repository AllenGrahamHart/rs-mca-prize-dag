#!/usr/bin/env python3
"""Verify the PMA source quotient code and aligned gcd-excess certificate."""

from __future__ import annotations

from itertools import product
from pathlib import Path
from random import Random
import importlib.util


NODE = "pma_ratehalf_source_aligned_gcd_excess"
ROOT = Path(__file__).resolve().parents[3]
BASE = (
    ROOT
    / "background"
    / "nodes"
    / "pma_ratehalf_core_triple_excess_reduction"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("pma_core_triple_base", BASE)
assert SPEC is not None and SPEC.loader is not None
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


def monic(poly: list[int], p: int) -> list[int]:
    poly = base.trim(poly[:])
    if poly == [0]:
        return poly
    return base.scale(poly, pow(poly[-1], -1, p), p)


def divmod_poly(
    numerator: list[int], denominator: list[int], p: int
) -> tuple[list[int], list[int]]:
    numerator = base.trim(numerator[:])
    denominator = base.trim(denominator[:])
    assert denominator != [0]
    if base.degree(numerator) < base.degree(denominator):
        return [0], numerator
    quotient = [0] * (base.degree(numerator) - base.degree(denominator) + 1)
    inverse = pow(denominator[-1], -1, p)
    while numerator != [0] and base.degree(numerator) >= base.degree(denominator):
        shift = base.degree(numerator) - base.degree(denominator)
        coefficient = numerator[-1] * inverse % p
        quotient[shift] = coefficient
        term = [0] * shift + base.scale(denominator, coefficient, p)
        numerator = base.sub(numerator, term, p)
    return base.trim(quotient), base.trim(numerator)


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    left = base.trim(left[:])
    right = base.trim(right[:])
    while right != [0]:
        _, remainder = divmod_poly(left, right, p)
        left, right = right, remainder
    return monic(left, p)


def gcd_many(polys: list[list[int]], p: int) -> list[int]:
    out = polys[0]
    for poly in polys[1:]:
        out = gcd_poly(out, poly, p)
    return out


def matrix_rank(rows: list[list[int]], p: int) -> int:
    work = [[value % p for value in row] for row in rows]
    rank = 0
    width = len(work[0]) if work else 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for index in range(len(work)):
            if index == rank or not work[index][column]:
                continue
            factor = work[index][column]
            work[index] = [
                (x - factor * y) % p
                for x, y in zip(work[index], work[rank])
            ]
        rank += 1
    return rank


def source_quotient_code() -> tuple[dict[str, object], dict[int, list[int]]]:
    p = 17
    ell, b = 2, 1
    core = list(range(7))
    petals = ((7, 8), (9, 10), (11, 12))
    petal_points = [x for petal in petals for x in petal]
    l_core = base.locator(core, p)
    l_petals = [base.locator(petal, p) for petal in petals]
    l = [1]
    for petal_locator in l_petals:
        l = base.mul(l, petal_locator, p)

    images: set[tuple[int, ...]] = set()
    min_weight = len(core)
    sign_mutation = False
    constant_mutation = False
    basis_words: list[list[int]] = []
    selected: dict[int, list[int]] = {}
    for labels in product(range(p), repeat=3):
        values = [
            labels[index]
            for index, petal in enumerate(petals)
            for _ in petal
        ]
        e_c = base.interpolate(petal_points, values, p)
        assert base.degree(e_c) < 3 * ell
        for index, petal_locator in enumerate(l_petals):
            _, remainder = divmod_poly(
                base.sub(e_c, [labels[index]], p), petal_locator, p
            )
            assert remainder == [0]

        quotient, p_star = divmod_poly(base.mul(l_core, e_c, p), l, p)
        assert base.degree(p_star) < 3 * ell
        assert base.add(p_star, base.mul(l, quotient, p), p) == base.mul(
            l_core, e_c, p
        )
        word = []
        for x in core:
            expected = (
                -base.evaluate(p_star, x, p)
                * pow(base.evaluate(l, x, p), -1, p)
            ) % p
            assert base.evaluate(quotient, x, p) == expected
            word.append(expected)
            wrong_sign = (
                base.evaluate(p_star, x, p)
                * pow(base.evaluate(l, x, p), -1, p)
            ) % p
            sign_mutation |= wrong_sign != expected

        images.add(tuple(word))
        if labels != (0, 0, 0):
            weight = sum(value != 0 for value in word)
            min_weight = min(min_weight, weight)
            assert weight >= ell + b - 1
        if labels in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            basis_words.append(word)
        if labels == (1, 2, 3):
            selected = {
                "p": p,
                "ell": ell,
                "b": b,
                "core": core,
                "l_core": l_core,
                "l": l,
                "p_star": p_star,
                "y": word,
            }

        # A nonconstant residue on one petal is outside the three-label source.
        if labels == (0, 0, 0):
            mutated_values = [0, 1, 0, 0, 0, 0]
            mutated_e = base.interpolate(petal_points, mutated_values, p)
            _, rem = divmod_poly(mutated_e, l_petals[0], p)
            constant_mutation = rem != [0]

    assert len(images) == p**3
    assert matrix_rank(basis_words, p) == 3
    fourth_coordinate_mutation = any(
        matrix_rank(
            basis_words
            + [[int(index == coordinate) for index in range(len(core))]],
            p,
        )
        == 4
        for coordinate in range(len(core))
    )
    assert selected
    return (
        {
            "words": len(images),
            "min_weight": min_weight,
            "sign_mutation": sign_mutation,
            "constant_mutation": constant_mutation,
            "fourth_coordinate_mutation": fourth_coordinate_mutation,
        },
        selected,
    )


def aligned_gcd_checks(fixture: dict[int, list[int]]) -> dict[str, object]:
    p = int(fixture["p"])
    core = list(fixture["core"])
    l_core = list(fixture["l_core"])
    l = list(fixture["l"])
    p_star = list(fixture["p_star"])
    y = list(fixture["y"])
    k0 = int(fixture["ell"]) + int(fixture["b"]) - 1
    rng = Random(0xA11C0DE)
    cases = 0
    positive_tau = False
    ambient_overcount = False
    dropped_p1_overcount = False
    for _ in range(2_000):
        polys = []
        while len(polys) < 3:
            candidate = [rng.randrange(p) for _ in range(k0)]
            candidate = base.trim(candidate)
            if candidate not in polys:
                polys.append(candidate)
        h1, h2, h3 = polys
        p1 = base.add(p_star, base.mul(l, h1, p), p)
        p2 = base.add(p_star, base.mul(l, h2, p), p)
        p3 = base.add(p_star, base.mul(l, h3, p), p)
        a_poly = base.sub(h1, h2, p)
        b_poly = base.sub(h1, h3, p)
        ba_poly = base.sub(b_poly, a_poly, p)

        sets = [
            {x for x in core if base.evaluate(poly, x, p) == 0}
            for poly in (p1, p2, p3)
        ]
        agreements = [
            sum(base.evaluate(poly, x, p) == y[index] for index, x in enumerate(core))
            for poly in (h1, h2, h3)
        ]
        assert agreements == [len(row) for row in sets]

        u12 = base.degree(gcd_many([l_core, a_poly, p1], p))
        u13 = base.degree(gcd_many([l_core, b_poly, p1], p))
        u23 = base.degree(gcd_many([l_core, ba_poly, p2], p))
        tau = base.degree(gcd_many([l_core, a_poly, b_poly, p1], p))
        assert u12 == len(sets[0] & sets[1])
        assert u13 == len(sets[0] & sets[2])
        assert u23 == len(sets[1] & sets[2])
        assert tau == len(sets[0] & sets[1] & sets[2])
        aligned_bonus = u12 + u13 + u23 - tau
        minimum = min(len(row) for row in sets)
        assert aligned_bonus >= 3 * minimum - len(core)
        positive_tau |= tau > 0

        equality_sets = (
            {x for x in core if base.evaluate(a_poly, x, p) == 0},
            {x for x in core if base.evaluate(b_poly, x, p) == 0},
            {x for x in core if base.evaluate(ba_poly, x, p) == 0},
        )
        equality_common = equality_sets[0] & equality_sets[1]
        equality_bonus = 2 * len(equality_common) + sum(
            len(row - equality_common) for row in equality_sets
        )
        ambient_overcount |= equality_bonus > aligned_bonus
        dropped_p1 = base.degree(gcd_many([l_core, a_poly], p))
        dropped_p1_overcount |= dropped_p1 > u12
        cases += 1

    assert positive_tau and ambient_overcount and dropped_p1_overcount
    return {
        "cases": cases,
        "positive_tau": positive_tau,
        "ambient_overcount": ambient_overcount,
        "dropped_p1_overcount": dropped_p1_overcount,
    }


def tail_boundary() -> dict[str, int]:
    ell, b, a = 11, 7, 1
    n_core = 4 * ell + b - 2
    k0 = ell + b - 1
    m = 2 * ell + b + a - 2
    j_value = m * m - n_core * (k0 - 1)
    threshold = 3 * m - n_core
    assert (n_core, k0, m, j_value, threshold) == (49, 17, 28, 0, 35)
    return {"j": j_value, "threshold": threshold}


def main() -> None:
    source, fixture = source_quotient_code()
    aligned = aligned_gcd_checks(fixture)
    boundary = tail_boundary()
    mutations = sum(
        bool(value)
        for value in (
            source["sign_mutation"],
            source["constant_mutation"],
            source["fourth_coordinate_mutation"],
            aligned["positive_tau"],
            aligned["ambient_overcount"],
            aligned["dropped_p1_overcount"],
            boundary["j"] <= 0,
        )
    )
    assert mutations == 7
    print(
        f"{NODE}_PASS source_words={source['words']} "
        f"source_min_weight={source['min_weight']} "
        f"aligned_cases={aligned['cases']} tail_j={boundary['j']} "
        f"tail_threshold={boundary['threshold']} mutations={mutations}"
    )


if __name__ == "__main__":
    main()

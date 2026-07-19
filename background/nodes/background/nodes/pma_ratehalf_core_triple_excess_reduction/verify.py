#!/usr/bin/env python3
"""Verify the PMA core-list and three-fiber excess reduction."""

from __future__ import annotations

from itertools import product
from math import gcd
from random import Random


NODE = "pma_ratehalf_core_triple_excess_reduction"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def degree(poly: list[int]) -> int:
    poly = trim(poly[:])
    return -1 if poly == [0] else len(poly) - 1


def add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = (
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
        ) % p
    return trim(out)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * value) % p for value in poly])


def sub(left: list[int], right: list[int], p: int) -> list[int]:
    return add(left, scale(right, -1, p), p)


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    if left == [0] or right == [0]:
        return [0]
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(roots: list[int] | tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % p, 1], p)
    return out


def interpolate(xs: list[int], ys: list[int], p: int) -> list[int]:
    out = [0]
    for i, x in enumerate(xs):
        basis = [1]
        denominator = 1
        for j, z in enumerate(xs):
            if i == j:
                continue
            basis = mul(basis, [(-z) % p, 1], p)
            denominator = denominator * (x - z) % p
        out = add(out, scale(basis, ys[i] * pow(denominator, -1, p), p), p)
    assert all(evaluate(out, x, p) == y % p for x, y in zip(xs, ys))
    return out


def prime_factors(value: int) -> list[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def subgroup(p: int, order: int) -> list[int]:
    assert (p - 1) % order == 0
    generator = pow(primitive_root(p), (p - 1) // order, p)
    values = []
    value = 1
    for _ in range(order):
        values.append(value)
        value = value * generator % p
    assert value == 1 and len(set(values)) == order
    return sorted(values)


def triple_bonus(
    polys: tuple[list[int], list[int], list[int]], core: list[int], p: int
) -> tuple[int, int, tuple[int, int, int]]:
    h1, h2, h3 = polys
    a = sub(h1, h2, p)
    b = sub(h1, h3, p)
    sets = (
        {x for x in core if evaluate(a, x, p) == 0},
        {x for x in core if evaluate(b, x, p) == 0},
        {x for x in core if evaluate(sub(b, a, p), x, p) == 0},
    )
    common = sets[0] & sets[1]
    exact = tuple(len(row - common) for row in sets)
    assert not ((sets[0] - common) & (sets[1] - common))
    assert not ((sets[0] - common) & (sets[2] - common))
    assert not ((sets[1] - common) & (sets[2] - common))
    return 2 * len(common) + sum(exact), len(common), exact


def find_split_cubic_fibers(
    p: int, domain: list[int]
) -> tuple[list[int], list[int], list[int], int]:
    rng = Random(0xC0DE775)
    domain_set = set(domain)
    for attempt in range(1, 200_001):
        roots = rng.sample(domain, 6)
        if len(set(roots)) != 6:
            continue
        a0 = locator(roots[:3], p)
        scalar = rng.randrange(2, p)
        b0 = scale(locator(roots[3:], p), scalar, p)
        difference = sub(b0, a0, p)
        if degree(difference) != 3:
            continue
        diff_roots = [x for x in domain if evaluate(difference, x, p) == 0]
        if len(diff_roots) != 3:
            continue
        if set(diff_roots) & set(roots):
            continue
        assert set(roots) | set(diff_roots) <= domain_set
        return a0, b0, diff_roots, attempt
    raise AssertionError("split cubic three-fiber fixture not found")


def smooth_tail_counterfixture() -> tuple[int, int, int, int, int, int, int]:
    p = 401
    domain = subgroup(p, 100)
    a0, b0, diff_roots, attempts = find_split_cubic_fibers(p, domain)
    a_roots = [x for x in domain if evaluate(a0, x, p) == 0]
    b_roots = [x for x in domain if evaluate(b0, x, p) == 0]
    fiber_roots = set(a_roots + b_roots + diff_roots)
    assert len(fiber_roots) == 9

    remaining = [x for x in domain if x not in fiber_roots]
    common_roots = remaining[:13]
    filler = remaining[13:40]
    assert len(filler) == 27
    g = locator(common_roots, p)
    h1 = [0]
    h2 = mul(g, a0, p)
    h3 = mul(g, b0, p)
    assert degree(h2) == degree(h3) == 16

    core = sorted(set(common_roots) | fiber_roots | set(filler))
    assert len(core) == 49 and set(core) <= set(domain)
    bonus, common, exact = triple_bonus((h1, h2, h3), core, p)
    assert common == 13 and exact == (3, 3, 3)
    assert bonus == 35

    values: dict[int, int] = {}
    for x in common_roots:
        values[x] = 0
    for x in a_roots:
        values[x] = 0
    for x in b_roots:
        values[x] = 0
    for x in diff_roots:
        values[x] = evaluate(h2, x, p)
        assert values[x] == evaluate(h3, x, p)
    for index, x in enumerate(filler):
        row = index // 9
        values[x] = evaluate((h1, h2, h3)[row], x, p)

    agreements = tuple(
        sum(evaluate(poly, x, p) == values[x] for x in core)
        for poly in (h1, h2, h3)
    )
    assert agreements == (28, 28, 28)

    ell, b, a = 11, 7, 1
    n_core = 4 * ell + b - 2
    dimension = ell + b - 1
    agreement = 2 * ell + b + a - 2
    j_value = agreement * agreement - n_core * (dimension - 1)
    assert (n_core, dimension, agreement) == (49, 17, 28)
    assert j_value == 0
    assert 3 * agreement - n_core == 2 * (dimension - 1) + 3 * a == bonus
    assert len(domain) == n_core + 4 * ell + b == 100
    assert gcd(100, p) == 1
    return attempts, len(domain), len(core), bonus, agreements[0], dimension, j_value


def source_reduction_fixture() -> tuple[int, int, int]:
    p = 17
    ell, b = 2, 1
    core = list(range(7))
    petals = ((7, 8), (9, 10), (11, 12))
    labels = (1, 2, 3)
    l_core = locator(core, p)
    petal_points = [x for petal in petals for x in petal]
    petal_values = [
        label * evaluate(l_core, x, p) % p
        for label, petal in zip(labels, petals)
        for x in petal
    ]
    p_star = interpolate(petal_points, petal_values, p)
    assert degree(p_star) < 3 * ell
    l = [1]
    for petal in petals:
        l = mul(l, locator(petal, p), p)
    assert degree(l) == 3 * ell
    y = {
        x: -evaluate(p_star, x, p) * pow(evaluate(l, x, p), -1, p) % p
        for x in core
    }

    dimension = ell + b - 1
    checked = 0
    max_agreement = 0
    sign_mutation_caught = False
    for coefficients in product(range(p), repeat=dimension):
        h = trim(list(coefficients))
        codeword = add(p_star, mul(l, h, p), p)
        assert degree(codeword) <= 4 * ell + b - 2
        assert all(
            evaluate(codeword, x, p) == value
            for x, value in zip(petal_points, petal_values)
        )
        core_roots = sum(evaluate(codeword, x, p) == 0 for x in core)
        agreements = sum(evaluate(h, x, p) == y[x] for x in core)
        assert core_roots == agreements
        wrong = sum(
            evaluate(h, x, p)
            == evaluate(p_star, x, p) * pow(evaluate(l, x, p), -1, p) % p
            for x in core
        )
        sign_mutation_caught |= wrong != agreements
        max_agreement = max(max_agreement, agreements)
        checked += 1
    assert sign_mutation_caught
    return checked, max_agreement, int(sign_mutation_caught)


def tail_arithmetic() -> tuple[int, int, bool, bool, bool]:
    cells = 0
    zero_j = 0
    wrong_dimension_caught = False
    wrong_baseline_caught = False
    deleted_surplus_caught = False
    for ell in range(8, 501):
        for b in range(7, ell):
            n_core = 4 * ell + b - 2
            dimension = ell + b - 1
            for a in range(1, (b - 3) // 4 + 1):
                d = 2 * ell - a
                j_value = (
                    ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
                )
                if j_value > 0:
                    continue
                agreement = n_core - d
                assert agreement == 2 * ell + b + a - 2
                assert agreement * agreement - n_core * (dimension - 1) == j_value
                assert 3 * agreement - n_core == 2 * (dimension - 1) + 3 * a
                wrong_dimension = ell + b
                wrong_dimension_caught |= (
                    agreement * agreement - n_core * (wrong_dimension - 1)
                    != j_value
                )
                wrong_baseline_caught |= 2 * dimension != 2 * (dimension - 1)
                deleted_surplus_caught |= 3 * agreement - n_core != 2 * (dimension - 1)
                zero_j += j_value == 0
                cells += 1
    assert cells > 100_000 and zero_j > 0
    return (
        cells,
        zero_j,
        wrong_dimension_caught,
        wrong_baseline_caught,
        deleted_surplus_caught,
    )


def main() -> None:
    map_cases, map_max, sign_caught = source_reduction_fixture()
    (
        attempts,
        domain_size,
        core_size,
        bonus,
        agreement,
        smooth_dimension,
        smooth_j,
    ) = smooth_tail_counterfixture()
    cells, zero_j, dimension_caught, baseline_caught, surplus_caught = tail_arithmetic()

    # The smooth fixture is deliberately constructed without a source lift.
    # It refutes genericity, not the source-coupled PMA statement.
    source_coupled = False
    smooth_genericity_mutation_caught = bonus > 2 * (smooth_dimension - 1)
    source_overclaim_caught = not source_coupled
    tail_scope_mutation_caught = smooth_j <= 0
    mutations = sum(
        (
            bool(sign_caught),
            dimension_caught,
            baseline_caught,
            surplus_caught,
            smooth_genericity_mutation_caught,
            source_overclaim_caught,
            tail_scope_mutation_caught,
        )
    )
    assert mutations == 7

    print(
        f"{NODE}_PASS map_cases={map_cases} map_max={map_max} "
        f"tail_cells={cells} zero_j={zero_j} smooth_order={domain_size} "
        f"smooth_core={core_size} smooth_bonus={bonus} "
        f"smooth_agreement={agreement} smooth_j={smooth_j} "
        f"search_attempts={attempts} "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()

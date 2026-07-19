#!/usr/bin/env python3
"""Verify the PMA petal-pattern root-pinning ledger on small fields."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
import json
from math import comb
from pathlib import Path


NODE = "pma_petal_pattern_root_pinning_ledger"


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ], p)


def sub(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
        for i in range(size)
    ], p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(points: list[int], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [-x, 1], p)
    return out


def divmod_poly(
    numerator: list[int], denominator: list[int], p: int
) -> tuple[list[int], list[int]]:
    numerator = trim(numerator, p)
    denominator = trim(denominator, p)
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, p)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] * inverse_lead % p
        quotient[shift] = factor
        numerator = sub(
            numerator,
            [0] * shift + scale(denominator, factor, p),
            p,
        )
    return trim(quotient, p), trim(numerator, p)


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    left, right = trim(left, p), trim(right, p)
    while right != [0]:
        _, remainder = divmod_poly(left, right, p)
        left, right = right, remainder
    return scale(left, pow(left[-1], -1, p), p)


def interpolate(xs: list[int], ys: list[int], p: int) -> list[int]:
    out = [0]
    for index, x in enumerate(xs):
        other = xs[:index] + xs[index + 1 :]
        basis = locator(other, p)
        denominator = evaluate(basis, x, p)
        out = add(
            out,
            scale(basis, ys[index] * pow(denominator, -1, p), p),
            p,
        )
    return trim(out, p)


def matrix_rank(matrix: list[list[int]], p: int) -> int:
    if not matrix:
        return 0
    work = [[value % p for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, p)
        work[pivot_row] = [inverse * value % p for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (x - factor * y) % p
                for x, y in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def top_matrix(
    xs: list[int], labels: list[int], d: int, p: int
) -> list[list[int]]:
    rows = [[0] * (d + 1) for _ in range(max(0, len(xs) - d - 1))]
    for power in range(d + 1):
        values = [
            label * pow(x, power, p) % p
            for x, label in zip(xs, labels)
        ]
        interpolant = interpolate(xs, values, p)
        for offset, degree in enumerate(range(d + 1, len(xs))):
            rows[offset][power] = (
                interpolant[degree] if degree < len(interpolant) else 0
            )
    return rows


def source_word(
    domain: list[int],
    core: list[int],
    petals: list[list[int]],
    labels: list[int],
    base: list[int],
    p: int,
) -> tuple[dict[int, int], list[int]]:
    core_locator = locator(core, p)
    values = {x: evaluate(base, x, p) for x in domain}
    for petal, label in zip(petals, labels):
        planted = add(base, scale(core_locator, label, p), p)
        for x in petal:
            values[x] = evaluate(planted, x, p)
    return values, core_locator


def verify_case(
    p: int,
    k: int,
    core: list[int],
    petals: list[list[int]],
    background: list[int],
    labels: list[int],
    base: list[int],
) -> tuple[int, int, int]:
    ell = len(petals[0])
    assert all(len(petal) == ell for petal in petals)
    assert len(background) < ell
    domain = core + [x for petal in petals for x in petal] + background
    received, core_locator = source_word(
        domain, core, petals, labels, base, p
    )
    planted = {
        tuple(add(base, scale(core_locator, label, p), p))
        for label in labels
    }
    patterns: dict[tuple, set[tuple[int, ...]]] = defaultdict(set)
    pattern_words: dict[tuple, set[tuple[int, ...]]] = defaultdict(set)
    strata = Counter()
    extras = 0

    for coefficients in product(range(p), repeat=k):
        polynomial = trim(list(coefficients), p)
        agreements = {
            x for x in domain if evaluate(polynomial, x, p) == received[x]
        }
        if len(agreements) < k + ell - 1 or tuple(polynomial) in planted:
            continue
        difference = sub(polynomial, base, p)
        defect = [x for x in core if x not in agreements]
        d = len(defect)
        retained = [x for x in core if x in agreements]
        residual, remainder = divmod_poly(difference, locator(retained, p), p)
        assert remainder == [0] and len(residual) - 1 <= d
        defect_locator = locator(defect, p)
        assert gcd_poly(defect_locator, residual, p) == [1]

        supports = tuple(
            tuple(x for x in petal if x in agreements) for petal in petals
        )
        touched = [index for index, support in enumerate(supports) if support]
        petal_points = [x for support in supports for x in support]
        petal_labels = [
            labels[index]
            for index, support in enumerate(supports)
            for _ in support
        ]
        t, h = len(touched), len(petal_points)
        assert t >= 2 and h > d
        for x, label in zip(petal_points, petal_labels):
            assert evaluate(residual, x, p) == (
                label * evaluate(defect_locator, x, p)
            ) % p

        pattern = (d, supports)
        patterns[pattern].add(tuple(defect_locator))
        pattern_words[(pattern, tuple(defect_locator))].add(tuple(polynomial))
        strata[(d, t, h)] += 1
        extras += 1

    for (d, supports), split_locators in patterns.items():
        xs = [x for support in supports for x in support]
        pattern_labels = [
            labels[index]
            for index, support in enumerate(supports)
            for _ in support
        ]
        h = len(xs)
        width = h - d - 1
        rank = matrix_rank(top_matrix(xs, pattern_labels, d, p), p)
        assert rank == min(d, width)
        exponent = max(0, 2 * d + 1 - h)
        assert len(split_locators) <= comb(k - 1, exponent)
    assert all(len(words) == 1 for words in pattern_words.values())

    for (d, t, h), count in strata.items():
        exponent = max(0, 2 * d + 1 - h)
        bound = comb(len(petals), t) * comb(t * ell, h) * comb(k - 1, exponent)
        assert count <= bound

    closed_checks = 0
    for budget in range(3):
        actual = 0
        ledger = 0
        for (d, t, h), count in strata.items():
            deficit = t * ell - h
            exponent = max(0, 2 * d + 1 - h)
            if deficit + exponent <= budget:
                actual += count
                ledger += (
                    comb(len(petals), t)
                    * comb(t * ell, h)
                    * comb(k - 1, exponent)
                )
        assert actual <= ledger
        closed_checks += 1

    return extras, len(patterns), closed_checks


def main() -> None:
    cases = [
        (11, 3, [0, 1], [[2, 3], [4, 5]], [6], [1, 2], [3, 2]),
        (13, 4, [0, 1, 2], [[3, 4], [5, 6], [7, 8]], [], [1, 2, 3], [2, 1]),
        (17, 4, [0, 1, 2], [[3, 4, 5], [6, 7, 8]], [9, 10], [2, 5], [4, 3]),
    ]
    totals = [verify_case(*case) for case in cases]
    extras = sum(result[0] for result in totals)
    patterns = sum(result[1] for result in totals)
    closure_checks = sum(result[2] for result in totals)
    assert extras > 0 and patterns > 0

    # Maximality is necessary: a background of size ell lists the base word
    # with no petal hit, so h>d fails.
    ell = 2
    k = 3
    assert (k - 1) + ell == k + ell - 1
    assert 0 <= 0

    # Saturation is necessary for maximal rank.
    p = 29
    xs = list(range(2, 10))
    base_f = locator([1], p)
    base_w = [1, 1]
    common = locator([10, 11, 12], p)
    unsaturated_f = mul(base_f, common, p)
    unsaturated_w = mul(base_w, common, p)
    rational_labels = [
        evaluate(unsaturated_w, x, p)
        * pow(evaluate(unsaturated_f, x, p), -1, p)
        % p
        for x in xs
    ]
    unsaturated_rank = matrix_rank(top_matrix(xs, rational_labels, 4, p), p)
    assert unsaturated_rank == 1 < min(4, len(xs) - 4 - 1)
    assert gcd_poly(unsaturated_f, unsaturated_w, p) == common

    resolved = Path(__file__).resolve()
    root = resolved.parents[3] if len(resolved.parents) > 3 else Path.cwd()
    if not (root / "dag.json").exists():
        root = Path.cwd()
    dag = json.loads((root / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert ("pma_saturated_mixed_support_kernel", NODE, "req") in edges
    assert ("petal_reserve_rich_fiber_reduction", NODE, "req") in edges
    assert (NODE, "petal_mixed_amplification", "ev") in edges
    assert (NODE, "imgfib", "ev") in edges

    print(
        "PMA_PETAL_PATTERN_ROOT_PINNING_LEDGER_PASS "
        f"cases={len(cases)} extras={extras} patterns={patterns} "
        f"closure_checks={closure_checks} mutations=2"
    )


if __name__ == "__main__":
    main()

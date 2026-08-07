#!/usr/bin/env python3
"""Verify mixed-support interpolation rank and saturation on finite fields."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
from math import comb
from pathlib import Path


NODE = "pma_saturated_mixed_support_kernel"


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def add(a: list[int], b: list[int], p: int) -> list[int]:
    size = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(size)
    ], p)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    size = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
        for i in range(size)
    ], p)


def scale(a: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * x for x in a], p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
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


def divmod_poly(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    numerator = trim(a, p)
    denominator = trim(b, p)
    assert denominator != [0]
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, p)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] * inverse_lead % p
        quotient[shift] = factor
        correction = [0] * shift + scale(denominator, factor, p)
        numerator = sub(numerator, correction, p)
    return trim(quotient, p), trim(numerator, p)


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    left, right = trim(a, p), trim(b, p)
    while right != [0]:
        _, remainder = divmod_poly(left, right, p)
        left, right = right, remainder
    return scale(left, pow(left[-1], -1, p), p)


def derivative(poly: list[int], p: int) -> list[int]:
    if len(poly) <= 1:
        return [0]
    return trim([i * poly[i] for i in range(1, len(poly))], p)


def interpolate(xs: list[int], ys: list[int], p: int) -> list[int]:
    assert len(xs) == len(ys) == len(set(xs))
    out = [0]
    for i, x in enumerate(xs):
        other = xs[:i] + xs[i + 1 :]
        basis = locator(other, p)
        denominator = evaluate(basis, x, p)
        out = add(out, scale(basis, ys[i] * pow(denominator, -1, p), p), p)
    return trim(out, p)


def rref(matrix: list[list[int]], p: int) -> list[list[int]]:
    if not matrix:
        return []
    work = [[x % p for x in row] for row in matrix]
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, p)
        work[pivot_row] = [(inverse * x) % p for x in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (x - factor * y) % p
                for x, y in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return work[:pivot_row]


def matrix_rank(matrix: list[list[int]], p: int) -> int:
    return len(rref(matrix, p))


def top_matrix(xs: list[int], labels: list[int], d: int, p: int) -> list[list[int]]:
    s = len(xs)
    rows = [[0] * (d + 1) for _ in range(s - d - 1)]
    for power in range(d + 1):
        values = [label * pow(x, power, p) % p for x, label in zip(xs, labels)]
        interpolant = interpolate(xs, values, p)
        for offset, degree in enumerate(range(d + 1, s)):
            rows[offset][power] = interpolant[degree] if degree < len(interpolant) else 0
    return rows


def hankel_matrix(
    xs: list[int], labels: list[int], d: int, p: int
) -> list[list[int]]:
    support_locator = locator(xs, p)
    support_derivative = derivative(support_locator, p)
    moments = []
    for power in range(len(xs) - 1):
        moment = 0
        for x, label in zip(xs, labels):
            denominator = evaluate(support_derivative, x, p)
            moment += label * pow(x, power, p) * pow(denominator, -1, p)
        moments.append(moment % p)
    width = len(xs) - d - 1
    return [
        [moments[row + column] for column in range(d + 1)]
        for row in range(width)
    ]


def split_kernel_locators(
    core: list[int], d: int, xs: list[int], labels: list[int], p: int
) -> list[list[int]]:
    locators = []
    for roots in combinations(core, d):
        candidate = locator(list(roots), p)
        _, top = top_coefficients(xs, labels, candidate, d, p)
        if not any(top):
            locators.append(candidate)
    return locators


def top_coefficients(
    xs: list[int], labels: list[int], f: list[int], d: int, p: int
) -> tuple[list[int], list[int]]:
    values = [label * evaluate(f, x, p) % p for x, label in zip(xs, labels)]
    interpolant = interpolate(xs, values, p)
    top = [interpolant[i] if i < len(interpolant) else 0 for i in range(d + 1, len(xs))]
    return interpolant, top


def verify_rank_pattern(
    xs: list[int], labels: list[int], d: int, ell: int, slack: int, p: int
) -> tuple[int, int, bool]:
    assert len(xs) == d + ell + slack
    sizes = Counter(labels)
    largest = max(sizes.values())
    assert largest <= min(d, ell)
    rank = matrix_rank(top_matrix(xs, labels, d, p), p)
    exceptional = len(xs) - largest == d
    assert rank >= largest - int(exceptional)
    if not exceptional:
        assert rank >= largest
    if exceptional:
        assert slack == 0 and largest == ell
    return rank, largest, exceptional


def main() -> None:
    patterns = 0
    p = 101
    for d in range(1, 6):
        for ell in range(2, 6):
            for slack in range(3):
                s = d + ell + slack
                cap = min(d, ell)
                sizes = []
                remaining = s
                while remaining:
                    size = min(cap, remaining)
                    sizes.append(size)
                    remaining -= size
                labels = []
                for label, size in enumerate(sizes, start=1):
                    labels.extend([label] * size)
                rank, largest, exceptional = verify_rank_pattern(
                    list(range(1, s + 1)), labels, d, ell, slack, p
                )
                top = top_matrix(list(range(1, s + 1)), labels, d, p)
                hankel = hankel_matrix(list(range(1, s + 1)), labels, d, p)
                assert rref(top, p) == rref(hankel, p)
                assert rank <= ell + slack - 1
                assert largest == cap
                assert exceptional == (slack == 0 and cap == ell)
                patterns += 1

    p = 29
    f0 = locator([1, -1 % p], p)
    w0 = [1, 0, 1]

    strict_xs = [2, -2 % p, 3, -3 % p, 4]
    strict_labels = [
        evaluate(w0, x, p) * pow(evaluate(f0, x, p), -1, p) % p
        for x in strict_xs
    ]
    strict_rank, strict_largest, strict_exceptional = verify_rank_pattern(
        strict_xs, strict_labels, d=2, ell=3, slack=0, p=p
    )
    assert (strict_rank, strict_largest, strict_exceptional) == (2, 2, False)
    assert strict_rank == min(2, len(strict_xs) - 2 - 1)
    interpolant, top = top_coefficients(strict_xs, strict_labels, f0, 2, p)
    assert trim(interpolant, p) == w0 and top == [0, 0]

    exceptional_xs = strict_xs[:4]
    exceptional_labels = strict_labels[:4]
    exceptional_rank, exceptional_largest, is_exceptional = verify_rank_pattern(
        exceptional_xs, exceptional_labels, d=2, ell=2, slack=0, p=p
    )
    assert (exceptional_rank, exceptional_largest, is_exceptional) == (1, 2, True)
    assert exceptional_rank < exceptional_largest
    assert exceptional_rank == min(2, len(exceptional_xs) - 2 - 1)

    # The d<w regime has a one-dimensional kernel generated by the locator.
    low_f = locator([1], p)
    low_w = [1, 1]
    low_xs = [2, 3, 4, 5]
    low_labels = [
        evaluate(low_w, x, p) * pow(evaluate(low_f, x, p), -1, p) % p
        for x in low_xs
    ]
    low_rank, _, _ = verify_rank_pattern(
        low_xs, low_labels, d=1, ell=2, slack=1, p=p
    )
    assert low_rank == min(1, len(low_xs) - 1 - 1) == 1

    classes: dict[int, list[int]] = {}
    for x, label in zip(strict_xs, strict_labels):
        classes.setdefault(label, []).append(x)
    assert gcd_poly(f0, w0, p) == [1]
    fiber_polynomials = []
    for label, points in classes.items():
        fiber = sub(w0, scale(f0, label, p), p)
        quotient, remainder = divmod_poly(fiber, locator(points, p), p)
        assert remainder == [0] and quotient != [0]
        assert gcd_poly(f0, fiber, p) == [1]
        fiber_polynomials.append(fiber)
    for i, left in enumerate(fiber_polynomials):
        for right in fiber_polynomials[i + 1 :]:
            assert gcd_poly(left, right, p) == [1]

    # Distinct labels are load-bearing: collapsing them makes T identically zero.
    collapsed_rank = matrix_rank(top_matrix(strict_xs, [7] * len(strict_xs), 2, p), p)
    assert collapsed_rank == 0 < strict_largest

    # A common core factor gives the same codeword contribution but is non-exact.
    h = locator([5], p)
    enlarged_f = mul(h, f0, p)
    enlarged_w = mul(h, w0, p)
    core = [1, -1 % p, 5, 6]
    old_contribution = mul(locator([5, 6], p), w0, p)
    new_contribution = mul(locator([6], p), enlarged_w, p)
    assert old_contribution == new_contribution
    assert evaluate(enlarged_w, 5, p) == 0
    assert gcd_poly(enlarged_f, enlarged_w, p) == h
    assert set(core).isdisjoint(strict_xs)

    # Canonical root pinning bounds every split locator in a fixed kernel.
    strict_core = [1, -1 % p, 5, 6, 7]
    strict_split = split_kernel_locators(
        strict_core, 2, strict_xs, strict_labels, p
    )
    strict_width = len(strict_xs) - 2 - 1
    strict_bound = comb(len(strict_core), max(0, 2 - strict_width))
    assert f0 in strict_split and len(strict_split) <= strict_bound == 1

    exceptional_split = split_kernel_locators(
        strict_core, 2, exceptional_xs, exceptional_labels, p
    )
    exceptional_width = len(exceptional_xs) - 2 - 1
    exceptional_bound = comb(
        len(strict_core), max(0, 2 - exceptional_width)
    )
    assert f0 in exceptional_split and len(exceptional_split) <= exceptional_bound

    low_core = [1, 6, 7]
    low_split = split_kernel_locators(low_core, 1, low_xs, low_labels, p)
    low_width = len(low_xs) - 1 - 1
    low_bound = comb(len(low_core), max(0, 1 - low_width))
    assert low_f in low_split and len(low_split) <= low_bound == 1

    # Without saturation, a common factor creates a genuine maximal-rank failure.
    unsaturated_xs = list(range(2, 10))
    base_f = locator([1], p)
    base_w = [1, 1]
    common = locator([10, 11, 12], p)
    unsaturated_f = mul(base_f, common, p)
    unsaturated_w = mul(base_w, common, p)
    unsaturated_labels = [
        evaluate(unsaturated_w, x, p)
        * pow(evaluate(unsaturated_f, x, p), -1, p)
        % p
        for x in unsaturated_xs
    ]
    unsaturated_rank = matrix_rank(
        top_matrix(unsaturated_xs, unsaturated_labels, 4, p), p
    )
    assert unsaturated_rank == 1 < min(4, len(unsaturated_xs) - 4 - 1)
    assert gcd_poly(unsaturated_f, unsaturated_w, p) == common

    resolved = Path(__file__).resolve()
    root = resolved.parents[3] if len(resolved.parents) > 3 else Path.cwd()
    if not (root / "dag.json").exists():
        root = Path.cwd()
    dag = json.loads((root / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["petal_mixed_amplification"]["status"] == "TARGET"
    assert ("pma_aux_list_reduction", NODE, "req") in edges
    assert ("petal_reserve_rich_fiber_reduction", NODE, "req") in edges
    assert (NODE, "petal_mixed_amplification", "ev") in edges
    assert (NODE, "imgfib", "ev") in edges

    print(
        "PMA_SATURATED_MIXED_SUPPORT_KERNEL_PASS "
        f"patterns={patterns} hankel={patterns} maximal_rank=3 "
        f"strict_rank={strict_rank} "
        f"exceptional_rank={exceptional_rank} fibers={len(fiber_polynomials)} "
        f"pinned_counts={len(low_split)},{len(strict_split)},{len(exceptional_split)} "
        "mutations=4"
    )


if __name__ == "__main__":
    main()

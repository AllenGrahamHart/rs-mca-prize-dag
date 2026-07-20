#!/usr/bin/env python3
"""Finite-field replay for the exceptional quotient-distance router."""

from __future__ import annotations

from itertools import combinations


P = 101


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def rank(columns: list[list[int]]) -> int:
    if not columns:
        return 0
    matrix = [list(row) for row in zip(*columns, strict=True)]
    rows = len(matrix)
    cols = len(columns)
    pivot = 0
    for column in range(cols):
        choice = next(
            (row for row in range(pivot, rows) if matrix[row][column] % P),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scale = inv(matrix[pivot][column])
        matrix[pivot] = [(scale * value) % P for value in matrix[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = matrix[row][column] % P
            if factor:
                matrix[row] = [
                    (left - factor * right) % P
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def column(x: int, r: int) -> list[int]:
    return [pow(x, degree, P) for degree in range(2 * r + 1)]


def in_span(target: list[int], columns: list[list[int]]) -> bool:
    return rank(columns) == rank(columns + [target])


def locator_value(x: int, roots: tuple[int, ...]) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def main() -> None:
    r = 5
    roots = (1, 2, 3, 4)
    triple = (5, 6, 7)
    extras = (8, 9)
    domain = roots + triple + extras
    theta_2 = 17

    eta = {}
    omega = {}
    for x in triple:
        denominator = 1
        for y in triple:
            if y != x:
                denominator = denominator * (x - y) % P
        eta[x] = theta_2 * inv(denominator) % P
        a_x = locator_value(x, roots)
        omega[x] = eta[x] * inv(a_x * a_x) % P

    root_weights = {x: 11 + x for x in roots}
    source_weights = root_weights | omega
    h_1 = [
        sum(weight * pow(x, degree, P) for x, weight in source_weights.items()) % P
        for degree in range(2 * r + 1)
    ]

    theta = []
    for shift in range(3):
        theta.append(
            sum(
                weight
                * pow(x, shift, P)
                * pow(locator_value(x, roots), 2, P)
                for x, weight in source_weights.items()
            )
            % P
        )
    assert theta == [0, 0, theta_2]

    root_columns = [column(x, r) for x in roots]
    outside = triple + extras
    supports = []
    for size in range(4):
        for support in combinations(outside, size):
            if in_span(h_1, root_columns + [column(x, r) for x in support]):
                supports.append(support)
    assert supports == [triple]

    # The union of two hypothetical triples and the root columns is still
    # inside the Vandermonde independence range r+5 <= 2r+1.
    for other in combinations(outside, 3):
        union = tuple(dict.fromkeys(roots + triple + other))
        assert rank([column(x, r) for x in union]) == len(union)

    # Both zero moments are load-bearing: with only the degree-zero equation,
    # a two-point vector can retain a nonzero quadratic moment.
    x, y = extras
    two_eta = {x: 1, y: -1 % P}
    assert sum(two_eta.values()) % P == 0
    assert sum(t * value for t, value in two_eta.items()) % P != 0
    assert sum(t * t * value for t, value in two_eta.items()) % P != 0

    for x, y in combinations(outside, 2):
        assert (x - y) % P != 0
        # The two-column degree-zero/one Vandermonde determinant is nonzero.
        assert (1 * y - 1 * x) % P != 0

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "QUOTIENT_DISTANCE_ROUTER_PASS "
        f"r={r} roots={len(roots)} unique_triple={triple} theta={theta}"
    )


if __name__ == "__main__":
    main()

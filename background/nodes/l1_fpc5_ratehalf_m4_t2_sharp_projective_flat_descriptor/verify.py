#!/usr/bin/env python3
"""Tiny replay of the sharp FPC5 flat descriptor and gcd division."""

from __future__ import annotations

from itertools import combinations
import random


P = 97


def trim(poly: list[int]) -> list[int]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pad(poly: list[int], length: int) -> list[int]:
    return trim(poly) + [0] * (length - len(trim(poly)))


def add(left: list[int], right: list[int]) -> list[int]:
    length = max(len(left), len(right))
    return trim(
        [
            ((left[i] if i < len(left) else 0)
             + (right[i] if i < len(right) else 0))
            % P
            for i in range(length)
        ]
    )


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value % P for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def evaluate(poly: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % P
    return value


def divmod_poly(numerator: list[int], denominator: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(numerator)
    denominator = trim(denominator)
    assert denominator != [0]
    if len(remainder) < len(denominator):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, P)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - coefficient * value
            ) % P
        remainder = trim(remainder)
    return trim(quotient), remainder


def exact_div(numerator: list[int], denominator: list[int]) -> list[int]:
    quotient, remainder = divmod_poly(numerator, denominator)
    assert remainder == [0]
    return quotient


def monic_gcd(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    if left == [0]:
        return [0]
    return scale(left, pow(left[-1], -1, P))


def gcd_basis(polynomials: list[list[int]]) -> list[int]:
    common = trim(polynomials[0])
    for polynomial in polynomials[1:]:
        common = monic_gcd(common, polynomial)
    return common


def locator(points: tuple[int, ...] | list[int]) -> list[int]:
    out = [1]
    for point in points:
        out = mul(out, [(-point) % P, 1])
    return out


def rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    columns = max(len(row) for row in matrix)
    a = [pad(row, columns) for row in matrix]
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(a)) if a[row][column]), None
        )
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][column], -1, P)
        a[pivot_row] = [value * inverse % P for value in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row and a[row][column]:
                factor = a[row][column]
                a[row] = [
                    (left - factor * right) % P
                    for left, right in zip(a[row], a[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def nullspace(matrix: list[list[int]], columns: int) -> list[list[int]]:
    a = [pad(row, columns) for row in matrix]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(a)) if a[row][column]), None
        )
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][column], -1, P)
        a[pivot_row] = [value * inverse % P for value in a[pivot_row]]
        for row in range(len(a)):
            if row != pivot_row and a[row][column]:
                factor = a[row][column]
                a[row] = [
                    (left - factor * right) % P
                    for left, right in zip(a[row], a[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(a):
            break
    free_columns = [c for c in range(columns) if c not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -a[row][free] % P
        basis.append(vector)
    return basis


def primitive_root() -> int:
    for candidate in range(2, P):
        if pow(candidate, 48, P) != 1 and pow(candidate, 32, P) != 1:
            return candidate
    raise AssertionError("no primitive root")


def in_span(vector: list[int], basis: list[list[int]], length: int) -> bool:
    rows = [pad(item, length) for item in basis]
    return rank(rows) == rank(rows + [pad(vector, length)])


def main() -> None:
    official_k = 2**40
    official_ell = (official_k + 4) // 5
    assert 5 * official_ell == official_k + 4
    assert official_k - 1 == 5 * official_ell - 5

    ell, j = 4, 5
    generator = primitive_root()
    domain = [pow(generator, 3 * exponent, P) for exponent in range(32)]
    points = domain[:]
    random.Random(3).shuffle(points)
    core = points[:15]
    background = points[15:16]
    tail = points[16:]
    petals = [tail[index * ell : (index + 1) * ell] for index in range(4)]

    first, second = 1, 3
    c1, c2 = 1, 72
    l1, l2 = locator(petals[first]), locator(petals[second])
    variables_per_side = ell - 2
    congruence_rows = []
    for point in background:
        row = [
            c2 * evaluate(l1, point) * pow(point, degree, P) % P
            for degree in range(variables_per_side)
        ]
        row += [
            -c1 * evaluate(l2, point) * pow(point, degree, P) % P
            for degree in range(variables_per_side)
        ]
        congruence_rows.append([value % P for value in row])
    cofactor_basis = nullspace(congruence_rows, 2 * variables_per_side)
    assert len(cofactor_basis) == ell - 1 == 3

    f_basis: list[list[int]] = []
    w_basis: list[list[int]] = []
    inverse_label_gap = pow(c2 - c1, -1, P)
    for vector in cofactor_basis:
        a1 = vector[:variables_per_side]
        a2 = vector[variables_per_side:]
        f_poly = scale(add(mul(l1, a1), scale(mul(l2, a2), -1)), inverse_label_gap)
        w_poly = add(scale(f_poly, c1), mul(l1, a1))
        assert len(f_poly) - 1 <= j and len(w_poly) - 1 <= j
        assert all(evaluate(w_poly, point) == 0 for point in background)
        assert all(
            evaluate(w_poly, point) == c1 * evaluate(f_poly, point) % P
            for point in petals[first]
        )
        assert all(
            evaluate(w_poly, point) == c2 * evaluate(f_poly, point) % P
            for point in petals[second]
        )
        f_basis.append(f_poly)
        w_basis.append(w_poly)

    assert rank(f_basis) == ell - 1
    assert rank([pad(poly, j + 1) for poly in f_basis]) == ell - 1
    assert any(len(poly) - 1 == j for poly in f_basis)
    assert j - (ell - 2) == ell - 1

    witness_f = [67, 32, 8, 88, 89, 1]
    witness_w = [40, 90, 43, 55, 78, 76]
    assert in_span(witness_f, f_basis, j + 1)
    assert in_span(witness_w, w_basis, j + 1)
    witness_a1 = exact_div(add(witness_w, scale(witness_f, -c1)), l1)
    witness_a2 = exact_div(add(witness_w, scale(witness_f, -c2)), l2)
    assert len(witness_a1) <= variables_per_side
    assert len(witness_a2) <= variables_per_side
    reconstructed_f = scale(
        add(mul(l1, witness_a1), scale(mul(l2, witness_a2), -1)),
        inverse_label_gap,
    )
    reconstructed_w = add(scale(reconstructed_f, c1), mul(l1, witness_a1))
    assert reconstructed_f == witness_f
    assert reconstructed_w == witness_w
    assert all(evaluate(witness_w, point) == 0 for point in background)

    split_hits: list[tuple[tuple[int, ...], list[int]]] = []
    for roots in combinations(core, j):
        f_poly = locator(roots)
        if in_span(f_poly, f_basis, j + 1):
            split_hits.append((roots, f_poly))
    assert split_hits
    assert any(poly == witness_f for _, poly in split_hits)
    assert len({tuple(poly) for _, poly in split_hits}) == len(split_hits)

    common = gcd_basis(f_basis)
    assert common == [1]
    forced_root = next(point for point in core if point not in split_hits[0][0])
    forced_factor = locator([forced_root])
    lifted_basis = [mul(forced_factor, poly) for poly in f_basis]
    assert gcd_basis(lifted_basis) == forced_factor
    reduced_basis = [exact_div(poly, forced_factor) for poly in lifted_basis]
    assert reduced_basis == [trim(poly) for poly in f_basis]
    assert rank(reduced_basis) == rank(lifted_basis) == ell - 1

    lifted = mul(forced_factor, split_hits[0][1])
    assert len(lifted) - 1 == j + 1
    assert exact_div(lifted, forced_factor) == split_hits[0][1]
    assert len(set(split_hits[0][0]) | {forced_root}) == j + 1

    print(
        "L1_FPC5_SHARP_PROJECTIVE_FLAT_DESCRIPTOR_PASS "
        f"dim={len(f_basis)} projective_dim={ell - 2} "
        f"split_hits={len(split_hits)} official_ell={official_ell}"
    )


if __name__ == "__main__":
    main()

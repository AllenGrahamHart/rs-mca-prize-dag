#!/usr/bin/env python3
"""Finite-field replay for the distance-three pair-Lagrange normal form."""

from __future__ import annotations


P = 101


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def product(values: list[int]) -> int:
    out = 1
    for value in values:
        out = out * value % P
    return out


def locator(roots: tuple[int, ...], x: int) -> int:
    return product([(x - root) % P for root in roots])


def rank(columns: list[list[int]]) -> int:
    matrix = [list(row) for row in zip(*columns, strict=True)]
    rows = len(matrix)
    cols = len(columns)
    pivot = 0
    for col in range(cols):
        choice = next(
            (row for row in range(pivot, rows) if matrix[row][col] % P),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scale = inv(matrix[pivot][col])
        matrix[pivot] = [(scale * value) % P for value in matrix[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = matrix[row][col] % P
            if factor:
                matrix[row] = [
                    (left - factor * right) % P
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def main() -> None:
    roots_a = (1, 2, 3, 4)
    triple = (5, 6, 7)
    pairs = ((1, 2), (3, 4))
    xis = (11, 13)
    lambdas = (17, 19)
    e = len(pairs)

    def a_value(x: int) -> int:
        return locator(roots_a, x)

    def b_value(x: int) -> int:
        return locator(triple, x)

    def quotient_value(index: int, x: int) -> int:
        retained = tuple(root for root in roots_a if root not in pairs[index])
        return locator(retained, x)

    def phi(z: int) -> int:
        return product([(z - xi) % P for xi in xis]) * inv(
            product([(-xi) % P for xi in xis])
        ) % P

    def lagrange(index: int, z: int) -> int:
        numerator = product(
            [(z - xi) % P for j, xi in enumerate(xis) if j != index]
        )
        denominator = product(
            [(xis[index] - xi) % P for j, xi in enumerate(xis) if j != index]
        )
        return numerator * inv(denominator) % P

    def q_value(z: int, x: int) -> int:
        correction = sum(
            lambdas[i]
            * inv(xis[i])
            * lagrange(i, z)
            * quotient_value(i, x)
            for i in range(e)
        ) % P
        return (phi(z) * a_value(x) + z * b_value(x) * correction) % P

    for x in range(1, 25):
        assert q_value(0, x) == a_value(x)

    for i, xi in enumerate(xis):
        expected_roots = (tuple(root for root in roots_a if root not in pairs[i]) + triple)
        for x in range(1, 25):
            expected = lambdas[i] * b_value(x) * quotient_value(i, x) % P
            assert q_value(xi, x) == expected
        assert {x for x in range(1, 8) if q_value(xi, x) == 0} == set(expected_roots)

    for z in range(0, 31):
        ratios = [q_value(z, t) * inv(a_value(t)) % P for t in triple]
        assert ratios == [phi(z)] * 3

    for i, pair in enumerate(pairs):
        for a in pair:
            assert q_value(0, a) == 0
            assert q_value(xis[i], a) != 0
            for j, xi in enumerate(xis):
                if j != i:
                    assert q_value(xi, a) == 0

    x_samples = tuple(range(1, e + 4))
    x_basis = [[a_value(x) for x in x_samples]] + [
        [b_value(x) * quotient_value(i, x) % P for x in x_samples]
        for i in range(e)
    ]
    z_samples = (0, *xis)
    z_basis = [[phi(z) for z in z_samples]] + [
        [z * lagrange(i, z) % P for z in z_samples] for i in range(e)
    ]
    assert rank(x_basis) == rank(z_basis) == e + 1

    # Overlapping pairs leave an unpaired exceptional root fixed for all z.
    bad_pairs = ((1, 2), (2, 3))
    unpaired = 4
    for z in (0, 1, 2, 11, 13, 17):
        bad_correction = sum(
            lambdas[i]
            * inv(xis[i])
            * lagrange(i, z)
            * locator(tuple(root for root in roots_a if root not in bad_pairs[i]), unpaired)
            for i in range(e)
        ) % P
        bad_q = (phi(z) * a_value(unpaired) + z * b_value(unpaired) * bad_correction) % P
        assert bad_q == 0

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_PAIR_LAGRANGE_NORMAL_FORM_PASS "
        f"e={e} pairs={pairs} xis={xis} rank={e + 1}"
    )


if __name__ == "__main__":
    main()

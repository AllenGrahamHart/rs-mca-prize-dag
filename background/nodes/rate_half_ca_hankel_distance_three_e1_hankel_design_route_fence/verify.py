#!/usr/bin/env python3
"""Exact F_17 replay for the e=1 Hankel-design route fence."""

from __future__ import annotations

from itertools import combinations


P = 17
D = tuple(range(1, P))
D_RES = tuple(range(2, P))


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return out


def locator_coefficients(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = poly_mul(out, [(-root) % P, 1])
    return out


def poly_eval(coefficients: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % P
    return value


def rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    pivot = 0
    for col in range(cols):
        choice = next(
            (row for row in range(pivot, rows) if work[row][col] % P),
            None,
        )
        if choice is None:
            continue
        work[pivot], work[choice] = work[choice], work[pivot]
        scale = inv(work[pivot][col])
        work[pivot] = [(scale * value) % P for value in work[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = work[row][col] % P
            if factor:
                work[row] = [
                    (left - factor * right) % P
                    for left, right in zip(work[row], work[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def hankel(sequence: list[int], rows: int, cols: int) -> list[list[int]]:
    return [[sequence[i + j] for j in range(cols)] for i in range(rows)]


def matvec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector, strict=True)) % P for row in matrix]


def pairing(left: list[int], matrix: list[list[int]], right: list[int]) -> int:
    return sum(
        left[i] * matrix[i][j] * right[j]
        for i in range(len(left))
        for j in range(len(right))
    ) % P


def det3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % P


def adjugate4(matrix: list[list[int]]) -> list[list[int]]:
    out = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            minor = [
                [matrix[row][col] for col in range(4) if col != i]
                for row in range(4)
                if row != j
            ]
            sign = -1 if (i + j) % 2 else 1
            out[i][j] = sign * det3(minor) % P
    return out


def moment_column(x: int) -> list[int]:
    return [pow(x, degree, P) for degree in range(7)]


def in_span(target: list[int], columns: list[list[int]]) -> bool:
    if columns:
        matrix = [list(row) for row in zip(*columns, strict=True)]
        augmented = [row + [target[i]] for i, row in enumerate(matrix)]
    else:
        matrix = [[] for _ in target]
        augmented = [[value] for value in target]
    return rank(matrix) == rank(augmented)


def main() -> None:
    roots_a = (2, 5)
    roots_b = (3, 13, 15)
    external = {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}
    omitted = 14
    supported = (0, 1, 2, 4, 15)

    a = locator_coefficients(roots_a) + [0]
    b = locator_coefficients(roots_b)
    q_1 = [(right - left) % P for left, right in zip(a, b, strict=True)]
    assert a == [10, 10, 1, 0]
    assert b == [10, 7, 3, 1]
    assert q_1 == [0, 14, 2, 1]

    h_0 = [0, 10, 2, 16, 7, 8, 3]
    h_1 = [15, 16, 6, 2, 14, 12, 1]
    m_0 = hankel(h_0, 4, 4)
    m_1 = hankel(h_1, 4, 4)
    u = a
    v = [0, *a[:3]]

    assert matvec(m_0, u) == [0] * 4
    assert matvec(m_0, v) == [0] * 4
    assert pairing(u, m_1, u) == 0
    assert pairing(v, m_1, u) == 0
    crossing = pairing(v, m_1, v)
    assert crossing == 14

    c_h = None
    for z in range(P):
        q = [(left + z * right) % P for left, right in zip(a, q_1, strict=True)]
        matrix = [
            [(m_0[i][j] + z * m_1[i][j]) % P for j in range(4)]
            for i in range(4)
        ]
        assert matvec(matrix, q) == [0] * 4
        assert rank(matrix) == (2 if z == 0 else 3)
        adj = adjugate4(matrix)
        if z == 0:
            assert adj == [[0] * 4 for _ in range(4)]
        if z == 1:
            c_h = adj[0][0] * inv(q[0] * q[0]) % P
            assert c_h
        if c_h is not None:
            expected = [[c_h * z * q[i] * q[j] % P for j in range(4)] for i in range(4)]
            assert adj == expected
    assert c_h is not None

    assert rank(m_1) == 3
    assert matvec(m_1, q_1) == [0] * 4
    assert rank(m_0 + m_1) == 4

    def lift(sequence: list[int]) -> list[int]:
        out = [0]
        for value in sequence:
            out.append((out[-1] + value) % P)
        return out

    y_0 = lift(h_0)
    y_1 = lift(h_1)
    assert y_0 == [0, 0, 10, 12, 11, 1, 9, 12]
    assert y_1 == [0, 15, 14, 3, 5, 2, 14, 15]

    locators = [(roots, locator_coefficients(roots)) for roots in combinations(D, 4)]

    def annihilates(sequence: list[int], coefficients: list[int]) -> bool:
        matrix = hankel(sequence, 4, 5)
        return matvec(matrix, coefficients) == [0] * 4

    common = [
        roots for roots, coefficients in locators
        if annihilates(y_0, coefficients) and annihilates(y_1, coefficients)
    ]
    assert common == []

    found: dict[int, list[tuple[int, ...]]] = {}
    for z in range(P):
        sequence = [(left + z * right) % P for left, right in zip(y_0, y_1, strict=True)]
        matches = [roots for roots, coefficients in locators if annihilates(sequence, coefficients)]
        if matches:
            found[z] = matches
    infinity = [roots for roots, coefficients in locators if annihilates(y_1, coefficients)]
    assert set(found) == set(supported)
    assert infinity == []
    expected_exceptional = [
        tuple(sorted((1, 2, 5, extra))) for extra in D if extra not in (1, 2, 5)
    ]
    assert found[0] == expected_exceptional
    assert found[1] == [(1, *roots_b)]
    for z, roots in external.items():
        assert found[z] == [(1, *roots)]

    active = tuple(x for roots in external.values() for x in roots)
    assert len(set(active)) == 9
    assert omitted not in active
    for x in range(P):
        external_product = 1
        for roots in external.values():
            external_product = external_product * poly_eval(locator_coefficients(roots), x) % P
        assert external_product == poly_eval(locator_coefficients(tuple(sorted(active))), x)

    p_x_roots = tuple(x for x in D_RES if x != omitted)
    p_x = locator_coefficients(p_x_roots)
    raw_ratio = None
    for x in range(P):
        raw_product = 1
        for z in supported:
            q = [(left + z * right) % P for left, right in zip(a, q_1, strict=True)]
            raw_product = raw_product * poly_eval(q, x) % P
        value = poly_eval(p_x, x)
        if value:
            ratio = raw_product * inv(value) % P
            raw_ratio = ratio if raw_ratio is None else raw_ratio
            assert ratio == raw_ratio
        else:
            assert raw_product == 0
    assert raw_ratio

    root_columns = [moment_column(x) for x in roots_a]
    outside_a = tuple(x for x in D_RES if x not in roots_a)
    support_triples = []
    for size in range(4):
        matches = []
        for support in combinations(outside_a, size):
            columns = root_columns + [moment_column(x) for x in support]
            if in_span(h_1, columns):
                matches.append(support)
        if size < 3:
            assert matches == []
        else:
            support_triples = matches
    assert support_triples == [roots_b, external[15], external[2], external[4]]

    print(
        "RATE_HALF_CA_HANKEL_DISTANCE_THREE_E1_HANKEL_DESIGN_ROUTE_FENCE_PASS "
        f"field={P} locators={len(locators)} supported={supported} "
        f"c_H={c_h} crossing={crossing} quotient_triples={len(support_triples)}"
    )


if __name__ == "__main__":
    main()

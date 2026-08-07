#!/usr/bin/env python3
"""Tiny rank replay for the rate-half codimension-two guarded slice."""

from __future__ import annotations


P = 1009


def evaluate(poly: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = (out[i + j] + left * right) % P
    return out


def locator(roots: range) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if a[row][col]), None
        )
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][col], P - 2, P)
        a[pivot_row] = [(entry * inverse) % P for entry in a[pivot_row]]
        for row in range(rows):
            if row != pivot_row and a[row][col]:
                scale = a[row][col]
                a[row] = [
                    (left - scale * right) % P
                    for left, right in zip(a[row], a[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def equation_row(d: int, x: int, f_scale: int, w_scale: int) -> list[int]:
    powers = [pow(x, degree, P) for degree in range(d + 1)]
    return [f_scale * value % P for value in powers] + [
        w_scale * value % P for value in powers
    ]


def main() -> None:
    official_k = 2**40
    ell_official = (official_k + 4) // 5
    assert 5 * ell_official == official_k + 4
    assert 4 * ell_official + (ell_official - 3) == official_k + 1

    cells = 0
    for ell in range(4, 13):
        background = range(1, ell - 2)
        petal_1 = range(100, 100 + ell)
        petal_2 = range(300, 300 + ell)
        l0 = locator(background)
        l1 = locator(petal_1)
        l2 = locator(petal_2)
        d = 2 * ell - 3
        c1, c2 = 2, 5

        petal_rows = [
            equation_row(d, x, -c1, 1) for x in petal_1
        ] + [equation_row(d, x, -c2, 1) for x in petal_2]
        assert rank(petal_rows) == 2 * ell
        assert 2 * (d + 1) - rank(petal_rows) == 2 * ell - 4

        guarded_rows = [equation_row(d, x, 0, 1) for x in background]
        guarded_rows += petal_rows
        guarded_rank = rank(guarded_rows)
        assert guarded_rank == 3 * ell - 3
        assert 2 * (d + 1) - guarded_rank == ell - 1
        assert (d + 1) - (ell - 1) == ell - 1

        congruence_rows: list[list[int]] = []
        for x in background:
            row = [
                c2 * evaluate(l1, x) * pow(x, degree, P) % P
                for degree in range(ell - 2)
            ]
            row += [
                -c1 * evaluate(l2, x) * pow(x, degree, P) % P
                for degree in range(ell - 2)
            ]
            congruence_rows.append([entry % P for entry in row])
        assert rank(congruence_rows) == ell - 3
        assert 2 * (ell - 2) - rank(congruence_rows) == ell - 1

        assert len(l0) - 1 == ell - 3
        cells += 1

    print(
        "L1_FPC5_RATEHALF_M4_T2_GUARDED_SLICE_PASS "
        f"cells={cells} official_ell={ell_official}"
    )


if __name__ == "__main__":
    main()

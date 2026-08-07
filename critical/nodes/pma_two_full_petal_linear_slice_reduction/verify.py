#!/usr/bin/env python3
"""Tiny finite-field replay of the two-full-petal slice dimensions."""

from __future__ import annotations


P = 101


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return out


def locator(roots: range) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def rank(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], P - 2, P)
        a[r] = [(x * inv) % P for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x - q * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def main() -> None:
    cells = 0
    for ell in range(1, 9):
        l1 = locator(range(1, ell + 1))
        l2 = locator(range(20, 20 + ell))
        for s in range(ell):
            d = ell + s
            columns: list[list[int]] = []
            for side, loc in ((1, l1), (-1, l2)):
                for shift in range(s + 1):
                    col = [0] * (d + 1)
                    for i, value in enumerate(loc):
                        col[i + shift] = side * value % P
                    columns.append(col)
            matrix = [[column[i] for column in columns] for i in range(d + 1)]
            assert rank(matrix) == 2 * s + 2
            assert (d + 1) - rank(matrix) == ell - s - 1
            cells += 1
    print(f"PMA_TWO_FULL_PETAL_SLICE_PASS cells={cells} max_ell=8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent integer audit of the bordered-Hankel flag split."""

from fractions import Fraction


def det(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    value = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, len(work)):
            scale = work[row][column] / pivot_value
            for index in range(column, len(work)):
                work[row][index] -= scale * work[column][index]
    return value


e = 183251937963
d = 3 * e - 2
g_off = e - 7
h_reg = 2 * e + 7
assert (d, d + 2, g_off, h_reg) == (
    549755813887,
    549755813889,
    183251937956,
    366503875933,
)
assert g_off + h_reg == 3 * e

h = [1, 0, 1, 0, 1, 2, 3, 4, 5]
M = [[h[i + j] for j in range(3)] for i in range(3)]
q = [-1, 0, 1]
for s in (0, 1):
    exponent = 3 + s
    v = [h[exponent + i] for i in range(3)]
    recurrence = sum(left * right for left, right in zip(q, v))
    border_exponents = [0, 1, 2, exponent]
    border = [[h[i + j] for j in border_exponents] for i in border_exponents]
    assert det(border) == -(recurrence**2)

print(
    "RATE_HALF_SHAPE_A_BORDERED_HANKEL_FLAG_AUDIT_PASS",
    f"d={d} padding={g_off} regular={h_reg}",
)

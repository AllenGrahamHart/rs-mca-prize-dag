#!/usr/bin/env python3
"""Exact linear-algebra checks for the joint-window syzygy router."""


def rank(rows, q):
    a = [row[:] for row in rows]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = pow(a[r][c], q - 2, q)
        a[r] = [x * z % q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [(x - z * y) % q for x, y in zip(a[i], a[r])]
        r += 1
    return r


q = 17
Ru = [[1, 0, 2, 3], [0, 1, 4, 5]]
Rv_full = [[0, 0, 1, 0], [0, 0, 0, 1]]
Rv_def = [[0, 0, 1, 0], [1, 1, 7, 8]]

assert rank(Ru, q) == rank(Rv_full, q) == rank(Rv_def, q) == 2
assert rank(Ru + Rv_full, q) == 4
assert rank(Ru + Rv_def, q) == 3

# The deficient fixture has the genuinely two-sided relation
# row0(Ru)+row1(Ru)+row0(Rv)-row1(Rv)=0.
relation = [
    (Ru[0][i] + Ru[1][i] + Rv_def[0][i] - Rv_def[1][i]) % q
    for i in range(4)
]
assert relation == [0, 0, 0, 0]

# Proportional systems can be deficient algebraically, demonstrating why
# the tangent-gate exclusion is load-bearing.
assert rank(Ru + Ru, q) == 2

print("XR_JOINT_WINDOW_RANK_SYZYGY_ROUTER_ALL_PASS checks=6")

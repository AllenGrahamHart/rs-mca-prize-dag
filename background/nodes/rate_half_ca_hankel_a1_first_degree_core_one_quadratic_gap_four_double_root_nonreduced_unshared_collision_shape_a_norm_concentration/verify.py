#!/usr/bin/env python3
"""Replay the shape-A concentrated norm ledger."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def locator(roots):
    out = [1]
    for root in roots:
        out = mul(out, [-root, 1])
    return out


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
row_count = (9 * e - 7) // 2

require(2 * n == 3 * e - 7, "shape-A row degree")
require(row_count > e, "T interpolation margin")
require((e - 7) + e == 2 * e - 7, "norm residual split")

# Small exact product fixture for product(A H R)=L^m (X-x*)^r product(H).
blocks = ((1, 2), (2, 3), (3, 1))
hs = ((7,), (), (8,))
x_star = 5
rs = ((x_star,), (x_star,), ())
left = [1]
for block, h_roots, r_roots in zip(blocks, hs, rs):
    left = mul(left, mul(locator(block), mul(locator(h_roots), locator(r_roots))))
right = mul(locator((1, 2, 3)), locator((1, 2, 3)))
right = mul(right, mul(locator((x_star, x_star)), mul(locator((7,)), locator((8,)))))
require(left == right, "factor-product concentration fixture")

print(
    "RATE_HALF_SHAPE_A_NORM_CONCENTRATION_PASS "
    f"m={m} n={n} padding_degree={e-7} residual_degree_cap={e}"
)

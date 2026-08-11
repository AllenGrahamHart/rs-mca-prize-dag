#!/usr/bin/env python3
"""Finite-field audit of the dual-GRS polynomial representation."""


MOD = 101
U0 = list(range(1, 29))
P = 10
D = 19
MAX_DUAL_DEGREE = P - 3


def mul(values):
    out = 1
    for value in values:
        out = out * value % MOD
    return out


def derivative_value(roots, x):
    return mul((x - root) % MOD for root in roots if root != x)


weights = {x: pow(derivative_value(U0, x), -1, MOD) for x in U0}


def evaluate(coefficients, x):
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * x + coefficient) % MOD
    return out


def moment(coefficients, degree):
    return sum(
        weights[x] * evaluate(coefficients, x) * pow(x, degree, MOD)
        for x in U0
    ) % MOD


for coefficients in (
    [3],
    [2, 5, 7],
    [1, 0, 4, 0, 9, 2, 8, 6],
):
    assert len(coefficients) - 1 <= MAX_DUAL_DEGREE
    for degree in range(D + 1):
        assert moment(coefficients, degree) == 0

# The next domain degree fails at the top moment, pinning p-3 sharply.
tamper = [0] * (MAX_DUAL_DEGREE + 1) + [1]
assert moment(tamper, D) == 1

# A clean fiber is represented by its p-3 inside roots.
inside = set(U0[: MAX_DUAL_DEGREE])
inside_coefficients = [1]
for root in inside:
    updated = [0] * (len(inside_coefficients) + 1)
    for index, coefficient in enumerate(inside_coefficients):
        updated[index] = (updated[index] - root * coefficient) % MOD
        updated[index + 1] = (updated[index + 1] + coefficient) % MOD
    inside_coefficients = updated

assert len(inside_coefficients) - 1 == MAX_DUAL_DEGREE
assert all(evaluate(inside_coefficients, x) == 0 for x in inside)
assert all(moment(inside_coefficients, degree) == 0 for degree in range(D + 1))

print("RATE_HALF_QUADRATIC_EXTREMAL_DUAL_MDS_BIFORM_AUDIT_PASS")

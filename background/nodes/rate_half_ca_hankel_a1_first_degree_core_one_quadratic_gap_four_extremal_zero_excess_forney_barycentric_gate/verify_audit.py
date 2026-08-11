#!/usr/bin/env python3
"""Finite-field audit of both forms of the minimum-circuit identity."""


MOD = 101
D = list(range(80))
s0 = 0
U0 = list(range(1, 29))
U = {s0, *U0}


def mul(values):
    out = 1
    for value in values:
        out = out * value % MOD
    return out


def locator_value(roots, x):
    return mul((x - root) % MOD for root in roots)


def derivative_value(roots, x):
    return mul((x - root) % MOD for root in roots if root != x)


omega_derivative = {x: derivative_value(D, x) for x in D}

for rank_loss in (0, 1, 2):
    inside_size = 7 - rank_loss
    inside = set(U0[:inside_size])
    x_set = set(U0) - inside
    outside = set(range(29, 41))
    support = U | outside
    zeros = set(D) - support
    padded = set(range(41, 41 + rank_loss))

    assert len(outside) == 12
    assert len(x_set) == 21 + rank_loss
    assert len(zeros) == 39

    constant_values = set()
    simplified_values = set()
    for x in x_set:
        g_x = locator_value(zeros, x)
        dual_x = pow(omega_derivative[x], -1, MOD)
        source_x = (x - s0) * dual_x * g_x % MOD
        q_x = locator_value(inside | outside, x)
        r_x = locator_value(padded, x)
        full_q_x = q_x * r_x % MOD
        lx_prime = derivative_value(x_set, x)
        lu_prime = derivative_value(U0, x)
        b_x = locator_value(outside, x)

        normalized = source_x * full_q_x * lx_prime * pow(r_x, -1, MOD)
        constant_values.add(normalized % MOD)
        simplified_values.add(source_x * b_x * lu_prime % MOD)

    assert len(constant_values) == 1
    assert simplified_values == constant_values
    assert next(iter(constant_values)) != 0

print("RATE_HALF_QUADRATIC_EXTREMAL_FORNEY_BARYCENTRIC_AUDIT_PASS")

#!/usr/bin/env python3
"""Replay the center-adjusted heavy-row residual ledger."""

PRIME = 101


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


def divide(dividend, divisor):
    work = dividend[:]
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], PRIME - 2, PRIME)
    while len(work) >= len(divisor):
        coefficient = work[-1] * inverse % PRIME
        shift = len(work) - len(divisor)
        quotient[shift] = coefficient
        for i, value_i in enumerate(divisor):
            work[shift + i] = (work[shift + i] - coefficient * value_i) % PRIME
        while work and work[-1] == 0:
            work.pop()
    return quotient, work


def value(poly, point):
    return sum(
        coefficient * pow(point, power, PRIME)
        for power, coefficient in enumerate(poly)
    ) % PRIME


e = 11
tau = 17
roots = (2, 3, 5, 7, 11)
g_star = [1]
for root in roots:
    g_star = multiply(g_star, [(-root) % PRIME, 1])
s_b = multiply([(-tau) % PRIME, 1], [(-tau) % PRIME, 1])

checks = 0
for d_a in (0, 1):
    center_roots = roots[:d_a]
    off_roots = roots[d_a:]
    j_star = [1]
    for root in center_roots:
        j_star = multiply(j_star, [(-root) % PRIME, 1])
    g_off, remainder = divide(g_star, j_star)
    require(not remainder, "center factor division")

    residual = [1]
    for root in (23, 31) + ((37,) if d_a else ()):
        residual = multiply(residual, [(-root) % PRIME, 1])
    h_row = multiply(g_off, s_b)
    heavy_row = multiply(h_row, residual)

    require(len(j_star) - 1 == d_a, "center degree")
    require(len(g_off) - 1 == e - 6 - d_a, "off-line degree")
    require(len(h_row) - 1 == e - 4 - d_a, "row modulus degree")
    require(len(heavy_row) - 1 == e - 2, "exact heavy-row degree")
    checks += 4

    quotient, remainder = divide(heavy_row, h_row)
    require(not remainder and quotient == residual, "exact quotient")
    require(len(quotient) - 1 == 2 + d_a, "residual degree")
    require(value(quotient, tau) != 0, "correction coprimality")
    checks += 3

    for root in off_roots:
        require(value(heavy_row, root) == 0, "off-line padded root")
        checks += 1
    for root in center_roots:
        require(value(heavy_row, root) != 0, "center was falsely retained")
        checks += 1

    require(value(g_star, tau) != 0, "unshared root")
    require(value(heavy_row, tau) == 0, "correction root")
    require(value(residual, tau) != 0, "residual correction unit")
    checks += 3

print(f"RATE_HALF_NONREDUCED_HEAVY_ROW_CENTER_ADJUSTED_PASS checks={checks}")

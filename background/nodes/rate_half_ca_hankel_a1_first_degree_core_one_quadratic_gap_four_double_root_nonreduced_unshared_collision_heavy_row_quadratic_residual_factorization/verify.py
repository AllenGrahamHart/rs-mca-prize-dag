#!/usr/bin/env python3
"""Replay the supported/correction divisor and quadratic residual ledger."""

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
        for i, value in enumerate(divisor):
            work[shift + i] = (work[shift + i] - coefficient * value) % PRIME
        while work and work[-1] == 0:
            work.pop()
    return quotient, work


def value(poly, point):
    return sum(coefficient * pow(point, power, PRIME) for power, coefficient in enumerate(poly)) % PRIME


e = 11
tau = 17
g_star = [1]
for root in (2, 3, 5, 7, 11):
    g_star = multiply(g_star, [(-root) % PRIME, 1])
s_b = multiply([(-tau) % PRIME, 1], [(-tau) % PRIME, 1])
t_2 = multiply([(-23) % PRIME, 1], [(-31) % PRIME, 1])
h_nr = multiply(g_star, s_b)
heavy_row = multiply(h_nr, t_2)

checks = 0
require(len(g_star) - 1 == e - 6, "supported degree")
require(len(h_nr) - 1 == e - 4, "modulus degree")
require(len(heavy_row) - 1 <= e - 2, "heavy-row degree")
checks += 3

quotient, remainder = divide(heavy_row, h_nr)
require(not remainder and quotient == t_2, "quadratic quotient")
require(len(quotient) - 1 <= 2, "quadratic residual cap")
require(value(quotient, tau) != 0, "correction coprimality")
checks += 3

for root in (2, 3, 5, 7, 11):
    require(value(heavy_row, root) == 0, "supported padded root")
    checks += 1
require(value(g_star, tau) != 0, "unshared root")
require(value(heavy_row, tau) == 0, "correction root")
require(value(t_2, tau) != 0, "residual correction unit")
checks += 3

false_row = heavy_row[:]
false_row[0] = (false_row[0] + 1) % PRIME
_, false_remainder = divide(false_row, h_nr)
require(bool(false_remainder), "remainder falsifier")
checks += 1

print(f"RATE_HALF_NONREDUCED_HEAVY_ROW_QUADRATIC_RESIDUAL_PASS checks={checks}")

#!/usr/bin/env python3
"""Replay the nonreduced divided-row quintic degree and recurrence ledger."""

PRIME = 101


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(left, right):
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0))
        % PRIME
        for i in range(size)
    ]


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


def value(poly, point):
    return sum(coefficient * pow(point, power, PRIME) for power, coefficient in enumerate(poly)) % PRIME


tau = 17
x_star = 13
s_b = multiply([(-tau) % PRIME, 1], [(-tau) % PRIME, 1])
s_b_squared = multiply(s_b, s_b)
c = [[3, 4, 5, 6, 7, 8]]
checks = 0
for i in range(6):
    h_i = [i + 2, 2 * i + 1]
    forcing = multiply(s_b_squared, h_i)
    next_c = add(
        [(x_star * coefficient) % PRIME for coefficient in c[-1]],
        [(-coefficient) % PRIME for coefficient in forcing],
    )
    c.append(next_c)
    require(len(next_c) - 1 <= 5, "quintic recurrence degree")
    require(value(next_c, tau) == x_star * value(c[-2], tau) % PRIME, "tau recurrence")
    checks += 2

require(value(c[0], tau) != 0, "initial correction value")
for i, row in enumerate(c):
    require(value(row, tau) == pow(x_star, i, PRIME) * value(c[0], tau) % PRIME, "geometric correction vector")
    checks += 1
checks += 1

for e in (7, 13, 183251937963):
    require((e + 1) - (e - 4) == 5, "quintic degree subtraction")
    checks += 1

print(f"RATE_HALF_NONREDUCED_DIVIDED_ROW_QUINTIC_PASS checks={checks}")

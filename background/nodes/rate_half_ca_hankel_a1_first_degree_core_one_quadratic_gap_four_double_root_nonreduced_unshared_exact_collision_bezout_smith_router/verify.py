#!/usr/bin/env python3
"""Exact truncated-polynomial replay of the collision Smith router."""


def add(left, right, prime=101):
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = (out.get(exponent, 0) + coefficient) % prime
        if out[exponent] == 0:
            del out[exponent]
    return out


def multiply(left, right, prime=101):
    out = {}
    for i, x in left.items():
        for j, y in right.items():
            out[i + j] = (out.get(i + j, 0) + x * y) % prime
    return {i: x for i, x in out.items() if x}


def scale(poly, scalar, prime=101):
    return {i: scalar * x % prime for i, x in poly.items() if scalar * x % prime}


def valuation(poly):
    return min(poly) if poly else 10**9


def require(condition, message):
    if not condition:
        raise AssertionError(message)


z2 = {2: 1}
fixtures = {
    "two_unramified": ({3: -3}, {6: 2}),
    "one_ramified": ({3: -2}, {6: 1, 7: -1}),
}
checks = 0
for name, (c1, c0) in fixtures.items():
    c1 = {i: x % 101 for i, x in c1.items()}
    c0 = {i: x % 101 for i, x in c0.items()}
    require(valuation(c1) >= 3 and valuation(c0) == 6, name)
    for order_a in range(0, 7):
        a = {order_a: 1}
        matrix = (
            (z2, scale(multiply(a, c0), -1)),
            (a, add(z2, scale(multiply(a, c1), -1))),
        )
        determinant = add(
            multiply(z2, matrix[1][1]),
            multiply(a, multiply(a, c0)),
        )
        require(valuation(determinant) == 4, f"determinant {name} a={order_a}")
        first = min(valuation(entry) for row in matrix for entry in row)
        profile = (first, 4 - first)
        if order_a == 0:
            require(profile == (0, 4), "corank-one rejected branch")
        elif order_a == 1:
            require(profile == (1, 3), "first-order profile")
        else:
            require(profile == (2, 2), "second-order profile")
        checks += 1

print(f"RATE_HALF_NONREDUCED_COLLISION_BEZOUT_SMITH_PASS checks={checks}")

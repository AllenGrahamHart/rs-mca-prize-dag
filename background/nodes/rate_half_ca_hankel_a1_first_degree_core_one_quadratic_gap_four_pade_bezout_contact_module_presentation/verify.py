#!/usr/bin/env python3
"""Finite-field and integral replays of the Pade-Bezout presentation."""

from fractions import Fraction
from itertools import combinations
from random import Random


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def det_mod(matrix, prime):
    a = [row[:] for row in matrix]
    out = 1
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col] % prime), None)
        require(pivot is not None, "unexpected singular matrix")
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        value = a[col][col] % prime
        out = out * value % prime
        inverse = pow(value, -1, prime)
        for row in range(col + 1, len(a)):
            factor = a[row][col] * inverse % prime
            for j in range(col, len(a)):
                a[row][j] = (a[row][j] - factor * a[col][j]) % prime
    return out % prime


def evaluate(coefficients, value, prime):
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * value + coefficient) % prime
    return out


def det_integer(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    out = Fraction(1)
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        value = a[col][col]
        out *= value
        for row in range(col + 1, len(a)):
            factor = a[row][col] / value
            for j in range(col, len(a)):
                a[row][j] -= factor * a[col][j]
    require(out.denominator == 1, "integral determinant")
    return out.numerator


def valuation(value, prime):
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def smith_valuations(matrix, prime):
    size = len(matrix)
    previous = 0
    out = []
    for minor_size in range(1, size + 1):
        best = 10**9
        for rows in combinations(range(size), minor_size):
            for columns in combinations(range(size), minor_size):
                minor = [[matrix[i][j] for j in columns] for i in rows]
                best = min(best, valuation(det_integer(minor), prime))
        out.append(best - previous)
        previous = best
    return out


def bezout_matrix(q, pade):
    degree = len(q) - 1
    p = pade + [0] * (degree + 1 - len(pade))
    return [[
        sum(
            q[row + 1 + k] * p[column - k]
            - p[row + 1 + k] * q[column - k]
            for k in range(column + 1)
            if row + 1 + k <= degree
        )
        for column in range(degree)
    ] for row in range(degree)]


def multiplication_matrix(q, pade):
    degree = len(q) - 1
    p = pade + [0] * (degree - len(pade))
    columns = []
    polynomial = p[:]
    for _ in range(degree):
        columns.append(polynomial + [0] * (degree - len(polynomial)))
        following = [0] + polynomial
        while len(following) > degree:
            leading = following.pop()
            for i in range(degree):
                following[i] -= leading * q[i]
        polynomial = following
    return [[columns[j][i] for j in range(degree)] for i in range(degree)]


checks = 0
for prime in (101, 127):
    rng = Random(prime)
    for degree in range(1, 7):
        for trial in range(12):
            q = [rng.randrange(prime) for _ in range(degree)]
            q.append(rng.randrange(1, prime))
            moments = [rng.randrange(prime) for _ in range(degree)]
            for shift in range(degree - 1):
                tail = -sum(q[j] * moments[shift + j] for j in range(degree))
                moments.append(tail * pow(q[-1], -1, prime) % prime)

            transform = [
                [q[i + j + 1] % prime if i + j + 1 <= degree else 0
                 for j in range(degree)]
                for i in range(degree)
            ]
            hankel = [
                [moments[i + j] % prime for j in range(degree)]
                for i in range(degree)
            ]
            gram = [[0] * degree for _ in range(degree)]
            for i in range(degree):
                for j in range(degree):
                    gram[i][j] = sum(
                        transform[i][u] * hankel[u][v] * transform[j][v]
                        for u in range(degree) for v in range(degree)
                    ) % prime

            pade = [
                sum(transform[i][j] * moments[j] for j in range(degree)) % prime
                for i in range(degree)
            ]
            expected_det = pow(q[-1], degree, prime)
            require(det_mod(transform, prime) in
                    {expected_det, (-expected_det) % prime}, "det(T_Q)")

            for _ in range(16):
                x = rng.randrange(prime)
                y = rng.randrange(prime)
                if x == y:
                    y = (y + 1) % prime
                qx = evaluate(q, x, prime)
                qy = evaluate(q, y, prime)
                px = evaluate(pade, x, prime)
                py = evaluate(pade, y, prime)
                bez_value = (qx * py - px * qy) * pow(x - y, -1, prime) % prime
                gram_value = sum(
                    gram[i][j] * pow(x, i, prime) * pow(y, j, prime)
                    for i in range(degree) for j in range(degree)
                ) % prime
                require(bez_value == gram_value, "Bezout Gram identity")
                checks += 1

print(f"RATE_HALF_PADE_BEZOUT_CONTACT_MODULE_PASS checks={checks}")

integral_checks = 0
rng = Random(176)
for degree in range(1, 5):
    for _ in range(30):
        q = [rng.randrange(-10, 11) for _ in range(degree)] + [1]
        pade = [rng.randrange(-10, 11) for _ in range(degree)]
        bezout = bezout_matrix(q, pade)
        multiplication = multiplication_matrix(q, pade)
        for prime in (2, 3, 5):
            if det_integer(bezout) == 0 or det_integer(multiplication) == 0:
                continue
            require(
                smith_valuations(bezout, prime)
                == smith_valuations(multiplication, prime),
                "Bezout/multiplication Smith mismatch",
            )
            integral_checks += 1

print(f"RATE_HALF_PADE_BEZOUT_MODULE_SMITH_PASS checks={integral_checks}")

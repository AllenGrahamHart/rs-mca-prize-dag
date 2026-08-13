#!/usr/bin/env python3
"""Verify the truncated-source/minimal-recurrence separation counterexample."""

PRIME = 101
D = 13
U = list(range(1, 20))
CERTIFICATES = {
    1: [
        19, 6, 47, 37, 31, 62, 4, 97, 45, 45, 10, 55, 19, 38, 15, 77,
        48, 13, 31, 15, 14, 72, 34, 58, 80, 84, 20, 3, 7, 98, 28,
    ],
    2: [
        17, 65, 86, 42, 83, 10, 82, 77, 54, 30, 27, 1, 42, 83, 12, 52,
        41, 80, 17, 68, 91, 8, 26, 26, 17, 54, 22, 81, 40, 80,
    ],
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rank_mod(matrix):
    work = [row[:] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (i for i in range(row, len(work)) if work[i][column] % PRIME),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, PRIME)
        work[row] = [value * inverse % PRIME for value in work[row]]
        for i in range(row + 1, len(work)):
            factor = work[i][column] % PRIME
            if factor:
                work[i] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(work[i], work[row])
                ]
        row += 1
    return row


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


def locator(points):
    out = [1]
    for point in points:
        out = multiply(out, [(-point) % PRIME, 1])
    return out


def evaluate(polynomial, point):
    out = 0
    for coefficient in reversed(polynomial):
        out = (out * point + coefficient) % PRIME
    return out


checks = 0
for regular_corank, certificate in CERTIFICATES.items():
    compressed_size = D - regular_corank
    compressed = list(range(30, 30 + compressed_size))
    points = U + compressed
    require(len(certificate) == len(points), "certificate length")
    require(all(certificate), "zero certificate coordinate")
    require(set(U).isdisjoint(compressed), "supports overlap")

    for power in range(2 * D + 1):
        require(
            sum(
                weight * pow(point, power, PRIME)
                for weight, point in zip(certificate, points)
            ) % PRIME == 0,
            f"moment transfer power {power}",
        )
        checks += 1

    source_weights = certificate[:len(U)]
    moments = [
        sum(
            weight * pow(point, power, PRIME)
            for weight, point in zip(source_weights, U)
        ) % PRIME
        for power in range(2 * D + 1)
    ]
    hankel = [[moments[i + j] for j in range(D + 1)] for i in range(D + 1)]
    require(rank_mod(hankel) == compressed_size, "Hankel rank")

    minimal = locator(compressed)
    x_star = compressed[0]
    require(x_star not in U and evaluate(minimal, x_star) == 0, "separation")
    for shift in range(regular_corank + 1):
        vector = [0] * shift + minimal + [0] * (regular_corank - shift)
        require(len(vector) == D + 1, "kernel vector length")
        require(
            all(
                sum(hankel[i][j] * vector[j] for j in range(D + 1))
                % PRIME == 0
                for i in range(D + 1)
            ),
            "kernel ideal",
        )

    multiplier = [(-x_star) % PRIME, 1]
    if regular_corank == 2:
        multiplier = multiply(multiplier, [(-90) % PRIME, 1])
    q = multiply(minimal, multiplier)
    derivative = [(i * q[i]) % PRIME for i in range(1, len(q))]
    second = [(i * derivative[i]) % PRIME for i in range(1, len(derivative))]
    require(len(q) == D + 1, "Q degree")
    require(evaluate(q, x_star) == evaluate(derivative, x_star) == 0, "double root")
    require(evaluate(second, x_star) != 0, "root not exact double")
    checks += 5

print(f"RATE_HALF_TRUNCATED_SOURCE_SEPARATION_REFUTED checks={checks}")

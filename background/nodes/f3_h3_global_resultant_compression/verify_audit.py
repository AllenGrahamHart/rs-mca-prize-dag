#!/usr/bin/env python3
"""Independent modular Sylvester audit of the resultant identities."""

from __future__ import annotations

from math import comb


def trim(poly: list[int], prime: int) -> list[int]:
    poly = [value % prime for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def determinant(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    answer = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        value = work[column][column]
        answer = answer * value % prime
        inverse = pow(value, prime - 2, prime)
        for row in range(column + 1, len(work)):
            scale = work[row][column] * inverse % prime
            if scale:
                work[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(work[row], work[column])
                ]
    return answer % prime


def sylvester_resultant(f: list[int], g: list[int], prime: int) -> int:
    f, g = trim(f, prime), trim(g, prime)
    m, n = len(f) - 1, len(g) - 1
    f_high, g_high = list(reversed(f)), list(reversed(g))
    size = m + n
    matrix: list[list[int]] = []
    for shift in range(n):
        row = [0] * size
        row[shift : shift + m + 1] = f_high
        matrix.append(row)
    for shift in range(m):
        row = [0] * size
        row[shift : shift + n + 1] = g_high
        matrix.append(row)
    return determinant(matrix, prime)


def subgroup_generator(order: int, prime: int) -> int:
    for value in range(2, prime):
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1:
            return value
    raise AssertionError("no generator")


def evaluate_product(values: list[int], prime: int) -> int:
    answer = 1
    for value in values:
        answer = answer * value % prime
    return answer


def audit_order(n: int, prime: int) -> int:
    d = n - 1
    f = [((-1) ** j * comb(n, j)) % prime for j in range(1, n + 1)]
    generator = subgroup_generator(n, prime)
    roots = [(1 - pow(generator, exponent, prime)) % prime for exponent in range(1, n)]
    assert len(set(roots)) == d
    checks = 0

    for target in (2, 3, 5):
        product_poly = [0] * (d + 1)
        for degree, coefficient in enumerate(f):
            product_poly[d - degree] = coefficient * pow(target, degree, prime) % prime
        direct = evaluate_product(
            [(target - left * right) % prime for left in roots for right in roots], prime
        )
        assert sylvester_resultant(f, product_poly, prime) == direct
        checks += 1

        quotient_poly = [
            coefficient * pow(target, degree, prime) % prime
            for degree, coefficient in enumerate(f)
        ]
        quotient_all = sylvester_resultant(f, quotient_poly, prime)
        quotient_off = evaluate_product(
            [
                (left * target - right) % prime
                for i, left in enumerate(roots)
                for j, right in enumerate(roots)
                if i != j
            ],
            prime,
        )
        assert quotient_all == n * pow(target - 1, d, prime) * quotient_off % prime
        checks += 1

    c, e = roots[0], roots[1]
    for parameter in (0, 1, 4):
        y = (e + c * parameter) % prime
        h = [0] * (d + 1)
        for degree, coefficient in enumerate(f):
            h[d - degree] = (
                coefficient * pow(y, degree, prime) * pow(c, d - degree, prime)
            ) % prime
        direct = evaluate_product(
            [(e + c * parameter - c * left * right) % prime for left in roots for right in roots],
            prime,
        )
        assert sylvester_resultant(f, h, prime) == direct
        checks += 1
    return checks


def main() -> None:
    checks = sum(audit_order(n, prime) for n, prime in ((4, 17), (8, 17), (16, 97)))
    print(
        "AUDIT_F3_H3_GLOBAL_RESULTANT_COMPRESSION_PASS "
        f"orders=4,8,16 modular_determinants={checks}"
    )


if __name__ == "__main__":
    main()

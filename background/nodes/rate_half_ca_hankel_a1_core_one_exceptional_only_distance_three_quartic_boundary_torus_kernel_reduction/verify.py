#!/usr/bin/env python3
"""Exact finite-field controls for the quartic torus-kernel matrix."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int], prime: int) -> list[int]:
    while len(poly) > 1 and poly[-1] % prime == 0:
        poly.pop()
    return [value % prime for value in poly]


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out, prime)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly], prime)


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out, prime)


def locator(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def evaluate(poly: list[int], point: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * point + coefficient) % prime
    return out


def derivative(poly: list[int], prime: int) -> list[int]:
    return [index * poly[index] % prime for index in range(1, len(poly))] or [0]


def divide_exact(numerator: list[int], denominator: list[int], prime: int) -> list[int]:
    work = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, prime)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] * inverse_lead % prime
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[shift + index] = (
                work[shift + index] - coefficient * value
            ) % prime
    require(not any(work[: len(denominator) - 1]), "nonexact division")
    return trim(quotient, prime)


def prime_factors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("no primitive root")


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank or work[row][column] == 0:
                continue
            scalar = work[row][column]
            work[row] = [
                (value - scalar * pivot_value) % prime
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def build_control(e: int, prime: int) -> tuple[int, int, bool]:
    domain_order = 8 * e + 8
    require((prime - 1) % domain_order == 0, "domain order does not divide field order")
    generator = pow(
        primitive_root(prime), (prime - 1) // domain_order, prime
    )
    domain: list[int] = []
    value = 1
    for _ in range(domain_order):
        domain.append(value)
        value = value * generator % prime
    require(value == 1 and len(set(domain)) == domain_order, "bad subgroup")

    s, x_0 = domain[:2]
    pairs = [tuple(domain[2 + 2 * k : 4 + 2 * k]) for k in range(e)]
    triple = tuple(domain[2 + 2 * e : 5 + 2 * e])
    b_poly = locator(triple, prime)
    d_polys = [locator(pair, prime) for pair in pairs]

    internal = list(range(2, e + 2))
    lambdas = [(11 + 2 * index) % prime or 1 for index in range(e)]
    i_poly = locator(tuple(internal), prime)
    i_prime = derivative(i_poly, prime)
    l_basis = [
        scale(
            locator(
                tuple(point for other, point in enumerate(internal) if other != index),
                prime,
            ),
            pow(evaluate(i_prime, xi, prime), -1, prime),
            prime,
        )
        for index, xi in enumerate(internal)
    ]
    w_basis = {
        (i, k): divide_exact(
            l_basis[i], [(-internal[k]) % prime, 1], prime
        )
        for i in range(e)
        for k in range(e)
        if i != k
    }

    q_e_values: dict[tuple[int, int], int] = {}
    for k, pair in enumerate(pairs):
        for row in pair:
            a_over_d = 1
            for other, d_poly in enumerate(d_polys):
                if other != k:
                    a_over_d = a_over_d * evaluate(d_poly, row, prime) % prime
            q_e_values[k, row] = (
                evaluate(b_poly, row, prime)
                * lambdas[k]
                * pow(
                    internal[k] * evaluate(i_prime, internal[k], prime),
                    -1,
                    prime,
                )
                * a_over_d
            ) % prime

    matrix: list[list[int]] = []
    for moment in range(2 * e - 5):
        coefficient_rows = [[0] * e for _ in range(e - 1)]
        for i in range(e):
            for k, pair in enumerate(pairs):
                if i == k:
                    continue
                trace = 0
                for row in pair:
                    q_value = q_e_values[k, row]
                    trace += (
                        pow(row, moment + 1, prime)
                        * (row - s)
                        * (row - x_0)
                        * evaluate(b_poly, row, prime)
                        * pow(q_value, 3, prime)
                        * pow(evaluate(d_polys[i], row, prime), 2, prime)
                    )
                trace = trace * pow(internal[i] - internal[k], -1, prime) % prime
                for z_degree, coefficient in enumerate(w_basis[i, k]):
                    coefficient_rows[z_degree][i] = (
                        coefficient_rows[z_degree][i] + trace * coefficient
                    ) % prime
        matrix.extend(coefficient_rows)

    # Independently reconstruct QTK3 and QBM2 for an arbitrary torus vector.
    theta = [index + 3 for index in range(e)]
    direct_rows: list[int] = []
    for moment in range(2 * e - 5):
        direct_coefficients = [0] * (e - 1)
        for k, pair in enumerate(pairs):
            for row in pair:
                v_row = [0]
                q_value = q_e_values[k, row]
                for i in range(e):
                    if i == k:
                        continue
                    scalar = (
                        -q_value
                        * theta[i]
                        * pow(evaluate(d_polys[i], row, prime), 2, prime)
                        * pow(internal[i] - internal[k], -1, prime)
                    ) % prime
                    v_row = add(v_row, scale(w_basis[i, k], scalar, prime), prime)
                weight = (
                    pow(row, moment + 1, prime)
                    * (row - s)
                    * (row - x_0)
                    * evaluate(b_poly, row, prime)
                    * pow(q_value, 2, prime)
                ) % prime
                for z_degree, coefficient in enumerate(v_row):
                    direct_coefficients[z_degree] = (
                        direct_coefficients[z_degree] + weight * coefficient
                    ) % prime
        direct_rows.extend(direct_coefficients)

    require(len(direct_rows) == len(matrix), "row count mismatch")
    for direct, row in zip(direct_rows, matrix, strict=True):
        product = sum(value * label for value, label in zip(row, theta, strict=True))
        require(direct == -product % prime, "linear moment factorization mismatch")

    rank = matrix_rank(matrix, prime)
    deletion_ranks = [
        matrix_rank(
            [row[:column] + row[column + 1 :] for row in matrix], prime
        )
        for column in range(e)
    ]
    torus_eligible = rank < e and all(value == rank for value in deletion_ranks)
    return len(matrix), rank, torus_eligible


def main() -> None:
    expected = {
        (3, 97): (2, 2, True),
        (4, 241): (9, 4, False),
        (5, 97): (20, 5, False),
        (7, 193): (54, 7, False),
    }
    observed = {
        key: build_control(*key)
        for key in expected
    }
    require(observed == expected, "unexpected torus-kernel control ranks")
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_TORUS_KERNEL_PASS "
        f"controls={observed} e3_dimension_fence=True e4_plus_full_rank=True"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact controls for the bounded-error Pade-circuit reduction."""

from __future__ import annotations

from itertools import permutations
from math import comb


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly])


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def locator(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [-root % prime, 1], prime)
    return out


def lagrange(index: int, points: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    denominator = 1
    for other, point in enumerate(points):
        if other == index:
            continue
        out = mul(out, [-point % prime, 1], prime)
        denominator = denominator * (points[index] - point) % prime
    return scale(out, pow(denominator, -1, prime), prime)


def determinant(matrix: list[list[list[int]]], prime: int) -> list[int]:
    size = len(matrix)
    out = [0]
    for perm in permutations(range(size)):
        inversions = sum(
            1
            for left in range(size)
            for right in range(left + 1, size)
            if perm[left] > perm[right]
        )
        term = [1]
        for row, column in enumerate(perm):
            term = mul(term, matrix[row][column], prime)
        out = add(out, scale(term, -1 if inversions % 2 else 1, prime), prime)
    return trim(out)


def circuit_fixture() -> tuple[int, int, int]:
    prime = 101
    internal = (1, 2, 3, 4)
    i_poly = locator(internal, prime)
    fixture: tuple[int, list[int], list[int], list[int]] | None = None

    for u in range(5, 18):
        q_poly = [u * u % prime, -2 * u % prime, 1]
        for root in range(20, 34):
            g_poly = [-root % prime, 1]
            for a_0 in range(8):
                for a_1 in range(1, 9):
                    a_poly = [a_0, a_1]
                    k_poly = add(mul(i_poly, a_poly, prime), mul(g_poly, q_poly, prime), prime)
                    roots = [x for x in range(prime) if evaluate(k_poly, x, prime) == 0]
                    if len(k_poly) == 6 and len(roots) == 5 and not set(roots) & set(internal):
                        fixture = (u, a_poly, g_poly, roots)
                        break
                if fixture is not None:
                    break
            if fixture is not None:
                break
        if fixture is not None:
            break
    need(fixture is not None, "failed to find split synthetic complement")
    u, a_poly, g_poly, roots = fixture

    selected = roots[:4]
    matrix: list[list[list[int]]] = []
    kernel = a_poly + g_poly
    for gamma in selected:
        i_value = evaluate(i_poly, gamma, prime)
        need(i_value != 0, "external fixture met the internal locator")
        inverse = pow(i_value, -1, prime)
        q_gamma = scale([gamma * gamma % prime, -2 * gamma % prime, 1], inverse, prime)
        matrix.append([[1], [gamma], q_gamma, scale(q_gamma, gamma, prime)])
        row_value = sum(
            evaluate(entry, u, prime) * coefficient
            for entry, coefficient in zip(matrix[-1], kernel)
        ) % prime
        need(row_value == 0, "selected root did not give the Pade kernel")

    delta = determinant(matrix, prime)
    need(delta != [0], "fixture circuit was identically singular")
    need(len(delta) - 1 <= 4, "fixture determinant exceeded degree four")
    need(evaluate(delta, u, prime) == 0, "fixture orbit did not annul determinant")
    determinant_roots = sum(
        1 for value in range(prime) if evaluate(delta, value, prime) == 0
    )
    need(determinant_roots <= 4, "nonzero determinant had too many roots")
    return len(roots), len(delta) - 1, determinant_roots


def tail_norm_fixture() -> int:
    prime = 101
    internal = (2, 3, 5, 7)
    orbit_coordinates = (11, 13, 17)
    norms = [
        [value * value % prime, -2 * value % prime, 1]
        for value in orbit_coordinates
    ]
    norms.append([5, 3, 2])
    discriminant = (3 * 3 - 4 * 2 * 5) % prime
    need(discriminant != 0, "tail norm accidentally became a square")
    weights = (19, 23, 29, 31)
    bases = [lagrange(index, internal, prime) for index in range(len(internal))]

    moments: list[list[int]] = []
    for norm_coefficient in (2, 1, 0):
        polynomial = [0]
        for index, basis in enumerate(bases):
            coefficient = weights[index] * norms[index][norm_coefficient] % prime
            if norm_coefficient == 1:
                coefficient = -coefficient * pow(2, -1, prime) % prime
            polynomial = add(polynomial, scale(basis, coefficient, prime), prime)
        moments.append(polynomial)

    for index, point in enumerate(internal):
        for u in (37, 41, 43):
            reconstructed = (
                u * u * evaluate(moments[0], point, prime)
                - 2 * u * evaluate(moments[1], point, prime)
                + evaluate(moments[2], point, prime)
            ) % prime
            expected = weights[index] * evaluate(norms[index], u, prime) % prime
            need(reconstructed == expected, "tail norm interpolation failed")
    return discriminant


def official_counts() -> tuple[int, int]:
    e = 2**38 - 1
    outputs = []
    for tail, boundary_loss, numerator, denominator in (
        (6, 2, 9999, 10000),
        (8, 3, 991, 1000),
    ):
        size = 2 * (tail + 1)
        orbit_count = 3 * e - tail - boundary_loss
        all_subsets = comb(3 * e, size)
        own_subsets = comb(e, size)
        degree = 2 * (tail + 1)
        lower_numerator = orbit_count * own_subsets - degree * all_subsets
        lower_denominator = orbit_count - degree
        need(lower_numerator > 0 and lower_denominator > 0, "vacuous circuit count")
        lower = (lower_numerator + lower_denominator - 1) // lower_denominator
        need(denominator * lower > numerator * own_subsets, "official ratio failed")
        outputs.append(len(str(lower)))
    return outputs[0], outputs[1]


def main() -> None:
    fixture = circuit_fixture()
    tail_discriminant = tail_norm_fixture()
    digits = official_counts()
    print(
        "RATE_HALF_DISTANCE_THREE_BOUNDED_ERROR_PADE_CIRCUIT_PASS "
        f"fixture={fixture} tail_discriminant={tail_discriminant} "
        f"lower_bound_digits={digits} "
        "ratios=(9999/10000,991/1000)"
    )


if __name__ == "__main__":
    main()

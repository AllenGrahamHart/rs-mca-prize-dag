#!/usr/bin/env python3
"""Replay the H3 double-accident joint-ideal router."""

from __future__ import annotations

import json
from functools import reduce
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_low_distance_joint_ideal_router"
DEPENDENCIES = {
    "f3_h3_cutoff18_double_accident_reduction",
    "f3_h3_low_distance_ideal_star_router",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_mobius_excess_half"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def subtract(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (left[index] if index < len(left) else 0) - (
            right[index] if index < len(right) else 0
        )
    return trim(out)


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = trim(dividend[:])
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor):
        assert divisor[-1] in (1, -1)
        coefficient = work[-1] // divisor[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift + index] -= coefficient * value
        trim(work)
    assert work == [0] or not work
    return trim(quotient)


def shifted(exponent: int) -> list[int]:
    return [1] + [0] * (exponent - 1) + [-1]


def beta(pair: tuple[int, int]) -> list[int]:
    return multiply(shifted(pair[0]), shifted(pair[1]))


def reduce_cyclotomic(poly: list[int], n: int) -> list[int]:
    degree = n // 2
    out = [0] * degree
    for exponent, coefficient in enumerate(poly):
        quotient, remainder = divmod(exponent, degree)
        out[remainder] += coefficient * (-1 if quotient % 2 else 1)
    return trim(out)


def evaluate(poly: list[int], value: int, modulus: int) -> int:
    total = 0
    for coefficient in reversed(poly):
        total = (total * value + coefficient) % modulus
    return total


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                row for row in range(pivot_index + 1, size)
                if work[row][pivot_index] != 0
            )
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]
                assert numerator % previous == 0
                work[row][column] = numerator // previous
        previous = pivot
    return sign * work[-1][-1]


def principal_norm(poly: list[int], n: int) -> int:
    degree = n // 2
    element = reduce_cyclotomic(poly, n)
    if element == [0]:
        return 0
    columns: list[list[int]] = []
    for shift in range(degree):
        shifted_element = [0] * shift + element
        reduced = reduce_cyclotomic(shifted_element, n)
        columns.append(reduced + [0] * (degree - len(reduced)))
    matrix = [[columns[column][row] for column in range(degree)] for row in range(degree)]
    return abs(bareiss_determinant(matrix))


def half_vector(pair: tuple[int, int], n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for exponent, coefficient in ((sum(pair), 1), (pair[0], -1), (pair[1], -1)):
        exponent %= n
        coordinate = exponent % (n // 2)
        sign = 1 if exponent < n // 2 else -1
        out[coordinate] = out.get(coordinate, 0) + coefficient * sign
    return {coordinate: value for coordinate, value in out.items() if value}


def squared_norm(vector: dict[int, int]) -> int:
    return sum(value * value for value in vector.values())


def squared_distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in set(left) | set(right)
    )


def finite_fixture() -> tuple[list[int], int]:
    # Exact official toy row found by a tiny deterministic scan.
    n, p, generator, target = 32, 1153, 194, 230
    star = ((2, 25), (5, 10), (6, 8))
    quotient_lifts = ((9, 4), (23, 26))
    assert p % n == 1 and p >= n * n
    assert pow(generator, n, p) == 1 and pow(generator, n // 2, p) == p - 1
    assert target != 1

    vectors = [half_vector(pair, n) for pair in star]
    assert [squared_norm(vector) for vector in vectors] == [3, 3, 3]
    assert squared_distance(vectors[0], vectors[1]) == 6
    assert squared_distance(vectors[0], vectors[2]) == 6

    products = [beta(pair) for pair in star]
    assert [evaluate(poly, generator, p) for poly in products] == [target] * 3

    quotient_values = []
    for u, v in quotient_lifts:
        c_value = evaluate(shifted(u), generator, p)
        d_value = evaluate(shifted(v), generator, p)
        quotient_values.append(d_value * pow(c_value, -1, p) % p)
    assert quotient_values == [target, target]

    pi = [1, -1]
    pi_squared = multiply(pi, pi)
    alpha_f = divide_exact(subtract(products[1], products[0]), pi_squared)
    alpha_g = divide_exact(subtract(products[2], products[0]), pi_squared)
    (u0, v0), (u1, v1) = quotient_lifts
    c0, d0 = shifted(u0), shifted(v0)
    c1, d1 = shifted(u1), shifted(v1)
    theta = divide_exact(subtract(multiply(d1, c0), multiply(d0, c1)), pi_squared)
    coupling = divide_exact(subtract(multiply(products[0], c0), d0), pi)
    generators = [alpha_f, alpha_g, theta, coupling]

    assert all(reduce_cyclotomic(poly, n) != [0] for poly in generators[:3])
    assert [evaluate(poly, generator, p) for poly in generators] == [0, 0, 0, 0]
    norms = [principal_norm(poly, n) for poly in generators]
    assert all(value > 0 for value in norms[:3])
    assert all(value % p == 0 for value in norms)
    assert norms[0] <= 6 ** (n // 4) // 4
    assert norms[1] <= 6 ** (n // 4) // 4
    common = reduce(gcd, norms)
    assert common % p == 0
    assert common <= 6 ** (n // 4) // 4

    # A quotient with the wrong target fails precisely at the coupling gate.
    wrong = next(
        (u, v) for u in range(1, n) for v in range(1, n)
        if u != v and evaluate(shifted(v), generator, p)
        * pow(evaluate(shifted(u), generator, p), -1, p) % p != target
    )
    wrong_coupling = divide_exact(
        subtract(multiply(products[0], shifted(wrong[0])), shifted(wrong[1])), pi
    )
    assert evaluate(wrong_coupling, generator, p) != 0
    return norms, common


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "lambda=(beta_E C_0-D_0)/pi",
        "Y_18>0  =>  p in D_n^DA",
        "possibly unrelated accidents",
        "does not construct",
    ):
        assert marker in statement


def main() -> None:
    norms, common = finite_fixture()
    packet_check()
    print(
        "F3_H3_DOUBLE_ACCIDENT_LOW_DISTANCE_JOINT_IDEAL_ROUTER_PASS "
        f"fixture=32/1153 principal_norms={','.join(map(str, norms))} gcd={common}"
    )


if __name__ == "__main__":
    main()

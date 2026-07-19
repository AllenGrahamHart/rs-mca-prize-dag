#!/usr/bin/env python3
"""Verify the pair ideal-index interface and its exact route ledger."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_pair_ideal_index_probe_result.json"


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def scale(value: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in value]


def mul(left: list[int], right: list[int]) -> list[int]:
    degree = len(left)
    result = [0] * degree
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if not b:
                continue
            exponent = i + j
            if exponent >= degree:
                result[exponent - degree] -= a * b
            else:
                result[exponent] += a * b
    return result


def monomial(order: int, exponent: int) -> list[int]:
    degree = order // 2
    result = [0] * degree
    exponent %= order
    result[exponent % degree] = -1 if exponent >= degree else 1
    return result


def equations(order: int, pair: tuple[int, int]) -> tuple[list[int], list[int]]:
    degree = order // 2
    one = [1] + [0] * (degree - 1)
    x, y = (monomial(order, exponent) for exponent in pair)
    u = add(x, y)
    product = mul(x, y)
    v = scale(add(one, u), -1)
    c = mul(u, sub(v, product))
    c_power, v_power, cleared = c, v, mul(v, v)
    power = 1
    while power < order:
        cleared = sub(mul(cleared, cleared), scale(mul(c_power, v_power), 2))
        c_power = mul(c_power, c_power)
        v_power = mul(v_power, v_power)
        power *= 2
    return sub(c_power, v_power), sub(cleared, scale(v_power, 2))


def evaluate(value: list[int], root: int, prime: int) -> int:
    return sum(coefficient * pow(root, exponent, prime) for exponent, coefficient in enumerate(value)) % prime


def multiplication_matrix(value: list[int]) -> list[list[int]]:
    degree = len(value)
    rows = [[0] * degree for _ in range(degree)]
    for column in range(degree):
        for exponent, coefficient in enumerate(value):
            target = exponent + column
            if target >= degree:
                rows[target - degree][column] -= coefficient
            else:
                rows[target][column] += coefficient
    return rows


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rows, columns = len(work), len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[rank])
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def primitive_root(prime: int) -> int:
    factors = []
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError(prime)


def legal_pairs(order: int) -> list[tuple[int, int]]:
    half = order // 2
    available = [exponent for exponent in range(1, order) if exponent != half]
    return [
        pair
        for pair in itertools.combinations(available, 2)
        if (pair[1] - pair[0]) % order != half
    ]


def representatives(order: int) -> list[tuple[int, int]]:
    unseen = set(legal_pairs(order))
    output = []
    while unseen:
        pair = min(unseen)
        orbit = {
            tuple(sorted(((unit * pair[0]) % order, (unit * pair[1]) % order)))
            for unit in range(1, order, 2)
        }
        unseen.difference_update(orbit)
        output.append(pair)
    return output


def check_split_rank() -> int:
    checks = 0
    for order, primes in ((8, (17, 41, 73, 89)), (16, (17, 97, 113, 193))):
        degree = order // 2
        for prime in primes:
            generator = primitive_root(prime)
            root = pow(generator, (prime - 1) // order, prime)
            primitive_roots = [pow(root, unit, prime) for unit in range(1, order, 2)]
            for pair in legal_pairs(order):
                first, second = equations(order, pair)
                left = multiplication_matrix(first)
                right = multiplication_matrix(second)
                block = [a + b for a, b in zip(left, right)]
                rank_deficient = rank_mod(block, prime) < degree
                common_root = any(
                    evaluate(first, omega, prime) == 0
                    and evaluate(second, omega, prime) == 0
                    for omega in primitive_roots
                )
                if rank_deficient != common_root:
                    raise AssertionError((order, prime, pair, rank_deficient, common_root))
                checks += 1
    return checks


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def check_ledger() -> tuple[int, int, int]:
    data = json.loads(RESULT.read_text())
    if data["status"] != "COMPLETE" or data["orders"] != [16, 32, 64, 128]:
        raise AssertionError((data["status"], data["orders"]))
    expected_counts = {"16": 14, "32": 36, "64": 82, "128": 176}
    if data["orbit_counts"] != expected_counts or len(data["rows"]) != 308:
        raise AssertionError((data["orbit_counts"], len(data["rows"])))
    for order in data["orders"]:
        actual = sorted(tuple(row["pair"]) for row in data["rows"] if row["order"] == order)
        if actual != representatives(order):
            raise AssertionError((order, len(actual)))

    factor_rows = {row["index"]: row for row in data["factor_rows"]}
    distinct_indices = {row["index"] for row in data["rows"] if int(row["index"]) > 1}
    if set(factor_rows) != distinct_indices:
        raise AssertionError((len(factor_rows), len(distinct_indices)))
    primes = set()
    max_v2 = 0
    for index_text, row in factor_rows.items():
        product = 1
        for factor in row["factors"]:
            prime = int(factor["prime"])
            if not is_prime(prime):
                raise AssertionError(prime)
            product *= prime ** int(factor["exponent"])
            primes.add(prime)
            max_v2 = max(max_v2, int(factor["v2_prime_minus_1"]))
        if product != int(index_text):
            raise AssertionError((index_text, product))
    expected_primes = {3, 11, 17, 31, 97, 193, 257, 449, 577, 641, 769, 1153}
    if primes != expected_primes or max_v2 != 8 or data["max_v2_prime_minus_1"] != 8:
        raise AssertionError((primes, max_v2))
    return len(data["rows"]), len(primes), max_v2


def main() -> None:
    split_checks = check_split_rank()
    rows, primes, max_v2 = check_ledger()
    print(
        "DLI_WCL_ELL2_WEIGHT5_PAIR_IDEAL_INDEX_PASS "
        f"split_rank_checks={split_checks} ladder_rows={rows} "
        f"bad_primes={primes} max_v2={max_v2}"
    )


if __name__ == "__main__":
    main()

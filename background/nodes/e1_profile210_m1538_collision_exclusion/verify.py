#!/usr/bin/env python3
"""Verify the profile-(2,10) cofactor-1538 exclusion."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m1538_collision_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
COUNT = 64
MEAN = 18
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
COFACTOR = 1538
RATIONAL_PRIME = 769
BASE_ROOT = 7
EXPECTED_TYPES = {
    (11, 20, -1, -1),
    (14, 15, 1, 1),
    (18, 21, 1, -1),
    (19, 50, -1, 1),
    (36, 49, -1, 1),
}
EXPECTED_QUOTIENTS = {
    94726573109454554355723205753386381132700979257546174561074519931854171378433,
    94726572813333334850450851147142254866189741290919693369950466971809955939327,
    94726573091729884801570429320134633068624255208740225490737339440982526158079,
    94726573091644995672964768686916625315139627899621468752369565038943115036671,
    94726573091678309360928070176107749808616100579343144696817893372730754023169,
}


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_interval(variance: int, lower_count: int) -> tuple[Fraction, Fraction]:
    upper_count = COUNT - lower_count
    low_sqrt = sqrt_interval(Fraction(variance * upper_count, lower_count))
    high_sqrt = sqrt_interval(Fraction(variance * lower_count, upper_count))
    low_value = (Fraction(MEAN) - low_sqrt[1], Fraction(MEAN) - low_sqrt[0])
    high_value = (Fraction(MEAN) + high_sqrt[0], Fraction(MEAN) + high_sqrt[1])
    if low_value[0] <= 0:
        raise RuntimeError("infeasible product interval")
    return (
        low_value[0] ** lower_count * high_value[0] ** upper_count,
        low_value[1] ** lower_count * high_value[1] ** upper_count,
    )


def fold_lag(lag: int, sign: int) -> tuple[int, int]:
    lag %= 256
    if lag > 128:
        lag = 256 - lag
    if lag > 64:
        return 128 - lag, -sign
    if lag in (0, 64):
        raise RuntimeError("unexpected fixed lag")
    return lag, sign


def finite_field_types() -> tuple[int, set[tuple[int, int, int, int]]]:
    logs = {pow(BASE_ROOT, exponent, RATIONAL_PRIME): exponent for exponent in range(1, 256, 2)}
    if len(logs) != 128 or pow(BASE_ROOT, 128, RATIONAL_PRIME) != -1 % RATIONAL_PRIME:
        raise RuntimeError("base primitive-root check failed")
    hits = 0
    canonical = set()
    for root, exponent in logs.items():
        traces = [0] + [
            (pow(root, lag, RATIONAL_PRIME) + pow(pow(root, lag, RATIONAL_PRIME), -1, RATIONAL_PRIME))
            % RATIONAL_PRIME
            for lag in range(1, 64)
        ]
        for first in range(1, 64):
            for second in range(first + 1, 64):
                if (first + second) % 2 == 0:
                    continue
                for first_sign in (-1, 1):
                    for second_sign in (-1, 1):
                        if (
                            MEAN
                            + first_sign * traces[first]
                            + second_sign * traces[second]
                        ) % RATIONAL_PRIME:
                            continue
                        hits += 1
                        d, ds = fold_lag(exponent * first, first_sign)
                        e, es = fold_lag(exponent * second, second_sign)
                        if d > e:
                            d, e, ds, es = e, d, es, ds
                        canonical.add((d, e, ds, es))
    return hits, canonical


def polynomial_add(first: list[int], second: list[int], multiplier: int = 1) -> list[int]:
    result = [0] * max(len(first), len(second))
    for index in range(len(result)):
        result[index] = (
            (first[index] if index < len(first) else 0)
            + multiplier * (second[index] if index < len(second) else 0)
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def chebyshev_polynomials(limit: int) -> list[list[int]]:
    polynomials = [[2], [0, 1]]
    for _ in range(2, limit + 1):
        polynomials.append(
            polynomial_add([0] + polynomials[-1], polynomials[-2], -1)
        )
    return polynomials


def multiplication_norm(modulus: list[int], value: list[int]) -> int:
    degree = len(modulus) - 1
    matrix = [[0] * degree for _ in range(degree)]
    for column in range(degree):
        reduced = [0] * column + value[:]
        for top in range(len(reduced) - 1, degree - 1, -1):
            coefficient = reduced[top]
            if coefficient:
                shift = top - degree
                for index, entry in enumerate(modulus):
                    reduced[index + shift] -= coefficient * entry
        for row in range(degree):
            matrix[row][column] = reduced[row] if row < len(reduced) else 0

    previous = 1
    determinant_sign = 1
    for pivot_index in range(degree - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap = next(
                row
                for row in range(pivot_index + 1, degree)
                if matrix[row][pivot_index]
            )
            matrix[pivot_index], matrix[swap] = matrix[swap], matrix[pivot_index]
            determinant_sign *= -1
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, degree):
            for column in range(pivot_index + 1, degree):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise RuntimeError("non-exact Bareiss division")
                matrix[row][column] = numerator // previous
            matrix[row][pivot_index] = 0
        previous = pivot
    return determinant_sign * matrix[-1][-1]


def main() -> None:
    target = COFACTOR * P_MIN
    comparisons = 0
    closest = None
    for lower_count in range(1, COUNT):
        if Fraction(6 * (COUNT - lower_count), lower_count) >= MEAN**2:
            continue
        _lower, upper = product_interval(6, lower_count)
        if not upper < target:
            raise RuntimeError(f"moment separation failed at {lower_count}")
        margin = Fraction(target, 1) / upper
        if closest is None or margin < closest[0]:
            closest = (margin, lower_count)
        comparisons += 1
    if comparisons != 62 or closest is None or closest[1] != 63:
        raise RuntimeError("moment comparison census drift")
    boundary, _upper = product_interval(4, 63)
    if not boundary > target:
        raise RuntimeError("moment boundary drift")

    lucas_previous, lucas = 2, 18
    for _ in range(2, 65):
        lucas_previous, lucas = lucas, 18 * lucas - lucas_previous
    if lucas % COFACTOR != 2:
        raise RuntimeError("variance-two Lucas remainder drift")

    hits, canonical = finite_field_types()
    if hits != 640 or canonical != EXPECTED_TYPES:
        raise RuntimeError(f"finite-field screen drift: {hits}, {canonical}")

    chebyshev = chebyshev_polynomials(64)
    quotients = set()
    for first, second, first_sign, second_sign in sorted(canonical):
        value = polynomial_add(
            polynomial_add([MEAN], chebyshev[first], first_sign),
            chebyshev[second],
            second_sign,
        )
        norm = abs(multiplication_norm(chebyshev[64], value))
        if norm % COFACTOR:
            raise RuntimeError("screened norm lost cofactor divisibility")
        quotient = norm // COFACTOR
        if not quotient < P_MIN:
            raise RuntimeError("screened norm quotient reached prize interval")
        quotients.add(quotient)
    if quotients != EXPECTED_QUOTIENTS:
        raise RuntimeError("exact norm ledger drift")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_split_prime_ideal_router",
        "e1_prize_n256_s18_profile_36_sharp_product_window",
        "e1_prize_n256_s18_variance_cofactor_windows",
    )
    if nodes[NODE]["status"] != "PROVED" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("DAG status drift")
    for supplier in suppliers:
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("missing evidence edge")

    print(
        "E1_PROFILE210_M1538_COLLISION_EXCLUSION_PASS "
        f"moment_comparisons={comparisons} field_hits={hits} "
        f"galois_types={len(canonical)} exact_norms={len(quotients)} "
        "remaining_split_cofactors=514,1028 maximum_orbits=266"
    )


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Exact controls for the support-only quartic pair-crossing gate."""

from __future__ import annotations

import runpy
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction"
    / "verify.py"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def proportional(left: list[int], right: list[int], prime: int) -> bool:
    pivot = next((index for index, value in enumerate(right) if value), None)
    if pivot is None:
        return not any(left)
    scalar = left[pivot] * pow(right[pivot], -1, prime) % prime
    return all(a == scalar * b % prime for a, b in zip(left, right, strict=True))


def build_control(e: int, prime: int) -> list[int]:
    source = runpy.run_path(str(SOURCE))
    locator = source["locator"]
    evaluate = source["evaluate"]
    derivative = source["derivative"]
    primitive_root = source["primitive_root"]
    matrix_rank = source["matrix_rank"]

    domain_order = 8 * e + 8
    require((prime - 1) % domain_order == 0, "bad field order")
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
    active = tuple(domain[5 + 2 * e :])
    a_poly = locator(tuple(row for pair in pairs for row in pair), prime)
    b_poly = locator(triple, prime)
    c_poly = locator(active, prime)
    d_polys = [locator(pair, prime) for pair in pairs]
    a_prime = derivative(a_poly, prime)

    ranks: list[int] = []
    for l in range(e):
        rows: list[list[int]] = []
        for k, (a, b) in enumerate(pairs):
            if k == l:
                continue

            def original_weight(row: int) -> int:
                a_over_d = 1
                for other, d_poly in enumerate(d_polys):
                    if other != k:
                        a_over_d = a_over_d * evaluate(d_poly, row, prime) % prime
                return (
                    pow(evaluate(b_poly, row, prime), 3, prime)
                    * pow(a_over_d, 3, prime)
                    * pow(evaluate(d_polys[l], row, prime), 2, prime)
                    * pow(evaluate(c_poly, row, prime), -1, prime)
                ) % prime

            def global_weight(row: int) -> int:
                return (
                    row
                    * (row - s)
                    * (row - x_0)
                    * pow(evaluate(b_poly, row, prime), 4, prime)
                    * pow(evaluate(a_prime, row, prime), 4, prime)
                    * pow(evaluate(d_polys[l], row, prime), 2, prime)
                ) % prime

            f_a = original_weight(a)
            f_b = original_weight(b)
            g_a = global_weight(a)
            g_b = global_weight(b)
            original_row = [
                (f_b * pow(a, degree, prime) - f_a * pow(b, degree, prime))
                % prime
                for degree in range(5)
            ]
            simplified_row = [
                (g_b * pow(a, degree, prime) + g_a * pow(b, degree, prime))
                % prime
                for degree in range(5)
            ]
            require(
                proportional(original_row, simplified_row, prime),
                "derivative-normalized crossing row mismatch",
            )
            require(any(simplified_row), "zero crossing row")
            rows.append(simplified_row)
        ranks.append(matrix_rank(rows, prime))
    return ranks


def perfect_matchings(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        remainder = items[1:index] + items[index + 1 :]
        for tail in perfect_matchings(remainder):
            yield ((first, second),) + tail


def exhaustive_e6() -> dict[tuple[int, ...], int]:
    source = runpy.run_path(str(SOURCE))
    locator = source["locator"]
    evaluate = source["evaluate"]
    derivative = source["derivative"]
    primitive_root = source["primitive_root"]
    matrix_rank = source["matrix_rank"]

    e = 6
    prime = 113
    domain_order = 56
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
    exceptional = tuple(domain[2:14])
    triple = tuple(domain[14:17])
    a_poly = locator(exceptional, prime)
    b_poly = locator(triple, prime)
    a_prime = derivative(a_poly, prime)
    base_weight = {
        row: (
            row
            * (row - s)
            * (row - x_0)
            * pow(evaluate(b_poly, row, prime), 4, prime)
            * pow(evaluate(a_prime, row, prime), 4, prime)
        )
        % prime
        for row in exceptional
    }

    histogram: dict[tuple[int, ...], int] = {}
    survivors = 0
    for pairs in perfect_matchings(exceptional):
        ranks: list[int] = []
        for l, (left, right) in enumerate(pairs):
            rows: list[list[int]] = []
            for k, (a, b) in enumerate(pairs):
                if k == l:
                    continue
                d_a = (a - left) * (a - right) % prime
                d_b = (b - left) * (b - right) % prime
                g_a = base_weight[a] * d_a * d_a % prime
                g_b = base_weight[b] * d_b * d_b % prime
                rows.append(
                    [
                        (g_b * pow(a, degree, prime) + g_a * pow(b, degree, prime))
                        % prime
                        for degree in range(5)
                    ]
                )
            ranks.append(matrix_rank(rows, prime))
        pattern = tuple(sorted(ranks))
        histogram[pattern] = histogram.get(pattern, 0) + 1
        survivors += max(ranks) < 5

    require(sum(histogram.values()) == 10395, "matching coverage mismatch")
    require(survivors == 0, "unexpected all-deficient matching")
    return histogram


def check_abstract_antiweight() -> list[int]:
    source = runpy.run_path(str(SOURCE))
    locator = source["locator"]
    evaluate = source["evaluate"]
    mul = source["mul"]
    matrix_rank = source["matrix_rank"]

    prime = 113
    pairs = [(2 * index + 1, 2 * index + 2) for index in range(6)]
    weights = {
        row: value
        for a, b in pairs
        for row, value in ((a, 1), (b, prime - 1))
    }
    ranks: list[int] = []
    for l, (left, right) in enumerate(pairs):
        d_l = locator((left, right), prime)
        p_l = mul(d_l, d_l, prime)
        rows: list[list[int]] = []
        for k, (a, b) in enumerate(pairs):
            if k == l:
                continue
            g_a = weights[a] * pow(evaluate(d_l, a, prime), 2, prime) % prime
            g_b = weights[b] * pow(evaluate(d_l, b, prime), 2, prime) % prime
            row = [
                (g_b * pow(a, degree, prime) + g_a * pow(b, degree, prime))
                % prime
                for degree in range(5)
            ]
            require(
                sum(
                    value * coefficient
                    for value, coefficient in zip(row, p_l, strict=True)
                )
                % prime
                == 0,
                "abstract antiweight kernel mismatch",
            )
            rows.append(row)
        ranks.append(matrix_rank(rows, prime))
    require(all(value <= 4 for value in ranks), "antiweight route fence lost defect")
    return ranks


def main() -> None:
    expected = {
        (4, 241): [3, 3, 3, 3],
        (5, 97): [4, 4, 4, 4, 4],
        (6, 113): [5, 5, 5, 5, 5, 5],
        (7, 193): [5, 5, 5, 5, 5, 5, 5],
    }
    observed = {key: build_control(*key) for key in expected}
    require(observed == expected, "unexpected pair-crossing ranks")
    histogram = exhaustive_e6()
    expected_histogram = {
        (5, 5, 5, 5, 5, 5): 9811,
        (4, 5, 5, 5, 5, 5): 574,
        (4, 4, 5, 5, 5, 5): 9,
        (4, 4, 4, 5, 5, 5): 1,
    }
    require(histogram == expected_histogram, "unexpected e6 matching histogram")
    antiweight_ranks = check_abstract_antiweight()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_PAIR_CROSSING_PASS "
        f"controls={observed} first_rank_five_e=6 "
        "e6_matchings=10395 e6_all_deficient=0 "
        f"abstract_antiweight_ranks={antiweight_ranks}"
    )


if __name__ == "__main__":
    main()

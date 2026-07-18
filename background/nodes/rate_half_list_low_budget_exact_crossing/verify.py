#!/usr/bin/env python3
"""Verify the exact rate-half ordinary-list crossings for budgets one and two."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_low_budget_exact_crossing"
JOHNSON = "rate_half_list_integer_johnson_safe_anchor"
CONSUMER = "rate_half_list_adjacent_crossing"


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % prime
    return product


def evaluate(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def root_polynomial(roots: list[int], prime: int) -> list[int]:
    result = [1]
    for root in roots:
        result = multiply(result, [(-root) % prime, 1], prime)
    return result


def johnson_margin(length: int, dimension: int, budget: int, agreement: int) -> int:
    lists = budget + 1
    degree, remainder = divmod(lists * agreement, length)
    lower = length * degree * (degree - 1) // 2 + remainder * degree
    upper = lists * (lists - 1) // 2 * (dimension - 1)
    return lower - upper


def budget_one_witness(domain: list[int], prime: int) -> tuple[int, ...]:
    length = len(domain)
    dimension = length // 2
    quarter = length // 4
    agreement = 3 * quarter - 1
    overlap_size = 2 * quarter - 2
    overlap = domain[:overlap_size]
    remainder = domain[overlap_size:]
    only_size = quarter + 1
    first_only = remainder[:only_size]
    second_only = remainder[only_size:]
    first_set = set(overlap + first_only)
    second_set = set(overlap + second_only)
    assert len(first_set) == len(second_set) == agreement
    assert first_set | second_set == set(domain)

    roots = overlap + first_only[:1]
    first = [0]
    second = root_polynomial(roots, prime)
    assert len(second) - 1 == dimension - 1
    first_values = [0] * length
    second_values = [evaluate(second, x, prime) for x in domain]
    received = [0 if x in first_set else second_values[j] for j, x in enumerate(domain)]
    return tuple(
        sum(value == target for value, target in zip(values, received, strict=True))
        for values in (first_values, second_values)
    )


def budget_two_witness(
    prime: int, length: int, primitive: int, coset: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    dimension = length // 2
    quarter = length // 4
    zeta = pow(primitive, (prime - 1) // length, prime)
    domain = [(coset * pow(zeta, exponent, prime)) % prime for exponent in range(length)]
    assert len(set(domain)) == length
    fourth_root = pow(zeta, quarter, prime)
    assert pow(fourth_root, 2, prime) == prime - 1
    coset_scale = pow(pow(coset, quarter, prime), -1, prime)

    fibers = {value: [] for value in (1, prime - 1, fourth_root, (-fourth_root) % prime)}
    for x in domain:
        y = pow(x, quarter, prime) * coset_scale % prime
        fibers[y].append(x)
    assert {len(fiber) for fiber in fibers.values()} == {quarter}

    minus_i = (-fourth_root) % prime
    exceptional = fibers[minus_i][0]
    common = root_polynomial(fibers[minus_i][1:], prime)
    y_coefficient = coset_scale
    y_minus_one = [prime - 1] + [0] * (quarter - 1) + [y_coefficient]
    i_y_plus_one = [fourth_root] + [0] * (quarter - 1) + [
        fourth_root * y_coefficient % prime
    ]
    codewords = (
        [0],
        multiply(common, y_minus_one, prime),
        multiply(common, i_y_plus_one, prime),
    )
    assert max(len(poly) - 1 for poly in codewords) <= dimension - 1
    values = tuple(tuple(evaluate(poly, x, prime) for x in domain) for poly in codewords)
    assert len(set(values)) == 3

    received = []
    for index, x in enumerate(domain):
        y = pow(x, quarter, prime) * coset_scale % prime
        received.append(values[1][index] if y == fourth_root else 0)
    agreements = tuple(
        sum(value == target for value, target in zip(word, received, strict=True))
        for word in values
    )
    assert exceptional in fibers[minus_i]
    return agreements, tuple(sorted(len(fiber) for fiber in fibers.values()))


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[JOHNSON]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (JOHNSON, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    official_n = 1 << 41
    official_k = 1 << 40
    official_a = 3 * official_n // 4
    assert johnson_margin(official_n, official_k, 1, official_a) == 1
    assert johnson_margin(official_n, official_k, 2, official_a) == 3
    assert johnson_margin(official_n, official_k, 1, official_a - 1) <= 0
    assert johnson_margin(official_n, official_k, 2, official_a - 1) <= 0

    fixtures = ((17, 8, 3, 1), (97, 16, 5, 5))
    for prime, length, primitive, coset in fixtures:
        zeta = pow(primitive, (prime - 1) // length, prime)
        domain = [(coset * pow(zeta, exponent, prime)) % prime for exponent in range(length)]
        one_agreements = budget_one_witness(domain, prime)
        two_agreements, fiber_sizes = budget_two_witness(prime, length, primitive, coset)
        predecessor = 3 * length // 4 - 1
        assert min(one_agreements) >= predecessor
        assert min(two_agreements) >= predecessor
        assert fiber_sizes == (length // 4,) * 4

    check_dag()
    print(
        "RATE_HALF_LIST_LOW_BUDGET_EXACT_CROSSING_PASS "
        f"official_margins=1,3 fixtures={len(fixtures)} dag=2/2"
    )


if __name__ == "__main__":
    main()

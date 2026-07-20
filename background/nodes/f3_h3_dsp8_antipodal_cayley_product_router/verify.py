#!/usr/bin/env python3
"""Verify the DSP8 antipodal Cayley-product router."""

from __future__ import annotations

import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_antipodal_cayley_product_router"
DEPENDENCIES = {
    "f3_h3_dsp8_primitive_shift_pair_adapter",
    "f3_h3_antipodal_tail_distance_six_split",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def subgroup(prime: int, order: int) -> tuple[list[int], dict[int, int]]:
    root = next(
        pow(base, (prime - 1) // order, prime)
        for base in range(2, prime)
        if pow(pow(base, (prime - 1) // order, prime), order // 2, prime)
        == prime - 1
    )
    powers = [pow(root, exponent, prime) for exponent in range(order)]
    return powers, {value: exponent for exponent, value in enumerate(powers)}


def cayley(value: int, prime: int) -> int:
    assert value != 1
    return (1 + value) * pow((1 - value) % prime, -1, prime) % prime


def signed_support(
    pair: tuple[int, int], order: int
) -> dict[int, int]:
    half = order // 2
    answer: dict[int, int] = {}
    for exponent, coefficient in (
        ((pair[0] + pair[1]) % order, 1),
        (pair[0], -1),
        (pair[1], -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        answer[exponent] = answer.get(exponent, 0) + coefficient
    return {key: value for key, value in answer.items() if value}


def is_generic(support: dict[int, int]) -> bool:
    return len(support) == 3 and all(abs(value) == 1 for value in support.values())


def target(pair: tuple[int, int], powers: list[int], prime: int) -> int:
    return (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime


def ordered_edge_count(vertices: dict[tuple[int, int], frozenset[int]]) -> int:
    items = list(vertices.items())
    return sum(
        left_key != right_key and left_support.isdisjoint(right_support)
        for left_key, left_support in items
        for right_key, right_support in items
    )


def row_check(prime: int, order: int) -> tuple[int, int, int, int]:
    powers, exponent_of = subgroup(prime, order)
    half = order // 2
    allowed = [exponent for exponent in range(order) if exponent not in (0, half)]
    cayley_by_exponent = {
        exponent: cayley(powers[exponent], prime) for exponent in allowed
    }
    assert len(set(cayley_by_exponent.values())) == order - 2

    total_edges = 0
    total_weighted = 0
    total_factorizations = 0
    maximum_p = 0
    for a_exponent in range(1, half):
        a = powers[a_exponent]
        t = (1 - a * a) % prime
        c = cayley(a, prime)

        ordered_representations = {
            (left, right)
            for left in range(1, order)
            for right in range(1, order)
            if target((left, right), powers, prime) == t
        }
        antipodal = {
            (a_exponent, a_exponent + half),
            (a_exponent + half, a_exponent),
        }
        assert antipodal <= ordered_representations
        direct_nonantipodal = ordered_representations - antipodal

        direct_factors = set()
        for left, right in direct_nonantipodal:
            u_exponent = (left - a_exponent) % order
            v_exponent = (right - a_exponent) % order
            assert u_exponent in allowed and v_exponent in allowed
            direct_factors.add(
                (cayley_by_exponent[u_exponent], cayley_by_exponent[v_exponent])
            )

        factor_fiber = {
            (cayley_by_exponent[u], cayley_by_exponent[v])
            for u in allowed
            for v in allowed
            if cayley_by_exponent[u] * cayley_by_exponent[v] % prime == c
        }
        assert direct_factors == factor_fiber
        assert len(ordered_representations) == 2 + len(factor_fiber)
        assert (len(ordered_representations) >= 25) == (len(factor_fiber) >= 23)
        maximum_p = max(maximum_p, len(ordered_representations))
        total_factorizations += len(factor_fiber)

        direct_vertices: dict[tuple[int, int], frozenset[int]] = {}
        for left, right in combinations_with_replacement(range(1, order), 2):
            if target((left, right), powers, prime) != t:
                continue
            support = signed_support((left, right), order)
            if not is_generic(support):
                continue
            u = (left - a_exponent) % order
            v = (right - a_exponent) % order
            key = tuple(sorted((cayley_by_exponent[u], cayley_by_exponent[v])))
            assert key not in direct_vertices
            direct_vertices[key] = frozenset(support)

        factor_vertices: dict[tuple[int, int], frozenset[int]] = {}
        for u, v in combinations_with_replacement(allowed, 2):
            alpha, beta = cayley_by_exponent[u], cayley_by_exponent[v]
            if alpha * beta % prime != c:
                continue
            left = (a_exponent + u) % order
            right = (a_exponent + v) % order
            assert left and right
            pair = tuple(sorted((left, right)))
            support = signed_support(pair, order)
            if not is_generic(support):
                continue
            key = tuple(sorted((alpha, beta)))
            assert key not in factor_vertices
            factor_vertices[key] = frozenset(support)

        assert direct_vertices == factor_vertices
        direct_edges = ordered_edge_count(direct_vertices)
        factor_edges = ordered_edge_count(factor_vertices)
        assert direct_edges == factor_edges

        quotient = 0
        for z_exponent in range(1, order):
            w = (1 - t * (1 - powers[z_exponent])) % prime
            if w in exponent_of and exponent_of[w] != 0:
                quotient += 1
        total_edges += direct_edges
        total_weighted += direct_edges * quotient

    assert total_factorizations > 0
    assert total_edges > 0
    return total_factorizations, total_edges, total_weighted, maximum_p


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md").read_text().split()
    )
    for marker in (
        "C(h)=(1+h)/(1-h)",
        "P(1-a^2)=2+M_a",
        "P(1-a^2)>=25iffM_a>=23",
        "K_25^A=sum_(ainA_H,M_a>=23)E_aL_a",
        "suppliesnobound",
    ):
        assert marker in statement


def main() -> None:
    rows = [row_check(97, 32), row_check(1_153, 32)]
    packet_check()
    print(
        "F3_H3_DSP8_ANTIPODAL_CAYLEY_PRODUCT_ROUTER_PASS "
        f"rows=2 factorizations={sum(row[0] for row in rows)} "
        f"ordered_edges={sum(row[1] for row in rows)} "
        f"weighted={sum(row[2] for row in rows)} max_P={max(row[3] for row in rows)}"
    )


if __name__ == "__main__":
    main()

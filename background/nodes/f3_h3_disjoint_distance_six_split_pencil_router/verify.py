#!/usr/bin/env python3
"""Verify the disjoint distance-six split-pencil router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_disjoint_distance_six_split_pencil_router"
DEPENDENCIES = {
    "f3_h3_low_distance_quotient_incidence_router",
    "f3_h3_distance_six_support_overlap_payment",
}
CONSUMER = "f3_h3_mobius_excess_half"


def subgroup(p: int, n: int) -> tuple[list[int], dict[int, int]]:
    primitive = next(
        candidate
        for candidate in range(2, p)
        if len({pow(candidate, exponent, p) for exponent in range(1, p)}) == p - 1
    )
    generator = pow(primitive, (p - 1) // n, p)
    values = [pow(generator, exponent, p) for exponent in range(n)]
    return values, {value: exponent for exponent, value in enumerate(values)}


def signed_support(exponents: dict[int, int], n: int, x: int, y: int, p: int) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for value, coefficient in ((x * y % p, 1), (x, -1), (y, -1)):
        exponent = exponents[value]
        coordinate = exponent % (n // 2)
        sign = 1 if exponent < n // 2 else -1
        coefficients[coordinate] = coefficients.get(coordinate, 0) + coefficient * sign
    return {coordinate: value for coordinate, value in coefficients.items() if value}


def polynomial_value(t: int, r: int, x: int, p: int) -> int:
    return (x * x - (1 + r - t) * x + r) % p


def row_check(p: int, n: int) -> tuple[int, int, int]:
    h_values, exponents = subgroup(p, n)
    roots = [value for value in h_values if value != 1]
    fibers: dict[int, list[tuple[int, int]]] = {}
    for x in roots:
        for y in roots:
            target = (1 - x) * (1 - y) % p
            fibers.setdefault(target, []).append((x, y))

    checked_targets = 0
    checked_edges = 0
    checked_records = 0
    for target, ordered_pairs in fibers.items():
        unordered = {tuple(sorted(pair)) for pair in ordered_pairs}
        parameters: dict[int, tuple[int, int]] = {}
        for x, y in unordered:
            parameter = x * y % p
            assert parameter not in parameters or parameters[parameter] == (x, y)
            assert polynomial_value(target, parameter, x, p) == 0
            assert polynomial_value(target, parameter, y, p) == 0
            parameters[parameter] = (x, y)

        split_parameters: dict[int, tuple[int, int]] = {}
        for parameter in h_values:
            q_roots = [x for x in roots if polynomial_value(target, parameter, x, p) == 0]
            if not q_roots:
                continue
            root_pair = tuple(sorted((q_roots[0], q_roots[-1])))
            assert root_pair[0] * root_pair[1] % p == parameter
            split_parameters[parameter] = root_pair
        assert split_parameters == parameters

        diagonal = sum(1 for x, y in unordered if x == y)
        assert len(ordered_pairs) == 2 * len(parameters) - diagonal

        quotient_roots = [
            z for z in roots if (1 - target * (1 - z)) % p in roots
        ]
        quotient_pairs = [
            (z, (1 - target * (1 - z)) % p) for z in quotient_roots
        ]
        assert all((1 - w) % p == target * (1 - z) % p for z, w in quotient_pairs)

        generic: dict[int, tuple[dict[int, int], tuple[int, int]]] = {}
        for parameter, pair in parameters.items():
            support = signed_support(exponents, n, pair[0], pair[1], p)
            if len(support) == 3 and set(abs(value) for value in support.values()) == {1}:
                generic[parameter] = (support, pair)

        edge_count = 0
        raw_count = 0
        generic_items = sorted(generic.items())
        for left_index, (r, (left_support, left_pair)) in enumerate(generic_items):
            for s, (right_support, right_pair) in generic_items[left_index + 1 :]:
                distance = sum(
                    (left_support.get(key, 0) - right_support.get(key, 0)) ** 2
                    for key in set(left_support) | set(right_support)
                )
                disjoint = set(left_support).isdisjoint(right_support)
                assert disjoint == (distance == 6)
                if not disjoint:
                    continue
                edge_count += 1
                raw_count += 8 * len(quotient_pairs)

                # Compare coefficients of (X-r)Q_(t,s) and (X-s)Q_(t,r).
                left = [
                    1,
                    -(1 + r + s - target),
                    s + r * (1 + s - target),
                    -r * s,
                ]
                right = [
                    1,
                    -(1 + r + s - target),
                    r + s * (1 + r - target),
                    -r * s,
                ]
                difference = [(a - b) % p for a, b in zip(left, right)]
                assert difference == [0, 0, target * (s - r) % p, 0]

                x, y = left_pair
                u, v = right_pair
                assert (x * y + u + v - u * v - x - y) % p == 0

        assert raw_count == 8 * edge_count * len(quotient_pairs)
        checked_targets += 1
        checked_edges += edge_count
        checked_records += raw_count
    return checked_targets, checked_edges, checked_records


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
        "Q_(t,r)(X)=X^2-(1+r-t)X+r",
        "P(t)=2|S_t|-diag(t)",
        "=t(s-r)X",
        "J_25^0=8D_6,25^0",
        "10J_25^0+17J_25^A <=892n^2",
        "supplies no bound",
    ):
        assert marker in statement


def main() -> None:
    totals = [row_check(p, n) for p, n in ((17, 8), (97, 16), (193, 16))]
    packet_check()
    print(
        "F3_H3_DISJOINT_DISTANCE_SIX_SPLIT_PENCIL_ROUTER_PASS "
        f"rows={len(totals)} targets={sum(item[0] for item in totals)} "
        f"edges={sum(item[1] for item in totals)} "
        f"raw_records={sum(item[2] for item in totals)}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the DSP8 primitive cubic shift-pair adapter."""

from __future__ import annotations

import json
from itertools import combinations
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_primitive_shift_pair_adapter"
DEPENDENCY = "f3_h3_disjoint_distance_six_split_pencil_router"
CONSUMER = "f3_h3_dsp8_correlation_bound"


def subgroup(p: int, n: int) -> tuple[list[int], dict[int, int]]:
    primitive = next(
        candidate
        for candidate in range(2, p)
        if len({pow(candidate, exponent, p) for exponent in range(1, p)}) == p - 1
    )
    generator = pow(primitive, (p - 1) // n, p)
    values = [pow(generator, exponent, p) for exponent in range(n)]
    return values, {value: exponent for exponent, value in enumerate(values)}


def signed_support(
    exponents: dict[int, int], n: int, x: int, y: int, p: int
) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for value, coefficient in ((x * y % p, 1), (x, -1), (y, -1)):
        exponent = exponents[value]
        coordinate = exponent % (n // 2)
        sign = 1 if exponent < n // 2 else -1
        coefficients[coordinate] = coefficients.get(coordinate, 0) + coefficient * sign
    return {coordinate: value for coordinate, value in coefficients.items() if value}


def q_value(t: int, r: int, x: int, p: int) -> int:
    return (x * x - (1 + r - t) * x + r) % p


def cubic_pair(t: int, r: int, s: int, p: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = (
        1,
        -(1 + r + s - t) % p,
        (s + r * (1 + s - t)) % p,
        (-r * s) % p,
    )
    b = (
        1,
        a[1],
        (r + s * (1 + r - t)) % p,
        a[3],
    )
    return a, b


def cubic_from_roots(values: tuple[int, int, int], p: int) -> tuple[int, ...]:
    x, y, z = values
    return (
        1,
        (-(x + y + z)) % p,
        (x * y + x * z + y * z) % p,
        (-x * y * z) % p,
    )


def exhaustive_decorated_pairs(
    p: int, n: int, h_values: list[int], exponents: dict[int, int]
) -> set[tuple[object, ...]]:
    triples = []
    for roots in combinations(h_values, 3):
        coordinates = frozenset(exponents[value] % (n // 2) for value in roots)
        if len(coordinates) == 3:
            triples.append((roots, coordinates, cubic_from_roots(roots, p)))

    records: set[tuple[object, ...]] = set()
    for a_roots, a_coordinates, a in triples:
        for b_roots, b_coordinates, b in triples:
            if not a_coordinates.isdisjoint(b_coordinates):
                continue
            if a[1] != b[1] or a[3] != b[3] or a[2] == b[2]:
                continue
            lam = (a[2] - b[2]) % p
            for r in a_roots:
                for s in b_roots:
                    if a[3] != (-r * s) % p:
                        continue
                    a_residual = tuple(value for value in a_roots if value != r)
                    b_residual = tuple(value for value in b_roots if value != s)
                    assert len(a_residual) == len(b_residual) == 2
                    if 1 in a_residual or 1 in b_residual:
                        continue
                    t = lam * pow((s - r) % p, p - 2, p) % p
                    assert all(q_value(t, s, value, p) == 0 for value in a_residual)
                    assert all(q_value(t, r, value, p) == 0 for value in b_residual)
                    records.add((a, b, r, s))
    return records


def row_check(p: int, n: int) -> tuple[int, int, int]:
    h_values, exponents = subgroup(p, n)
    roots = [value for value in h_values if value != 1]
    h_set = set(h_values)
    fibers: dict[int, set[tuple[int, int]]] = {}
    for x in roots:
        for y in roots:
            pair = (x, y) if x <= y else (y, x)
            fibers.setdefault((1 - x) * (1 - y) % p, set()).add(pair)

    d_total = 0
    k_records: set[tuple[object, ...]] = set()
    adapter_records: set[tuple[object, ...]] = set()
    checked_converses = 0
    for t, pairs in fibers.items():
        generic = []
        for x, y in pairs:
            support = signed_support(exponents, n, x, y, p)
            if len(support) == 3 and set(abs(value) for value in support.values()) == {1}:
                generic.append((x * y % p, x, y, frozenset(support)))

        quotient = []
        for z in roots:
            w = (1 - t * (1 - z)) % p
            if w in h_set and w != 1:
                quotient.append((z, w))

        for left_index, left in enumerate(generic):
            for right in generic[left_index + 1 :]:
                if not left[3].isdisjoint(right[3]):
                    continue
                d_total += len(quotient)
                for first, second in ((left, right), (right, left)):
                    r, x, y, _ = first
                    s, u, v, _ = second
                    assert r != s
                    a, b = cubic_pair(t, r, s, p)
                    lam = t * (s - r) % p
                    assert tuple((aa - bb) % p for aa, bb in zip(a, b)) == (0, 0, lam, 0)
                    assert a[3] == b[3] == (-r * s) % p
                    assert gcd(n, 3) == 1

                    recovered_t = lam * pow((s - r) % p, p - 2, p) % p
                    assert recovered_t == t
                    alpha = a[1]
                    assert recovered_t == (1 + alpha + r + s) % p
                    q_s = (1, (alpha + r) % p, s)
                    q_r = (1, (alpha + s) % p, r)
                    assert q_s == (1, (t - 1 - s) % p, s)
                    assert q_r == (1, (t - 1 - r) % p, r)
                    assert all(q_value(t, s, value, p) == 0 for value in (u, v))
                    assert all(q_value(t, r, value, p) == 0 for value in (x, y))

                    six_coordinates = {
                        exponents[value] % (n // 2) for value in (r, s, x, y, u, v)
                    }
                    assert len(six_coordinates) == 6
                    adapter_record = (a, b, r, s)
                    assert adapter_record not in adapter_records
                    adapter_records.add(adapter_record)
                    for z, w in quotient:
                        record = (a, b, r, s, z, w)
                        assert record not in k_records
                        k_records.add(record)
                        assert (1 - w) % p == t * (1 - z) % p
                        checked_converses += 1

    k_total = len(k_records)
    j_total = 4 * k_total
    assert k_total == 2 * d_total
    assert j_total == 8 * d_total
    if n <= 16:
        exhaustive = exhaustive_decorated_pairs(p, n, h_values, exponents)
        assert adapter_records == exhaustive, (
            len(adapter_records),
            len(exhaustive),
            len(adapter_records - exhaustive),
            len(exhaustive - adapter_records),
        )
    return d_total, k_total, checked_converses


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "A_(E,F)-B_(E,F)=t(s-r)X",
        "gcd(n,3)=1",
        "J_25^c=4K_25^c=8D_6,25^c",
        "10K_25^0+17K_25^A<=223n^2",
        "supplies no estimate",
    ):
        assert marker in statement

    for d0 in range(8):
        for da in range(8):
            j_lhs = 10 * (8 * d0) + 17 * (8 * da)
            k_lhs = 10 * (2 * d0) + 17 * (2 * da)
            assert j_lhs == 4 * k_lhs
            assert 892 == 4 * 223


def main() -> None:
    rows = [row_check(p, n) for p, n in ((17, 8), (97, 16), (193, 16))]
    packet_check()
    print(
        "F3_H3_DSP8_PRIMITIVE_SHIFT_PAIR_ADAPTER_PASS "
        f"rows={len(rows)} D={sum(row[0] for row in rows)} "
        f"K={sum(row[1] for row in rows)} converses={sum(row[2] for row in rows)}"
    )


if __name__ == "__main__":
    main()

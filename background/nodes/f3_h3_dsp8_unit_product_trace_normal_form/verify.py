#!/usr/bin/env python3
"""Verify the DSP8 unit-product trace normal form."""

from __future__ import annotations

import json
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_unit_product_trace_normal_form"
DEPENDENCY = "f3_h3_dsp8_primitive_shift_pair_adapter"
CONSUMER = "f3_h3_dsp8_unit_trace_elliptic_curve_router"


def subgroup(p: int, n: int) -> tuple[list[int], dict[int, int]]:
    primitive = next(
        candidate
        for candidate in range(2, p)
        if len({pow(candidate, exponent, p) for exponent in range(1, p)}) == p - 1
    )
    generator = pow(primitive, (p - 1) // n, p)
    values = [pow(generator, exponent, p) for exponent in range(n)]
    return values, {value: exponent for exponent, value in enumerate(values)}


def cubic(roots: tuple[int, int, int], p: int) -> tuple[int, ...]:
    x, y, z = roots
    return (
        1,
        (-(x + y + z)) % p,
        (x * y + x * z + y * z) % p,
        (-x * y * z) % p,
    )


def product(values: tuple[int, ...], p: int) -> int:
    answer = 1
    for value in values:
        answer = answer * value % p
    return answer


def row_check(p: int, n: int) -> tuple[int, int]:
    h_values, exponents = subgroup(p, n)
    h_set = set(h_values)
    triples = []
    for roots in combinations(h_values, 3):
        coordinates = frozenset(exponents[value] % (n // 2) for value in roots)
        if len(coordinates) == 3:
            triples.append((roots, coordinates, cubic(roots, p)))

    inverse_three = pow(3, -1, n)
    original_records: set[tuple[object, ...]] = set()
    normalized_records: set[tuple[object, ...]] = set()
    quotient_records = 0
    for a_roots, a_coordinates, a in triples:
        for b_roots, b_coordinates, b in triples:
            if not a_coordinates.isdisjoint(b_coordinates):
                continue
            if a[1] != b[1] or a[3] != b[3] or a[2] == b[2]:
                continue
            lam = (a[2] - b[2]) % p
            for capital_r in a_roots:
                for capital_s in b_roots:
                    if a[3] != (-capital_r * capital_s) % p:
                        continue
                    a_residual = tuple(value for value in a_roots if value != capital_r)
                    b_residual = tuple(value for value in b_roots if value != capital_s)
                    if 1 in a_residual or 1 in b_residual:
                        continue

                    original = (a, b, capital_r, capital_s)
                    assert original not in original_records
                    original_records.add(original)

                    rs_exponent = (exponents[capital_r] + exponents[capital_s]) % n
                    q = h_values[rs_exponent * inverse_three % n]
                    assert pow(q, 3, p) == capital_r * capital_s % p
                    q_inverse = pow(q, p - 2, p)
                    r, u, v = tuple(value * q_inverse % p for value in a_roots)
                    s, x, y = tuple(value * q_inverse % p for value in b_roots)
                    # Restore the distinguished roots after combination ordering.
                    r = capital_r * q_inverse % p
                    s = capital_s * q_inverse % p
                    uv = tuple(value * q_inverse % p for value in a_residual)
                    xy = tuple(value * q_inverse % p for value in b_residual)
                    u, v = uv
                    x, y = xy

                    assert q == r * s % p
                    assert r * u * v % p == 1
                    assert s * x * y % p == 1
                    sigma = (r + u + v) % p
                    assert sigma == (s + x + y) % p

                    t = lam * pow((capital_s - capital_r) % p, p - 2, p) % p
                    target = (1 + r * s * (r + s - sigma)) % p
                    assert target == t
                    assert target == (1 - r * s * u) * (1 - s * pow(u, p - 2, p)) % p
                    assert target == (1 - r * s * x) * (1 - r * pow(x, p - 2, p)) % p

                    assert (u + v) % p == (sigma - r) % p
                    assert u * v % p == pow(r, p - 2, p)
                    assert (x + y) % p == (sigma - s) % p
                    assert x * y % p == pow(s, p - 2, p)

                    scaled_a = tuple(sorted(q * value % p for value in (r, u, v)))
                    scaled_b = tuple(sorted(q * value % p for value in (s, x, y)))
                    assert scaled_a == tuple(sorted(a_roots))
                    assert scaled_b == tuple(sorted(b_roots))
                    normalized = (tuple(sorted((r, u, v))), tuple(sorted((s, x, y))), r, s, sigma)
                    assert normalized not in normalized_records
                    normalized_records.add(normalized)

                    for z in h_values:
                        if z == 1:
                            continue
                        w = (1 - target * (1 - z)) % p
                        if w in h_set and w != 1:
                            assert (1 - w) % p == (1 + r * s * (r + s - sigma)) * (1 - z) % p
                            quotient_records += 1

    assert original_records
    assert len(original_records) == len(normalized_records)
    assert quotient_records > 0
    return len(original_records), quotient_records


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    compact_statement = "".join(statement.split())
    for marker in (
        "q=rs,ruv=sxy=1",
        "sigma:=r+u+v=s+x+y",
        "=1+rs(r+s-sigma)",
        "F_(r,sigma)(T)=T^2-(sigma-r)T+r^(-1)",
    ):
        assert marker in compact_statement
    assert "suppliesnobound" in compact_statement

    n = 8192
    ambient = comb(n, 3) * comb(n - 3, 3)
    assert ambient > 223 * n * n


def main() -> None:
    records, quotient = row_check(97, 16)
    packet_check()
    print(
        "F3_H3_DSP8_UNIT_PRODUCT_TRACE_NORMAL_FORM_PASS "
        f"records={records} quotient_records={quotient}"
    )


if __name__ == "__main__":
    main()

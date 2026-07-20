#!/usr/bin/env python3
"""Verify the DSP8 unit-trace elliptic-curve router."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_unit_trace_elliptic_curve_router"
DEPENDENCY = "f3_h3_dsp8_unit_product_trace_normal_form"
CONSUMER = "f3_h3_dsp8_nodal_trace_parameter_router"


def subgroup(prime: int, order: int) -> tuple[list[int], dict[int, int]]:
    root = next(
        pow(base, (prime - 1) // order, prime)
        for base in range(2, prime)
        if pow(pow(base, (prime - 1) // order, prime), order // 2, prime)
        == prime - 1
    )
    powers = [pow(root, exponent, prime) for exponent in range(order)]
    return powers, {value: exponent for exponent, value in enumerate(powers)}


def geometry_check(prime: int) -> tuple[int, int]:
    inverse_three = pow(3, -1, prime)
    singular: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for sigma in range(prime):
        for x in range(prime):
            for y in range(prime):
                f = (x * x * y + x * y * y - sigma * x * y + 1) % prime
                fx = y * (2 * x + y - sigma) % prime
                fy = x * (x + 2 * y - sigma) % prime
                fz = (-sigma * x * y + 3) % prime
                if f == fx == fy == fz == 0:
                    singular[sigma].add((x, y))

    expected_sigmas = {sigma for sigma in range(prime) if pow(sigma, 3, prime) == 27 % prime}
    assert set(singular) == expected_sigmas
    for sigma in expected_sigmas:
        point = sigma * inverse_three % prime
        assert singular[sigma] == {(point, point)}

    # The three points at infinity are smooth for every sigma.
    for sigma in range(prime):
        for x, y in ((1, 0), (0, 1), (1, -1 % prime)):
            fx = y * (2 * x + y) % prime
            fy = x * (x + 2 * y) % prime
            fz = -sigma * x * y % prime
            assert (fx, fy, fz) != (0, 0, 0)

    assert (-3) % prime != 0
    return len(expected_sigmas), sum(len(points) for points in singular.values())


def curve_ledger_check(prime: int, order: int) -> tuple[int, int]:
    powers, exponent_of = subgroup(prime, order)
    half = order // 2
    by_trace: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for r_exponent in range(order):
        for u_exponent in range(order):
            v_exponent = (-r_exponent - u_exponent) % order
            sigma = (
                powers[r_exponent] + powers[u_exponent] + powers[v_exponent]
            ) % prime
            assert (
                powers[r_exponent]
                + powers[u_exponent]
                + pow(powers[r_exponent] * powers[u_exponent] % prime, -1, prime)
            ) % prime == sigma
            by_trace[sigma].append((r_exponent, u_exponent, v_exponent))

    raw_records = set()
    canonical_multiplicity: Counter[tuple[object, ...]] = Counter()
    roots = range(1, order)
    for points in by_trace.values():
        for r_exponent, u_exponent, v_exponent in points:
            for s_exponent, x_exponent, y_exponent in points:
                coordinates = {
                    exponent % half
                    for exponent in (
                        r_exponent,
                        u_exponent,
                        v_exponent,
                        s_exponent,
                        x_exponent,
                        y_exponent,
                    )
                }
                if len(coordinates) != 6:
                    continue
                r, s = powers[r_exponent], powers[s_exponent]
                q = r * s % prime
                residual = (
                    q * powers[u_exponent] % prime,
                    q * powers[v_exponent] % prime,
                    q * powers[x_exponent] % prime,
                    q * powers[y_exponent] % prime,
                )
                if 1 in residual:
                    continue
                sigma = (
                    r + powers[u_exponent] + powers[v_exponent]
                ) % prime
                t = (1 + r * s * (r + s - sigma)) % prime
                for z_exponent in roots:
                    w = (1 - t * (1 - powers[z_exponent])) % prime
                    if w not in exponent_of or exponent_of[w] == 0:
                        continue
                    raw = (
                        r_exponent,
                        u_exponent,
                        s_exponent,
                        x_exponent,
                        z_exponent,
                        exponent_of[w],
                    )
                    assert raw not in raw_records
                    raw_records.add(raw)
                    canonical = (
                        r_exponent,
                        tuple(sorted((u_exponent, v_exponent))),
                        s_exponent,
                        tuple(sorted((x_exponent, y_exponent))),
                        z_exponent,
                        exponent_of[w],
                    )
                    canonical_multiplicity[canonical] += 1

    assert raw_records
    assert canonical_multiplicity
    assert set(canonical_multiplicity.values()) == {4}
    assert len(raw_records) == 4 * len(canonical_multiplicity)
    return len(raw_records), len(canonical_multiplicity)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md").read_text().split()
    )
    for marker in (
        "X^2Y+XY^2-sigmaXYZ+Z^3=0",
        "sigma^3!=27",
        "sigma^3=27",
        "G_25^c=4K_25^c=J_25^c",
        "10G_25^0+17G_25^A<=892n^2",
        "suppliesnopoint-pairestimate",
    ):
        assert marker in statement


def main() -> None:
    singular_sigmas, singular_points = geometry_check(31)
    raw, canonical = curve_ledger_check(97, 16)
    packet_check()
    print(
        "F3_H3_DSP8_UNIT_TRACE_ELLIPTIC_CURVE_ROUTER_PASS "
        f"singular_sigmas={singular_sigmas} singular_points={singular_points} "
        f"raw={raw} canonical={canonical} factor={raw // canonical}"
    )


if __name__ == "__main__":
    main()

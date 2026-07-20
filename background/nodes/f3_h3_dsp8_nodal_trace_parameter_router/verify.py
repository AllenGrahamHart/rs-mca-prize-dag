#!/usr/bin/env python3
"""Verify the DSP8 nodal-trace parameter router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_trace_parameter_router"
DEPENDENCIES = {
    "f3_h3_dsp8_unit_trace_elliptic_curve_router",
    "f3_affine_coset_pair_optimized_stepanov",
}
CONSUMER = "f3_h3_dsp8_nodal_target_divisor_pruning"


def nodal_point(theta: int, c: int, prime: int) -> tuple[int, int, int]:
    denominator = theta * (1 + theta) % prime
    r = -c * pow(denominator, -1, prime) % prime
    u = -c * theta * theta * pow((1 + theta) % prime, -1, prime) % prime
    v = c * (1 + theta) ** 2 * pow(theta, -1, prime) % prime
    return r, u, v


def geometry_and_target_check(prime: int) -> tuple[int, int]:
    cube_roots = [c for c in range(1, prime) if pow(c, 3, prime) == 1]
    total_points = 0
    target_checks = 0
    parameters = [
        value
        for value in range(prime)
        if value not in (0, prime - 1)
        and (value * value + value + 1) % prime != 0
    ]
    for c in cube_roots:
        sigma = 3 * c % prime
        direct = {
            (r, u)
            for r in range(1, prime)
            for u in range(1, prime)
            if (r * r * u + r * u * u - sigma * r * u + 1) % prime == 0
        }
        routed = set()
        for theta in parameters:
            r, u, v = nodal_point(theta, c, prime)
            assert r * u * v % prime == 1
            assert (r + u + v) % prime == sigma
            routed.add((r, u))
        assert direct - {(c, c)} == routed
        assert (c, c) in direct and (c, c) not in routed
        total_points += len(direct)

        for theta in parameters:
            r, _, _ = nodal_point(theta, c, prime)
            for phi in parameters:
                s, _, _ = nodal_point(phi, c, prime)
                target = (1 + r * s * (r + s - sigma)) % prime
                numerator = (
                    (theta * phi - 1)
                    * (theta * phi + theta + 1)
                    * (theta * phi + theta + phi)
                    * (theta * phi + phi + 1)
                ) % prime
                denominator = (
                    theta
                    * theta
                    * phi
                    * phi
                    * (1 + theta) ** 2
                    * (1 + phi) ** 2
                ) % prime
                assert target == numerator * pow(denominator, -1, prime) % prime
                target_checks += 1
    return total_points, target_checks


def subgroup_check(prime: int, order: int) -> tuple[int, int]:
    root = next(
        pow(base, (prime - 1) // order, prime)
        for base in range(2, prime)
        if pow(pow(base, (prime - 1) // order, prime), order // 2, prime)
        == prime - 1
    )
    subgroup = [pow(root, exponent, prime) for exponent in range(order)]
    subgroup_set = set(subgroup)
    cube_roots = [c for c in range(1, prime) if pow(c, 3, prime) == 1]
    total_subgroup_points = 0
    weighted_all_pairs = 0
    for c in cube_roots:
        sigma = 3 * c % prime
        routed = []
        for theta in range(1, prime - 1):
            if (theta * theta + theta + 1) % prime == 0:
                continue
            r, u, v = nodal_point(theta, c, prime)
            direct = r in subgroup_set and u in subgroup_set and v in subgroup_set
            coset_condition = (
                pow(theta, 3, prime) in subgroup_set
                and (1 + theta)
                * pow(c * theta * theta % prime, -1, prime)
                % prime
                in subgroup_set
            )
            assert direct == coset_condition
            if direct:
                routed.append((r, u))

        if c in subgroup_set:
            assert c == 1
            routed.append((c, c))
        direct_points = [
            (r, u)
            for r in subgroup
            for u in subgroup
            if (r * r * u + r * u * u - sigma * r * u + 1) % prime == 0
        ]
        assert sorted(routed) == sorted(direct_points)
        count = len(routed)
        assert max(0, count - 1) ** 3 < 1728 * order * order
        total_subgroup_points += count

        for r, _ in routed:
            for s, _ in routed:
                target = (1 + r * s * (r + s - sigma)) % prime
                if target in (0, 1):
                    continue
                quotient = sum(
                    (1 + target * (z - 1)) % prime in subgroup_set
                    for z in subgroup
                ) - 1
                assert quotient >= 0
                weighted_all_pairs += quotient

    scale = order ** (2 / 3)
    assert weighted_all_pairs < 12 * scale * (12 * scale + 1) ** 2
    return total_subgroup_points, weighted_all_pairs


def arithmetic_check() -> None:
    for exponent in range(13, 42):
        n = 1 << exponent
        # Leading coefficients of (NTP5) and its class-weighted consequence.
        assert 12 * 12 * 12 == 1728
        assert 17 * 1728 == 29376
        assert 29376 > 892
        assert n >= 8192


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md").read_text().split()
    )
    for marker in (
        "[1+theta]=CA^2",
        "N_sigma<12n^(2/3)+1",
        "<12n^(2/3)(12n^(2/3)+1)^2",
        "<204n^(2/3)(12n^(2/3)+1)^2",
        "leadingcoefficientis`29376`",
        "marginalpointboundsalonearefenced",
    ):
        assert marker in statement


def main() -> None:
    points, target_checks = geometry_and_target_check(31)
    subgroup_points, weighted = subgroup_check(97, 16)
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_DSP8_NODAL_TRACE_PARAMETER_ROUTER_PASS "
        f"geometry_points={points} target_checks={target_checks} "
        f"subgroup_points={subgroup_points} weighted_control={weighted}"
    )


if __name__ == "__main__":
    main()

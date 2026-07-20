#!/usr/bin/env python3
"""Verify the cubic-preimage affine coset-pair Stepanov bound."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_affine_coset_pair_cubic_preimage_stepanov"
DEPENDENCY = "f3_h2_stepanov_inhouse"
CONSUMER = "f3_h3_dsp8_nodal_cube_preimage_envelope"


def floor_cuberoot(value: int) -> int:
    low, high = 0, 1
    while high**3 <= value:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**3 <= value:
            low = middle
        else:
            high = middle
    return low


def ceil_cuberoot(value: int) -> int:
    root = floor_cuberoot(value)
    return root if root**3 == value else root + 1


def maximal_multiplicity(a: int, b: int) -> int:
    target = a * b * b
    low, high = 0, 1
    while high * (a + high) < target:
        low, high = high, 2 * high
    while low + 1 < high:
        middle = (low + high) // 2
        if middle * (a + middle) < target:
            low = middle
        else:
            high = middle
    return low


def parameter_check() -> tuple[int, int]:
    minimum_slack = 0
    worst_scaled_numerator = 0
    for multiplier in (1, 3):
        for exponent in range(13, 42):
            n = 1 << exponent
            m = multiplier * n
            b = ceil_cuberoot(2 * m)
            a = m // b
            d = maximal_multiplicity(a, b)
            slacks = (
                a * b * b - d * (a + d),
                m + 1 - a * b,
                n * n + 1 - (a + m * b),
                132651 * d**3 * m * m - 4096 * (a + 2 * m * b) ** 3,
            )
            assert min(slacks) > 0
            assert (d + 1) * (a + d + 1) >= a * b * b
            row_slack = min(slacks)
            minimum_slack = row_slack if not minimum_slack else min(
                minimum_slack, row_slack
            )
            scaled_numerator = 4096 * (a + 2 * m * b) ** 3
            worst_scaled_numerator = max(worst_scaled_numerator, scaled_numerator)
    return minimum_slack, worst_scaled_numerator


def prime_factors(value: int) -> set[int]:
    factors = set()
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    return factors


def subgroup(prime: int, order: int) -> list[int]:
    factors = prime_factors(order)
    for base in range(2, prime):
        generator = pow(base, (prime - 1) // order, prime)
        if all(pow(generator, order // factor, prime) != 1 for factor in factors):
            return [pow(generator, exponent, prime) for exponent in range(order)]
    raise AssertionError("subgroup generator not found")


def finite_field_check(prime: int, order: int) -> int:
    group = subgroup(prime, order)
    group_set = set(group)
    maximum = 0
    for alpha in range(1, prime):
        for beta in range(1, prime):
            count = sum((alpha * value + beta) % prime in group_set for value in group)
            maximum = max(maximum, count)
    assert 4096 * maximum**3 < 132651 * order * order
    return maximum


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "m in {n,3n}".replace(" ", ""),
        "<(51/16)m^(2/3)",
        "order-`3n`cube-preimagesubgroup",
        "suppliesnomulti-fiberorenergyestimate",
    ):
        assert marker in statement


def main() -> None:
    slack, scaled = parameter_check()
    maximum = finite_field_check(97, 48)
    packet_check()
    print(
        "F3_AFFINE_COSET_PAIR_CUBIC_PREIMAGE_STEPANOV_PASS "
        f"official_cases=58 minimum_slack={slack} control_max={maximum} "
        f"scaled_checksum={scaled % 1000000007}"
    )


if __name__ == "__main__":
    main()

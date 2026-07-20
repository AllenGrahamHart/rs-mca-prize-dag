#!/usr/bin/env python3
"""Verify the DSP8 nodal cube-preimage envelope."""

from __future__ import annotations

from fractions import Fraction
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_cube_preimage_envelope"
DEPENDENCIES = {
    "f3_h3_dsp8_nodal_trace_parameter_router",
    "f3_affine_coset_pair_cubic_preimage_stepanov",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


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


def nodal_point(theta: int, c: int, prime: int) -> tuple[int, int, int]:
    r = -c * pow(theta * (1 + theta) % prime, -1, prime) % prime
    u = -c * theta * theta * pow((1 + theta) % prime, -1, prime) % prime
    v = c * (1 + theta) ** 2 * pow(theta, -1, prime) % prime
    return r, u, v


def cube_preimage_check(prime: int, order: int) -> tuple[int, int, int]:
    group = subgroup(prime, order)
    group_set = set(group)
    g = gcd(3, prime - 1)
    preimage = {value for value in range(1, prime) if pow(value, 3, prime) in group_set}
    assert len(preimage) == g * order
    assert all(
        (left * right) % prime in preimage
        for left in preimage
        for right in preimage
    )
    cube_roots = [value for value in range(1, prime) if pow(value, 3, prime) == 1]
    assert len(cube_roots) == g

    direct = set()
    for c in cube_roots:
        sigma = 3 * c % prime
        for r in group:
            for u in group:
                if (r * r * u + r * u * u - sigma * r * u + 1) % prime == 0:
                    direct.add((c, r, u))

    routed = set()
    parameter_count = 0
    for theta in range(1, prime - 1):
        if theta not in preimage or (1 + theta) % prime not in preimage:
            continue
        if (theta * theta + theta + 1) % prime == 0:
            continue
        candidates = [
            c
            for c in cube_roots
            if theta * (1 + theta) * pow(c, -1, prime) % prime in group_set
        ]
        assert len(candidates) == 1
        c = candidates[0]
        r, u, v = nodal_point(theta, c, prime)
        assert r in group_set and u in group_set and v in group_set
        routed.add((c, r, u))
        parameter_count += 1

    routed.add((1, 1, 1))
    assert routed == direct
    assert parameter_count == len(routed) - 1
    return g, len(preimage), len(direct)


def constants_check() -> None:
    live_g_allowance = Fraction(76599, 40)
    assert 8192**2 > 400**3
    one_root = 17 * Fraction(51, 16) * (Fraction(51, 16) + Fraction(1, 400)) ** 2
    assert one_root == Fraction(88226787, 160000)
    assert one_root < 552
    assert one_root < live_g_allowance

    cubic_bound = Fraction(2081, 1000)
    assert cubic_bound**3 > 9
    assert 2081**3 - 9 * 1000**3 == 11897441
    three_root = 17 * Fraction(51, 16) * (
        Fraction(51, 16) * cubic_bound + Fraction(1, 400)
    ) ** 2
    assert three_root == Fraction(9773067835947, 4096000000)
    assert three_root < 2387
    assert three_root > live_g_allowance


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
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "K={xinF_p^*:x^3inH}",
        "|K|=gn",
        "<(51/16)(gn)^(2/3)+1",
        "<552n^2ifp=2(mod3)",
        "<2387n^2ifp=1(mod3)",
        "76599/40=1914.975",
        "doesnotcloseDSP8",
    ):
        assert marker in statement


def main() -> None:
    control_one = cube_preimage_check(257, 16)
    control_three = cube_preimage_check(97, 16)
    constants_check()
    packet_check()
    print(
        "F3_H3_DSP8_NODAL_CUBE_PREIMAGE_ENVELOPE_PASS "
        f"one_root={control_one} three_root={control_three}"
    )


if __name__ == "__main__":
    main()

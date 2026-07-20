#!/usr/bin/env python3
"""Verify the DSP8 nodal target-divisor pruning rules."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_target_divisor_pruning"
DEPENDENCY = "f3_h3_dsp8_nodal_trace_parameter_router"
CONSUMER = "f3_h3_dsp8_correlation_bound"


def q(value: int, prime: int) -> int:
    return value * (value + 1) % prime


def roots(value: int, prime: int) -> tuple[int, int, int]:
    return (
        -pow(q(value, prime), -1, prime) % prime,
        -value * value * pow((value + 1) % prime, -1, prime) % prime,
        (value + 1) ** 2 * pow(value, -1, prime) % prime,
    )


def orbit(value: int, prime: int) -> set[int]:
    return {
        value,
        -value - 1,
        pow(value, -1, prime),
        -(value + 1) * pow(value, -1, prime),
        -value * pow((value + 1) % prime, -1, prime),
        -pow((value + 1) % prime, -1, prime),
    }


def zero_maps(value: int, prime: int) -> set[int]:
    return {
        pow(value, -1, prime),
        -(value + 1) * pow(value, -1, prime),
        -value * pow((value + 1) % prime, -1, prime),
        -pow((value + 1) % prime, -1, prime),
    }


def negative_collision_polynomials(a: int, b: int) -> tuple[int, ...]:
    """Numerators of R/U/V(a) + R/U/V(b), with harmless signs removed."""

    return (
        a * a + a + b * b + b,
        a * a * b * b + a * b * b + b + 1,
        a * a * b * b + 2 * a * a * b + a * a
        + a * b * b + 2 * a * b + a - b,
        a * a * b * b + a * a * b + a + 1,
        a * a * b + a * a + a * b * b + b * b,
        -a * a * b + a * b * b + 2 * a * b + a + b * b + 2 * b + 1,
        a * a * b * b + a * a * b + 2 * a * b * b
        + 2 * a * b - a + b * b + b,
        a * a * b + a * a - a * b * b + 2 * a * b + 2 * a + b + 1,
        a * a * b + a * b * b + 4 * a * b + a + b,
    )


def algebra_check(prime: int) -> tuple[int, int, int, int]:
    parameters = [
        value
        for value in range(1, prime - 1)
        if (value * value + value + 1) % prime != 0
    ]
    positive_pruned = 0
    negative_pruned = 0
    identity_pruned = 0
    live = 0
    for a in parameters:
        triple_a = roots(a, prime)
        assert sum(triple_a) % prime == 3
        assert triple_a[0] * triple_a[1] * triple_a[2] % prime == 1
        for transform in orbit(a, prime):
            assert sorted(roots(transform % prime, prime)) == sorted(triple_a)

        for b in parameters:
            triple_b = roots(b, prime)
            positive_overlap = not set(triple_a).isdisjoint(triple_b)
            assert positive_overlap == (b in {x % prime for x in orbit(a, prime)})

            negative_flags = [
                (left + right) % prime == 0
                for left in triple_a
                for right in triple_b
            ]
            polynomial_flags = [
                value % prime == 0 for value in negative_collision_polynomials(a, b)
            ]
            assert negative_flags == polynomial_flags

            qa = q(a, prime)
            qb = q(b, prime)
            denominator = qa * qa * qb * qb % prime
            r = triple_a[0]
            s = triple_b[0]
            target = (1 + r * s * (r + s - 3)) % prime
            numerator = (
                (a * b - 1)
                * (a * b + a + 1)
                * (a * b + a + b)
                * (a * b + b + 1)
            ) % prime
            identity_numerator = (qa + qb + 3 * qa * qb) % prime
            assert target == numerator * pow(denominator, -1, prime) % prime
            assert (target - 1) % prime == (
                -identity_numerator * pow(denominator, -1, prime)
            ) % prime
            assert (target == 0) == (b in {x % prime for x in zero_maps(a, prime)})

            if positive_overlap:
                positive_pruned += 1
            elif any(negative_flags):
                negative_pruned += 1
            elif target == 1:
                identity_pruned += 1
            else:
                assert target != 0
                live += 1
    return positive_pruned, negative_pruned, identity_pruned, live


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert (DEPENDENCY, CONSUMER, "ev") not in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "S(a)={a,-a-1,a^(-1),-(a+1)/a,-a/(a+1),-1/(a+1)}",
        "b in S(a)",
        "t(a,b)-1=-(q(a)+q(b)+3q(a)q(b))/(q(a)^2q(b)^2)",
        "nine tests `T_i(a)+T_j(b)=0`",
        "do not promote DSP8",
    ):
        assert marker.replace(" ", "") in statement.replace(" ", "")


def main() -> None:
    positive, negative, identity, live = algebra_check(31)
    packet_check()
    print(
        "F3_H3_DSP8_NODAL_TARGET_DIVISOR_PRUNING_PASS "
        f"positive={positive} negative={negative} identity={identity} live={live}"
    )


if __name__ == "__main__":
    main()

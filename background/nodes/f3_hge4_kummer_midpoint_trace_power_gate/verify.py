#!/usr/bin/env python3
"""Verify the HGE4 Kummer midpoint trace and power gate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_kummer_midpoint_trace_power_gate"
DEPENDENCIES = {
    "f3_hge4_near_third_belyi_necklace_bound",
    "f3_hge4_near_third_kummer_midpoint_pencil",
}
CONSUMER = "f3_hge4_norm_gate_count"
GCD_COMPILER = "f3_hge4_kummer_trace_power_gcd_compiler"


def prime_factors(value: int) -> set[int]:
    factors: set[int] = set()
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


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def subgroup(prime: int, order: int) -> set[int]:
    assert (prime - 1) % order == 0
    generator = pow(primitive_root(prime), (prime - 1) // order, prime)
    return {pow(generator, exponent, prime) for exponent in range(order)}


def dickson_trace(trace: int, index: int, prime: int) -> int:
    previous, current = 2, trace % prime
    if index == 0:
        return previous
    for _ in range(1, index):
        previous, current = current, (trace * current - previous) % prime
    return current


def endpoint_identity_check() -> None:
    for u, v in ((Fraction(2), Fraction(3)), (Fraction(5), Fraction(-7))):
        s = (u + v) / 2
        a = (v - u) / 2
        w = -1 / (u * v)
        z = -3 * (u + v) / (u * v * (v - u) ** 2)
        lam = w - z * s
        kappa = 1 - a * a * lam
        x = v / u
        assert kappa == -(1 + x) ** 2 / (8 * x)
        assert kappa == -s * s / (2 * u * v)


def finite_field_check(prime: int, order: int) -> tuple[int, int]:
    roots = subgroup(prime, order)
    traces: set[int] = set()
    square_traces: set[int] = set()
    power_candidates = 0
    mth_powers = {pow(value, order, prime) for value in range(1, prime)}
    for x in roots - {1, prime - 1}:
        inverse = pow(x, -1, prime)
        trace = (x + inverse) % prime
        direct = (-(1 + x) ** 2 * pow(8 * x, -1, prime)) % prime
        traced = (-(trace + 2) * pow(8, -1, prime)) % prime
        assert direct == traced != 0
        assert dickson_trace(trace, order, prime) == 2
        assert traced == (-(1 + inverse) ** 2 * pow(8 * inverse, -1, prime)) % prime
        passes = pow(traced, (prime - 1) // order, prime) == 1
        assert passes == (traced in mth_powers)
        if passes:
            assert pow(x, (prime - 1) // 2, prime) == 1
        power_candidates += int(passes)
        traces.add(trace)
        if pow(x, (prime - 1) // 2, prime) == 1:
            square_traces.add(trace)
    assert len(traces) == (order - 2) // 2
    if (prime - 1) // order % 2:
        assert len(square_traces) == order // 4 - 1
    assert power_candidates % 2 == 0
    return len(traces), power_candidates // 2


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert (NODE, GCD_COMPILER, "req") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "kappa=-(1+x)^2/(8x)",
        "C_m(tau)=2",
        "(p-1)/m",
        "exactly `(m-2)/2`",
        "only `m/4-1` trace values",
        "does not bound the number of pencils",
        "no converse",
    ):
        assert marker in text


def main() -> None:
    endpoint_identity_check()
    fixtures = [finite_field_check(97, 32), finite_field_check(193, 64)]
    packet_check()
    print(
        "F3_HGE4_KUMMER_MIDPOINT_TRACE_POWER_GATE_PASS "
        f"trace_fixtures={fixtures} endpoint_identities=2"
    )


if __name__ == "__main__":
    main()

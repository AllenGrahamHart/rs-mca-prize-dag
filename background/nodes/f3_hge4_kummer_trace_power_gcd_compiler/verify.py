#!/usr/bin/env python3
"""Verify the HGE4 Kummer trace-power polynomial gcd compiler."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_kummer_trace_power_gcd_compiler"
DEPENDENCY = "f3_hge4_kummer_midpoint_trace_power_gate"
CONSUMER = "f3_hge4_norm_gate_count"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def subtract(left: list[int], right: list[int], prime: int) -> list[int]:
    return add(left, [(-value) % prime for value in right], prime)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] = (out[i + j] + first * second) % prime
    return trim(out)


def divmod_poly(numerator: list[int], denominator: list[int], prime: int) -> tuple[list[int], list[int]]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    assert denominator != [0]
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inverse % prime
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] = (numerator[index + shift] - coefficient * value) % prime
        trim(numerator)
    return trim(quotient), numerator


def remainder(poly: list[int], modulus: list[int], prime: int) -> list[int]:
    return divmod_poly(poly, modulus, prime)[1]


def monic_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left, right = trim(left[:]), trim(right[:])
    while right != [0]:
        left, right = right, remainder(left, right, prime)
    inverse = pow(left[-1], -1, prime)
    return [(value * inverse) % prime for value in left]


def power_mod(base: list[int], exponent: int, modulus: list[int], prime: int) -> list[int]:
    out = [1]
    base = remainder(base, modulus, prime)
    while exponent:
        if exponent & 1:
            out = remainder(multiply(out, base, prime), modulus, prime)
        base = remainder(multiply(base, base, prime), modulus, prime)
        exponent //= 2
    return out


def trace_quotient(order: int, prime: int) -> list[int]:
    assert order >= 4 and order % 2 == 0
    index = order // 2 - 1
    previous, current = [1], [0, 1]
    if index == 0:
        return previous
    for _ in range(1, index):
        previous, current = current, subtract([0] + current, previous, prime)
    return current


def dickson(index: int, prime: int) -> list[int]:
    previous, current = [2], [0, 1]
    if index == 0:
        return previous
    for _ in range(1, index):
        previous, current = current, subtract([0] + current, previous, prime)
    return current


def candidate_gcd(order: int, prime: int) -> list[int]:
    quotient = (prime - 1) // order
    trace_order = order // 2 if quotient % 2 else order
    trace_poly = trace_quotient(trace_order, prime)
    inverse_eight = pow(8, -1, prime)
    scalar = [(-2 * inverse_eight) % prime, (-inverse_eight) % prime]
    powered = subtract(power_mod(scalar, quotient, trace_poly, prime), [1], prime)
    return monic_gcd(trace_poly, powered, prime)


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
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def direct_trace_candidates(order: int, prime: int) -> set[int]:
    quotient = (prime - 1) // order
    generator = pow(primitive_root(prime), quotient, prime)
    traces: set[int] = set()
    for exponent in range(1, order):
        x = pow(generator, exponent, prime)
        if x == prime - 1:
            continue
        trace = (x + pow(x, -1, prime)) % prime
        scalar = (-(trace + 2) * pow(8, -1, prime)) % prime
        if pow(scalar, quotient, prime) == 1:
            traces.add(trace)
    return traces


def arithmetic_check() -> None:
    expected = {(8, 137): 1, (16, 593): 1, (32, 1249): 1, (32, 97): 0}
    for (order, prime), count in expected.items():
        quotient = (prime - 1) // order
        assert quotient * order == prime - 1
        trace_order = order // 2 if quotient % 2 else order
        q_poly = trace_quotient(trace_order, prime)
        assert len(q_poly) - 1 == trace_order // 2 - 1
        c_poly = subtract(dickson(trace_order, prime), [2], prime)
        factor = multiply([-4, 0, 1], multiply(q_poly, q_poly, prime), prime)
        assert c_poly == factor
        candidate = candidate_gcd(order, prime)
        direct = direct_trace_candidates(order, prime)
        assert len(candidate) - 1 == len(direct) == count
        for trace in direct:
            assert sum(value * pow(trace, index, prime) for index, value in enumerate(candidate)) % prime == 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "C_m(X)-2=(X^2-4)Q_m(X)^2",
        "N_trace(m,p)=deg G_(m,p)",
        "(8,137,1)",
        "may be nonconstant",
        "not primitive pencils",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_HGE4_KUMMER_TRACE_POWER_GCD_COMPILER_PASS "
        "factorizations=4 gcd_controls=3_nonempty+1_empty"
    )


if __name__ == "__main__":
    main()

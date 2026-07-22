#!/usr/bin/env python3
"""Verify the unordered-product cutoff-12 compiler contract."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_unordered_product_cutoff12_candidate_compiler"
DEPENDENCIES = {
    "f3_h3_global_resultant_compression",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def prime_factors(value: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.add(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // q, prime) != 1 for q in factors):
            return candidate
    raise AssertionError("no primitive root")


def fiber_counts(n: int, prime: int) -> tuple[Counter[int], Counter[int], Counter[int]]:
    assert (prime - 1) % n == 0
    generator = pow(primitive_root(prime), (prime - 1) // n, prime)
    subgroup = [pow(generator, exponent, prime) for exponent in range(n)]
    shifted = [(1 - value) % prime for value in subgroup if value != 1]

    ordered = Counter((x * y) % prime for x in shifted for y in shifted)
    diagonal = Counter((x * x) % prime for x in shifted)
    unordered = Counter(
        (shifted[left] * shifted[right]) % prime
        for left in range(len(shifted))
        for right in range(left, len(shifted))
    )
    return ordered, diagonal, unordered


def finite_field_check() -> None:
    checks = 0
    for n, primes in ((4, (5, 13, 17, 29)), (8, (17, 41, 73, 89))):
        for prime in primes:
            ordered, diagonal, unordered = fiber_counts(n, prime)
            for target in set(ordered) | set(diagonal) | set(unordered):
                p_value = ordered[target]
                d_value = diagonal[target]
                u_value = unordered[target]
                assert p_value == 2 * u_value - d_value
                assert 0 <= d_value <= 2
                assert not (p_value >= 25 and u_value <= 12)
                checks += 1
    assert checks > 100


def arithmetic_check() -> None:
    n = 8192
    ordered_degree = (n - 1) ** 2
    unordered_degree = n * (n - 1) // 2
    assert ordered_degree == 67_092_481
    assert unordered_degree == 33_550_336
    assert unordered_degree < ordered_degree

    for diagonal, expected in ((0, 26), (1, 25), (2, 24)):
        assert 2 * 13 - diagonal == expected
    for diagonal in range(3):
        assert 2 * 14 - diagonal >= 26


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "Ucal_n(T)^2=Pcal_n(T)Delta_n(T)",
        "deg Ucal_n=n(n-1)/2",
        "(T-1)Y-1",
        "p divides a_(n,12)^neq",
        "iff some t!=1 has U(t)>=13",
        "P(t)=2U(t)-D(t)",
        "U(t)=13,       D(t)=2,       P(t)=24",
        "not an official-scale elimination algorithm",
    ):
        assert marker in text


def main() -> None:
    finite_field_check()
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_UNORDERED_PRODUCT_CUTOFF12_CANDIDATE_COMPILER_PASS "
        "degree8192=33550336 generators=13 selector=t_ne_1 boundary=U13_D2_P24"
    )


if __name__ == "__main__":
    main()

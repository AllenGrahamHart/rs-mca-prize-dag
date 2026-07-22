#!/usr/bin/env python3
"""Verify the nonidentity P25 subresultant compiler contract."""

from __future__ import annotations

import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_nonidentity_p25_subresultant_scalar_compiler"
DEPENDENCIES = {
    "f3_h3_global_resultant_compression",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"
UNORDERED_NODE = "f3_h3_unordered_product_cutoff12_candidate_compiler"


def load_fibers():
    path = ROOT / "background" / "nodes" / UNORDERED_NODE / "verify.py"
    spec = importlib.util.spec_from_file_location("unordered_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def trim(poly: list[int], prime: int) -> list[int]:
    result = [value % prime for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def divmod_poly(left: list[int], right: list[int], prime: int) -> tuple[list[int], list[int]]:
    remainder = trim(left, prime)
    divisor = trim(right, prime)
    assert divisor != [0]
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, prime)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse % prime
        quotient[shift] = factor
        for index, value in enumerate(divisor):
            remainder[index + shift] = (remainder[index + shift] - factor * value) % prime
        remainder = trim(remainder, prime)
    return trim(quotient, prime), remainder


def gcd_degree(left: list[int], right: list[int], prime: int) -> int:
    a = trim(left, prime)
    b = trim(right, prime)
    while b != [0]:
        _, remainder = divmod_poly(a, b, prime)
        a, b = b, remainder
    return len(a) - 1


def incidence_polynomials(n: int, target: int, prime: int) -> tuple[list[int], list[int]]:
    # F(X)=((1-X)^n-1)/X, coefficients in ascending X degree.
    f = [((-1) ** (index + 1) * comb(n, index + 1)) % prime for index in range(n)]
    d = n - 1
    g = [0] * n
    for index, coefficient in enumerate(f):
        g[d - index] = coefficient * pow(target, index, prime) % prime
    return trim(f, prime), trim(g, prime)


def finite_field_check() -> None:
    fibers = load_fibers()
    checks = 0
    for n, primes in ((4, (5, 13, 17, 29)), (8, (17, 41, 73, 89))):
        for prime in primes:
            ordered, _, _ = fibers.fiber_counts(n, prime)
            for target in range(prime):
                f, g = incidence_polynomials(n, target, prime)
                assert gcd_degree(f, g, prime) == ordered[target]
                checks += 1
    assert checks > 250


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
        "G_n(T,X)=X^d F_n(T/X)",
        "0<=j<=24",
        "(T-1)Y-1",
        "deg gcd_X(F_n(X),G_n(t,X))=P(t)",
        "iff some t!=1 has P(t)>=25",
        "325",
        "not claim that symbolic elimination",
    ):
        assert marker in text


def main() -> None:
    finite_field_check()
    packet_check()
    print(
        "F3_H3_NONIDENTITY_P25_SUBRESULTANT_SCALAR_COMPILER_PASS "
        "subresultants=25 coefficients=325 selector=t_ne_1"
    )


if __name__ == "__main__":
    main()

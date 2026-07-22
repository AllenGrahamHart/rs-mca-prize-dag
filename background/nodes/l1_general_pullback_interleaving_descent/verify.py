#!/usr/bin/env python3
"""Verify the general polynomial-pullback interleaving descent."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_general_pullback_interleaving_descent"


def trim(polynomial: tuple[int, ...]) -> tuple[int, ...]:
    out = list(polynomial)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(tuple(out))


def subtract(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % prime
    return trim(tuple(out))


def multiply(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(tuple(out))


def power(base: tuple[int, ...], exponent: int, prime: int) -> tuple[int, ...]:
    out = (1,)
    for _ in range(exponent):
        out = multiply(out, base, prime)
    return out


def compose(outer: tuple[int, ...], inner: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = (0,)
    for coefficient in reversed(outer):
        out = add(multiply(out, inner, prime), (coefficient,), prime)
    return out


def evaluate(polynomial: tuple[int, ...], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(polynomial):
        out = (out * value + coefficient) % prime
    return out


def decompose(polynomial: tuple[int, ...], pullback: tuple[int, ...], prime: int) -> tuple[tuple[int, ...], ...]:
    pullback = trim(pullback)
    s = len(pullback) - 1
    assert pullback[-1] == 1 and s >= 1
    residual = trim(polynomial)
    components: list[list[int]] = [[0] for _ in range(s)]
    while residual != (0,):
        degree = len(residual) - 1
        residue = degree % s
        quotient_degree = degree // s
        coefficient = residual[-1]
        while len(components[residue]) <= quotient_degree:
            components[residue].append(0)
        components[residue][quotient_degree] = (
            components[residue][quotient_degree] + coefficient
        ) % prime
        term = (0,) * residue + tuple(
            coefficient * value % prime
            for value in power(pullback, quotient_degree, prime)
        )
        residual = subtract(residual, term, prime)
    return tuple(trim(tuple(component)) for component in components)


def reconstruct(components: tuple[tuple[int, ...], ...], pullback: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = (0,)
    for residue, component in enumerate(components):
        term = (0,) * residue + compose(component, pullback, prime)
        out = add(out, term, prime)
    return trim(out)


def verify_decomposition() -> int:
    checks = 0
    prime = 5
    for pullback in ((1, 2, 1), (2, 1, 0, 1)):
        s = len(pullback) - 1
        for k in range(1, 6):
            caps = [max(0, (k - residue + s - 1) // s) for residue in range(s)]
            for coefficients in itertools.product(range(prime), repeat=k):
                polynomial = trim(tuple(coefficients))
                components = decompose(polynomial, pullback, prime)
                assert reconstruct(components, pullback, prime) == polynomial
                for component, cap in zip(components, caps):
                    if component != (0,):
                        assert len(component) - 1 < cap
                checks += 1
    return checks


def verify_complete_fibers() -> int:
    checks = 0
    prime = 17
    domain = tuple(range(1, prime))
    pullback = (0, 3, 1)
    fibers: dict[int, list[int]] = {}
    for x in domain:
        fibers.setdefault(evaluate(pullback, x, prime), []).append(x)
    complete = {label: tuple(points) for label, points in fibers.items() if len(points) == 2}
    assert len(complete) == 7

    def received(x: int) -> int:
        return (pow(x, 5, prime) + 4 * x + 3) % prime

    quotient_received: dict[int, tuple[int, int]] = {}
    for label, (x0, x1) in complete.items():
        slope = (received(x1) - received(x0)) * pow((x1 - x0) % prime, -1, prime) % prime
        intercept = (received(x0) - x0 * slope) % prime
        quotient_received[label] = (intercept, slope)
        checks += 2

    for coefficients in itertools.islice(itertools.product(range(prime), repeat=4), 500):
        polynomial = trim(tuple(coefficients))
        components = decompose(polynomial, pullback, prime)
        for label, points in complete.items():
            full_agreement = all(evaluate(polynomial, x, prime) == received(x) for x in points)
            quotient_agreement = all(
                evaluate(component, label, prime) == target
                for component, target in zip(components, quotient_received[label])
            )
            assert full_agreement == quotient_agreement
            checks += 1
    return checks


def verify_kernel_charge() -> int:
    prime = 5
    labels = (0, 1)
    caps = (4, 3)
    counts: dict[tuple[int, ...], int] = {}
    for first in itertools.product(range(prime), repeat=caps[0]):
        for second in itertools.product(range(prime), repeat=caps[1]):
            key = tuple(evaluate(first, label, prime) for label in labels) + tuple(
                evaluate(second, label, prime) for label in labels
            )
            counts[key] = counts.get(key, 0) + 1
    kappa = sum(max(0, cap - len(labels)) for cap in caps)
    assert len(counts) == prime ** (2 * len(labels))
    assert set(counts.values()) == {prime**kappa}
    return sum(counts.values()) + len(counts)


def main() -> None:
    checks = verify_decomposition() + verify_complete_fibers() + verify_kernel_charge()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["list_subsqrt_interleaving_collapse"]["status"] == "PROVED"
    assert ("list_subsqrt_interleaving_collapse", NODE, "req") in edges
    checks += 3
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "f(X)=sum_(j=0)^(s-1) X^j g_j(P(X))",
        "kappa=sum_(j=0)^(s-1) max(0,k_j-b)",
        "q^kappa L_s(B,K_0,h)",
        "kappa=0",
        "non-smooth label domain",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_GENERAL_PULLBACK_INTERLEAVING_DESCENT_PASS checks={checks}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the full-pullback divisibility/Johnson closure."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_full_pullback_divisibility_johnson_closure"


def verify_dyadic_arithmetic() -> int:
    checks = 0
    for exponent in range(4, 13):
        n = 1 << exponent
        for rate_denominator in (2, 4, 8, 16):
            k = n // rate_denominator
            if k <= 1:
                continue
            for scale_exponent in range(1, exponent + 1):
                s = 1 << scale_exponent
                for ell in range(s, n - k + 2, s):
                    threshold = k + ell - 1
                    assert threshold % s != 0
                    h0 = (threshold + s - 1) // s
                    b = n // s
                    dimension = (k + s - 1) // s
                    degree = dimension - 1
                    if s <= k:
                        assert h0 == (k + ell) // s
                        assert (h0 * h0 > b * degree) == (
                            (k + ell) ** 2 > (k - s) * n
                        )
                    else:
                        assert h0 == ell // s + 1
                        assert dimension == 1 and degree == 0
                        assert h0 * h0 > b * degree
                    if h0 * h0 > b * degree:
                        denominator = h0 * h0 - b * degree
                        numerator = b * (h0 - degree)
                        assert denominator >= 1
                        assert numerator // denominator <= b * b
                    checks += 1
    return checks


def evaluate_linear(coefficients: tuple[int, int], x: int, prime: int) -> int:
    return (coefficients[0] + coefficients[1] * x) % prime


def verify_tiny_interleaved_johnson() -> int:
    prime = 3
    labels = (0, 1, 2)
    codewords = tuple(
        tuple(evaluate_linear(coefficients, x, prime) for x in labels)
        for coefficients in itertools.product(range(prime), repeat=2)
    )
    tuples = tuple(itertools.product(codewords, repeat=2))
    received_symbols = tuple(itertools.product(range(prime), repeat=2))
    maximum = 0
    for received in itertools.product(received_symbols, repeat=len(labels)):
        size = 0
        for first, second in tuples:
            agreement = sum(
                (first[index], second[index]) == received[index]
                for index in range(len(labels))
            )
            size += agreement >= 2
        maximum = max(maximum, size)
    b = 3
    h0 = 2
    degree = 1
    bound = b * (h0 - degree) // (h0 * h0 - b * degree)
    assert maximum <= bound == 3

    for left, right in itertools.combinations(tuples, 2):
        common = sum(
            (left[0][index], left[1][index])
            == (right[0][index], right[1][index])
            for index in range(len(labels))
        )
        assert common <= degree
    return len(received_symbols) ** len(labels) + len(tuples) ** 2


def main() -> None:
    checks = verify_dyadic_arithmetic() + verify_tiny_interleaved_johnson()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_tame_fixed_petal_refinement_census",
        "l1_general_pullback_interleaving_descent",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "a_*=k+sigma=k+ell-1",
        "h_0^2>b d",
        "(k+ell)^2>(k-s)n",
        "floor(b(h_0-d)/(h_0^2-bd)) <= b^2",
        "n b^2 <= n^3",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_FULL_PULLBACK_DIVISIBILITY_JOHNSON_PASS checks={checks}")


if __name__ == "__main__":
    main()

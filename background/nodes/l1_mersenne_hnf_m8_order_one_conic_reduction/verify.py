#!/usr/bin/env python3
"""Reconstruct the h=7 residual and its conic model exactly."""

from __future__ import annotations

import json
import math
import runpy
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_conic_reduction"
DEPENDENCY = "l1_mersenne_hnf_order_one_involution_component_exclusion"
CONSUMER = "l1_mixed_petal_amplification"

Poly = dict[tuple[int, int], Fraction]


def add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for monomial, value in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + value
        if not out[monomial]:
            del out[monomial]
    return out


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (r1, c1), a in left.items():
        for (r2, c2), b in right.items():
            key = (r1 + r2, c1 + c2)
            out[key] = out.get(key, Fraction(0)) + a * b
    return {key: value for key, value in out.items() if value}


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return {key: value * scalar for key, value in poly.items() if value * scalar}


def factor(power: int) -> Poly:
    return {(1, power): Fraction(1), (1, 1): Fraction(-1)}


def convolution(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b_value in enumerate(right):
            out[i + j] += a * b_value
    return out


def linear_combination(*terms: tuple[int, list[int]]) -> list[int]:
    size = max(len(poly) for _, poly in terms)
    out = [0] * size
    for scalar, poly in terms:
        for i, value in enumerate(poly):
            out[i] += scalar * value
    return out


def main() -> None:
    # The four partitions 7, 5+2, 4+3, and 3+2+2.
    phi = scale(factor(7), Fraction(1, 7))
    phi = add(phi, scale(multiply(factor(5), factor(2)), Fraction(1, 10)))
    phi = add(phi, scale(multiply(factor(4), factor(3)), Fraction(1, 12)))
    phi = add(
        phi,
        scale(multiply(factor(3), multiply(factor(2), factor(2))), Fraction(1, 24)),
    )
    integral = scale(phi, Fraction(math.factorial(7)))

    # Divide the known factors rho*c*(c-1)*(c+1) coefficientwise via the
    # already-pinned residual constructor from the dependency.
    dependency_verifier = ROOT / f"background/nodes/{DEPENDENCY}/verify.py"
    namespace = runpy.run_path(str(dependency_verifier))
    quotient = namespace["divide_monomial"](integral, 1, 1)
    quotient = namespace["divide_c_linear"](quotient, 1)
    quotient = namespace["divide_c_linear"](quotient, -1)
    content, residual = namespace["primitive"](quotient)
    assert content == 6
    assert namespace["digest"](residual) == namespace["EXPECTED_DIGESTS"][7]

    expected: Poly = {
        (2, 4): Fraction(35),
        (2, 3): Fraction(-70),
        (2, 2): Fraction(35),
        (1, 4): Fraction(154),
        (1, 3): Fraction(-84),
        (1, 2): Fraction(84),
        (1, 1): Fraction(-154),
        (0, 4): Fraction(120),
        (0, 2): Fraction(120),
        (0, 0): Fraction(120),
    }
    assert residual == expected

    # Polynomial completion-of-square and conic coefficients.
    a_squared = [121, 110, 267, 110, 121]
    b = [1, 0, 1, 0, 1]
    discriminant = [7 * a_squared[i] - 600 * b[i] for i in range(5)]
    assert discriminant == [247, 770, 1269, 770, 247]
    assert [247, 770, 1269 - 2 * 247] == [247, 770, 775]
    assert 7 * 6**2 == 247 - 770 + 775

    denominator = [247, 0, -7]
    z_numerator = [-523, 84, 7]
    w_numerator = [1482, -276, 42]
    cleared_conic = linear_combination(
        (247, convolution(z_numerator, z_numerator)),
        (770, convolution(z_numerator, denominator)),
        (775, convolution(denominator, denominator)),
        (-7, convolution(w_numerator, w_numerator)),
    )
    assert cleared_conic == [0] * len(cleared_conic)
    z_plus_denominator = linear_combination((1, z_numerator), (1, denominator))
    shifted = [0] + z_plus_denominator
    cleared_line = linear_combination(
        (1, w_numerator), (-6, denominator), (-1, shifted)
    )
    assert cleared_line == [0] * len(cleared_line)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(OCR2)", "(OCR4)", "(OCR6)", "(OCR8)", "1269"):
        assert anchor in statement
    for anchor in ("Only four partitions", "Completing the square", "252=7*6^2"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CONIC_REDUCTION_PASS terms=10 charts=3")


if __name__ == "__main__":
    main()

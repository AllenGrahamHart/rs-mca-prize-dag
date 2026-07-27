#!/usr/bin/env python3
"""Verify the exact order-one curve factors and the c=-1 torsion exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_involution_component_exclusion"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"
ROWS = (
    (65536, 8191, 13, 7, 2, 4, 10, 6),
    (1048576, 131071, 17, 7, 2, 4, 10, 6),
    (4194304, 524287, 19, 7, 2, 4, 10, 6),
    (17179869184, 2147483647, 31, 7, 2, 4, 10, 6),
    (131072, 8191, 13, 15, 6, 12, 64, 14),
)
EXPECTED_DIGESTS = {
    7: "6c55b84fd7f69f985ee4a4d59f0c247ede9495da64d229bd504d56e6ee6d9465",
    15: "1e1f72eba3965fa2e33f77ceff7f08b905746beecd376809016452e016adc5d1",
}

Poly = dict[tuple[int, int], Fraction]


def add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for monomial, value in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + value
        if out[monomial] == 0:
            del out[monomial]
    return out


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (rho_left, c_left), a in left.items():
        for (rho_right, c_right), b in right.items():
            monomial = (rho_left + rho_right, c_left + c_right)
            out[monomial] = out.get(monomial, Fraction(0)) + a * b
    return {monomial: value for monomial, value in out.items() if value}


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return {monomial: value * scalar for monomial, value in poly.items() if value * scalar}


def shift(poly: Poly, rho_shift: int, c_shift: int) -> Poly:
    return {
        (rho_degree + rho_shift, c_degree + c_shift): value
        for (rho_degree, c_degree), value in poly.items()
    }


def phi_integral(h: int) -> Poly:
    left: list[Poly] = [{(0, 0): Fraction(1)}]
    right: list[Poly] = [{(0, 0): Fraction(1)}]
    falling = {(0, 0): Fraction(1)}
    rising = {(0, 0): Fraction(1)}
    for degree in range(1, h + 1):
        falling = multiply(falling, {(1, 1): Fraction(1), (0, 0): Fraction(-(degree - 1))})
        rising = multiply(rising, {(1, 0): Fraction(1), (0, 0): Fraction(degree - 1)})
        left.append(scale(falling, Fraction((-1) ** degree, math.factorial(degree))))
        right.append(scale(shift(rising, 0, degree), Fraction(1, math.factorial(degree))))
    phi: Poly = {}
    for index in range(h + 1):
        phi = add(phi, multiply(left[index], right[h - index]))
    integral = scale(phi, Fraction(math.factorial(h)))
    assert all(value.denominator == 1 for value in integral.values())
    return integral


def evaluate_c(poly: Poly, value: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for (rho_degree, c_degree), coefficient in poly.items():
        out[rho_degree] = out.get(rho_degree, Fraction(0)) + coefficient * value**c_degree
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def evaluate_rho(poly: Poly, value: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for (rho_degree, c_degree), coefficient in poly.items():
        out[c_degree] = out.get(c_degree, Fraction(0)) + coefficient * value**rho_degree
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def divide_monomial(poly: Poly, rho_degree: int, c_degree: int) -> Poly:
    assert all(i >= rho_degree and j >= c_degree for i, j in poly)
    return {(i - rho_degree, j - c_degree): value for (i, j), value in poly.items()}


def divide_c_linear(poly: Poly, root: int) -> Poly:
    quotient: Poly = {}
    for rho_degree in {i for i, _ in poly}:
        coefficients = {
            c_degree: value
            for (i, c_degree), value in poly.items()
            if i == rho_degree
        }
        top = max(coefficients)
        q = [Fraction(0)] * top
        q[top - 1] = coefficients.get(top, Fraction(0))
        for degree in range(top - 1, 0, -1):
            q[degree - 1] = coefficients.get(degree, Fraction(0)) + root * q[degree]
        assert coefficients.get(0, Fraction(0)) + root * q[0] == 0
        for c_degree, value in enumerate(q):
            if value:
                quotient[(rho_degree, c_degree)] = value
    return quotient


def degree_data(poly: Poly) -> tuple[int, int, int, int]:
    rho_degree = max(i for i, _ in poly)
    c_degree = max(j for _, j in poly)
    total_degree = max(i + j for i, j in poly)
    return rho_degree, c_degree, total_degree, len(poly)


def primitive(poly: Poly) -> tuple[int, Poly]:
    integers = [int(value) for value in poly.values()]
    content = math.gcd(*[abs(value) for value in integers])
    return content, {monomial: Fraction(int(value) // content) for monomial, value in poly.items()}


def digest(poly: Poly) -> str:
    payload = [
        [rho_degree, c_degree, int(value)]
        for (rho_degree, c_degree), value in sorted(poly.items())
    ]
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    results = json.loads(
        (ROOT / "experiments/prize_resolution/l1_mersenne_order_one_phi_factor_result.json").read_text()
    )
    assert results["status"] == "COMPLETE"
    assert results["peak_mb"] == 88

    checked: dict[int, tuple[int, int, int, int, str]] = {}
    for h in (7, 15):
        integral = phi_integral(h)
        assert evaluate_rho(integral, 0) == {}
        for c_value in (0, 1, -1):
            assert evaluate_c(integral, c_value) == {}
        quotient = divide_monomial(integral, 1, 1)
        quotient = divide_c_linear(quotient, 1)
        quotient = divide_c_linear(quotient, -1)
        content, residual = primitive(quotient)
        rho_degree, c_degree, total_degree, terms = degree_data(residual)
        checked[h] = (rho_degree, c_degree, total_degree, terms, digest(residual))
        assert checked[h][4] == EXPECTED_DIGESTS[h]
        result = next(row for row in results["rows"] if row["h"] == h)
        assert (rho_degree, c_degree, total_degree, terms, content) == (
            result["residual_rho_degree"],
            result["residual_c_degree"],
            result["residual_total_degree"],
            result["residual_terms"],
            result["content"],
        )
        assert result["residual_stdlib_sha256"] == EXPECTED_DIGESTS[h]

    for n, p, q, h, rho_degree, c_degree, terms, content in ROWS:
        assert p == 2**q - 1
        assert pow(2, q, p) == 1 and 2 % p != 1
        assert q > 2 and all(q % divisor for divisor in range(2, math.isqrt(q) + 1))
        assert n & (n - 1) == 0
        assert n % q != 0
        assert pow(2, n, p) != 1
        assert checked[h][:2] == (rho_degree, c_degree)
        assert checked[h][3] == terms
        assert next(row for row in results["rows"] if row["h"] == h)["content"] == content

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_MERSENNE_HNF_ORDER_ONE_INVOLUTION_COMPONENT_EXCLUSION_PASS "
        f"rows={len(ROWS)} h7={checked[7]} h15={checked[15]}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the generic canonical-span criterion and DAG wiring."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    ])


def scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def shift(poly: list[Fraction], amount: int) -> list[Fraction]:
    return [Fraction(0)] * amount + poly


def substitute_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [coefficient * scalar**index for index, coefficient in enumerate(poly)]


def elementary(values: tuple[Fraction, ...], degree: int) -> Fraction:
    coefficients = [Fraction(1)]
    for value in values:
        coefficients = multiply(coefficients, [Fraction(1), value])
    return coefficients[degree]


def exact_span_check() -> None:
    for h in (4, 6, 9):
        b_poly = [Fraction(1), Fraction(2), Fraction(-1), Fraction(3)]
        c_poly = [Fraction(1)] + [Fraction((index % 4) - 1) for index in range(1, h - 2)]
        outer = tuple(map(Fraction, (-6, -1, 2, 5)))
        assert sum(outer) == 0
        alpha = elementary(outer, 2)
        beta = elementary(outer, 3)
        gamma = elementary(outer, 4)
        assert alpha != 0

        b2 = multiply(b_poly, b_poly)
        c2 = multiply(c_poly, c_poly)
        c3 = multiply(c2, c_poly)
        c4 = multiply(c2, c2)
        rbar = add(
            scale(multiply(b2, c2), alpha),
            scale(shift(multiply(b_poly, c3), h), beta),
        )
        rbar = add(rbar, scale(shift(c4, 2 * h), gamma))

        s_poly = add(rbar, scale(multiply(b2, c2), -alpha))
        x_poly = shift(multiply(b_poly, c3), h)
        y_poly = shift(c4, 2 * h)
        extracted_beta = s_poly[h]
        after_beta = add(s_poly, scale(x_poly, -extracted_beta))
        extracted_gamma = after_beta[2 * h]
        remainder = add(after_beta, scale(y_poly, -extracted_gamma))
        assert extracted_beta == beta
        assert extracted_gamma == gamma
        assert remainder == [0]

        quartic = [Fraction(1)]
        for value in outer:
            quartic = multiply(quartic, [value, Fraction(1)])
        assert quartic == [gamma, beta, alpha, Fraction(0), Fraction(1)]

        lam = Fraction(2)
        b_scaled = substitute_scale(b_poly, lam)
        c_scaled = substitute_scale(c_poly, lam)
        alpha_scaled = lam ** (2 * h) * alpha
        beta_scaled = lam ** (3 * h) * beta
        gamma_scaled = lam ** (4 * h) * gamma
        rbar_scaled = scale(substitute_scale(rbar, lam), lam ** (2 * h))
        reconstructed = add(
            scale(multiply(multiply(b_scaled, b_scaled), multiply(c_scaled, c_scaled)), alpha_scaled),
            scale(shift(multiply(b_scaled, multiply(multiply(c_scaled, c_scaled), c_scaled)), h), beta_scaled),
        )
        reconstructed = add(
            reconstructed,
            scale(shift(multiply(multiply(c_scaled, c_scaled), multiply(c_scaled, c_scaled)), 2 * h), gamma_scaled),
        )
        assert rbar_scaled == reconstructed


def strictness_fixture() -> None:
    # E=1+z^4 divides 1-z^24 and has the required primary contact at 2h=8.
    h = 4
    b_poly = [Fraction(1), 0, 0, 0, Fraction(-1, 4)]
    b2 = multiply(b_poly, b_poly)
    b4 = multiply(b2, b2)
    quotient = [Fraction(0)] * 21
    for index in range(6):
        quotient[4 * index] = Fraction((-1) ** index)
    residual = add(quotient, scale(b4, -1))
    assert next(index for index, value in enumerate(residual) if value) == 2 * h
    rbar = residual[2 * h:]
    alpha = rbar[0]
    c_poly = [Fraction(1)]
    s_poly = add(rbar, scale(b2, -alpha))
    x_poly = shift(b_poly, h)
    beta = s_poly[h]
    after_beta = add(s_poly, scale(x_poly, -beta))
    gamma = after_beta[2 * h]
    final = add(after_beta, scale(shift(c_poly, 2 * h), -gamma))
    assert alpha == Fraction(5, 8)
    assert beta == Fraction(-5, 8)
    assert gamma == Fraction(205, 256)
    assert [(index, value) for index, value in enumerate(final) if value] == [
        (12, Fraction(-1)),
    ]


def official_arithmetic_check() -> None:
    s = 1 << 37
    d = 4 * s
    r = s - 1
    h = (s // 2) + 1
    v = h - 3
    assert d == 1 << 39
    assert r == 2 * h - 3
    assert v == (1 << 36) - 2
    assert 2 * h == s + 2


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "S=beta X+gamma Y",
        "beta=[z^h]S",
        "fractional-linear image",
        "reconstructs the generic",
        "normalized to one",
        "does not prove that the certifier always rejects",
    ):
        assert marker in statement


def main() -> None:
    exact_span_check()
    strictness_fixture()
    official_arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_CANONICAL_SPAN_PASS "
        "span_dimension=2 outer_coefficients_unique=3 strict_fixture_reject=1"
    )


if __name__ == "__main__":
    main()

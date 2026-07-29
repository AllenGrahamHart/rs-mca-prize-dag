#!/usr/bin/env python3
"""Verify the cofactor-514 energy-ten profile-(6,1) cubic exclusion."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


sys.set_int_max_str_digits(100_000)

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m514_e10_profile61_cubic_exclusion"
PARENT = "e1_s18_m514_hermite_two_profile_exclusion"
TARGETS = {
    "e1_profile018_m514_five_ideal_occupancy",
    "e1_official_low_square_mass_pair_budget",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 514
TERMS = 96
MARGIN_NUM_SHA256 = "952d22b394697036ca2fdca96a8aefb2651dc7f72d51d9596e1e9ddc126f2569"
MARGIN_DEN_SHA256 = "c2413142f8ae5f57569b9fd7ab666ad23adf76b95360115cc093cd238ce2acb0"


def unit_log_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    """Bound log(value) for 1 <= value <= 2 by the atanh series."""
    assert 1 <= value <= 2
    z = (value - 1) / (value + 1)
    total = Fraction(0)
    power = z
    for index in range(TERMS):
        total += power / (2 * index + 1)
        power *= z * z
    lower = 2 * total
    upper = lower + 2 * power / ((2 * TERMS + 1) * (1 - z * z))
    return lower, upper


def log_interval(value: Fraction | int) -> tuple[Fraction, Fraction]:
    value = Fraction(value)
    assert value >= 1
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    while value < 2**exponent:
        exponent -= 1
    while value >= 2 ** (exponent + 1):
        exponent += 1
    reduced = value / 2**exponent
    lower, upper = unit_log_interval(reduced)
    log2_lower, log2_upper = unit_log_interval(Fraction(2))
    return (
        lower + exponent * log2_lower,
        upper + exponent * log2_upper,
    )


def add(left: tuple[Fraction, ...], right: tuple[Fraction, ...]):
    return tuple(a + b for a, b in zip(left, right))


def scale(value: tuple[Fraction, ...], factor: Fraction):
    return tuple(factor * item for item in value)


def main() -> None:
    # The two nested absolute layers have sizes 14 and 2.
    layers = (14, 2)
    phi = 0
    for left in layers:
        for middle in layers:
            for right in layers:
                phi += min(
                    left * middle - min(left, middle),
                    left * right - min(left, right),
                    middle * right - min(middle, right),
                )
    assert phi == 268
    m3_cap = phi - phi % 6
    assert m3_cap == 264

    # Coefficients are triples: coefficient of log(a), log(b), and 1.
    coefficients = (
        (Fraction(-71825, 16384), Fraction(88209, 16384), Fraction(-85024, 16384)),
        (Fraction(13803075, 17571840), Fraction(-13803075, 17571840), Fraction(11695712, 17571840)),
        (Fraction(-315315, 8785920), Fraction(315315, 8785920), Fraction(-238688, 8785920)),
        (Fraction(2145, 4392960), Fraction(-2145, 4392960), Fraction(1568, 4392960)),
    )
    a = Fraction(33, 2)
    b = Fraction(65, 2)

    def evaluate(point: Fraction) -> tuple[Fraction, ...]:
        total = (Fraction(0), Fraction(0), Fraction(0))
        for degree, coefficient in enumerate(coefficients):
            total = add(total, scale(coefficient, point**degree))
        return total

    def derivative(point: Fraction) -> tuple[Fraction, ...]:
        total = (Fraction(0), Fraction(0), Fraction(0))
        for degree, coefficient in enumerate(coefficients[1:], start=1):
            total = add(total, scale(coefficient, degree * point ** (degree - 1)))
        return total

    assert evaluate(a) == (1, 0, 0)
    assert derivative(a) == (0, 0, 1 / a)
    assert evaluate(b) == (0, 1, 0)
    assert derivative(b) == (0, 0, 1 / b)

    raw_moments = (1, 18, 18**2 + 20, 18**3 + 3 * 18 * 20 + m3_cap)
    mean = (Fraction(0), Fraction(0), Fraction(0))
    for coefficient, moment in zip(coefficients, raw_moments):
        mean = add(mean, scale(coefficient, moment))
    assert mean == (
        Fraction(14971, 16384),
        Fraction(1413, 16384),
        Fraction(7819, 1098240),
    )

    log_a = log_interval(a)
    log_b = log_interval(b)
    gamma_numerator_lower = Fraction(1568) + 2145 * (log_a[0] - log_b[1])
    assert gamma_numerator_lower > 0

    mean_upper = mean[0] * log_a[1] + mean[1] * log_b[1] + mean[2]
    target_lower = log_interval(COFACTOR * P_MIN)[0] / 64
    margin = target_lower - mean_upper
    assert margin > 0
    assert margin.numerator.bit_length() == 27800
    assert margin.denominator.bit_length() == 27814
    assert hashlib.sha256(str(margin.numerator).encode("ascii")).hexdigest() == MARGIN_NUM_SHA256
    assert hashlib.sha256(str(margin.denominator).encode("ascii")).hexdigest() == MARGIN_DEN_SHA256

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("(10;6,1,0)", "M_3<=264", "twelve"):
        assert text in statement
    for text in ("27800", "27814", "33/2", "65/2"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges

    print(
        "E1_S18_M514_E10_PROFILE61_CUBIC_EXCLUSION_PASS "
        "phi=268 m3_cap=264 survivors=12 margin_bits=27800/27814"
    )


if __name__ == "__main__":
    main()

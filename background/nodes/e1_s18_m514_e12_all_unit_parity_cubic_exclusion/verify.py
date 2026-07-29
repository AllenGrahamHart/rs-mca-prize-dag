#!/usr/bin/env python3
"""Verify the cofactor-514 all-unit energy-twelve exclusion."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


sys.set_int_max_str_digits(100_000)

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m514_e12_all_unit_parity_cubic_exclusion"
PARENTS = {
    "e1_profile210_m514_parity_trace_cap",
    "e1_prize_field_floor_even_norm_exclusion",
}
TARGETS = {
    "e1_profile018_m514_five_ideal_occupancy",
    "e1_official_low_square_mass_pair_budget",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 514
TERMS = 96
MARGIN_NUM_SHA256 = "bf0c4b435d768c921d73cef835f9f385390738d9f98650c4b8d62102ce1564a9"
MARGIN_DEN_SHA256 = "e19ab847a193d23d88528b283bfd800bae43816515738c3ba11580e0fff1857b"


def unit_log_interval(value: Fraction) -> tuple[Fraction, Fraction]:
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
    return lower + exponent * log2_lower, upper + exponent * log2_upper


def add(left: tuple[Fraction, ...], right: tuple[Fraction, ...]):
    return tuple(a + b for a, b in zip(left, right))


def scale(value: tuple[Fraction, ...], factor: Fraction):
    return tuple(factor * item for item in value)


def main() -> None:
    parity_rows = []
    for odd_lags in range(1, 13, 2):
        even_oriented = 2 * (12 - odd_lags)
        bound = even_oriented * (even_oriented - 1) + 3 * min(
            2 * even_oriented * odd_lags,
            4 * odd_lags**2 - 2 * odd_lags,
        )
        parity_rows.append((odd_lags, bound))
    assert parity_rows == [(1, 468), (3, 396), (5, 452), (7, 510), (9, 354), (11, 134)]
    m3_cap = max(bound for _, bound in parity_rows)
    assert m3_cap == 510

    # Coefficients are triples: coefficient of log(17), log(40), and 1.
    coefficients = (
        (Fraction(-17600, 12167), Fraction(29767, 12167), Fraction(-43447, 12167)),
        (Fraction(2774400, 8273560), Fraction(-2774400, 8273560), Fraction(3367959, 8273560)),
        (Fraction(-58140, 4136780), Fraction(58140, 4136780), Fraction(-59087, 4136780)),
        (Fraction(1360, 8273560), Fraction(-1360, 8273560), Fraction(1311, 8273560)),
    )

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

    assert evaluate(Fraction(17)) == (1, 0, 0)
    assert derivative(Fraction(17)) == (0, 0, Fraction(1, 17))
    assert evaluate(Fraction(40)) == (0, 1, 0)
    assert derivative(Fraction(40)) == (0, 0, Fraction(1, 40))

    raw_moments = (1, 18, 18**2 + 24, 18**3 + 3 * 18 * 24 + m3_cap)
    mean = (Fraction(0), Fraction(0), Fraction(0))
    for coefficient, moment in zip(coefficients, raw_moments):
        mean = add(mean, scale(coefficient, moment))
    assert mean == (
        Fraction(11608, 12167),
        Fraction(559, 12167),
        Fraction(-173, 44965),
    )

    log17 = log_interval(17)
    log40 = log_interval(40)
    gamma_numerator_lower = Fraction(1311) + 1360 * (log17[0] - log40[1])
    assert gamma_numerator_lower > 0

    mean_upper = mean[0] * log17[1] + mean[1] * log40[1] + mean[2]
    target_lower = log_interval(COFACTOR * P_MIN)[0] / 64
    margin = target_lower - mean_upper
    assert margin > 0
    assert margin.numerator.bit_length() == 27282
    assert margin.denominator.bit_length() == 27294
    assert hashlib.sha256(str(margin.numerator).encode("ascii")).hexdigest() == MARGIN_NUM_SHA256
    assert hashlib.sha256(str(margin.denominator).encode("ascii")).hexdigest() == MARGIN_DEN_SHA256

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("(12;12,0,0)", "M_3<=510", "eleven"):
        assert text in statement
    for text in ("27282", "27294", "17", "40"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges

    print(
        "E1_S18_M514_E12_ALL_UNIT_PARITY_CUBIC_EXCLUSION_PASS "
        "m3_cap=510 survivors=11 margin_bits=27282/27294"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the cofactor-514 all-unit energy-eleven exclusion."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys


sys.set_int_max_str_digits(100_000)

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m514_e11_all_unit_dyadic_cubic_exclusion"
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
MARGIN_NUM_SHA256 = "6c345f4540ddd77b415303c050f65e393c1ff3afe64e0cc4f2b68982bcff3a57"
MARGIN_DEN_SHA256 = "7b96452bc48f7cb9caa1c9bed568b5b15f41e3ca92deb88e26529c58350a3eea"


@lru_cache(maxsize=None)
def relation_cap(exponent: int, size: int) -> int | None:
    if size == 0:
        return 0
    if size < 0 or size % 2 or size > 2**exponent - 2 or exponent <= 1:
        return None
    best: int | None = None
    for odd_size in range(0, size + 1, 2):
        if odd_size > 2 ** (exponent - 1):
            continue
        even_size = size - odd_size
        child = relation_cap(exponent - 1, even_size)
        if child is None:
            continue
        candidate = child + 3 * min(
            even_size * odd_size,
            odd_size**2 - odd_size,
        )
        best = candidate if best is None else max(best, candidate)
    return best


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
    assert [relation_cap(6, size) for size in (20, 16, 12, 8, 4, 0)] == [
        348,
        210,
        114,
        42,
        6,
        0,
    ]
    top_rows = []
    for odd_lags in range(1, 12, 2):
        odd_size = 2 * odd_lags
        even_size = 22 - odd_size
        child = relation_cap(6, even_size)
        assert child is not None
        bound = child + 3 * min(
            even_size * odd_size,
            odd_size**2 - odd_size,
        )
        top_rows.append((odd_lags, bound))
    assert top_rows == [(1, 354), (3, 300), (5, 384), (7, 378), (9, 222), (11, 0)]
    m3_cap = max(bound for _, bound in top_rows)
    assert m3_cap == 384

    # Coefficients are triples: coefficient of log(17), log(37), and 1.
    coefficients = (
        (Fraction(-9583, 4000), Fraction(13583, 4000), Fraction(-16580, 4000)),
        (Fraction(1186923, 2516000), Fraction(-1186923, 2516000), Fraction(1234980, 2516000)),
        (Fraction(-50949, 2516000), Fraction(50949, 2516000), Fraction(-45740, 2516000)),
        (Fraction(629, 2516000), Fraction(-629, 2516000), Fraction(540, 2516000)),
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
    assert evaluate(Fraction(37)) == (0, 1, 0)
    assert derivative(Fraction(37)) == (0, 0, Fraction(1, 37))

    raw_moments = (1, 18, 18**2 + 22, 18**3 + 3 * 18 * 22 + m3_cap)
    mean = (Fraction(0), Fraction(0), Fraction(0))
    for coefficient, moment in zip(coefficients, raw_moments):
        mean = add(mean, scale(coefficient, moment))
    assert mean == (
        Fraction(3761, 4000),
        Fraction(239, 4000),
        Fraction(-1353, 125800),
    )

    log17 = log_interval(17)
    log37 = log_interval(37)
    gamma_numerator_lower = Fraction(540) + 629 * (log17[0] - log37[1])
    assert gamma_numerator_lower > 0

    mean_upper = mean[0] * log17[1] + mean[1] * log37[1] + mean[2]
    target_lower = log_interval(COFACTOR * P_MIN)[0] / 64
    margin = target_lower - mean_upper
    assert margin > 0
    assert margin.numerator.bit_length() == 27836
    assert margin.denominator.bit_length() == 27849
    assert hashlib.sha256(str(margin.numerator).encode("ascii")).hexdigest() == MARGIN_NUM_SHA256
    assert hashlib.sha256(str(margin.denominator).encode("ascii")).hexdigest() == MARGIN_DEN_SHA256

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("(11;11,0,0)", "M_3<=384", "ten"):
        assert text in statement
    for text in ("27836", "27849", "U_6(22-2o)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    for target in TARGETS:
        expected = (
            "CONDITIONAL"
            if target == "e1_profile018_m514_five_ideal_occupancy"
            else "TARGET"
        )
        assert nodes[target]["status"] == expected
        assert (NODE, target, "ev") in edges

    print(
        "E1_S18_M514_E11_ALL_UNIT_DYADIC_CUBIC_EXCLUSION_PASS "
        "m3_cap=384 survivors=10 margin_bits=27836/27849"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the analytic m=16 high-variance exclusion."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m16_high_variance_exclusion"
BP = 317494674775468773183020924238786383963
PARENT = "e1_prize_n256_s18_variance_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_log_interval(value: Fraction, terms: int = 20) -> tuple[Fraction, Fraction]:
    """Atanh-series interval for log(value), with 1 <= value <= 2."""
    assert 1 <= value <= 2
    if value == 1:
        return Fraction(0), Fraction(0)
    t = (value - 1) / (value + 1)
    partial = sum(
        (2 * t ** (2 * index + 1)) / (2 * index + 1)
        for index in range(terms)
    )
    tail = (
        2
        * t ** (2 * terms + 1)
        / ((2 * terms + 1) * (1 - t * t))
    )
    return partial, partial + tail


def log_interval(value: Fraction, terms: int = 20) -> tuple[Fraction, Fraction]:
    assert value > 0
    if value < 1:
        lower, upper = log_interval(1 / value, terms)
        return -upper, -lower
    power = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        power += 1
    low_two, high_two = raw_log_interval(Fraction(2), terms)
    low_reduced, high_reduced = raw_log_interval(reduced, terms)
    return (
        power * low_two + low_reduced,
        power * high_two + high_reduced,
    )


def verify_chord_bound() -> int:
    checks = 0
    for fours in range(7):
        for twos in range(9):
            for ones in range(2):
                for neg_fours in range(fours + 1):
                    for neg_twos in range(twos + 1):
                        for neg_ones in range(ones + 1):
                            weights = 4 * fours + 2 * twos + ones
                            signed = abs(
                                4 * (fours - 2 * neg_fours)
                                + 2 * (twos - 2 * neg_twos)
                                + ones
                                - 2 * neg_ones
                            )
                            square_mass = 16 * fours + 4 * twos + ones
                            assert square_mass - signed * signed <= 4 * (
                                weights - signed
                            )
                            checks += 1
    assert 6 * 4 + 8 * 2 + 1 == 41
    assert 6 * 16 + 8 * 4 + 1 == 129
    assert 4 * 41 - 129 == 35
    return checks + 3


def layer_profiles(energy: int, l1: int) -> list[tuple[int, ...]]:
    profiles: list[tuple[int, ...]] = []
    maximum_level = 1
    while (maximum_level + 1) ** 2 <= energy:
        maximum_level += 1

    def visit(
        level: int,
        remaining_energy: int,
        remaining_l1: int,
        remaining_classes: int,
        reverse_profile: list[int],
    ) -> None:
        if level == 0:
            if remaining_energy == 0:
                profiles.append(tuple(reversed(reverse_profile)))
            return
        maximum = min(
            remaining_energy // (level * level),
            remaining_l1 // level,
            remaining_classes,
        )
        for count in range(maximum + 1):
            visit(
                level - 1,
                remaining_energy - count * level * level,
                remaining_l1 - count * level,
                remaining_classes - count,
                reverse_profile + [count],
            )

    visit(maximum_level, energy, l1, 15, [])
    return profiles


def phi(profile: tuple[int, ...]) -> int:
    layers = [
        2 * sum(profile[level - 1 :])
        for level in range(1, len(profile) + 1)
    ]
    total = 0
    for first, second, third in product(layers, repeat=3):
        total += min(
            first * second - min(first, second),
            first * third - min(first, third),
            second * third - min(second, third),
        )
    return total


Linear = tuple[Fraction, Fraction, Fraction]


def add(*values: Linear) -> Linear:
    return tuple(sum(value[index] for value in values) for index in range(3))  # type: ignore[return-value]


def scale(value: Linear, scalar: int | Fraction) -> Linear:
    return tuple(scalar * entry for entry in value)  # type: ignore[return-value]


def verify_cubic() -> int:
    profiles = layer_profiles(65, 25)
    assert len(profiles) == 73
    scored = [(phi(profile), profile) for profile in profiles]
    assert max(scored) == (5950, (0, 5, 5, 0, 0, 0, 0, 0))

    one: Linear = (Fraction(1), Fraction(0), Fraction(0))
    log_15: Linear = (Fraction(0), Fraction(1), Fraction(0))
    log_66: Linear = (Fraction(0), Fraction(0), Fraction(1))
    coefficients: tuple[Linear, ...] = (
        add(scale(log_15, Fraction(3388, 4913)), scale(log_66, Fraction(1525, 4913)), scale(one, Fraction(-509, 289))),
        add(scale(log_15, Fraction(220, 4913)), scale(log_66, Fraction(-220, 4913)), scale(one, Fraction(5571, 31790))),
        add(scale(log_15, Fraction(-9, 4913)), scale(log_66, Fraction(9, 4913)), scale(one, Fraction(-619, 143055))),
        add(scale(log_15, Fraction(2, 132651)), scale(log_66, Fraction(-2, 132651)), scale(one, Fraction(1, 31790))),
    )

    def polynomial(value: int) -> Linear:
        return add(*(scale(coefficient, value**index) for index, coefficient in enumerate(coefficients)))

    def derivative(value: int) -> Linear:
        return add(*(scale(coefficients[index], index * value ** (index - 1)) for index in range(1, 4)))

    assert polynomial(15) == log_15
    assert derivative(15) == scale(one, Fraction(1, 15))
    assert polynomial(66) == log_66
    assert derivative(66) == scale(one, Fraction(1, 66))

    mean = add(
        coefficients[0],
        scale(coefficients[1], 18),
        scale(coefficients[2], 454),
        scale(coefficients[3], 18802),
    )
    assert mean == (
        Fraction(2879, 143055),
        Fraction(125678, 132651),
        Fraction(6973, 132651),
    )

    _, log_ratio_upper = log_interval(Fraction(22, 5))
    assert Fraction(459) - 220 * log_ratio_upper > 0

    _, log_15_upper = log_interval(Fraction(15))
    _, log_66_upper = log_interval(Fraction(66))
    log_2_lower, _ = log_interval(Fraction(2))
    mean_upper = (
        mean[0] + mean[1] * log_15_upper + mean[2] * log_66_upper
    )
    assert mean_upper < Fraction(1299, 320) * log_2_lower

    profiles_114 = layer_profiles(57, 23)
    profiles_122 = layer_profiles(61, 23)
    assert len(profiles_114) == 52
    assert len(profiles_122) == 57
    assert max((phi(profile), profile) for profile in profiles_114) == (
        4702,
        (1, 5, 4, 0, 0, 0, 0),
    )
    assert max((phi(profile), profile) for profile in profiles_122) == (
        5118,
        (0, 4, 5, 0, 0, 0, 0),
    )

    log_62: Linear = (Fraction(0), Fraction(0), Fraction(1))
    coefficients_62: tuple[Linear, ...] = (
        add(scale(log_15, Fraction(65348, 103823)), scale(log_62, Fraction(38475, 103823)), scale(one, Fraction(-191243, 103823))),
        add(scale(log_15, Fraction(5189400, 96555390)), scale(log_62, Fraction(-5189400, 96555390)), scale(one, Fraction(18091381, 96555390))),
        add(scale(log_15, Fraction(-107415, 48277695)), scale(log_62, Fraction(107415, 48277695)), scale(one, Fraction(-234953, 48277695))),
        add(scale(log_15, Fraction(1860, 96555390)), scale(log_62, Fraction(-1860, 96555390)), scale(one, Fraction(3619, 96555390))),
    )

    def polynomial_62(value: int) -> Linear:
        return add(*(scale(coefficient, value**index) for index, coefficient in enumerate(coefficients_62)))

    def derivative_62(value: int) -> Linear:
        return add(*(scale(coefficients_62[index], index * value ** (index - 1)) for index in range(1, 4)))

    assert polynomial_62(15) == log_15
    assert derivative_62(15) == scale(one, Fraction(1, 15))
    assert polynomial_62(62) == log_62
    assert derivative_62(62) == scale(one, Fraction(1, 62))

    _, log_62_upper = log_interval(Fraction(62))
    _, log_62_over_15_upper = log_interval(Fraction(62, 15))
    assert Fraction(3619) - 1860 * log_62_over_15_upper > 0
    expected_rows = (
        (
            114,
            16690,
            (
                Fraction(5045, 205437),
                Fraction(97990, 103823),
                Fraction(5833, 103823),
            ),
        ),
        (
            122,
            17538,
            (
                Fraction(17881, 1027185),
                Fraction(97838, 103823),
                Fraction(5985, 103823),
            ),
        ),
    )
    for variance, third_moment, expected_mean in expected_rows:
        mean_62 = add(
            coefficients_62[0],
            scale(coefficients_62[1], 18),
            scale(coefficients_62[2], 324 + variance),
            scale(coefficients_62[3], third_moment),
        )
        assert mean_62 == expected_mean
        upper = (
            mean_62[0]
            + mean_62[1] * log_15_upper
            + mean_62[2] * log_62_upper
        )
        assert upper < Fraction(1299, 320) * log_2_lower

    assert 61 % 2 == 1 and 24 % 2 == 0
    return (
        len(profiles)
        + len(scored)
        + len(profiles_114)
        + len(profiles_122)
        + 20
    )


def verify_quadratics() -> int:
    rows = (
        (138, 69, 26, 70, 1767),
        (146, 73, 27, 72, 1808),
        (154, 77, 28, 74, 1848),
        (162, 81, 29, 76, 1888),
        (170, 85, 30, 78, 1929),
        (178, 89, 31, 80, 1969),
    )
    log_2_lower, _ = log_interval(Fraction(2))
    _, log_18_upper = log_interval(Fraction(18))
    checks = 0
    for variance, energy, l1, bound, denominator in rows:
        assert energy == variance // 2
        assert l1 == (energy + 35) // 4
        assert bound == 18 + 2 * l1
        assert Fraction(18) < Fraction(denominator, 36) < Fraction(bound)
        endpoint = Fraction(bound - 18, 18) - Fraction(
            (bound - 18) ** 2, denominator
        )
        _, endpoint_log_upper = log_interval(Fraction(bound, 18))
        assert endpoint > endpoint_log_upper
        norm_upper = 64 * log_18_upper - Fraction(64 * variance, denominator)
        assert norm_upper < Fraction(1299, 5) * log_2_lower
        checks += 7
    return checks


def main() -> None:
    pins = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    checks = 0
    for key, value in pins.items():
        if key.endswith("_file"):
            assert digest(ROOT / value) == pins[key[:-5] + "_sha256"]
            checks += 1
    assert pins["planning_census_load_bearing"] is False
    checks += 1

    primary = json.loads((ROOT / pins["planning_result_file"]).read_text())
    audit = json.loads((ROOT / pins["planning_audit_result_file"]).read_text())
    assert primary["complete"] is True and not primary["errors"]
    assert audit["complete"] is True and not audit["errors"]
    assert primary["totals"] == audit["totals"]
    assert primary["totals"]["combination_count"] == 10009125
    assert primary["totals"]["signed_vector_count"] == 320292000
    assert primary["totals"]["energy_counts"][0] == 0
    assert sum(primary["totals"]["energy_counts"][:13]) == 540332
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    checks += 3

    checks += verify_chord_bound()
    checks += verify_cubic()
    checks += verify_quadratics()
    prime_floor = BP * 2**128
    assert (16 * prime_floor) ** 5 > 2**1299
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert "V in {114,122,130,138,146,154,162,170,178}" in statement
    assert "Phi(n)<=5950" in proof
    assert "10<=V<=106" in statement
    checks += 3
    print(f"E1_PRIZE_N256_S18_M16_HIGH_VARIANCE_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()

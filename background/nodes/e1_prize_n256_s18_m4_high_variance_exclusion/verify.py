#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) m=4 high-variance exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m4_high_variance_exclusion"
PARENT = "e1_prize_n256_s18_variance_cofactor_windows"
BP = 317494674775468773183020924238786383963
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
Linear = tuple[Fraction, Fraction, Fraction]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_log_interval(value: Fraction, terms: int = 20) -> tuple[Fraction, Fraction]:
    assert 1 <= value <= 2
    if value == 1:
        return Fraction(0), Fraction(0)
    t = (value - 1) / (value + 1)
    partial = sum(
        2 * t ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    tail = 2 * t ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - t * t)
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
    return power * low_two + low_reduced, power * high_two + high_reduced


def add(*values: Linear) -> Linear:
    return tuple(sum(value[i] for value in values) for i in range(3))  # type: ignore[return-value]


def scale(value: Linear, scalar: int | Fraction) -> Linear:
    return tuple(scalar * entry for entry in value)  # type: ignore[return-value]


def linear_interval(value: Linear, a: int, b: int) -> tuple[Fraction, Fraction]:
    intervals = ((Fraction(0), Fraction(0)), log_interval(Fraction(a)), log_interval(Fraction(b)))
    lower = value[0]
    upper = value[0]
    for coefficient, (log_lower, log_upper) in zip(value[1:], intervals[1:]):
        if coefficient >= 0:
            lower += coefficient * log_lower
            upper += coefficient * log_upper
        else:
            lower += coefficient * log_upper
            upper += coefficient * log_lower
    return lower, upper


def hermite_coefficients(a: int, b: int) -> tuple[Linear, ...]:
    matrix = [
        [Fraction(1), Fraction(a), Fraction(a * a), Fraction(a**3)],
        [Fraction(0), Fraction(1), Fraction(2 * a), Fraction(3 * a * a)],
        [Fraction(1), Fraction(b), Fraction(b * b), Fraction(b**3)],
        [Fraction(0), Fraction(1), Fraction(2 * b), Fraction(3 * b * b)],
    ]
    rhs: list[Linear] = [
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1, a), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(1, b), Fraction(0), Fraction(0)),
    ]
    for column in range(4):
        pivot = next(row for row in range(column, 4) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        rhs[column], rhs[pivot] = rhs[pivot], rhs[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        rhs[column] = scale(rhs[column], 1 / divisor)
        for row in range(4):
            if row == column or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                left - factor * right
                for left, right in zip(matrix[row], matrix[column])
            ]
            rhs[row] = add(rhs[row], scale(rhs[column], -factor))
    assert matrix == [
        [Fraction(int(i == j)) for j in range(4)] for i in range(4)
    ]
    return tuple(rhs)


def polynomial(coefficients: tuple[Linear, ...], value: int) -> Linear:
    return add(*(
        scale(coefficient, value**index)
        for index, coefficient in enumerate(coefficients)
    ))


def derivative(coefficients: tuple[Linear, ...], value: int) -> Linear:
    return add(*(
        scale(coefficients[index], index * value ** (index - 1))
        for index in range(1, 4)
    ))


def verify_hermite_row(variance: int, maximum_m3: int, a: int, b: int) -> int:
    coefficients = hermite_coefficients(a, b)
    log_a: Linear = (Fraction(0), Fraction(1), Fraction(0))
    log_b: Linear = (Fraction(0), Fraction(0), Fraction(1))
    one: Linear = (Fraction(1), Fraction(0), Fraction(0))
    assert polynomial(coefficients, a) == log_a
    assert derivative(coefficients, a) == scale(one, Fraction(1, a))
    assert polynomial(coefficients, b) == log_b
    assert derivative(coefficients, b) == scale(one, Fraction(1, b))
    cubic_lower, _ = linear_interval(coefficients[3], a, b)
    assert cubic_lower > 0
    mean = add(
        coefficients[0],
        scale(coefficients[1], 18),
        scale(coefficients[2], 324 + variance),
        scale(coefficients[3], 5832 + 54 * variance + maximum_m3),
    )
    _, mean_upper = linear_interval(mean, a, b)
    log_two_lower, _ = log_interval(Fraction(2))
    assert mean_upper < Fraction(1289, 320) * log_two_lower
    return 7


def verify_chord_bound() -> int:
    checks = 0
    for fours in range(7):
        for twos in range(9):
            for ones in range(2):
                for neg_fours in range(fours + 1):
                    for neg_twos in range(twos + 1):
                        for neg_ones in range(ones + 1):
                            weight = 4 * fours + 2 * twos + ones
                            signed = abs(
                                4 * (fours - 2 * neg_fours)
                                + 2 * (twos - 2 * neg_twos)
                                + ones - 2 * neg_ones
                            )
                            square_mass = 16 * fours + 4 * twos + ones
                            assert square_mass - signed * signed <= 4 * (
                                weight - signed
                            )
                            checks += 1
    assert 6 * 4 + 8 * 2 + 1 == 41
    assert 6 * 16 + 8 * 4 + 1 == 129
    assert 4 * 41 - 129 == 35
    return checks + 3


def layer_profiles(energy: int, l1: int) -> list[tuple[int, ...]]:
    profiles: list[tuple[int, ...]] = []
    maximum_level = math.isqrt(energy)

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
    return sum(
        min(
            first * second - min(first, second),
            first * third - min(first, third),
            second * third - min(second, third),
        )
        for first, second, third in product(layers, repeat=3)
    )


def verify_layer_rows() -> int:
    rows = (
        (170, 85, 29, 139, 9286, 15, 76),
        (178, 89, 31, 169, 10374, 15, 79),
        (186, 93, 31, 183, 10594, 15, 78),
        (194, 97, 33, 211, 11750, 15, 82),
    )
    checks = 0
    for variance, energy, l1, count, cap, a, b in rows:
        assert energy == variance // 2
        assert l1 <= (energy + 35) // 4 and l1 % 2 == energy % 2
        profiles = layer_profiles(energy, l1)
        assert len(profiles) == count
        assert max(phi(profile) for profile in profiles) == cap
        checks += verify_hermite_row(variance, cap, a, b) + count + 4
    return checks


def verify_quadratic_rows() -> int:
    rows = (
        (202, 101, 33, 84, 2049),
        (210, 105, 35, 88, 2129),
        (218, 109, 35, 88, 2129),
        (226, 113, 37, 92, 2209),
    )
    log_two_lower, _ = log_interval(Fraction(2))
    _, log_18_upper = log_interval(Fraction(18))
    checks = 0
    for variance, energy, l1, bound, denominator in rows:
        assert energy == variance // 2
        assert l1 <= (energy + 35) // 4 and l1 % 2 == energy % 2
        assert bound == 18 + 2 * l1
        assert Fraction(18) < Fraction(denominator, 36) < Fraction(bound)
        endpoint = Fraction(bound - 18, 18) - Fraction(
            (bound - 18) ** 2, denominator
        )
        _, endpoint_log_upper = log_interval(Fraction(bound, 18))
        assert endpoint > endpoint_log_upper
        norm_upper = 64 * log_18_upper - Fraction(64 * variance, denominator)
        assert norm_upper < Fraction(1289, 5) * log_two_lower
        checks += 7
    return checks


def row_signature(packet: dict) -> list[tuple[int, int, int, int | None, int | None]]:
    return [
        (
            row["variance"], row["energy"], row["count"],
            row["minimum_m3"], row["maximum_m3"],
        )
        for row in packet["rows"]
    ]


def main() -> None:
    checks = 0
    pins = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pins.items():
        if key.endswith("_file"):
            assert digest(ROOT / value) == pins[key[:-5] + "_sha256"]
            checks += 1
    assert pins["counts_load_bearing"] is False

    expected_counts = [
        0, 16, 16, 100, 144, 420, 820, 17084, 2776, 24268,
        36520, 417876, 38920, 243340, 299040, 2874126, 161456,
        638428, 281292, 4027172,
    ]
    counts = json.loads((ROOT / pins["counts_result_file"]).read_text())
    assert counts["complete"] is True and not counts["errors"]
    assert counts["totals"]["combination_count"] == math.comb(126, 4)
    assert counts["totals"]["signed_vector_count"] == 32 * math.comb(126, 4)
    assert counts["totals"]["energy_counts"][:20] == expected_counts
    assert sum(expected_counts) == 9063814
    checks += 6

    primary = json.loads((ROOT / pins["primary_m3_result_file"]).read_text())
    audit = json.loads((ROOT / pins["audit_m3_result_file"]).read_text())
    assert primary["complete"] is True and not primary["errors"]
    assert audit["complete"] is True and not audit["errors"]
    assert primary["returned_shards"] == audit["returned_shards"] == 32
    assert row_signature(primary) == row_signature(audit)
    assert [row[2] for row in row_signature(primary)] == expected_counts
    checks += 7

    maximum_rows = (
        (82, 912, 13, 34), (90, 1104, 13, 35),
        (98, 1548, 13, 39), (106, 1728, 13, 39),
        (114, 1968, 13, 40), (122, 2256, 13, 42),
        (130, 3264, 14, 48), (138, 3132, 13, 46),
        (146, 3888, 13, 49), (154, 3264, 12, 45),
        (162, 4248, 13, 49),
    )
    maxima = {row[0]: row[4] for row in row_signature(primary)}
    for variance, maximum, a, b in maximum_rows:
        assert maxima[variance] == maximum
        checks += verify_hermite_row(variance, maximum, a, b) + 1

    checks += verify_chord_bound()
    checks += verify_layer_rows()
    checks += verify_quadratic_rows()
    prime_floor = BP * 2**128
    assert (4 * prime_floor) ** 5 > 2**1289
    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert "V in {82,90,98,...,226}" in statement
    assert "10<=V<=74" in statement
    assert "max M_3" in proof and "(15,82)" in proof
    checks += 3
    print(
        "E1_PRIZE_N256_S18_M4_HIGH_VARIANCE_EXCLUSION_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()

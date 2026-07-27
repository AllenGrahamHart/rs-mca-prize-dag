#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 sparse-L1 variance exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_sparse_l1_variance_exclusion"
PARENT = "e1_n256_s16_high_variance_collision_exclusion"
NORM_PARENT = "collision_norm_criterion"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "variance_parent_file": "background/nodes/e1_n256_s16_high_variance_collision_exclusion/statement.md",
    "variance_parent_file_sha256": "9ff382e14946f9797e29859e118893a239a2e0b6a452ddb38978bd42360cbfa0",
}

ROWS = (
    (102, 102, 51, 27, 70, 1568, "slack"),
    (104, 104, 52, 28, 72, 1600, "slack"),
    (106, 106, 53, 29, 74, 1607, "chord"),
    (108, 110, 55, 30, 76, 1643, "chord"),
    (112, 112, 56, 32, 80, 1714, "integer"),
    (114, 118, 59, 33, 82, 1749, "integer"),
    (120, 124, 62, 34, 84, 1785, "integer"),
    (126, 130, 65, 35, 86, 1820, "integer"),
    (132, 134, 67, 36, 88, 1855, "integer"),
)


def integer_l1_maxima(max_energy: int) -> dict[int, int]:
    states = {(0, 0): 0}
    for count in range(21):
        for (energy, state_count), l1_norm in tuple(states.items()):
            if state_count != count:
                continue
            for value in range(1, math.isqrt(max_energy - energy) + 1):
                key = (energy + value * value, count + 1)
                states[key] = max(states.get(key, -1), l1_norm + value)
    return {
        energy: max(states.get((energy, count), -1) for count in range(22))
        for energy in range(max_energy + 1)
    }


def taylor(argument: Fraction, degree: int) -> Fraction:
    return sum(
        argument**index / math.factorial(index)
        for index in range(degree + 1)
    )


def alternating_log_lower(argument: Fraction, even_degree: int) -> Fraction:
    assert even_degree % 2 == 0
    return sum(
        (-1) ** (index + 1) * argument**index / index
        for index in range(1, even_degree + 1)
    )


def maximum_part_square_sum(total: int) -> int:
    quotient, remainder = divmod(total, 4)
    return 16 * quotient + (0, 1, 4, 5)[remainder]


def attainable_absolute_sums(count_4: int, count_2: int, count_1: int) -> set[int]:
    sums = {0}
    for value, count in ((4, count_4), (2, count_2), (1, count_1)):
        for _ in range(count):
            sums = {current + sign * value for current in sums for sign in (-1, 1)}
    return {abs(current) for current in sums}


def chord_ledger(coefficients: dict[int, int]) -> tuple[int, int, int, int]:
    groups: dict[int, list[int]] = defaultdict(list)
    diameter_square_mass = 0
    for left, right in combinations(sorted(coefficients), 2):
        difference = right - left
        product = coefficients[left] * coefficients[right]
        if difference == 64:
            diameter_square_mass += product * product
        elif difference < 64:
            groups[difference].append(product)
        else:
            groups[128 - difference].append(-product)
    energy = sum(sum(values) ** 2 for values in groups.values())
    l1_norm = sum(abs(sum(values)) for values in groups.values())
    cross_sum = sum(
        sum(left * right for left, right in combinations(values, 2))
        for values in groups.values()
    )
    return energy, l1_norm, diameter_square_mass, cross_sum


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("collision_norm_file", "collision_norm_file_sha256"),
        ("variance_parent_file", "variance_parent_file_sha256"),
    ):
        actual = hashlib.sha256((ROOT / pin[file_key]).read_bytes()).hexdigest()
        assert actual == pin[hash_key]

    maxima = integer_l1_maxima(67)
    expected = {
        56: 32,
        57: 33,
        58: 32,
        59: 33,
        60: 34,
        61: 33,
        62: 34,
        63: 35,
        64: 34,
        65: 35,
        66: 36,
        67: 35,
    }
    assert {energy: maxima[energy] for energy in expected} == expected

    chord_magnitudes = 3 * (4,) + 12 * (2,) + 6 * (1,)
    assert len(chord_magnitudes) == 21
    assert sum(chord_magnitudes) == 42
    assert sum(value * value for value in chord_magnitudes) == 102
    assert all(value * value <= 4 * value for value in chord_magnitudes)

    dynamic_maxima = [0] + [-1] * 42
    for total in range(1, 43):
        dynamic_maxima[total] = max(
            dynamic_maxima[total - part] + part * part
            for part in (1, 2, 4)
            if part <= total
        )
    assert dynamic_maxima == [maximum_part_square_sum(total) for total in range(43)]

    expected_slacks = {
        1: (0, 4, 8, 4),
        2: (0, 6, 0, 6),
        3: (4, 0, 4, 8),
    }
    actual_slacks = {
        difference: tuple(
            8 * negative
            - (
                maximum_part_square_sum(negative + difference)
                + maximum_part_square_sum(negative)
                - difference * difference
            )
            for negative in range(4)
        )
        for difference in range(1, 4)
    }
    assert actual_slacks == expected_slacks

    low_slack_patterns = {0: set(), 2: set(), 4: set(), 6: set()}
    for count_4 in range(4):
        for count_2 in range(13):
            for count_1 in range(7):
                if count_4 + count_2 + count_1 == 0:
                    continue
                for class_sum in attainable_absolute_sums(count_4, count_2, count_1):
                    slack = (
                        (class_sum - 2) ** 2
                        + 4 * count_2
                        + 3 * count_1
                        - 4
                    )
                    assert slack >= 0
                    assert slack % 2 == 0
                    if slack in low_slack_patterns:
                        low_slack_patterns[slack].add((count_2, count_1, class_sum))
    expected_low_slack_patterns = {
        0: {(0, 0, 0), (0, 0, 4), (1, 0, 2), (0, 1, 1), (0, 1, 3)},
        2: {(0, 2, 2)},
        4: {(1, 1, 1), (1, 1, 3)},
        6: {(0, 2, 0), (0, 2, 4), (1, 2, 2), (0, 3, 1), (0, 3, 3)},
    }
    assert low_slack_patterns == expected_low_slack_patterns
    assert {value: 4 * value - value * value for value in (4, 2, 1)} == {
        4: 0,
        2: 4,
        1: 3,
    }
    assert 4 * (42 - 29) - (102 - 52) == 2
    assert 12 * 4 + 4 + 4 > 52
    assert 4 * (42 - 29) - (102 - 51) == 1
    assert 4 * (42 - 28) - (102 - 51) == 5
    assert 12 * 4 + 4 + 3 > 51
    assert 4 * (42 - 29) - (102 - 50) == 0
    assert 12 * 4 + 6 > 50
    assert 4 * (42 - 28) - (102 - 49) == 3
    assert 12 * 4 + 5 > 49
    assert 4 * (42 - 28) - (102 - 48) == 2
    assert 12 * 4 + 4 + 4 > 48
    assert 4 * (42 - 27) - (102 - 48) == 6
    delta_4_plus_2_minimum = min(
        4 * (12 - count_2)
        + (6 - 2 - count_1)
        + class_sum * class_sum
        + 4
        for count_2, count_1, class_sum in expected_low_slack_patterns[4]
    )
    delta_6_minimum = min(
        4 * (12 - count_2) + (6 - count_1) + class_sum * class_sum
        for count_2, count_1, class_sum in expected_low_slack_patterns[6]
    )
    assert (
        12 * 4 + 4,
        11 * 4 + 4 + 4,
        12 * 4 + 3 * 4,
        delta_4_plus_2_minimum,
        delta_6_minimum,
    ) == (52, 52, 60, 52, 52)
    assert 4 * (42 - 28) - (102 - 47) == 1
    assert 4 * (42 - 27) - (102 - 47) == 5
    assert 12 * 4 + 4 + 3 > 47
    assert 4 * (42 - 26) - (102 - 47) == 9
    delta_6_after_unit_minimum = min(
        4 * (12 - count_2) + (5 - count_1) + class_sum * class_sum
        for count_2, count_1, class_sum in expected_low_slack_patterns[6]
    )
    delta_4_plus_2_after_unit_minimum = min(
        4 * (12 - count_2)
        + (5 - 2 - count_1)
        + class_sum * class_sum
        + 4
        for count_2, count_1, class_sum in expected_low_slack_patterns[4]
    )
    assert (
        11 * 4 + 3 + 4,
        delta_6_after_unit_minimum,
        delta_4_plus_2_after_unit_minimum,
    ) == (51, 51, 51)
    assert 1 + 3 * 2 > 6
    assert 4 * (42 - 28) - (102 - 46) == 0
    assert 12 * 4 + 6 > 46
    assert 4 * (42 - 27) - (102 - 46) == 4
    assert (11 * 4 + 6, 11 * 4 + 5 + 1, 12 * 4 + 2 * 4 + 2) == (
        50,
        50,
        58,
    )
    assert 4 * (42 - 27) - (102 - 45) == 3
    assert 12 * 4 + 5 > 45
    assert 4 * (42 - 26) - (102 - 45) == 7
    assert (11 * 4 + 5, 11 * 4 + 4 + 1, 12 * 4 + 2 * 4 + 1) == (
        49,
        49,
        57,
    )
    special_l1_bounds = {
        45: 25,
        46: 26,
        47: 25,
        48: 26,
        49: 27,
        50: 28,
        51: 27,
        52: 28,
    }

    e50_witness = {
        48: -2,
        51: -2,
        67: -1,
        81: 2,
        83: 1,
        84: -1,
        111: 1,
    }
    witness_support = sorted(e50_witness)
    assert math.gcd(
        256, *(position - witness_support[0] for position in witness_support)
    ) == 1
    assert chord_ledger(e50_witness) == (50, 28, 0, -26)
    assert {
        energy: (energy + 66) // 4
        for energy in (53, 54, 55)
    } == {53: 29, 54: 30, 55: 30}

    optimized_linear = Fraction(23, 336)
    optimized_quadratic = Fraction(1, 1344)
    optimized_allowance = Fraction(1, 150)
    assert 2 * optimized_quadratic == Fraction(1, 672)
    assert optimized_linear + 16 * 2 * optimized_quadratic == Fraction(62, 672)
    assert 2 * optimized_quadratic * 14 * 48 == 1
    assert (
        optimized_allowance
        - 2 * optimized_linear
        - 4 * optimized_quadratic
        == optimized_allowance - Fraction(47, 336)
    )
    assert (
        optimized_allowance
        + 56 * optimized_linear
        - 56**2 * optimized_quadratic
        == Fraction(113, 75)
    )
    assert 16 + 2 * special_l1_bounds[50] == 72
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + optimized_allowance
        > Fraction(47, 336)
    )
    assert taylor(Fraction(113, 75), 6) > Fraction(9, 2)
    optimized_decay = Fraction(32, 3) * (
        Fraction(25, 336) - optimized_allowance
    )
    assert optimized_decay == Fraction(1138, 1575)
    assert taylor(optimized_decay, 3) > 2

    optimized_decay_98 = Fraction(32, 3) * (
        Fraction(49, 672) - optimized_allowance
    )
    assert optimized_decay_98 == Fraction(53, 75)
    assert taylor(optimized_decay_98, 3) > 2

    second_linear = Fraction(11, 161)
    second_quadratic = Fraction(1, 1288)
    assert 2 * second_quadratic == Fraction(1, 644)
    assert second_linear + 16 * 2 * second_quadratic == Fraction(60, 644)
    assert 2 * second_quadratic * 14 * 46 == 1
    assert (
        optimized_allowance
        - 2 * second_linear
        - 4 * second_quadratic
        == optimized_allowance - Fraction(45, 322)
    )
    assert (
        optimized_allowance
        + 52 * second_linear
        - 52**2 * second_quadratic
        == Fraction(35261, 24150)
    )
    assert 16 + 2 * special_l1_bounds[48] == 68
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + optimized_allowance
        > Fraction(45, 322)
    )
    assert taylor(Fraction(35261, 24150), 5) > Fraction(17, 4)
    optimized_decay_96 = Fraction(32, 3) * (
        Fraction(12, 161) - optimized_allowance
    )
    assert optimized_decay_96 == Fraction(26224, 36225)
    assert taylor(optimized_decay_96, 3) > 2

    third_linear = Fraction(43, 630)
    third_quadratic = Fraction(1, 1260)
    assert 2 * third_quadratic == Fraction(1, 630)
    assert third_linear + 16 * 2 * third_quadratic == Fraction(59, 630)
    assert 2 * third_quadratic * 14 * 45 == 1
    assert (
        optimized_allowance
        - 2 * third_linear
        - 4 * third_quadratic
        == optimized_allowance - Fraction(44, 315)
    )
    assert (
        optimized_allowance
        + 50 * third_linear
        - 50**2 * third_quadratic
        == Fraction(1507, 1050)
    )
    assert 16 + 2 * special_l1_bounds[47] == 66
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + optimized_allowance
        > Fraction(44, 315)
    )
    assert taylor(Fraction(1507, 1050), 4) > Fraction(33, 8)
    optimized_decay_94 = Fraction(32, 3) * (
        Fraction(47, 630) - optimized_allowance
    )
    assert optimized_decay_94 == Fraction(3424, 4725)
    assert taylor(optimized_decay_94, 3) > 2

    tight_allowance = Fraction(1, 160)
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + tight_allowance
        > Fraction(45, 322)
    )
    assert (
        tight_allowance
        + 52 * second_linear
        - 52**2 * second_quadratic
        == Fraction(37601, 25760)
    )
    assert taylor(Fraction(37601, 25760), 5) > Fraction(17, 4)
    optimized_decay_92 = Fraction(32, 3) * (
        Fraction(23, 322) - tight_allowance
    )
    assert optimized_decay_92 == Fraction(73, 105)
    assert taylor(optimized_decay_92, 4) > 2

    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + tight_allowance
        > Fraction(44, 315)
    )
    assert (
        tight_allowance
        + 50 * third_linear
        - 50**2 * third_quadratic
        == Fraction(1607, 1120)
    )
    assert taylor(Fraction(1607, 1120), 4) > Fraction(33, 8)
    optimized_decay_90 = Fraction(32, 3) * (
        Fraction(1, 14) - tight_allowance
    )
    assert optimized_decay_90 == Fraction(73, 105)
    assert taylor(optimized_decay_90, 4) > 2

    excluded = [90, 92, 94, 96, 98, 100]
    for lower_v, upper_v, upper_energy, upper_l1, bound, denominator, method in ROWS:
        energies = range(lower_v // 2, upper_energy + 1)
        if method == "slack":
            assert all(special_l1_bounds[energy] <= upper_l1 for energy in energies)
        elif method == "chord":
            assert all((energy + 66) // 4 <= upper_l1 for energy in energies)
        else:
            assert method == "integer"
            assert all(maxima[energy] <= upper_l1 for energy in energies)
        assert bound == 16 + 2 * upper_l1
        assert 16 < Fraction(denominator, 32) < bound

        endpoint_exponent = (
            Fraction(bound - 16, 16)
            - Fraction((bound - 16) ** 2, denominator)
        )
        assert taylor(endpoint_exponent, 12) > Fraction(bound, 16)

        six_bit_exponent = Fraction(32 * lower_v, 3 * denominator)
        assert taylor(six_bit_exponent, 9) > 2
        excluded.extend(range(lower_v, upper_v + 1, 2))

    assert excluded == list(range(90, 136, 2))

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[NORM_PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NORM_PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "90<=V<=134" in statements[NODE]
    assert "V<=88" in statements[NODE]

    print(
        "E1_N256_S16_SPARSE_L1_VARIANCE_EXCLUSION_PASS "
        "excluded=23 residual_max=88 majorants=15"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the N=256 square-mass-16 sparse-L1 variance exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
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


def atanh_log_bounds(value: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    assert value > 1
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(
        parameter ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    first_omitted_degree = 2 * terms + 1
    remainder = (
        2
        * parameter**first_omitted_degree
        / (first_omitted_degree * (1 - parameter * parameter))
    )
    return lower, lower + remainder


def layer_triple_cap(counts: tuple[int, ...]) -> int:
    layer_sizes = [
        2 * sum(counts[level:])
        for level in range(len(counts))
        if sum(counts[level:])
    ]
    cap = 0
    for first, second, third in product(layer_sizes, repeat=3):
        pair_caps = (
            first * second - min(first, second),
            first * third - min(first, third),
            second * third - min(second, third),
        )
        cap += min(pair_caps)
    return cap


def add_log_forms(*forms: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(sum(form[index] for form in forms) for index in range(3))  # type: ignore[return-value]


def scale_log_form(
    scalar: Fraction, form: tuple[Fraction, Fraction, Fraction]
) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(scalar * value for value in form)  # type: ignore[return-value]


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


def relaxed_minimum_energy_by_slack(maximum_slack: int) -> list[int | None]:
    class_types = set()
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
                    if slack == 0:
                        assert 4 * count_2 + count_1 <= class_sum * class_sum
                    if 0 < slack <= maximum_slack:
                        class_types.add((slack, count_2, count_1, class_sum))

    answers: list[int | None] = []
    for target_slack in range(maximum_slack + 1):
        best = None
        for diameter_2 in range(4):
            for diameter_1 in range(3):
                if diameter_2 + 2 * diameter_1 > 4:
                    continue
                if diameter_1 + diameter_2 > 3:
                    continue
                diameter_slack = 4 * diameter_2 + 3 * diameter_1
                if diameter_slack > target_slack:
                    continue
                class_slack_target = target_slack - diameter_slack
                states = {(0, 0, 0): 0}
                for used_slack in range(class_slack_target + 1):
                    current = [
                        item for item in states.items() if item[0][0] == used_slack
                    ]
                    for (state_slack, used_2, used_1), energy in current:
                        for slack, count_2, count_1, class_sum in class_types:
                            new_state = (
                                state_slack + slack,
                                used_2 + count_2,
                                used_1 + count_1,
                            )
                            if new_state[0] > class_slack_target:
                                continue
                            if new_state[1] > 12 - diameter_2:
                                continue
                            if new_state[2] > 6 - diameter_1:
                                continue
                            new_energy = energy + class_sum * class_sum
                            states[new_state] = min(
                                states.get(new_state, new_energy), new_energy
                            )
                for (state_slack, used_2, used_1), energy in states.items():
                    if state_slack != class_slack_target:
                        continue
                    total_energy = (
                        energy
                        + 4 * (12 - diameter_2 - used_2)
                        + (6 - diameter_1 - used_1)
                    )
                    best = total_energy if best is None else min(best, total_energy)
        answers.append(best)
    return answers


def relaxed_equality_signatures(
    target_energy: int, target_l1: int
) -> tuple[tuple[int, int, tuple[tuple[int, int, int, int], ...]], ...]:
    target_slack = target_energy + 66 - 4 * target_l1
    class_types = set()
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
                    if 0 < slack <= target_slack:
                        class_types.add((slack, count_2, count_1, class_sum))
    ordered_types = sorted(class_types)
    signatures = []
    for diameter_2 in range(4):
        for diameter_1 in range(3):
            if diameter_2 + 2 * diameter_1 > 4:
                continue
            if diameter_1 + diameter_2 > 3:
                continue
            class_slack = target_slack - 4 * diameter_2 - 3 * diameter_1
            if class_slack < 0:
                continue

            @lru_cache(maxsize=None)
            def search(
                start: int,
                remaining_slack: int,
                remaining_2: int,
                remaining_1: int,
                remaining_energy: int,
            ) -> tuple[tuple[int, ...], ...]:
                if remaining_slack == 0:
                    return ((),) if remaining_energy == 0 else ()
                found = []
                for index in range(start, len(ordered_types)):
                    slack, count_2, count_1, class_sum = ordered_types[index]
                    energy = class_sum * class_sum - 4 * count_2 - count_1
                    if slack > remaining_slack:
                        break
                    if count_2 > remaining_2 or count_1 > remaining_1:
                        continue
                    for suffix in search(
                        index,
                        remaining_slack - slack,
                        remaining_2 - count_2,
                        remaining_1 - count_1,
                        remaining_energy - energy,
                    ):
                        found.append((index,) + suffix)
                return tuple(found)

            baseline = 4 * (12 - diameter_2) + (6 - diameter_1)
            for indices in search(
                0,
                class_slack,
                12 - diameter_2,
                6 - diameter_1,
                target_energy - baseline,
            ):
                signatures.append(
                    (
                        diameter_2,
                        diameter_1,
                        tuple(ordered_types[index] for index in indices),
                    )
                )
    return tuple(signatures)


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
    relaxed_slack_table = relaxed_minimum_energy_by_slack(21)
    assert relaxed_slack_table == [
        54,
        None,
        56,
        53,
        50,
        55,
        52,
        49,
        46,
        51,
        48,
        45,
        42,
        47,
        44,
        41,
        38,
        43,
        40,
        37,
        34,
        39,
    ]
    closed_form_slack_table = [54, None]
    for slack in range(2, 22):
        intercept = {0: 54, 1: 60, 2: 58, 3: 56}[slack % 4]
        closed_form_slack_table.append(intercept - slack)
    assert relaxed_slack_table == closed_form_slack_table
    assert 4 * (42 - 27) - (102 - 44) == 2
    assert 4 * (42 - 26) - (102 - 44) == 6
    assert 4 * (42 - 25) - (102 - 44) == 10
    assert 4 * (42 - 27) - (102 - 43) == 1
    assert 4 * (42 - 26) - (102 - 43) == 5
    assert 4 * (42 - 25) - (102 - 43) == 9
    assert 4 * (42 - 24) - (102 - 43) == 13
    assert [4 * (42 - l1) - (102 - 42) for l1 in (27, 26, 25)] == [
        0,
        4,
        8,
    ]
    assert [relaxed_slack_table[slack] for slack in (0, 4, 8)] == [54, 50, 46]
    assert [4 * (42 - l1) - (102 - 41) for l1 in (26, 25, 24)] == [
        3,
        7,
        11,
    ]
    assert [relaxed_slack_table[slack] for slack in (3, 7, 11)] == [53, 49, 45]
    assert [4 * (42 - l1) - (102 - 40) for l1 in (26, 25, 24, 23, 22)] == [
        2,
        6,
        10,
        14,
        18,
    ]
    assert [relaxed_slack_table[slack] for slack in (2, 6, 10, 14, 18)] == [
        56,
        52,
        48,
        44,
        40,
    ]
    assert [4 * (42 - l1) - (102 - 39) for l1 in (26, 25, 24, 23, 22, 21)] == [
        1,
        5,
        9,
        13,
        17,
        21,
    ]
    assert [relaxed_slack_table[slack] for slack in (1, 5, 9, 13, 17, 21)] == [
        None,
        55,
        51,
        47,
        43,
        39,
    ]
    special_l1_bounds = {
        39: 21,
        40: 22,
        41: 23,
        42: 24,
        43: 23,
        44: 24,
        45: 25,
        46: 26,
        47: 25,
        48: 26,
        49: 27,
        50: 28,
        51: 27,
        52: 28,
    }
    energy_38_signatures = relaxed_equality_signatures(38, 22)
    assert len(energy_38_signatures) == 24
    assert {diameter_1 for _, diameter_1, _ in energy_38_signatures} == {0}
    assert {diameter_2 for diameter_2, _, _ in energy_38_signatures} == {
        0,
        1,
        2,
        3,
    }
    assert max(len(classes) for _, _, classes in energy_38_signatures) == 4
    assert {
        class_type
        for _, _, classes in energy_38_signatures
        for class_type in classes
    } == {
        (4, 1, 1, 1),
        (8, 2, 0, 0),
        (8, 2, 1, 1),
        (8, 3, 0, 2),
        (12, 3, 1, 1),
        (16, 4, 0, 0),
        (16, 4, 1, 1),
        (16, 5, 0, 2),
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

    e42_witness = {
        7: -1,
        24: -1,
        55: -2,
        76: -1,
        82: -2,
        87: 1,
        103: 2,
    }
    witness_support = sorted(e42_witness)
    assert math.gcd(
        256, *(position - witness_support[0] for position in witness_support)
    ) == 1
    assert chord_ledger(e42_witness) == (42, 24, 0, -30)
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

    fourth_linear = Fraction(3, 44)
    fourth_quadratic = Fraction(1, 1232)
    assert 2 * fourth_quadratic == Fraction(1, 616)
    assert fourth_linear + 16 * 2 * fourth_quadratic == Fraction(58, 616)
    assert 2 * fourth_quadratic * 14 * 44 == 1
    assert (
        tight_allowance
        - 2 * fourth_linear
        - 4 * fourth_quadratic
        == tight_allowance - Fraction(43, 308)
    )
    assert (
        tight_allowance
        + 48 * fourth_linear
        - 48**2 * fourth_quadratic
        == Fraction(17357, 12320)
    )
    assert 16 + 2 * special_l1_bounds[44] == 64
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + tight_allowance
        > Fraction(43, 308)
    )
    assert taylor(Fraction(17357, 12320), 4) > 4
    optimized_decay_88 = Fraction(32, 3) * (
        Fraction(1, 14) - tight_allowance
    )
    assert optimized_decay_88 == Fraction(73, 105)
    assert taylor(optimized_decay_88, 4) > 2

    fifth_linear = Fraction(41, 602)
    fifth_quadratic = Fraction(1, 1204)
    assert 2 * fifth_quadratic == Fraction(1, 602)
    assert fifth_linear + 16 * 2 * fifth_quadratic == Fraction(57, 602)
    assert 2 * fifth_quadratic * 14 * 43 == 1
    assert (
        tight_allowance
        - 2 * fifth_linear
        - 4 * fifth_quadratic
        == tight_allowance - Fraction(42, 301)
    )
    assert (
        tight_allowance
        + 46 * fifth_linear
        - 46**2 * fifth_quadratic
        == Fraction(66541, 48160)
    )
    assert 16 + 2 * special_l1_bounds[43] == 62
    assert (
        alternating_log_lower(Fraction(1, 7), 4)
        + tight_allowance
        > Fraction(42, 301)
    )
    assert taylor(Fraction(66541, 48160), 4) > Fraction(31, 8)
    optimized_decay_86 = Fraction(32, 3) * (
        Fraction(1, 14) - tight_allowance
    )
    assert optimized_decay_86 == Fraction(73, 105)
    assert taylor(optimized_decay_86, 4) > 2

    def energy_profiles(
        target_energy: int, l1_ceiling: int
    ) -> list[tuple[int, tuple[int, ...], int]]:
        profiles = []
        for counts in product(
            range(43), range(11), range(5), range(3), range(2), range(2)
        ):
            profile_l1 = sum(
                (index + 1) * count for index, count in enumerate(counts)
            )
            profile_energy = sum(
                (index + 1) ** 2 * count for index, count in enumerate(counts)
            )
            if (
                profile_energy == target_energy
                and profile_l1 <= l1_ceiling
                and sum(counts) <= 21
            ):
                profiles.append((layer_triple_cap(counts), counts, profile_l1))
        return profiles

    energy_42_profiles = energy_profiles(42, 24)
    assert len(energy_42_profiles) == 42
    assert max(energy_42_profiles) == (3660, (6, 9, 0, 0, 0, 0), 24)
    assert sum(cap == 3660 for cap, _, _ in energy_42_profiles) == 1
    energy_41_profiles = energy_profiles(41, 23)
    assert len(energy_41_profiles) == 39
    assert max(energy_41_profiles) == (3438, (5, 9, 0, 0, 0, 0), 23)
    assert sum(cap == 3438 for cap, _, _ in energy_41_profiles) == 1
    energy_40_profiles = energy_profiles(40, 22)
    assert len(energy_40_profiles) == 34
    assert max(energy_40_profiles) == (3224, (4, 9, 0, 0, 0, 0), 22)
    assert sum(cap == 3224 for cap, _, _ in energy_40_profiles) == 1
    energy_39_profiles = energy_profiles(39, 21)
    assert len(energy_39_profiles) == 29
    assert max(energy_39_profiles) == (3018, (3, 9, 0, 0, 0, 0), 21)
    assert sum(cap == 3018 for cap, _, _ in energy_39_profiles) == 1
    energy_38_profiles = energy_profiles(38, 22)
    assert len(energy_38_profiles) == 32
    assert max(energy_38_profiles) == (3012, (6, 8, 0, 0, 0, 0), 22)
    assert sum(cap == 3012 for cap, _, _ in energy_38_profiles) == 1

    log_14 = (Fraction(1), Fraction(0), Fraction(0))
    log_60 = (Fraction(0), Fraction(1), Fraction(0))
    hermite_coefficients = (
        (
            Fraction(8100, 12167),
            Fraction(4067, 12167),
            Fraction(-949, 529),
        ),
        (
            Fraction(630, 12167),
            Fraction(-630, 12167),
            Fraction(42883, 222180),
        ),
        (
            Fraction(-111, 48668),
            Fraction(111, 48668),
            Fraction(-1159, 222180),
        ),
        (
            Fraction(1, 48668),
            Fraction(-1, 48668),
            Fraction(37, 888720),
        ),
    )

    def evaluate_form_polynomial(
        coefficients: tuple[tuple[Fraction, Fraction, Fraction], ...],
        value: int,
    ) -> tuple[Fraction, Fraction, Fraction]:
        return add_log_forms(
            *(
                scale_log_form(Fraction(value**degree), coefficient)
                for degree, coefficient in enumerate(coefficients)
            )
        )

    def evaluate_form_derivative(
        coefficients: tuple[tuple[Fraction, Fraction, Fraction], ...],
        value: int,
    ) -> tuple[Fraction, Fraction, Fraction]:
        return add_log_forms(
            *(
                scale_log_form(
                    Fraction(degree * value ** (degree - 1)), coefficient
                )
                for degree, coefficient in enumerate(coefficients)
                if degree
            )
        )

    assert evaluate_form_polynomial(hermite_coefficients, 14) == log_14
    assert evaluate_form_polynomial(hermite_coefficients, 60) == log_60
    assert evaluate_form_derivative(hermite_coefficients, 14) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 14),
    )
    assert evaluate_form_derivative(hermite_coefficients, 60) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 60),
    )
    assert Fraction(37, 888720) - Fraction(2, 48668) > 0
    assert Fraction(5) > Fraction(30, 7)

    assert 16**2 + 84 == 340
    assert 16**3 + 3 * 16 * 84 + 3660 == 11788
    expected_hermite = add_log_forms(
        hermite_coefficients[0],
        scale_log_form(Fraction(16), hermite_coefficients[1]),
        scale_log_form(Fraction(340), hermite_coefficients[2]),
        scale_log_form(Fraction(11788), hermite_coefficients[3]),
    )
    assert expected_hermite == (
        Fraction(11692, 12167),
        Fraction(475, 12167),
        Fraction(361, 31740),
    )

    log_2_lower, log_2_upper = atanh_log_bounds(Fraction(2), 8)
    log_8_over_7_lower, log_8_over_7_upper = atanh_log_bounds(Fraction(8, 7), 8)
    log_16_over_15_lower, _ = atanh_log_bounds(Fraction(16, 15), 8)
    assert log_2_lower < log_2_upper
    hermite_margin_lower = (
        Fraction(-66901, 389344) * log_2_upper
        + Fraction(11692, 12167) * log_8_over_7_lower
        + Fraction(475, 12167) * log_16_over_15_lower
        - Fraction(361, 31740)
    )
    assert hermite_margin_lower > 0

    assert 16**2 + 82 == 338
    assert 16**3 + 3 * 16 * 82 + 3438 == 11470
    expected_hermite_82 = add_log_forms(
        hermite_coefficients[0],
        scale_log_form(Fraction(16), hermite_coefficients[1]),
        scale_log_form(Fraction(338), hermite_coefficients[2]),
        scale_log_form(Fraction(11470), hermite_coefficients[3]),
    )
    assert expected_hermite_82 == (
        Fraction(11668, 12167),
        Fraction(499, 12167),
        Fraction(1269, 148120),
    )
    hermite_margin_82_lower = (
        Fraction(-68437, 389344) * log_2_upper
        + Fraction(11668, 12167) * log_8_over_7_lower
        + Fraction(499, 12167) * log_16_over_15_lower
        - Fraction(1269, 148120)
    )
    assert hermite_margin_82_lower > 0

    log_58 = (Fraction(0), Fraction(1), Fraction(0))
    hermite_coefficients_58 = (
        (Fraction(841, 1331), Fraction(490, 1331), Fraction(-445, 242)),
        (Fraction(609, 10648), Fraction(-609, 10648), Fraction(9837, 49126)),
        (Fraction(-27, 10648), Fraction(27, 10648), Fraction(-1093, 196504)),
        (Fraction(1, 42592), Fraction(-1, 42592), Fraction(9, 196504)),
    )
    assert evaluate_form_polynomial(hermite_coefficients_58, 14) == log_14
    assert evaluate_form_polynomial(hermite_coefficients_58, 58) == log_58
    assert evaluate_form_derivative(hermite_coefficients_58, 14) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 14),
    )
    assert evaluate_form_derivative(hermite_coefficients_58, 58) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 58),
    )
    assert Fraction(67, 16) > Fraction(29, 7)
    assert Fraction(9, 196504) - Fraction(3, 2 * 42592) > 0
    assert 16**2 + 80 == 336
    assert 16**3 + 3 * 16 * 80 + 3224 == 11160
    expected_hermite_80 = add_log_forms(
        hermite_coefficients_58[0],
        scale_log_form(Fraction(16), hermite_coefficients_58[1]),
        scale_log_form(Fraction(336), hermite_coefficients_58[2]),
        scale_log_form(Fraction(11160), hermite_coefficients_58[3]),
    )
    assert expected_hermite_80 == (
        Fraction(5095, 5324),
        Fraction(229, 5324),
        Fraction(355, 49126),
    )
    log_32_over_29_lower, _ = atanh_log_bounds(Fraction(32, 29), 8)
    hermite_margin_80_lower = (
        Fraction(-7657, 42592) * log_2_upper
        + Fraction(5095, 5324) * log_8_over_7_lower
        + Fraction(229, 5324) * log_32_over_29_lower
        - Fraction(355, 49126)
    )
    assert hermite_margin_80_lower > 0

    log_57 = (Fraction(0), Fraction(1), Fraction(0))
    hermite_coefficients_57 = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    assert evaluate_form_polynomial(hermite_coefficients_57, 14) == log_14
    assert evaluate_form_polynomial(hermite_coefficients_57, 57) == log_57
    assert evaluate_form_derivative(hermite_coefficients_57, 14) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 14),
    )
    assert evaluate_form_derivative(hermite_coefficients_57, 57) == (
        Fraction(0),
        Fraction(0),
        Fraction(1, 57),
    )
    assert Fraction(67, 16) > Fraction(57, 14)
    assert Fraction(71, 1475502) - Fraction(3, 79507) > 0
    assert 16**2 + 78 == 334
    assert 16**3 + 3 * 16 * 78 + 3018 == 10858
    expected_hermite_78 = add_log_forms(
        hermite_coefficients_57[0],
        scale_log_form(Fraction(16), hermite_coefficients_57[1]),
        scale_log_form(Fraction(334), hermite_coefficients_57[2]),
        scale_log_form(Fraction(10858), hermite_coefficients_57[3]),
    )
    assert expected_hermite_78 == (
        Fraction(75917, 79507),
        Fraction(3590, 79507),
        Fraction(538, 105393),
    )
    log_64_over_57_lower, log_64_over_57_upper = atanh_log_bounds(
        Fraction(64, 57), 8
    )
    hermite_margin_78_lower = (
        Fraction(-468281, 2544224) * log_2_upper
        + Fraction(75917, 79507) * log_8_over_7_lower
        + Fraction(3590, 79507) * log_64_over_57_lower
        - Fraction(538, 105393)
    )
    assert hermite_margin_78_lower > 0

    assert 16**2 + 76 == 332
    assert 16**3 + 3 * 16 * 76 + 2806 == 10550
    expected_hermite_76_at_2806 = add_log_forms(
        hermite_coefficients_57[0],
        scale_log_form(Fraction(16), hermite_coefficients_57[1]),
        scale_log_form(Fraction(332), hermite_coefficients_57[2]),
        scale_log_form(Fraction(10550), hermite_coefficients_57[3]),
    )
    assert expected_hermite_76_at_2806 == (
        Fraction(75727, 79507),
        Fraction(3780, 79507),
        Fraction(1318, 737751),
    )
    hermite_margin_76_at_2806_lower = (
        Fraction(-480441, 2544224) * log_2_upper
        + Fraction(75727, 79507) * log_8_over_7_lower
        + Fraction(3780, 79507) * log_64_over_57_lower
        - Fraction(1318, 737751)
    )
    assert hermite_margin_76_at_2806_lower > 0

    assert 16**3 + 3 * 16 * 76 + 2807 == 10551
    expected_hermite_76_at_2807 = add_log_forms(
        hermite_coefficients_57[0],
        scale_log_form(Fraction(16), hermite_coefficients_57[1]),
        scale_log_form(Fraction(332), hermite_coefficients_57[2]),
        scale_log_form(Fraction(10551), hermite_coefficients_57[3]),
    )
    assert expected_hermite_76_at_2807 == (
        Fraction(75729, 79507),
        Fraction(3778, 79507),
        Fraction(2707, 1475502),
    )
    hermite_margin_76_at_2807_upper = (
        Fraction(-480313, 2544224) * log_2_lower
        + Fraction(75729, 79507) * log_8_over_7_upper
        + Fraction(3778, 79507) * log_64_over_57_upper
        - Fraction(2707, 1475502)
    )
    assert hermite_margin_76_at_2807_upper < 0

    excluded = [78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
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

    assert excluded == list(range(78, 136, 2))

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
    assert "78<=V<=134" in statements[NODE]
    assert "V<=76" in statements[NODE]

    print(
        "E1_N256_S16_SPARSE_L1_VARIANCE_EXCLUSION_PASS "
        "excluded=29 residual_max=76 majorants=21"
    )


if __name__ == "__main__":
    main()

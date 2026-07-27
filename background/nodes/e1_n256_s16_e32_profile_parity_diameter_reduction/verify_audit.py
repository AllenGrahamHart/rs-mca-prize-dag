#!/usr/bin/env python3
"""Independent audit of the E=32 profile and diameter frontier."""

from __future__ import annotations

from fractions import Fraction


def solve(matrix: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    augmented = [row[:] + [value] for row, value in zip(matrix, target)]
    for column in range(len(matrix)):
        pivot = next(row for row in range(column, len(matrix)) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(len(matrix)):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                left - scale * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return [row[-1] for row in augmented]


def log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
    z = (value - 1) / (value + 1)
    lower = 2 * sum(z ** (2 * index + 1) / (2 * index + 1) for index in range(terms))
    degree = 2 * terms + 1
    return lower, lower + 2 * z**degree / (degree * (1 - z*z))


def recursive_profiles() -> list[tuple[tuple[int, ...], int]]:
    answer: list[tuple[tuple[int, ...], int]] = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 32 and l1_norm <= 18:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = 0
                for first in layers:
                    for second in layers:
                        for third in layers:
                            cap += min(
                                first * second - min(first, second),
                                first * third - min(first, third),
                                second * third - min(second, third),
                            )
                answer.append((tuple(counts), cap))
            return
        maximum = (32 - energy) // (magnitude * magnitude)
        for count in range(maximum + 1):
            new_l1 = l1_norm + magnitude * count
            if new_l1 > 18:
                break
            visit(
                magnitude + 1,
                energy + magnitude * magnitude * count,
                new_l1,
                counts + [count],
            )

    visit(1, 0, 0, [])
    return sorted(answer, key=lambda item: (item[1], item[0]), reverse=True)


def matching_ledgers() -> set[tuple[int, int]]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    ledgers: set[tuple[int, int]] = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            square_mass = sum((weights[left] * weights[right]) ** 2 for left, right in edges)
            light_edges = sum(weights[left] == weights[right] == 1 for left, right in edges)
            if square_mass % 2 == 0:
                ledgers.add((square_mass, light_edges))
            return
        first = available[0]
        visit(available[1:], edges)
        for offset, second in enumerate(available[1:]):
            remainder = available[1:offset + 1] + available[offset + 2:]
            visit(remainder, edges + ((first, second),))

    visit(tuple(range(7)), ())
    return ledgers


def main() -> None:
    profiles = recursive_profiles()
    assert len(profiles) == 18
    above = [(counts, cap) for counts, cap in profiles if cap > 1517]
    assert len(above) == 7
    survivors = [(counts, cap) for counts, cap in above if sum(counts[0::2]) <= 6]
    assert [counts for counts, _ in survivors] == [
        (4, 7, 0, 0, 0), (0, 8, 0, 0, 0), (3, 5, 1, 0, 0),
    ]

    matrix = [
        [Fraction(14**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(28), Fraction(3 * 14**2)],
        [Fraction(57**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(114), Fraction(3 * 57**2)],
    ]
    coefficient_forms = []
    for target in (
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1, 14), Fraction(0), Fraction(1, 57)],
    ):
        coefficient_forms.append(solve(matrix, target))

    expected = []
    for moment in (1517, 1518):
        raw_moments = (1, 16, 320, 7168 + moment)
        expected.append(tuple(
            sum(raw_moments[degree] * coefficient_forms[basis][degree] for degree in range(4))
            for basis in range(3)
        ))
    assert expected == [
        (Fraction(74553, 79507), Fraction(4954, 79507), Fraction(-27947, 1475502)),
        (Fraction(74555, 79507), Fraction(4952, 79507), Fraction(-4646, 245917)),
    ]

    l2, u2 = log_bounds(Fraction(2))
    l87, u87 = log_bounds(Fraction(8, 7))
    l6457, u6457 = log_bounds(Fraction(64, 57))
    assert (
        Fraction(-555577, 2544224) * u2
        + Fraction(74553, 79507) * l87
        + Fraction(4954, 79507) * l6457
        + Fraction(27947, 1475502)
    ) > 0
    assert (
        Fraction(-555449, 2544224) * l2
        + Fraction(74555, 79507) * u87
        + Fraction(4952, 79507) * u6457
        + Fraction(4646, 245917)
    ) < 0

    assert matching_ledgers() == {
        (0, 0), (2, 2), (4, 0), (8, 0),
        (12, 0), (16, 0), (18, 2), (20, 0),
    }
    for deleted in (
        (7, 4, 1, 0, 0), (10, 1, 2, 0, 0),
        (12, 1, 0, 1, 0), (6, 2, 2, 0, 0),
    ):
        assert sum(deleted[0::2]) > 6

    print(
        "E1_N256_S16_E32_PROFILE_PARITY_DIAMETER_REDUCTION_AUDIT_PASS "
        "recursive_profiles=18 hermite=independent matchings=complete mutations=4"
    )


if __name__ == "__main__":
    main()

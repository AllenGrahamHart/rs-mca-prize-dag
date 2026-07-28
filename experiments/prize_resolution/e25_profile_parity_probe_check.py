#!/usr/bin/env python3
"""Independent checker for the exact E25 profile/parity route probe."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "e25_profile_parity_probe_modal.py"
RESULT = HERE / "e25_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)


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
            augmented[row] = [left - scale * right for left, right in zip(augmented[row], augmented[column])]
    return [row[-1] for row in augmented]


def recursive_profiles(l1_bound: int) -> list[dict[str, object]]:
    answer: list[dict[str, object]] = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 25:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(
                    min(a * b - min(a, b), a * c - min(a, c), b * c - min(b, c))
                    for a in layers for b in layers for c in layers
                )
                answer.append({
                    "cap": cap,
                    "profile": counts,
                    "l1": l1_norm,
                    "odd_classes": sum(counts[0::2]),
                })
            return
        for count in range((25 - energy) // (magnitude * magnitude) + 1):
            next_l1 = l1_norm + magnitude * count
            if next_l1 > l1_bound:
                break
            visit(magnitude + 1, energy + magnitude * magnitude * count, next_l1, counts + [count])

    visit(1, 0, 0, [])
    return sorted(answer, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def atanh_bounds(value: Fraction, terms: int = 12) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(parameter ** (2 * index + 1) / (2 * index + 1) for index in range(terms))
    degree = 2 * terms + 1
    upper = lower + 2 * parameter**degree / (degree * (1 - parameter * parameter))
    return lower, upper


def verify_boundary() -> None:
    matrix = [
        [Fraction(14**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(28), Fraction(3 * 14**2)],
        [Fraction(57**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(114), Fraction(3 * 57**2)],
    ]
    coefficient_forms = [
        solve(matrix, target)
        for target in (
            [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(1, 14), Fraction(0), Fraction(1, 57)],
        )
    ]
    l2, u2 = atanh_bounds(Fraction(2))
    l87, u87 = atanh_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_bounds(Fraction(64, 57))
    signs = []
    for moment in (13, 14):
        raw = (1, 16, 306, 6496 + moment)
        form = tuple(
            sum(raw[degree] * coefficient_forms[basis][degree] for degree in range(4))
            for basis in range(3)
        )
        coefficient_2 = Fraction(-(644921 - 128 * moment), 2544224)
        lower = coefficient_2 * u2 + form[0] * l87 + form[1] * l6457 - form[2]
        upper = coefficient_2 * l2 + form[0] * u87 + form[1] * u6457 - form[2]
        signs.append(1 if lower > 0 else -1 if upper < 0 else 0)
    assert signs == [1, -1]


def main() -> None:
    packet = json.loads(RESULT.read_text())
    atlas = json.loads(ATLAS.read_text())
    assert packet["schema"] == "e1-e25-profile-parity-route-probe-v1"
    assert packet["complete"] is True and packet["variance"] == 50 and packet["energy"] == 25
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(ATLAS.read_bytes()).hexdigest() == packet["atlas_sha256"]
    assert packet["cubic_cutoff"] == 13
    assert [row["moment"] for row in packet["cubic_boundary"]] == [13, 14]
    assert [row["certified_sign"] for row in packet["cubic_boundary"]] == [1, -1]
    verify_boundary()

    profiles = recursive_profiles(int(packet["l1_bound"]))
    assert packet["profiles"] == profiles and packet["profile_count"] == len(profiles)
    above = [row for row in profiles if int(row["cap"]) > 13]
    survivors = [row for row in above if int(row["odd_classes"]) <= 5]
    assert packet["above_cutoff"] == above
    assert packet["parity_survivors"] == survivors
    assert packet["survivors_by_odd_count"] == {
        str(odd): [row for row in survivors if int(row["odd_classes"]) == odd]
        for odd in (1, 3, 5)
    }

    geometry = atlas["light_geometry"]
    assert packet["atlas_input"] == {
        "support_counts": geometry["support_counts"],
        "orbit_counts": geometry["orbit_counts"],
    }
    used = {str(int(row["odd_classes"])) for row in survivors}
    templates = sum(int(geometry["orbit_counts"][odd]) for odd in used)
    assert packet["relevant_affine_templates"] == templates
    assert packet["direct_vector_floor"] == templates * 310_124 * 64
    assert packet["diameter_ledgers"] == [[1, -38], [5, -36], [9, -34], [17, -30], [21, -28]]

    trace = packet["slack_trace"]
    qualifying = [row for row in trace if row[2] is not None and int(row[2]) <= 25]
    assert qualifying and packet["l1_bound"] == qualifying[0][0]
    print(
        "E25_PROFILE_PARITY_PROBE_CHECK_PASS "
        f"l1={packet['l1_bound']} profiles={len(profiles)} survivors={len(survivors)} "
        f"templates={templates} floor={packet['direct_vector_floor']}"
    )


if __name__ == "__main__":
    main()

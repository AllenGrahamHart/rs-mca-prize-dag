#!/usr/bin/env python3
"""Independent audit of the E32 profile-(0,8) classification and packets."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"


def circular_distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def valuation(value: int) -> int:
    answer = 0
    while value % 2 == 0:
        value //= 2
        answer += 1
    return answer


def gap_classification() -> Counter[int]:
    valuations: Counter[int] = Counter()
    retained = 0
    for first_gap in range(1, 126):
        for second_gap in range(1, 127 - first_gap):
            for third_gap in range(1, 128 - first_gap - second_gap):
                last_gap = 128 - first_gap - second_gap - third_gap
                if last_gap <= 0:
                    continue
                support = (0, first_gap, first_gap + second_gap, first_gap + second_gap + third_gap)
                classes = Counter(
                    circular_distance(support[left], support[right])
                    for left in range(4)
                    for right in range(left + 1, 4)
                )
                if classes[64] not in (0, 2):
                    continue
                if any(count % 2 for chord, count in classes.items() if chord != 64):
                    continue
                retained += 1
                assert classes[64] == 2
                assert {(value + 64) % 128 for value in support} == set(support)
                step = next(value for value in support if 0 < value < 64)
                valuations[valuation(step)] += 1
    assert retained == 63
    return valuations


def main() -> None:
    assert gap_classification() == Counter({0: 32, 1: 16, 2: 8, 3: 4, 4: 2, 5: 1})
    production = json.loads((NOTES / "e32_profile08_light_template_census_result.json").read_text())
    audit = json.loads((NOTES / "e32_profile08_light_template_audit_result.json").read_text())
    assert len(production["rows"]) == 48 and len(audit["rows"]) == 6
    assert sum(int(row["vectors"]) for row in production["rows"]) == 119_087_616
    assert sum(int(row["vectors"]) for row in audit["rows"]) == 119_087_616
    assert all(int(row["profile_08"]) == 0 for row in production["rows"])
    assert all(int(row["profile_08"]) == 0 for row in audit["rows"])
    assert "folded_class" in (NOTES / "e32_profile08_light_template_census.cpp").read_text()
    assert "F(X)F(X^-1)" in (
        ROOT / "background/nodes/e1_n256_s16_e32_profile_08_light_template_exclusion/proof.md"
    ).read_text()

    print(
        "E1_N256_S16_E32_PROFILE_08_LIGHT_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "gap_profiles=63 valuations=6 engines=2 vectors=119087616"
    )


if __name__ == "__main__":
    main()

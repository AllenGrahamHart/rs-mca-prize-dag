#!/usr/bin/env python3
"""Verify the KoalaBear m2 V4 outer-recurrence router."""

from itertools import combinations
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROWS = ((2, 4), (4, 2), (8, 1))
CATALOGUE = (
    ("PSL(2,29)", 12180, (1, 29)),
    ("PGL(2,29)", 24360, (1, 29)),
    ("A30", 132626429906095529318154240000000, (1, 29)),
    ("S30", 265252859812191058636308480000000, (1, 29)),
)
DESTINATIONS = {
    2: (4, "m4_empty"),
    3: (6, "m6_to_m2"),
    5: (10, "m10_to_m2_m3_m6"),
    6: (12, "m12_empty"),
    10: (20, "source_profile_empty"),
    15: (30, "m30_to_m6_to_m2"),
}


def defect_profiles() -> set[tuple[int, int]]:
    profiles = set()
    for doubles in range(4):
        for triples in range(2):
            defect = doubles + 3 * triples
            used_weight = 2 * doubles + 3 * triples
            if defect <= 3 and used_weight <= 24:
                profiles.add((doubles, triples))
    return profiles


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    evidence = (NODE / "source_evidence.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "does not delete any" in statement
    assert "Recurrence to a degree-two decomposition" in contract
    assert (
        "1a923cc8f4428ec22864109cdc60d0c87326e8939cc1d72d217d22df2a4b8da0"
        in evidence
    )

    v4 = {(0, 0), (1, 0), (0, 1), (1, 1)}
    subgroups = {
        frozenset({(0, 0)}),
        frozenset({(0, 0), (1, 0)}),
        frozenset({(0, 0), (0, 1)}),
        frozenset({(0, 0), (1, 1)}),
        frozenset(v4),
    }
    orders = sorted(len(group) for group in subgroups)
    assert orders == [1, 2, 2, 2, 4]
    assert all(r * delta == 8 for r, delta in ROWS)
    assert {delta for _, delta in ROWS} == {1, 2, 4}

    live_r = {r for r, _ in ROWS}
    assert len(CATALOGUE) == 4
    assert all(subdegrees == (1, 29) for _, _, subdegrees in CATALOGUE)
    assert not any(live_r & set(row) for _, _, row in CATALOGUE)

    proper = tuple(value for value in range(2, 30) if 30 % value == 0)
    assert proper == tuple(DESTINATIONS)
    assert tuple(2 * value for value in proper) == tuple(
        inner for inner, _ in DESTINATIONS.values()
    )

    assert defect_profiles() == {(0, 0), (1, 0), (2, 0), (3, 0), (0, 1)}
    symmetric = {(doubles, 0) for doubles in range(4)}
    assert (0, 1) not in symmetric
    parity_rows = {
        doubles: tuple(
            fixed
            for fixed in range(doubles + 1)
            if (doubles - fixed) % 2 == 0
        )
        for doubles in range(4)
    }
    assert parity_rows == {0: (0,), 1: (1,), 2: (0, 2), 3: (1, 3)}

    labels = set(range(12))
    partner = {value: value ^ 1 for value in labels}
    fixed_edges = {
        frozenset(edge)
        for edge in combinations(labels, 2)
        if frozenset(partner[value] for value in edge) == frozenset(edge)
    }
    assert len(fixed_edges) == 6
    print("RATE_HALF_KB_M2_V4_OUTER_RECURRENCE_ROUTER_PASS")


if __name__ == "__main__":
    main()

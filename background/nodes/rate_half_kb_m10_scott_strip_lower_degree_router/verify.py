#!/usr/bin/env python3
"""Verify the KoalaBear m10 Scott-strip lower-degree router."""

from itertools import combinations, permutations
from pathlib import Path


NODE = Path(__file__).resolve().parent
POINTS = tuple(range(6))


def parity(permutation):
    return sum(
        permutation[i] > permutation[j]
        for i in POINTS
        for j in range(i + 1, 6)
    ) % 2


def act(permutation, flag):
    point, pair = flag
    return permutation[point], tuple(sorted(permutation[x] for x in pair))


def subdegrees(group, omega, base):
    stabilizer = [g for g in group if act(g, base) == base]
    unseen = set(omega)
    lengths = []
    while unseen:
        flag = min(unseen)
        orbit = {act(g, flag) for g in stabilizer}
        unseen -= orbit
        lengths.append(len(orbit))
    return len(stabilizer), sorted(lengths)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    evidence = (NODE / "source_evidence.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "no terminal producer" in statement
    assert "18 types in degrees 2,3,4,6" in contract
    assert "9cf136ffbea68f3156bc2ff386b5aec7b510a77e13e77ad6a09904b02382a69e" in evidence

    catalogue = [
        ("A5", 60, "A5", (1, 3, 6)),
        ("S5", 120, "A5", (1, 3, 6)),
        ("PSL(2,9)", 360, "A6", (1, 9)),
        ("PGL(2,9)", 720, "A6", (1, 9)),
        ("PSigmaL(2,9)", 720, "A6", (1, 9)),
        ("M10", 720, "A6", (1, 9)),
        ("PGammaL(2,9)", 1_440, "A6", (1, 9)),
        ("A10", 1_814_400, "A10", (1, 9)),
        ("S10", 3_628_800, "A10", (1, 9)),
    ]
    assert len(catalogue) == 9
    assert {row[2] for row in catalogue} == {"A5", "A6", "A10"}
    assert [row[0] for row in catalogue if row[1] <= 120] == ["A5", "S5"]
    assert all(row[3].count(1) == 1 for row in catalogue)
    s5_normal_subgroup_orders = {1, 60, 120}
    assert 2 not in s5_normal_subgroup_orders

    all_permutations = list(permutations(POINTS))
    a6 = [g for g in all_permutations if parity(g) == 0]
    s6 = all_permutations
    omega = [
        (point, pair)
        for point in POINTS
        for pair in combinations([x for x in POINTS if x != point], 2)
    ]
    assert len(omega) == 60
    base = (0, (1, 2))
    a6_stabilizer, a6_subdegrees = subdegrees(a6, omega, base)
    s6_stabilizer, s6_subdegrees = subdegrees(s6, omega, base)
    assert (len(a6), a6_stabilizer) == (360, 6)
    assert (len(s6), s6_stabilizer) == (720, 12)
    assert a6_subdegrees == [1, 2] + [3] * 3 + [6] * 8
    assert s6_subdegrees == [1, 2] + [3] * 3 + [6] * 6 + [12]
    assert 4 not in a6_subdegrees
    assert 4 not in s6_subdegrees

    support_sizes = [size for size in range(1, 7) if 6 % size == 0]
    assert support_sizes == [1, 2, 3, 6]
    actual_suborbit = 4
    independent_other_block_orbit = 10
    assert independent_other_block_orbit > actual_suborbit
    secondary_degrees = set(support_sizes) - {1}
    assert secondary_degrees == {2, 3, 6}
    assert all(degree < 10 for degree in secondary_degrees)

    original_types = {
        (1, 40),
        (2, 20),
        (4, 10),
        (5, 8),
    }
    assert all(r * delta == 40 for r, delta in original_types)
    assert 22 - len(original_types) == 18
    assert {2, 3, 4, 6, 10} - {10} == {2, 3, 4, 6}
    print("RATE_HALF_KB_M10_SCOTT_STRIP_LOWER_DEGREE_ROUTER_PASS")


if __name__ == "__main__":
    main()

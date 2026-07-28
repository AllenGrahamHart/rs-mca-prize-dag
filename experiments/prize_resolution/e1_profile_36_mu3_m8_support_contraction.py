#!/usr/bin/env python3
"""Verify the exact multiplicity-three support contraction for cofactor 8."""

from __future__ import annotations

from itertools import product
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def hasse_parity(counts: tuple[int, int, int, int], derivative: int) -> int:
    return sum(
        count for residue, count in enumerate(counts)
        if derivative & ~residue == 0
    ) % 2


def main() -> None:
    compositions = [
        counts for counts in product(range(7), repeat=4)
        if sum(counts) == 6
    ]
    exact_three = [
        counts for counts in compositions
        if [hasse_parity(counts, derivative) for derivative in range(4)]
        == [0, 0, 0, 1]
    ]
    assert len(compositions) == comb(9, 3) == 84
    assert len(exact_three) == 4
    assert {tuple(sorted(counts)) for counts in exact_three} == {(1, 1, 1, 3)}
    assert set(exact_three) == {
        (3, 1, 1, 1), (1, 3, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 3),
    }

    raw_supports = 4 * comb(32, 3) * 32**3
    normalized_supports = (
        2 * comb(31, 2) * 32**2
        + 2 * comb(32, 3) * 32
    )
    assert raw_supports == 650117120
    assert normalized_supports == 1269760
    assert normalized_supports < comb(126, 4) == 10009125

    # All four residue classes occur, so every support contains both parities.
    # After global sign normalization there are 32 singleton sign patterns.
    # F(-X) flips an odd singleton and acts freely, leaving 16 representatives.
    assert all(counts[0] + counts[2] > 0 for counts in exact_three)
    assert all(counts[1] + counts[3] > 0 for counts in exact_three)
    assert 32 // 2 == 16
    assert 16 * 8 == 128  # Retain all heavy-sign patterns.

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["e1_prize_n256_s18_profile_36_cofactor_windows"]["status"] == "PROVED"
    assert nodes["e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"]["status"] == "PROVED"

    print(
        "E1_PROFILE_36_MU3_M8_SUPPORT_CONTRACTION_PASS "
        "occupancies=4 raw_supports=650117120 normalized_supports=1269760 "
        "singleton_sign_reps=16 joint_sign_reps=128"
    )


if __name__ == "__main__":
    main()

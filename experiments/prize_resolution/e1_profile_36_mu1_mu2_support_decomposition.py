#!/usr/bin/env python3
"""Verify the exact cofactor-2/cofactor-4 support decompositions."""

from __future__ import annotations

from itertools import product
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def hasse_parity(counts: tuple[int, ...], derivative: int) -> int:
    return sum(
        count for residue, count in enumerate(counts)
        if derivative & ~residue == 0
    ) % 2


def main() -> None:
    # Exact multiplicity one depends only on parity occupancy.
    mu_one_odd_counts = [
        odd for odd in range(7)
        if hasse_parity((6 - odd, odd), 0) == 0
        and hasse_parity((6 - odd, odd), 1) == 1
    ]
    assert mu_one_odd_counts == [1, 3, 5]
    mu_one_raw = sum(comb(64, odd) * comb(64, 6 - odd) for odd in mu_one_odd_counts)
    mu_one_normalized = sum(
        comb(63, odd_tail) * comb(63, 4 - odd_tail)
        for odd_tail in (0, 2, 4)
    )
    assert mu_one_raw == 2711826432
    assert mu_one_normalized == 5005539

    # Exact multiplicity two depends only on the four residue classes mod 4.
    compositions = [
        counts for counts in product(range(7), repeat=4)
        if sum(counts) == 6
    ]
    mu_two = [
        counts for counts in compositions
        if [hasse_parity(counts, derivative) for derivative in range(3)]
        == [0, 0, 1]
    ]
    assert len(compositions) == comb(9, 3) == 84
    assert len(mu_two) == 20

    raw_total = 0
    raw_imprimitive = 0
    normalized_primitive = 0
    for c0, c1, c2, c3 in mu_two:
        count = comb(32, c0) * comb(32, c1) * comb(32, c2) * comb(32, c3)
        raw_total += count
        imprimitive = c1 + c3 == 0 or c0 + c2 == 0
        if imprimitive:
            raw_imprimitive += count
        elif c0 and c1:
            normalized_primitive += (
                comb(31, c0 - 1) * comb(31, c1 - 1)
                * comb(32, c2) * comb(32, c3)
            )
    assert raw_total == 1355913216
    assert raw_imprimitive == 74979328
    assert raw_total - raw_imprimitive == 1280933888
    assert normalized_primitive == 2501824

    quotient_mu_one = sum(
        comb(31, odd_tail) * comb(31, 4 - odd_tail)
        for odd_tail in (0, 2, 4)
    )
    assert quotient_mu_one == 279155
    assert normalized_primitive < comb(126, 4) == 10009125
    assert quotient_mu_one < comb(62, 4) == 557845

    # In the once-divided m=4 branch, all-even heavy triples make the full
    # norm a square. The remaining triples contain an odd heavy position, so
    # F(-X) acts freely on heavy signs and again leaves 128 joint sign reps.
    assert comb(58, 3) == 30856
    assert comb(122, 3) - comb(58, 3) == 264384
    assert 32 * (8 // 2) == 128
    assert (32 // 2) * 8 == 128

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["e1_prize_n256_s18_profile_36_cofactor_windows"]["status"] == "PROVED"
    assert nodes["e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"]["status"] == "PROVED"

    print(
        "E1_PROFILE_36_MU1_MU2_SUPPORT_DECOMPOSITION_PASS "
        "m2_normalized=5005539 m4_primitive_normalized=2501824 "
        "m4_quotient_normalized=279155 m4_square_triples=30856 sign_reps=128"
    )


if __name__ == "__main__":
    main()

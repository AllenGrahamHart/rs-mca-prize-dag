#!/usr/bin/env python3
"""Verify the prize N=256 leading-profile synthesis and weight frontier."""

from __future__ import annotations

import hashlib
import json
from functools import cache
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_exclusion"
SUPPLIERS = {
    "e1_low_square_mass_weighted_kernel_dictionary",
    "e1_prize_n256_s18_variance_cofactor_windows",
    "e1_prize_n256_s18_m1028_collision_exclusion",
    "e1_prize_n256_s18_m514_collision_exclusion",
    "e1_prize_n256_s18_m256_collision_exclusion",
    "e1_prize_n256_s18_m16_collision_exclusion",
    "e1_prize_n256_s18_m4_collision_exclusion",
    "e1_prize_n256_s18_m2_collision_exclusion",
}
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
EDGE_CAP = 65127585921474870475467050631501738502567
OLD_MAX = 1873053318886373426584792000465260242
NEW_MAX = 1386246316188473270092082114587711840


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@cache
def multiplicity(h: int, ell: int, a: int, b: int) -> int:
    n0 = h - a - b
    if n0 < 0:
        return 0
    total = 0
    for j in range(b + 1):
        for r in range(n0 + 1):
            tx = a + j + r
            ty = a + b - j + r
            if (
                tx <= ell
                and ty <= ell
                and (tx - ell) % 2 == 0
                and (ty - ell) % 2 == 0
            ):
                total += comb(b, j) * comb(n0, r) * 2**r
    return total


def eligible_profiles() -> list[tuple[int, int, int, int]]:
    rows = []
    for a in range(129):
        for b in range(129 - a):
            square_mass = 4 * a + b
            if not 0 < square_mass <= 66:
                continue
            if not (
                (b > 0 and square_mass >= 18)
                or (b == 0 and a >= 15)
            ):
                continue
            weight = multiplicity(128, 33, a, b)
            if weight:
                rows.append((weight, a, b, square_mass))
    return rows


def main() -> None:
    checks = 0
    pins = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pins.items():
        if key.endswith("_file"):
            assert digest(ROOT / value) == pins[key[:-5] + "_sha256"]
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges
        checks += 2

    profiles = eligible_profiles()
    assert len(profiles) == 271
    assert max(profiles) == (OLD_MAX, 4, 2, 18)
    residual = [row for row in profiles if row[1:3] != (4, 2)]
    assert len(residual) == 270
    assert max(residual) == (NEW_MAX, 3, 6, 18)
    cap = 2 * EDGE_CAP // NEW_MAX
    assert cap == 93962
    assert NEW_MAX * cap <= 2 * EDGE_CAP
    assert NEW_MAX * (cap + 1) > 2 * EDGE_CAP
    checks += 7

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    assert "Thus all seven classes are empty" in statement
    assert "|D_p(33)|<=93962" in statement
    assert "RowC" in (ROOT / "background" / "nodes" / NODE / "claim_contract.md").read_text()
    checks += 3
    print(
        "E1_PRIZE_N256_S18_PROFILE_EXCLUSION_PASS "
        f"eligible=271 residual=270 next=(3,6,18) cap={cap} checks={checks}"
    )


if __name__ == "__main__":
    main()

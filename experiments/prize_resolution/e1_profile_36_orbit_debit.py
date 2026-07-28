#!/usr/bin/env python3
"""Verify the exact aggregate debit of pure-dyadic profile-36 orbits."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EDGE_CAP = 65127585921474870475467050631501738502567
PROFILE_WEIGHT = 1386246316188473270092082114587711840
ORIENTED_VECTORS_PER_ORBIT = 256


def main() -> None:
    orbit_debit = ORIENTED_VECTORS_PER_ORBIT * PROFILE_WEIGHT
    maximum_orbits = (2 * EDGE_CAP) // orbit_debit
    remaining = 2 * EDGE_CAP - maximum_orbits * orbit_debit

    assert orbit_debit == 354879056944249157143573021334454231040
    assert maximum_orbits == 367
    assert maximum_orbits * ORIENTED_VECTORS_PER_ORBIT == 93952
    assert remaining == 14557944410300279242802433258774213454
    assert remaining // PROFILE_WEIGHT == 10
    assert (maximum_orbits + 1) * ORIENTED_VECTORS_PER_ORBIT == 94208
    assert (maximum_orbits + 1) * orbit_debit > 2 * EDGE_CAP

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["e1_low_square_mass_weighted_kernel_dictionary"]["status"] == "PROVED"
    assert nodes["e1_prize_n256_s18_profile_36_cofactor_windows"]["status"] == "PROVED"
    assert nodes["e1_official_low_square_mass_pair_budget"]["status"] == "TARGET"

    print(
        "E1_PROFILE_36_ORBIT_DEBIT_PASS oriented_per_orbit=256 "
        "maximum_orbits=367 oriented_used=93952 residual_equivalent=10 "
        "orbit_368_fails=true"
    )


if __name__ == "__main__":
    main()

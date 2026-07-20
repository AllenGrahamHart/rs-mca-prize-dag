#!/usr/bin/env python3
"""Verify the exact exceptional-only quotient-distance ceiling arithmetic."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


E = 2**38 - 1
R = 2 * E + 1
ORDINARY = 4 * E
EXCEPTIONAL_ROOTS = R - 1
LOWER = 2 * E // 3 + 3
NODE = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_"
    "quotient_distance_ceiling"
)
DEPS = {
    "rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_"
    "two_sided_resultant_saturation",
}


def quotient_ceiling(root_ordinary_degree: int) -> Fraction:
    root_incidence = EXCEPTIONAL_ROOTS * root_ordinary_degree
    return Fraction(ORDINARY * R - root_incidence, ORDINARY)


def main() -> None:
    ceiling = quotient_ceiling(E - 1)
    assert EXCEPTIONAL_ROOTS == 2 * E
    assert ceiling.denominator == 1
    assert ceiling == Fraction(3 * (E + 1), 2)
    assert ceiling == 412316860416
    assert LOWER == 183251937965
    assert R + 2 == 549755813889
    assert (R + 2) - int(ceiling) == 137438953473
    assert int(ceiling) - LOWER + 1 == 229064922452

    # The ceiling must react to either load-bearing saturation count.
    assert quotient_ceiling(E - 2) != ceiling
    assert quotient_ceiling(E) != ceiling

    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    node = next(item for item in dag["nodes"] if item["id"] == NODE)
    assert node["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dep in DEPS:
        assert (dep, NODE, "req") in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "QUOTIENT_DISTANCE_CEILING_PASS "
        f"e={E} lower={LOWER} upper={int(ceiling)} "
        f"upper_killed={(R+2)-int(ceiling)}"
    )


if __name__ == "__main__":
    main()

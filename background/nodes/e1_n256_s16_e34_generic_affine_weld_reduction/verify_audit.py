#!/usr/bin/env python3
"""Independent packet audit for the E34 generic affine-weld reduction."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e34_generic_orbit_result.json"


def main() -> None:
    packet = json.loads(PACKET.read_text())
    assert packet["complete"] is True and packet["errors"] == []
    primary = packet["results"]["primary"]
    audit = packet["results"]["audit"]
    assert primary["rows"] == audit["rows"] and len(primary["rows"]) == 57
    assert sum(row["heavy_triples"] for row in primary["rows"]) == 325376
    shapes = Counter(
        (
            tuple(row["weld_sizes"]),
            tuple(row["pair_intersections"]),
            row["triple_intersection"],
            row["union_size"],
            row["supports"],
        )
        for row in primary["rows"]
    )
    assert shapes == Counter(
        {
            ((4, 4, 4), (1, 1, 1), 0, 9, 66405): 52,
            ((3, 4, 4), (2, 1, 1), 0, 7, 72486): 4,
            ((3, 4, 3), (2, 1, 2), 0, 5, 58325): 1,
        }
    )
    assert sum(row["census_vectors"] for row in primary["rows"]) == 243285056
    print(
        "E1_N256_S16_E34_GENERIC_AFFINE_WELD_REDUCTION_AUDIT_PASS "
        "orbits=57 shapes=3"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent packet audit for the E32 common four-odd light router."""

from __future__ import annotations

import json
import subprocess
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"


def distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def main() -> None:
    completed = subprocess.run(
        ["python3", str(NOTES / "e32_four_odd_light_orbit_check.py")],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "repeated_wedges=148 mutation=1" in completed.stdout
    packet = json.loads((NOTES / "e32_four_odd_light_orbit_result.json").read_text())
    rows = packet["rows"]
    assert isinstance(rows, list) and len(rows) == 148
    for row in rows:
        representative = tuple(map(int, row["representative"]))
        repeated = int(row["repeated_distance"])
        edges = [
            frozenset((left, right))
            for left, right in combinations(representative, 2)
            if distance(left, right) == repeated
        ]
        assert len(edges) == 2 and edges[0] & edges[1]
        assert all(distance(left, right) != 64 for left, right in combinations(representative, 2))
    assert sum(int(row["normalized_count"]) for row in rows[:-1]) < 28_800

    print(
        "E1_N256_S16_E32_FOUR_ODD_LIGHT_TEMPLATE_REDUCTION_AUDIT_PASS "
        "representatives=148 all_wedges=true no_light_diameters=true mutation=1"
    )


if __name__ == "__main__":
    main()

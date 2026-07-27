#!/usr/bin/env python3
"""Independent packet audit for the E34 progression exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
MULTIPLICITIES = {1: 32, 2: 16, 4: 8, 8: 4, 16: 2}


def main() -> None:
    primary = json.loads((NOTES / "e34_progression_census_result.json").read_text())
    audit = json.loads((NOTES / "e34_progression_audit_result.json").read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["errors"] == audit["errors"] == []
    assert len(primary["results"]) == len(audit["results"]) == 5

    keys = (
        "t",
        "supports",
        "vectors",
        "energy_34",
        "profile_67",
        "full_conductor",
        "maximum_m3",
    )
    for expected_t, left, right in zip(MULTIPLICITIES, primary["results"], audit["results"]):
        assert left["t"] == right["t"] == expected_t
        assert left["supports"] == 1195965 and left["vectors"] == 38270880
        assert all(left[key] == right[key] for key in keys)

    weighted = {
        key: sum(MULTIPLICITIES[result["t"]] * result[key] for result in primary["results"])
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert weighted == {
        "supports": 74149830,
        "vectors": 2372794560,
        "energy_34": 5768472,
        "profile_67": 3618496,
        "full_conductor": 3131008,
    }
    assert max(result["maximum_m3"] for result in primary["results"]) == 1722

    assert 1722 < 1947 and not 1948 < 1947
    assert sum(MULTIPLICITIES.values()) == 62
    print(
        "E1_N256_S16_E34_PROGRESSION_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "shards=5 orbits=62 mutations=2"
    )


if __name__ == "__main__":
    main()

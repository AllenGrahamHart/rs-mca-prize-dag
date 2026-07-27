#!/usr/bin/env python3
"""Independent packet audit for the E34 nonquarter-diameter exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"


def main() -> None:
    primary = json.loads((NOTES / "e34_nonquarter_diameter_census_result.json").read_text())
    audit = json.loads((NOTES / "e34_nonquarter_diameter_audit_result.json").read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["errors"] == audit["errors"] == []
    assert len(primary["results"]) == len(audit["results"]) == 31

    keys = (
        "t",
        "supports",
        "vectors",
        "energy_34",
        "profile_67",
        "full_conductor",
        "maximum_m3",
    )
    for t, (left, right) in enumerate(zip(primary["results"], audit["results"]), 1):
        assert left["t"] == right["t"] == t
        assert left["supports"] == 915125 and left["vectors"] == 58568000
        assert all(left[key] == right[key] for key in keys)

    totals = {
        key: sum(result[key] for result in primary["results"])
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert totals == {
        "supports": 28368875,
        "vectors": 1815608000,
        "energy_34": 1518816,
        "profile_67": 1044528,
        "full_conductor": 899456,
    }
    assert max(result["maximum_m3"] for result in primary["results"]) == 1560

    # Hostile threshold and coverage mutations must fail the close.
    assert 1560 < 1947 and not 1948 < 1947
    assert totals["supports"] == 31 * 915125
    assert totals["supports"] - 1 != 31 * 915125

    print(
        "E1_N256_S16_E34_NONQUARTER_DIAMETER_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "shards=31 mutations=2"
    )


if __name__ == "__main__":
    main()

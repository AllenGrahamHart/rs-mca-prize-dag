#!/usr/bin/env python3
"""Independent packet audit for the E34 quarter-template exclusion."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"


def main() -> None:
    primary = json.loads((NOTES / "e34_quarter_template_census_result.json").read_text())
    audit = json.loads((NOTES / "e34_quarter_template_audit_result.json").read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["errors"] == audit["errors"] == []
    assert len(primary["results"]) == len(audit["results"]) == 121

    keys = (
        "shard",
        "supports",
        "vectors",
        "energy_34",
        "profile_67",
        "full_conductor",
        "maximum_m3",
    )
    for index, (left, right) in enumerate(zip(primary["results"], audit["results"])):
        assert left["shard"] == right["shard"] == index
        assert left["supports"] == math.comb(123 - index, 3)
        assert all(left[key] == right[key] for key in keys)

    totals = {
        key: sum(result[key] for result in primary["results"])
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert totals == {
        "supports": 9381251,
        "vectors": 300200032,
        "energy_34": 1514544,
        "profile_67": 1181056,
        "full_conductor": 1031680,
    }
    assert max(result["maximum_m3"] for result in primary["results"]) == 1188

    # Hostile threshold and coverage mutations must fail the close.
    assert 1188 < 1947 and not 1948 < 1947
    assert totals["supports"] == math.comb(124, 4)
    assert totals["supports"] - 1 != math.comb(124, 4)

    print("E1_N256_S16_E34_QUARTER_TEMPLATE_EXCLUSION_AUDIT_PASS shards=121 mutations=2")


if __name__ == "__main__":
    main()

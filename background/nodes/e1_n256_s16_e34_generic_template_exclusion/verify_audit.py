#!/usr/bin/env python3
"""Independent packet audit for the E34 generic exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"


def main() -> None:
    primary = json.loads((NOTES / "e34_generic_census_result.json").read_text())
    audit = json.loads((NOTES / "e34_generic_audit_result.json").read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["errors"] == audit["errors"] == []
    assert len(primary["results"]) == len(audit["results"]) == 57
    keys = (
        "orbit",
        "heavy",
        "supports",
        "vectors",
        "energy_34",
        "profile_67",
        "full_conductor",
        "maximum_m3",
    )
    for orbit, (left, right) in enumerate(zip(primary["results"], audit["results"])):
        assert left["orbit"] == right["orbit"] == orbit
        assert all(left[key] == right[key] for key in keys)
    totals = {
        key: sum(result[key] for result in primary["results"])
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert totals == {
        "supports": 3801329,
        "vectors": 243285056,
        "energy_34": 793742,
        "profile_67": 505466,
        "full_conductor": 418464,
    }
    assert max(result["maximum_m3"] for result in primary["results"]) == 1770
    assert 1770 < 1947 and not 1948 < 1947
    print(
        "E1_N256_S16_E34_GENERIC_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "shards=57 mutations=2"
    )


if __name__ == "__main__":
    main()

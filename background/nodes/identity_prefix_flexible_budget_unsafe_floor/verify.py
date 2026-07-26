#!/usr/bin/env python3
"""Check the harvested unsafe-floor contract and its deployed evidence links."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "identity_prefix_flexible_budget_unsafe_floor"
TARGET = "unsafe_crossing_family_instantiation"


def main():
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin["commit"] == "b13de8113a03f06b6fc22bbd2f289a8abcdf7e95"
    assert pin["sha256"] == "356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce"
    assert set(pin["labels"]) == {
        "lem:capff1-identity-prefix-floor",
        "cor:capg-budget-conversion",
        "prop:capg-moved-frontier",
    }

    checked = 0
    for n in range(3, 25):
        for k in range(1, n):
            for m in range(k + 1, n + 1):
                w = m - k - 1
                for base_size in (2, 3, 4, 5):
                    den = base_size**w
                    num = math.comb(n, m)
                    for budget in range(0, 8):
                        ceil_floor = (num + den - 1) // den >= budget + 1
                        strict_floor = num > den * budget
                        assert ceil_floor == strict_floor
                        checked += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert status[NODE] == "PROVED"
    assert status[TARGET] == "TARGET"
    assert (NODE, TARGET, "ev") in edges
    assert ("deployed_identity_prefix_owner_scope_audit", TARGET, "ev") in edges

    rows = json.loads(
        (ROOT / "background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json")
        .read_text()
    )["rows"]
    mca_rows = [row for row in rows if row["object"] == "MCA"]
    assert len(mca_rows) == 2
    for row in mca_rows:
        assert row["owner"] == "SIMPLE_POLE_LIST"
        assert row["a_plus"] == row["a0"] + 1
        assert row["attack_a0"] > row["B_star"]
        assert row["attack_a_plus"] <= row["B_star"]

    # Off-by-one controls: equality does not supply the required extra slope.
    assert math.ceil(8 / 2) == 4
    assert not (8 > 2 * 4)
    assert 9 > 2 * 4

    print(
        "IDENTITY_PREFIX_FLEXIBLE_BUDGET_UNSAFE_FLOOR_PASS "
        f"arithmetic_contracts={checked} deployed_mca_rows={len(mca_rows)}"
    )


if __name__ == "__main__":
    main()

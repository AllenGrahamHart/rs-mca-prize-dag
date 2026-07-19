#!/usr/bin/env python3
"""Verify the NG-COUNT contract and its strip-free implication."""

from __future__ import annotations

import json
from pathlib import Path


NODE = "f3_hge4_norm_gate_count"
ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node = nodes[NODE]
    assert node["status"] == "TARGET" and node.get("key") is True
    for token in (
        "14 n^3",
        "F-4-minimal",
        "norm-gate",
        "p >= n^2",
        "NG-ZERO is NOT",
    ):
        assert token in node["statement"]

    required_edge = {
        "from": NODE,
        "to": "f3_hge4_aggregate_budget",
        "kind": "req",
    }
    assert required_edge in dag["edges"]

    statement = (Path(__file__).with_name("statement.md")).read_text()
    attack = (Path(__file__).with_name("attack.md")).read_text()
    frontier = (Path(__file__).with_name("frontier.md")).read_text()
    contract = (Path(__file__).with_name("claim_contract.md")).read_text()
    for token in (
        "H_max=min(k+t,floor(n/2))",
        "N_h^strip",
        "N_h^raw",
        "(NG-COUNT)",
        "(RAW-NG)",
        "U2-boundary",
        "DLI/skew",
        "NG-ZERO is not claimed",
    ):
        assert token in statement
    assert "N_h^strip <= N_h^raw" in attack
    assert "raw non-toral count zero" in frontier
    assert "the full official corridor" in contract

    # The aggregate compiler reserves 1+1+14=16 cubic units. Raising the
    # HGE4 allocation to 15 breaks that exact split.
    for n in (2**13, 2**20, 2**41):
        unit = n**3
        assert unit + unit + 14 * unit == 16 * unit
        assert unit + unit + 15 * unit > 16 * unit

    # Exhaustive tiny monotonicity check for the only implication asserted by
    # this node: deletion cannot increase a record count.
    checked = 0
    for raw4 in range(6):
        for raw5 in range(6):
            for strip4 in range(raw4 + 1):
                for strip5 in range(raw5 + 1):
                    raw_total = raw4 + raw5
                    strip_total = strip4 + strip5
                    assert strip_total <= raw_total
                    for budget in range(12):
                        if raw_total <= budget:
                            assert strip_total <= budget
                    checked += 1

    refs = set(node.get("refs", []))
    expected_refs = {
        f"critical/nodes/{NODE}/statement.md",
        f"critical/nodes/{NODE}/attack.md",
        f"critical/nodes/{NODE}/frontier.md",
        f"critical/nodes/{NODE}/claim_contract.md",
        f"critical/nodes/{NODE}/verify.py",
    }
    assert expected_refs <= refs
    assert all((ROOT / ref).is_file() for ref in expected_refs)
    print(f"F3_HGE4_NORM_GATE_COUNT_CONTRACT_PASS monotonicity_cases={checked}")


if __name__ == "__main__":
    main()

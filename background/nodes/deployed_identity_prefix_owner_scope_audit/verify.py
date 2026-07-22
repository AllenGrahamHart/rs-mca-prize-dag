#!/usr/bin/env python3
"""Verify row pins and ownership for the deployed identity-prefix audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "deployed_identity_prefix_owner_scope_audit"
PARENTS = {
    "v13_2_discrete_subfield_census_guard",
    "l1_interior_bc_floor_higher_shell_q_routing",
    "f1_full_field_pole_forcing",
    "f1_pole_same_rate_scope_router",
}


def main() -> None:
    data = json.loads((Path(__file__).with_name("deployed_rows.json")).read_text())
    assert data["upstream_commit"] == "32a41660e3088eeeb15a16645330856794302ff0"
    assert data["compiler_sha256"] == "70dcc2b07bc9e9d70af59305ea02437020095007aedf4846185df1a3c0a04ca8"
    assert data["paving_sha256"] == "8e89be94dd6291dc5563897e72ae34b49880512cd37f72287b4288ff030cbbc0"
    assert data["compiler_architecture_id"] == "GRANDE_FINALE_V3_EXACT_COMPLETION"

    expected_ids = {"kb_mca", "kb_list", "m31_mca", "m31_list"}
    assert {row["row_id"] for row in data["rows"]} == expected_ids
    for row in data["rows"]:
        assert row["a_plus"] == row["a0"] + 1
        assert row["w"] == row["a_plus"] - row["K"]
        assert row["attack_a0"] > row["B_star"]
        assert row["attack_a_plus"] <= row["B_star"]
        assert row["B_star"] // row["attack_a_plus"] == row["full_budget_Q_multiplier"]
        assert row["owner"] == (
            "SIMPLE_POLE_LIST" if row["object"] == "MCA" else "Q_BOUNDARY"
        )
        assert row["official_smooth_scope"] == row["row_id"].startswith("kb_")

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert status[NODE] == "PROVED"
    for parent in PARENTS:
        assert status[parent] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, "mca_safe", "ev") in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges

    higher_q = (
        ROOT / "background/nodes/l1_interior_bc_floor_higher_shell_q_routing/statement.md"
    ).read_text()
    pole = (ROOT / "critical/nodes/f1_full_field_pole_forcing/statement.md").read_text()
    scope = (
        ROOT / "background/nodes/f1_pole_same_rate_scope_router/statement.md"
    ).read_text()
    assert "higher-shell boundary-Q mass" in higher_q
    assert "FORCES the pole mechanism" in pole
    assert "same rate" in scope

    print("DEPLOYED_IDENTITY_PREFIX_OWNER_SCOPE_AUDIT_PASS rows=4 verdict=NO_ISSUE")


if __name__ == "__main__":
    main()

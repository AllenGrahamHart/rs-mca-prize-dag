#!/usr/bin/env python3
"""Verify the source-bound finite-Q shortcut route cuts."""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_CEILING, getcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "upstream_finite_q_shortcut_route_cuts"
PARENT = "deployed_identity_prefix_owner_scope_audit"


def moment_floor(base: int, width: int, delta: str) -> int:
    getcontext().prec = 50
    log2_base = Decimal(base).ln() / Decimal(2).ln()
    value = Decimal(width) * log2_base / Decimal(delta)
    return int(value.to_integral_value(rounding=ROUND_CEILING))


def main() -> None:
    data = json.loads(Path(__file__).with_name("route_cuts.json").read_text())
    assert data["upstream_commit"] == "32a41660e3088eeeb15a16645330856794302ff0"
    assert data["grande_finale_sha256"] == "34618918de8fc1c1aac5642393f49019c60ff7041a9efeacbf0b8ea01eb3d8cd"
    assert data["lean_table_sha256"] == "7f94c2530f35439366b24ac5e0a91d255bf4f9609a93dc434c0dfed0380ba3be"

    expected_floors = [94196, 94991, 641593, 680397]
    expected_dimensions = [913633, 913634, 913681, 913682]
    assert [row["moment_floor_real"] for row in data["rows"]] == expected_floors
    assert [row["boundary_q_dimension"] for row in data["rows"]] == expected_dimensions

    n = 1 << 21
    for row in data["rows"]:
        assert moment_floor(row["base"], row["w"], row["delta_real_12"]) == row[
            "moment_floor_real"
        ]
        assert n - row["a_plus"] - row["w"] == row["boundary_q_dimension"]
        assert Decimal(row["packing_log2"]) - Decimal(row["delta_real_12"]) > 1_660_000
    assert data["rows"][2]["moment_floor_ceiling_average"] == 641594
    assert data["rows"][2]["moment_floor_real"] == 641593

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert status[NODE] == "PROVED" and status[PARENT] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, "f2_growing_order_myerson", "ev") in edges
    assert (NODE, "xr_tangent_support_mismatch_bridge", "ev") in edges

    statement = (Path(__file__).with_name("statement.md")).read_text()
    assert "r(Delta_Q-log2(tau))" in statement
    assert "unless `tau=1`" in statement

    print(
        "UPSTREAM_FINITE_Q_SHORTCUT_ROUTE_CUTS_PASS "
        "moment_floors=94196,94991,641593,680397 dimensions=4"
    )


if __name__ == "__main__":
    main()

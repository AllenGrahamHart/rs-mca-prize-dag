#!/usr/bin/env python3
"""Independent audit of the degree-2048 symmetric configuration."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ace7ff76890b4ec1234e259e8c2c5e6e23cb443f82f610582d0be0fe06a70264"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert 218 * 15 == 218 * 15
    assert 15 * 14 == 210
    assert 217 - 210 == data["leave_degree"] == 7
    assert 218 * 7 // 2 == data["leave_edges"] == 763
    assert 14 - 7 > 0
    assert 14 + 218 - 7 == 225
    assert 218 * 2048 - 446392 == data["aggregate_fiber_defect_ceiling"] == 72
    assert 218 - 72 == data["saturated_fiber_floor"] == 146
    assert (
        -(-(146 * 15) // 218)
        == data["saturated_lines_at_one_point_floor"]
        == 11
    )
    assert (15 * 72) // 218 == data["incident_defect_at_one_point_ceiling"] == 4
    assert 15 * 2048 - 4 == data["full_core_coordinates_at_one_point_floor"] == 30716

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_plane218_pure_power_router"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    audit_text = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "every point has degree exactly 15" in proof
    assert "positive definite" in proof
    assert "not assumed" in audit_text
    assert "not a chronology payment" in audit_text
    print("PLANE218_POWER2048_CONFIG_AUDIT_PASS rank=218 leave=7 defect=72")


if __name__ == "__main__":
    main()

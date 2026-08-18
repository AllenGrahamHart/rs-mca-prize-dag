#!/usr/bin/env python3
"""Independent audit of the dimension-three pair-overlap moment floor."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "eef820acd53814309a2862a5328f8cf1aa3132b001109ed5dc0cdbc45a485aed"


def independently_balance(k_prime: int) -> tuple[int, int]:
    slots = 1048576 + k_prime
    marks = 520 * (67470 + k_prime)
    low = marks // slots
    high_slots = marks - low * slots
    low_slots = slots - high_slots
    required = low_slots * low * (low - 1) // 2
    required += high_slots * (low + 1) * low // 2
    available = 520 * 519 // 2 * (k_prime - 1)
    return available - required, low


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    boundaries = ((3, 33), (1167, 33), (1168, 34), (3331, 34),
                  (3332, 35), (4835, 35), (4836, 35), (5505, 36))
    for k_prime, expected_floor in boundaries:
        _, actual_floor = independently_balance(k_prime)
        assert actual_floor == expected_floor
    assert independently_balance(4835)[0] == -data["last_excluded_deficit"] == -2110
    assert independently_balance(4836)[0] == data["first_feasible_slack"] == 115260
    assert data["first_feasible_residual_dimension"] == 4836
    assert data["residual_dimension_ceiling"] == 595763
    assert 1048576 - 595763 == data["common_core_floor"] == 452813
    assert 1048576 - 4836 == data["common_core_ceiling"] == 1043740
    assert 4922 - 4836 + 1 == data["shared_payment_overlap_row_count"] == 87

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    parent = "rate_half_mca_rank11_pair_pencil_dimension_three_rich_plane_recurrence_sharpening"
    assert nodes[parent]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "gap(4835)=-2110" in proof
    assert "gap(4836)=115260" in proof
    assert "cauchy bound is weaker" in audit
    assert "no source-interface transport" in audit
    print("RANK11_D3_PAIR_MOMENT_AUDIT_PASS interval=4836..595763 payment_rows=87")


if __name__ == "__main__":
    main()

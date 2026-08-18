#!/usr/bin/env python3
"""Independent audit of the q=3170 saturated plane-line endpoint."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "aa8c63b148f1fc666e055dd05357ef1a0a9b492c6d0bbbbcd8a70cb666f24406"


def c2(value: int) -> int:
    return value * (value - 1) // 2


def ceil_ratio(a: int, b: int) -> int:
    value = a // b
    return value if value * b == a else value + 1


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    minima = []
    for kprime in range(4960, 4983):
        full = -13661092 + 2953 * kprime
        planes = ceil_ratio(full, kprime - 2044)
        marks = 218 * planes
        low = marks // 3170
        high_points = marks - low * 3170
        low_points = 3170 - high_points
        required = low_points * c2(low) + high_points * c2(low + 1)
        gap = 15 * c2(planes) - required
        saturated = c2(planes) - gap
        minima.append((planes, saturated))
    assert min(item[0] for item in minima) == data["distinct_plane_floor"] == 339
    assert max(item[0] for item in minima) == data["distinct_plane_ceiling_on_rows"] == 358
    assert min(item[1] for item in minima) == data["minimum_saturated_plane_pairs"] == 22752
    assert ceil_ratio(22752, c2(15)) == data["distinct_saturated_line_floor"] == 217
    assert (15 * 1116046 - 2097152) // 14 == \
        data["saturated_line_common_core_floor"] == 1045967
    assert 4960 - 2609 == data["saturated_line_residual_recurrence_floor"] == 2351

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_plane218_projective_direction_bank"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "ceil(22752/105)=217" in proof
    assert "actual received-pair core" in audit
    print("RANK11_D3_ENDPOINT_DESIGN_AUDIT_PASS rows=23 planes=339..358 lines=217 recurrence=2351")


if __name__ == "__main__":
    main()

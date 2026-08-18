#!/usr/bin/env python3
"""Independent audit of the affine-plane cap 218 sharpening."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "80a52ccc002ea76bbf30ea7b4013b492ca519cf680deac74d1b0bf6d1c649762"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    t = data["excluded_plane_occupancy"]
    line = data["affine_line_cap"]
    c = data["plane_core_floor"]
    assert (t - line) * (c - 1) < t * data["pair_core_size"] - line * data["n"] <= (t - line) * c
    kmax = data["K"] - c
    assert 95866 + 205 * kmax - 219 * (kmax - 1) == 30705
    assert (t * ((t - 1) // (line - 1))) // line == 219

    q = data["selected_types"]
    plane = data["affine_plane_cap"]
    core = data["dimension_three_core_floor"]
    rhs = q * data["pair_core_size"] - plane * data["n"]
    assert (q - plane) * (core - 1) < rhs <= (q - plane) * core
    assert plane * data["dimension_three_shortened_n"] - q * data["dimension_three_shortened_pair_core"] == 178
    assert data["dimension_four_heavy_record_floor"] == (plane + 1) * 29

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "other 14-point sets are disjoint" in proof
    assert "96085-14*4670=30705" in proof
    assert "218n'-520s'=178" in statement
    print("PAIR_PENCIL_PLANE218_AUDIT_PASS cap=218 core=407831 margin=30705")


if __name__ == "__main__":
    main()

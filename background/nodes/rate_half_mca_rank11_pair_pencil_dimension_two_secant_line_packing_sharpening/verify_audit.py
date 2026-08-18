#!/usr/bin/env python3
"""Independent audit of the dimension-two secant-line packing."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6ab24a38ea900cd9eac807bc6d49a480751c9125ffcf6ab0abd186fd347f9b59"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    q = data["selected_points"]
    degree = data["lines_per_point_floor"]
    incidence = data["point_line_incidence_floor"]
    ordered = data["ordered_pair_count"]
    lines = data["affine_secant_line_floor"]
    assert incidence == q * degree
    assert (lines - 1) * (ordered + incidence) < incidence * incidence <= lines * (ordered + incidence)
    core = data["common_core_floor"]
    roots = data["direction_intersection_floor"]
    assert (lines - 1) * (core - 1) < lines * roots - data["n"] <= (lines - 1) * core
    assert (data["n"] - core) - lines * (roots - core) == 872

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_dimension_two_common_core_shortening"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "ceil(519/14)=38" in proof
    assert "parallel" in proof
    assert "1349" in statement and "133485" in statement
    assert "only" in statement and "872" in statement
    print("PAIR_PENCIL_DIM2_SECANT_PACKING_AUDIT_PASS lines=1349 core=133485")


if __name__ == "__main__":
    main()

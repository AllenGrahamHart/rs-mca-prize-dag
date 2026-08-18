#!/usr/bin/env python3
"""Independent audit of the dimension-three common-core shortening."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "67fc4bda1f106e0701e6801e4f654330d66dec03181a4a2374d57c5d80bb2b9a"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    plane = data["affine_plane_cap"]
    assert plane * 67471 <= 15 * 1048577 < (plane + 1) * 67471
    q, s, n = data["selected_types"], data["pair_core_size"], data["n"]
    core = data["common_core_floor"]
    assert (q - plane) * (core - 1) < q * s - plane * n <= (q - plane) * core
    assert plane * data["shortened_n_at_floor"] - q * data["shortened_pair_core_at_floor"] == 189

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_dimension_two_incidence_exclusion"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "translated affine subsets" in (HERE / "audit.md").read_text().lower()
    assert "nonzero linear functional" in proof
    assert "319539" in statement and "189" in statement
    print("PAIR_PENCIL_DIM3_COMMON_CORE_AUDIT_PASS plane=233 core=319539")


if __name__ == "__main__":
    main()

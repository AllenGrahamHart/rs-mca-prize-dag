#!/usr/bin/env python3
"""Independent audit of the 218-plane pure-power router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8726a61ae156eb16e99b079545303aa1c43cdadb5b47c9a62122618a6f5fa17a"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    feasible: list[tuple[int, int]] = []
    for e in (1 << exponent for exponent in range(22)):
        for k in range(2044, 5026):
            if e <= k - 1 and 28396 + 204 * k <= 218 * e:
                feasible.append((e, k))
    by_degree: dict[int, list[int]] = {}
    for e, k in feasible:
        by_degree.setdefault(e, []).append(k)
    assert {e: (min(rows), max(rows), len(rows)) for e, rows in by_degree.items()} == {
        2048: (2049, 2049, 1),
        4096: (4097, 4237, 141),
    }
    assert (28396 + 204 * 2049, 218 * 2048) == (446392, 446464)
    assert 218 * 2048 - (28396 + 204 * 2049) == 72
    assert 210 * 4096 < 28396 + 204 * 4097 <= 211 * 4096
    assert 218 * 4096 - (28396 + 204 * 4097) == 28744
    assert data["cases"]["4096"]["duplicate_line_ceiling"] == 218 - 211

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_plane218_projective_direction_bank"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    audit_text = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "f<=re<=218e" in proof
    assert "projective equivalence to a pure power" in audit_text
    assert "does not assert" in audit_text
    print("PAIR_PENCIL_PLANE218_POWER_AUDIT_PASS degrees=2048,4096 rows=1,141")


if __name__ == "__main__":
    main()

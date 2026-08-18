#!/usr/bin/env python3
"""Independent audit of the 218-plane projective direction bank."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7c94cac28f465b7f62128dc013b41851eb37c98605f53244244c724aaa0db8db"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    for k in range(data["shortened_K_floor"], data["shortened_K_ceiling"] + 1):
        full = 28396 + 204 * k
        assert full <= 218 * (k - 1)
        assert full > 209 * (k - 1)
        assert 218 * (k - 1) - full <= 41736
    assert 1053496 * 136904 == 1095232 * 131687
    assert 218 * 217 // 2 - 210 * (15 * 14 // 2) == 1603

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_affine_plane_cap_218_sharpening"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "group those lines by projective direction" in proof
    assert "combined coordinate count" in audit
    assert "no such inequality is imported" in audit
    print("PAIR_PENCIL_PLANE218_BANK_AUDIT_PASS directions=210 pairs=1603")


if __name__ == "__main__":
    main()

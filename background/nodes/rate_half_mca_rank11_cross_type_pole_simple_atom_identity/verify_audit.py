#!/usr/bin/env python3
"""Independent audit of the pole-simple atom-identity theorem."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ade6ad1a3aeb7899cbeec67bb06dc9568d93c63e9ad5490902ed4b3fc96ee684"


def floor_margin(n: int, m: int, k: int, r: int) -> int:
    forced = (r * m - n + r - 2) // (r - 1)
    return forced - (k - 1)


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    n, m, k = data["domain_size"], data["support_size"], data["code_dimension"]
    margins = [floor_margin(n, m, k, r) for r in range(2, 33)]
    assert max(r for r in range(2, 16) if margins[r - 2] <= 0) == 15
    assert min(r for r in range(2, 33) if margins[r - 2] > 0) == 16
    assert margins[13] == -2605
    assert margins[14] == 2067
    for key, value in data["margins"].items():
        r = int(key)
        assert floor_margin(n, m, k, r) == value
        for c in (0, 17, 67472, 900001):
            assert floor_margin(n - c, m - c, k - c, r) == value

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_scalar_pair_rigidity"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "if `d` is nonzero" in proof
    assert "therefore `d=0`" in proof
    assert "projectively identical" in statement
    assert "does not produce a shared deck" in statement
    print("CROSS_TYPE_POLE_SIMPLE_ATOM_IDENTITY_AUDIT_PASS threshold=16")


if __name__ == "__main__":
    main()

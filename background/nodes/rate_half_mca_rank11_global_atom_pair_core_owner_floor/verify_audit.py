#!/usr/bin/env python3
"""Independent audit of the global-atom pair-core owner floor."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "deaebba8de032ae673d53863d29d5b57610dc35c09a6098c1fa6b28f31f58e20"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    q = data["quotient_type_floor"]
    s = data["pair_core_size"]
    c = data["pair_intersection_cap"]
    bound = Fraction(q * s * s, s + (q - 1) * c)
    assert data["owner_floor"] == -(-bound.numerator // bound.denominator)
    assert data["owner_floor"] - data["generic_large_owner_floor"] == data["improvement"]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_global_atom_record_extension"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "belongs to all 18 anchor supports" in proof
    assert "cauchy--schwarz" in proof
    assert "1187712" in statement
    assert "does not bound the number of atoms" in statement
    print("GLOBAL_ATOM_PAIR_CORE_OWNER_FLOOR_AUDIT_PASS floor=1187712")


if __name__ == "__main__":
    main()

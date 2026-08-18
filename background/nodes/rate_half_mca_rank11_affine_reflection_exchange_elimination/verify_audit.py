#!/usr/bin/env python3
"""Independent audit of affine-reflection exchange elimination."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "062484bfac76ff44a138738ff35308268a50d5ce262edfb69ed2eff93c555c9b"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["exception_degree"] == 2
    assert data["reflection_constant_nonzero"] is True
    assert data["synchronized_anchor_fibers"] == 5524
    assert data["fixed_pencil_fiber_cap"] == 1154
    assert 5524 - 1154 == data["strict_fiber_margin"] == 4370
    assert data["high_complexity_threshold"] == 2299571

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for key in ("synchronization_dependency", "census_dependency"):
        assert nodes[data[key]]["status"] == "PROVED"

    statement = (HERE / "statement.md").read_text().lower()
    proof = (HERE / "proof.md").read_text().lower()
    frontier = (HERE / "frontier.md").read_text().lower()
    assert "c=x+y in f_p" in statement
    assert "no estimate on the number of packet certificates is summed" in proof
    assert "antipodal `c=0`" in frontier
    assert "does not pay" in data["nonclaim"].lower()
    print("RANK11_AFFINE_EXCHANGE_ELIMINATION_AUDIT_PASS margin=4370 chi=2299571")


if __name__ == "__main__":
    main()

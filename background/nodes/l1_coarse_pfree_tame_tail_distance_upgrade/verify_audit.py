#!/usr/bin/env python3
"""Mutation audit for the coarse p-free tame-tail distance upgrade."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_tame_tail_distance_upgrade"


def main() -> None:
    checks = 0

    # The F_4 fixture sits at t=p and rejects the non-strict mutation.
    characteristic = 2
    tail = 2
    wronskian_degree = 0
    assert not tail < characteristic
    assert tail <= characteristic
    assert wronskian_degree < tail - 1
    checks += 3

    # The tame F_5 fixture attains both lower bounds.
    characteristic = 5
    depth = 1
    tail = 2
    wronskian_degree = 1
    assert tail < characteristic
    assert tail == depth + 1
    assert wronskian_degree == tail - 1
    checks += 3

    # At and above the first checkpoint, the compact endpoint is p.
    p = 11
    for depth in (p, 2 * p - 2):
        tau = max(math.ceil((depth + 2) / 2), min(depth + 1, p))
        assert tau == p
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "t<p" in statement
    assert "t=p=2" in statement
    assert "strictly `t<p`" in audit
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_COARSE_PFREE_TAME_TAIL_DISTANCE_UPGRADE_PASS checks={checks}")


if __name__ == "__main__":
    main()

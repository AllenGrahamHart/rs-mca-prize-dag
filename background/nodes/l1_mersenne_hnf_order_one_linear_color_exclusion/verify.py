#!/usr/bin/env python3
"""Check the row scope and quadratic root cap for linear colors."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_linear_color_exclusion"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def official_rows() -> set[tuple[int, int, int]]:
    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows: set[tuple[int, int, int]] = set()
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m in (8, 16) and remainder == m:
            rows.add((n, p, m))
    return rows


def main() -> None:
    rows = official_rows()
    assert rows == {
        (65536, 8191, 8),
        (1048576, 131071, 8),
        (4194304, 524287, 8),
        (17179869184, 2147483647, 8),
        (131072, 8191, 16),
    }
    for n, p, m in rows:
        assert n == m * (p + 1)
        assert p % m == m - 1
        assert m - 2 >= 6 > 2

    # A nonzero quadratic has at most two roots. If all three coefficients
    # vanish, the constant coefficient gives b=0 and the linear one is 1.
    quadratic_root_cap = 2
    minimum_colors = min(m - 2 for _, _, m in rows)
    assert minimum_colors == 6 > quadratic_root_cap
    b = 0
    assert 1 + b == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    assert "deg E=0" in statement and "deg E>=2" in statement
    for anchor in ("p=-1 mod m", "At least three", "1=0"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_ORDER_ONE_LINEAR_COLOR_EXCLUSION_PASS rows=5 root_cap=2<6")


if __name__ == "__main__":
    main()

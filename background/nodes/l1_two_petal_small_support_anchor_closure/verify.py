#!/usr/bin/env python3
"""Verify the two-petal automatic B11 anchor inequalities."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_two_petal_small_support_anchor_closure"


def main() -> None:
    checks = 0
    valid = 0

    for ell in range(2, 18):
        for a in range(1, ell + 1):
            for z in range(1, a + 1):
                for r in range(0, ell):
                    for d in range(a, 2 * ell + 1):
                        if r > d:
                            continue
                        if a + z + r < ell + d:
                            continue
                        valid += 1
                        assert ell - r <= z
                        assert ell - a <= z
                        assert d <= ell + z - 1
                        assert (ell - r) + (ell - a) <= 2 * z
                        checks += 4
                        if z == 1:
                            assert r == ell - 1
                            assert d == a
                            assert d in (ell - 1, ell)
                            checks += 3

    assert valid > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "petal_reserve_rich_fiber_reduction",
        "pma_b11_first_match_router",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "d <= ell+A-1",
        "G_R=(ell-r)+(ell-a) <= 2A",
        "r=ell-1",
        "d=a in {ell-1,ell}",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_TWO_PETAL_SMALL_SUPPORT_PASS "
        f"checks={checks} valid_profiles={valid}"
    )


if __name__ == "__main__":
    main()

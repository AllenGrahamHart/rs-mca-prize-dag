#!/usr/bin/env python3
"""Verify the polarized sparse/dense automatic B11 gate."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_polarized_b11_box_closure"


def main() -> None:
    checks = 0
    valid = 0

    for ell in range(2, 13):
        for touched in range(2, 5):
            for sizes in itertools.product(range(1, ell + 1), repeat=touched):
                ordered = sorted(sizes, reverse=True)
                h = sum(ordered)
                p = sum(min(a, ell - a) for a in ordered)
                deficits = sorted(ell - a for a in ordered)
                g2 = deficits[0] + deficits[1]
                for r in range(0, ell):
                    for d in range(max(ordered), 2 * ell + 1):
                        if r > d or h + r < ell + d:
                            continue
                        for cap in range(p, p + 3):
                            valid += 1
                            gr = (ell - r) + deficits[0]
                            assert g2 <= 2 * cap or gr <= cap
                            if ell > cap:
                                dense = [a for a in ordered if 2 * a > ell]
                                assert dense
                                if len(dense) >= 2:
                                    assert g2 <= p <= cap
                                else:
                                    assert gr <= p <= cap
                            checks += 1

    assert valid > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_polarized_petal_entropy_ledger",
        "petal_reserve_rich_fiber_reduction",
        "pma_b11_first_match_router",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_residual_intersection_pin", "req") in edges
    for consumer in (
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "G_2<=2P       or       G_R<=P",
        "p -> infinity       or       d-ell -> infinity",
        "p>P or d>ell+E",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_POLARIZED_B11_BOX_PASS checks={checks} valid={valid}")


if __name__ == "__main__":
    main()

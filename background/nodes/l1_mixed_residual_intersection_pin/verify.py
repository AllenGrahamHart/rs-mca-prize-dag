#!/usr/bin/env python3
"""Verify the L1 mixed-residual intersection contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mixed_residual_intersection_pin"


def main() -> None:
    checks = 0

    # Exhaust the Boolean/arithmetic boundary of the paid union and (I3).
    for ell in range(1, 7):
        for d in range(0, 2 * ell + 4):
            for u_plus_e in range(0, 8):
                for g2 in range(0, 6):
                    for gr in range(0, 6):
                        for e_root in (0, 2, 5):
                            for e_d in (0, 1, 3):
                                for v2, vr in ((0, 0), (2, 1), (4, 3)):
                                    root_paid = u_plus_e <= e_root
                                    anchor_paid = d <= ell + e_d and (
                                        g2 <= v2 or gr <= vr
                                    )
                                    residual = u_plus_e > e_root and (
                                        d > ell + e_d
                                        or (g2 > v2 and gr > vr)
                                    )
                                    assert residual == (not (root_paid or anchor_paid))
                                    checks += 1

    # A fixed c-fiber partition admits a large set with no complete fiber.
    for block_size in range(2, 9):
        for block_count in range(1, 10):
            n = block_size * block_count
            avoidance = block_count * (block_size - 1)
            assert avoidance == n - n // block_size
            assert avoidance < n
            checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_polarized_petal_entropy_ledger",
        "pma_b11_first_match_router",
        "petal_reserve_rich_fiber_reduction",
        "l1_polarized_b11_box_closure",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "petal_mixed_amplification",
        "l1_mixed_petal_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    crosswalk = (
        ROOT / "background" / "nodes" / NODE / "upstream_crosswalk.md"
    ).read_text()
    for anchor in (
        "p+e > E_root",
        "G_2 > V_2 and G_R > V_R",
        "Omega(n/log_2^2 n)",
        "p>P       or       d>ell+E",
    ):
        assert anchor in statement
        checks += 1
    for anchor in ("PR `#977`", "pma_source_paving_bridge", "n-n/c"):
        assert anchor in crosswalk
        checks += 1

    print(f"L1_MIXED_RESIDUAL_INTERSECTION_PASS checks={checks}")


if __name__ == "__main__":
    main()

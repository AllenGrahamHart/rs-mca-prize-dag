#!/usr/bin/env python3
"""Verify the marked common-pencil next-strip boundary fiber bound."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_common_pencil_next_strip_boundary_fiber_bound"


def main() -> None:
    checks = 0
    profiles = 0

    for polarity_cap in range(1, 12):
        for ell in range(2 * polarity_cap + 1, 40):
            for p in range(1, polarity_cap + 1):
                for m in range(1, 10):
                    for gap in range(1, p + 1):
                        d = (m + 1) * ell - gap
                        assert m * ell < d < (m + 1) * ell
                        assert d + p >= (m + 1) * ell

                        lower_t = (d - p + ell) // ell
                        assert lower_t >= m + 1
                        for t in range(lower_t, min(2 * m, lower_t + 3) + 1):
                            for v in range(p + 1):
                                support_degree = t * ell - v
                                freedom = d - support_degree
                                assert freedom <= v - gap
                                if v < gap:
                                    assert support_degree > d
                                else:
                                    assert freedom + 1 <= v - gap + 1 <= p
                                checks += 3
                                profiles += 1

    assert profiles > 10000

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_bounded_polarity_marked_full_pencil_reduction",
        "l1_polarized_petal_entropy_ledger",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_quotient_chart_bounded_core_boundary_closure", "req") in edges
    checks += 1
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "g=(m+1)ell-d",
        "t>=m+1",
        "q^(v-g+1)<=q^p",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_NEXT_STRIP_BOUNDARY_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()


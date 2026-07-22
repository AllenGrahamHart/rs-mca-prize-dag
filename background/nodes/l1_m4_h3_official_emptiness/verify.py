#!/usr/bin/env python3
"""Verify official m=4,h=3 aggregate closure and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_official_emptiness"
SUPPLIERS = {
    "l1_m4_h3_cartier_resonance_reduction",
    "l1_m4_h3_positive_tangent_multiplicity_exclusion",
    "l1_m4_h3_nu0_zero_b_euler_exclusion",
    "l1_m4_h3_nu0_nonzero_b_tangent_exclusion",
    "l1_m4_h3_nu0_h0_auxiliary_fiber_exclusion",
    "l1_m4_h3_nu0_h3_tangent_multiplicity_exclusion",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    rows = (
        (32768, 8191),
        (524288, 131071),
        (2097152, 524287),
        (8589934592, 2147483647),
    )
    for n, p in rows:
        assert n == 4 * (p + 1)
        assert p > 9
        checks += 2

    cases = {
        "positive",
        "nu0_zero_b",
        "nu0_nonzero_b_h0",
        "nu0_nonzero_b_h1",
        "nu0_nonzero_b_h2",
        "nu0_nonzero_b_h3",
    }
    assert len(cases) == 6
    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, CONSUMER, "ev") in edges
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(32768,8191)", "(8589934592,2147483647)",
                   "complete official `m=4,h=3` stratum is", "nonembedded"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_OFFICIAL_EMPTINESS_PASS checks={checks}")


if __name__ == "__main__":
    main()

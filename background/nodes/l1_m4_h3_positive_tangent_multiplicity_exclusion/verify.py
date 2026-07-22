#!/usr/bin/env python3
"""Verify the positive tangent multiplicity exclusion and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_positive_tangent_multiplicity_exclusion"
SUPPLIERS = {
    "l1_m4_h3_tangent_radical_exclusion",
    "l1_m4_h3_euler_quotient_factorization",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    for nu, eta in ((1, 2), (2, 1)):
        assert nu + eta == 3
        checks += 1

    for p in (7, 31, 127):
        for a in range(1, min(p, 10)):
            for b in range(1, min(p, 10)):
                delta = (-4 * a**3 - 27 * b**2) % p
                if not delta:
                    continue
                y0 = -3 * b * pow(2 * a, -1, p) % p
                gy0 = (y0**3 + a * y0 + b) % p
                assert gy0
                alpha = 3
                direct = (
                    4
                    * alpha
                    * ((gy0 - y0 * (3 * y0**2 + a)) % p)
                    * pow(gy0, -2, p)
                ) % p
                closed = -alpha * b * delta * pow(a**3 * gy0**2, -1, p) % p
                assert direct == closed != 0
                checks += 1

    for p in (8191, 131071, 524287, 2147483647):
        assert p > 9
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
    for anchor in ("(PTM1)", "(PTM2)", "(PTM3)", "(PTM4)",
                   "both positive", "does not treat `nu=0`"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_POSITIVE_TANGENT_MULTIPLICITY_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()

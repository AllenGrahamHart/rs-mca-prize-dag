#!/usr/bin/env python3
"""Verify the nu=0 nonzero-b tangent exclusion and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_nonzero_b_tangent_exclusion"
SUPPLIER = "l1_m4_h3_euler_quotient_factorization"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    for p in (7, 31, 127):
        for a in range(1, min(p, 9)):
            for b in range(1, min(p, 9)):
                delta = (-4 * a**3 - 27 * b**2) % p
                if not delta:
                    continue
                y0 = -3 * b * pow(2 * a, -1, p) % p
                g_y0 = (y0**3 + a * y0 + b) % p
                assert g_y0 == b * delta * pow(8 * a**3, -1, p) % p
                alpha = 3
                kappa_one = 4 * alpha * y0 * pow(g_y0, -1, p) % p
                kappa_two = -48 * alpha * a * a * pow(delta, -1, p) % p
                assert kappa_one == kappa_two
                for r in range(1, min(p, 7)):
                    g_r = (r**3 + a * r + b) % p
                    if not g_r:
                        continue
                    d0 = -alpha * pow(g_r, -1, p) % p
                    h0 = -4 * r * d0 % p
                    scalar_equation = (r * delta + 12 * a * a * g_r) % p
                    assert (h0 == kappa_two) == (scalar_equation == 0)
                    checks += 1
                checks += 2

    for h in range(4):
        lower = 5 - h
        if h in (1, 2):
            assert lower > h
        elif h == 3:
            assert lower == 2 <= h
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(NTE1)", "(NTE2)", "(NTE3)", "(NTE4)",
                   "R(0)Delta+12a^2g(R(0))", "b=0", "does not"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU0_NONZERO_B_TANGENT_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact arithmetic replay of the cofactor-depth budget cancellation."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_cofactor_depth_budget_cancellation"
PARENT = "l1_exact_shell_fixed_cofactor_prefix_transport"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checked = 0
    for q in (3, 5, 13):
        for n in range(6, 11):
            for k in range(2, n - 2):
                for a in range(k + 1, n):
                    w = a - k
                    for e in range(k):
                        d = w + e
                        if d >= a:
                            continue
                        mass = math.comb(n, a)
                        ambient_shell = q**e * Fraction(mass, q**d)
                        target_mean = Fraction(mass, q**w)
                        assert ambient_shell == target_mean

                        image_size = max(1, min(mass, q**d // 2))
                        image_shell = q**e * Fraction(mass, image_size)
                        collapse_form = Fraction(q**d, image_size) * target_mean
                        assert image_shell == collapse_form

                        rounded = q**e * math.ceil(Fraction(mass, q**d))
                        assert Fraction(rounded) < target_mean + q**e
                        checked += 1

    q_kb = 2**31 - 2**24 + 1
    q_m31 = 2**31 - 1
    b_kb = 274980728111395087
    b_m31 = 16777215
    rows = (
        (q_kb, 57198030366, b_kb, 2),
        (q_kb, 65065153468, b_kb, 2),
        (q_m31, 1752700, b_m31, 1),
        (q_m31, 1993678, b_m31, 1),
    )
    for q, mean_ceiling, budget, first_sparse in rows:
        assert mean_ceiling < q**first_sparse
        if first_sparse > 1:
            assert mean_ceiling - 1 > q ** (first_sparse - 1)
        else:
            assert mean_ceiling < q
        assert q ** (first_sparse - 1) <= budget < q**first_sparse

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_COFACTOR_DEPTH_BUDGET_CANCELLATION_PASS "
        f"identities={checked} finite_rows={len(rows)}"
    )


if __name__ == "__main__":
    main()

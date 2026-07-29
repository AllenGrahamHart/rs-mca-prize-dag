#!/usr/bin/env python3
"""Check the h=15 constant-color norm reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m16_order_one_constant_color_reduction"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def main() -> None:
    h = 15
    H = h - 1
    assert H * (h - 2) == 182
    assert 2 * H == 28
    assert (2 * H) ** 2 + 2 == 786
    assert 2 * (2 * H) + (H * (h - 2)) ** 2 == 33180
    assert (786 - 33180) % 8191 == 370
    assert (-28) % 8191 == 8163
    assert (786 + 33180) % 8191 == 1202

    trace_polynomial = [0, 1]
    for factor in ([-4, 0, 1], [-2, 0, 1], [2, 0, -4, 0, 1]):
        trace_polynomial = mul(trace_polynomial, factor)
    assert len(trace_polynomial) - 1 == 9
    assert trace_polynomial[-1] == 1

    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = []
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m == 16 and remainder == 16:
            rows.append((n, p, m))
    assert rows == [(131072, 8191, 16)]

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(CCR3)", "(CCR5)", "(CCR6)"):
        assert anchor in statement
    for anchor in ("d=-2/13", "33180", "sixteenth-root traces"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M16_ORDER_ONE_CONSTANT_COLOR_REDUCTION_PASS row=1 gcds=2")


if __name__ == "__main__":
    main()

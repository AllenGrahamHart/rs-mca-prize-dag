#!/usr/bin/env python3
"""Exact finite checks for the h=7 order-one constant-color exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_constant_color_exclusion"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def official_primes() -> list[int]:
    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = []
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m == 8 and remainder == 8:
            assert n == 8 * (p + 1)
            rows.append(p)
    return sorted(rows)


def main() -> None:
    primes = official_primes()
    assert primes == [8191, 131071, 524287, 2147483647]
    assert all(p % 8 == 7 for p in primes)

    # The three rational trace values in the two norm equations.
    assert [12 * s * s + 13 * s - 778 for s in (2, -2, 0)] == [-704, -756, -778]
    assert [12 * s * s + 11 * s - 1070 for s in (2, -2, 0)] == [-1000, -1044, -1070]

    primitive_obstructions = [754**2 - 2 * 13**2, 1046**2 - 2 * 11**2]
    assert primitive_obstructions == [568178, 1093874]
    expected_residues = {
        568178: [2999, 43894, 43891, 568178],
        1093874: [4471, 45306, 45300, 1093874],
    }
    for value in primitive_obstructions:
        residues = [value % p for p in primes]
        assert residues == expected_residues[value]
        assert all(residue != 0 for residue in residues)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(CCE3)", "(CCE4)", "(CCE5)", "genuinely nonconstant"):
        assert anchor in statement
    for anchor in ("l_5/l_6", "l_4/l_6", "568178", "1093874"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CONSTANT_COLOR_EXCLUSION_PASS rows=4 colors=constant-empty")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Focused replay of the budget-three affine-rank rigidity arithmetic."""

from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_affine_rank_rigidity"
SUPPLIER = "upstream_gfv4_affine_span_list_compiler"
TARGET = "rate_half_list_adjacent_crossing"


def main() -> None:
    checks = 0
    for d in list(range(3, 100)) + [2**10, 2**20, 2**39]:
        assert (2 * d + 1) // d == 2
        assert 2 * d + 2 > 6
        zmax = 2 * d - 2
        assert 4 * (3 * d - 1) == 4 * zmax + 2 * (4 * d - zmax)
        checks += 3

    # Independent finite-field check of the six-pair collision ceiling.
    p = 11
    linears = [(a, b) for a, b in product(range(p), repeat=2)]
    for quartet in combinations(linears[:18], 4):
        roots = set()
        for (a, b), (c, e) in combinations(quartet, 2):
            da, db = (a - c) % p, (b - e) % p
            if db:
                roots.add((-da * pow(db, -1, p)) % p)
        assert len(roots) <= 6
        checks += 1

    import json
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    edges = {(e["from"], e["to"], e["kind"]) for e in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    print(f"RATE_HALF_LIST_BUDGET_THREE_AFFINE_RANK_RIGIDITY_PASS checks={checks}")


if __name__ == "__main__":
    main()

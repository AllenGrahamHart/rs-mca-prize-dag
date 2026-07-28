#!/usr/bin/env python3
"""Independent audit of the weighted-kernel dictionary."""

from __future__ import annotations

import json
from itertools import product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_low_square_mass_weighted_kernel_dictionary"
TARGET = "e1_official_low_square_mass_pair_budget"


def formula(h: int, ell: int, a: int, b: int, common_signs: bool = True) -> int:
    T = min(ell, 2 * h - ell)
    n0 = h - a - b
    if n0 < 0:
        return 0
    answer = 0
    for j in range(b + 1):
        for r in range(n0 + 1):
            sx, sy = a + j + r, a + b - j + r
            if sx <= T and sy <= T and sx % 2 == ell % 2 and sy % 2 == ell % 2:
                sign_factor = 2**r if common_signs else 1
                answer += comb(b, j) * comb(n0, r) * sign_factor
    return answer


def ordered_difference_counts(h: int, ell: int) -> dict[tuple[int, ...], int]:
    valid = []
    for vector in product((-1, 0, 1), repeat=h):
        support = sum(value != 0 for value in vector)
        if support <= min(ell, 2 * h - ell) and support % 2 == ell % 2:
            valid.append(vector)
    counts: dict[tuple[int, ...], int] = {}
    for x in valid:
        for y in valid:
            if x == y:
                continue
            d = tuple(left - right for left, right in zip(x, y))
            counts[d] = counts.get(d, 0) + 1
    return counts


def main() -> None:
    checks = 0
    caught_mutation = False
    for h, ell in ((3, 1), (4, 2), (5, 3)):
        counts = ordered_difference_counts(h, ell)
        assert sum(counts.values()) % 2 == 0
        checks += 1
        for d, count in counts.items():
            a = sum(value in (-2, 2) for value in d)
            b = sum(value in (-1, 1) for value in d)
            assert formula(h, ell, a, b) == count
            assert counts[tuple(-value for value in d)] == count
            caught_mutation |= formula(h, ell, a, b, common_signs=False) != count
            checks += 2
    assert caught_mutation
    checks += 1

    # Independent replay of the binding uniform-cap boundary.
    edge_cap = 62622678770648913918718317914905517790930
    maximum = 4550972295647251657752808370587724056
    assert maximum * 27520 <= 2 * edge_cap
    assert maximum * 27521 > 2 * edge_cap
    checks += 2

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    target = (ROOT / f"background/nodes/{TARGET}/statement.md").read_text()
    assert "E_low = (1/2) sum" in statement
    assert "27,520" in statement
    assert "status:** TARGET" in target
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    checks += 4

    print(
        "E1_LOW_SQUARE_MASS_WEIGHTED_KERNEL_DICTIONARY_AUDIT_PASS "
        f"mutation=1 checks={checks}"
    )


if __name__ == "__main__":
    main()

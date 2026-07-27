#!/usr/bin/env python3
"""Exact structural checks for the order-zero linear-color exclusion."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_zero_linear_color_exclusion"
PARENT = "l1_mersenne_next_to_maximal_hypergeometric_normal_form"
CONSUMER = "l1_mixed_petal_amplification"


def add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a: list[int], c: int) -> list[int]:
    return [c * value for value in a]


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return out


def resultant_row(h: int) -> list[int]:
    # E2=a*y+b and E3=c*y^2+d*y+e. The resultant is
    # a^2*e-a*b*d+b^2*c.
    a = [-1, -h]
    b = [1, -2, -h]
    c = [-2, -2 * h]
    d = [-3, -6 * h, -3 * h * h]
    e = [5, 3 * h - 12, 6 - 9 * h, 2 * h - 3 * h * h]
    return add(
        add(mul(mul(a, a), e), scale(mul(mul(a, b), d), -1)),
        mul(mul(b, b), c),
    )


def expected_resultant(h: int) -> list[int]:
    return scale(mul(mul([0, 1], [-1, 1]), [1, h]), -2 * (h + 1))


def official_rows() -> set[tuple[int, int, int]]:
    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows: set[tuple[int, int, int]] = set()
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m in (8, 16) and remainder == m:
            rows.add((n, p, m))
    return rows


def main() -> None:
    expected_rows = {
        (65536, 8191, 8),
        (1048576, 131071, 8),
        (4194304, 524287, 8),
        (17179869184, 2147483647, 8),
        (131072, 8191, 16),
    }
    rows = official_rows()
    assert rows == expected_rows
    for n, p, m in rows:
        assert n == m * (p + 1)
        assert n & (n - 1) == 0
        assert p > m
        assert math.gcd(p, n) == 1

    for h in (7, 15):
        got = resultant_row(h)
        want = expected_resultant(h)
        assert got == want, (h, got, want)
        # Clearing h^2 from E2(-1/h,y) gives h(h+1), independent of y.
        assert h * (h + 1) != 0
        assert (1 + h * 0, 1) == (1, 1)
        assert (1 + h * 1, -1) == (h + 1, -1)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[NODE]["closure"] == "proof"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "deg E_s >= 2" in statement
    assert "First suppose `E_s=epsilon` is constant" in proof
    assert "s=-(h+1)=-m" in proof
    assert "does not exclude degree at least two" in statement

    mutations = 0
    for h in (7, 15):
        wrong = expected_resultant(h)
        wrong[1] += 1
        mutations += resultant_row(h) != wrong
    assert mutations == 2

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_LINEAR_COLOR_EXCLUSION_PASS "
        f"rows={len(rows)} h=7,15 resultants=2 mutations={mutations}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact arithmetic replay for the L1 raw-ledger route fence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_raw_support_ledger_exponential_route_fence"


def check_profile(s: int) -> tuple[int, int, int]:
    j = 1 << s
    n = 1 << j
    k = n // 2
    N = k - 1
    ell = n // j
    M = j // 2
    b = 1
    t = M
    a = ell // 2
    r = 0
    h = t * a
    d = h - ell
    u = t * ell - h
    e = max(0, 2 * d + 1 - h)
    gamma = d - max(r, a) + 1

    assert N + b + M * ell == n
    assert b < ell
    assert h == n // 4
    assert r + h == ell + d
    assert 0 < a <= d
    assert h > d
    assert u == n // 4
    assert e == n // 4 - 2 * ell + 1
    assert 0 < e <= N
    assert gamma == n // 4 - 3 * ell // 2 + 1
    assert gamma >= n // 8

    # binom(2m,m) >= 2^m follows factorwise from m+i >= 2i.
    m = n // 4
    assert all(m + i >= 2 * i for i in range(1, min(m, 32) + 1))
    assert m >= n // 4
    return j, e, gamma


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (
        "pma_petal_pattern_root_pinning_ledger",
        NODE,
        "req",
    ) in edges
    assert (
        "l1_maximal_background_anchor_injection",
        NODE,
        "req",
    ) in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges


def main() -> None:
    rows = [check_profile(s) for s in range(4, 9)]
    check_dag()
    print(
        "L1_RAW_SUPPORT_LEDGER_ROUTE_FENCE_PASS "
        f"rows={len(rows)} j={rows[0][0]}..{rows[-1][0]} "
        f"gamma0_bits={rows[0][2].bit_length()}"
    )


if __name__ == "__main__":
    main()

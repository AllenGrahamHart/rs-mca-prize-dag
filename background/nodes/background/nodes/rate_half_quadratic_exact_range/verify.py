#!/usr/bin/env python3
"""Exact boundary replay for the rate-half quadratic range."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
N = 1 << 41
K = 1 << 40
SCALE = 1 << 128


def margin(k: int, r: int) -> int:
    n = 2 * k
    return (n - r) ** 2 - n * (k + r)


def cutoff_radius(k: int) -> int:
    return 3 * k - isqrt(7 * k * k) - 1


def main() -> None:
    r_q = cutoff_radius(K)
    b_q = r_q + 1
    q_exclusive = (b_q + 1) * SCALE

    assert r_q == 389_500_552_608
    assert b_q == 389_500_552_609
    assert q_exclusive == 132_540_169_959_144_315_698_788_704_090_115_531_231_543_332_700_160

    square = 7 * K * K
    root_floor = isqrt(square)
    assert root_floor * root_floor < square < (root_floor + 1) ** 2
    assert margin(K, r_q) == 5_154_112_775_168 > 0
    assert margin(K, r_q + 1) == -663_955_886_271 < 0
    assert (q_exclusive - 1) // SCALE == b_q
    assert q_exclusive // SCALE == b_q + 1

    a_fixed = N - r_q
    assert a_fixed == 1_809_522_702_944
    for b in (1, b_q, b_q + 1, (1 << 39) + 1, K - 1):
        r_safe = min(b - 1, r_q)
        assert 0 <= r_safe <= r_q
        assert margin(K, r_safe) >= 0
        assert r_safe + 1 <= b
        assert N - b + 1 <= N - r_safe

    # At the last CA-only block the lower candidate is exactly half-distance.
    b_ca_only = (1 << 39) + 1
    assert b_ca_only - 1 == (N - K) // 2
    assert b_ca_only <= K - 1

    # Exhaust the cutoff identity at small rate-half dimensions.
    for k in range(1, 257):
        predicted = cutoff_radius(k)
        admissible = [r for r in range(k) if margin(k, r) >= 0]
        assert predicted == max(admissible)
        assert margin(k, predicted) >= 0
        if predicted + 1 < k:
            assert margin(k, predicted + 1) < 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_quadratic_exact_range"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "mca_quadratic_prize_rows",
        "rate_half_quadratic_exact_range",
        "req",
    ) in edges
    assert (
        "rate_half_mca_sparse_layer_reduction",
        "rate_half_quadratic_exact_range",
        "req",
    ) in edges
    assert (
        "rate_half_sparse_pinning_rigidity",
        "rate_half_quadratic_exact_range",
        "req",
    ) in edges
    assert (
        "rate_half_quadratic_exact_range",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_QUADRATIC_EXACT_RANGE_PASS "
        f"r_q={r_q} b_q={b_q} q_exclusive={q_exclusive}"
    )


if __name__ == "__main__":
    main()

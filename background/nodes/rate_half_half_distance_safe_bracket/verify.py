#!/usr/bin/env python3
"""Exact arithmetic audit for the rate-half half-distance bracket."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    n, k = 1 << 41, 1 << 40
    r = (n - k) // 2
    agreement = n - r
    q = 1 << 169
    budget = q // (1 << 128)

    assert 2 * r == n - k
    assert agreement == 3 * n // 4
    assert budget == n
    assert n <= budget
    assert ((1 << 169) - 1) // (1 << 128) == n - 1
    assert k + 8_594_128_896 < agreement

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_half_distance_safe_bracket"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "mca_from_ca_reduction",
        "rate_half_half_distance_safe_bracket",
        "req",
    ) in edges
    assert (
        "rate_half_half_distance_safe_bracket",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_HALF_DISTANCE_SAFE_BRACKET_PASS "
        f"agreement={agreement} radius={r} budget={budget}"
    )


if __name__ == "__main__":
    main()

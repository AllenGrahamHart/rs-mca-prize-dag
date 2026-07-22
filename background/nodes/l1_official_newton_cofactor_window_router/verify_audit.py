#!/usr/bin/env python3
"""Mutation audit for the official Newton cofactor-window router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_newton_cofactor_window_router"


def powers_from_elementary(values: list[int], prime: int) -> list[int]:
    powers = [0]
    for j in range(1, len(values)):
        value = 0
        for i in range(1, j):
            sign = 1 if i % 2 == 1 else -1
            value += sign * values[i] * powers[j - i]
        value += (1 if j % 2 == 1 else -1) * j * values[j]
        powers.append(value % prime)
    return powers


def main() -> None:
    checks = 0

    # Relaxing the cap by one bit admits the p=257 order-32 boundary.
    q = 257**32
    assert (q - 1) % (1 << 13) == 0
    assert 1 << 256 < q < 1 << 257
    checks += 2

    # Relaxing the minimum domain by one octave admits p=127.
    q = 127**32
    assert (q - 1) % (1 << 12) == 0
    assert q < 1 << 256
    checks += 2

    # At depth d=p, Newton loses the e_p coordinate. Two formal elementary
    # vectors have the same first p power sums but different e_p.
    prime = 5
    first = [1, 0, 0, 0, 0, 0]
    second = [1, 0, 0, 0, 0, 1]
    assert powers_from_elementary(first, prime) == powers_from_elementary(second, prime)
    assert first != second
    checks += 2

    # The next excess layer reaches depth p at the conservative boundary.
    p = 3583
    ell = p - 3174
    assert ell - 1 + 3174 == p - 1
    assert ell - 1 + 3175 == p
    checks += 2

    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "strict `d<p` is required" in audit
    assert "F2 summit is not a requirement" in audit
    assert "No computation or probabilistic evidence is load-bearing" in audit
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f2_growing_order_myerson"]["status"] == "TARGET"
    assert ("f2_growing_order_myerson", NODE, "req") not in edges
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 4

    print(f"AUDIT_L1_OFFICIAL_NEWTON_COFACTOR_WINDOW_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()

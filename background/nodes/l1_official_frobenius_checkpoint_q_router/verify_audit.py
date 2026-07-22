#!/usr/bin/env python3
"""Mutation audit for the official Frobenius-checkpoint Q router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_frobenius_checkpoint_q_router"


def p_free_powers(elementary: list[int], prime: int) -> tuple[int, ...]:
    powers = [0]
    kept = []
    for j in range(1, len(elementary)):
        value = 0
        for i in range(1, j):
            value += (1 if i % 2 else -1) * elementary[i] * powers[j - i]
        value += (1 if j % 2 else -1) * j * elementary[j]
        powers.append(value % prime)
        if j % prime:
            kept.append(powers[j])
    return tuple(kept)


def main() -> None:
    checks = 0

    # Omitting E_p loses injectivity.
    prime = 5
    first = [1, 0, 0, 0, 0, 0]
    second = [1, 0, 0, 0, 0, 1]
    assert p_free_powers(first, prime) == p_free_powers(second, prime)
    assert first != second
    checks += 2

    # Every multiple needs its own checkpoint; E_(2p) is not recovered from
    # the first checkpoint and the p-free sums through depth 2p.
    prime = 3
    first = [1] + [0] * 6
    second = first.copy()
    second[6] = 1
    assert first[3] == second[3]
    assert p_free_powers(first, prime) == p_free_powers(second, prime)
    assert first != second
    checks += 3

    # The integer consequence p>n/24 permits 23 checkpoints but not a
    # universal 22-checkpoint conclusion without more arithmetic.
    p = 101
    n = 24 * p - 1
    depth = n - 1
    assert p > n / 24
    assert depth // p == 23
    checks += 2

    # The cap/minimum-size argument pays exponent 453 but not 452.
    assert 256 * 23 < 13 * 453
    assert not (256 * 23 < 13 * 452)
    checks += 2

    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    assert "Fib_mix(s,c) subset Fib_free(s)" in statement
    assert "q^r M<=q/2^128" in statement
    assert "preserves only a qualitative polynomial statement" in statement
    assert "F2 summit remains TARGET" in audit
    assert "No computation or probabilistic evidence is load-bearing" in audit
    checks += 5

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f2_growing_order_myerson"]["status"] == "TARGET"
    assert ("f2_growing_order_myerson", NODE, "req") not in edges
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 4

    print(f"AUDIT_L1_OFFICIAL_FROBENIUS_CHECKPOINT_Q_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()

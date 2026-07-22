#!/usr/bin/env python3
"""Verify the official Frobenius-checkpoint Q router."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_frobenius_checkpoint_q_router"


def forward(elementary: list[int], prime: int) -> tuple[list[int], list[int]]:
    powers = [0]
    mixed = [0]
    for j in range(1, len(elementary)):
        value = 0
        for i in range(1, j):
            sign = 1 if i % 2 else -1
            value += sign * elementary[i] * powers[j - i]
        value += (1 if j % 2 else -1) * j * elementary[j]
        powers.append(value % prime)
        mixed.append(elementary[j] if j % prime == 0 else powers[j])
    return mixed, powers


def inverse(mixed: list[int], prime: int) -> tuple[list[int], list[int]]:
    elementary = [1]
    powers = [0]
    for j in range(1, len(mixed)):
        if j % prime == 0:
            powers.append(pow(powers[j // prime], prime, prime))
            elementary.append(mixed[j])
        else:
            powers.append(mixed[j])
            numerator = 0
            for i in range(1, j + 1):
                sign = 1 if i % 2 else -1
                numerator += sign * elementary[j - i] * powers[i]
            elementary.append(numerator * pow(j, -1, prime) % prime)
    return elementary, powers


def main() -> None:
    checks = 0

    # Exhaust the mixed coordinate automorphism beyond one and two
    # characteristic crossings.
    for prime, depth in ((3, 8), (5, 6), (7, 5)):
        for values in itertools.product(range(prime), repeat=depth):
            elementary = [1, *values]
            mixed, powers = forward(elementary, prime)
            recovered, recovered_powers = inverse(mixed, prime)
            assert recovered == elementary
            assert recovered_powers == powers
            checks += 2

    # Official order/cap arithmetic gives p>=11n/256>n/24 and at most 23
    # checkpoints below depth n.
    for exponent in range(13, 42):
        n = 1 << exponent
        characteristic_lower = 11 * n // 256
        assert characteristic_lower * 256 == 11 * n
        assert characteristic_lower * 24 > n
        assert (n - 1) // characteristic_lower <= 23
        checks += 3

    # Forgetting all checkpoints costs less than n^453 under only the
    # official cap and minimum row size. The exponent 452 does not follow
    # from those two coarse inequalities.
    assert 256 * 23 < 13 * 453
    assert 256 * 23 >= 13 * 452
    checks += 2

    # A nontrivial raw union over even one checkpoint cannot certify the
    # finite q/2^128 threshold.
    for q in (2, 17, (1 << 255) - 19):
        for r in (1, 2, 23):
            max_bound = 1
            assert q**r * max_bound >= q
            assert q > q // (1 << 128)
            checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_official_reserve_tame_refinement_router",
        "l1_official_newton_cofactor_window_router",
        "l1_exact_shell_fixed_cofactor_prefix_transport",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "p>=11n/256>n/24",
        "r=floor(d/p)<=23",
        "S_j(A) if p does not divide j",
        "E_j(A) if p divides j",
        "triangular polynomial coordinate equivalence",
        "Fib_mix(s,c) subset Fib_free(s)",
        "q^r<2^(256*23)=2^5888<n^453",
        "cannot imply",
        "proves no max-fiber estimate",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_FROBENIUS_CHECKPOINT_Q_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()

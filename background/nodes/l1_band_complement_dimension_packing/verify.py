#!/usr/bin/env python3
"""Exact replay of complement packing for a small Reed-Solomon shell."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_band_complement_dimension_packing"
PARENT = "l1_exact_shell_balanced_shifted_lattice_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def main() -> None:
    p = 7
    H = tuple(range(6))
    n = len(H)
    k = 2
    m = 3
    omega = n - m
    w = m - k
    s = omega - w
    assert 2 * m <= n + k - 1 and s == n - 2 * m + k == 2

    # Two prescribed exact codewords, with the full degree-one code enumerated.
    received = (0, 0, 0, 4, 5, 6)
    exact_supports: dict[tuple[int, ...], tuple[int, ...]] = {}
    for coefficients in itertools.product(range(p), repeat=k):
        agreement = tuple(
            x for x, value in zip(H, received)
            if evaluate(coefficients, x, p) == value
        )
        if len(agreement) == m:
            complement = tuple(x for x in H if x not in agreement)
            exact_supports[coefficients] = complement
    assert len(exact_supports) >= 2

    complements = list(exact_supports.values())
    for i, left in enumerate(complements):
        for right in complements[i + 1 :]:
            assert len(set(left).intersection(right)) <= s - 1
    bound = math.comb(n, s) // math.comb(omega, s)
    assert len(exact_supports) <= bound

    product_checks = 0
    for N in range(8, 31):
        for O in range((N + 1) // 2, N + 1):
            for dimension in range(1, O // 2 + 1):
                ratio = math.comb(N, dimension) / math.comb(O, dimension)
                assert ratio <= (2 * N / O) ** dimension
                product_checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_BAND_COMPLEMENT_DIMENSION_PACKING_PASS "
        f"exact={len(exact_supports)} s={s} bound={bound} "
        f"product_checks={product_checks}"
    )


if __name__ == "__main__":
    main()

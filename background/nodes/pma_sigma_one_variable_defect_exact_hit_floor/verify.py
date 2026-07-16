#!/usr/bin/env python3
"""Verify the variable-defect sigma-one exact-hit floor."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "pma_sigma_one_variable_defect_exact_hit_floor"


def falling(x: int, length: int) -> int:
    out = 1
    for j in range(length):
        out *= x - j
    return out


def main() -> None:
    n = 65536
    k = n // 2
    K = k - 1
    L = n - k
    M = L // 2
    d = n // 8
    a = d + 2
    q = 65537**2
    s_n = n // (32 * 16)
    hyperplanes = comb(L, 2) + L + d + 1

    assert 1 <= d <= M - 2
    assert d <= k // 2 - s_n - 3
    assert q > 2 * hyperplanes
    assert q - 1 - a > 2 * (M - a)
    assert k - (k // 2 + a) > s_n

    numerator = (
        comb(K, d)
        * q**d
        * (q - hyperplanes)
        * 2**a
        * comb(M, a)
        * (q - 1 - a - 2 * (M - a))
    )
    denominator = falling(q - 1, a) * (q - 1 - a)
    floor_mean = numerator // denominator

    assert comb(K, d) >= 3**d
    assert 2**a * comb(M, a) >= 3**a
    assert 4 * q * numerator >= 3 ** (d + a) * denominator
    assert floor_mean > n**3000

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, "petal_mixed_amplification", "ev") in edges
    assert (NODE, "imgfib", "ev") in edges

    # Mutation controls: the support and unused-label off-by-one errors both
    # materially change the certified object.
    assert (K - d) + (a - 1) == k
    wrong_denominator = falling(q - 1, a) * (q - a)
    assert wrong_denominator != denominator

    print(
        "PMA_VARIABLE_DEFECT_FLOOR_PASS "
        f"mean_bits={floor_mean.bit_length()} "
        f"n3000_bits={(n**3000).bit_length()} "
        f"hyperplanes={hyperplanes} d={d} a={a} mutations=2"
    )


if __name__ == "__main__":
    main()

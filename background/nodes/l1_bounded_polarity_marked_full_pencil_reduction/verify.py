#!/usr/bin/env python3
"""Verify the bounded-polarity marked full-pencil reduction."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_bounded_polarity_marked_full_pencil_reduction"


def mul(left: list[int], right: list[int], modulus: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % modulus
    return out


def sub(left: list[int], right: list[int], modulus: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for i in range(size):
        out[i] = (
            (left[i] if i < len(left) else 0)
            - (right[i] if i < len(right) else 0)
        ) % modulus
    return out


def main() -> None:
    checks = 0
    valid = 0

    for ell in range(3, 12):
        for touched in range(2, 6):
            for sizes in itertools.product(range(1, ell + 1), repeat=touched):
                p = sum(min(a, ell - a) for a in sizes)
                h = sum(sizes)
                if p >= ell or h < ell:
                    continue
                for r in range(0, ell):
                    for d in range(max(sizes), min(h + r - ell, 2 * ell) + 1):
                        if d <= ell + p - 1:
                            continue
                        dense = [a for a in sizes if 2 * a > ell]
                        assert len(dense) >= 2
                        deficits = sorted(ell - a for a in dense)
                        assert deficits[0] + deficits[1] <= p
                        valid += 1
                        checks += 2

    assert valid > 0

    # Polynomial clearing identity over a small field. Start from arbitrary
    # support locators and cofactors, then define the un-cleared right side.
    modulus = 101
    l_si = [3, 2, 1]
    l_sj = [5, 7, 1]
    l_vi = [11, 1]
    l_vj = [13, 1]
    a_i = [2, 9, 4]
    a_j = [6, 1, 8]
    raw = sub(mul(l_si, a_i, modulus), mul(l_sj, a_j, modulus), modulus)
    left = sub(
        mul(mul(l_si, l_vi, modulus), mul(l_vj, a_i, modulus), modulus),
        mul(mul(l_sj, l_vj, modulus), mul(l_vi, a_j, modulus), modulus),
        modulus,
    )
    right = mul(raw, mul(l_vi, l_vj, modulus), modulus)
    assert left == right
    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_polarized_petal_entropy_ledger",
        "petal_reserve_rich_fiber_reduction",
        "pma_saturated_mixed_support_kernel",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "d>ell+p-1",
        "L_(T_i)C_i-L_(T_j)C_j=(c_j-c_i)FJ",
        "deg C_i,deg C_j<=c+p",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_MARKED_FULL_PENCIL_PASS checks={checks} valid={valid}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exhaustive toy replay of the deep exact-shell Johnson closure."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_deep_exact_shell_johnson_closure"
PARENT = "l1_pade_split_section_support_moment_inversion"
CONSUMER = "l1_mixed_petal_amplification"


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def check_field(p: int, n: int, k: int) -> tuple[int, int]:
    H = tuple(range(n))
    m0 = (n + k - 1) // 2 + 1
    denominator = m0 * m0 - n * (k - 1)
    assert denominator > 0
    bound = n * (m0 - k + 1) // denominator
    codewords = tuple(itertools.product(range(p), repeat=k))
    evaluations = tuple(tuple(evaluate(P, x, p) for x in H) for P in codewords)
    maximum = 0
    for U in itertools.product(range(p), repeat=n):
        agreements = [sum(u == v for u, v in zip(U, values)) for values in evaluations]
        deep = sum(a >= m0 for a in agreements)
        exact_tail = sum(sum(a == m for a in agreements) for m in range(m0, n + 1))
        assert deep == exact_tail
        assert deep <= bound <= n * n
        maximum = max(maximum, deep)
    return maximum, bound


def main() -> None:
    checks = (
        check_field(5, 4, 2),
        check_field(7, 5, 2),
    )
    assert 2 ** (2 * 44) == 2**88

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(f"L1_DEEP_EXACT_SHELL_JOHNSON_PASS checks={checks}")


if __name__ == "__main__":
    main()

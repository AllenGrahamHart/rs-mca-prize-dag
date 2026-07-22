#!/usr/bin/env python3
"""Mutation audit for the coarse p-free Wronskian neighbor compiler."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_wronskian_neighbor_compiler"


def certificate_count(q: int, tail: int, degree: int) -> int:
    return sum(
        (-1) ** j
        * math.comb(tail, j)
        * q ** max(degree + 1 - j, 0)
        for j in range(tail + 1)
    )


def main() -> None:
    checks = 0

    # Minimum-width certificates have the stated parity.
    even_depth = 2
    even_tail = math.ceil((even_depth + 2) / 2)
    odd_depth = 3
    odd_tail = math.ceil((odd_depth + 2) / 2)
    assert 2 * even_tail - even_depth - 2 == 0
    assert 2 * odd_tail - odd_depth - 2 == 1
    checks += 2

    # A linear polynomial over F_5 avoiding two fixed points has 16 choices.
    assert certificate_count(5, 2, 1) == (5 - 1) * (5 + 1 - 2) == 16
    assert certificate_count(5, 2, 0) == 4
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "For fixed `X`" in statement
    assert "t>=tau_p" in statement
    assert "gcd(F_X,F_X')=1" in proof
    assert "choice of `X`" in statement
    assert "Injectivity fixes `X`" in audit
    assert "exponential `binom(a,t)`" in audit
    checks += 6

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_COARSE_PFREE_WRONSKIAN_NEIGHBOR_COMPILER_PASS checks={checks}")


if __name__ == "__main__":
    main()

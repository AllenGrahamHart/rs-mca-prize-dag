#!/usr/bin/env python3
"""Mutation audit for the official coarse p-free entropy reserve."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_coarse_pfree_entropy_reserve"


def bits(gap: int, checkpoint_cap: int, field_bits: int = 13) -> int:
    return (field_bits - 4) * gap - field_bits * checkpoint_cap


def main() -> None:
    checks = 0

    assert bits(3175, 23) == 28276
    assert bits(3174, 23) < 28276  # lose the d_0=ell_0-1 off-by-one
    assert bits(3175, 24) < 28276  # allow one extra checkpoint
    assert bits(3175, 23, 12) < 28276  # weaken q>2^13 to q>2^12
    checks += 4

    mutated_rate = Fraction(1, 32)
    assert (1 - mutated_rate) / mutated_rate == 31
    assert 31 > 15
    checks += 2

    assert 28276 - 128 == 28148
    assert 28149 - 28276 > -128  # one extra inflation bit misses the target
    checks += 2

    p = 3583
    d0 = 408
    d = p
    r = 1
    delta = d - d0
    endpoint_15 = -18 * delta + 22 * r + 15 * (d - r)
    endpoint_16 = -18 * delta + 22 * r + 16 * (d - r)
    assert endpoint_15 == -3398
    assert endpoint_15 < -106
    assert endpoint_16 == 184
    assert endpoint_16 > -106
    checks += 4

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "ambient target" in statement
    assert "does not prove `(CER6)`" in statement
    assert "not normalized by the attained image" in audit
    assert "Fifteen bits force extras emptiness; sixteen" in audit
    assert "numerically compatible" in audit
    assert "target, map, structured subtraction" in audit
    assert "Positive-cofactor Pade graphs still require" in audit
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_OFFICIAL_COARSE_PFREE_ENTROPY_RESERVE_PASS checks={checks}")


if __name__ == "__main__":
    main()

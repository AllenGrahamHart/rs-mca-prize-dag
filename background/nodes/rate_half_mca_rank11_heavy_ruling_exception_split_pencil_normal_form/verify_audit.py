#!/usr/bin/env python3
"""Independent audit of the exception split-pencil normal form."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "0abba81a802b3ef46b0c7a59144f05ffa1b6c3af8b5dfd20346848fdeea00711"


def value(poly: list[int], x: int, p: int) -> int:
    return sum(coefficient * pow(x, degree, p) for degree, coefficient in enumerate(poly)) % p


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["minimum_anchor_slopes"] == data["minimum_split_fibers"] == 20
    assert 1 == data["exception_degree_minimum"]
    assert data["exception_degree_maximum"] == data["pair_core_margin"] == 11
    assert data["maximum_scalar_zero_anchor_slopes"] == 0
    assert data["pencil_gcd_degree"] == data["denominator_anchor_core_gcd_degree"] == 0

    toy = data["toy"]
    p, u, v = toy["field"], toy["u"], toy["v"]
    all_roots: list[int] = []
    for gamma, expected in zip(toy["slopes"], toy["root_sets"]):
        fiber = [0] * max(len(u), len(v))
        for i in range(len(fiber)):
            fiber[i] = (
                (u[i] if i < len(u) else 0)
                + gamma * (v[i] if i < len(v) else 0)
            ) % p
        roots = [x for x in range(p) if value(fiber, x, p) == 0]
        assert roots == expected
        all_roots.extend(roots)
    assert len(all_roots) == len(set(all_roots)) == 6
    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "unique polynomials `u,v`" in proof
    assert "scalar cannot vanish at an anchor" in proof
    assert "does not assert whole-domain root-freeness" in Path(__file__).with_name("audit.md").read_text().lower()
    print(
        "RANK11_EXCEPTION_SPLIT_PENCIL_AUDIT_PASS "
        f"anchors={data['minimum_anchor_slopes']} degree_range=1..11 toy_roots={len(all_roots)}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent audit of the dihedral exception-SPI fence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "3daaf19044cb9003355121fa416fa45354415c6ff1a4ac669cba7251c01c15c1"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    n = data["official_domain_order"]
    assert n == 1 << data["official_domain_exponent"]
    counts = [n // (2 * d) for d in data["quotient_degrees"]]
    assert [2 * d for d in data["quotient_degrees"]] == data["pencil_degrees"]
    assert counts == data["fiber_counts"]
    assert min(counts) == 262144 > data["minimum_required_fibers"]

    toy = data["toy"]
    p, order, d = toy["field"], toy["domain_order"], toy["quotient_degree"]
    h = pow(toy["primitive_field_generator"], (p - 1) // order, p)
    points = [pow(h, i, p) for i in range(order)]
    quotient = sorted({pow(x, d, p) for x in points})
    a = pow(h, d, p)
    pairs = {
        tuple(sorted((z, a * pow(z, -1, p) % p)))
        for z in quotient
    }
    assert len(pairs) == toy["expected_fiber_count"] == 4
    assert all(left != right for left, right in pairs)
    slopes = {-(left + right) % p for left, right in pairs}
    assert len(slopes) == len(pairs)
    roots_by_slope = []
    for gamma in slopes:
        roots = {
            x
            for x in points
            if (pow(x, 2 * d, p) + gamma * pow(x, d, p) + a) % p == 0
        }
        assert len(roots) == toy["expected_fiber_size"] == 8
        roots_by_slope.append(roots)
    assert sum(len(roots) for roots in roots_by_slope) == order
    assert len(set().union(*roots_by_slope)) == order

    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "(z-w)(zw-a)=0" in proof
    statement = Path(__file__).with_name("statement.md").read_text().lower()
    assert "not an actual mca counterexample" in statement
    print(
        "RANK11_EXCEPTION_SPI_DIHEDRAL_FENCE_AUDIT_PASS "
        f"official_min={min(counts)} toy_partition={order}"
    )


if __name__ == "__main__":
    main()

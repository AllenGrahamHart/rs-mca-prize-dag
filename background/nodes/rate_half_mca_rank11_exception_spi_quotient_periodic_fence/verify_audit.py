#!/usr/bin/env python3
"""Independent audit of the quotient-periodic exception-SPI fence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "01c960dee395b776edef296f31b799234b4c480f478a7cbb2adb4b8e6711218e"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    order = data["official_domain_order"]
    assert order == 1 << data["official_domain_exponent"]
    recomputed = []
    for degree in data["supported_degrees"]:
        assert degree & (degree - 1) == 0
        assert order % degree == 0
        recomputed.append(order // degree)
    assert recomputed == data["fiber_counts"]
    assert min(recomputed) == 262144 > data["minimum_required_fibers"]

    toy = data["toy"]
    p, n, e = toy["field"], toy["domain_order"], toy["degree"]
    h = pow(toy["primitive_field_generator"], (p - 1) // n, p)
    fibers: dict[int, list[int]] = {}
    for i in range(n):
        x = pow(h, i, p)
        fibers.setdefault(pow(x, e, p), []).append(x)
    assert len(fibers) == n // e == 8
    assert sorted(len(points) for points in fibers.values()) == [e] * (n // e)
    flattened = [x for points in fibers.values() for x in points]
    assert len(flattened) == len(set(flattened)) == n
    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "homomorphism" in proof
    assert "not actual" not in proof
    statement = Path(__file__).with_name("statement.md").read_text().lower()
    assert "not an actual mca counterexample" in statement
    print(
        "RANK11_EXCEPTION_SPI_PERIODIC_FENCE_AUDIT_PASS "
        f"official_min={min(recomputed)} toy_partition={len(flattened)}"
    )


if __name__ == "__main__":
    main()

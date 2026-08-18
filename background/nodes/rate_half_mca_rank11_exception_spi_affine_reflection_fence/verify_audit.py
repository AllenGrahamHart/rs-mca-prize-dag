#!/usr/bin/env python3
"""Independent audit of the affine-reflection exception-SPI fence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "373f3d0292a9d6dc0d0ad10cf7deef900e23a606cb77b9cd16fcd98a7500c12b"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    p = data["official_base_prime"]
    n = data["official_domain_order"]
    assert p - 1 == 127 * 2**24
    assert n == 2**21
    q, r = divmod(n * (n - 1), p - 1)
    assert q == 2064 and r > 0
    assert q + 1 == data["forced_reflection_points"]
    assert q // 2 == data["forced_quadratic_fibers"] == 1032

    toy = data["toy"]
    tp, order, c = toy["field"], toy["domain_order"], toy["reflection_constant"]
    h = pow(toy["primitive_field_generator"], (tp - 1) // order, tp)
    domain = [pow(h, i, tp) for i in range(order)]
    domain_set = set(domain)
    points = sorted(x for x in domain if (c - x) % tp in domain_set)
    assert len(points) == 12
    used: set[int] = set()
    products: set[int] = set()
    fibers = 0
    for x in points:
        if x in used:
            continue
        y = (c - x) % tp
        assert y != x and y in domain_set
        used.update((x, y))
        products.add(x * y % tp)
        fibers += 1
    assert used == set(points)
    assert fibers == len(products) == toy["quadratic_fibers"] == 6

    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "sum_(c in f_p) r_c=n^2" in proof
    statement = Path(__file__).with_name("statement.md").read_text().lower()
    assert "not an actual unsafe mca" in statement
    print(
        "RANK11_EXCEPTION_SPI_AFFINE_REFLECTION_AUDIT_PASS "
        f"official_fibers={q // 2} toy_fibers={fibers}"
    )


if __name__ == "__main__":
    main()

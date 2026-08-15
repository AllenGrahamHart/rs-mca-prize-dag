#!/usr/bin/env python3
"""Independent split enumeration for the projective-basis cap."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    n, m = p["domain_size"], p["support_size"]
    maximum = -1
    maximizers = []
    for q in range(2, m):
        r = m - q
        bound = comb(q, 3) + comb(r + 1, 3)
        if bound > maximum:
            maximum, maximizers = bound, [q]
        elif bound == maximum:
            maximizers.append(q)
    require(maximum == comb(m - 1, 3), "split maximum")
    require(maximizers == [2, m - 1], "split maximizers")
    bases = m * (m - 1) * (m - 2) - 6 * maximum
    cap, remainder = divmod(n * (n - 1) * (n - 2), bases)
    require(maximum == p["maximum_collinear_unordered_triples"], "collinear triples")
    require(bases == p["minimum_independent_ordered_triples_per_record"], "bases")
    require(cap == p["projective_basis_record_cap"], "record cap")
    require(remainder == p["division_remainder"], "remainder")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_BASIS_CAP_AUDIT_PASS "
        f"splits_checked={m - 2} cap={cap} remainder={remainder}"
    )


if __name__ == "__main__":
    main()

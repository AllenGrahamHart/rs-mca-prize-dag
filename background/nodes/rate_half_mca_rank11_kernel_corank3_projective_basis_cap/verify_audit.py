#!/usr/bin/env python3
"""Independent plane-split enumeration for the corank-three cap."""

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
    for q in range(3, m):
        r = m - q
        bound = (
            comb(q, 4)
            + (q // 2) * comb(r, 2)
            + 2 * comb(r, 3)
            + comb(r, 4)
        )
        if bound > maximum:
            maximum, maximizers = bound, [q]
        elif bound == maximum:
            maximizers.append(q)
    require(maximum == comb(m - 1, 4), "split maximum")
    require(maximizers == [3, m - 1], "split maximizers")
    bases = m * (m - 1) * (m - 2) * (m - 3) - 24 * maximum
    cap, remainder = divmod(n * (n - 1) * (n - 2) * (n - 3), bases)
    require(maximum == p["maximum_coplanar_unordered_quadruples"], "coplanar quadruples")
    require(bases == p["minimum_independent_ordered_quadruples_per_record"], "bases")
    require(cap == p["projective_basis_record_cap"], "record cap")
    require(remainder == p["division_remainder"], "remainder")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_BASIS_CAP_AUDIT_PASS "
        f"splits_checked={m - 3} cap={cap} remainder={remainder}"
    )


if __name__ == "__main__":
    main()

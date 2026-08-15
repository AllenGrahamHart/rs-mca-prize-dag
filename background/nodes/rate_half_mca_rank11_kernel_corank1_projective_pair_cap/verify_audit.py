#!/usr/bin/env python3
"""Independent concentration audit of the projective-pair cap."""

from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    n, m = p["domain_size"], p["support_size"]
    global_maximum = -1
    maximizer = None
    for classes in range(2, m + 1):
        concentrated = (m - classes + 1) ** 2 + classes - 1
        if concentrated > global_maximum:
            global_maximum = concentrated
            maximizer = classes
    require(maximizer == 2, "class-count maximizer")
    require(global_maximum == (m - 1) ** 2 + 1, "concentration value")
    independent = m * m - global_maximum
    cap, remainder = divmod(n * (n - 1), independent)
    require(independent == p["minimum_independent_ordered_pairs_per_record"], "independent pairs")
    require(cap == p["projective_pair_record_cap"], "record cap")
    require(remainder == p["division_remainder"], "remainder")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK1_PROJECTIVE_PAIR_CAP_AUDIT_PASS "
        f"classes_checked={m - 1} cap={cap} remainder={remainder}"
    )


if __name__ == "__main__":
    main()

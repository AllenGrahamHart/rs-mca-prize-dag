#!/usr/bin/env python3
"""Independent partition audit of the rank-two quotient pair floor."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def maximum_dependent_pairs(kprime: int, loops: int) -> int:
    remaining = 67472 + kprime - 9
    nonloops = remaining - loops
    class_cap = kprime - 10 - loops
    full_classes, remainder = divmod(nonloops, class_cap)
    maximum_square_sum = full_classes * class_cap * class_cap + remainder * remainder
    independent = (nonloops * nonloops - maximum_square_sum) // 2
    return comb(remaining, 2) - independent


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    pair_floor = p["independent_pair_floor"]
    rows = 0
    for kprime in (11, 11773, 15446, 15670, 15671, 17609, 22525):
        unrestricted = comb(67472 + kprime - 9, 2)
        candidates = [maximum_dependent_pairs(kprime, loops) for loops in range(kprime - 10)]
        require(max(candidates) == unrestricted - pair_floor, f"sharp cap K={kprime}")
        require(candidates.index(max(candidates)) == kprime - 11, f"maximal closure K={kprime}")
        rows += len(candidates)
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_EXTENSION_DEFICIT_AUDIT_PASS "
        f"rows={rows} pair_floor={pair_floor}"
    )


if __name__ == "__main__":
    main()

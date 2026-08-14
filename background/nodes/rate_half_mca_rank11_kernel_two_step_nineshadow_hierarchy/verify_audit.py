#!/usr/bin/env python3
"""Independent closure-size and coloop audit of the hierarchy."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    rows = json.loads(CONTRACT.read_text())["parameters"]["couplings"]
    closure_checks = 0
    coloop_checks = 0
    for d, _, outside_floor, partner_floor, pair_floor, coloop_cap, multiplicity in rows:
        for kprime in (d + 11, 101, 17609, 18102):
            mprime = 67472 + kprime
            for closure_size in range(0, kprime - d + 1):
                outside = mprime - closure_size
                parallel_cap = kprime - d + 1 - closure_size
                ordered = outside * (outside - parallel_cap)
                require(ordered // 2 >= pair_floor, f"pair count d={d} K={kprime} c={closure_size}")
                closure_checks += 1
        target_rank = 12 - d
        require(coloop_cap == target_rank - 1, f"coloop rank d={d}")
        for coloops in range(target_rank):
            require(comb(coloops, 2) <= multiplicity, f"coloop pairs d={d}")
            coloop_checks += 1
        require((outside_floor, partner_floor) == (67472 + d, 67471 + d), f"printed floors d={d}")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_HIERARCHY_AUDIT_PASS "
        f"closure_checks={closure_checks} coloop_checks={coloop_checks}"
    )


if __name__ == "__main__":
    main()

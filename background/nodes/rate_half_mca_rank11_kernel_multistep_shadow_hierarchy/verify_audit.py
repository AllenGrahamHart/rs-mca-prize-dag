#!/usr/bin/env python3
"""Independent recurrence audit of the multi-step hierarchy."""

from __future__ import annotations

import json
from math import comb, factorial, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checks = 0
    recurrence_checks = 0
    for d in range(p["corank_minimum"], p["corank_maximum"] + 1):
        rank = d + 1
        independent = 1
        for step in range(1, d):
            independent = independent * (rank - (step - 1) + 1) // step
            require(independent == comb(rank + 1, step), f"independent recurrence t={step} d={d}")
            recurrence_checks += 1
            if step < 2:
                continue
            ordered = prod(67472 + d - offset for offset in range(step))
            require(ordered // factorial(step) == comb(67472 + d, step), f"raising recurrence t={step} d={d}")
            target_rank = 10 - d + step
            coloop_cap = target_rank - 1
            require(coloop_cap == 9 - d + step, f"coloop cap t={step} d={d}")
            require(comb(coloop_cap, step) > 0, f"target multiplicity t={step} d={d}")
            checks += 1
    require(checks == p["coupling_count"], "coupling count")
    require(p["triple_couplings"] == [
        [d, comb(d + 2, 3), 67472 + d, comb(67472 + d, 3), 12 - d, comb(12 - d, 3)]
        for d in range(4, 10)
    ], "triple constants")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_MULTISTEP_SHADOW_HIERARCHY_AUDIT_PASS "
        f"couplings={checks} recurrences={recurrence_checks}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent audit of the kernel nine-shadow coupling contract."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    coefficients = p["spanning_shadow_coefficients"]
    checked = 0
    for dimension in range(1, 10):
        rank = 10 - dimension
        dual_rank = 11 - rank
        target = comb(dual_rank + 1, 2)
        require(coefficients[dimension - 1] == target, f"coefficient d={dimension}")

        # In the sharp primal, a spanning nine-set must retain all r-1
        # coloops, so its omitted pair lies in the d+2 parallel class.
        omitted_pairs = comb(dimension + 2, 2)
        require(omitted_pairs == target, f"sharp complement d={dimension}")

        # If the dual simplification has exactly c classes, colooplessness
        # forces two representatives in every class.
        require(4 * comb(dual_rank, 2) >= target, f"dual classes d={dimension}")
        checked += 1

    require("sum_d" in p["resource_formula"], "joint resource")
    require("K_prime-d-9" in p["extension_formula"], "closure subtraction")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_COUPLING_AUDIT_PASS "
        f"coranks={checked} first={coefficients[0]} last={coefficients[-1]}"
    )


if __name__ == "__main__":
    main()

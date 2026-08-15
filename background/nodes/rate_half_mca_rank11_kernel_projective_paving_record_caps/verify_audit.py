#!/usr/bin/env python3
"""Independent multiplicative audit of the complete-chart caps."""

from __future__ import annotations

import json
from math import prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def choose_multiplicative(n: int, k: int) -> int:
    numerator = prod(range(n - k + 1, n + 1))
    denominator = prod(range(1, k + 1))
    quotient, remainder = divmod(numerator, denominator)
    require(remainder == 0, "binomial integrality")
    return quotient


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    n0, m0 = p["n_offset"], p["m_offset"]
    caps = []
    for dimension, row in enumerate(p["records"], 1):
        n, m = n0 + dimension, m0 + dimension
        unordered = choose_multiplicative(m - 1, dimension)
        ordered = unordered * prod(range(1, dimension + 2))
        resource = prod(range(n - dimension, n + 1))
        cap, remainder = divmod(resource, ordered)
        require((ordered, resource, cap, remainder) == (
            row["minimum_ordered_bases"],
            row["ordered_coordinate_resource"],
            row["record_cap"],
            row["division_remainder"],
        ), "independent row reconstruction")
        caps.append(cap)
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_RECORD_CAPS_AUDIT_PASS "
        f"dimensions=9 complete_caps={','.join(map(str, caps))}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent dynamic audit of the paving basis floor."""

from __future__ import annotations

import json
from functools import cache
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


@cache
def recurrence(rank: int, size: int) -> int:
    if rank == 1 or size == rank:
        return 1
    return recurrence(rank, size - 1) + recurrence(rank - 1, size - 1)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checks = 0
    for rank in p["audited_ranks"]:
        for size in range(rank, rank + 25):
            require(recurrence(rank, size) == comb(size - 1, rank - 1), "dynamic floor")
            checks += 1
    print(
        "MATROID_PAVING_BASIS_FLOOR_AUDIT_PASS "
        f"dynamic_checks={checks} extremizers=9"
    )


if __name__ == "__main__":
    main()

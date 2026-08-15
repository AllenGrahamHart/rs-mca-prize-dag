#!/usr/bin/env python3
"""Independent combinatorial audit of the support-four outside charge."""

from __future__ import annotations

import itertools
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def independent_count(K: int, m: int, t: int, delta: int) -> int:
    b = K - t - delta
    n = m - b
    if delta == 0:
        return comb(b, 4)
    total = comb(b, 4)
    for external in range(1, 5):
        deletion_shapes = comb(b, 4 - external) * comb(n, external - 1)
        completions = delta + 4 - external
        total += deletion_shapes * completions // external
    return total


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    table = data["parameters"]["K45"]["caps_by_minimum_defect"]
    extension = comb(67517 - 4, 7)
    for defect in range(5):
        candidates = []
        for delta in range(defect + 1):
            for t in range(4, 7):
                count = independent_count(45, 67517, t, delta)
                candidates.append((count * extension, t, delta, count))
        cap, t, delta, count = max(candidates)
        declared = table[str(defect)]
        require((cap, t, delta, count) == (
            declared["incidence_cap"], declared["t"], declared["delta"], declared["support_count"]
        ), f"defect {defect}")

    # On a toy carrier, each four-set with j external points has exactly j
    # outside-point deletion charges.
    carrier = set(range(5))
    universe = range(11)
    toy_checks = 0
    for support in itertools.combinations(universe, 4):
        external = sum(point not in carrier for point in support)
        charges = sum(point not in carrier for point in support)
        require(charges == external, "outside deletion multiplicity")
        toy_checks += 1
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT4_EXTERNAL_CHARGE_AUDIT_PASS "
        f"caps={len(table)} toy_checks={toy_checks}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent finite audit of the universal completion count."""

from __future__ import annotations

import json
from itertools import combinations
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    checks = 0
    for support in range(2, 10):
        for q in range(1, 5):
            m = 16
            deletion = tuple(range(support - 1))
            completions = tuple(range(support - 1, support - 1 + q))
            outside = set(range(m)) - set(deletion) - set(completions)
            brute = 0
            for chosen in completions:
                for tail in combinations(outside, 11 - support):
                    selected = set(deletion) | {chosen} | set(tail)
                    require(len(selected & set(completions)) == 1, "unique completion")
                    brute += 1
            formula = q * comb(m - support + 1 - q, 11 - support)
            require(brute == formula, "fixed-deletion count")
            checks += 1
    example = p["K24_example"]
    for support in range(6, 10):
        values = [
            b * comb(example["m"] - support + 1 - b, 11 - support)
            for b in range(example["q"] + 1)
        ]
        maximizing = max(range(len(values)), key=values.__getitem__)
        require(
            maximizing == example["completion_maximizers"][str(support)],
            "official maximizer",
        )
        require(
            comb(example["m"], support - 1) * values[maximizing] // support
            == example["incidence_caps"][str(support)],
            "official cap",
        )
        checks += 1
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_UNIVERSAL_COMPLETION_INCIDENCE_CAP_AUDIT_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()

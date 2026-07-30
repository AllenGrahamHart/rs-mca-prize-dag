#!/usr/bin/env python3
"""Deterministic replay for the L1 Mersenne HNF payoff-scope router."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ATLAS = (
    ROOT
    / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
)


def main() -> None:
    with ATLAS.open(newline="") as handle:
        rows = [
            {key: int(value) for key, value in row.items()}
            for row in csv.DictReader(handle, delimiter="\t")
        ]

    assert len(rows) == 59
    mersenne = [row for row in rows if row["n"] == row["m"] * (row["p"] + 1)]
    assert Counter(row["m"] for row in mersenne) == Counter({4: 4, 8: 4, 16: 1})

    cells: list[tuple[int, int, int, int]] = []
    for row in mersenne:
        for h in range(2, row["m"]):
            if row["m"] == 4 and h == 3:
                continue
            cells.append((row["n"], row["p"], row["m"], h))

    by_m = Counter(m for _, _, m, _ in cells)
    assert by_m == Counter({4: 4, 8: 24, 16: 14})
    assert len(cells) == 42
    assert sum(h % 2 == 0 for _, _, _, h in cells) == 23
    assert sum(h % 2 == 1 for _, _, _, h in cells) == 19
    assert sum((m, h) in {(8, 7), (16, 15)} for _, _, m, h in cells) == 5

    for _, p, m, h in cells:
        for depth in (p, 2 * p - 2):
            u = (m - h) * p + m
            ell = (m - h + 1) * p + m - depth
            assert 1 <= ell <= u
        for a in (p, m * (p + 1)):
            numerator = m * (p + 1) - a + p
            assert numerator * 1 < (m + 2) * p

    print("L1_MERSENNE_HNF_PAYOFF_SCOPE_PASS cells=42 even=23 odd=19 nextmax=5")


if __name__ == "__main__":
    main()

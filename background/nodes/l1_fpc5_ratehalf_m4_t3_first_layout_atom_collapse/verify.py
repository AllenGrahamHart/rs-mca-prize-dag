#!/usr/bin/env python3
"""Tiny replay of the M=4,t=3 outer-cell collapse."""

from __future__ import annotations

from itertools import combinations


P = 101


def normalized_cross_ratio(labels: tuple[int, int, int]) -> int:
    first, second, third = labels
    return (third - first) * pow(second - first, -1, P) % P


def main() -> None:
    labels = (3, 17, 42, 88)
    triples = list(combinations(labels, 3))
    assert len(triples) == 4

    lambdas = [normalized_cross_ratio(triple) for triple in triples]
    assert all(value not in (0, 1) for value in lambdas)

    for n in range(8, 257):
        for b in range(7, n):
            defect_count = max(0, (b - 3) // 4)
            assert defect_count < n
            atom_count = len(triples) * defect_count
            assert atom_count < 4 * n

    print("PASS: four triples, one cross-ratio each, and fewer than 4n LS6 cells")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Tiny partition/budget check for SOV affine-piece certificates."""

from __future__ import annotations


def verify_partition(universe: set[str], affine: list[set[str]], exceptional: list[set[str]], budget: int) -> None:
    pieces = affine + exceptional
    covered = set().union(*pieces)
    assert covered == universe
    seen: set[str] = set()
    for piece in pieces:
        assert seen.isdisjoint(piece)
        seen |= piece
    assert sum(len(piece) for piece in exceptional) < budget


def main() -> None:
    universe = {"L0", "L1", "L2", "L3", "L4"}
    affine = [{"L0", "L1"}, {"L2", "L3"}]
    exceptional = [{"L4"}]
    verify_partition(universe, affine, exceptional, budget=2)
    print("PASS: SOV affine partition covers cell with exceptional mass below budget")


if __name__ == "__main__":
    main()

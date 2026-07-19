#!/usr/bin/env python3
"""Conditional assembly of the h=3 repeat-boundary star theorem."""

from __future__ import annotations

from dataclasses import dataclass


OFFICIAL_MIN_N = 2**13
OFFICIAL_MAX_N = 2**41


@dataclass(frozen=True)
class Implication:
    premises: frozenset[str]
    conclusion: str


GATES = frozenset(
    (
        "H3-VALUE-INJECTIVE",
        "H3-SLOPE-RATIO-HIT",
        "LOOSE-GEN-RANK/NV",
        "LOOSE-A-RANK/NV",
        "LOOSE-B-RANK/NV",
    )
)

IMPLICATIONS = (
    Implication(
        frozenset(("H3-VALUE-INJECTIVE", "H3-SLOPE-RATIO-HIT")),
        "H3-NO-DISJOINT-EDGES",
    ),
    Implication(
        frozenset(("LOOSE-GEN-RANK/NV", "LOOSE-A-RANK/NV", "LOOSE-B-RANK/NV")),
        "H3-NO-LOOSE-TRIANGLE",
    ),
    Implication(
        frozenset(("H3-NO-LOOSE-TRIANGLE",)),
        "H3-NO-PAIRWISE-CORELESS",
    ),
    Implication(
        frozenset(("H3-NO-DISJOINT-EDGES", "H3-NO-PAIRWISE-CORELESS")),
        "H3-STAR-OBSTRUCTION",
    ),
    Implication(frozenset(("H3-STAR-OBSTRUCTION",)), "tau_coord<=1"),
    Implication(frozenset(("tau_coord<=1",)), "repeat_residue<=90n^2"),
)


def closure(known: frozenset[str]) -> frozenset[str]:
    result = set(known)
    changed = True
    while changed:
        changed = False
        for implication in IMPLICATIONS:
            if implication.conclusion in result:
                continue
            if implication.premises <= result:
                result.add(implication.conclusion)
                changed = True
    return frozenset(result)


def residue_bound(tau: int, n: int) -> int:
    return (72 * tau + 18) * n * n


def main() -> None:
    print("h=3 repeat star conditional assembly")
    print("open gates:")
    for gate in sorted(GATES):
        print(f"  {gate}")
    result = closure(GATES)
    required = {
        "H3-NO-DISJOINT-EDGES",
        "H3-NO-LOOSE-TRIANGLE",
        "H3-NO-PAIRWISE-CORELESS",
        "H3-STAR-OBSTRUCTION",
        "tau_coord<=1",
        "repeat_residue<=90n^2",
    }
    if not required <= result:
        raise AssertionError((required - result, result))
    print("derived:")
    for item in sorted(required):
        print(f"  {item}")

    official_ns = [2**s for s in range(13, 42)]
    bad = [n for n in official_ns if residue_bound(1, n) >= n**3]
    if bad:
        raise AssertionError(("official repeat-residue payment failed", bad[:5]))
    print(
        f"repeat_residue <= 90n^2 is below n^3 for official n="
        f"2^13..2^41; first_bound={residue_bound(1, OFFICIAL_MIN_N)}"
    )
    print("H3_REPEAT_STAR_CONDITIONAL_ASSEMBLY_PASS")


if __name__ == "__main__":
    main()

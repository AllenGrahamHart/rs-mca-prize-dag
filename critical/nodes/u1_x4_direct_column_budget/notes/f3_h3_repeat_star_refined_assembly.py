#!/usr/bin/env python3
"""Refined branch-level assembly of the h=3 repeat-boundary star route."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_repeat_loose_secondary_payment import total_secondary_bound
from f3_h3_repeat_same_lambda_scale_count import scale_collision_pair_bound
from f3_h3_repeat_star_conditional_assembly import OFFICIAL_MIN_N, residue_bound


@dataclass(frozen=True)
class Implication:
    premises: frozenset[str]
    conclusion: str


STRICT_BRANCH_GATES = frozenset(
    (
        "H3-VALUE-GEN-INJECTIVE",
        "H3-VALUE-SCALE-INJECTIVE",
        "H3-SLOPE-GG-HIT",
        "H3-SLOPE-MIXED-HIT",
        "LOOSE-GEN-RANK/NV",
        "LOOSE-A-RANK/NV",
        "LOOSE-B-RANK/NV",
    )
)


IMPLICATIONS = (
    Implication(
        frozenset(("H3-VALUE-GEN-INJECTIVE", "H3-VALUE-SCALE-INJECTIVE")),
        "H3-VALUE-INJECTIVE",
    ),
    Implication(
        frozenset(("H3-SLOPE-GG-HIT", "H3-SLOPE-MIXED-HIT")),
        "H3-SLOPE-RATIO-HIT",
    ),
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


def main() -> None:
    print("h=3 repeat star refined assembly")
    print("strict primitive gates:")
    for gate in sorted(STRICT_BRANCH_GATES):
        print(f"  {gate}")
    result = closure(STRICT_BRANCH_GATES)
    required = {
        "H3-VALUE-INJECTIVE",
        "H3-SLOPE-RATIO-HIT",
        "H3-NO-DISJOINT-EDGES",
        "H3-NO-LOOSE-TRIANGLE",
        "H3-NO-PAIRWISE-CORELESS",
        "H3-STAR-OBSTRUCTION",
        "tau_coord<=1",
        "repeat_residue<=90n^2",
    }
    if not required <= result:
        raise AssertionError((required - result, result))
    print("strict derived:")
    for item in sorted(required):
        print(f"  {item}")

    official_ns = [2**s for s in range(13, 42)]
    bad_repeat = [n for n in official_ns if residue_bound(1, n) >= n**3]
    if bad_repeat:
        raise AssertionError(("strict repeat-residue payment failed", bad_repeat[:5]))

    scale_bad = [n for n in official_ns if scale_collision_pair_bound(n) >= n * n]
    secondary_bad = [n for n in official_ns if total_secondary_bound(n) >= n * n]
    if scale_bad or secondary_bad:
        raise AssertionError((scale_bad[:5], secondary_bad[:5]))
    print(
        "paid ledgers kept separate from strict tau route: "
        f"scale_pairs(first_official)={scale_collision_pair_bound(OFFICIAL_MIN_N)}, "
        f"loose_secondary(first_official)={total_secondary_bound(OFFICIAL_MIN_N)}"
    )
    print(
        f"strict repeat_residue <= 90n^2 is below n^3 for official n=2^13..2^41; "
        f"first_bound={residue_bound(1, OFFICIAL_MIN_N)}"
    )
    print("H3_REPEAT_STAR_REFINED_ASSEMBLY_PASS")


if __name__ == "__main__":
    main()

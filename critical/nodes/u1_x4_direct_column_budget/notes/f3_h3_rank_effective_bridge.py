#!/usr/bin/env python3
"""Rank-effective bridge arithmetic for the h=3 RC-RANK interface."""

from __future__ import annotations


C_RED = 13
A = 5
D = 1
CONDITIONS_PER_CURVE = C_RED * D * (A + D)


PINNED_RANKS = {
    "constant-ratio collapsed": 50,
    "private-divisor rational": 293,
    "shifted polynomial": 247,
    "shared denominator": 247,
    "repaired random full-rank": 320,
}

EXPECTED_CAPACITIES = {
    "constant-ratio collapsed": 0,
    "private-divisor rational": 3,
    "shifted polynomial": 3,
    "shared denominator": 3,
    "repaired random full-rank": 4,
}


def rank_capacity(rank: int, conditions_per_curve: int = CONDITIONS_PER_CURVE) -> int:
    """Maximum multiplicity m for which rank > m*conditions_per_curve."""

    if rank <= conditions_per_curve:
        return 0
    return (rank - 1) // conditions_per_curve


def rc_rank_for_capacity(rank: int, multiplicity: int) -> bool:
    return rank > multiplicity * CONDITIONS_PER_CURVE


def main() -> None:
    print("h=3 rank-effective bridge compiler")
    print(f"conditions_per_curve={CONDITIONS_PER_CURVE}")
    print("source                         rank  capacity")
    for name, rank in PINNED_RANKS.items():
        cap = rank_capacity(rank)
        if cap != EXPECTED_CAPACITIES[name]:
            raise AssertionError((name, rank, cap, EXPECTED_CAPACITIES[name]))
        if cap > 0 and not rc_rank_for_capacity(rank, cap):
            raise AssertionError((name, rank, cap, "capacity should pass"))
        if rc_rank_for_capacity(rank, cap + 1):
            raise AssertionError((name, rank, cap, "capacity not maximal"))
        print(f"{name:30s} {rank:5d} {cap:9d}")

    # The duplicate rows from the rank-stress packet are the capacity rule in action.
    private_rank = PINNED_RANKS["private-divisor rational"]
    if not rc_rank_for_capacity(private_rank, 2):
        raise AssertionError("private duplicate pair should pass")
    if rc_rank_for_capacity(private_rank, 4):
        raise AssertionError("private duplicate quadruple should fail")

    # A family bridge that only controls raw list length is too weak; it must
    # control the sum of per-image rank capacities consumed by activated shapes.
    print("private duplicate pair passes; private duplicate quadruple fails")
    print("bridge contract must bound rank-capacity units, not raw curve multiplicity")
    print("H3_RANK_EFFECTIVE_BRIDGE_PASS")


if __name__ == "__main__":
    main()

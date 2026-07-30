#!/usr/bin/env python3
"""Independent degree-15 two-subset action audit."""

from itertools import combinations, permutations

POINTS = tuple(range(6))
PAIRS = tuple(combinations(POINTS,2))
BASE = (0,1)

def parity(permutation: tuple[int,...]) -> int:
    return sum(permutation[i] > permutation[j] for i in POINTS for j in range(i+1,6)) % 2

def act(permutation: tuple[int,...], pair: tuple[int,int]) -> tuple[int,int]:
    return tuple(sorted((permutation[pair[0]],permutation[pair[1]])))

def subdegrees(group: list[tuple[int,...]]) -> list[int]:
    stabilizer = [g for g in group if act(g,BASE) == BASE]
    unseen = set(PAIRS)
    lengths = []
    while unseen:
        pair = min(unseen)
        orbit = {act(g,pair) for g in stabilizer}
        unseen -= orbit
        lengths.append(len(orbit))
    return sorted(lengths)

def cycle_lengths(permutation: tuple[int,...]) -> list[int]:
    unseen = set(PAIRS)
    lengths = []
    while unseen:
        start = min(unseen)
        orbit = set()
        point = start
        while point not in orbit:
            orbit.add(point)
            point = act(permutation,point)
        unseen -= orbit
        lengths.append(len(orbit))
    return sorted(lengths)

def main() -> None:
    s6 = list(permutations(POINTS))
    a6 = [g for g in s6 if parity(g) == 0]
    assert len(PAIRS) == 15
    assert len(a6) == 360 and len(s6) == 720
    assert subdegrees(a6) == [1,6,8]
    assert subdegrees(s6) == [1,6,8]
    five_cycle = (1,2,3,4,0,5)
    assert parity(five_cycle) == 0
    assert cycle_lengths(five_cycle) == [5,5,5]
    print("RATE_HALF_KB_M4_OUTER_A6S6_ROUTE_CUT_AUDIT_PASS")

if __name__ == "__main__":
    main()

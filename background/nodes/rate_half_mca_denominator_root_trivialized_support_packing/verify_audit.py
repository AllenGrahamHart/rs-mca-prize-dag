#!/usr/bin/env python3
from itertools import combinations
from math import comb


universe = range(8)
M = 4
k = 2
supports = [set(s) for s in combinations(universe, M)]

# Greedily construct a family whose pairwise intersections are below k.
family = []
for support in supports:
    if all(len(support & other) < k for other in family):
        family.append(support)

shadows = []
for support in family:
    shadow = {tuple(s) for s in combinations(sorted(support), k)}
    assert all(shadow.isdisjoint(previous) for previous in shadows)
    shadows.append(shadow)

assert len(family) * comb(M, k) <= comb(8, k)
assert len(family) > 1

print(f"PASS independent shadow-disjointness audit family={len(family)}")

#!/usr/bin/env python3
"""Reconcile maelcar #1147's T_sm against OUR banked H4 collision census.

Our record (critical/nodes/u1_x4_direct_column_budget/notes/F3_IDENTIFICATION.md:21):
    (32,4,97): 792 = 2 x 396
i.e. 792 ORDERED / 396 UNORDERED disjoint 4-subset pairs of mu_32 in F_97
with matching power sums p1,p2,p3.

Their #1147 row: (n,p,T_sm,max K) = (32,97,9,2).

Question: are we counting the same universe? Their T_sm should equal our 396
after (a) imposing their smoothness predicate and (b) quotienting by the
cyclic shift action of order n.
"""
from collections import defaultdict
from itertools import combinations

n, p = 32, 97


def root_of_order(p, n):
    for c in range(2, p):
        z = pow(c, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            return z
    raise AssertionError


zeta = root_of_order(p, n)
roots = [pow(zeta, e, p) for e in range(n)]


def elementary(v):
    e1 = sum(v) % p
    e2 = sum(v[i] * v[j] for i in range(4) for j in range(i + 1, 4)) % p
    e3 = sum(v[i] * v[j] * v[k] for i in range(4)
             for j in range(i + 1, 4) for k in range(j + 1, 4)) % p
    return e1, e2, e3


def smooth(key):
    e1, e2, e3 = key
    m = e1 * pow(4, -1, p) % p
    sigma = (6 * m * m - e2) * pow(2, -1, p) % p
    rho = (e3 - 4 * m**3 + 4 * m * sigma) * pow(8, -1, p) % p
    return rho != 0 and (sigma**3 - 27 * rho**2) % p != 0


def canon(a, b):
    ims = []
    for s in range(n):
        x = tuple(sorted((v + s) % n for v in a))
        y = tuple(sorted((v + s) % n for v in b))
        ims.append(tuple(sorted((x, y))))
    return min(ims)


buckets = defaultdict(list)
for sup in combinations(range(n), 4):
    buckets[elementary(tuple(roots[x] for x in sup))].append(sup)

all_unordered = set()
smooth_unordered = set()
all_orbits = set()
smooth_orbits = set()
for key, members in buckets.items():
    s = smooth(key)
    for a, b in combinations(members, 2):
        if set(a) & set(b):
            continue
        all_unordered.add((a, b))
        all_orbits.add(canon(a, b))
        if s:
            smooth_unordered.add((a, b))
            smooth_orbits.add(canon(a, b))

print(f"n={n} p={p}  (matching e1,e2,e3 == matching power sums p1,p2,p3)")
print()
print(f"  unordered disjoint matched pairs, ALL      : {len(all_unordered)}")
print(f"  ordered   (= 2x)                           : {2*len(all_unordered)}")
print(f"  OUR BANKED (32,4,97)                       : 792 = 2 x 396",
      "  MATCH" if len(all_unordered) == 396 else "  MISMATCH")
print()
print(f"  ...after their smoothness predicate         : {len(smooth_unordered)}")
print(f"  shift-orbits of ALL matched pairs           : {len(all_orbits)}")
print(f"  shift-orbits of SMOOTH matched pairs (T_sm) : {len(smooth_orbits)}")
print(f"  THEIR REPORTED T_sm                         : 9",
      "  MATCH" if len(smooth_orbits) == 9 else "  MISMATCH")
print()
print(f"  non-smooth unordered pairs discarded        : "
      f"{len(all_unordered) - len(smooth_unordered)}")
sizes = {}
for o in smooth_orbits:
    cnt = sum(1 for pr in smooth_unordered if canon(*pr) == o)
    sizes[o] = cnt
print(f"  smooth orbit sizes                          : {sorted(sizes.values())}")
print(f"  sum of smooth orbit sizes                   : {sum(sizes.values())}"
      f" (= smooth unordered {len(smooth_unordered)})")
print()
print("CONCLUSION: their T_sm is our H4 collision census restricted to the")
print("smooth (rho != 0, sigma^3 != 27 rho^2) locus and quotiented by the")
print("order-n cyclic shift. Same universe, strictly smaller count.")

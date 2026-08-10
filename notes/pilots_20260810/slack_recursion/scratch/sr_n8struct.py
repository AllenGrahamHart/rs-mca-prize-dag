#!/usr/bin/env python3
"""Structure of the n=8 all-word MAXIMIZER (F_LIST = 7): dump the agreement
sets A_i (index sets in D = mu_8) of every coset attaining the maximum, plus
the pairwise-intersection profile of the complements B_i = D\\A_i."""
import json, sys
from itertools import combinations
from math import comb
import sr_words as SW

q = int(sys.argv[1])
out = sys.argv[2] if len(sys.argv) > 2 else None
n, k = 8, 4
a = k + 1
g = SW.find_gen(q, n)
D = [pow(g, i, q) for i in range(n)]
dmax = n - 1 - a
us = []
for d in range(dmax + 1):
    if d == 0:
        us.append((0, [1]))
        continue
    for co in range(q ** d):
        c = []
        x = co
        for _ in range(d):
            c.append(x % q)
            x //= q
        c.append(1)
        us.append((d, c))
LAs = []
for A in combinations(range(n), a):
    p = [1]
    for i in A:
        x = D[i]
        np_ = [0] * (len(p) + 1)
        for j, c in enumerate(p):
            if c:
                np_[j + 1] = (np_[j + 1] + c) % q
                np_[j] = (np_[j] - c * x) % q
        p = np_
    LAs.append((A, p))
cnt = {}
for A, LA in LAs:
    for d, u in us:
        P = [0] * (a + d + 1)
        for i, c in enumerate(LA):
            if c:
                for j, e in enumerate(u):
                    if e:
                        P[i + j] = (P[i + j] + c * e) % q
        key = tuple(P[j] if j < len(P) else 0 for j in range(k, n))
        cnt.setdefault(key, []).append((A, tuple(P)))
best = max(len({p for _, p in v}) for v in cnt.values())
hits = [(key, v) for key, v in cnt.items() if len({p for _, p in v}) == best]
recs = []
for key, v in hits[:40]:
    As = sorted(set(A for A, _ in v))
    Bs = [tuple(sorted(set(range(n)) - set(A))) for A in As]
    inter = {}
    for i in range(len(Bs)):
        for j in range(i + 1, len(Bs)):
            s = len(set(Bs[i]) & set(Bs[j]))
            inter[str(s)] = inter.get(str(s), 0) + 1
    pts = sorted(set(x for B in Bs for x in B))
    recs.append(dict(key=list(key), n_A=len(As), A_sets=[list(x) for x in As],
                     B_sets=[list(x) for x in Bs],
                     B_pair_intersections=inter,
                     points_covered=pts, n_points=len(pts),
                     deg=max(i for i, c in enumerate(v[0][1]) if c)))
res = dict(n=n, q=q, g=g, MAXWORD_LIST=best, n_maximizing_cosets=len(hits),
           samples=recs[:12])
print(json.dumps(res, indent=1)[:6000])
if out:
    with open(out, "w") as f:
        json.dump(res, f, indent=1)

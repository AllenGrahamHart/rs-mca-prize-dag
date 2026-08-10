"""D3 continued: F_LMAX(a=K+1) and F_DECAY across a q-ladder at n_s=8.

At n_s=8, a=5 the size-5 root sets give Im(M_S) of dimension 3 = a HYPERPLANE
in F^4, with normal nu_S.  A key is reached from S iff nu_S . key = 0.  So the
maximiser lies in the null space of some rank-3 triple of normals; those
C(56,3) = 27720 candidates are enumerated, ranked by the cheap normal count,
and the top ones are then counted EXACTLY (with the h-validity filter and the
size-6/7 contributions).  Anchor: this must reproduce the brute-force
F_LMAX(8,17,5) = 7 already verified in d3_lmax.py.
"""
import math
from math import isqrt, comb
from itertools import combinations

import ffield as ff
from d3_lmax import build, count_at, lmax_closure


def normals(n_s, K, q, a):
    D = ff.subgroup(n_s, q)
    out = []
    for S in combinations(range(n_s), a):
        PS = ff.poly_from_roots([D[i] for i in S], q)
        nh = n_s - a
        rows = [[PS[K + t - i] if 0 <= K + t - i <= a else 0 for i in range(nh)]
                for t in range(n_s - K)]
        Im = ff.colspace(rows, n_s - K, nh, q)
        ns = ff.nullspace([list(r) for r in Im], n_s - K, q)
        if len(ns) == 1:
            out.append(ns[0])
    return out


def lmax5(n_s, K, q, a, topk=60):
    nus = normals(n_s, K, q, a)
    cands = {}
    for T in combinations(range(len(nus)), 3):
        ns = ff.nullspace([nus[i] for i in T], n_s - K, q)
        if len(ns) != 1:
            continue
        v = ff.canon_subspace([ns[0]], n_s - K, q)
        if v in cands:
            continue
        w = list(v[0])
        cands[v] = sum(1 for nu in nus
                       if sum(a1 * b1 for a1, b1 in zip(nu, w)) % q == 0)
    ranked = sorted(cands.items(), key=lambda kv: -kv[1])[:topk]
    D, items, R = build(n_s, K, q, a)
    best = 0
    for v, _ in ranked:
        c = count_at(items, list(v[0]), q)
        if c is not None and c > best:
            best = c
    return best, len(nus), len(cands)


if __name__ == "__main__":
    n_s, K = 8, 4
    print("=== F_LMAX(a=5) via the rank-3 normal-triple candidate family ===")
    print(f"{'q':>10} {'log2q':>7} {'B_s':>7} {'#normals':>9} {'#cands':>8} "
          f"{'F_LMAX(5)':>10} {'F_LMAX(6)':>10} {'F_DECAY':>9} {'/log2q':>8} {'safe(5)?':>9}")
    ratios = []
    for q in (17, 41, 97, 257, 65537):
        if (q - 1) % n_s:
            continue
        Bs = isqrt(q)
        v5, nn, nc = lmax5(n_s, K, q, 5)
        v6, _, _ = lmax_closure(n_s, K, q, 6)
        dec = math.log2(v5) - math.log2(v6)
        r = dec / math.log2(q)
        ratios.append(r)
        print(f"{q:>10} {math.log2(q):>7.2f} {Bs:>7} {nn:>9} {nc:>8} "
              f"{v5:>10} {v6:>10} {dec:>9.4f} {r:>8.4f} {str(v5 <= Bs):>9}")
    print()
    print(f"  ANCHOR: q=17 must give F_LMAX(5) = 7 (brute-force verified).")
    print(f"  measured F_DECAY/log2 q range: [{min(ratios):.4f}, {max(ratios):.4f}]")

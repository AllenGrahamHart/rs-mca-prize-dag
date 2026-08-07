#!/usr/bin/env python3
"""Evaluate OUR SOL_TARGET_4 conjecture T_4(q,N) <= C N^3 on the densest rows,
including the row maelcar #1147 uses for its K(d,e) counterexample.

SOL_TARGET_4_H4_COLLISION_CENSUS.md:
    q odd prime > 4, N a power of two with N | q-1,
    T_4(q,N) = #{ORDERED pairs (A,B): A,B disjoint 4-subsets of mu_N,
                 p_i(A) = p_i(B) for i = 1,2,3}
    Conjecture: exists absolute C with T_4(q,N) <= C N^3 for ALL such (q,N).

NOTE: matching p_1,p_2,p_3 <=> matching e_1,e_2,e_3 (Newton, char > 3).
This counts ALL matched pairs -- no smoothness restriction, no orbit
quotient -- i.e. exactly our T_4, not maelcar's T_sm.
"""
from itertools import chain, combinations

import numpy as np


def root_of_order(p, n):
    for c in range(2, p):
        z = pow(c, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            return z
    raise AssertionError


def T4(N, q):
    roots = np.array([pow(root_of_order(q, N), e, q) for e in range(N)],
                     dtype=np.int64)
    total = N * (N - 1) * (N - 2) * (N - 3) // 24
    quad = np.fromiter(chain.from_iterable(combinations(range(N), 4)),
                       dtype=np.uint8, count=4 * total).reshape(-1, 4)
    key = np.empty(total, dtype=np.int64)
    for lo in range(0, total, 1 << 20):
        hi = min(lo + (1 << 20), total)
        c = quad[lo:hi].astype(np.int64)
        v0, v1, v2, v3 = (roots[c[:, i]] for i in range(4))
        e1 = (v0 + v1 + v2 + v3) % q
        e2 = (v0*v1 + v0*v2 + v0*v3 + v1*v2 + v1*v3 + v2*v3) % q
        e3 = (v0*v1*v2 + v0*v1*v3 + v0*v2*v3 + v1*v2*v3) % q
        key[lo:hi] = (e1 * q + e2) * q + e3
    order = np.argsort(key, kind="stable").astype(np.int32)
    ks = key[order]
    del key
    starts = np.flatnonzero(np.r_[True, ks[1:] != ks[:-1]]).astype(np.int32)
    del ks
    lengths = np.diff(np.r_[starts, np.int32(total)]).astype(np.int32)
    keep = lengths >= 2
    starts, lengths = starts[keep], lengths[keep]

    unordered = 0
    for L in np.unique(lengths):
        s = starts[lengths == L]
        blk = order[s[:, None] + np.arange(L, dtype=np.int32)]
        for a, b in combinations(range(int(L)), 2):
            A, B = quad[blk[:, a]], quad[blk[:, b]]
            d = np.ones(len(A), dtype=bool)
            for i in range(4):
                for j in range(4):
                    d &= (A[:, i] != B[:, j])
            unordered += int(d.sum())
        del blk
    return 2 * unordered


print("SOL_TARGET_4 ladder on the densest admissible row per N")
print("(q = smallest prime = 1 mod N; all satisfy q odd prime > 4, N | q-1)")
print()
print(f"{'N':>5} {'q':>5} {'T_4(q,N)':>12} {'N^3':>12} {'T_4 / N^3':>11}")
print("-" * 50)
prev = None
for N, q in ((16, 17), (32, 97), (64, 193), (128, 257)):
    t = T4(N, q)
    r = t / N**3
    growth = "" if prev is None else f"   x{r/prev:.3f} vs prev"
    print(f"{N:>5} {q:>5} {t:>12} {N**3:>12} {r:>11.4f}{growth}")
    prev = r
print()
print("CONTROL: our banked record (background/nodes/u1_x4_direct_column_budget/")
print("         notes/F3_IDENTIFICATION.md:21) states (32,4,97): 792 = 2 x 396")
print("         and (16,4,97): 12 = 2 x 6.")
print()
print("READ THIS AS: evidence only, not a falsification. C is an absolute")
print("constant; a rising ratio across the densest rows is a WARNING that the")
print("conjecture may need a q-vs-N hypothesis, which it currently does NOT have.")

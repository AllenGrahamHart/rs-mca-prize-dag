#!/usr/bin/env python3
"""STAGE 3 -- how large can the RAY COUNT V be?

Stage 1: the K_V family (V rays, M=C(V,2) data) is admissible, has rank
EXACTLY V h, and caps at V = (h+1)/(d+1)+1 because its cores share one
(k-1)-set.
Stage 2: SPREAD-V drops the common (k-1)-set.  Its support system is
combinatorially PERFECT (all |S_a|=A, all |S_a^S_b|=k+d distinct, all
triples = k-1) at ANY V -- but it is ALGEBRAICALLY DEGENERATE: the ray
blocks collapse (rank = m+h-d, not Vh) and all C(V,2) band pairs coincide.

Stage 3 asks the decisive question EXHAUSTIVELY at toy scale:

  (Q1) how large can a "ray clique" be -- V supports of size A, pairwise
       meeting in exactly k+d, all triples <= k-1?
  (Q2) among those, how large can V be with the ray system INDEPENDENT
       (rank = V h), which is what non-degeneracy needs?

Run: tools/ramguard local -- python3 stage3.py
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import advlib as A                                            # noqa: E402
import tslib as T                                             # noqa: E402
import occlib                                                 # noqa: E402

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def ray_cliques(n, k, h, d, cap=200000):
    """All supports S (|S| = A) meeting S1 = [0..A-1] in exactly k+d, then a
    randomised max-clique hunt in the compatibility graph (pairwise
    intersection k+d, all triples <= k-1)."""
    Ai = k + h
    S1 = frozenset(range(Ai))
    out = []
    for inside in itertools.combinations(range(Ai), k + d):
        for outside in itertools.combinations(range(Ai, n), h - d):
            out.append(frozenset(inside) | frozenset(outside))
            if len(out) > cap:
                return S1, out
    return S1, out


def grow_clique(S1, cands, k, d, rng, rounds=400):
    """Randomised greedy: build maximal sets {S1} u ... with all pairwise
    intersections = k+d and all triple intersections <= k-1."""
    best = [S1]
    kd = k + d
    for _ in range(rounds):
        cur = [S1]
        order = list(range(len(cands)))
        rng.shuffle(order)
        for idx in order:
            S = cands[idx]
            ok = True
            for a in range(len(cur)):
                if len(cur[a] & S) != kd:
                    ok = False
                    break
            if not ok:
                continue
            for a in range(len(cur)):
                for b in range(a + 1, len(cur)):
                    if len(cur[a] & cur[b] & S) > k - 1:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                cur.append(S)
        if len(cur) > len(best):
            best = cur
    return best


def independent_rank(row, S, zs):
    rows = []
    for a, s in enumerate(S):
        rows += T.ray_rows(row, tuple(sorted(s)), zs[a])
    return T.rank_mod(rows, row.q)


def main():
    res = []
    rng = random.Random(20260802)
    # toy shapes where the enumeration is bounded
    SHAPES = [
        dict(n=14, k=3, h=4, d=1, q=6421),
        dict(n=16, k=3, h=5, d=1, q=6421),
        dict(n=18, k=3, h=5, d=1, q=6421),
        dict(n=20, k=3, h=5, d=1, q=6421),
        dict(n=18, k=3, h=6, d=1, q=6421),
        dict(n=20, k=3, h=6, d=2, q=6421),
        dict(n=18, k=4, h=5, d=1, q=6421),
        dict(n=20, k=4, h=6, d=1, q=6421),
    ]
    for sh in SHAPES:
        n, k, h, d, q = sh["n"], sh["k"], sh["h"], sh["d"], sh["q"]
        S1, cands = ray_cliques(n, k, h, d)
        clique = grow_clique(S1, cands, k, d, rng, rounds=250)
        V = len(clique)
        kv_cap = (h + 1) // (d + 1) + 1
        row = T.Row2(n, k, h, q)
        # rank of the ray system over several slope choices
        best = None
        for _ in range(40):
            zs = rng.sample(range(1, q), V)
            rk = independent_rank(row, clique, zs)
            if best is None or rk > best[0]:
                best = (rk, zs)
        rk, zs = best
        m = len(set().union(*clique)) - k
        rec = dict(shape=sh, n_candidates=len(cands), V_found=V,
                   KV_cap=kv_cap, rank=rk, Vh=V * h, m=m,
                   two_m_minus_1=2 * m - 1, two_R_minus_1=2 * row.R - 1,
                   independent=rk == V * h,
                   M_if_complete=V * (V - 1) // 2)
        res.append(rec)
        tag = f"n={n} k={k} h={h} d={d}"
        chk(f"S3 {tag}: max ray-clique V={V} (K_V cap {kv_cap})", True,
            f"candidates={len(cands)} M=C(V,2)={rec['M_if_complete']}")
        chk(f"S3 {tag}: ray system INDEPENDENT (rank == V*h = {V*h})",
            rk == V * h, f"rank={rk} m={m} 2m-1={2*m-1}")
        chk(f"S3 {tag}: V does NOT exceed the K_V cap {kv_cap}",
            V <= kv_cap, f"V={V}")

    # ---- can we ADD a ray to a saturated K_V family? --------------------
    print("\n=== can a K_V family be extended by one more ray? ===")
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421),
               dict(k=3, h=7, d=1, V=5, q=6421),
               dict(k=3, h=9, d=1, V=6, q=10007)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        M = V * (V - 1) // 2
        n = (k - 1) + M * (d + 1)
        n = max(n, k + h + 2)
        row = T.Row2(n, k, h, q)
        b = A.build_KV(row, d, V, seed=0)
        if b is None:
            continue
        u, v, info = b
        S = [frozenset(s) for s in info["supports"].values()]
        found = 0
        exemplar = None
        Ai = k + h
        # exhaustive over A-subsets is too big; sample structured candidates
        pool = list(range(n))
        for _ in range(200000):
            cand = frozenset(random.Random(_).sample(pool, Ai))
            if all(len(cand & s) == k + d for s in S) and \
               all(len(cand & S[a] & S[b]) <= k - 1
                   for a in range(len(S)) for b in range(a + 1, len(S))):
                found += 1
                exemplar = sorted(cand)
                break
        chk(f"S3-EXT k={k} h={h} d={d} V={V}: NO {V+1}-st ray compatible "
            f"with the saturated K_V family (200k random A-sets)",
            found == 0, f"found={found} ex={exemplar}")

    with open(os.path.join(HERE, "stage3.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)
    del occlib


if __name__ == "__main__":
    main()

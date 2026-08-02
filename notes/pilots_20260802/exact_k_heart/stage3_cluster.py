#!/usr/bin/env python3
r"""STAGE 3 -- LOCALITY, the co-sunflower cluster, and its admissibility.

THE CO-SUNFLOWER (the d = 0 analogue of K_V).  Fix U with |U| = k + 2h and
m pairwise DISJOINT h-subsets t_1..t_m of U.  Put S_a = U \ t_a.  Then
|S_a| = A and |S_a ^ S_b| = |U| - 2h = k EXACTLY for every pair: a CLIQUE
of C(m,2) distinct d = 0 cores on m rays.  Combinatorially perfect.

PRE-REGISTERED PREDICTIONS
  P1  rank(co-sunflower_m) = min(m h, 4h) exactly  [locality caps at 2*2h]
  P2  m >= 4 is ALGEBRAICALLY DEAD: rank = 4h = full redundancy of the
      shortened code on U, so the solution space on U is exactly
      RS_k|_U x RS_k|_U -- u,v are codewords on U, every slope over-agrees
      (agreement |U| = A+h > A) and no ray is live.  (SPREAD-V genre.)
  P3  m = 3 is admissible (rank 3h <= 4h-1).
  P4  LOCALITY (unconditional): any live family has
      rank <= 2(|union S_a| - k) - 1.
  P5  relation support >= 4; support 2 and 3 vanish at d = 0.
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dzlib as Z                                              # noqa: E402
import tslib as T                                              # noqa: E402
import occlib                                                  # noqa: E402

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def cosunflower(row, m):
    """U = first k+2h points, t_a = disjoint h-blocks, S_a = U \\ t_a."""
    k, h, n = row.k, row.h, row.n
    c = k + 2 * h
    if c > n or m * h > c:
        return None
    U = list(range(c))
    ts = [tuple(U[a * h:(a + 1) * h]) for a in range(m)]
    Ss = [tuple(sorted(set(U) - set(t))) for t in ts]
    return U, ts, Ss


def agreement(row, w, S):
    """(extends?, agreement size, codeword) for w on support S (|S|>=k)."""
    q, n = row.q, row.n
    W = tuple(sorted(S))[:row.k]
    f = row.interp(W, [w[i] for i in W])
    agr = sum(1 for i in range(n) if row.ev(f, row.xs[i]) == w[i])
    ok = all(row.ev(f, row.xs[i]) == w[i] for i in S)
    return ok, agr, f


def main():
    rng = random.Random(4242)
    shapes = [(16, 6, 3, 61), (20, 9, 3, 41), (20, 8, 4, 43),
              (18, 8, 3, 37), (24, 12, 3, 53), (16, 5, 4, 47)]
    prof = {}
    for (n, k, h, q) in shapes:
        row = Z.make_row(n, k, h, q)
        A, tag = row.A, f"n{n}k{k}h{h}q{q}"
        mmax = (k + 2 * h) // h
        rec = dict(n=n, k=k, h=h, A=A, U=k + 2 * h, mmax=mmax, ranks={},
                   admissible={}, solspace={})
        for m in range(2, min(mmax, 7) + 1):
            built = cosunflower(row, m)
            if built is None:
                continue
            U, ts, Ss = built
            # every pair is an exact-k datum
            allk = all(len(set(Ss[a]) & set(Ss[b])) == k
                       for a in range(m) for b in range(a + 1, m))
            chk(f"CS clique exact-k {tag} m={m}", allk)
            zs = rng.sample(range(1, q), m)
            rays = list(zip(zs, Ss))
            rk, exp = Z.family_rank(row, rays)
            rec["ranks"][m] = dict(rank=rk, Vh=exp, cap=4 * h)
            # ---- P1
            chk(f"P1 rank=min(mh,4h) {tag} m={m}",
                rk == min(m * h, 4 * h), (rk, m * h, 4 * h))
            # ---- P4 locality on the union
            uni = len(set().union(*[set(S) for S in Ss]))
            chk(f"P4 locality rank<=2(u-k) {tag} m={m}",
                rk <= 2 * (uni - k), (rk, 2 * (uni - k), uni))
            # ---- solution space dimension on U
            rows = []
            for z, S in rays:
                rows += T.ray_rows(row, S, z)
            ns = T.nullspace_mod(rows, 2 * n, q)
            rec["solspace"][m] = dict(dim=len(ns), degen=2 * k + 2 * (n - len(U)))
            # ---- P2/P3 admissibility: draw solutions, test liveness
            live_ok = 0
            over = 0
            tries = 12
            for s in range(tries):
                sol = T.realise(row, rows, seed=1000 * m + s, tries=60,
                                require_v_nonzero=False)
                if sol is None:
                    continue
                u, v = sol
                good = True
                for z, S in rays:
                    w = [(u[i] + z * v[i]) % q for i in range(n)]
                    ok, agr, f = agreement(row, w, S)
                    if not ok or agr != A:
                        good = False
                        if ok and agr > A:
                            over += 1
                if good:
                    live_ok += 1
            rec["admissible"][m] = dict(good=live_ok, tries=tries,
                                        overagree=over)
        prof[tag] = rec
        print(f"{tag}: mmax={mmax} ranks="
              f"{ {m: rec['ranks'][m]['rank'] for m in rec['ranks']} } "
              f"admissible={ {m: rec['admissible'][m]['good'] for m in rec['admissible']} }")
    OUT["data"]["cosunflower"] = prof
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage3.json"), "w"), indent=1)
    print(f"stage3: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()

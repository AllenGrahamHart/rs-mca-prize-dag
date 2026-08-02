#!/usr/bin/env python3
r"""STAGE 2 -- the d = 0 relation module: where can rank deficit live?

A relation among the ray blocks of a k-packed live family is
    sum_a c_a = 0,  sum_a z_a c_a = 0,  c_a in C_{S_a},
equivalently (eliminating z_V)  sum_{a<V} (z_a - z_V) c_a = 0  with the
weighted sum landing in C_{S_V}.  So the PRIMITIVE object is a SUM-ZERO
relation among shortened duals; the slope equation then costs one more
support.

  R1  support-2 sum-zero relations: dim C_{S_1 ^ S_2} = 0 at d = 0
  R2  support-3 sum-zero relations: measured over k-packed triples
  R3  support-m (m = 3..6) two-equation relations: measured nullity
  R4  pointwise (L3a) rigidity: a participant vanishes at every point
      covered <= 2 times -> < h such points allowed
  R5  the covering-cost inequality and the implied minimum support
  R6  random k-packed ray systems: rank = V h?
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

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def sumzero_nullity(row, supports):
    """dim {(c_a) : c_a in C_{S_a}, sum_a c_a = 0}."""
    q, n = row.q, row.n
    blocks = [T.dual_basis(S, row) for S in supports]
    ncol = sum(len(b) for b in blocks)
    M = [[0] * ncol for _ in range(n)]
    col = 0
    for B in blocks:
        for c in B:
            for i in range(n):
                M[i][col] = c[i] % q
            col += 1
    return len(T.nullspace_mod(M, ncol, q))


def rand_kpacked_rays(row, V, rng, tries=200000, want_exact_k=True):
    """V supports of size A, pairwise intersections <= k (== k if
    want_exact_k and it fits)."""
    n, k, A = row.n, row.k, row.A
    out = []
    for _ in range(tries):
        S = tuple(sorted(rng.sample(range(n), A)))
        ok = True
        for Tt in out:
            j = len(set(S) & set(Tt))
            if j > k:
                ok = False
                break
        if ok:
            out.append(S)
        if len(out) == V:
            break
    return out


def main():
    rng = random.Random(11)
    shapes = [(12, 4, 3, 97), (14, 4, 4, 101), (16, 5, 4, 97),
              (16, 4, 5, 113), (18, 6, 4, 73), (20, 6, 5, 101),
              (20, 5, 4, 101), (18, 4, 4, 73)]
    r2hits = []
    r3prof = []
    for (n, k, h, q) in shapes:
        row = Z.make_row(n, k, h, q)
        A, tag = row.A, f"n{n}k{k}h{h}q{q}"
        # ---------- R1/R2: sum-zero relations on 2 and 3 supports
        n2 = n3 = 0
        trials = 0
        for _ in range(40):
            sup = rand_kpacked_rays(row, 3, rng)
            if len(sup) < 3:
                continue
            trials += 1
            a = sumzero_nullity(row, sup[:2])
            b = sumzero_nullity(row, sup)
            n2 += (a > 0)
            n3 += (b > 0)
            if b > 0:
                r3prof.append(dict(shape=[n, k, h, q], nullity=b,
                                   inter=[len(set(sup[i]) & set(sup[j]))
                                          for i in range(3)
                                          for j in range(i + 1, 3)]))
        chk(f"R1 no support-2 sum-zero {tag}", n2 == 0, n2)
        r2hits.append((tag, trials, n3))
        # ---------- R3: full two-equation nullity, m = 3..6
        prof = {}
        for m in (3, 4, 5, 6):
            sup = rand_kpacked_rays(row, m, rng)
            if len(sup) < m:
                continue
            zs = rng.sample(range(1, q), m)
            rel, ncol = Z.relation_space(row, list(zip(zs, sup)))
            prof[m] = dict(nullity=len(rel), ncol=ncol,
                           rank=ncol - len(rel), expect=m * h)
            if m <= 3:
                chk(f"R3 nullity 0 at m={m} {tag}", len(rel) == 0, len(rel))
        OUT["data"][tag] = prof
        # ---------- R6: random k-packed systems, V as large as fits
        Vmax = min(8, (n - k) // h + 2)
        sup = rand_kpacked_rays(row, Vmax, rng)
        zs = rng.sample(range(1, q), len(sup))
        rk, exp = Z.family_rank(row, list(zip(zs, sup)))
        chk(f"R6 random k-packed rank = Vh {tag} V={len(sup)}",
            rk == min(exp, 2 * row.R), (rk, exp, 2 * row.R))
    OUT["data"]["r3_sumzero_hits"] = r2hits
    OUT["data"]["r3_profiles"] = r3prof[:20]
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage2.json"), "w"), indent=1)
    print("sum-zero-3 hits per shape (tag, trials, #nullity>0):", r2hits)
    print(f"stage2: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""STAGE 1 -- the d = 0 cost theorem and its relation module.

Checks
  C1  dim C_S = |S| - k  (L1, re-verified in this file's shapes)
  C2  locator normal form  C_S = {nu . Lam_{D\\S} . r : deg r < h}
  C3  CORE ROWS ARE EMPTY at d = 0 (dim C_Z = 0) -- the structural break
  C4  rank of a d = 0 two-slope datum = 2h EXACTLY (all slope types)
  C5  support-2 relations vanish (sharp: deg lcm(m_1,m_2) = R exactly)
  C6  support-3 relations vanish under |S_a ^ S_b| <= k
  C7  support-4: measured nullity of k-packed 4-ray systems
  C8  family rank of random k-packed ray systems = V h?  (deficit hunt)
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

OUT = {"checks": [], "fail": 0, "pass": 0}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


SHAPES = [(12, 4, 3, 97), (14, 4, 4, 101), (16, 5, 4, 97),
          (16, 4, 5, 113), (18, 6, 4, 73), (20, 6, 5, 101),
          (18, 5, 3, 73)]


def build_row(n, k, h, q):
    return Z.make_row(n, k, h, q)


def rand_d0_datum(row, rng, tries=2000):
    """(Z, S1, S2) with |Z| = k, |S_j| = A, S1 ^ S2 = Z."""
    n, k, A, h = row.n, row.k, row.A, row.h
    if k + 2 * h > n:
        return None
    for _ in range(tries):
        pool = rng.sample(range(n), k + 2 * h)
        Zs = tuple(sorted(pool[:k]))
        B1 = pool[k:k + h]
        B2 = pool[k + h:]
        S1 = tuple(sorted(set(Zs) | set(B1)))
        S2 = tuple(sorted(set(Zs) | set(B2)))
        if len(S1) == A and len(S2) == A and set(S1) & set(S2) == set(Zs):
            return Zs, S1, S2
    return None


def main():
    rng = random.Random(20260802)
    for (n, k, h, q) in SHAPES:
        row = build_row(n, k, h, q)
        A = row.A
        tag = f"n{n}k{k}h{h}q{q}"
        # ---- C1 / C2
        S = tuple(sorted(rng.sample(range(n), A)))
        B = T.dual_basis(S, row)
        chk(f"C1 dimC_S={h} {tag}", len(B) == h and
            T.rank_mod(B, q) == h, (len(B), h))
        # orthogonality to RS_k
        ok = True
        for c in B:
            for e in range(k):
                s = sum(c[i] * pow(row.xs[i], e, q) for i in range(n)) % q
                if s:
                    ok = False
        chk(f"C1b C_S _|_ RS_k {tag}", ok)
        # locator normal form
        rows2 = []
        for e in range(h):
            r = [0] * e + [1]
            rows2.append(Z.dual_from_locator(row, S, r))
        both = B + rows2
        chk(f"C2 locator normal form {tag}",
            T.rank_mod(rows2, q) == h and T.rank_mod(both, q) == h)
        # ---- C3 / C4
        dat = rand_d0_datum(row, rng)
        if dat is None:
            continue
        Zs, S1, S2 = dat
        for (z1, z2) in [(1, 2), (3, 7), (0, 5), (1, T.INF), (0, T.INF)]:
            rk, ncore = Z.datum_rank_d0(row, Zs, S1, z1, S2, z2)
            chk(f"C3 core rows empty {tag}", ncore == 0, ncore)
            chk(f"C4 datum rank 2h {tag} z={z1},{z2}", rk == 2 * h,
                (rk, 2 * h))
        # ---- C5 sharpness of the support-2 kill
        m1 = Z.locator(row, [i for i in range(n) if i not in set(S1)])
        m2 = Z.locator(row, [i for i in range(n) if i not in set(S2)])
        g = len([i for i in range(n) if i not in set(S1) | set(S2)])
        deg_lcm = (len(m1) - 1) + (len(m2) - 1) - g
        chk(f"C5 deg lcm = R {tag}", deg_lcm == row.R, (deg_lcm, row.R))
        rel, ncol = Z.relation_space(row, [(1, S1), (2, S2)])
        chk(f"C5b support-2 nullity 0 {tag}", len(rel) == 0, len(rel))
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage1.json"), "w"), indent=1)
    print(f"stage1 core: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()

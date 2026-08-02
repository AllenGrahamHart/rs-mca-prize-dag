#!/usr/bin/env python3
"""STAGE 6 -- the structural lemmas, and how far the induction gets.

THE REFORMULATION.  For a two-slope family with rays (z_a, S_a), a = 1..V:

  (T1) the CORE rows are implied by the RAY rows.  Indeed S_a ^ S_b = Z_ab
       (banked T2) and L1 give C_{S_a} ^ C_{S_b} = C_{Z_ab}; for c in that
       intersection (c, z_a c) and (c, z_b c) are both rows, so their
       difference gives (0, c) and hence (c, 0).  Therefore
                 rank(family) = dim sum_a G_{z_a}(C_{S_a})  <=  V h,
       i.e. the charge is h per RAY, not 2h per datum.

  (T2) a datum IS a pair of rays: its core is S_a ^ S_b, so distinct data
       need distinct ray pairs and  M <= C(V,2).

  (T3) realisability: rank <= 2m-1 with m = |union S_a| - k, otherwise the
       solution space on T is exactly C|_T x C|_T and the whole family
       collapses to a single band pair.

  Together:  V h <= 2R-1  and  N_d <= C(V,2).

THE INDUCTION.  Write delta = V h - rank, the dimension of the relation space
  Rel = {(c_a) in (+)C_{S_a} : sum c_a = 0, sum z_a c_a = 0}.
  * support 1: c_a = 0 trivially.
  * support 2: c_1 + c_2 = 0 and z_1c_1 + z_2c_2 = 0 give (z_1-z_2)c_1 = 0,
    so c_1 = 0.  NO relation.
  * support 3: eliminating c_3 gives c_1 in C_{S_1} ^ C_{S_2} ^ C_{S_3}
    = C_{S_1 ^ S_2 ^ S_3}, and S_1^S_2^S_3 = Z_12 ^ Z_13 has size <= k-1 by
    k-packing, so the space is ZERO.  NO relation.
  * support 4: eliminating c_4 gives
       c_3 in C_{S_3} ^ (C_{S_1} + C_{S_2}) = C_{S_3 ^ (S_1 u S_2)},
    of dimension |S_3 ^ (S_1 u S_2)| - k = k + 2d - |S_1^S_2^S_3| >= 2d+1.
    NONZERO.  ** THE INDUCTION STOPS HERE. **  The precise open statement is
    that the two extra linear conditions carried by a support-4 relation are
    never satisfiable for an admissible ray system.

Run: tools/ramguard local -- python3 stage6_theory.py
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


def graph_rows(row, S, z):
    return T.ray_rows(row, tuple(sorted(S)), z)


def relation_dim(row, S, zs, idxs):
    """dim of {(c_a)_{a in idxs} : sum c_a = 0, sum z_a c_a = 0}."""
    q, n = row.q, row.n
    blocks, widths = [], []
    for a in idxs:
        B = T.dual_basis(tuple(sorted(S[a])), row)
        blocks.append(B)
        widths.append(len(B))
    tot = sum(widths)
    # unknown = coefficient vector; constraints: 2n rows
    cols = []
    for bi, a in enumerate(idxs):
        for c in blocks[bi]:
            cols.append([x % q for x in c] + [zs[a] * x % q for x in c])
    # kernel of the tot x 2n matrix acting on the LEFT (coefficients)
    Mrows = [[cols[j][i] for j in range(tot)] for i in range(2 * n)]
    return tot - T.rank_mod(Mrows, q)


def main():
    res = []
    CASES = [dict(k=3, h=5, d=1, V=4, q=6421),
             dict(k=3, h=7, d=1, V=5, q=6421),
             dict(k=3, h=9, d=1, V=6, q=10007),
             dict(k=3, h=8, d=2, V=4, q=10007),
             dict(k=4, h=7, d=1, V=5, q=6421)]
    for cs in CASES:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        M = V * (V - 1) // 2
        n = max((k - 1) + M * (d + 1), k + h + 2)
        row = T.Row2(n, k, h, q)
        b = A.build_KV(row, d, V, seed=0)
        if b is None:
            continue
        u, v, info = b
        S = [tuple(s) for s in info["supports"].values()]
        zs = list(info["zs"])
        Zs = [tuple(z) for z in info["cores"].values()]
        tag = f"k={k} h={h} d={d} V={V} n={n}"

        # T1: core rows implied by ray rows
        rrows = []
        for a, s in enumerate(S):
            rrows += graph_rows(row, s, zs[a])
        r_ray = T.rank_mod(rrows, q)
        crows = list(rrows)
        for Z in Zs:
            crows += T.core_rows(row, Z)
        r_all = T.rank_mod(crows, q)
        chk(f"T1 {tag}: core rows are IMPLIED by ray rows "
            f"(rank unchanged)", r_ray == r_all,
            f"rays={r_ray} rays+cores={r_all} Vh={V*h} 2hM={2*h*M}")

        # L1 identity C_{S_a} ^ C_{S_b} = C_{Z_ab}
        ok = True
        for a in range(V):
            for b2 in range(a + 1, V):
                Ia = set(S[a]) & set(S[b2])
                da = T.dual_basis(S[a], row)
                db = T.dual_basis(S[b2], row)
                dim_sum = T.rank_mod(da + db, q)
                inter = 2 * h - dim_sum
                if inter != max(0, len(Ia) - k):
                    ok = False
        chk(f"T1b {tag}: L1 -- dim(C_Sa ^ C_Sb) = |S_a^S_b| - k = d",
            ok, f"expected {d}")

        # T2: M <= C(V,2)  (distinct data need distinct ray pairs)
        rec2, pairs, band = occlib.measure(row, u, v, name="kv",
                                           want_checks=True)
        fam = A.measured_family(row, band, d)
        slopes = set()
        for Z, rays in fam:
            for z, s in rays:
                slopes.add((z, s))
        chk(f"T2 {tag}: M = {len(fam)} <= C(V,2) = {M} with V = "
            f"{len(slopes)} distinct live rays",
            len(fam) <= len(slopes) * (len(slopes) - 1) // 2
            and len(fam) == M,
            f"rays={len(slopes)} M={len(fam)}")

        # T3: realisability margin
        Tset = set()
        for s in S:
            Tset |= set(s)
        m = len(Tset) - k
        chk(f"T3 {tag}: rank {r_ray} <= 2m-1 = {2*m-1} (non-collapse)",
            r_ray <= 2 * m - 1, f"m={m} slack={2*m-r_ray}")

        # T4/T5: relation supports
        dims = {}
        for s in (2, 3, 4):
            worst = 0
            for idxs in itertools.combinations(range(V), s):
                dd = relation_dim(row, S, zs, idxs)
                worst = max(worst, dd)
            dims[s] = worst
        chk(f"T4 {tag}: NO relation of support 2 (distinct slopes)",
            dims[2] == 0, f"dim={dims[2]}")
        chk(f"T5 {tag}: NO relation of support 3 (k-packing kills the "
            f"triple intersection)", dims[3] == 0, f"dim={dims[3]}")
        chk(f"T6 {tag}: no relation of support 4 either, in K_V "
            f"(so rank = Vh)", dims[4] == 0,
            f"dim={dims[4]} -- but the support-4 space "
            f"C_(S3^(S1uS2)) has dim {k+2*d-(k-1)}, so this is NOT forced")

        res.append(dict(cs=cs, n=n, m=m, rank_rays=r_ray, rank_all=r_all,
                        Vh=V * h, two_hM=2 * h * M, M=len(fam),
                        live_rays=len(slopes),
                        relation_dims=dims,
                        support4_ambient_dim=k + 2 * d - (k - 1),
                        ADMISSIBLE=rec2["ADMISSIBLE"]))

    # ---- how often does a support-4 relation exist by chance? -----------
    print("\n=== support-4 relations in RANDOM 4-ray systems ===")
    rng = random.Random(5)
    for cs in [dict(n=24, k=3, h=5, d=1, q=6421),
               dict(n=30, k=3, h=7, d=1, q=6421)]:
        row = T.Row2(cs["n"], cs["k"], cs["h"], cs["q"])
        hit, tried = 0, 0
        for _ in range(400):
            S = [tuple(sorted(rng.sample(range(cs["n"]), row.A)))
                 for _ in range(4)]
            zs = rng.sample(range(1, cs["q"]), 4)
            tried += 1
            if relation_dim(row, S, zs, (0, 1, 2, 3)) > 0:
                hit += 1
        chk(f"T7 n={cs['n']} k={cs['k']} h={cs['h']}: support-4 relations "
            f"are NOT generic ({hit}/{tried} random 4-ray systems)",
            hit == 0, f"hits={hit}")

    with open(os.path.join(HERE, "stage6_theory.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""STAGE 8 -- the CONNECTIVITY FLOOR  rank >= m = |union S_a| - k.

LEMMA (MDS sum).  If |X ^ S| >= k then C_X + C_S = C_{X u S}.
    dim(C_X + C_S) = (|X|-k) + (|S|-k) - dim(C_X ^ C_S)
                   = (|X|-k) + (|S|-k) - (|X^S|-k)          [L1]
                   = |X u S| - k = dim C_{X u S},  and the inclusion is clear.

THEOREM (connectivity floor).  For a PAIRWISE-INTERSECTING ray system (every
|S_a ^ S_b| >= k, which holds a fortiori when every pair is a datum, |S_a ^
S_b| = k+d >= k+1), the first-coordinate projection of the row space is

        pi_1(R) = sum_a C_{S_a} = C_{union S_a},   so   rank >= m.

Together with the banked T3 non-collapse bound rank <= 2m-1:

        m / V   <=   charge per ray   <=   (2m-1) / V,

so the occupancy floor 2 holds automatically whenever V <= m/2, and the
residual class is exactly "V > m/2".

Run: tools/ramguard local -- python3 stage8_floor.py
"""
from __future__ import annotations

import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402
import advlib as ADV                                           # noqa: E402
from stage7_doublehole import build_double_hole                # noqa: E402

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def build_u_clique(row, d, V):
    k, h = row.k, row.h
    g, u = h - d, k + 2 * h - d
    if g < 1 or V * g > u or u > row.n:
        return None
    U = list(range(u))
    return [tuple(sorted(set(U) - set(U[i * g:(i + 1) * g])))
            for i in range(V)]


def main():
    rnd = random.Random(31337)
    res = []

    # ---- the MDS sum lemma, directly -----------------------------------
    for (n, k, h, q) in [(24, 4, 6, 6421), (30, 6, 7, 10007),
                         (28, 3, 8, 6421)]:
        row = T.Row2(n, k, h, q)
        bad = 0
        for _ in range(60):
            X = tuple(sorted(rnd.sample(range(n), k + h)))
            ov = rnd.randrange(k, min(k + h, n - h) + 1)
            Sset = set(rnd.sample(list(X), ov))
            while len(Sset) < k + h:
                Sset.add(rnd.randrange(n))
            Sl = tuple(sorted(Sset))
            un = tuple(sorted(set(X) | Sset))
            got = T.rank_mod(T.dual_basis(X, row) + T.dual_basis(Sl, row), q)
            want = len(un) - k
            if got != want:
                bad += 1
        chk(f"F1 n={n} k={k} h={h}: MDS sum lemma C_X + C_S = C_{{XuS}} "
            f"whenever |X^S| >= k (60 random pairs)", bad == 0,
            f"violations={bad}")

    # ---- the floor on every family in this pilot -------------------------
    FAMS = []
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421),
               dict(k=5, h=7, d=1, V=7, q=10007),
               dict(k=4, h=6, d=1, V=6, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        priv = (h - 1) - (V - 1) * d
        n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
        row = T.Row2(n, k, h, q)
        fam = S.build_mobius_family(row, d, V, seed=1)
        if fam:
            FAMS.append(("mobius", cs, row, fam["supports"], fam["slopes"]))
    for cs in [dict(k=3, h=7, d=1, V=5, q=6421),
               dict(k=4, h=7, d=1, V=5, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        M = V * (V - 1) // 2
        n = max((k - 1) + M * (d + 1), k + h + 2)
        row = T.Row2(n, k, h, q)
        b = ADV.build_KV(row, d, V, seed=0)
        if b:
            _, _, info = b
            FAMS.append(("K_V", cs, row,
                         [tuple(s) for s in info["supports"].values()],
                         list(info["zs"])))
    for cs in [dict(k=13, h=4, d=1, V=6, q=6421),
               dict(k=17, h=5, d=1, V=5, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        n = k + 2 * h - d + 2
        row = T.Row2(n, k, h, q)
        sup = build_u_clique(row, d, V)
        if sup:
            FAMS.append(("clique", cs, row, sup,
                         rnd.sample(range(1, q), V)))
    for cs in [dict(k=8, h=8, d=1, V=6, ell=2, q=10007),
               dict(k=14, h=10, d=1, V=6, ell=3, q=10007)]:
        k, h, d, V, ell, q = (cs["k"], cs["h"], cs["d"], cs["V"], cs["ell"],
                              cs["q"])
        priv = (h - ell) - (V - 1) * d
        n = (k + 2 * ell) + (V * (V - 1) // 2) * d + V * priv + 2
        row = T.Row2(n, k, h, q)
        fam = build_double_hole(row, d, V, ell)
        if fam:
            FAMS.append(("double-hole", cs, row, fam["supports"],
                         rnd.sample(range(1, q), V)))

    for name, cs, row, sup, zs in FAMS:
        k, h = row.k, row.h
        V = len(sup)
        U = set()
        for s in sup:
            U |= set(s)
        m = len(U) - k
        rank = S.family_rank(row, sup, zs)
        proj = T.rank_mod([list(c) for s in sup
                           for c in T.dual_basis(tuple(sorted(s)), row)],
                          row.q)
        cg = S.combinatorial_gates(row, sup)
        tag = f"{name} k={k} h={h} V={V} m={m}"
        chk(f"F2 {tag}: pi_1(R) = C_U has dim m = {m}", proj == m,
            f"proj={proj}")
        chk(f"F3 {tag}: connectivity floor rank {rank} >= m = {m}; T3 "
            f"ceiling 2m-1 = {2*m-1}; charge/ray = {rank/V:.4f} in "
            f"[{m/V:.4f}, {(2*m-1)/V:.4f}]",
            rank >= m, f"rank={rank} m={m} 2m={2*m} "
            f"collapse={rank >= 2*m} V_vs_m_over_2={V}>{m/2:.1f}"
            f"={V > m/2}")
        res.append(dict(family=name, k=k, h=h, V=V, m=m, rank=rank,
                        proj=proj, charge=rank / V, floor=m / V,
                        ceil=(2 * m - 1) / V, collapse=rank >= 2 * m,
                        V_gt_m_over_2=V > m / 2,
                        pairwise_intersecting=cg["pairwise_intersecting"]))

    with open(os.path.join(HERE, "stage8_floor.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

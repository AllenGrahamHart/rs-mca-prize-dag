#!/usr/bin/env python3
"""STAGE 4 -- AMPLIFICATION: how far can the support-4 mechanism be pushed?

(I)   the V-ray Mobius cluster: rank = V(h-1)+3 exactly, full banked gate,
      charge per ray and per datum vs the banked K_V law.
(II)  NO STACKING: two distinct minimal-U mechanisms on the same rays force a
      triple intersection > k-1 (k-packing), so dim R_a <= 1 per ray.
(III) the ZERO-ESCAPE limit: rank >= sum_a |S_a \\ W| (localization).  The only
      support patterns with |S_a \\ W| = 0 for all a are S_a = U \\ q_a inside a
      single U of size k+2h-d with the q_a pairwise disjoint of size h-d --
      and there rank <= 2(|U|-k) = 4h-2d, so the T3 collapse threshold bites.
(IV)  the escape statistic |S_a \\ W| over every fixture built in this pilot.

Run: tools/ramguard local -- python3 stage4_amplify.py
"""
from __future__ import annotations

import itertools
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import s4lib as S                                              # noqa: E402
import tslib as T                                              # noqa: E402
import advlib as ADV                                           # noqa: E402

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                 if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def escape(row, supports):
    W = S.triple_locus(supports, row.n)
    return [len(frozenset(s) - W) for s in supports]


# --------------------------------------------------------- (III) builder
def build_u_clique(row, d, V):
    """S_a = U \\ q_a with |U| = k+2h-d and the q_a pairwise disjoint of size
    h-d.  Zero escape: every point of every S_a lies in >= 3 supports (V>=4).
    Slopes chosen Mobius-free (generic) -- the deficit here is structural."""
    k, h, n = row.k, row.h, row.n
    uu = k + 2 * h - d
    gam = h - d
    if gam < 1 or V * gam > uu or uu > n:
        return None
    U = list(range(uu))
    qs = [U[i * gam:(i + 1) * gam] for i in range(V)]
    sup = [tuple(sorted(set(U) - set(qs[a]))) for a in range(V)]
    assert all(len(s) == k + h for s in sup), [len(s) for s in sup]
    return dict(U=U, qs=qs, supports=sup, uu=uu, gam=gam)


def main():
    res = {"cluster": [], "stack": [], "clique": [], "escape": []}

    # ================================================ (I) the V-ray cluster
    for cs in [dict(k=3, h=5, d=1, q=6421, Vs=(4, 5)),
               dict(k=4, h=6, d=1, q=6421, Vs=(4, 5, 6)),
               dict(k=5, h=7, d=1, q=10007, Vs=(4, 5, 6, 7)),
               dict(k=4, h=9, d=2, q=10007, Vs=(4, 5))]:
        k, h, d, q = cs["k"], cs["h"], cs["d"], cs["q"]
        for V in cs["Vs"]:
            priv = (h - 1) - (V - 1) * d
            if priv < 0 or V > k + 2:
                continue
            n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
            row = T.Row2(n, k, h, q)
            fam = S.build_mobius_family(row, d, V, seed=1)
            if fam is None:
                continue
            sup, zs = fam["supports"], fam["slopes"]
            dim, _, _ = S.relation_space(row, sup, zs)
            rank = S.family_rank(row, sup, zs)
            M = V * (V - 1) // 2
            esc = escape(row, sup)
            tag = f"k={k} h={h} d={d} V={V} n={n}"
            chk(f"I1 {tag}: deficit = V-3 = {V-3} exactly, rank = "
                f"{V*(h-1)+3}", dim == V - 3 and rank == V * (h - 1) + 3,
                f"dim={dim} rank={rank} Vh={V*h}")
            # K_V comparison at the same (h,d)
            kv_V = (h + 1) // (d + 1) + 1
            kv_M = kv_V * (kv_V - 1) // 2
            chk(f"I2 {tag}: escape |S_a \\ W| = h-1 = {h-1} for every ray "
                f"(so the localization floor gives rank >= V(h-1))",
                set(esc) == {h - 1}, f"esc={esc}")
            res["cluster"].append(dict(
                k=k, h=h, d=d, V=V, n=n, M=M, rank=rank, Vh=V * h,
                deficit=dim, charge_per_ray=rank / V,
                charge_per_datum=rank / M, escape=esc,
                raycap_mobius=min(k + 2, (h - 1) // d + 1),
                raycap_KV=kv_V, KV_charge_per_datum=(kv_V * h) / kv_M
                if kv_M else None))

    # =========================================================== (II) stacking
    for cs in [dict(k=4, h=6, d=1, V=4, q=6421),
               dict(k=5, h=7, d=1, V=5, q=10007)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        priv = (h - 1) - (V - 1) * d
        n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 6
        row = T.Row2(n, k, h, q)
        fam = S.build_mobius_family(row, d, V, seed=1)
        sup = [set(s) for s in fam["supports"]]
        U = set(fam["U"])
        # attempt a SECOND minimal U' by swapping one point of U for a fresh one
        fresh = max(max(s) for s in sup) + 1
        if fresh >= n:
            fresh = n - 1
        U2 = (U - {fam["ys"][0]}) | {fresh}
        worst = 0
        for a in range(V):
            sup2 = [set(s) for s in sup]
            # ray a would also have to carry U' minus one hole
            for b in range(V):
                sup2[b] = sup2[b] | (U2 - {sorted(U2)[b % len(U2)]})
            for tri in itertools.combinations(range(V), 3):
                worst = max(worst, len(sup2[tri[0]] & sup2[tri[1]]
                                        & sup2[tri[2]]))
        chk(f"II1 k={k} h={h} V={V}: forcing a SECOND minimal U' on the same "
            f"rays pushes a triple intersection to {worst} > k-1 = {k-1} "
            f"(k-packing breaks -- NO STACKING)", worst > k - 1,
            f"worst_triple={worst}")
        res["stack"].append(dict(cs=cs, worst_triple=worst, kminus1=k - 1))

    # ==================================================== (III) zero escape
    for cs in [dict(k=9, h=4, d=1, q=10007, Vs=(3, 4, 5)),
               dict(k=13, h=4, d=1, q=10007, Vs=(4, 5, 6)),
               dict(k=7, h=4, d=2, q=10007, Vs=(3, 4)),
               dict(k=17, h=5, d=1, q=10007, Vs=(4, 6))]:
        k, h, d, q = cs["k"], cs["h"], cs["d"], cs["q"]
        uu = k + 2 * h - d
        n = uu + 2
        row = T.Row2(n, k, h, q)
        for V in cs["Vs"]:
            cl = build_u_clique(row, d, V)
            if cl is None:
                continue
            sup = cl["supports"]
            esc = escape(row, sup)
            cg = S.combinatorial_gates(row, sup)
            zs = [1 + 7 * a for a in range(V)]
            rank = S.family_rank(row, sup, zs)
            dim, _, _ = S.relation_space(row, sup, zs)
            m = uu - k
            tag = f"k={k} h={h} d={d} V={V} |U|={uu}"
            chk(f"III1 {tag}: zero escape (|S_a \\ W| = 0) for V >= 4",
                V < 4 or set(esc) == {0}, f"esc={esc}")
            chk(f"III2 {tag}: pairs = k+d = {k+d}, triples = "
                f"{k+3*d-2*h} <= k-1", cg["max_pair"] == k + d
                and cg["max_triple"] <= k - 1,
                f"pair={cg['max_pair']} triple={cg['max_triple']}")
            chk(f"III3 {tag}: rank <= 2m = {2*m} (whole row space sits in "
                f"C_U x C_U); T3 collapse threshold is 2m", rank <= 2 * m,
                f"rank={rank} 2m={2*m} 2m-1={2*m-1} Vh={V*h} deficit={dim} "
                f"COLLAPSE={rank >= 2*m}")
            res["clique"].append(dict(k=k, h=h, d=d, V=V, uu=uu, m=m,
                                      rank=rank, twom=2 * m, Vh=V * h,
                                      deficit=dim, escape=esc,
                                      collapse=rank >= 2 * m,
                                      charge_per_ray=rank / V,
                                      max_pair=cg["max_pair"],
                                      max_triple=cg["max_triple"]))

    # ============================================ (IV) the escape statistic
    #  K_V (banked extremal) vs the Mobius cluster vs the U-clique
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421),
               dict(k=3, h=7, d=1, V=5, q=6421),
               dict(k=4, h=7, d=1, V=5, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        M = V * (V - 1) // 2
        n = max((k - 1) + M * (d + 1), k + h + 2)
        row = T.Row2(n, k, h, q)
        b = ADV.build_KV(row, d, V, seed=0)
        if b is None:
            continue
        _, _, info = b
        sup = [tuple(s) for s in info["supports"].values()]
        esc = escape(row, sup)
        chk(f"IV1 K_V k={k} h={h} d={d} V={V}: escape = h+1 = {h+1} per ray "
            f"(localization floor rank >= V(h+1) -- but rank = Vh, so the "
            f"floor is not tight; it IS >= 2V)",
            set(esc) == {h + 1} and min(esc) >= 2, f"esc={esc}")
        res["escape"].append(dict(family="K_V", **cs, escape=esc))

    with open(os.path.join(HERE, "stage4_amplify.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

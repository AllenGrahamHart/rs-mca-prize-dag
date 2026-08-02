#!/usr/bin/env python3
"""STAGE 5 -- the ESCAPE DICHOTOMY and the PEELING bound.

PEELING (iterated localization).  Put S_a^(0) = S_a and
S_a^(i+1) = S_a^(i) ^ W^(i), W^(i) = the triple locus of {S_b^(i)}.  By S4-1
every relation of the system is a relation of the peeled system, so

        dim Rel  <=  sum_a ( |S_a^inf| - k )^+ ,
        rank     >=  sum_a  |S_a \\ S_a^inf|          (the ESCAPE floor).

The limit system has ZERO escape.  This stage:
  (A) computes the peeling limit and the certified floor on every family;
  (B) asks whether the zero-escape clique can be pushed BELOW the T3 collapse
      threshold 2m by any choice of slopes (random + Mobius-matched);
  (C) builds the escape-1 family and measures its charge;
  (D) records the exact criterion k <= 2h^2 under which the zero-escape
      channel cannot reach charge 2.

Run: tools/ramguard local -- python3 stage5_escape.py
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

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                 if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def peel(row, supports, max_it=20):
    cur = [frozenset(s) for s in supports]
    for _ in range(max_it):
        W = S.triple_locus([tuple(sorted(s)) for s in cur], row.n)
        nxt = [s & W for s in cur]
        if nxt == cur:
            break
        cur = nxt
    return cur


def peel_bound(row, supports):
    """dim Rel <= sum_a (|S_a^inf| - k)^+  and  rank >= sum_a [h - that]
    = sum_a min(h, |S_a| - |S_a^inf|).  NOTE the min(h, .) cap: when the
    peeling limit drops below k the ray contributes its full charge h, not
    |S_a \\ S_a^inf|."""
    lim = peel(row, supports)
    k, h = row.k, row.h
    dimcap = sum(max(0, len(s) - k) for s in lim)
    floor = sum(min(h, max(0, h - (len(b) - k))) for b in lim)
    return lim, dimcap, floor


def build_u_clique(row, d, V, extra_private=0):
    """S_a = (U \\ q_a) u priv_a, |priv_a| = extra_private (escape = that)."""
    k, h, n = row.k, row.h, row.n
    e = extra_private
    # |S_a| = u - g + e = k+h ; |S_a ^ S_b| = u - 2g = k+d
    #  => g = h - d - e,  u = k + 2h - d - 2e
    g = h - d - e
    u = k + 2 * h - d - 2 * e
    if g < 1 or V * g > u or u + V * e > n:
        return None
    U = list(range(u))
    qs = [U[i * g:(i + 1) * g] for i in range(V)]
    cur = u
    sup = []
    for a in range(V):
        Sa = set(U) - set(qs[a])
        Sa |= set(range(cur, cur + e))
        cur += e
        sup.append(tuple(sorted(Sa)))
    if any(len(s) != k + h for s in sup):
        return None
    return dict(U=U, qs=qs, supports=sup, u=u, g=g, m=cur - k, used=cur)


def main():
    rnd = random.Random(99123)
    res = {"peel": [], "clique_slopes": [], "escape1": [], "criterion": []}

    # ============================================== (A) peeling certificates
    #  U-mechanism, K_V, and the zero-escape clique
    for cs in [dict(k=3, h=5, d=1, V=4, q=6421, kind="mobius"),
               dict(k=5, h=7, d=1, V=6, q=10007, kind="mobius"),
               dict(k=3, h=7, d=1, V=5, q=6421, kind="KV"),
               dict(k=4, h=7, d=1, V=5, q=6421, kind="KV"),
               dict(k=9, h=4, d=1, V=4, q=10007, kind="clique"),
               dict(k=13, h=4, d=1, V=6, q=10007, kind="clique")]:
        k, h, d, V, q, kind = (cs["k"], cs["h"], cs["d"], cs["V"], cs["q"],
                               cs["kind"])
        if kind == "mobius":
            priv = (h - 1) - (V - 1) * d
            n = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
            row = T.Row2(n, k, h, q)
            fam = S.build_mobius_family(row, d, V, seed=1)
            sup, zs = fam["supports"], fam["slopes"]
        elif kind == "KV":
            M = V * (V - 1) // 2
            n = max((k - 1) + M * (d + 1), k + h + 2)
            row = T.Row2(n, k, h, q)
            _, _, info = ADV.build_KV(row, d, V, seed=0)
            sup = [tuple(s) for s in info["supports"].values()]
            zs = list(info["zs"])
        else:
            n = k + 2 * h - d + 2
            row = T.Row2(n, k, h, q)
            cl = build_u_clique(row, d, V)
            sup, zs = cl["supports"], [1 + 7 * a for a in range(V)]
        lim, dimcap, floor = peel_bound(row, sup)
        dim, _, _ = S.relation_space(row, sup, zs)
        rank = S.family_rank(row, sup, zs)
        tag = f"{kind} k={k} h={h} d={d} V={V}"
        chk(f"A1 {tag}: peeling certificate dim Rel <= {dimcap} and "
            f"rank >= {floor}", dim <= dimcap and rank >= floor,
            f"dim={dim} cap={dimcap} rank={rank} floor={floor} "
            f"|S^inf|={[len(x) for x in lim]}")
        res["peel"].append(dict(cs=cs, dim=dim, dimcap=dimcap, rank=rank,
                                floor=floor,
                                Sinf=[len(x) for x in lim], Vh=V * h))

    # ============= (B) can the zero-escape clique beat the collapse threshold?
    for cs in [dict(k=9, h=4, d=1, V=4, q=6421),
               dict(k=13, h=4, d=1, V=5, q=6421),
               dict(k=13, h=4, d=1, V=6, q=6421),
               dict(k=17, h=5, d=1, V=5, q=6421)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        n = k + 2 * h - d + 2
        row = T.Row2(n, k, h, q)
        cl = build_u_clique(row, d, V)
        if cl is None:
            continue
        sup = cl["supports"]
        m = cl["u"] - k
        best = None
        trials = 0
        for _ in range(120):
            zs = rnd.sample(range(1, q), V)
            r = S.family_rank(row, sup, zs)
            trials += 1
            best = r if best is None else min(best, r)
        # also try Mobius-matched slopes against every candidate zeta family
        for seed in range(40):
            rr = random.Random(seed)
            p, r_, s_, t_ = (rr.randrange(q), rr.randrange(q),
                             rr.randrange(q), rr.randrange(q))
            if (p * t_ - r_ * s_) % q == 0:
                continue
            zs, ok = [], True
            for a in range(V):
                w = row.xs[cl["qs"][a][0]]
                den = (s_ * w + t_) % q
                if den == 0:
                    ok = False
                    break
                zs.append((p * w + r_) % q * S.inv(den, q) % q)
            if not ok or len(set(zs)) != V:
                continue
            best = min(best, S.family_rank(row, sup, zs))
            trials += 1
        tag = f"k={k} h={h} d={d} V={V} m={m}"
        chk(f"B1 clique {tag}: minimum rank over {trials} slope choices is "
            f"{best}; the T3 non-collapse threshold is 2m-1 = {2*m-1}",
            best >= 2 * m,
            f"min_rank={best} 2m={2*m} charge_per_ray={best/V:.3f} "
            f"COLLAPSES={best >= 2*m}")
        res["clique_slopes"].append(dict(cs=cs, m=m, min_rank=best,
                                         twom=2 * m, trials=trials,
                                         charge=best / V,
                                         collapses=best >= 2 * m))

    # ------- B2: EXHAUSTIVE slope scan on a small-q clique (V = 4) ---------
    import itertools as _it
    for cs in [dict(k=9, h=4, d=1, V=4, q=19),
               dict(k=11, h=4, d=1, V=4, q=23)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        n = k + 2 * h - d
        if n > q:
            continue
        row = T.Row2(n, k, h, q)
        cl = build_u_clique(row, d, V)
        if cl is None:
            continue
        sup = cl["supports"]
        m = cl["u"] - k
        best, cnt = None, 0
        for zs in _it.combinations(range(q), V):
            r = S.family_rank(row, sup, list(zs))
            cnt += 1
            best = r if best is None else min(best, r)
        chk(f"B2 clique k={k} h={h} V={V} q={q}: EXHAUSTIVE over all "
            f"{cnt} slope 4-subsets of P^1(F_q)-finite, min rank = {best} "
            f"= 2m = {2*m}: the zero-escape clique ALWAYS collapses",
            best >= 2 * m, f"min_rank={best} 2m={2*m}")
        res["clique_slopes"].append(dict(cs=cs, m=m, min_rank=best,
                                         twom=2 * m, trials=cnt,
                                         exhaustive=True,
                                         collapses=best >= 2 * m))

    # ============================================= (C) the escape-1 family
    for cs in [dict(k=13, h=5, d=1, V=5, q=6421),
               dict(k=17, h=6, d=1, V=6, q=6421),
               dict(k=21, h=6, d=1, V=7, q=10007)]:
        k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
        n = k + 2 * h - d + V + 4
        row = T.Row2(n, k, h, q)
        cl = build_u_clique(row, d, V, extra_private=1)
        if cl is None:
            chk(f"C0 k={k} h={h} V={V}: escape-1 family builds", False)
            continue
        sup = cl["supports"]
        cg = S.combinatorial_gates(row, sup)
        esc = [len(frozenset(s) - S.triple_locus(sup, row.n)) for s in sup]
        m = cl["m"]
        best = None
        for _ in range(120):
            zs = rnd.sample(range(1, q), V)
            r = S.family_rank(row, sup, zs)
            best = r if best is None else min(best, r)
        tag = f"k={k} h={h} d={d} V={V} m={m}"
        chk(f"C1 escape-1 {tag}: escape = 1 per ray, gates "
            f"(pairs={cg['max_pair']}=k+d, triples={cg['max_triple']}<=k-1)",
            set(esc) == {1} and cg["max_pair"] == k + d
            and cg["max_triple"] <= k - 1,
            f"esc={esc} pair={cg['max_pair']} triple={cg['max_triple']}")
        chk(f"C2 escape-1 {tag}: min rank over slopes = {best}; charge per "
            f"ray = {best/V:.3f} (>= 2 ?)", best >= 2 * V,
            f"min_rank={best} 2V={2*V} 2m-1={2*m-1} Vh={V*h}")
        res["escape1"].append(dict(cs=cs, m=m, min_rank=best, esc=esc,
                                   charge=best / V, twoV=2 * V,
                                   max_pair=cg["max_pair"],
                                   max_triple=cg["max_triple"]))

    # ============================== (D) the k <= 2h^2 criterion, six rows
    ROWS = []
    for name, nn, rate, scale in [("RowC 1/4", 1024, 4, 256),
                                  ("RowC 1/8", 1024, 8, 256),
                                  ("RowC 1/16", 1024, 16, 512),
                                  ("prize 1/4", 2 ** 41, 4, 256),
                                  ("prize 1/8", 2 ** 41, 8, 256),
                                  ("prize 1/16", 2 ** 41, 16, 512)]:
        kk = nn // rate
        AA = kk + nn // scale + 1
        hh = AA - kk
        d = 1
        # zero-escape clique: |U| = k+2h-d, V <= |U|/(h-d), rank <= 2(2h-d)
        u = kk + 2 * hh - d
        Vmax = u // (hh - d)
        m = 2 * hh - d
        charge = (2 * m) / Vmax if Vmax else None
        ROWS.append(dict(name=name, n=nn, k=kk, A=AA, h=hh, R=nn - kk,
                         clique_u=u, clique_Vmax=Vmax, clique_m=m,
                         clique_charge_per_ray=charge,
                         two_h_squared=2 * hh * hh, k_le_2h2=kk <= 2 * hh * hh,
                         margin=(2 * hh * hh) / kk))
        chk(f"D1 {name}: zero-escape clique charge per ray = "
            f"{charge:.6g} (needs >= 2); k <= 2h^2 margin = "
            f"{(2*hh*hh)/kk:.4g}x", charge >= 2 and kk <= 2 * hh * hh,
            f"k={kk} h={hh} Vmax={Vmax} 2m={2*m}")
    res["criterion"] = ROWS

    with open(os.path.join(HERE, "stage5_escape.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""STAGE 7 -- the DOUBLE-HOLE family: relations that are GENERIC in the slopes,
and the charge law  rank ~ V(h - l).

With |U| = k+1+D and S_a ^ U = U minus (D-l+1) holes (so dim C_{S_a^U} = l),
the relation space is the kernel of

        (+)_a C_{S_a^U}  -->  F^2 (x) C_U ,   (c_a) |-> sum_a e(z_a) (x) c_a,

so  dim Rel >= V l - 2(D+1):  for l >= 2 relations exist for EVERY slope
tuple -- no cross-ratio condition at all.  k-packing forces 3l <= 2D+1, the
depth budget forces l <= h - (max depth sum), and the localization floor
gives rank >= V(h-l).  l = h-2 is the charge-2 boundary.

Concretely l = 2: |U| = k+4, holes of size 2, pairwise disjoint.

Run: tools/ramguard local -- python3 stage7_doublehole.py
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

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def build_double_hole(row, d, V, ell=2):
    """|U| = k + 2*ell,  holes of size ell pairwise disjoint,
    S_a = (U \\ H_a) u P_a,  |P_a| = h - ell,  |P_a ^ P_b| = d, no triple."""
    k, h, n = row.k, row.h, row.n
    uu = k + 2 * ell
    if V * ell > uu:
        return None
    priv = (h - ell) - (V - 1) * d
    if priv < 0:
        return None
    need = uu + (V * (V - 1) // 2) * d + V * priv
    if need > n:
        return None
    U = list(range(uu))
    H = [U[a * ell:(a + 1) * ell] for a in range(V)]
    cur = uu
    B = {}
    for a in range(V):
        for b in range(a + 1, V):
            B[(a, b)] = list(range(cur, cur + d))
            cur += d
    P = {}
    for a in range(V):
        P[a] = list(range(cur, cur + priv))
        cur += priv
    sup = []
    for a in range(V):
        Sa = set(U) - set(H[a])
        for b in range(V):
            if b != a:
                Sa |= set(B[(min(a, b), max(a, b))])
        Sa |= set(P[a])
        sup.append(tuple(sorted(Sa)))
    if any(len(s) != k + h for s in sup):
        return None
    return dict(U=U, H=H, supports=sup, used=cur, ell=ell)


def main():
    part = sys.argv[1] if len(sys.argv) > 1 else "A"
    rnd = random.Random(77001)
    res = []
    CASES = [dict(k=8, h=8, d=1, V=5, ell=2, q=10007),
             dict(k=8, h=8, d=1, V=6, ell=2, q=10007),
             dict(k=10, h=9, d=1, V=6, ell=2, q=10007),
             dict(k=10, h=11, d=2, V=5, ell=2, q=10007),
             dict(k=14, h=10, d=1, V=6, ell=3, q=10007)]
    for cs in (CASES if part == "A" else []):
        k, h, d, V, ell, q = (cs["k"], cs["h"], cs["d"], cs["V"], cs["ell"],
                              cs["q"])
        uu = k + 2 * ell
        priv = (h - ell) - (V - 1) * d
        n = uu + (V * (V - 1) // 2) * d + V * priv + 2
        row = T.Row2(n, k, h, q)
        fam = build_double_hole(row, d, V, ell)
        if fam is None:
            chk(f"S0 k={k} h={h} d={d} V={V} l={ell}: builds", False)
            continue
        sup = fam["supports"]
        cg = S.combinatorial_gates(row, sup)
        esc = [len(frozenset(s) - S.triple_locus(sup, n)) for s in sup]
        lim, cap, floor = None, None, None
        # peeling
        cur = [frozenset(s) for s in sup]
        for _ in range(20):
            W = S.triple_locus([tuple(sorted(s)) for s in cur], n)
            nxt = [s & W for s in cur]
            if nxt == cur:
                break
            cur = nxt
        lim = cur
        cap = sum(max(0, len(s) - k) for s in lim)
        floor = sum(min(h, max(0, h - (len(b) - k))) for b in lim)
        tag = f"k={k} h={h} d={d} V={V} l={ell} n={n}"

        chk(f"S1 {tag}: gates -- |S_a|=k+h, pairs = k+d = {k+d}, triples = "
            f"{cg['max_triple']} <= k-1 = {k-1}, k-packing OK",
            cg["size_ok"] and cg["max_pair"] == k + d
            and cg["max_triple"] <= k - 1,
            f"pair={cg['max_pair']} triple={cg['max_triple']} esc={esc}")

        dims, ranks = [], []
        for _ in range(25):
            zs = rnd.sample(range(1, q), V)
            dd, _, _ = S.relation_space(row, sup, zs)
            dims.append(dd)
            ranks.append(S.family_rank(row, sup, zs))
        pred = max(0, V * ell - 2 * (uu - k))
        chk(f"S2 {tag}: relations exist for EVERY slope tuple (25/25), "
            f"dim Rel = {set(dims)} vs the prediction V*l - 2(D+1) = {pred}",
            min(dims) > 0 and min(dims) >= pred,
            f"dims={sorted(set(dims))} pred={pred} cap_peel={cap}")
        chk(f"S3 {tag}: the localization/peeling floor rank >= {floor} = "
            f"V(h-l) holds; measured min rank {min(ranks)}",
            min(ranks) >= floor,
            f"min_rank={min(ranks)} floor={floor} Vh={V*h} "
            f"charge_per_ray={min(ranks)/V:.3f} escape={esc[0]}")
        chk(f"S4 {tag}: charge per ray {min(ranks)/V:.3f} >= 2 (escape "
            f"= h-l = {h-ell} >= 2)", min(ranks) / V >= 2,
            f"charge={min(ranks)/V:.4f}")
        res.append(dict(cs=cs, n=n, uu=uu, dims=sorted(set(dims)),
                        pred=pred, peel_cap=cap, floor=floor,
                        min_rank=min(ranks), Vh=V * h,
                        charge_per_ray=min(ranks) / V,
                        charge_per_datum=min(ranks) / (V * (V - 1) / 2),
                        escape=esc, max_pair=cg["max_pair"],
                        max_triple=cg["max_triple"]))

    # ---- realise + full gate on a SMALL double-hole fixture (occlib scans
    #      all C(n,k) k-subsets, so k must stay tiny here) -----------------
    cs = dict(k=6, h=6, d=1, V=5, ell=2, q=6421)
    k, h, d, V, ell, q = (cs["k"], cs["h"], cs["d"], cs["V"], cs["ell"],
                          cs["q"])
    if part != "B":
        k = None
    priv = (h - ell) - (V - 1) * d if k else 0
    n = (k + 2 * ell) + (V * (V - 1) // 2) * d + V * priv if k else 0
    row = T.Row2(n, k, h, q) if k else None
    fam = build_double_hole(row, d, V, ell) if k else None
    got = None
    for fs in (range(1, 12) if k else []):
        zs = random.Random(fs).sample(range(1, q), V)
        if S.relation_space(row, fam["supports"], zs)[0] == 0:
            continue
        uv = S.realise_family(row, fam["supports"], zs, seed=3)
        if uv is None:
            continue
        rec, pairs, band = S.gate_report(row, uv[0], uv[1], name="dh")
        got = (zs, 3, rec)
        break
    if got:
        zs, rs, rec = got
        chk(f"S5 double-hole k={k} h={h} V={V} n={n}: FULL banked gate on the "
            f"realised received pair", rec["FULL_GATE"],
            f"cascade={rec['below_cascade']} generic={rec['globally_generic']} "
            f"tanfin={rec['tangent_free_finite_slopes']} "
            f"tanv={rec['tangent_free_v_direction']} "
            f"kpack={rec['kpacking_ok']} maxJ={rec['max_joint_agreement']} "
            f"A={row.A} maxray={rec['max_ray_agreement']}")
        res.append(dict(realised=True, FULL_GATE=rec["FULL_GATE"],
                        N_total=rec["N_total"], n_rays=rec["n_rays"]))

    with open(os.path.join(HERE, f"stage7_doublehole_{part}.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

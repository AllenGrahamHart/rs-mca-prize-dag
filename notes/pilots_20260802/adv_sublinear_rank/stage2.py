#!/usr/bin/env python3
"""STAGE 2 -- SPREAD-V: does the RAY COUNT V grow with n?

If V is capped by ~h/(d+1) (the K_V / common-Y cap) then N_d is LINEAR.
If V grows with n then N_d = C(V,2) is QUADRATIC and the "sublinear rank"
class is inhabited: rank = V h = Theta(sqrt(M) h).

Run: tools/ramguard local -- python3 stage2.py
"""
from __future__ import annotations

import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import advlib as _A                                           # noqa: E402,F401
import spread as SP                                           # noqa: E402
import tslib as T                                             # noqa: E402,F401
import occlib                                                 # noqa: E402

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


# (k, h, d, V, q).  h >= 4d+2 makes rank = Vh <= 2m-1 automatic.
LADDER = [
    dict(k=3, h=6, d=1, V=3, q=6421),
    dict(k=5, h=6, d=1, V=4, q=6421),
    dict(k=7, h=6, d=1, V=5, q=6421),
    dict(k=9, h=6, d=1, V=6, q=6421),
    dict(k=11, h=6, d=1, V=7, q=6421),
    dict(k=15, h=6, d=1, V=9, q=10007),
    dict(k=21, h=6, d=1, V=12, q=10007),
    dict(k=31, h=6, d=1, V=17, q=10007),
    dict(k=41, h=6, d=1, V=22, q=10007),
    dict(k=61, h=6, d=1, V=32, q=10007),
    # bigger h (K_V cap would be (h+1)/(d+1)+1 = 5.5 at h=8, 6.5 at h=10)
    dict(k=9, h=8, d=1, V=6, q=10007),
    dict(k=21, h=8, d=1, V=12, q=10007),
    dict(k=41, h=10, d=1, V=22, q=10007),
    # d = 2 (needs h >= 6; use h >= 4d+2 = 10)
    dict(k=10, h=10, d=2, V=4, q=10007),
    dict(k=22, h=10, d=2, V=8, q=10007),
    dict(k=40, h=12, d=2, V=14, q=10007),
    # d = 3
    dict(k=30, h=14, d=3, V=8, q=10007),
]


def main():
    res = []
    for cs in LADDER:
        L = SP.layout(cs["k"], cs["h"], cs["d"], cs["V"])
        if L is None:
            print(f"SKIP (budget) {cs}")
            continue
        cb = SP.combinatorics_ok(L)
        tag = (f"k={cs['k']} h={cs['h']} d={cs['d']} V={cs['V']} "
               f"n={L['n']}")
        ok1 = chk(f"S2 {tag}: |S_a| = A for all rays", cb["sizes_ok"])
        ok2 = chk(f"S2 {tag}: all pairwise |S_a^S_b| = k+d = {cs['k']+cs['d']}"
                  f", all DISTINCT",
                  cb["pair_ok"] and cb["pairs_distinct"],
                  f"pair_sizes={cb['pair_sizes']}")
        ok3 = chk(f"S2 {tag}: all triple |S_a^S_b^S_c| <= k-1 (k-packing)",
                  cb["triple_ok"], f"triple_sizes={cb['triple_sizes']}")
        ok4 = chk(f"S2 {tag}: m = |T|-k = 3d+2+V(h-2d-1) = {cb['m_pred']}",
                  cb["m_ok"], f"m={cb['m']}")
        b = SP.build(L, cs["q"], seed=1)
        if b is None:
            chk(f"S2 {tag}: realisation found", False, "no non-codeword sol")
            continue
        row, u, v, zs, rk = b
        rep, cores = SP.verify_data(row, u, v, L, zs)
        chk(f"S2 {tag}: ray system rank == V*h = {cs['V']*cs['h']}",
            rk == cs["V"] * cs["h"], f"rank={rk}")
        chk(f"S2 {tag}: realisable, rank <= 2m-1 = {2*cb['m']-1}",
            rk <= 2 * cb["m"] - 1, f"rank={rk} 2R-1={2*row.R-1}")
        chk(f"S2 {tag}: every ray support recovered EXACTLY (|S|=A)",
            rep["ray_support_exact"], f"sizes={rep['ray_sizes']} A={rep['A']}")
        chk(f"S2 {tag}: M = C(V,2) = {rep['M_pred']} data, ALL DISTINCT pairs",
            rep["M"] == rep["M_pred"]
            and rep["distinct_pairs"] == rep["M_pred"],
            f"M={rep['M']} distinct={rep['distinct_pairs']}")
        chk(f"S2 {tag}: every datum at depth EXACTLY d={cs['d']}",
            rep["depth_exact"], f"bad={rep['bad_depth']}")
        chk(f"S2 {tag}: cores k-packed", rep["kpacking_ok"],
            f"max|Z^Z'|={rep['kpacking_max']} <= k-1={cs['k']-1}")
        chk(f"S2 {tag}: family rank == V*h (per-RAY charge h)",
            rep["family_rank"] == rep["pred_rank"],
            f"rank={rep['family_rank']} Vh={rep['pred_rank']} "
            f"generic 2hM={2*cs['h']*rep['M']}")
        cost = rep["cost_per_datum"]
        chk(f"S2 {tag}: cost/datum = {cost:.4f} (sunflower h={cs['h']})",
            cost < cs["h"] if cs["V"] > 3 else True,
            f"= 2h/(V-1) = {2*cs['h']/(cs['V']-1):.4f}")
        res.append(dict(cs=cs, n=L["n"], R=row.R, m=cb["m"], rank=rk,
                        M=rep["M"], cost=cost, Vh=cs["V"] * cs["h"],
                        two_R_minus_1=rep["two_R_minus_1"],
                        sharp_occ_law=(row.R + 1) // (cs["h"] - cs["d"]),
                        n_over_2=row.n // 2,
                        beats_sharp_occ=rep["M"] > (row.R + 1) //
                        (cs["h"] - cs["d"]),
                        ray_support_exact=rep["ray_support_exact"],
                        depth_exact=rep["depth_exact"],
                        kpacking_ok=rep["kpacking_ok"]))
        del ok1, ok2, ok3, ok4

    # ---- full gates (exhaustive occlib) at the feasible sizes -----------
    print("\n=== full-gate (exhaustive occlib) verification ===")
    gates = []
    for cs in LADDER:
        L = SP.layout(cs["k"], cs["h"], cs["d"], cs["V"])
        if L is None:
            continue
        from math import comb
        if comb(L["n"], cs["k"]) > 60000:
            continue
        b = SP.build(L, cs["q"], seed=1)
        if b is None:
            continue
        row, u, v, zs, rk = b
        rec, pairs, band = occlib.measure(row, u, v, name="spread",
                                          want_checks=True)
        Nd = rec["ledger_by_depth"].get(str(cs["d"]), {}).get("N_d", 0)
        tag = (f"k={cs['k']} h={cs['h']} d={cs['d']} V={cs['V']} n={L['n']}")
        chk(f"S2-GATE {tag}: ADMISSIBLE", rec["ADMISSIBLE"],
            f"cascade={rec['below_cascade']}(maxJ={rec['max_joint_agreement']}"
            f"<=A-2={row.A-2}) tangent={rec['tangent_free_finite_slopes']}"
            f"(maxray={rec['max_ray_agreement']}<=A={row.A}) "
            f"vnz={rec['v_nonvanishing']}")
        chk(f"S2-GATE {tag}: measured N_d >= C(V,2) = "
            f"{cs['V']*(cs['V']-1)//2}",
            Nd >= cs["V"] * (cs["V"] - 1) // 2, f"N_d={Nd}")
        gates.append(dict(cs=cs, n=L["n"], ADMISSIBLE=rec["ADMISSIBLE"],
                          N_d=Nd, maxJ=rec["max_joint_agreement"],
                          maxray=rec["max_ray_agreement"], A=row.A,
                          kpacking_ok=rec["kpacking_ok"],
                          T1_ok=rec["T1_ok"],
                          N_total=rec["N_total"]))

    with open(os.path.join(HERE, "stage2.json"), "w") as fh:
        json.dump(dict(ladder=res, gates=gates), fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

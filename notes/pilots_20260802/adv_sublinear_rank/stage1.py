#!/usr/bin/env python3
"""STAGE 1 -- the K_V (complete-graph-of-rays) family, exactly measured.

Prediction under the RAY-CHARGE reformulation:
    rank(family)  =  V h        (V rays, h fresh conditions each)
    M             =  C(V,2)     (one datum per PAIR of rays)
    cost/datum    =  2h/(V-1)   ->  2(d+1)   as V -> (h+1)/(d+1)+1

The banked claim under attack: "cheapest admissible family anywhere = the
sunflower at exactly h; nothing below h" and SHARP-OCC's
N_d <= floor((R+1)/(h-d)).

Run: tools/ramguard local -- python3 stage1.py
"""
from __future__ import annotations

import json
import os
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


# (n, k, t=h, q, d, V)  with (V-1)(d+1) <= h+1 and (k-1)+C(V,2)(d+1)+V*tau<=n
CASES = [
    # d = 1 ladder: h = 2V-3 makes tau = 0 (no top-up needed)
    dict(k=3, h=3, d=1, V=3, q=6421),      # V=3: K_3 == the triangle sunflower
    dict(k=3, h=5, d=1, V=4, q=6421),      # M=6,  predicted cost 10/3
    dict(k=3, h=7, d=1, V=5, q=6421),      # M=10, predicted cost 14/4
    dict(k=3, h=9, d=1, V=6, q=10007),     # M=15, predicted cost 18/5
    dict(k=3, h=11, d=1, V=7, q=10007),    # M=21, predicted cost 22/6
    # h fixed, V varying (top-up tau > 0): shows the cost falling with V
    dict(k=3, h=9, d=1, V=3, q=10007),
    dict(k=3, h=9, d=1, V=4, q=10007),
    dict(k=3, h=9, d=1, V=5, q=10007),
    # d = 2 and d = 3
    dict(k=3, h=8, d=2, V=4, q=10007),     # M=6,  predicted cost 16/3
    dict(k=3, h=11, d=2, V=5, q=10007),    # M=10, predicted cost 22/4
    dict(k=3, h=11, d=3, V=4, q=10007),    # M=6,  predicted cost 22/3
    # larger k
    dict(k=4, h=7, d=1, V=5, q=6421),
    dict(k=5, h=5, d=1, V=4, q=6421),
]


def run_case(cs, seeds=8):
    k, h, d, V, q = cs["k"], cs["h"], cs["d"], cs["V"], cs["q"]
    M = V * (V - 1) // 2
    tau = (h + 1) - (V - 1) * (d + 1)
    if tau < 0:
        return None
    n = (k - 1) + M * (d + 1) + V * tau
    n = max(n, k + h + 2)
    row = T.Row2(n, k, h, q)
    R = row.R
    out = None
    for seed in range(seeds):
        b = A.build_KV(row, d, V, seed=seed)
        if b is None:
            continue
        u, v, info = b
        rec, pairs, band = occlib.measure(row, u, v,
                                          name=f"KV k={k} h={h} d={d} V={V}",
                                          want_checks=True)
        fam = A.measured_family(row, band, d)
        rk2 = A.family_rank_two_rays(row, fam) if fam else 0
        rkA = A.family_rank_all_rays(row, fam) if fam else 0
        drk = A.designed_rank(row, info)
        rrk = A.ray_only_rank(row, info)
        Nd = rec["ledger_by_depth"].get(str(d), {}).get("N_d", 0)
        out = dict(n=n, k=k, h=h, d=d, V=V, q=q, R=R, A=row.A, M_design=M,
                   tau=tau, seed=seed,
                   ADMISSIBLE=rec["ADMISSIBLE"],
                   below_cascade=rec["below_cascade"],
                   tangent_free=rec["tangent_free_finite_slopes"],
                   v_nonvanishing=rec["v_nonvanishing"],
                   kpacking_ok=rec["kpacking_ok"],
                   T1_ok=rec["T1_ok"], T3_ok=rec.get("T3_ok"),
                   max_joint=rec["max_joint_agreement"],
                   max_ray=rec["max_ray_agreement"],
                   max_v_side=rec["max_v_side_agreement"],
                   N_d=Nd, M_measured=len(fam),
                   rank_two_ray=rk2, rank_all_ray=rkA,
                   rank_designed=drk, rank_rays_only=rrk,
                   cost_two_ray=(rk2 / len(fam)) if fam else None,
                   cost_designed=(drk / M) if M else None,
                   pred_rank=V * h, pred_cost=2 * h / (V - 1),
                   sunflower_law=(R + 1) // (h - d) if h > d else None,
                   two_R_minus_1=2 * R - 1,
                   points_used=info["points_used"],
                   extra_rich=info["extra_rich"][:6])
        if rec["ADMISSIBLE"]:
            break
    return out


def main():
    res = []
    for cs in CASES:
        r = run_case(cs)
        if r is None:
            print(f"SKIP {cs}")
            continue
        res.append(r)
        tag = (f"k={r['k']} h={r['h']} d={r['d']} V={r['V']} n={r['n']} "
               f"R={r['R']}")
        chk(f"S1 {tag}: fixture ADMISSIBLE", r["ADMISSIBLE"],
            f"cascade={r['below_cascade']} tangent={r['tangent_free']} "
            f"vnz={r['v_nonvanishing']} maxJ={r['max_joint']}<=A-2="
            f"{r['A']-2} maxray={r['max_ray']}<=A={r['A']}")
        chk(f"S1 {tag}: k-packing holds", r["kpacking_ok"])
        chk(f"S1 {tag}: N_d = C(V,2) = {r['M_design']}",
            r["N_d"] == r["M_design"],
            f"N_d={r['N_d']} M_measured={r['M_measured']}")
        chk(f"S1 {tag}: designed rank == V*h = {r['pred_rank']}",
            r["rank_designed"] == r["pred_rank"],
            f"designed={r['rank_designed']} rays_only={r['rank_rays_only']}")
        chk(f"S1 {tag}: measured two-slope family rank == V*h",
            r["rank_two_ray"] == r["pred_rank"],
            f"rank={r['rank_two_ray']} vs V*h={r['pred_rank']} "
            f"(generic 2hM={2*r['h']*r['M_design']})")
        c = r["cost_two_ray"]
        chk(f"S1 {tag}: cost/datum {c} BELOW the sunflower's h={r['h']}",
            c is not None and c < r["h"] - 1e-9 if r["V"] > 3 else True,
            f"cost={c} pred={r['pred_cost']:.4f} h={r['h']}")
        chk(f"S1 {tag}: N_d BEATS SHARP-OCC law floor((R+1)/(h-d))"
            f"={r['sunflower_law']}",
            r["N_d"] > (r["sunflower_law"] or 0) if r["V"] > 3 else True,
            f"N_d={r['N_d']} law={r['sunflower_law']}")
        chk(f"S1 {tag}: family realisable (rank <= 2R-1)",
            r["rank_two_ray"] <= r["two_R_minus_1"],
            f"{r['rank_two_ray']} <= {r['two_R_minus_1']}")
    with open(os.path.join(HERE, "stage1.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

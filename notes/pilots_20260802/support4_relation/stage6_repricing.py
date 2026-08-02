#!/usr/bin/env python3
"""STAGE 6 -- exact RE-PRICING of the design ceiling under the support-4
(U-mechanism) adversary, at the six banked rows.

THE MECHANISM'S EXACT BUDGET (all verified at toy scale in stages 1/3/4):

    U          : one common set of size k+2 (shared by every cluster;
                 paid once, exactly as the banked K_V shares its Y)
    ray a      : S_a = (U \\ {y_a}) u (V-1 pair blocks of size d) u priv_a,
                 |priv_a| = (h-1) - (V-1)d  >= 0        [RAYCAP]
    per cluster: rank    = V(h-1) + 3          (deficit V-3, PROVED exact)
                 points  = V(h-1) - C(V,2) d
                 data    = C(V,2)
    RAYCAP     : V <= min(k+2, (h-1)//d + 1)
    across clusters sharing U: sum_i V_i <= k+2 (holes must be distinct, else
                 k-packing breaks)

    budgets    : sum_i rank_i <= 2R-1 (RS_k x RS_k in every kernel)
                 (k+2) + sum_i points_i <= n   i.e.  sum_i points_i <= R-2

Compared against the banked K_V law (adv_sublinear_rank/arith_repricing.py):
    rank = Vh, points = C(V,2)(d+1) + V*tau, tau = h+1-(V-1)(d+1),
    V <= (h+1)//(d+1) + 1, budgets 2R-1 and R+1.

Run: tools/ramguard local -- python3 stage6_repricing.py
"""
from __future__ import annotations

import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

CHECKS, FAIL = [0], []


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


ROWS = []
for name, n, rate, scale in [("RowC 1/4", 1024, 4, 256),
                             ("RowC 1/8", 1024, 8, 256),
                             ("RowC 1/16", 1024, 16, 512),
                             ("prize 1/4", 2 ** 41, 4, 256),
                             ("prize 1/8", 2 ** 41, 8, 256),
                             ("prize 1/16", 2 ** 41, 16, 512)]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append(dict(name=name, n=n, k=k, A=A, h=A - k, R=n - k))

BANKED_KV_N1 = {"prize 1/4": 18336, "prize 1/8": 24976, "prize 1/16": 114960}


def u_yield(n, k, R, h, d, V):
    if V < 3 or V > k + 2:
        return None
    priv = (h - 1) - (V - 1) * d
    if priv < 0:
        return None
    C2 = V * (V - 1) // 2
    rk = V * (h - 1) + 3
    pts = V * (h - 1) - C2 * d
    if pts <= 0 or rk <= 0:
        return None
    ncl = min((2 * R - 1) // rk, (R - 2) // pts, (k + 2) // V)
    return ncl * C2, ncl, pts, rk


def kv_yield(R, h, d, V):
    tau = (h + 1) - (V - 1) * (d + 1)
    if tau < 0:
        return None
    C2 = V * (V - 1) // 2
    pts = C2 * (d + 1) + V * tau
    rk = V * h
    ncl = min((2 * R - 1) // rk, (R + 1) // pts)
    return ncl * C2, ncl, pts, rk


def best(fn, args, cap):
    """Scan V coarse-to-fine (the yields are unimodal in V)."""
    bestv = (0, 3, None)
    Vs, x = set(), 3
    while x <= cap:
        Vs.add(x)
        x = max(x + 1, x * 3 // 2)
    Vs.add(cap)
    for V in sorted(Vs):
        y = fn(*args, V)
        if y and y[0] > bestv[0]:
            bestv = (y[0], V, y)
    c = bestv[1]
    for V in range(max(3, c - 600), min(cap, c + 600) + 1):
        y = fn(*args, V)
        if y and y[0] > bestv[0]:
            bestv = (y[0], V, y)
    return bestv


def main():
    out = []
    for r in ROWS:
        n, k, h, R = r["n"], r["k"], r["h"], r["R"]
        rec = dict(r)
        # sufficient per-ray floor: N_d <= C(V,2) with V <= (2R-1)/rho and
        # the ratified requirement N_d <= 0.68 n^2
        rec["rho_sufficient"] = (2 * R - 1) / (n * (2 * 0.68) ** 0.5)
        for d in (1, 2, 3):
            capU = min(k + 2, (h - 1) // d + 1)
            capK = (h + 1) // (d + 1) + 1
            NU, VU, yU = best(u_yield, (n, k, R, h, d), capU)
            NK, VK, yK = best(kv_yield, (R, h, d), capK)
            rec[f"d{d}"] = dict(
                U_N=NU, U_V=VU, U_clusters=yU[1] if yU else None,
                U_points=yU[2] if yU else None, U_rank=yU[3] if yU else None,
                U_charge_per_ray=(yU[3] / VU) if yU else None,
                U_charge_per_datum=(yU[3] / (VU * (VU - 1) / 2)) if yU else None,
                KV_N=NK, KV_V=VK,
                KV_charge_per_ray=h,
                ratio_U_over_KV=(NU / NK) if NK else None,
                raycap_U=capU, raycap_KV=capK)
        out.append(rec)

    for rec in out:
        nm, n, h = rec["name"], rec["n"], rec["h"]
        d1 = rec["d1"]
        chk(f"R1 {nm}: the support-4 (U) adversary's N_1 = {d1['U_N']} vs the "
            f"banked K_V N_1 = {d1['KV_N']} (ratio "
            f"{d1['ratio_U_over_KV']:.6f})",
            d1["U_N"] <= 1.02 * d1["KV_N"],
            f"V_U={d1['U_V']} V_KV={d1['KV_V']} clusters={d1['U_clusters']}")
        chk(f"R2 {nm}: per-ray charge of the mechanism = "
            f"{d1['U_charge_per_ray']:.6g} >= h-1 = {h-1}, vs the sufficient "
            f"floor rho = {rec['rho_sufficient']:.4f} -- margin "
            f"{d1['U_charge_per_ray']/rec['rho_sufficient']:.4g}x",
            d1["U_charge_per_ray"] >= rec["rho_sufficient"],
            f"charge={d1['U_charge_per_ray']:.6g}")
        chk(f"R3 {nm}: N_1 stays inside the ratified 0.68 n^2 = "
            f"{0.68*n*n:.4g} (margin {0.68*n*n/max(d1['U_N'],1):.4g}x)",
            d1["U_N"] <= 0.68 * n * n, f"N_1={d1['U_N']}")
        chk(f"R4 {nm}: SHARP-OCC weak form N_1 <= n/2 = {n//2} survives the "
            f"support-4 adversary", d1["U_N"] <= n // 2,
            f"N_1={d1['U_N']}")

    for nm, val in BANKED_KV_N1.items():
        rec = next(r for r in out if r["name"] == nm)
        chk(f"R5 {nm}: the banked K_V N_1 = {val} is reproduced exactly",
            rec["d1"]["KV_N"] == val, f"got={rec['d1']['KV_N']}")

    with open(os.path.join(HERE, "stage6_repricing.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

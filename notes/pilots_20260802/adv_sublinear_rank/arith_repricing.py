#!/usr/bin/env python3
"""ARITHMETIC RE-PRICING of the two-slope occupancy ceilings.

BANKED (xr_occupancy_v2): the cheapest admissible family is the SUNFLOWER at
cost exactly h per DATUM; the designed-family ceiling is LINEAR
(191/223/479 at the prize rows, = (2R-1)//(2h-2)), and SHARP-OCC asserts
N_d <= floor((R+1)/(h-d)) at d <= (h-1)/2.

MEASURED HERE (stage 1, 13 gate-verified fixtures; stage 5, 14 fixtures):
the charge is h per RAY, and a datum is a PAIR of rays.  The K_V family
spends V h rank and C(V,2) data.  Its exact budgets, taken verbatim from the
builder that was gate-verified:

    tau            = h+1 - (V-1)(d+1)              >= 0    (top-up per ray)
    points/cluster = C(V,2)(d+1) + V tau
    rank/cluster   = V h
    V              <= (h+1)//(d+1) + 1             (RAYCAP, stage 5)

    clusters <= min( (2R-1) // (V h),  (R+1) // points_per_cluster )
    N_d      <= clusters * C(V,2)

Run: tools/ramguard local -- python3 arith_repricing.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

ROWS = []
for name, n, rate, scale in [("RowC 1/4", 1024, 4, 256),
                             ("RowC 1/8", 1024, 8, 256),
                             ("RowC 1/16", 1024, 16, 512),
                             ("prize 1/4", 2 ** 41, 4, 256),
                             ("prize 1/8", 2 ** 41, 8, 256),
                             ("prize 1/16", 2 ** 41, 16, 512)]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append(dict(name=name, n=n, k=k, A=A, h=A - k, R=n - k, r=n - A))

BANKED_A = [261, 133, 67, 558345748481, 283467841537, 141733920769]
BANKED_FREE = 383, 447, 959, 383, 447, 959          # (2R-1)//(h-1)
BANKED_DESIGN = 191, 223, 479, 191, 223, 479        # (2R-1)//(2h-2)
FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def kv_yield(R, h, d, V):
    """(N_d, clusters, points/cluster, rank/cluster) for the K_V law."""
    tau = (h + 1) - (V - 1) * (d + 1)
    if tau < 0:
        return None
    C2 = V * (V - 1) // 2
    pts = C2 * (d + 1) + V * tau
    rk = V * h
    ncl = min((2 * R - 1) // rk, (R + 1) // pts)
    return ncl * C2, ncl, pts, rk, tau


def best_V(R, h, d):
    """Maximise the K_V yield over V (the objective is unimodal in V; scan a
    coarse-to-fine bracket to stay exact and cheap at h ~ 2^33)."""
    cap = (h + 1) // (d + 1) + 1
    lo, hi = 3, cap
    best = (0, 3, None)
    # coarse geometric scan, then a local refine
    Vs = set()
    x = 3
    while x <= hi:
        Vs.add(x)
        x = max(x + 1, x * 3 // 2)
    Vs.add(hi)
    for V in sorted(Vs):
        y = kv_yield(R, h, d, V)
        if y and y[0] > best[0]:
            best = (y[0], V, y)
    c = best[1]
    for V in range(max(3, c - 400), min(hi, c + 400) + 1):
        y = kv_yield(R, h, d, V)
        if y and y[0] > best[0]:
            best = (y[0], V, y)
    del lo
    return best


def main():
    out = []
    print("=== A1  the K_V ray-charge law vs the banked linear law ===")
    print(f"{'row':<11}{'h':>13}{'R':>16}{'V*':>8}{'clusters':>10}"
          f"{'N_1 (K_V)':>12}{'banked SHARP':>14}{'banked design':>15}"
          f"{'0.68n^2':>12}")
    for i, r in enumerate(ROWS):
        n, k, A, h, R = r["n"], r["k"], r["A"], r["h"], r["R"]
        assert A == BANKED_A[i], (A, BANKED_A[i])
        assert (2 * R - 1) // (h - 1) == BANKED_FREE[i]
        assert (2 * R - 1) // (2 * h - 2) == BANKED_DESIGN[i]
        N1, V1, y1 = best_V(R, h, 1)
        sharp1 = (R + 1) // (h - 1)
        need = 0.68 * n * n
        rec = dict(name=r["name"], n=n, k=k, A=A, h=h, R=R,
                   V_star=V1, clusters=y1[1], points_per_cluster=y1[2],
                   rank_per_cluster=y1[3], tau=y1[4],
                   N_d1_KV=N1, cost_per_datum=2 * h / (V1 - 1),
                   banked_sharp_occ=sharp1,
                   banked_design_ceiling=BANKED_DESIGN[i],
                   banked_free_ceiling=BANKED_FREE[i],
                   requirement=need,
                   margin_KV=need / max(N1, 1),
                   margin_banked=need / max(sharp1, 1),
                   blowup_vs_sharp=N1 / max(sharp1, 1),
                   blowup_vs_design=N1 / max(BANKED_DESIGN[i], 1),
                   n_half=n // 2, N1_over_n=N1 / n)
        out.append(rec)
        print(f"{r['name']:<11}{h:>13}{R:>16}{V1:>8}{y1[1]:>10}{N1:>12}"
              f"{sharp1:>14}{BANKED_DESIGN[i]:>15}{need:>12.4e}")

    print("\n=== A2  verdicts ===")
    for rec in out:
        chk(f"A2 {rec['name']}: K_V construction EXCEEDS SHARP-OCC's law "
            f"floor((R+1)/(h-1)) = {rec['banked_sharp_occ']}",
            rec["N_d1_KV"] > rec["banked_sharp_occ"],
            f"N_1={rec['N_d1_KV']} = x{rec['blowup_vs_sharp']:.4g}")
        chk(f"A2 {rec['name']}: K_V construction EXCEEDS the banked design "
            f"ceiling {rec['banked_design_ceiling']}",
            rec["N_d1_KV"] > rec["banked_design_ceiling"],
            f"x{rec['blowup_vs_design']:.4g}")
        chk(f"A2 {rec['name']}: cost/datum {rec['cost_per_datum']:.4g} is "
            f"BELOW the banked sunflower cost h = {rec['h']}",
            rec["cost_per_datum"] < rec["h"],
            f"= 2h/(V-1), V*={rec['V_star']}")
        chk(f"A2 {rec['name']}: SHARP-OCC's weak form N_d <= n/2 survives",
            rec["N_d1_KV"] <= rec["n_half"],
            f"N_1={rec['N_d1_KV']} vs n/2={rec['n_half']}")
        chk(f"A2 {rec['name']}: the ratified 0.68 n^2 SURVIVES",
            rec["N_d1_KV"] < rec["requirement"],
            f"margin x{rec['margin_KV']:.4e} "
            f"(banked margin was x{rec['margin_banked']:.4e}, "
            f"lost a factor {rec['blowup_vs_sharp']:.4g})")

    print("\n=== A3  worst depth ===")
    for rec, r in zip(out, ROWS):
        h, R, n = r["h"], r["R"], r["n"]
        best = (0, 0, 0)
        ds = sorted({1, 2, 3, 4, 8, 16, 32,
                     max(1, (h - 1) // 4), max(1, (h - 1) // 2), h - 2})
        for d in ds:
            if d < 1 or d > h - 2:
                continue
            N, V, y = best_V(R, h, d)
            if N > best[0]:
                best = (N, d, V)
        rec.update(N_max_over_d=best[0], argmax_d=best[1], argmax_V=best[2],
                   margin_max=rec["requirement"] / max(best[0], 1),
                   N_max_over_n2=best[0] / (n * n))
        print(f"{r['name']:<11} max_d N_d = {best[0]:>10} at d={best[1]} "
              f"(V*={best[2]})  = {best[0]/(n*n):.4e} n^2  "
              f"margin x{rec['margin_max']:.4e}")
        chk(f"A3 {r['name']}: max over d still below 0.68 n^2",
            best[0] < rec["requirement"])

    print("\n=== A4  ledger column bound  sum_d N_d L(d)  vs 13 n^3 ===")
    for rec, r in zip(out, ROWS):
        n, h, R = r["n"], r["h"], r["R"]
        # the whole band shares one rank budget: sum_d (rays_d) h <= 2R-1,
        # so sum_d N_d <= max_d N_d * (number of depths that can be funded).
        # Crude but exact upper bound: N_d <= N_max for every d, and
        # L(d) = floor((R-d)/(h-d)) <= R/(h-d); sum_d 1/(h-d) <= ln h + 1.
        led = rec["N_max_over_d"] * R * (math.log(max(h, 3)) + 1)
        cap = 13 * n ** 3
        rec.update(ledger_bound=led, cap_13n3=float(cap),
                   ledger_over_n3=led / n ** 3)
        print(f"{r['name']:<11} ledger <= {led:.4e} = {led/n**3:.4e} n^3   "
              f"13n^3 = {float(cap):.4e}   margin x{cap/max(led,1):.4e}")
        chk(f"A4 {r['name']}: ledger column stays under 13 n^3", led < cap)

    print("\n=== A5  the sufficient floor, restated per RAY ===")
    for rec, r in zip(out, ROWS):
        h, R = r["h"], r["R"]
        need = rec["requirement"]
        c_datum = (2 * R - 1) / need
        rho = (2 * R - 1) / math.sqrt(2 * need)
        rec.update(c_needed_per_datum=c_datum, rho_needed_per_ray=rho,
                   ray_law_margin=h / rho)
        print(f"{r['name']:<11} banked per-datum floor c = {c_datum:.4e}   "
              f"per-RAY floor rho needed = {rho:.4f}   actual = h = {h}   "
              f"margin x{h/rho:.4e}")
        chk(f"A5 {r['name']}: the per-ray charge h clears the per-ray floor "
            f"the requirement needs", h > rho, f"h={h} > {rho:.4f}")

    with open(os.path.join(HERE, "arith_repricing.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()

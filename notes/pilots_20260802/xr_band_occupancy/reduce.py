#!/usr/bin/env python3
"""Reduction arithmetic + empirical growth-law fit.

1. the high-band reduction: for d >= ceil(h/2) the map P -> f_P is injective,
   so N_d <= |list of codewords at agreement >= k+d with u|.  Report the
   agreement threshold as a multiple of k and the required list bound.
2. Deza's sunflower theorem applied to the equidistant clique at d=(h-1)/2.
3. the explicit sunflower law N_d = (n-k+1)/(h-d) at the six rows.
4. log-log fit of max admissible N over n from the battery checkpoints.

Run: tools/ramguard tiny -- python3 <this>
"""
import json
import math

HERE = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/"
        "xr_band_occupancy")
TH = json.load(open(f"{HERE}/theory.json"))
ROWS = [dict(name="RowC 1/4", n=1024, k=256, A=261, h=5),
        dict(name="RowC 1/8", n=1024, k=128, A=133, h=5),
        dict(name="RowC 1/16", n=1024, k=64, A=67, h=3),
        dict(name="prize 1/4", n=2199023255552, k=549755813888,
             A=558345748481, h=8589934593),
        dict(name="prize 1/8", n=2199023255552, k=274877906944,
             A=283467841537, h=8589934593),
        dict(name="prize 1/16", n=2199023255552, k=137438953472,
             A=141733920769, h=4294967297)]
SPLIT = {r["row"]: r for r in TH["ledger_mass_split"]}
OUT = {}

print("=" * 78)
print("1. HIGH-BAND REDUCTION  (d >= ceil(h/2): N_d <= |{c : agr(c,u) >= k+d}|)")
red = []
for r in ROWS:
    n, k, h, A = r["n"], r["k"], r["h"], r["A"]
    d0 = (h + 1) // 2
    tau = k + d0
    s = SPLIT[r["name"]]
    needB = (13 * n ** 3 / s["sumL_high"]) if s["sumL_high"] else None
    rec = dict(row=r["name"], d0=d0, tau=tau, tau_over_n=tau / n,
               tau_over_k=tau / k, epsilon=(tau - k) / k,
               A_over_k=A / k, johnson_over_k=math.sqrt(k * n) / k,
               required_list_bound_over_n2=(needB / n ** 2 if needB else None),
               required_list_bound=needB)
    red.append(rec)
    print(f"  {r['name']:<11} d0={d0:<11} tau=k+d0 = {tau/k:.6f} k = {tau/n:.5f} n"
          f"   (A = {A/k:.6f} k, Johnson = {math.sqrt(k*n)/k:.3f} k)"
          f"   need |list(tau)| <= "
          f"{(needB/n**2 if needB else 0):.4g} n^2")
OUT["high_band_reduction"] = red

print()
print("2. DEZA CLIQUE BOUND at d=(h-1)/2 (equidistant, lambda = k-1)")
dz = []
for r in ROWS:
    n, k, h = r["n"], r["k"], r["h"]
    if h % 2 == 0:
        dz.append(dict(row=r["name"], note="h even: no depth with lambda=k-1"))
        print(f"  {r['name']:<11} h even -- no equidistant depth")
        continue
    d = (h - 1) // 2
    kap = k + d
    deza = kap * kap - kap + 1
    cap = (n - k - d) // (h - d)
    dz.append(dict(row=r["name"], d=d, kappa=kap, deza=deza,
                   deza_over_n2=deza / n ** 2, sunflower_cap=cap + 1,
                   sunflower_over_n=(cap + 1) / n))
    print(f"  {r['name']:<11} d={d:<11} kappa=k+d={kap:<14} "
          f"Deza bound = {deza/n**2:.5g} n^2   sunflower branch <= "
          f"L(d)+1 = {cap+1} = {(cap+1)/n:.4g} n")
OUT["deza"] = dz

print()
print("3. EXPLICIT SUNFLOWER LAW N_d = (n-k+1)/(h-d) at the six rows")
sf = []
for r in ROWS:
    n, k, h = r["n"], r["k"], r["h"]
    for d in sorted(set([1, max(1, (h - 1) // 2), h - 2])):
        if not (1 <= d <= h - 2):
            continue
        val = (n - k + 1) / (h - d)
        sf.append(dict(row=r["name"], d=d, N_d=val, over_n=val / n,
                       over_n2=val / n ** 2))
    print(f"  {r['name']:<11} d=1: {(n-k+1)/(h-1):.4g}   "
          f"d=(h-1)/2: {(n-k+1)/(h-(h-1)//2):.4g}   "
          f"d=h-2: {(n-k+1)/2:.4g} = {(n-k+1)/2/n:.3f} n"
          f"   [target 0.68 n^2 = {0.68*n**2:.4g}]")
OUT["sunflower_law"] = sf

print()
print("4. EMPIRICAL GROWTH (max admissible N over n, per shape)")
gr = []
for fn, tagf in (("battery_sun.json", lambda r: r["k"] == 3 and r["t"] == 3),
                 ("battery_odd5.json", lambda r: r["t"] == 5),
                 ("battery_multi.json", lambda r: True),
                 ("battery_climb.json", lambda r: True)):
    try:
        data = json.load(open(f"{HERE}/{fn}"))
    except FileNotFoundError:
        continue
    best = {}
    for r in data:
        if "error" in r or not r.get("ADMISSIBLE") or not tagf(r):
            continue
        key = (r["n"], r["k"], r["t"])
        if key not in best or r["N_total"] > best[key]["N_total"]:
            best[key] = r
    pts = sorted((k[0], v["N_total"], v["Gamma_band_measured"],
                  v["ledger_slack_vs_measured"]) for k, v in best.items())
    if len(pts) >= 3:
        xs = [math.log(p[0]) for p in pts if p[1] > 0]
        ys = [math.log(p[1]) for p in pts if p[1] > 0]
        gs = [math.log(p[2]) for p in pts if p[2] > 0]
        mx = sum(xs) / len(xs)
        slopeN = (sum((x - mx) * (y - sum(ys) / len(ys)) for x, y in zip(xs, ys))
                  / sum((x - mx) ** 2 for x in xs))
        slopeG = (sum((x - mx) * (y - sum(gs) / len(gs)) for x, y in zip(xs, gs))
                  / sum((x - mx) ** 2 for x in xs))
    else:
        slopeN = slopeG = None
    gr.append(dict(file=fn, points=pts, loglog_slope_N=slopeN,
                   loglog_slope_Gamma=slopeG))
    print(f"  {fn}: (n, N, |Gamma_band|, ledger slack)")
    for p in pts:
        print(f"      n={p[0]:<4} N={p[1]:<5} Gamma={p[2]:<6} slack={p[3]}")
    print(f"      log-log exponent:  N ~ n^{slopeN}   "
          f"|Gamma_band| ~ n^{slopeG}")
OUT["growth"] = gr

json.dump(OUT, open(f"{HERE}/reduce.json", "w"), indent=1, default=str)
print(f"\ncheckpoint: {HERE}/reduce.json")

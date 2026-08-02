#!/usr/bin/env python3
"""Consolidated read-out of the banked JSONs (F2A.5b)."""
from __future__ import annotations
import glob, json, math, os, sys
sys.dont_write_bytecode = True
_H = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(_H, "results")

print("=== A. RAMP: is the measured exact exponent EQUAL to the k=p floor? ===")
print(f"{'p':>5} {'n':>4} {'beta_min band':>15} {'#rows':>6} "
      f"{'median |meas - kp floor| (bits)':>32} {'max':>8}")
allrows = []
for f in sorted(glob.glob(os.path.join(R, "ramp_p*.json"))):
    d = json.load(open(f))
    allrows += [(d["p"], r) for r in d["rows"]]
for p in sorted({x[0] for x in allrows}):
    for n in (32, 48, 64, 96):
        for lo, hi, lbl in ((0.0, 0.14, "beta_min<=0.13"),
                            (0.14, 0.51, "beta_min>0.13")):
            sel = [r for q, r in allrows
                   if q == p and r["n"] == n and lo <= r["beta_min"] < hi
                   and r["kp_floor_bits"] is not None]
            if not sel:
                continue
            ds = sorted(abs(r["worst_neglog2"] - r["kp_floor_bits"]) for r in sel)
            print(f"{p:5d} {n:4d} {lbl:>15} {len(ds):6d} "
                  f"{ds[len(ds)//2]:32.4f} {ds[-1]:8.3f}")

print("\n=== B. RAMP: exact exponent vs beta_min, worst slice, n=96 ===")
print(f"{'p':>5} {'c':>7} {'beta_min':>9} {'m=minority':>11} "
      f"{'-log2 rho (exact)':>18} {'k=p floor':>10} {'eta_n':>8} "
      f"{'>1/3':>5} {'>1/43':>6}")
for p, r in allrows:
    if r["n"] != 96:
        continue
    m = min(r["n_odd"], r["n_even"])
    print(f"{p:5d} {str(tuple(r['c'])):>7} {r['beta_min']:9.4f} {m:11d} "
          f"{r['worst_neglog2']:18.4f} "
          f"{(r['kp_floor_bits'] if r['kp_floor_bits'] is not None else float('nan')):10.4f} "
          f"{r['eta_n']:8.4f} {'Y' if r['eta_n']>1/3 else 'n':>5} "
          f"{'Y' if r['eta_n']>1/43 else 'n':>6}")

print("\n=== C. KILLERS: every window class with eta_n < 1/43 = 0.02326 ===")
print(f"{'p':>5} {'c':>7} {'n':>4} {'family':>17} {'beta_min':>9} "
      f"{'#Dval':>6} {'-log2 rho':>10} {'eta_n':>9} {'k=p floor':>10} "
      f"{'1-|R|max':>9}")
bad = []
for f in sorted(glob.glob(os.path.join(R, "killers_p*.json"))):
    d = json.load(open(f))
    for r in d["rows"]:
        if r["eta_n"] is not None and r["eta_n"] < 1 / 43:
            bad.append((d["p"], r))
for p, r in bad:
    print(f"{p:5d} {str(tuple(r['c'])):>7} {r['n']:4d} {r['family']:>17} "
          f"{r['beta_min']:9.4f} {r['distinct_delta']:6d} "
          f"{r['worst_neglog2']:10.5f} {r['eta_n']:9.6f} "
          f"{(r['kp_floor_bits'] if r['kp_floor_bits'] is not None else float('nan')):10.3f} "
          f"{1-r['flatness_max_absR']:9.5f}")
print(f"  -> {len(bad)} window classes fail even the WEAK 1/43 budget; "
      f"max beta_min among them = "
      f"{max((r['beta_min'] for _, r in bad), default=0):.4f}")

print("\n=== D. FLATSCAN: dial comparison, both primes ===")
for f in sorted(glob.glob(os.path.join(R, "flatscan_p*.json"))):
    d = json.load(open(f))
    rows = d["rows"]
    for key, thr, lbl in (("beta_min", 0.25, "beta_min >= 0.25"),
                          ("beta_min", 0.45, "beta_min >= 0.45"),
                          ("flat", 0.10, "1-max|R_k| >= 0.10"),
                          ("flat", 0.30, "1-max|R_k| >= 0.30"),
                          ("minLam_n", 4.0, "n*min Lambda >= 4"),
                          ("minLam_n", 8.0, "n*min Lambda >= 8")):
        sel = [r for r in rows if r[key] >= thr]
        if not sel:
            continue
        print(f"  p={d['p']:3d} n={d['n']}  {lbl:>22}: {len(sel):4d} windows, "
              f"min eta_n = {min(r['eta_n'] for r in sel):.6f}, "
              f"median = {sorted(r['eta_n'] for r in sel)[len(sel)//2]:.4f}")

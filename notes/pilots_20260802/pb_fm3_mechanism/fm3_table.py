#!/usr/bin/env python3
"""FM3 mechanism pilot -- render the decomposition tables from MINE.json."""
from __future__ import annotations
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True

SUP = ["ORD-LEX", "ORD-COLEX", "ORD-VALEX", "ORD-VALCOLEX", "ORD-ERRLEX"]
NUL = ["ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]
ORD = SUP + NUL + ["ORD-POLYLEX", "ORD-CODEWORD"]

d = json.load(open(os.path.join(_HERE, "MINE.json")))
cases = sorted(d, key=lambda c: -d[c]["mean_Wz"])

print("=" * 118)
print("TABLE 1 -- concentration excess of the selected pairwise-core law "
      "(support-keyed orders vs nulls)")
print("=" * 118)
hdr = (f"{'case':5s} {'n':>3s} {'q':>4s} {'K':>3s} {'h':>2s} {'A':>3s} "
       f"{'meanW':>7s} {'order':21s} {'ret':>6s} {'|B|100':>6s} {'|B|90':>6s} "
       f"{'E[core]':>7s} {'E0':>6s} {'P>=K':>9s} {'P0':>9s} {'excess':>8s}")
print(hdr)
for c in cases:
    r = d[c]
    n0 = r["null_uniform"]
    for o in ORD:
        e = r["orders"].get(o)
        if not e:
            continue
        exc = (e["p_ge_K_obs"] / n0["p_ge_K"]) if n0["p_ge_K"] > 0 else float("nan")
        print(f"{c:5s} {r['n']:3d} {r['q']:4d} {r['K']:3d} {r['h']:2d} "
              f"{r['A']:3d} {r['mean_Wz']:7.0f} {o:21s} "
              f"{e['retention_measured']:6.3f} {len(e['block_100']):6d} "
              f"{len(e['block_90']):6d} {e['mean_core']:7.2f} "
              f"{n0['mean']:6.2f} {e['p_ge_K_obs']:9.5f} "
              f"{n0['p_ge_K']:9.2e} {exc:8.1f}")
    print("-" * 118)

print()
print("=" * 118)
print("TABLE 2 -- null ladder: does block+birthday reproduce P[core>=K]?  "
      "(ratio observed / model; 1.00 = perfect)")
print("=" * 118)
print(f"{'case':5s} {'order':14s} {'meanW':>7s} {'P>=K obs':>9s} "
      f"{'N0 unif':>9s} {'N1 block':>9s} {'N2 marg':>9s} {'N3 greedy':>9s} "
      f"{'o/N0':>8s} {'o/N1':>8s} {'o/N2':>7s} {'o/N3':>7s} {'margL1':>7s}")
for c in cases:
    r = d[c]
    n0 = r["null_uniform"]["p_ge_K"]
    for o in SUP:
        e = r["orders"].get(o)
        if not e:
            continue
        n1 = e["null_block_residual"]["p_ge_K"]
        n2 = e["null_marginal_matched"]["p_ge_K"]
        g = e.get("null_greedy")
        n3 = g["p_ge_K"] if g else float("nan")
        ob = e["p_ge_K_obs"]
        rr = lambda x: (ob / x) if x > 0 else float("inf")
        print(f"{c:5s} {o[4:]:14s} {r['mean_Wz']:7.0f} {ob:9.5f} "
              f"{n0:9.2e} {n1:9.5f} {n2:9.5f} {n3:9.5f} "
              f"{rr(n0):8.1f} {rr(n1):8.2f} {rr(n2):7.2f} {rr(n3):7.2f} "
              f"{(g['marg_L1'] if g else float('nan')):7.2f}")
    print("-" * 118)

print()
print("=" * 100)
print("TABLE 3 -- retention: measured vs isolated-vertex prediction from "
      "each null")
print("=" * 100)
print(f"{'case':5s} {'order':14s} {'live':>4s} {'ret meas':>8s} "
      f"{'ret N1':>8s} {'ret N2':>8s} {'ret N3':>8s} {'ret N3(obs P)':>13s}")
for c in cases:
    r = d[c]
    live = r["live"]
    for o in SUP:
        e = r["orders"].get(o)
        if not e:
            continue
        g = e.get("null_greedy")
        pobs = (1 - e["p_ge_K_obs"]) ** (live - 1)
        print(f"{c:5s} {o[4:]:14s} {live:4d} {e['retention_measured']:8.3f} "
              f"{e['null_block_residual']['pred_retention']:8.3f} "
              f"{e['null_marginal_matched']['pred_retention']:8.3f} "
              f"{(g['pred_retention'] if g else float('nan')):8.3f} "
              f"{pobs:13.3f}")
    print("-" * 100)

print()
print("=" * 100)
print("TABLE 4 -- coordinate marginal profiles (selected freq per "
      "coordinate, x100), ORD-LEX / ORD-COLEX / null")
print("=" * 100)
for c in cases:
    r = d[c]
    print(f"[{c}] n={r['n']} A={r['A']} q={r['q']} h={r['h']} "
          f"uniform={100*r['A']/r['n']:.0f}")
    for o in ["ORD-LEX", "ORD-COLEX", "ORD-HASH-pb-null-01"]:
        e = r["orders"].get(o)
        if not e:
            continue
        s = " ".join(f"{100*p:3.0f}" for p in e["coord_freq"])
        print(f"   {o[4:]:14s} obs   {s}")
        g = e.get("null_greedy")
        if g:
            s = " ".join(f"{100*p:3.0f}" for p in g["marginals"])
            print(f"   {'':14s} model {s}")

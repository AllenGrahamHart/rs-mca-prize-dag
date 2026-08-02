#!/usr/bin/env python3
"""FM3 mechanism pilot -- consolidated evidence table over all 21 measured
parameter points (12 banked + R1-R3 new + F1a-c/F2a-b/F3a falsifiers).

Columns:
  Pi        analytic population count of >=K-core partners per witness,
            sum_{c=K}^{A-m} C(A,c) C(n-A,A-c) / q^(h-1)   (equidistribution)
  P_pop     measured pair probability P[core>=K] in the population, proxied
            by the two hash null-control selections (which POP.json shows
            are statistically indistinguishable from the population)
  P_sel     measured P[core>=K] for the ORD-LEX selected family
  tilt      P_sel / P_pop            (the selector's contribution)
  struct    P_pop / P_uniform        (the pencil's contribution)
  liveP     live * P_sel             (expected >=K partners per slope)
"""
from __future__ import annotations
import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(os.path.dirname(_HERE), "pb_selector_orders")
sys.dont_write_bytecode = True
sys.path.insert(0, _HERE)
from fm3_mine import analyse_case, hypergeom_overlap, tail  # noqa

FILES = ([(f"Q{i}", os.path.join(_BANK, f"k1_Q{i}.json")) for i in
          [9, 12, 4, 5, 10, 6, 7, 8, 1, 2, 3, 11]]
         + [(t, os.path.join(_HERE, f"k1_{t}.json")) for t in
            ["R1", "R2", "R3", "F1a", "F1b", "F1c", "F2a", "F2b"]])

rows = []
print(f"{'case':5s} {'n':>3s} {'q':>5s} {'K':>3s} {'A':>3s} {'h':>2s} "
      f"{'|W_z|':>8s} {'live':>5s} {'|B|':>3s} {'Pi':>9s} {'P_unif':>9s} "
      f"{'P_pop':>9s} {'P_sel':>9s} {'struct':>7s} {'tilt':>8s} "
      f"{'liveP':>7s} {'Glo':>4s} {'8n^3':>7s}")
for tag, path in FILES:
    if not os.path.exists(path):
        continue
    m = analyse_case(path, {})
    n, q, K, A, h, mm = m["n"], m["q"], m["K"], m["A"], m["h"], m["m"]
    Pi = sum(math.comb(A, c) * math.comb(n - A, A - c) / q ** (h - 1)
             for c in range(K, A - mm + 1))
    pu = m["null_uniform"]["p_ge_K"]
    pp = sum(m["orders"][o]["p_ge_K_obs"]
             for o in ["ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]) / 2
    ps = m["orders"]["ORD-LEX"]["p_ge_K_obs"]
    live = m["live"]
    rows.append(dict(case=tag, n=n, q=q, K=K, A=A, h=h, m=mm,
                     Wz=m["mean_Wz"], live=live,
                     block=len(m["orders"]["ORD-LEX"]["block_100"]),
                     Pi=Pi, P_unif=pu, P_pop=pp, P_sel=ps,
                     struct=(pp / pu if pu else None),
                     tilt=(ps / pp if pp else None),
                     liveP=live * ps,
                     gamma_lo=m["orders"]["ORD-LEX"]["gamma_lo"],
                     budget=8 * n ** 3))
    r = rows[-1]
    print(f"{tag:5s} {n:3d} {q:5d} {K:3d} {A:3d} {h:2d} {m['mean_Wz']:8.1f} "
          f"{live:5d} {r['block']:3d} {Pi:9.3f} {pu:9.2e} {pp:9.2e} "
          f"{ps:9.2e} "
          f"{(r['struct'] if r['struct'] else 0):7.2f} "
          f"{(r['tilt'] if r['tilt'] else float('inf')):8.1f} "
          f"{r['liveP']:7.2f} {r['gamma_lo']:4d} {r['budget']:7d}")

# F3a computed separately (4280 live slopes -- diff_stats does not scale)
f3 = os.path.join(_HERE, "F3A_STATS.json")
if os.path.exists(f3):
    d = json.load(open(f3))
    n, q, K, A, h, mm = 32, 4993, 8, 10, 2, 2
    Pi = math.comb(A, K) * math.comb(n - A, A - K) / q ** (h - 1)
    n0 = hypergeom_overlap(n, A)
    pu = tail(n0, K)
    pp = (d["ORD-HASH-pb-null-01"]["p_ge_K"]
          + d["ORD-HASH-pb-null-02"]["p_ge_K"]) / 2
    ps = d["ORD-LEX"]["p_ge_K"]
    live = d["ORD-LEX"]["live"]
    rows.append(dict(case="F3a", n=n, q=q, K=K, A=A, h=h, m=mm,
                     Wz=16178 / live, live=live, block=0, Pi=Pi, P_unif=pu,
                     P_pop=pp, P_sel=ps, struct=pp / pu, tilt=ps / pp,
                     liveP=live * ps, gamma_lo=d["ORD-LEX"]["gamma_lo"],
                     budget=8 * n ** 3))
    r = rows[-1]
    print(f"{'F3a':5s} {n:3d} {q:5d} {K:3d} {A:3d} {h:2d} {r['Wz']:8.1f} "
          f"{live:5d} {0:3d} {Pi:9.3f} {pu:9.2e} {pp:9.2e} {ps:9.2e} "
          f"{r['struct']:7.2f} {r['tilt']:8.1f} {r['liveP']:7.2f} "
          f"{r['gamma_lo']:4d} {r['budget']:7d}")

with open(os.path.join(_HERE, "EVIDENCE.json"), "w") as fh:
    json.dump(rows, fh, indent=1, sort_keys=True)
print("\n->", os.path.join(_HERE, "EVIDENCE.json"))

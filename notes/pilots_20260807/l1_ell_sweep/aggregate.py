#!/usr/bin/env python3
"""E5: aggregate results.jsonl + ub_results.jsonl into the deliverable tables
(D1 the sweep, D2 the F-w1 test, D3 the law in ell, D4 the clause-(b) shape)."""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
P = 97

rows = [json.loads(l) for l in open(os.path.join(HERE, "results.jsonl"))]
ubs = [json.loads(l) for l in open(os.path.join(HERE, "ub_results.jsonl"))]

cells = defaultdict(lambda: {"words": {}, "meta": None})
for r in rows:
    if not r["band"]:
        continue
    key = (r["n"], r["ell"], r["layout"])
    cells[key]["meta"] = r
    for w in r["words"]:
        cells[key]["words"][tuple(w["c"])] = w

print("=" * 118)
print("D1/D3  THE SWEEP -- exact retained counts, and the random-word law")
print("=" * 118)
print(f"{'n':>3} {'ell':>4} {'L':>2} {'t':>3} {'b':>2} {'Lam':>4} {'BOX':>15} "
      f"{'N_k+1':>14} {'RETPRED':>12} {'consec':>11} {'geom5':>11} "
      f"{'mindeg':>11} {'maxRET':>11} {'EXCmax':>7} {'band':>7}")
for key in sorted(cells):
    n, ell, lay = key
    m = cells[key]["meta"]
    ws = cells[key]["words"]
    named = {w["name"].split("(")[0]: w for w in m["words"]}
    allw = list(ws.values())
    for r in rows:
        if (r["n"], r["ell"], r["layout"]) == key and r["band"]:
            for w in r["words"]:
                named.setdefault(w["name"].split("(")[0], w)
                allw.append(w)
    dedup = {tuple(w["c"]): w for w in allw}
    allw = list(dedup.values())
    best = max(allw, key=lambda w: w["RET"])
    g = lambda nm: named[nm]["RET"] if nm in named else -1
    print(f"{n:>3} {ell:>4} {lay:>2} {m['t']:>3} {m['b']:>2} {m['Lambda']:>4} "
          f"{m['BOX_enum']:>15,} {m['N_k1']:>14,} {m['RETPRED']:>12,.0f} "
          f"{g('consec'):>11,} {g('geom5'):>11,} {g('mindeg'):>11,} "
          f"{best['RET']:>11,} {best['EXC']:>7.3f} "
          f"{'VACUOUS' if m['t'] < 3 else 'proper':>7}")

print()
print("=" * 118)
print("D4  CLAUSE-(b) SHAPE: RATIOBOX = RET/(BOX/q) and RATIOSHELL = "
      "RET/(N_k+1/q) as ell grows at fixed n")
print("=" * 118)
for nn in (16, 24, 32):
    for lay in ("A", "B"):
        ks = sorted(k for k in cells if k[0] == nn and k[2] == lay)
        if not ks:
            continue
        seg = []
        for k in ks:
            m = cells[k]["meta"]
            named = {w["name"].split("(")[0]: w for w in m["words"]}
            w = named.get("consec") or list(cells[k]["words"].values())[0]
            seg.append(f"ell={k[1]}(t={m['t']}): RB {w['RATIOBOX']:.4f} "
                       f"RS {w['RATIOSHELL']:.4f}")
        print(f"  n={nn} LAYOUT-{lay}: " + "   ".join(seg))

print()
print("=" * 118)
print("D2  THE F-w1 TEST: is RET > 10*BOX/q anywhere?")
print("=" * 118)
worst = 0.0
for key in sorted(cells):
    m = cells[key]["meta"]
    allw = []
    for r in rows:
        if (r["n"], r["ell"], r["layout"]) == key and r["band"]:
            allw += r["words"]
    dedup = {tuple(w["c"]): w for w in allw}
    best = max(dedup.values(), key=lambda w: w["RATIOBOX"])
    worst = max(worst, best["RATIOBOX"] / 10)
    print(f"  n={key[0]:>3} ell={key[1]} L{key[2]}: words tested "
          f"{len(dedup):>4}   max RET/(BOX/q) = {best['RATIOBOX']:.4f}   "
          f"F-w1 needs > 10   -> "
          f"{'*** FIRES ***' if best['RATIOBOX'] > 10 else 'silent'}"
          f"   (headroom {10/max(best['RATIOBOX'],1e-9):.1f}x)")
print(f"  GLOBAL: the largest observed RET/(10*BOX/q) is {worst:.5f}")

print()
print("=" * 118)
print("D2b  UB SCAN -- upper bound uniform over words (exhaustive when t<=3)")
print("=" * 118)
print(f"{'n':>3} {'ell':>4} {'L':>2} {'t':>3} {'words':>10} {'kind':>11} "
      f"{'maxUB':>15} {'10*BOX/q':>15} {'maxUB/thr':>10} {'#over':>6}")
seen=set()
for u in sorted(ubs, key=lambda z: (z["n"], z["ell"], z["layout"])):
    kk=(u["n"],u["ell"],u["layout"],u["nwords"])
    if kk in seen or "n_words_over_threshold" not in u: continue
    seen.add(kk)
    print(f"{u['n']:>3} {u['ell']:>4} {u['layout']:>2} {u['t']:>3} "
          f"{u['nwords']:>10,} {'EXHAUSTIVE' if u['exhaustive'] else 'search':>11} "
          f"{u['maxUB']:>15,} {u['F_w1_threshold_10BOXoverq']:>15,.0f} "
          f"{u['maxUB_over_threshold']:>10.4f} {u.get('n_words_over_threshold','?'):>6}")

print()
print("=" * 118)
print("P4  SCOPE TEST -- the same object with the floor band DROPPED")
print("=" * 118)
for r in rows:
    if r["band"]:
        continue
    for w in r["words"]:
        print(f"  n={r['n']} ell={r['ell']} L{r['layout']} band=OFF "
              f"a_cap={r['a_cap']} BOX={r['BOX_enum']:,}  word={w['name']}: "
              f"RET={w['RET']:,}  agreement hist={w['hist_agr']}  "
              f"core hist={w['hist_a']}")
    print(f"     Lambda={r['Lambda']}  => max legal agreement in-band is "
          f"k+Lambda={r['n']//2 + r['Lambda']}")

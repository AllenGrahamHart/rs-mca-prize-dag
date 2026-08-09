#!/usr/bin/env python3
"""Round-26 verdict analysis: join the exactly-computed cells to their
RESSIEVE low-weight profiles and score the registered predictions.

  tools/ramguard local -- python3 analyze26.py
"""
import glob
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z25 = os.path.abspath(os.path.join(HERE, "..", "z_n32_band"))

cells = {}
for fn in sorted(glob.glob(os.path.join(HERE, "CELLS26.main.s*.tsv"))):
    for ln in open(fn):
        f = ln.rstrip("\n").split("\t")
        cells[int(f[3])] = dict(sig=float(f[4]), TNUM=int(f[5]), NKER=int(f[6]),
                                TMASS=float(f[7]), CR=float(f[8]),
                                ZF=f[11], tag=f[12] if len(f) > 12 else "")
alt = {}
for fn in sorted(glob.glob(os.path.join(HERE, "CELLS26.alt.s*.tsv"))):
    for ln in open(fn):
        f = ln.rstrip("\n").split("\t")
        alt[int(f[3])] = (int(f[5]), int(f[6]))

cand = {}
for ln in open(os.path.join(HERE, "CANDS.N32.k1.tsv")):
    f = ln.rstrip("\n").split("\t")
    if f[0] == "p":
        continue
    cand[int(f[0])] = dict(umin=int(f[2]), H=float(f[3]),
                           pce=float(f[4]),
                           pc=float(f[5]) if f[5] else None,
                           AU=f[7] if len(f) > 7 else "")

r25 = {}
for fn in sorted(glob.glob(os.path.join(Z25, "CELLS*.tsv"))):
    for ln in open(fn):
        f = ln.rstrip("\n").split("\t")
        if len(f) < 9 or f[0] == "family" or int(f[1]) != 32 or int(f[2]) != 1:
            continue
        r25[int(f[3])] = float(f[8])

print("EXACT cells this round: %d   (two-way re-derived: %d, disagreements: %d)"
      % (len(cells), len(set(cells) & set(alt)),
         sum(1 for p in set(cells) & set(alt)
             if (cells[p]["TNUM"], cells[p]["NKER"]) != alt[p])))
print("Z-FLOOR violations: %d"
      % sum(1 for p in cells if cells[p]["ZF"] != "True"))

srt = sorted(cells.items(), key=lambda kv: -kv[1]["CR"])
print("\nMAX CRATIO = %.10f at p=%d (sigma %+.4f, TMASS %.6f, NKER %d)"
      % (srt[0][1]["CR"], srt[0][0], srt[0][1]["sig"], srt[0][1]["TMASS"],
         srt[0][1]["NKER"]))
print("cells > 2.0 : %d / %d ;  > 1.7681 (N=16 exhaustive record) : %d ;"
      "  > 1.4211 (round-25 N=32 sample max) : %d"
      % (sum(1 for v in cells.values() if v["CR"] > 2), len(cells),
         sum(1 for v in cells.values() if v["CR"] > 1.7680688810),
         sum(1 for v in cells.values() if v["CR"] > 1.4210954721)))

u5 = [(p, v) for p, v in cells.items() if cand.get(p, {}).get("umin") == 5]
u6 = [(p, v) for p, v in cells.items() if cand.get(p, {}).get("umin") == 6]
esc = [(p, v) for p, v in cells.items() if p not in cand]
print("\nSTRATA (exact):")
for nm, g in (("UMIN=5 (EXHAUSTIVE: all 90 in-band)", u5),
              ("UMIN=6 (sample of 2399)", u6),
              ("no orbit of weight<=7 (round-25 escape cells)", esc)):
    if g:
        crs = sorted(v["CR"] for _, v in g)
        print("  %-46s n=%3d  min %.4f  median %.4f  MAX %.4f"
              % (nm, len(g), crs[0], crs[len(crs) // 2], crs[-1]))

print("\nAMPLIFICATION LAW  TMASS ~ (1 + 2^{1-UMIN})^N   (ideal-multiple heuristic)")
for U in (5, 6):
    g = [v for p, v in cells.items() if cand.get(p, {}).get("umin") == U]
    if g:
        print("  UMIN=%d  law=%.4f   measured mean TMASS=%.4f  min %.4f  max %.4f"
              % (U, (1 + 2.0 ** (1 - U)) ** 32,
                 sum(v["TMASS"] for v in g) / len(g),
                 min(v["TMASS"] for v in g), max(v["TMASS"] for v in g)))

print("\nP-U8 PREDCR accuracy on the promoted cells with exact AU:")
d = [(cells[p]["CR"] - cand[p]["pc"]) for p in cells
     if p in cand and cand[p]["pc"] is not None]
if d:
    d.sort()
    print("  n=%d  min %.4f  median %.4f  max %.4f   (PREDCR uses only U<=7,"
          " so it is a LOWER bound in expectation)"
          % (len(d), d[0], d[len(d) // 2], d[-1]))
    print("  fraction with CRATIO >= PREDCR - 0.10 : %.3f"
          % (sum(1 for x in d if x >= -0.10) / float(len(d))))
    print("  fraction with |CRATIO - PREDCR| <= 0.25 : %.3f"
          % (sum(1 for x in d if abs(x) <= 0.25) / float(len(d))))

print("\nESCAPE replays vs round-25 banked CRATIO:")
for p, v in sorted(esc):
    b = r25.get(p)
    print("  p=%-13d CRATIO=%.10f  banked=%s  %s"
          % (p, v["CR"], ("%.10f" % b) if b else "-",
             "EXACT MATCH" if b and abs(b - v["CR"]) < 1e-12 else "??"))

print("\nTOP-20 exact cells:")
for p, v in srt[:20]:
    c = cand.get(p, {})
    print("  p=%-13d sigma=%+.4f UMIN=%-2s TMASS=%9.5f NKER=%-8d CRATIO=%.8f"
          "  2way=%s  AU(U<=7)=%s"
          % (p, v["sig"], c.get("umin", "-"), v["TMASS"], v["NKER"], v["CR"],
             ("AGREE" if alt.get(p) == (v["TNUM"], v["NKER"])
              else ("-" if p not in alt else "DISAGREE")), c.get("AU", "")))

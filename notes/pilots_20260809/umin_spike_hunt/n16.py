#!/usr/bin/env python3
"""GROUND-TRUTH ARM: the RESSIEVE census of the WHOLE N=16 band (U<=12,
escape test E4: it already matched the exhaustive reference enumerator on
every one of the 1305 in-band cells) is joined here to the banked EXHAUSTIVE
1305-cell CRATIO line from round 25.  This is where the instrument's RECALL
and its ranking power are MEASURED against truth rather than asserted.

  tools/ramguard local -- python3 n16.py
"""
import glob
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z25 = os.path.abspath(os.path.join(HERE, "..", "z_n32_band"))

cen = {int(k): {int(a): b for a, b in v.items()}
       for k, v in json.load(open(os.path.join(HERE, "N16_CENSUS.json"))).items()}

truth = {}
for fn in sorted(glob.glob(os.path.join(Z25, "CELLS*.tsv"))):
    for ln in open(fn):
        f = ln.rstrip("\n").split("\t")
        if len(f) < 9 or f[0] == "family" or int(f[1]) != 16:
            continue
        truth[int(f[3])] = (float(f[8]), float(f[7]), int(f[6]))   # CR, TMASS, NKER

print("banked exhaustive N=16 cells: %d ;  sieve census cells: %d"
      % (len(truth), len(cen)))

H = lambda p: ((1 << 16) - 1) / float(p)
rows = []
for p, cr in truth.items():
    d = cen.get(p, {})
    umin = min(d) if d else None
    bonus = sum(a * 2.0 ** (-u) for u, a in d.items())
    rows.append((p, cr[0], cr[1], cr[2], umin, bonus, 1 + bonus / (1 + H(p))))

# --- P-U3: census counts
for U in (4, 5, 6, 7, 8):
    n = sum(1 for r in rows if r[4] is not None and r[4] <= U)
    print("  in-band N=16 primes with UMIN <= %d : %d" % (U, n))
print("  cells with NO orbit of weight <= 12 : %d"
      % sum(1 for r in rows if r[4] is None))

# --- P-U2: the record cell
rec = [r for r in rows if r[0] == 161761][0]
print("  RECORD p=161761: UMIN=%s BONUS=%.4f PREDCR=%.4f  exact CRATIO=%.6f"
      % (rec[4], rec[5], rec[6], rec[1]))

# --- P-U2: recall of the top-20 by exact CRATIO inside the sieve's top-40
bycr = sorted(rows, key=lambda r: -r[1])
bypc = sorted(rows, key=lambda r: -r[6])
top20 = set(r[0] for r in bycr[:20])
for K in (20, 40, 60):
    hit = len(top20 & set(r[0] for r in bypc[:K]))
    print("  recall: top-20 by exact CRATIO found in sieve top-%d : %d/20 = %.2f"
          % (K, hit, hit / 20.0))
flagged = sum(1 for r in bycr[:20] if r[4] is not None)
print("  of the top-20 exact cells, %d/20 carry a weight<=12 orbit at all" % flagged)


def spearman(a, b):
    def rk(x):
        o = sorted(range(len(x)), key=lambda i: x[i])
        r = [0.0] * len(x)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2.0
            i = j + 1
        return r
    ra, rb = rk(a), rk(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((ra[i] - ma) * (rb[i] - mb) for i in range(n))
    da = math.sqrt(sum((x - ma) ** 2 for x in ra))
    db = math.sqrt(sum((x - mb) ** 2 for x in rb))
    return num / (da * db)


print("  Spearman(PREDCR, exact CRATIO) over all %d cells = %.4f"
      % (len(rows), spearman([r[6] for r in rows], [r[1] for r in rows])))
print("  max |PREDCR - CRATIO| over all cells = %.4f ; mean = %.4f"
      % (max(abs(r[6] - r[1]) for r in rows),
         sum(abs(r[6] - r[1]) for r in rows) / len(rows)))

# --- the amplification law  TMASS ~ (1 + 2^{1-UMIN})^N
print("\n  UMIN-stratified TMASS at N=16 (law: TMASS ~ (1+2^{1-U})^16):")
for U in range(4, 13):
    g = [r for r in rows if r[4] == U]
    if not g:
        continue
    print("    UMIN=%2d  n=%4d  meanTMASS=%.4f  maxTMASS=%.4f  law=%.4f  "
          "maxCRATIO=%.4f" % (U, len(g), sum(r[2] for r in g) / len(g),
                              max(r[2] for r in g), (1 + 2.0 ** (1 - U)) ** 16,
                              max(r[1] for r in g)))
g = [r for r in rows if r[4] is None]
print("    UMIN>12 n=%4d  meanTMASS=%.4f  maxCRATIO=%.4f"
      % (len(g), sum(r[2] for r in g) / len(g), max(r[1] for r in g)))

print("\n  TOP-12 N=16 cells by exact CRATIO:")
for r in bycr[:12]:
    print("    p=%-8d sigma=%+.4f UMIN=%-4s TMASS=%.5f CRATIO=%.6f PREDCR=%.4f"
          % (r[0], 16 - math.log2(r[0]), r[4], r[2], r[1], r[6]))

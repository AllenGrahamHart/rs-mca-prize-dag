#!/usr/bin/env python3
"""D1c - the V1 statistic at the h = 8 EXHAUSTIVE toy: conditional-badness
independence, tested inside each dyadic window (so size cannot confound)."""
import json
import math

d = json.load(open("notes/pilots_20260809/large_v2_hunt/state/d1_h8.json"))
cells = {tuple(int(x) for x in k.split(",")): v for k, v in d["cells"].items()}
M = 4
vs = sorted({v for v, _ in cells})
js = sorted({j for _, j in cells})

chi2 = 0.0
df = 0
print("window  n_all  n_bad  BADDENS   per-v BADFRAC (v=4,5,6,...)")
for j in js:
    na = sum(cells[(v, j)][1] for v in vs if (v, j) in cells)
    nb = sum(cells[(v, j)][0] for v in vs if (v, j) in cells)
    if na < 30 or nb == 0:
        continue
    r = nb / na
    row = []
    for v in vs:
        b, a = cells.get((v, j), (0, 0))
        if a == 0:
            row.append("  .  ")
            continue
        row.append("%.2f" % (b / a))
        e = r * a
        if e >= 3:
            chi2 += (b - e) ** 2 / (e * (1 - r) if r < 1 else e)
            df += 1
    print("2^%-3d %6d %6d  %.4f    %s" % (j, na, nb, r, " ".join(row)))
df = max(df - len([j for j in js]), 1)
print("\nhomogeneity of BADFRAC8 across v WITHIN windows: chi2 = %.2f on ~%d df"
      % (chi2, df))
print("(V1: badness independent of v_2(p-1); chi2 ~ df means no structure)")

prof_bad = {int(k): v for k, v in d["prof_bad"].items() if int(k) >= M}
prof_all = {int(k): v for k, v in d["prof_all"].items()}
tb, ta = sum(prof_bad.values()), sum(prof_all.values())
print("\npooled: %d bad of %d primes = 1 mod 16 below %d (%.4f)"
      % (tb, ta, d["maxbad"], tb / ta))
print(" v  EXCESS  BADFRAC8   binom 95%% CI")
for v in sorted(prof_all):
    a = prof_all[v]
    b = prof_bad.get(v, 0)
    p = b / a
    se = math.sqrt(max(p * (1 - p), 1e-9) / a)
    print("%3d %5d    %.4f     [%.4f, %.4f]%s"
          % (v, v - M, p, max(0, p - 1.96 * se), p + 1.96 * se,
             "   <- pooled %.4f inside" % (tb / ta)
             if abs(p - tb / ta) < 1.96 * se else "   OUTSIDE"))

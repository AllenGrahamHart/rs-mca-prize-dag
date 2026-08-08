#!/usr/bin/env python3
"""c2pp_gb_probe -- score the PRE-REGISTERED G-b criterion (PREREG P6).

Reads gb_results.json (written by gb_probe.py) and prints, per cell:
  the omega_j sequence and Sigma_W at every q-scale, the saturation onset,
  and the (F1)-(F4) verdict.  No new measurement is taken here.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "gb_results.json")) as fh:
    ST = json.load(fh)

CELLORDER = ["L0", "L1", "L2", "L4", "S1", "S2", "S3", "S4"]


def lsq_slope(xs, ys):
    m = len(xs)
    if m < 2:
        return float("nan")
    mx, my = sum(xs) / m, sum(ys) / m
    den = sum((x - mx) ** 2 for x in xs)
    return float("nan") if den == 0 else sum(
        (x - mx) * (y - my) for x, y in zip(xs, ys)) / den


rows_by_cell = {}
for key, rec in ST["rows"].items():
    cell, _ = key.split("|")
    rows_by_cell.setdefault(cell, []).append(rec)
for c in rows_by_cell:
    rows_by_cell[c].sort(key=lambda r: r["q"])

print("=" * 78)
print("G-b SCORED AGAINST THE PRE-REGISTERED CRITERION (PREREG P6)")
print("=" * 78)
summary = []
for cell in CELLORDER:
    rows = rows_by_cell.get(cell)
    if not rows:
        continue
    n, t = rows[0]["n"], rows[0]["t"]
    W = rows[0]["window"]
    J = len(W)
    bal = n / t
    xs = [math.log2(r["q"]) for r in rows]
    ys = [r["Sigma_W"] for r in rows]
    # saturation onset: first q whose (C_j, Z_j) equal the top-q values
    fin = [(x["C_j"], x["Z_j"]) for x in rows[-1]["junctions"]]
    onset = None
    for r in rows:
        if [(x["C_j"], x["Z_j"]) for x in r["junctions"]] == fin:
            onset = r["q"]
            break
    half = len(xs) // 2
    slope_top = lsq_slope(xs[half:], ys[half:])
    slope_all = lsq_slope(xs, ys)
    incs = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
    strictly_up = all(d > 0 for d in incs)
    med = sorted(incs)[len(incs) // 2] if incs else 0.0
    f1 = J >= 8
    f2 = strictly_up
    f3 = (slope_top >= 0.25) and (incs and med != 0
                                  and incs[-1] >= 0.5 * med)
    up3 = 0
    for jj in range(J):
        seq = [r["junctions"][jj]["log2_omega"] for r in rows[-3:]]
        if all(b > a for a, b in zip(seq, seq[1:])):
            up3 += 1
    f4 = up3 >= math.ceil(J / 2)
    verdict = ("G-b FIRES" if (f1 and f2 and f3 and f4) else
               f"SUB-DEPTH GROWTH SIGNAL (J={J})" if (f2 and f3 and f4) else
               "G-b SILENT")
    print(f"\n--- CELL {cell}:  n={n} t={t}  window={W}  J={J} consecutive "
          f"junctions;  balance log2 q = n/t = {bal:g}")
    print(f"    {'log2 q':>8} | " +
          " ".join(f"log2 w_{j}".rjust(10) for j in W) + " |  Sigma_W    R3_W")
    for r, x in zip(rows, xs):
        cells = " ".join(f"{u['log2_omega']:10.4f}" for u in r["junctions"])
        r3 = f"{r['R3_W']:8.4f}" if "R3_W" in r else "     ---"
        star = " <-SAT" if r["q"] == onset else ""
        print(f"    {x:8.2f} | {cells} | {r['Sigma_W']:8.4f} {r3}{star}")
    print(f"    saturation onset q = {onset} (log2 = {math.log2(onset):.2f}); "
          f"frozen Sigma_W = {ys[-1]:.4f} bits over {J} junctions "
          f"= {ys[-1] / J:.4f} bits/junction")
    print(f"    slope(all) = {slope_all:.4f}  slope(top half) = "
          f"{slope_top:.4f} bits/octave")
    print(f"    (F1) J>=8: {f1}   (F2) strictly increasing: {f2}   "
          f"(F3) no saturation: {f3}   (F4) >=ceil(J/2) junctions up: {f4}")
    print(f"    ==> {verdict}")
    summary.append((cell, n, t, J, bal, onset, ys[0], ys[-1], ys[-1] / J,
                    slope_top, verdict))

print("\n" + "=" * 78)
print("SUMMARY (every number TOY-SCOPE; no official-row transport is licensed)")
print("=" * 78)
print(f"{'cell':>4} {'n':>4} {'t':>3} {'J':>2} {'bal':>5} {'sat q':>10} "
      f"{'Sig(low q)':>10} {'Sig(sat)':>9} {'bits/junc':>9} "
      f"{'slope_top':>9}  verdict")
for s in summary:
    print(f"{s[0]:>4} {s[1]:>4} {s[2]:>3} {s[3]:>2} {s[4]:>5g} {s[5]:>10} "
          f"{s[6]:>10.4f} {s[7]:>9.4f} {s[8]:>9.4f} {s[9]:>9.4f}  {s[10]}")

deep = max(s[3] for s in summary)
print(f"\nDEEPEST DEPTH HONESTLY ACHIEVED: J = {deep} consecutive junctions of a "
      f"single tower.\nG-b's registered depth is >= 8; it was NOT reached and "
      "nothing is extrapolated.")

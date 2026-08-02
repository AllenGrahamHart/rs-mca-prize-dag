#!/usr/bin/env python3
"""Is the Fourier-flatness surrogate SHARP, not just a bound?  (F2A.5b)

The certificate chain gives
    Lambda_k(beta) >= (beta(1-beta)/ln 2) * (1 - |R_k|),
so  eta >= min_k Lambda_k >= 0.2705 * (1 - max_k|R_k|)  at the adversarial
slice beta = 1/4.  This script asks the converse: on the adjacent-pair
(arc-w) family, driven to n >> p^2 where the asymptotic exponent is visible,
is the EXACT eta equal to that same constant times the flatness?

Exact integer V_b throughout (O(n) hypergeometric sum per slice); the
flatness 1 - max_k |R_k| is a float diagnostic of an exactly known
trigonometric quantity.
"""
from __future__ import annotations
import json, math, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import boundary as B  # noqa: E402

PRED = 0.25 * 0.75 / math.log(2)          # beta(1-beta)/ln2 at beta = 1/4
print(f"predicted slope beta(1-beta)/ln2 at beta = 1/4 : {PRED:.5f}")
print(f"{'p':>6} {'w':>3} {'n':>8} {'n/p^2':>8} {'flat = 1-max|R_k|':>18} "
      f"{'exact eta_n':>13} {'eta / flat':>11} {'vs PRED':>9}")
rows = []
for p, w, nmax in ((23, 2, 8192), (23, 2, 16384), (23, 2, 65536),
                   (41, 2, 16384), (41, 2, 32768), (41, 2, 65536)):
    n = nmax
    # window: n coordinates, Delta cycling through {0,...,w-1}
    dl = [(i % w) for i in range(n)]
    fm, fk, _ = B.flatness(p, dl)
    flat = 1 - fm
    if w == 2:
        bs = [n // 4, 3 * n // 8, n // 2, 5 * n // 8, 3 * n // 4]
        V = B.V_two_value_at(p, n // 2, n // 2, 0, 1, 0, bs)
        best, bb = None, None
        for b in bs:
            x = B.neglog2_rho(V[b], n, b)
            if x is None:
                continue
            if best is None or x < best:
                best, bb = x, b
    else:
        # general w: only the b = n/4 slice, via the (b,r) DP on a reduced n
        n = min(n, 4096)
        dl = [(i % w) for i in range(n)]
        fm, fk, _ = B.flatness(p, dl)
        flat = 1 - fm
        N = B.count_dp(p, dl)
        Vv = B.V_from_counts(p, N, n, 0)
        best, bb = B.worst_in_band(Vv, n)
    eta = best / n
    rows.append({"p": p, "w": w, "n": n, "flat": flat, "eta_n": eta,
                 "ratio": eta / flat if flat else None,
                 "predicted_slope": PRED, "worst_b": bb})
    print(f"{p:6d} {w:3d} {n:8d} {n/(p*p):8.2f} {flat:18.8f} "
          f"{eta:13.9f} {eta/flat:11.5f} {eta/flat/PRED:9.4f}")

B.dump("sharpness.json", {"rows": rows, "predicted_slope": PRED})

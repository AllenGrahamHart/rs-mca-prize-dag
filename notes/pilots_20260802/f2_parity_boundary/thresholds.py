#!/usr/bin/env python3
"""Exact thresholds for the two candidate hypothesis clauses (F2A.5b).

T1  the beta_min at which the k=p (parity) floor stops binding, per budget:
    the exact Krawtchouk exponent lambda(beta_min, beta) crossing eta.
T2  the resulting n_max(beta_min) tables at p = 23, 101 and the OFFICIAL
    p ~ 2^31, for the 1/3 and 1/43 budgets.
T3  the same for the flatness clause, using the measured lower envelope.
T4  the mode-sum prefactor M_p = (1/2p) sum_{k odd}|hhat_p(k)| and the
    startup deficit log2(M_p * kappa) that any certificate must overcome.
"""
from __future__ import annotations
import json, math, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import boundary as B  # noqa: E402

N_REF = 1024


def lam(bm, frac, n=N_REF):
    m = int(round(bm * n))
    b = int(round(frac * n))
    x = B.kp_ratio_bits(n - m, m, b)
    return (x / n) if x is not None else None


def worst_lam(bm, n=N_REF):
    """min over the central band b/n in [1/4, 3/4] of the exact exponent."""
    best = None
    for j in range(1, 11):
        frac = 0.25 + 0.5 * j / 11
        v = lam(bm, frac, n)
        if v is None:
            continue
        if best is None or v < best[0]:
            best = (v, frac)
    v = lam(bm, 0.25, n)
    if v is not None and (best is None or v < best[0]):
        best = (v, 0.25)
    return best


def solve_bm(target):
    lo, hi = 0.0, 0.5
    for _ in range(26):
        mid = 0.5 * (lo + hi)
        w = worst_lam(mid)
        if w is None or w[0] < target:
            lo = mid
        else:
            hi = mid
    return hi


print("[T1] EXACT parity threshold: the smallest beta_min at which the k=p "
      "floor alone never binds, per budget (exact Krawtchouk, n=2048)")
out = {}
for tgt, name in ((1 / 3, "1/3"), (1 / 43, "1/43")):
    bm = solve_bm(tgt)
    w = worst_lam(bm)
    out[name] = bm
    print(f"   budget {name:>4} (eta = {tgt:.5f}):  beta_min* = {bm:.5f}   "
          f"(worst slice b/n = {w[1]:.4f}, lambda = {w[0]:.5f})")

print("\n[T2] n_max under the PARITY clause only: the largest window on which "
      "the k=p floor still permits the budget.  'inf' = never binds.")
print(f"{'beta_min':>9} | " + " | ".join(
    f"{lbl:>22}" for lbl in ("p=23 (log2p=4.52)", "p=101 (6.66)",
                             "OFFICIAL p~2^31 (31)")))
print(f"{'':>9} | " + " | ".join(f"{'n(1/3)':>10}{'n(1/43)':>12}"
                                 for _ in range(3)))
rows = []
for bm in (0.0, 1 / 128, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 3 / 16, 1 / 4,
           0.28, 0.30, 1 / 3, 0.4, 0.5):
    w = worst_lam(bm)
    L = w[0]
    cells = []
    rec = {"beta_min": bm, "lambda": L, "worst_frac": w[1]}
    for lg2p, tag in ((4.5236, "p23"), (6.6582, "p101"), (31.0, "official")):
        for tgt, tn in ((1 / 3, "third"), (1 / 43, "43")):
            v = float("inf") if L >= tgt else lg2p / (tgt - L)
            rec[f"n_max_{tag}_{tn}"] = v
            cells.append(f"{v:>10.0f}" if v != float("inf") else f"{'inf':>10}")
    rows.append(rec)
    print(f"{bm:9.5f} | " + " | ".join(
        f"{cells[2*i]}{cells[2*i+1]:>12}" for i in range(3)))

print("\n[T3] the mode-sum prefactor and the startup deficit any certificate "
      "must pay: -log2 rho_b >= n*min_k Lambda_k - log2(M_p) - log2(kappa)")
print(f"{'p':>10} {'M_p':>9} {'log2 M_p':>9} {'log2 kappa(n=96,b=24)':>23} "
       f"{'total deficit (bits)':>21}")
defs = []
for p in (23, 41, 67, 101, 151, 1009, 10007, 100003):
    M = B.hhat_L1(p)
    kap = B.kappa(96, 24)
    d = math.log2(M) + math.log2(kap)
    defs.append({"p": p, "M_p": M, "log2_M_p": math.log2(M),
                 "log2_kappa": math.log2(kap), "deficit_bits": d})
    print(f"{p:10d} {M:9.4f} {math.log2(M):9.4f} {math.log2(kap):23.4f} "
          f"{d:21.4f}")

# M_p = (1/2p) sum_{k odd} |hhat_p(k)| diverges logarithmically; the exact
# values above fit M_p = a*log2 p + b with a = 2 ln2/pi = 0.44127 (the analytic
# slope).  The official-scale entry is therefore an EXTRAPOLATION of an exactly
# known asymptotic, not of an empirical trend.
xs = [math.log2(d["p"]) for d in defs]
ys = [d["M_p"] for d in defs]
nn = len(xs)
sx, sy = sum(xs), sum(ys)
sxx = sum(x * x for x in xs)
sxy = sum(x * y for x, y in zip(xs, ys))
a = (nn * sxy - sx * sy) / (nn * sxx - sx * sx)
b_ = (sy - a * sx) / nn
M31 = a * 31.0 + b_
print(f"   fit  M_p = {a:.5f}*log2 p + {b_:.5f}   (analytic slope "
      f"2 ln2/pi = {2*math.log(2)/math.pi:.5f}; max residual "
      f"{max(abs(y - a*x - b_) for x, y in zip(xs, ys)):.4f})")
print(f"   EXTRAPOLATED official p ~ 2^31:  M_p = {M31:.4f}, "
      f"log2 M_p = {math.log2(M31):.4f} bits; total startup deficit at "
      f"(n=1024, b=256) = {math.log2(M31) + math.log2(B.kappa(1024, 256)):.4f}"
      f" bits")

B.dump("thresholds.json", {"parity_threshold": out, "n_max_rows": rows,
                           "deficits": defs, "n_ref": N_REF,
                           "M_p_fit": {"a": a, "b": b_, "M_official": M31}})

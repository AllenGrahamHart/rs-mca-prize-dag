#!/usr/bin/env python3
"""D3 ATTACK on the weakest usable band floor.

A. PIGEONHOLE TIGHTNESS AT THE REAL RUNG PARAMETERS (exact, no extrapolation).
   The proved cyclic construction's supply is
       L >= ceil(C(N-1,m) / (N q^{d-1})),   m = N/2 + d,
   the 1/N coming from pigeonholing a_0(A) = (-1)^m prod_{b in A} b, which
   ranges over one coset of size N (proof.md:72-82).  For d = 1 the class of
   A is determined by  S(A) = sum of the Z_N-logs of its elements (mod N).
   So the TRUE best supply of the construction is
       Lmax(N,m) = max_t #{ A subset of Z_N\{0}, |A| = m, sum(A) = t (mod N) }
   which is EXACTLY computable by a DP.  This decides whether the 1/N
   normalizer is real (barrier) or recoverable (route).

B. IN-VIVO simple-pole conversion loss (P12/P13) on the banked sunflower
   cells: how lossy are the two steps of the L -> M conversion?

Run from repo root:
  tools/ramguard local -- python3 notes/pilots_20260809/cancellation_recon/attack.py
"""
import math
import re
import sys
import types
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

n_row = 2 ** 41
k_row = 2 ** 40


def lg2(x):
    x = int(x)
    if x <= 0:
        return float("-inf")
    b = x.bit_length()
    return math.log2(x) if b <= 900 else b - 900 + math.log2(x >> (b - 900))


print("=" * 74)
print("A.  EXACT max class size of the cyclic pigeonhole, at the rung params")
print("=" * 74)


def class_profile(N, m):
    """exact #{A in C(Z_N\\{0}, m) : sum(A) = t mod N} for every t."""
    # dp[j][t]; iterate elements 1..N-1
    dp = [[0] * N for _ in range(m + 1)]
    dp[0][0] = 1
    for e in range(1, N):
        for j in range(min(m - 1, e - 1), -1, -1):
            row, tgt = dp[j], dp[j + 1]
            for t in range(N):
                v = row[t]
                if v:
                    tgt[(t + e) % N] += v
    return dp[m]


for N in (32, 64, 128):
    m = N // 2 + 1                      # d = 1
    prof = class_profile(N, m)
    tot = sum(prof)
    assert tot == math.comb(N - 1, m), "DP wrong"
    mx, mn = max(prof), min(prof)
    guar = Fraction(math.comb(N - 1, m), N)
    c = n_row // N
    reach = 2 * c - 1
    print(f"N={N:>4} m={m:>3}  C(N-1,m)=2^{lg2(math.comb(N-1,m)):.4f}")
    print(f"        guaranteed  C(N-1,m)/N = 2^{lg2(int(guar)):.4f}")
    print(f"        TRUE max class          = 2^{lg2(mx):.4f}   "
          f"excess over guarantee = {float(mx/guar):.9f}x "
          f"({lg2(mx) - lg2(int(guar)):+.6f} bits)")
    print(f"        TRUE min class          = 2^{lg2(mn):.4f}   "
          f"spread max/min = {mx/mn:.9f}")
    print(f"        -> rung c=n/N=2^{int(math.log2(c))}, reach 2c-1 = "
          f"{reach:,} = 2^{math.log2(reach+1):.2f}; need L > q/2^128 = 2^128 "
          f"at q=2^256: {'ADMISSIBLE' if lg2(mx) > 128 else 'SHORT by %.4f bits' % (128 - lg2(mx))}")
    print()

print("CEILING ON THE WHOLE REORGANISATION: even a PERFECT pigeonhole")
print("(all C(N-1,m) subsets in one class) gives at most C(N-1,m):")
for N in (128, 256):
    m = N // 2 + 1
    print(f"  N={N:>4}: C(N-1,m) = 2^{lg2(math.comb(N-1,m)):.4f}  vs need 2^128 -> "
          f"{'still SHORT by %.4f bits' % (128 - lg2(math.comb(N-1,m))) if lg2(math.comb(N-1,m)) < 128 else 'admissible'}")

print()
print("=" * 74)
print("B.  in-vivo simple-pole conversion loss (P12/P13)")
print("=" * 74)

CORE = (HERE / "scratch_e22_core.py").read_text()
CENS = (HERE / "scratch_e22_census.py").read_text()
CENS = re.sub(r"^import modal\s*$", "", CENS, flags=re.M)
CENS = re.sub(r"^app = modal\.App.*$", "", CENS, flags=re.M)
CENS = re.sub(r"^image = .*$", "", CENS, flags=re.M)
CENS = re.sub(r"^@app\.\w+\(.*\)\s*$", "", CENS, flags=re.M)


def cell_at(q, spec):
    ns = {"__name__": "e22_core", "__file__": "/tmp/x/e22_core.py"}
    exec(CORE, ns)
    ns["P"] = q
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/x/e22_census.py"}
    exec(CENS, ns2)
    ns2["P"] = q
    n, k, sigma, layout, scalar = spec
    return ns2["exact_cell"](n, k, sigma, layout, scalar), ns2


def polyeval(poly, x, q):
    acc = 0
    for co in reversed(poly):
        acc = (acc * x + co) % q
    return acc


SPEC = (16, 8, 1, "cyclic_step_1", "linear")
LADDER = [97, 113, 193, 241, 337, 449, 577, 769, 1153]
print(f"cell {SPEC}; poles alpha in F\\D; L = exact list size at agreement k+sigma")
print(f"{'q':>6} {'L':>5} {'M_best':>7} {'M_mean':>8} {'M_guar':>7} "
      f"{'LOSS_tot':>9} {'LOSS_CS':>8} {'LOSS_avg':>9} {'colTOT/bound':>13}")
for q in LADDER:
    cell, ns2 = cell_at(q, SPEC)
    domain = ns2["subgroup_domain"](16, q)
    polys = list(cell_polys) if False else None
    # recompute the list explicitly (exact_cell returns only summaries)
    word = ns2["sunflower_word"](*SPEC)
    found = []
    import itertools
    for idx in itertools.combinations(range(16), 9):
        p = ns2["polynomial_through"](list(idx), word["domain"], word["values"], 8)
        if p is None:
            continue
        if len(ns2["agreement_set"](p, word)) >= 9:
            found.append(p)
    found = sorted(set(found))
    L = len(found)
    dom = set(word["domain"])
    poles = [a for a in range(q) if a not in dom]
    best_M, tot_M, best_S2 = 0, 0, None
    colTOT = 0
    for a in poles:
        vals = {}
        for p in found:
            v = polyeval(p, a, q)
            vals[v] = vals.get(v, 0) + 1
        M = len(vals)
        S2 = sum(r * r for r in vals.values())
        colTOT += sum(r * (r - 1) // 2 for r in vals.values())
        tot_M += M
        if M > best_M:
            best_M, best_S2 = M, S2
    kk, nn = 8, 16
    M_guar = Fraction(L * (q - nn), (q - nn) + kk * (L - 1))
    S2_bound = Fraction(L) + Fraction(kk * L * (L - 1), q - nn)
    loss_tot = best_M / float(M_guar)
    loss_cs = best_M / (L * L / best_S2)
    loss_avg = float(S2_bound) / best_S2
    colbound = kk * L * (L - 1) // 2
    print(f"{q:>6} {L:>5} {best_M:>7} {tot_M/len(poles):>8.2f} "
          f"{float(M_guar):>7.2f} {loss_tot:>9.3f} {loss_cs:>8.3f} "
          f"{loss_avg:>9.3f} {colTOT/colbound:>13.5f}")

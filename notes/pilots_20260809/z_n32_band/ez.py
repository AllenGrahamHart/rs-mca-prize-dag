#!/usr/bin/env python3
"""EZ1..EZ7 escape tests (PREREG Z3).  tools/ramguard local -- python3 ..."""
import itertools
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bbm import bbm, record, swar_params                     # noqa: E402
from zcore import (check, summary, is_prime, primes_upto,    # noqa: E402
                   rows_M2, rows_M4, tmass_exact, assert_2power_grid,
                   elt_of_order, all_elts_of_order, cell)

print("=" * 104)
print("EZ2 -- BBM vs round-24 zcore.tmass_exact, EXACT Fraction equality")
print("=" * 104)
print("%-4s %-6s %-3s %-9s | %-14s %-14s %s" %
      ("fam", "N", "k", "p", "TMASS(BBM)", "TMASS(zcore)", "match"))
nagree = 0
cells = []
for N, mod in ((8, 16), (16, 32)):
    for p in primes_upto(1 << 12 if N == 8 else 1 << 16):
        if p <= 2 * N or (p - 1) % (2 * N):
            continue
        cells.append(("M4", N, 1, p))
for S, R in ((8, 2), (16, 2), (8, 3)):
    for p in primes_upto(1 << 11):
        if p <= 2 * S or (p - 1) % (2 * S):
            continue
        cells.append(("M2", S, R, p))
cells = cells[::max(1, len(cells) // 26)][:26]
for fam, N, k, p in cells:
    assert_2power_grid(N)
    rows = rows_M4(N, p) if fam == "M4" else rows_M2(N, k, p)
    tn, nk, dp = bbm(rows, p, rbuck=7)
    a = Fraction(tn, 1 << N)
    b = tmass_exact(rows, p)
    ok = (a == b)
    nagree += ok
    print("%-4s %-6d %-3d %-9d | %-14s %-14s %s" % (fam, N, k, p, a, b, ok))
check("EZ2 BBM == zcore.tmass_exact EXACTLY on %d cells at N in {8,16}" % len(cells),
      nagree == len(cells), "%d/%d" % (nagree, len(cells)))

# ---- the round-24 record cell, replayed
p = 161761
rows = rows_M4(16, p)
tn, nk, dp = bbm(rows, p, rbuck=13)
d = record(rows, p, tn, nk, "M4", "round24-record")
check("EZ2/P-Z9 record cell N=16 p=161761 TMASS == 159/64",
      d["TMASS"] == Fraction(159, 64), "TMASS=%s CRATIO=%.10f NKER=%d"
      % (d["TMASS"], d["CRATIO"], d["NKER"]))
check("EZ2/P-Z9 record cell CRATIO == 1.7680688810",
      abs(d["CRATIO"] - 1.7680688810) < 5e-10, "%.10f" % d["CRATIO"])
check("EZ2 record cell NKER == 289 (round-24 |ker cap T|)", nk == 289, "NKER=%d" % nk)

print()
print("=" * 104)
print("EZ3 -- degenerate identity: all columns == 0  =>  TMASS = 2^N exactly")
print("=" * 104)
for N in (8, 16):
    rows = [[0] * N]
    tn, nk, dp = bbm(rows, 97, rbuck=3)
    check("EZ3 N=%d all-zero columns TMASS = 2^N" % N,
          Fraction(tn, 1 << N) == (1 << N) and nk == 3 ** N,
          "TMASS=%s NKER=%d (3^%d=%d)" % (Fraction(tn, 1 << N), nk, N, 3 ** N))

print()
print("=" * 104)
print("EZ4 -- bucket independence: TNUM bit-identical across RBUCK")
print("=" * 104)
for (N, p) in ((16, 161761), (16, 65537)):
    vals = []
    for rb in (1, 5, 64, 256):
        tn, nk, dp = bbm(rows_M4(N, p), p, rbuck=rb)
        vals.append((rb, tn, nk, dp))
    ok = len(set(v[1] for v in vals)) == 1 and len(set(v[2] for v in vals)) == 1
    check("EZ4 N=%d p=%d TNUM,NKER identical over RBUCK in {1,5,64,256}" % (N, p), ok,
          " ".join("R%d:dpeak=%d" % (v[0], v[3]) for v in vals))

print()
print("=" * 104)
print("EZ5 -- negation identity  sum_r D1[r]D2[r] == sum_r D1[r]D2[-r]  (full-dict, N<=16)")
print("=" * 104)


def full_dicts(rows, p):
    from bbm import build_table, swar_params
    kappa = len(rows)
    N = len(rows[0])
    h = N // 2
    W, G, K = swar_params(p, kappa)
    assert kappa == 1
    D1, D2 = {}, {}
    for (idxs, D) in ((range(0, h), D1), (range(h, N), D2)):
        cols = [rows[0][j] % p for j in idxs]
        T = build_table(cols, p, 1, W, G, K)
        for kv, m in T:
            D[kv] = D.get(kv, 0) + m
    return D1, D2


for (N, p) in ((8, 257), (16, 161761), (16, 65537)):
    D1, D2 = full_dicts(rows_M4(N, p), p)
    a = sum(v * D2.get(r, 0) for r, v in D1.items())
    b = sum(v * D2.get((p - r) % p, 0) for r, v in D1.items())
    tn, nk, dp = bbm(rows_M4(N, p), p, rbuck=8)
    check("EZ5 N=%d p=%d  D2 negation-symmetric and both joins == TNUM" % (N, p),
          a == b == tn, "a=%d b=%d TNUM=%d" % (a, b, tn))

print()
print("=" * 104)
print("EZ1 / EZ6 -- Z-FLOOR and RC(i) on the N=16 in-band line")
print("=" * 104)
bad = 0
seen = 0
worst = None
for p in primes_upto(1 << 18):
    if p < (1 << 14) or p <= 32 or (p - 1) % 32:
        continue
    rows = rows_M4(16, p)
    tn, nk, dp = bbm(rows, p, rbuck=4)
    tm = Fraction(tn, 1 << 16)
    seen += 1
    if tm < Fraction(1 << 16, p):
        bad += 1
    d = cell(rows, p, want_AU=True)
    if d["UMIN"] is not None:
        sl = d["UMIN"] / p ** (2.0 / 16)
        if worst is None or sl < worst[0]:
            worst = (sl, p, d["UMIN"])
    if d["TMASS"] != tm:
        print("MISMATCH vs zcore at p=%d" % p)
        bad += 1000
check("EZ1 Z-FLOOR TMASS >= 2^N/p^kappa on the whole N=16 in-band line (%d cells)" % seen,
      bad == 0, "violations %d" % bad)
check("EZ6/RC(i) UMIN >= p^{2/N} on the N=16 in-band line", worst is None or worst[0] >= 1.0,
      "tightest slack x%.4f at p=%d (UMIN=%d)" % (worst[0], worst[1], worst[2]) if worst else "")

print()
print("EZ6 -- grid asserts")
try:
    assert_2power_grid(32)
    assert_2power_grid(16)
    ok = True
except AssertionError:
    ok = False
check("EZ6 CATCH-Z6 2N a 2-power at N in {16,32}", ok, "2N = 32, 64")
try:
    rows_M2(32, 2, 193)
    ok2 = True
except AssertionError:
    ok2 = False
check("EZ6 CATCH-19B 0 not in Lambda (asserted inside rows_M2/rows_M4)", ok2)

sys.exit(summary())

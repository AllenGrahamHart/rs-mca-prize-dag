#!/usr/bin/env python3
"""CATCH-23A ISOLATION: is round-22's d4_cone.py Fincke-Pohst enumerator
fail-closed?  Adjudicated by EXHAUSTIVE brute force over the whole box.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260807/ge_lattice_cert/catch_d4cone.py
"""
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))

import latlib as LL                                       # noqa: E402
import d4_cone                                            # noqa: E402

ROWS = [
    (4, 137, 8), (4, 401, 8), (8, 12289, 6),
    (8, 12289, 16), (8, 463249, 16), (8, 463457, 16),
]

print("== CATCH-23A: d4_cone.py (round 22) vs EXHAUSTIVE brute force ==")
print("   same lattice, same root (both call zeta_of_order(2h,p)), same box.\n")
print("%-4s %-9s %-5s %-10s %-10s %-10s %-9s" %
      ("h", "p", "2l'", "r22 #w", "BRUTE #w", "mine #w", "verdict"))
bad = []
for (h, p, L) in ROWS:
    z = LL.zeta_of_order(2 * h, p)
    cvec = [pow(z, j, p) for j in range(h)]
    w22, n22 = d4_cone.certify(h, p, L)
    bf = sorted(LL.brute_box(h, p, cvec, L))
    B = LL.coeff_basis(h, p, cvec)
    sp = os.path.join(HERE, "state", "c_%d_%d_%d.lll.json" % (h, p, L))
    ep = os.path.join(HERE, "state", "c_%d_%d_%d.enum.json" % (h, p, L))
    for f in (sp, ep):
        if os.path.exists(f):
            os.remove(f)
    import time
    st, info = LL.lll_resumable(sp, B, "c", [(3, 4), (99, 100)],
                                time.time() + 1e9, log=lambda *a: None)
    st2, info2 = LL.enum_resumable(ep, info["B"], min(4 * h, 2 * L), L, "c",
                                   time.time() + 1e9, log=lambda *a: None)
    mine = sorted(info2["found"])
    v = "AGREE" if sorted(w22) == bf else "**r22 MISSES %d**" % (
        len(bf) - len(w22))
    if sorted(w22) != bf:
        bad.append((h, p, L, len(w22), len(bf)))
    assert mine == bf, "MY enumerator disagrees with brute force!"
    print("%-4d %-9d %-5d %-10d %-10d %-10d %-9s"
          % (h, p, L, len(w22), len(bf), len(mine), v))

print("\n-- the missed vectors at (h=4, p=137, 2l'=8) --")
h, p, L = 4, 137, 8
z = LL.zeta_of_order(8, p)
cvec = [pow(z, j, p) for j in range(h)]
w22, _ = d4_cone.certify(h, p, L)
bf = sorted(LL.brute_box(h, p, cvec, L))
miss = [w for w in bf if w not in w22]
for w in miss:
    print("   MISSED by d4_cone: w = %s   sum w_j z^j mod p = %d"
          % (str(w), sum(w[j] * cvec[j] for j in range(h)) % p))

print("\n-- MECHANISM: the per-level integer window in d4_cone.certify --")
print("""   d4_cone.py:116-118 computes the half-width as

       hi = 0
       while Fraction((hi + 1) ** 2) <= lim:   hi += 1

   i.e.  hi = floor(sqrt(lim))  -- an INTEGER -- and then scans
   x_i in [ceil(-c - hi), floor(-c + hi)]   (d4_cone.py:119-124).

   The true Fincke-Pohst window is |x_i + c| <= sqrt(lim) with c RATIONAL,
   so the admissible interval has half-width sqrt(lim), not floor(sqrt(lim)).
   Whenever sqrt(lim) is not an integer the window is TRUNCATED by
   sqrt(lim) - floor(sqrt(lim)) < 1 on each side, which can drop an integer
   x_i.  The enumeration is therefore NOT fail-closed: it can miss lattice
   points, and a '0 witnesses' answer from it is not by itself a proof of
   emptiness.""")

print("\n-- demonstration of the truncation on a concrete level --")
B = LL.coeff_basis(h, p, cvec)
Br, Bs, mu = d4_cone.lll(B)
for i in range(h - 1, -1, -1):
    bi = d4_cone.dot(Bs[i], Bs[i])
    lim = Fraction(min(4 * h, 2 * L)) / bi
    from math import isqrt as _isq
    tr = 0
    while Fraction((tr + 1) ** 2) <= lim:
        tr += 1
    print("   level %d: ||b*_i||^2 = %s, lim = %s ~ %.4f, true half-width "
          "sqrt(lim) = %.4f, d4_cone uses %d  -> loses %.4f per side"
          % (i, bi, lim, float(lim), float(lim) ** 0.5, tr,
             float(lim) ** 0.5 - tr))

print("\nSUMMARY: %d of %d round-22 D4 rows are under-reported: %s"
      % (len(bad), len(ROWS), bad))

print("\n-- STRUCTURAL CONFIRMATION: every witness set MUST be closed under")
print("   the negacyclic shift sigma (Lambda_p is an ideal) and under -1. --")
sys.path.insert(0, HERE)
from symmetry import sigma, orbits                        # noqa: E402
for (h, p, L) in [(4, 137, 8), (8, 12289, 16), (8, 463249, 16)]:
    z = LL.zeta_of_order(2 * h, p)
    cvec = [pow(z, j, p) for j in range(h)]
    w22, _ = d4_cone.certify(h, p, L)
    bf = set(LL.brute_box(h, p, cvec, L))
    s22 = set(w22)
    cl = all(sigma(w) in s22 for w in s22)
    print("   h=%-3d p=%-8d : r22 set has %d elements, sigma-closed? %-6s ; "
          "true set has %d = one orbit of size 2h=%d, sigma-closed? %s"
          % (h, p, len(s22), cl, len(bf), 2 * h,
             all(sigma(w) in bf for w in bf)))
print("   => round-22's own output was already detectably incomplete: a")
print("      sigma-orbit cannot be reported in part.")

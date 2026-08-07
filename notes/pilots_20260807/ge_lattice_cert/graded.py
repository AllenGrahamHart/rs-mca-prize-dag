#!/usr/bin/env python3
"""RADIUS-GRADED certification at the REAL deployed Proth rows.

The full folded box at N'=128 is out of reach at 167-171-bit primes
(FPPRICE ~ 2^60 with LLL).  But the certification question is graded by the
support bound 2l':  a witness with ||w||_1 <= L has ||w||_2^2 <= 2L, so a
COMPLETE enumeration of the ball of radius sqrt(2L) certifies

    K_p has NO non-cyclotomic ternary kernel vector of support <= L.

That is exactly the C-4 anchor's form (banked at L = 6, toy prime 12289),
now at the four literal deployed prize primes.  This prices L, and the
runner certifies the largest L that fits the compute law.

Named functional: GRADEDPRICE(row, L) = FPPRICE(64, log2 p, sqrt(2L), delta).
"""
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))
import cells as C                                         # noqa: E402
import latlib as LL                                       # noqa: E402
from d4_price import fpcost                               # noqa: E402

print("== GRADEDPRICE: cost of certifying support <= L at the four deployed "
      "Proth rows (h=64) ==")
print("   (R^2 = min(4h, 2L); L = 128 is the full box)")
print("%-6s %-8s %-10s %-12s %-12s %-12s %-12s"
      % ("L", "R", "log2BOX", "1/2 (2^166.5)", "1/4 (2^168.1)",
         "1/8 (2^169.4)", "1/16 (2^170.5)"))
for L in (6, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64, 80, 96, 128):
    R2 = min(4 * 64, 2 * L)
    R = math.sqrt(R2)
    bc = LL.boxcount(64, L)
    row = []
    for c in C.EXTENSION:
        lp = math.log2(c["p"])
        row.append(fpcost(64, lp, R, 1.0219)[0])
    print("%-6d %-8.3f 2^%-8.2f %-12s %-12s %-12s %-12s"
          % (L, R, math.log2(bc),
             *["2^%.1f" % t for t in row]))

print("\n-- and the CLASSHEUR at each L for the smallest deployed prime "
      "(2^166.503): log2((BOXCOUNT(64,L)-1)/p) --")
p = C.EXTENSION[0]["p"]
for L in (6, 16, 32, 48, 64, 96, 128):
    bc = LL.boxcount(64, L)
    print("   L=%-4d log2 BOXCOUNT = %-9.2f  CLASSHEUR = 2^%-8.2f  %s"
          % (L, math.log2(bc), math.log2(bc - 1) - math.log2(p),
             "emptiness expected" if math.log2(bc - 1) < math.log2(p)
             else "WITNESSES EXPECTED"))
print("\n   (the crossover L where BOXCOUNT(64,L) = p is where the heuristic")
print("    stops predicting emptiness -- below it, emptiness is generic;")
print("    a graded certificate below the crossover is the meaningful one.)")
lo, hi = 1, 128
while lo < hi:
    mid = (lo + hi) // 2
    if LL.boxcount(64, mid) >= p:
        hi = mid
    else:
        lo = mid + 1
print("   crossover at L = %d for p = 2^%.3f" % (lo, math.log2(p)))

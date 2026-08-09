#!/usr/bin/env python3
"""ALG-3 (spot check only): the character sum of round-24's S2,
   TMASS = (2^N/p^kappa) * sum_u prod_j cos^2(pi <u,col_j>/p),  all terms >= 0.

Registered in PREREG Z1.0(iv) as REJECTED for the N=32 band (p^kappa terms,
>= 1e9 at every in-band cell) and retained only as an extra check where p^kappa
is small.  Run here on the N<=16 ladder anchors, including the round-24 record
cell, as a THIRD independent algorithm for the ladder's N=16 end.
"""
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bbm import bbm                                          # noqa: E402
from zcore import rows_M4, rows_M2, check, summary           # noqa: E402


def tmass_char(rows, p):
    kappa = len(rows)
    assert kappa == 1, "kappa=1 only (p^kappa terms)"
    N = len(rows[0])
    cols = [c % p for c in rows[0]]
    tot = 0.0
    cmp_ = math.cos
    pi_p = math.pi / p
    for u in range(p):
        g = 1.0
        for c in cols:
            x = cmp_(pi_p * ((u * c) % p))
            g *= x * x
            if g < 1e-300:
                g = 0.0
                break
        tot += g
    return tot * (2.0 ** N) / p


for (N, p, tag) in ((8, 17, "ladder N=8"), (8, 97, "ladder N=8"),
                    (16, 161761, "ROUND-24 RECORD"), (16, 65537, "ladder N=16"),
                    (16, 130817, "ladder N=16")):
    rows = rows_M4(N, p)
    tn, nk, dp = bbm(rows, p, rbuck=4)
    exact = Fraction(tn, 1 << N)
    ch = tmass_char(rows, p)
    rel = abs(ch - float(exact)) / float(exact)
    check("ALG-3 character sum == BBM at N=%d p=%d (%s)" % (N, p, tag), rel < 1e-9,
          "exact %s = %.12f   char %.12f   rel err %.2e" % (exact, float(exact), ch, rel))

print()
print("N=32 in-band feasibility of ALG-3, as registered: the smallest in-band")
print("p^kappa over the whole reached grid is 2^30 = 1.07e9 (Tier 1, sigma=+2)")
print("and 193^4 = 1.39e9 (Tier 2); at ~32 cos evaluations per term that is")
print(">= 3.4e10 float ops per cell in pure Python.  NOT RUN at N=32.")
sys.exit(summary())

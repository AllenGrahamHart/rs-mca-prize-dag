#!/usr/bin/env python3
import sys
sys.path.insert(0, "notes/pilots_20260811/rh_moving_kernel")
from e2_exhibit_and_stratum import (cat, nullspace, rank, gcd_of_space,
                                    recurrence_space, irreducibles, trim)
q, R, r, p = 13, 8, 6, 4
irr = irreducibles(p, q)
P = irr[0]
B = recurrence_space(P, R, q)
print("P =", P)
print("recurrence basis:", B)
y0 = [(B[0][m] + 3 * B[1][m] + 5 * B[3][m]) % q for m in range(R)]
y1 = [(2 * B[0][m] + B[2][m]) % q for m in range(R)]
print("y0 =", y0, " y1 =", y1)
st = cat(y0, R, r) + cat(y1, R, r)
print("stacked rank =", rank(st, q), " expected p =", p)
K0 = nullspace(st, q)
print("dim K0 =", len(K0))
for v in K0:
    print("  ", v)
print("gcd(K0) =", gcd_of_space(K0, q))

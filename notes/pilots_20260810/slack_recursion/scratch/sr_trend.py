#!/usr/bin/env python3
"""sr_trend: the SUPPLY VERDICT table (D3).

Exact integers / exact log2 for:
  PLATEAU(n)   = C(n/2-1, n/4)                     slack-0 max list (t=1)
  PRODW(n)     = C(n, n/2+1)/n                     PRODUCT WORD theorem (lower)
  CWUB(n)      = C(n, n/2)/(n/2+1) = 2*PRODW(n)    distance-4 constant-weight
                                                    (Johnson) upper bound
  the surplus over the plateau in bits, against the razor need 4.7286..4.8286.
"""
import json, sys
from math import comb, log2

rows = []
for r in range(3, 9):
    n = 1 << r
    k = n // 2
    a = k + 1
    m = n - a
    plateau = comb(m, n // 4)
    assert plateau == comb(n // 2 - 1, n // 4)
    tot = comb(n, a)
    assert tot % n == 0, (n, tot % n)
    prod = tot // n
    ub = comb(n, k) // (k + 1) if comb(n, k) % (k + 1) == 0 else comb(n, k) / (k + 1)
    rows.append(dict(
        n=n, k=k, a=a, N_quotient=n // 2, h=n // 4,
        PLATEAU=str(plateau), lg_PLATEAU=round(log2(plateau), 4),
        PRODW=str(prod), lg_PRODW=round(log2(prod), 4),
        UB_cw=str(ub), lg_UB=round(log2(float(ub)), 4),
        surplus_bits_lower=round(log2(prod) - log2(plateau), 4),
        surplus_bits_upper=round(log2(float(ub)) - log2(plateau), 4),
        razor_need_lo=4.7286, razor_need_hi=4.8286,
        beats_razor=(log2(prod) - log2(plateau)) > 4.8286,
        UB_over_LB_bits=round(log2(float(ub) / prod), 4)))
out = dict(object="MAXWORD_LIST(n) for n=2^r, t=1, a=k+1, D=mu_n",
           theorem="C(n,a)/n <= MAXWORD_LIST(n) <= C(n,a-1)/a = 2*C(n,a)/n",
           exact_at_n8=7, rows=rows)
print(json.dumps(out, indent=1))
if len(sys.argv) > 1:
    with open(sys.argv[1], "w") as f:
        json.dump(out, f, indent=1)

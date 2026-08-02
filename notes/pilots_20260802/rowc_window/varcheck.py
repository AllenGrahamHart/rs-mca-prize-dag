#!/usr/bin/env python3
"""RowC window pilot -- instrument check: the EXACT second-moment identity of
moments.py, evaluated at the toy shapes and compared with the measured
variance of N in TOY.json.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/varcheck.py

This is the validation that licenses using the same identity at RowC 1/4,
where no measurement is possible.
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from math import comb

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))


def exact(n, A, K, q):
    h = A - K
    C = comb(n, A)
    Q = Fraction(q)
    mu = Fraction(C) / Q ** (h - 1)
    Sh0 = 0
    Shi = Fraction(0)
    for c in range(K + 1, A):
        t = comb(A, c) * comb(n - A, A - c)
        Sh0 += t
        Shi += Fraction(t) * Q ** (K + c - 2 * A)
    var = mu + Q * C * Shi - Q * C * Q ** (-2 * h) * (1 + Sh0)
    Slow = C - 1 - Sh0
    Ep2 = Q * C * Fraction(Slow) * Q ** (-2 * h) / 2
    Score = sum(comb(A, c) * comb(n - A, A - c) for c in range(K, A + 1))
    Ehi = Fraction(q * (q - 1), 2) * C * Fraction(Score) * Q ** (-2 * h)
    Egate = (q + 1) * Fraction(comb(n, A + 1)) * Q ** (K - A - 1)
    return dict(mu=float(mu), var=float(var), Ep2low=float(Ep2),
                Ehi_diff=float(Ehi), Egate=float(Egate),
                var_over_mu=float(var / mu))


def main():
    data = json.load(open(os.path.join(HERE, "TOY.json")))
    print("%-4s %20s %10s %10s %10s %10s %10s %10s" %
          ("cfg", "(n,A,K,h,q)", "mu exact", "E[N] meas", "Var exact",
           "Var meas", "Var ratio", "gate ex/ms"))
    rows = []
    for r in data:
        c = r["cfg"]
        n, A, K, h, q = c["n"], c["A"], c["K"], c["h"], int(c["q"])
        ex = exact(n, A, K, q)
        meas_gate = 1 - r["frac_admissible"]
        rows.append(dict(name=c["name"], exact=ex, measured=r))
        print("%-4s %20s %10.4f %10.4f %10.4f %10.4f %10.4f %6.4f/%6.4f" %
              (c["name"], "(%d,%d,%d,%d,%d)" % (n, A, K, h, q),
               ex["mu"], r["E_N"], ex["var"], r["Var_N"],
               r["Var_N"] / ex["var"], ex["Egate"], meas_gate))
    print()
    print("Gamma_lo vs the exact high-core prediction (toy contamination):")
    print("%-4s %12s %12s %12s %12s %12s" %
          ("cfg", "E[live]", "E[Glo]", "E[Ghi]", "2*E[hi pairs]",
           "cond ratio"))
    for r in data:
        c = r["cfg"]
        n, A, K = c["n"], c["A"], c["K"]
        pc = r["predicted"]["P_core_ge_K"]
        mu = r["predicted"]["mu"]
        print("%-4s %12.4f %12.4f %12.4f %12.4f %12.4f" %
              (c["name"], r["E_live"], r["E_gamma_lo"], r["E_gamma_hi"],
               2 * mu * mu * pc / 2, r["cond_ratio_gamma_lo"]))
    with open(os.path.join(HERE, "VARCHECK.json"), "w") as fh:
        json.dump(rows, fh, indent=1, default=str)
    print("\nwrote VARCHECK.json")


if __name__ == "__main__":
    main()

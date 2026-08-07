#!/usr/bin/env python3
"""D1 + reachability map: the ROW LIST, priced.

Named functionals (PREREG P0):
  BOXCOUNT(h,L), CLASSHEUR = (BOXCOUNT-1)/p, GHRATIO = R/lambda_1^GH,
  MAXNORMCEIL(h) = (4h)^{h/2}, FPPRICE(n, log2 det, R, delta) = log2 of the
  Fincke-Pohst node count under the GSA (round-22 d4_price.py's model,
  reused verbatim).
"""
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'ge_floor_falsifier')))

import latlib as LL                                       # noqa: E402
import cells as C                                         # noqa: E402
from d4_price import fpcost                               # noqa: E402 (round 22)

DELTAS = [(1.0219, "LLL"), (1.0128, "BKZ-20"), (1.0094, "BKZ-45"),
          (1.0060, "BKZ-90")]


def gh(n, logdet2):
    return math.sqrt(n / (2 * math.pi * math.e)) * 2 ** (logdet2 / n)


def row(cid, kind, h, L, p, plab, extra=""):
    R2 = min(4 * h, 2 * L)
    R = math.sqrt(R2)
    lp = math.log2(p)
    bc = LL.boxcount(h, L)
    ch = math.log2(bc - 1) - lp
    g = gh(h, lp)
    prices = []
    for (d, nm) in DELTAS:
        c, pk = fpcost(h, lp, R, d)
        prices.append(c)
    print("%-12s %-9s %-4d %-5d %-8.1f %-7.2f %-8.2f %-8.3f %-9.1f  "
          "%-7.1f %-7.1f %-7.1f %-7.1f  %s"
          % (cid, kind, h, L, lp, R, math.log2(bc), R / g, ch,
             prices[0], prices[1], prices[2], prices[3], plab + extra))
    return dict(cid=cid, h=h, L=L, lp=lp, R=R, boxlog=math.log2(bc),
                ghratio=R / g, classheur=ch, prices=prices)


def main():
    print("=" * 128)
    print("D1 -- THE ROW LIST, PRICED.   R^2 = min(4h, 2*2l');  "
          "lambda_1^GH = sqrt(n/2 pi e) p^(1/n)")
    print("CLASSHEUR = log2((BOXCOUNT(h,2l')-1)/p) = log2 E[#nonzero folded "
          "box classes in K_p].  <0 means emptiness is the generic truth.")
    print("=" * 128)
    print("%-12s %-9s %-4s %-5s %-8s %-7s %-8s %-8s %-9s  %-7s %-7s %-7s "
          "%-7s  %s"
          % ("cell", "kind", "h", "2l'", "log2 p", "R", "log2BOX", "R/lam1",
             "CLASSHEUR", "LLL", "BKZ20", "BKZ45", "BKZ90", "prime"))
    print("-" * 128)
    out = {}
    for c in C.PINNED:
        out[c["cid"]] = row(c["cid"], "PINNED", c["h"], c["L"], c["p"],
                            "e1 named exhibit field (250-bit)")
    for c in C.EXTENSION:
        out[c["cid"]] = row(c["cid"], "EXTENSION", c["h"], c["L"], c["p"],
                            "deployed Proth rate-%s row" % c["rate"])
    for c in C.ANCHOR:
        out[c["cid"]] = row(c["cid"], "PRICED", c["h"], c["L"], c["p"],
                            c["plabel"])
    row("corridor", "EXHIBIT", 64, 128, C.QCORR, "corridor literal prime")
    print("-" * 128)

    print("\n-- MAXNORMCEIL: the rigorous AM-GM norm ceiling (4h)^{h/2} --")
    for h in (4, 8, 64, 128, 256):
        print("   h=%-4d  (4h)^{h/2} = 2^%-9.3f   "
              "(a row with log2 p above this is certified FREE)"
              % (h, (h / 2.0) * math.log2(4 * h)))

    print("\n-- FPPRICE(h=64, R=16) as a function of log2 p:  where does the")
    print("   round-22 'laptop-scale per row' claim actually hold? --")
    print("   %-10s %-9s %-9s %-9s %-9s %-9s"
          % ("log2 p", "R/lam1", "LLL", "BKZ-20", "BKZ-45", "BKZ-90"))
    for lp in (140, 160, 167, 171, 180, 190, 200, 210, 220, 230, 240, 250,
               256, 260):
        g = gh(64, lp)
        cs = [fpcost(64, lp, 16.0, d)[0] for (d, _) in DELTAS]
        print("   %-10d %-9.3f %-9.1f %-9.1f %-9.1f %-9.1f"
              % (lp, 16.0 / g, cs[0], cs[1], cs[2], cs[3]))
    # crossover: smallest log2 p for which LLL price <= 2^30
    lo, hi = 140.0, 300.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if fpcost(64, mid, 16.0, 1.0219)[0] <= 30.0:
            hi = mid
        else:
            lo = mid
    print("\n   FPPRICE(LLL) crosses 2^30 nodes at log2 p = %.1f;" % hi)
    lo2, hi2 = 140.0, 300.0
    for _ in range(60):
        mid = (lo2 + hi2) / 2
        if fpcost(64, mid, 16.0, 1.0219)[0] <= 40.0:
            hi2 = mid
        else:
            lo2 = mid
    print("   crosses 2^40 nodes at log2 p = %.1f." % hi2)
    print("   The four deployed Proth rows sit at log2 p = %s."
          % ", ".join("%.1f" % math.log2(c["p"]) for c in C.EXTENSION))


if __name__ == "__main__":
    main()

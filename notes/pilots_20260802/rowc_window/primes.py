#!/usr/bin/env python3
"""RowC window pilot -- part 4: how many admissible primes are in each band,
and explicit ones.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/primes.py

The bands are intervals of q; the row's own descriptor requires q prime,
n | q-1, q < 2^256.  Counts use the prime-number theorem in arithmetic
progressions,  pi(x; n, 1) ~ li(x)/phi(n)  -- a heuristic for the prize rows'
1e-8-bit-wide bands (far below any unconditional short-interval result) and
essentially certain for the RowC bands, which are 33 and 7.8 binary orders
wide.  Explicit primes are exhibited (certified by sympy.isprime) at the RowC
1/4 band ends, so the RowC verdict does not rest on the heuristic at all.
"""

from __future__ import annotations

import json
import os
import sys

sys.dont_write_bytecode = True

from mpmath import mp, mpf, li, log, exp  # noqa: E402
from sympy import isprime, totient  # noqa: E402

mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
LN2 = log(mpf(2))

BANDS = [
    # (row, n, lo_log2, hi_log2, label)
    ("RowC 1/4", 1024, "166.998846866", "200.113029521", "program band"),
    ("RowC 1/4", 1024, "192.290423616", "200.113029521", "sound sub-band"),
    ("RowC 1/8", 1024, "113.693350434", "133.183389935", "bare band only"),
    ("RowC 1/16", 1024, "118.834056376", "159.843628428", "bare band only"),
    ("prize 1/4", 1 << 41, "209.2571859719226392599",
     "209.2571859814340184307", "bare band only"),
    ("prize 1/8", 1 << 41, "141.9343163607043275598",
     "141.9343163622384266194", "bare band only"),
    ("prize 1/16", 1 << 41, "176.5755899096156853148",
     "176.5755899204926254551", "bare band only"),
]


def main():
    out = []
    print("%-11s %-16s %14s %14s %16s %16s" %
          ("row", "band", "lo log2 q", "hi log2 q", "integers", "primes=1 mod n"))
    for row, n, lo, hi, lab in BANDS:
        LO, HI = mpf(lo), mpf(hi)
        qlo, qhi = exp(LO * LN2), exp(HI * LN2)
        ints = qhi - qlo
        cnt = (li(qhi) - li(qlo)) / mpf(int(totient(n)))
        out.append(dict(row=row, band=lab, lo_log2=str(LO), hi_log2=str(HI),
                        log2_integers=str(log(ints) / LN2),
                        log2_primes=str(log(cnt) / LN2) if cnt > 0 else None))
        print("%-11s %-16s %14s %14s %16s %16s" %
              (row, lab, mp.nstr(LO, 12), mp.nstr(HI, 12),
               "2^" + mp.nstr(log(ints) / LN2, 6),
               "2^" + mp.nstr(log(cnt) / LN2, 6)))

    print()
    print("explicit certified primes q = 1 mod 1024 inside the RowC 1/4 band:")
    pts = [("just above the tangent gate", "167.02"),
           ("gate slack 2^-20", "171.0"),
           ("L1 (row-sound floor)", "192.30"),
           ("mid sound band", "196.0"),
           ("just under L3", "200.10")]
    ex = []
    for lab, lq in pts:
        x = int(exp(mpf(lq) * LN2))
        q = x + ((1 - x) % 1024)
        while not isprime(q):
            q += 1024
        ex.append(dict(label=lab, log2_target=lq, q=str(q),
                       log2_q=str(log(mpf(q)) / LN2)))
        print("  %-28s q = %d" % (lab, q))
        print("  %-28s   (log2 q = %s)" % ("", mp.nstr(log(mpf(q)) / LN2, 14)))
    with open(os.path.join(HERE, "PRIMES.json"), "w") as fh:
        json.dump(dict(bands=out, explicit=ex), fh, indent=1)
    print("\nwrote PRIMES.json")


if __name__ == "__main__":
    main()

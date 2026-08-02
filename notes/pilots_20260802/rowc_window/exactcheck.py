#!/usr/bin/env python3
"""RowC window pilot -- part 7: the GRID-FREE closure of the admissible family.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/exactcheck.py

sweep.py samples log2 q on a 0.25 grid.  Here the same conclusion is reached
with no grid at all.

For a fixed agreement A the two banked q-conditions are monotone in
B* = floor(q/2^128), so the admissible q-interval of the CELL (A, q) is
exactly

    q_min(A) = 2^128 * ( B_quot_ub(A) + (n-A+1) + 16 n^3 )   [the GATE]
    q_max(A) = 2^128 * ( maxcensus(A-1) + 1 )                [A-1 unsafe]

(both banked verbatim in
 critical/nodes/xr_smallcore_spread_count/notes/
 audit_consumption_replay_20260710.py:52-89,108-112,129-130),
and mu(q) = C(n,A) q^{1-h} is strictly decreasing in q, so

    sup over the cell of the random low-core supply  =  mu(q_min(A)).

Comparing that supremum with 8 n^3 for every cell decides the entire
admissible family with no sampling.  The cells tile the q-axis, so the union
of the cells IS the admissible family.

Prize rows: maxcensus is evaluated in 60-digit Stirling (the exact binomials
have ~10^12 digits when the active dyadic scale is large); exact integers are
used for every quantity that enters a verdict, which at the feasible cells
means every active scale has np <= 256 (asserted).
"""

from __future__ import annotations

import json
import os
import sys
from math import comb

sys.dont_write_bytecode = True

from mpmath import mp, mpf, log, loggamma  # noqa: E402

mp.dps = 60
LN2 = log(mpf(2))
HERE = os.path.dirname(os.path.abspath(__file__))

ROWC = [("RowC 1/4", 1 << 10, 1 << 8, 261),
        ("RowC 1/8", 1 << 10, 1 << 7, 133),
        ("RowC 1/16", 1 << 10, 1 << 6, 67)]
PRIZE = [("prize 1/4", 1 << 41, 1 << 39, 558345748481),
         ("prize 1/8", 1 << 41, 1 << 38, 283467841537),
         ("prize 1/16", 1 << 41, 1 << 37, 141733920769)]


def lgb(n, r):
    if r < 0 or r > n:
        return mpf("-inf")
    if n <= 4096:
        return log(mpf(comb(n, r))) / LN2
    return (loggamma(mpf(n + 1)) - loggamma(mpf(r + 1))
            - loggamma(mpf(n - r + 1))) / LN2


def scales(n, k, A):
    t, out, np_ = A - k, [], 2
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            out.append((np_, lp))
        np_ *= 2
    return out


def mxlog(n, k, A):
    s = scales(n, k, A)
    return max([lgb(a, b) for a, b in s] or [mpf("-inf")])


def cell(n, k, A, b8):
    sc = scales(n, k, A)
    assert all(a <= 4096 for a, _ in sc), "exact census unavailable"
    need = sum(comb(a, b) for a, b in sc) + (n - A + 1) + 16 * n ** 3
    qmin = need << 128
    lqmin = log(mpf(qmin)) / LN2
    lqmax = mxlog(n, k, A - 1) + 128
    feas = bool(lqmin < lqmax and qmin < (1 << 256))
    h = A - k
    lmu = lgb(n, A) - (h - 1) * lqmin
    return dict(A=A, h=h, feasible=feas, log2_qmin=float(lqmin),
                log2_qmax=float(lqmax), log2_mu_sup=float(lmu),
                slack_bits=b8 - float(lmu),
                over_budget=bool(feas and float(lmu) > b8))


def candA(n, k, lgB):
    """smallest A with maxcensus(A) <= 2^lgB (maxcensus is non-increasing)."""
    lo, hi = k + 1, k + (1 << 35)
    if mxlog(n, k, lo) <= lgB:
        return lo
    assert mxlog(n, k, hi) <= lgB
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if mxlog(n, k, m) > lgB:
            lo = m
        else:
            hi = m
    return hi


def main():
    out = {}
    for name, n, k, Ab in ROWC:
        b8 = 3 + 3 * (n.bit_length() - 1)
        cells = []
        for A in range(k + 1, k + 41):
            if not scales(n, k, A):
                break
            try:
                cells.append(cell(n, k, A, b8))
            except AssertionError:
                cells.append(dict(A=A, feasible=False, note="census too large"))
        feas = [c for c in cells if c.get("feasible")]
        out[name] = dict(n=n, k=k, A_banked=Ab, log2_8n3=b8, cells=cells,
                         feasible_A=[c["A"] for c in feas],
                         any_over_budget=any(c["over_budget"] for c in feas),
                         min_slack_bits=min(c["slack_bits"] for c in feas))
        print("%-11s feasible cells: %s" % (name, [c["A"] for c in feas]))
        for c in feas:
            print("    A=%3d h=%2d  q in [2^%.4f, 2^%.4f)   sup log2 mu = "
                  "%12.4f   (8n^3 = 2^%d, slack %.4f bits)   over-budget: %s"
                  % (c["A"], c["h"], c["log2_qmin"], c["log2_qmax"],
                     c["log2_mu_sup"], b8, c["slack_bits"], c["over_budget"]))

    for name, n, k, Ab in PRIZE:
        b8 = 3 + 3 * (n.bit_length() - 1)
        A1 = candA(n, k, mpf(127))
        A2 = candA(n, k, log(mpf((1 << 128) - 1)) / LN2)
        cells = [cell(n, k, A, b8) for A in sorted({A1, A2, Ab})]
        feas = [c for c in cells if c["feasible"]]
        out[name] = dict(n=n, k=k, A_banked=Ab, log2_8n3=b8, cells=cells,
                         A_at_Bstar_min=A1, A_at_Bstar_max=A2,
                         unique_candidate=bool(A1 == A2 == Ab),
                         feasible_A=[c["A"] for c in feas],
                         any_over_budget=any(c["over_budget"] for c in feas),
                         min_slack_bits=min(c["slack_bits"] for c in feas))
        print("%-11s candidate A is unique over the whole admissible B* range "
              "[2^127, 2^128): %s  (A = %d = banked)" %
              (name, A1 == A2 == Ab, A1))
        for c in feas:
            print("    A=%d h=%d  q in [2^%.4f, 2^%.4f)   sup log2 mu = %.6g"
                  "   (8n^3 = 2^%d, slack %.6g bits)   over-budget: %s"
                  % (c["A"], c["h"], c["log2_qmin"], c["log2_qmax"],
                     c["log2_mu_sup"], b8, c["slack_bits"], c["over_budget"]))

    print()
    print("ANY admissible cell at ANY row with random low-core supply > 8n^3?"
          "  %s" % any(v["any_over_budget"] for v in out.values()))
    print("tightest supply slack anywhere in the admissible family: %.4f bits"
          % min(v["min_slack_bits"] for v in out.values()))
    with open(os.path.join(HERE, "EXACTCHECK.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("wrote EXACTCHECK.json")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""RowC window pilot -- part 6: THE FAMILY-UNIFORM SWEEP.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/sweep.py

The six rows are not (n,k,A,q) quadruples with q free: A itself is DERIVED
from q by the banked candidate rule (the row is the first agreement past the
quotient-realizable point), because that rule is stated against
B* = floor(q/2^128).  Banked verbatim in
`critical/nodes/xr_smallcore_spread_count/notes/
 audit_consumption_replay_20260710.py:76-89, 108-112, 129-130`:

  unsafe_realizable(n,k,A,B*) := exists a dyadic scale np (np | n, np*(A-k)
      <= n) with lp = floor((n-A) np / n) in [1, np-1] and C(np,lp) > B*
  the candidate A satisfies  unsafe_realizable(A-1) and not
      unsafe_realizable(A)
  the consumption GATE is  B_quot_ub(A) + (n-A+1) + 16 n^3 <= B*

So the correct family-uniform question is NOT "fix A = 261 and lower q" but
"for each admissible q, take the row that q actually defines and ask whether
its random low-core supply mu = C(n,A(q)) q^{1-h} exceeds 8 n^3".

This file answers it by exhaustive sweep of log2 q over [129, 256) at all six
(n, k) shapes.
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

SHAPES = [("RowC 1/4", 1 << 10, 1 << 8, 261),
          ("RowC 1/8", 1 << 10, 1 << 7, 133),
          ("RowC 1/16", 1 << 10, 1 << 6, 67),
          ("prize 1/4", 1 << 41, 1 << 39, 558345748481),
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
    t = A - k
    out, np_ = [], 2
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            out.append((np_, lp))
        np_ *= 2
    return out


def unsafe(n, k, A, B):
    return any(comb(np_, lp) > B for np_, lp in scales(n, k, A))


def quot_ub(n, k, A):
    return sum(comb(np_, lp) for np_, lp in scales(n, k, A))


def candidate_A(n, k, B):
    """smallest A > k with not unsafe(n,k,A,B).

    unsafe(.,A,.) is monotone non-increasing in A (raising A drops dyadic
    scales from the active set and lowers every lp), so binary search is
    exact; both endpoints are asserted.
    """
    lo, hi = k + 1, k + (1 << 34)
    if not unsafe(n, k, lo, B):
        return lo
    if unsafe(n, k, hi, B):
        return None
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if unsafe(n, k, mid, B):
            lo = mid
        else:
            hi = mid
    return hi


def main():
    out = {}
    for name, n, k, Abank in SHAPES:
        b8 = 3 + 3 * (n.bit_length() - 1)
        rows = []
        worst = None
        lq = 129
        while lq < 256.0001:
            q = int(mpf(2) ** mpf(lq))
            B = q >> 128
            if B < 1:
                lq += 0.25
                continue
            A = candidate_A(n, k, B)
            if A is None:
                lq += 0.25
                continue
            h = A - k
            gate = quot_ub(n, k, A) + (n - A + 1) + 16 * n ** 3 <= B
            lmu = float(lgb(n, A) - (h - 1) * mpf(lq))
            rec = dict(log2q=round(lq, 4), A=A, h=h, gate_ok=bool(gate),
                       log2_mu=lmu, over_budget=bool(lmu > b8))
            rows.append(rec)
            if gate and (worst is None or lmu > worst["log2_mu"]):
                worst = rec
            lq += 0.25
        gated = [r for r in rows if r["gate_ok"]]
        out[name] = dict(n=n, k=k, A_banked=Abank, log2_8n3=b8,
                         min_gated_log2q=min(r["log2q"] for r in gated)
                         if gated else None,
                         A_at_min_gated=min(gated, key=lambda r: r["log2q"])
                         ["A"] if gated else None,
                         worst_gated=worst,
                         any_gated_over_budget=any(r["over_budget"]
                                                   for r in gated),
                         n_gated_points=len(gated),
                         A_range_gated=sorted({r["A"] for r in gated}),
                         ungated_over_budget=[r for r in rows
                                              if r["over_budget"]
                                              and not r["gate_ok"]][:6])
        print("%-11s banked A=%s | gated q range starts at 2^%s with A=%s | "
              "A over the whole gated range: %s" %
              (name, Abank, out[name]["min_gated_log2q"],
               out[name]["A_at_min_gated"], out[name]["A_range_gated"]))
        if worst is None:
            print("            NO q in [2^129, 2^256) passes the gate")
            continue
        print("            worst gated first moment: log2 mu = %.4f  "
              "(8n^3 = 2^%d, slack %.4f bits) at 2^%s, A=%d, h=%d" %
              (worst["log2_mu"], b8, b8 - worst["log2_mu"],
               worst["log2q"], worst["A"], worst["h"]))
        print("            ANY gated q with mu > 8n^3 ? %s   |  ungated q "
              "with mu > 8n^3: %d sampled points" %
              (out[name]["any_gated_over_budget"],
               len([r for r in rows if r["over_budget"] and not r["gate_ok"]])))
    with open(os.path.join(HERE, "SWEEP.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nwrote SWEEP.json")


if __name__ == "__main__":
    main()

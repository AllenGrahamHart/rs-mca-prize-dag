#!/usr/bin/env python3
"""RowC window pilot -- part 5: THE BANKED CONSUMPTION FLOOR ON q.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/floors.py

The consumer `xr_smallcore_spread_count` closes only if the row's numerator
budget covers the quotient charge, the tangent charge and the 16n^3 reserve:

    B_quot_ub(n,k,A) + B_tan_max(n,A) + 16 n^3  <=  B*   ...............(GATE)

verbatim from the banked replay
`critical/nodes/xr_smallcore_spread_count/notes/
 audit_consumption_replay_20260710.py:129-130`
("GATE  B_quot_ub + B_tan_max + 16 n^3 <= B*"), with

    B_quot_ub(n,k,A) = sum over dyadic scales np | n, np*(A-k) <= n, of
                       C(np, lp),  lp = floor((n-A) np / n), 1 <= lp <= np-1
    B_tan_max(n,A)   = n - A + 1
    B*               = floor(q / 2^128).

B_quot_ub and B_tan_max are pure combinatorics of (n,k,A) -- they do NOT
depend on q.  So (GATE) is exactly a LOWER BOUND ON q:

    q  >=  2^128 * ( B_quot_ub + B_tan_max + 16 n^3 )   =:  q_FLOOR.

The row's own candidate-selection rule adds a second q-condition (banked in
the same replay): at agreement A-1 some dyadic census count must EXCEED B*
(the unsafe side is realizable) while at A none may (the safe side is not) --
an upper and a lower bound on B* respectively.

This file evaluates all of them exactly and compares q_FLOOR with the
exposure ceiling L3 = (log2 C(n,A) - log2 8n^3)/(h-1), below which a random
admissible pencil has more than 8n^3 low-core live slopes.
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

ROWS = [
    ("RowC 1/4", 1 << 10, 1 << 8, 261),
    ("RowC 1/8", 1 << 10, 1 << 7, 133),
    ("RowC 1/16", 1 << 10, 1 << 6, 67),
    ("prize 1/4", 1 << 41, 1 << 39, 558345748481),
    ("prize 1/8", 1 << 41, 1 << 38, 283467841537),
    ("prize 1/16", 1 << 41, 1 << 37, 141733920769),
]
B_ROWC = 1 << 122
B_PRIZE = 317494674775468773183020924238786383963


def lgb(n, r):
    if r < 0 or r > n:
        return mpf("-inf")
    if n <= 4096:
        return log(mpf(comb(n, r))) / LN2
    return (loggamma(mpf(n + 1)) - loggamma(mpf(r + 1))
            - loggamma(mpf(n - r + 1))) / LN2


def quot_ub(n, k, A):
    """verbatim re-implementation of the banked census upper bound."""
    t = A - k
    tot, np_ = 0, 2
    scales = []
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            tot += comb(np_, lp)
            scales.append((np_, lp, comb(np_, lp)))
        np_ *= 2
    return tot, scales


def quot_max(n, k, A):
    t = A - k
    best, np_ = 0, 2
    while np_ <= n and np_ * t <= n:
        lp = (n - A) * np_ // n
        if 1 <= lp <= np_ - 1:
            best = max(best, comb(np_, lp))
        np_ *= 2
    return best


def main():
    recs = []
    print("=" * 100)
    print("THE BANKED CONSUMPTION GATE AS A FLOOR ON q")
    print("=" * 100)
    print("%-11s %12s %12s %12s %12s %12s %12s" %
          ("row", "lg B_quot", "lg B_tan", "lg 16n^3", "lg sum",
           "lg q_FLOOR", "lg B*(pin)"))
    for name, n, k, A in ROWS:
        h = A - k
        bq, scales = quot_ub(n, k, A)
        bt = n - A + 1
        b16 = 16 * n ** 3
        tot = bq + bt + b16
        qfloor_bits = 128 + float(log(mpf(tot)) / LN2)
        Bs = B_ROWC if name.startswith("RowC") else B_PRIZE
        rec = dict(row=name, n=n, k=k, A=A, h=h,
                   B_quot_ub=str(bq), B_tan_max=bt, budget16=str(b16),
                   gate_sum=str(tot),
                   log2_B_quot=float(log(mpf(bq)) / LN2),
                   log2_gate_sum=float(log(mpf(tot)) / LN2),
                   q_floor_exact=str(tot << 128),
                   log2_q_floor=qfloor_bits,
                   gate_holds_at_pin=bool(tot <= Bs),
                   log2_Bstar_pin=float(log(mpf(Bs)) / LN2),
                   quot_max_at_A=str(quot_max(n, k, A)),
                   quot_max_at_Am1=str(quot_max(n, k, A - 1)),
                   dyadic_scales=[[a, b, str(c)] for a, b, c in scales])
        C1 = lgb(n, A)
        b8 = 3 + 3 * (n.bit_length() - 1)
        L3 = (C1 - b8) / (h - 1)
        rec["log2_L3"] = float(L3)
        rec["floor_above_L3"] = bool(qfloor_bits > L3)
        rec["margin_bits_floor_minus_L3"] = qfloor_bits - float(L3)
        # worst-case first moment at the smallest admissible q
        rec["log2_mu_at_floor"] = float(C1 - (h - 1) * mpf(qfloor_bits))
        rec["supply_slack_bits_at_floor"] = b8 - rec["log2_mu_at_floor"]
        recs.append(rec)
        print("%-11s %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f" %
              (name, rec["log2_B_quot"], float(log(mpf(bt)) / LN2),
               float(log(mpf(b16)) / LN2), rec["log2_gate_sum"],
               qfloor_bits, rec["log2_Bstar_pin"]))

    print()
    print("%-11s %12s %12s %14s %16s %14s" %
          ("row", "lg q_FLOOR", "lg L3", "FLOOR > L3 ?", "margin bits",
           "lg mu at floor"))
    for r in recs:
        print("%-11s %12.4f %12.4f %14s %+16.4f %14.4f  (8n^3 = 2^%d, slack "
              "%.4f bits)" %
              (r["row"], r["log2_q_floor"], r["log2_L3"],
               "SAFE" if r["floor_above_L3"] else "EXPOSED",
               r["margin_bits_floor_minus_L3"], r["log2_mu_at_floor"],
               3 + 3 * (r["n"].bit_length() - 1),
               r["supply_slack_bits_at_floor"]))

    print()
    print("gate holds at the banked envelope pin (sanity, must be all True):")
    for r in recs:
        print("  %-11s %s   (lg B* pin = %.4f, lg gate sum = %.4f, slack "
              "%.4f bits)" %
              (r["row"], r["gate_holds_at_pin"], r["log2_Bstar_pin"],
               r["log2_gate_sum"],
               r["log2_Bstar_pin"] - r["log2_gate_sum"]))

    print()
    print("dyadic scales entering B_quot_ub (np, lp, C(np,lp)):")
    for r in recs:
        print("  %-11s %s" % (r["row"], ", ".join(
            "(%s,%s,2^%.1f)" % (a, b, float(log(mpf(int(c))) / LN2))
            for a, b, c in r["dyadic_scales"])))

    with open(os.path.join(HERE, "FLOORS.json"), "w") as fh:
        json.dump(recs, fh, indent=1)
    print("\nwrote FLOORS.json")


if __name__ == "__main__":
    main()

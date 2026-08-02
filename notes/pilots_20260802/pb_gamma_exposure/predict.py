#!/usr/bin/env python3
"""PRE-REGISTRATION of the |Gamma| law, frozen before any measurement.

Writes PREDICTIONS.json and REFUSES to overwrite it.  Every number here is
derived from the naive law only:

    E[# exact-A witnesses over all slopes]  =  C(n,A) / q^(h-1)
    E[|W_z|]  =  lambda  =  C(n,A) / q^h
    |Gamma|_poisson  =  q (1 - exp(-lambda))

plus the planted split-fibre floor

    M_inf(shape) = greedy maximal family of a-subsets J of the b labels with
                   |J ^ J'| <= a-2   (the P-B low-core clause, and nothing
                   else -- no Sidon/energy clause)

and the pre-registered claims C1-C6 below.
"""

from __future__ import annotations

import json
import math
import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "PREDICTIONS.json")

SHAPES = {
    # name: (n, m, K, h, g, a, b)   -- all from the banked k1 grid
    "S1": dict(n=32, m=2, K=8, h=2, g=2, a=4, b=14),    # Q4/Q5/Q6 shape
    "S2": dict(n=32, m=2, K=8, h=3, g=1, a=5, b=14),    # Q7/Q8 shape
    "S3": dict(n=32, m=2, K=16, h=2, g=2, a=8, b=14),   # Q9/Q12 shape
    "S4": dict(n=32, m=4, K=8, h=5, g=1, a=3, b=7),     # Q11 shape (official
                                                        # m=4, h=5)
}


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if x % p == 0:
            return x == p
    d, r = x - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        y = pow(a, d, x)
        if y in (1, x - 1):
            continue
        for _ in range(r - 1):
            y = y * y % x
            if y == x - 1:
                break
        else:
            return False
    return True


def ladder(n: int, lo_exp: int, hi_exp: int) -> list[int]:
    """smallest prime q = 1 mod n at or above 2^e, for e in [lo_exp, hi_exp]"""
    out = []
    for e in range(lo_exp, hi_exp + 1):
        base = 1 << e
        c = base + (n - base % n) % n
        if c % n != 1 % n:
            c = base - base % n + 1
            if c < base:
                c += n
        while not is_prime(c):
            c += n
        if c not in out:
            out.append(c)
    return out


def greedy_lowcore(b: int, a: int) -> int:
    """greedy maximal |J ^ J'| <= a-2 family, lexicographic order (the same
    greedy the banked builder uses, with the Sidon clause removed and no
    field: this is the char-0 / large-q limit M_inf)."""
    fam: list[set] = []
    for J in combinations(range(b), a):
        Js = set(J)
        if any(len(Js & S) > a - 2 for S in fam):
            continue
        fam.append(Js)
    return len(fam)


def sum_class_max(b: int, a: int) -> int:
    """exact size of the largest sum-mod-b class of weight-a subsets of
    {0..b-1}; every class has minimum distance >= 4, so this is an exact
    constructive lower bound on the maximum low-core family A(b,4,a)."""
    cur = [[0] * b for _ in range(a + 1)]
    cur[0][0] = 1
    for i in range(b):
        for c in range(min(i, a - 1), -1, -1):
            row, nxt = cur[c], cur[c + 1]
            for s in range(b):
                v = row[s]
                if v:
                    nxt[(s + i) % b] += v
    return max(cur[a])


def main() -> None:
    if os.path.exists(OUT):
        raise SystemExit(f"REFUSING to overwrite frozen {OUT}")

    payload = {
        "pilot": "pb_gamma_exposure",
        "frozen_before_measurement": True,
        "law": {
            "witnesses_total": "C(n,A) / q^(h-1)",
            "mean_Wz": "lambda = C(n,A) / q^h",
            "gamma_poisson": "q (1 - exp(-lambda))",
            "gamma_floor": "M_lowcore(q) <= |Gamma| (planted, q-independent "
                           "in the large-q limit)",
            "gamma_pred": "max(gamma_poisson, M_lowcore)",
        },
        "claims": {
            "C1": "witnesses_measured / (C(n,A)/q^(h-1)) in [0.5, 2.0] at "
                  "every ladder point whose predicted count is >= 100",
            "C2": "|Gamma| >= M_lowcore(q) at every ladder point (the planted "
                  "family is a hard floor)",
            "C3": "|Gamma| / gamma_poisson in [0.5, 2.0] whenever "
                  "gamma_poisson >= 4 * M_inf",
            "C4": "|Gamma| -> M_inf as q -> infinity: at the top of each "
                  "ladder |Gamma| == M_inf exactly (all randomly-supplied "
                  "witnesses gone)",
            "C5": "HEADLINE.  LEX first-match retention |Gamma_lo|/|Gamma| "
                  ">= 0.90 at every ladder point with mean |W_z| <= 0.1, "
                  "i.e. the K1 support-keyed collapse is ABSENT in the "
                  "low-density (official) regime.  Contrast: retention "
                  "<= 0.10 at every ladder point with mean |W_z| >= 100.",
            "C6": "the crossover q at which the construction starts to "
                  "dominate the random supply is q_cross = "
                  "(C(n,A)/M_inf)^(1/(h-1)); above it |Gamma| is "
                  "q-independent",
        },
        "shapes": {},
    }

    for nm, s in SHAPES.items():
        n, m, K, h, g, a, b = (s["n"], s["m"], s["K"], s["h"],
                               s["g"], s["a"], s["b"])
        A = K + h
        C = math.comb(n, A)
        M_inf = greedy_lowcore(b, a)
        M_sum = sum_class_max(b, a)
        qs = ladder(n, 7, 31)
        pts = []
        for q in qs:
            lam = C / q ** h
            wit = C / q ** (h - 1)
            gp = q * (1.0 - math.exp(-lam)) if lam < 700 else float(q)
            pts.append(dict(
                q=q, log2q=math.log2(q),
                mean_Wz=lam,
                witnesses_pred=wit,
                witnesses_pred_int=round(wit),
                gamma_poisson=gp,
                gamma_pred=max(gp, float(M_inf)),
                regime=("low-density (official)" if lam <= 0.1 else
                        "high-density (banked K1 grid)" if lam >= 100 else
                        "crossover"),
                retention_pred=(0.90 if lam <= 0.1 else
                                0.10 if lam >= 100 else None),
            ))
        q_cross = (C / M_inf) ** (1.0 / (h - 1)) if h > 1 else float("inf")
        payload["shapes"][nm] = dict(
            params=s, A=A, C_n_A=C,
            M_inf_greedy_lowcore=M_inf,
            M_sumclass_lower_bound=M_sum,
            q_cross=q_cross, log2_q_cross=math.log2(q_cross),
            ladder=pts,
        )

    with open(OUT, "w") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
    print(f"FROZE {OUT}")
    for nm, d in payload["shapes"].items():
        print(f"  {nm}: n={d['params']['n']} m={d['params']['m']} "
              f"K={d['params']['K']} h={d['params']['h']} A={d['A']} "
              f"C={d['C_n_A']}  M_inf={d['M_inf_greedy_lowcore']} "
              f"(sum-class bound {d['M_sumclass_lower_bound']})  "
              f"q_cross=2^{d['log2_q_cross']:.2f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""C2'' pilot -- exact delta census and joint-ratio measurement.

For a row (n, t, q):

  X   = q^t * Pr_x[x t-null]                     (exact joint account)
  A   = prod_j q^{L_j} Pr_x[block j holds]       (product of level marginals)
  R   = X / A                                    (the C2'' joint ratio)

  delta(x) = sum_j (L_j - |S_j(x)|)^+            (cross-junction nullity)

and the two candidate record measures
  pi_MF   = uniform x on {0,1}^n   (mean-field / marginal side)
  pi_NULL = uniform on t-null x    (conditioned / joint side)

Everything is exact (Fraction / int).
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

from dli_model import blocks, count_null, delta_from_supports, delta_of

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------- pi_MF exact
def mf_support_law(n, t):
    """Exact joint law of (|S_0|,...,|S_Lam|) under uniform x on {0,1}^n.

    The level-(Lam+1) cells partition Z/n into h = n/2^(Lam+1) progressions of
    2^(Lam+1) coordinates; every level-(j+1) cell is contained in exactly one of
    them, so the restrictions of x are independent across progressions and the
    per-progression joint contribution can be enumerated exhaustively.
    Returns Counter{(s_0,...,s_Lam): #x}.
    """
    B = blocks(t)
    lam = len(B) - 1
    g = 2 ** (lam + 1)
    ngroups = n // g
    assert n % g == 0
    per = Counter()
    for y in range(1 << g):
        vec = []
        for j in range(lam + 1):
            step = 2 ** (lam - j)                # cells inside this progression
            u = 0
            for r in range(step):
                bits = {(y >> a) & 1 for a in range(r, g, step)}
                u += (len(bits) > 1)
            vec.append(u)
        per[tuple(vec)] += 1
    law = Counter({(0,) * (lam + 1): 1})
    for _ in range(ngroups):
        nxt = Counter()
        for k1, v1 in law.items():
            for k2, v2 in per.items():
                nxt[tuple(a + b for a, b in zip(k1, k2))] += v1 * v2
        law = nxt
    assert sum(law.values()) == 2 ** n
    return law


def delta_law_from_support_law(law, t):
    out = Counter()
    for k, v in law.items():
        out[delta_from_supports(list(k), t)] += v
    return out


def expect_q_delta(delta_law, q, total):
    return sum(Fraction(v * q**d, total) for d, v in delta_law.items())


# ---------------------------------------------------------------- row census
def census_row(n, t, q, collect_solutions=True):
    B = blocks(t)
    Ls = [len(b) for b in B]
    res = {"n": n, "t": t, "q": q, "blocks": [list(b) for b in B], "L": Ls}

    # --- joint and marginals (exact) -------------------------------------
    tot_all, sols = count_null(n, t, q, collect=True)
    res["n_tnull"] = tot_all
    per_block = []
    for j, U in enumerate(B):
        per_block.append(count_null(n, t, q, rows_wanted=[u * 2**j for u in U]))
    res["n_block"] = per_block
    Pr_joint = Fraction(tot_all, 2**n)
    X = q**t * Pr_joint
    A = Fraction(1)
    for j, U in enumerate(B):
        A *= q ** Ls[j] * Fraction(per_block[j], 2**n)
    res["X"] = str(X)
    res["A"] = str(A)
    res["R"] = str(X / A)
    res["R_float"] = float(X / A)
    res["log2R"] = None if X == 0 else float(
        (X / A).numerator.bit_length() - (X / A).denominator.bit_length())

    # --- pi_MF delta law (exact) -----------------------------------------
    law = mf_support_law(n, t)
    dlaw = delta_law_from_support_law(law, t)
    res["mf_delta_hist"] = {str(d): v for d, v in sorted(dlaw.items())}
    Eq = expect_q_delta(dlaw, q, 2**n)
    res["mf_E_q_delta"] = str(Eq)
    res["mf_E_q_delta_float"] = float(Eq)
    res["mf_Pr_delta_pos"] = str(Fraction(sum(v for d, v in dlaw.items() if d),
                                          2**n))

    # --- pi_NULL delta law (exact) ---------------------------------------
    M0 = 1
    while M0 <= t:
        M0 *= 2
    stride = n // M0
    full = (1 << n) - 1
    dn = Counter()
    coset_deltas = Counter()
    noncoset_deltas = Counter()
    for m in sols:
        d = delta_of(m, n, t)
        dn[d] += 1
        rot = ((m << stride) | (m >> (n - stride))) & full
        (coset_deltas if rot == m else noncoset_deltas)[d] += 1
    res["null_delta_hist"] = {str(d): v for d, v in sorted(dn.items())}
    res["null_delta_hist_coset"] = {str(d): v for d, v in sorted(coset_deltas.items())}
    res["null_delta_hist_noncoset"] = {str(d): v
                                       for d, v in sorted(noncoset_deltas.items())}
    if tot_all:
        En = sum(Fraction(v * q**d, tot_all) for d, v in dn.items())
        res["null_E_q_delta"] = str(En)
        res["null_E_q_delta_float"] = float(En)

    # --- delta = t stratum vs the archived coset class --------------------
    same = all(d == t for d in coset_deltas) and all(d != t for d in noncoset_deltas)
    res["delta_eq_t_is_exactly_coset"] = bool(same)

    # --- contribution split of the t-null count by delta ------------------
    res["tnull_by_delta"] = {str(d): v for d, v in sorted(dn.items())}
    res["tnull_delta0"] = dn.get(0, 0)
    res["mf_delta0_mass"] = str(Fraction(dlaw.get(0, 0), 2**n))
    return res


def main(argv):
    rows = [
        (16, 2, 97), (16, 2, 193), (16, 3, 97), (16, 4, 97), (16, 4, 193),
        (16, 5, 97), (16, 6, 97), (16, 7, 97), (16, 8, 97), (16, 8, 193),
        (32, 2, 97), (32, 2, 193), (32, 2, 8353), (32, 2, 32801),
        (32, 3, 97), (32, 3, 193), (32, 4, 97), (32, 4, 193),
    ]
    if len(argv) > 1:
        pick = set(int(a) for a in argv[1:])
        rows = [r for i, r in enumerate(rows) if i in pick]
    out = []
    for (n, t, q) in rows:
        r = census_row(n, t, q)
        out.append(r)
        print(f"n={n} t={t} q={q}: #tnull={r['n_tnull']} R={r['R_float']:.6g} "
              f"MF_E[q^delta]={r['mf_E_q_delta_float']:.6g} "
              f"NULL_E[q^delta]={r.get('null_E_q_delta_float', float('nan')):.6g} "
              f"delta=t<->coset:{r['delta_eq_t_is_exactly_coset']}")
        sys.stdout.flush()
    tag = "_".join(argv[1:]) if len(argv) > 1 else "all"
    (HERE / "results" / f"census_{tag}.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(sys.argv)

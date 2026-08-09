#!/usr/bin/env python3
"""D1 consistency + D3 pricing table for the re-posed (annulus) anticode.

Registered at notes/pilots_20260809/m7_complement_repose/PREREG.md R1/R3
(Q1, Q2, P6, P7).

Sections
  (A) D1 CONSISTENCY: reproduce the two harvest fixtures from the R1
      statement and test Q2 (the free `kappa` sharpening at #1148, read
      straight from #1148's own shipped certificate with the harvest's
      own parse).
  (B) D3 m4_t2: the exact pricing table at the official rate-half
      M=4,t=2 cell for ell = 4..16, in four orientations, against the
      measured maximum.
  (C) D3 LS6: the same at the round-23 probe cell (ell,b,a) = (4,1,1).
  (D) the M31 hull extrapolation: the first-moment count of NON-exhibited
      split members of (RC1) at the node's real parameters.

Stdlib only.  Run via tools/ramguard tiny|local -- python3 from repo root.
"""
from __future__ import annotations

import json
from math import comb, log2, lgamma

FIX = ("notes/pilots_20260809/pr_harvest/replay/1148/experimental/data/"
       "certificates/atlas-full-affine-hull/"
       "SP01zxa_quadratic_cover_pair_input.txt")


def anticode(sigma, a, delta):
    """(PC3'): a-subsets of a sigma-set, pairwise intersection <= a-delta."""
    e = a - delta + 1
    if a <= 0 or e <= 0 or e > sigma:
        return None
    return comb(sigma, e) // comb(a, e)


def lg(x):
    return round(log2(x), 3) if x and x > 0 else None


def lcomb(n, k):
    """log2 C(n,k) for huge n,k."""
    if k < 0 or k > n:
        return None
    return (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) / log2(2.718281828459045) / 1.0 \
        if False else (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) / 0.6931471805599453


# ---------------------------------------------------------------- (A)
def section_a():
    tok = iter(map(int, open(FIX, encoding="ascii").read().split()))
    p = next(tok)
    core = [next(tok) for _ in range(next(tok))]
    nb = next(tok)
    branches = []
    for _ in range(nb):
        next(tok), next(tok)
        branches.append({next(tok) for _ in range(next(tok))})
    U = set().union(*branches)
    j = len(U) - len(branches[0])                    # locator degree 479
    roots = [U - B for B in branches]
    K = set.intersection(*roots)
    Ub = set.union(*branches)
    ovl = [len(roots[i] & roots[k])
           for i in range(nb) for k in range(i + 1, nb)]
    r = max(ovl)
    delta = j - r
    kappa = len(K)
    sigma = len(U) - kappa
    a = j - kappa
    aco = sigma - a
    out_1148 = {
        "field_is_M31": p == 2 ** 31 - 1,
        "|U|": len(U), "|core|": len(core), "j_locator_degree": j,
        "OVL_min_max": [min(ovl), r], "DELTA": delta,
        "kappa_MEASURED_intersect_all_roots": kappa,
        "union_of_branches": len(Ub),
        "Q2_kappa_positive": kappa > 0,
        "ANN_SIGMA": sigma, "ANN_A": a, "ANN_ACO": aco,
        "sigma_lt_2a_COMPLEMENT_WINS": sigma < 2 * a,
        "AC_AMBIENT_1023_harvest": anticode(1023, j, delta),
        "AC_DIRECT_annulus": anticode(sigma, a, delta),
        "AC_COMP_annulus_THE_REPOSE": anticode(sigma, aco, delta),
        "AC_COMP_harvest_value_kappa0": anticode(len(U), len(U) - j, delta),
        "TRUTH_upstream_claim": nb,
    }
    for k in ("AC_AMBIENT_1023_harvest", "AC_DIRECT_annulus",
              "AC_COMP_annulus_THE_REPOSE", "AC_COMP_harvest_value_kappa0"):
        out_1148["log2_" + k] = lg(out_1148[k])

    # our M31 fixture, exactly as the node states it (RC2)/(RC3)
    m, t = 72428, 4980
    kap, jj = t - 1, t
    sig, aa = m - kap, jj - kap
    out_m31 = {
        "m": m, "t": t, "kappa": kap, "j": jj, "DELTA": 1,
        "ANN_SIGMA": sig, "ANN_A": aa, "ANN_ACO": sig - aa,
        "sigma_lt_2a_COMPLEMENT_WINS": sig < 2 * aa,
        "AC_DIRECT_annulus": anticode(sig, aa, 1),
        "AC_COMP_annulus": anticode(sig, sig - aa, 1),
        "node_exhibited_count_RC2": m - t + 1,
    }
    return {"upstream_1148": out_1148, "ours_M31_route_cut": out_m31}


# ---------------------------------------------------------------- (B)
def section_b(ells=range(4, 17)):
    rows = []
    for ell in ells:
        d = 2 * ell - 3
        N = 5 * ell - 5                     # |C| = k-1
        n = 10 * ell - 8
        b = ell - 3
        s = ell - 3
        r_proved = 2 * s                    # (RH0a)
        r_sharp = ell - 3                   # round-23 sharpening
        row = {"ell": ell, "d_j": d, "N_core": N, "n": n, "b": b,
               "r_proved_2s": r_proved, "r_sharp": r_sharp,
               "DELTA_sharp": d - r_sharp,
               # (RH0b) as printed in the node
               "RH0b_node": (comb(N + b, 2 * s + 1) // comb(ell + 2 * s,
                                                            2 * s + 1)
                             if 2 * s + 1 <= ell + 2 * s else None),
               # ambient = the whole domain n (the "vacuous ceiling")
               "AC_AMBIENT_n": anticode(n, d, d - r_sharp),
               # ambient = the core C  ==  the node's own sharpening
               "AC_DIRECT_core": anticode(N, d, d - r_sharp),
               # THE RE-POSE: complement inside the core annulus
               "AC_COMP_core": anticode(N, N - d, d - r_sharp),
               "MEASURED_MAXPACK": {4: 4, 5: 4, 6: 4}.get(ell),
               }
        for k in ("RH0b_node", "AC_AMBIENT_n", "AC_DIRECT_core",
                  "AC_COMP_core"):
            row["log2_" + k] = lg(row[k])
        for k in ("RH0b_node", "AC_DIRECT_core"):
            v = row["log2_" + k]
            row["exp_per_ell_" + k] = round(v / ell, 4) if v else None
        rows.append(row)
    return rows


# ---------------------------------------------------------------- (C)
def section_c():
    out = []
    for (ell, b, a) in [(4, 1, 1), (9, 8, 1), (11, 8, 1)]:
        n = 8 * ell + 2 * b - 2
        N = 4 * ell + b - 2
        j = 2 * ell - a
        h = ell - 2 * a                      # proved pairwise overlap cap
        J = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
        delta = j - h
        row = {"ell": ell, "b": b, "a": a, "n": n, "N_core": N, "j": j,
               "h_overlap_cap": h, "J": J,
               "regime": "OFF-TAIL (Johnson-paid)" if J > 0 else "LIVE TAIL",
               "node_tail_hypotheses_b_ge_7": b >= 7,
               "AC_DIRECT_core": anticode(N, j, delta),
               "AC_COMP_core": anticode(N, N - j, delta),
               "AC_AMBIENT_n": anticode(n, j, delta),
               "fixed_owner_bound_g0_as_printed":
                   (comb(2 * ell + a + b - 2, h + 1) //
                    comb(2 * ell - a, h + 1)
                    if h + 1 <= 2 * ell - a else None),
               "BONF_min_m_fail_minus_1": None}
        for m in range(2, 400):
            if m * j - m * (m - 1) // 2 * h > N:
                row["BONF_min_m_fail_minus_1"] = m - 1
                break
        out.append(row)
    return out


# ---------------------------------------------------------------- (D)
def section_d():
    """First-moment count of split members of (RC1) that are NOT of the
    exhibited form J_a = R(X-a).  A monic degree-t member of
    V = span{RX,R,1,X,X^2,X^3} is F = R(X+beta) + c(X), deg c <= 3: a
    q^5 family (5 free coefficients).  A uniformly random monic degree-t
    polynomial splits with all roots in an m-set with probability
    C(m,t)/q^t.  Hence E[#split members] ~ q^5 * C(m,t)/q^t, and the
    exhibited family contributes m-t+1 of them."""
    rows = []
    for (q, m, t, measured) in [(31, 16, 6, 253.25), (31, 16, 8, 0.25),
                                (31, 16, 9, 0.0)]:
        pred = comb(m, t) / q ** (t - 5)
        rows.append({"q": q, "m": m, "t": t,
                     "predicted_first_moment_extras": round(pred, 4),
                     "MEASURED_mean_extras": measured,
                     "ratio": round(measured / pred, 4) if pred else None})
    q, m, t = 2 ** 31 - 1, 72428, 4980
    lgq = log2(q)
    rows.append({"q": "2^31-1", "m": m, "t": t,
                 "log2_predicted_first_moment_extras":
                     round(lcomb(m, t) - (t - 5) * lgq, 1),
                 "MEASURED_mean_extras": "NOT COMPUTABLE (see report)",
                 "note": "extrapolation of the same law to the node's real "
                         "parameters"})
    return rows


def main():
    print(json.dumps({
        "A_D1_consistency_and_Q2": section_a(),
        "B_D3_m4_t2_pricing": section_b(),
        "C_D3_LS6_pricing": section_c(),
        "D_M31_hull_first_moment_law": section_d(),
    }, indent=1))


if __name__ == "__main__":
    main()

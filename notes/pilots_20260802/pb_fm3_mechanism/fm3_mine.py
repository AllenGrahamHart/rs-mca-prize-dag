#!/usr/bin/env python3
"""FM3 mechanism pilot -- stage 1: mine the banked selection data.

For every banked case (pb_selector_orders/k1_Q*.json) and every order, compute

  * the FULL pairwise-core histogram of the selected family
    (not just the >= K count),
  * per-coordinate selection frequencies and the global block B at
    thresholds 100% / 99% / 90%,
  * three nulls to decompose the concentration excess:
      N0  uniform random A-subsets of [n]            (hypergeometric, exact)
      N1  global block B_100 + uniform residual      (exact)
      N2  coordinate-marginal-matched max-entropy    (conditional Bernoulli
          fitted to the OBSERVED marginals; overlap law by exact DP)
      N3  parameter-free GREEDY-DEPLETION model      (no fitted input at all:
          the selector's own greedy is simulated as a Markov chain from
          nu(i,a) = C(n-i,A-a)/q^h, and two independent copies are convolved
          by exact DP)
  * predicted Gamma_lo retention from each null via the isolated-vertex
    formula (1 - P[core >= K])^(live-1), against the measured retention.

Read-only w.r.t. every other directory.  Run under the compute law:

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_fm3_mechanism/fm3_mine.py
"""
from __future__ import annotations

import json
import math
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(os.path.dirname(_HERE), "pb_selector_orders")
sys.dont_write_bytecode = True

SUPPORT_ORDERS = ["ORD-LEX", "ORD-COLEX", "ORD-VALEX", "ORD-VALCOLEX",
                  "ORD-ERRLEX"]
NULL_ORDERS = ["ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]
POLY_ORDERS = ["ORD-POLYLEX", "ORD-CODEWORD"]
ORDERS = SUPPORT_ORDERS + NULL_ORDERS + POLY_ORDERS

# greedy-model description of each support-keyed order:
#   (coordinate-processing sequence, prefer_include)
# ORD-LEX      : coords 0..n-1, prefer include   (lex-minimum)
# ORD-ERRLEX   : = reverse of LEX  == lex-MAXIMUM: coords 0..n-1, prefer exclude
# ORD-COLEX    : minimise the bitmask: coords n-1..0, prefer exclude
# ORD-VALEX    : lex in value order:   value-rank ascending, prefer include
# ORD-VALCOLEX : colex in value order: value-rank descending, prefer exclude
GREEDY_SPEC = {
    "ORD-LEX": ("exp-asc", True),
    "ORD-ERRLEX": ("exp-asc", False),
    "ORD-COLEX": ("exp-desc", False),
    "ORD-VALEX": ("val-asc", True),
    "ORD-VALCOLEX": ("val-desc", False),
}


def popcount(x):
    return bin(x).count("1")


# --------------------------------------------------------------------------
# N0 : uniform A-subsets, hypergeometric overlap law
# --------------------------------------------------------------------------
def hypergeom_overlap(n, A):
    tot = math.comb(n, A)
    return [math.comb(A, t) * math.comb(n - A, A - t) / tot
            for t in range(A + 1)]


# --------------------------------------------------------------------------
# N1 : fixed block of size L + uniform residual
# --------------------------------------------------------------------------
def block_overlap(n, A, L):
    """core = L + Hypergeom(n-L, A-L)."""
    base = hypergeom_overlap(n - L, A - L) if A > L else [1.0]
    out = [0.0] * (A + 1)
    for t, p in enumerate(base):
        if L + t <= A:
            out[L + t] += p
    return out


# --------------------------------------------------------------------------
# N2 : conditional-Bernoulli (max-entropy given coordinate marginals,
#      exact size A) -- fit weights by IPF, then exact overlap DP
# --------------------------------------------------------------------------
def cb_fit(marg, A, iters=400):
    """weights w_i with P(i in S) = marg[i] under P(S) prop prod w_i, |S|=A.

    Coordinates with marg == 1 (resp. 0) are handled by the caller (forced
    in / out).  Returns w (list of floats) for the free coordinates.
    """
    n = len(marg)
    w = [max(min(p, 1 - 1e-12), 1e-12) / (1 - max(min(p, 1 - 1e-12), 1e-12))
         for p in marg]
    for _ in range(iters):
        cur = cb_marginals(w, A)
        err = max(abs(cur[i] - marg[i]) for i in range(n))
        if err < 1e-11:
            break
        for i in range(n):
            c = min(max(cur[i], 1e-14), 1 - 1e-14)
            t = min(max(marg[i], 1e-14), 1 - 1e-14)
            w[i] *= (t / (1 - t)) * ((1 - c) / c)
    return w


def cb_marginals(w, A):
    n = len(w)
    # forward: F[i][a] = weight of choosing a among first i coords
    F = [[0.0] * (A + 1) for _ in range(n + 1)]
    F[0][0] = 1.0
    for i in range(n):
        fi, fj = F[i], F[i + 1]
        wi = w[i]
        for a in range(min(i, A) + 1):
            v = fi[a]
            if v == 0.0:
                continue
            fj[a] += v
            if a + 1 <= A:
                fj[a + 1] += v * wi
    B = [[0.0] * (A + 1) for _ in range(n + 1)]
    B[n][0] = 1.0
    for i in range(n - 1, -1, -1):
        bi, bj = B[i], B[i + 1]
        wi = w[i]
        for a in range(min(n - i, A) + 1):
            v = 0.0
            if a <= A:
                v += bj[a]
            if a >= 1:
                v += bj[a - 1] * wi
            bi[a] = v
    Z = F[n][A]
    out = []
    for i in range(n):
        s = 0.0
        for a in range(min(i, A) + 1):
            if A - a - 1 >= 0:
                s += F[i][a] * w[i] * B[i + 1][A - a - 1]
        out.append(s / Z if Z else 0.0)
    return out


def cb_overlap(w, A):
    """exact law of |S ^ S'| for two independent conditional-Bernoulli draws."""
    n = len(w)
    # state (a, b, c); dict-of-dict to stay small
    cur = {(0, 0, 0): 1.0}
    for i in range(n):
        wi = w[i]
        nxt = {}
        rem = n - i - 1
        for (a, b, c), v in cur.items():
            for da, db in ((0, 0), (1, 0), (0, 1), (1, 1)):
                na, nb = a + da, b + db
                if na > A or nb > A:
                    continue
                if na + rem < A or nb + rem < A:
                    continue
                nc = c + (1 if (da and db) else 0)
                ww = v * (wi ** (da + db))
                k = (na, nb, nc)
                nxt[k] = nxt.get(k, 0.0) + ww
        cur = nxt
    out = [0.0] * (A + 1)
    Z = 0.0
    for (a, b, c), v in cur.items():
        if a == A and b == A:
            out[c] += v
            Z += v
    return [v / Z for v in out] if Z else out


# --------------------------------------------------------------------------
# N3 : parameter-free greedy-depletion model
# --------------------------------------------------------------------------
def greedy_pi(n, A, q, h, prefer_include):
    """pi[i][a] = P(coordinate i chosen | i coords processed, a chosen).

    nu(i,a) = C(n-i, A-a) / q^h  is the expected number of witnesses in W_z
    consistent with the decisions made on the first i processed coordinates
    (a of them chosen).  Poissonising and conditioning on 'at least one
    witness survives the current branch' gives, with
    nu_in = nu(i+1, a+1), nu_out = nu(i+1, a):

        prefer include:  P(include) = (1 - e^-nu_in ) / (1 - e^-(nu_in+nu_out))
        prefer exclude:  P(exclude) = (1 - e^-nu_out) / (1 - e^-(nu_in+nu_out))
    """
    qh = float(q) ** h
    pi = [[0.0] * (A + 1) for _ in range(n)]
    for i in range(n):
        rem = n - i - 1
        for a in range(0, min(i, A) + 1):
            need = A - a
            if need < 0 or need > rem + 1:
                continue
            nu_in = (math.comb(rem, need - 1) / qh) if need - 1 >= 0 else 0.0
            nu_out = (math.comb(rem, need) / qh) if need <= rem else 0.0
            pin = -math.expm1(-nu_in)
            pout = -math.expm1(-nu_out)
            tot = -math.expm1(-(nu_in + nu_out))
            if tot <= 0.0:
                # both branches vanishing: fall back on the ratio of means
                s = nu_in + nu_out
                pi[i][a] = (nu_in / s) if s > 0 else 0.0
                continue
            if prefer_include:
                pi[i][a] = pin / tot
            else:
                pi[i][a] = 1.0 - pout / tot
    return pi


def greedy_marginals(pi, n, A):
    st = {0: 1.0}
    marg = []
    for i in range(n):
        p = 0.0
        nxt = {}
        for a, v in st.items():
            pr = pi[i][a] if a <= A else 0.0
            p += v * pr
            nxt[a + 1] = nxt.get(a + 1, 0.0) + v * pr
            nxt[a] = nxt.get(a, 0.0) + v * (1 - pr)
        marg.append(p)
        st = {a: v for a, v in nxt.items() if v > 1e-18 and a <= A}
    return marg


def greedy_overlap(pi, n, A):
    """overlap law for two INDEPENDENT copies of the greedy chain."""
    cur = {(0, 0, 0): 1.0}
    for i in range(n):
        nxt = {}
        rem = n - i - 1
        for (a, b, c), v in cur.items():
            pa = pi[i][a] if a <= A else 0.0
            pb = pi[i][b] if b <= A else 0.0
            for da, pda in ((1, pa), (0, 1 - pa)):
                if pda <= 0.0:
                    continue
                na = a + da
                if na > A or na + rem < A:
                    continue
                for db, pdb in ((1, pb), (0, 1 - pb)):
                    if pdb <= 0.0:
                        continue
                    nb = b + db
                    if nb > A or nb + rem < A:
                        continue
                    nc = c + (1 if (da and db) else 0)
                    k = (na, nb, nc)
                    nxt[k] = nxt.get(k, 0.0) + v * pda * pdb
        cur = {k: v for k, v in nxt.items() if v > 1e-18}
    out = [0.0] * (A + 1)
    Z = 0.0
    for (a, b, c), v in cur.items():
        if a == A and b == A:
            out[c] += v
            Z += v
    return [v / Z for v in out] if Z else out


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def tail(dist, K):
    return sum(dist[K:]) if K < len(dist) else 0.0


def isolated(p, live):
    """expected Gamma_lo retention if pair events were independent."""
    if live <= 1:
        return 1.0
    return (1.0 - p) ** (live - 1)


def observed_hist(masks, A):
    hist = [0] * (A + 1)
    M = len(masks)
    for i in range(M):
        mi = masks[i]
        for j in range(i + 1, M):
            hist[popcount(mi & masks[j])] += 1
    tot = M * (M - 1) // 2
    return hist, tot


def analyse_case(path, rankmap_cache):
    d = json.load(open(path))
    prm = d["parameters"]
    n, q, K, h, m, A = (prm["n"], prm["q"], prm["K"], prm["h"], prm["m"],
                        prm["A"])
    live = d["orders"]["ORD-LEX"]["live_slopes"]
    omega = prm["omega"]
    D = [pow(omega, i, q) for i in range(n)]
    rank = [0] * n
    for r, i in enumerate(sorted(range(n), key=lambda i: D[i])):
        rank[i] = r

    n0 = hypergeom_overlap(n, A)
    res = dict(case=d["case"], n=n, q=q, K=K, h=h, m=m, A=A, live=live,
               A_minus_m=A - m,
               mean_Wz=d["witness_census"]["total_exact_A_witnesses"] / live,
               null_uniform=dict(
                   hist=n0, mean=sum(t * n0[t] for t in range(A + 1)),
                   p_ge_K=tail(n0, K),
                   pred_retention=isolated(tail(n0, K), live)),
               orders={})

    for o in ORDERS:
        if o not in d["orders"]:
            continue
        od = d["orders"][o]
        sm = od["selected_masks"]
        slopes = sorted(int(z) for z in sm)
        masks = [sm[str(z)] for z in slopes]
        M = len(masks)
        hist, npairs = observed_hist(masks, A)
        obs = [c / npairs for c in hist] if npairs else [0.0] * (A + 1)
        # per-coordinate frequency
        freq = [0] * n
        for msk in masks:
            for i in range(n):
                if (msk >> i) & 1:
                    freq[i] += 1
        p = [f / M for f in freq]
        B100 = [i for i in range(n) if freq[i] == M]
        B99 = [i for i in range(n) if p[i] >= 0.99]
        B90 = [i for i in range(n) if p[i] >= 0.90]
        # measured Gamma_lo
        glo = od["gamma_lo_size"]

        n1 = block_overlap(n, A, len(B100))
        # N2 : conditional Bernoulli on the free coordinates
        free = [i for i in range(n) if 0.0 < p[i] < 1.0]
        forced = len(B100)
        zero = sum(1 for i in range(n) if p[i] == 0.0)
        if free and A - forced > 0 and A - forced < len(free):
            w = cb_fit([p[i] for i in free], A - forced)
            ov = cb_overlap(w, A - forced)
            n2 = [0.0] * (A + 1)
            for t, v in enumerate(ov):
                if forced + t <= A:
                    n2[forced + t] += v
            cb_err = max(abs(x - p[i]) for x, i
                         in zip(cb_marginals(w, A - forced), free))
        else:
            n2 = n1
            cb_err = None

        entry = dict(
            retention_measured=glo / M,
            gamma_lo=glo, live=M,
            hist_counts=hist, hist_prob=obs, pairs=npairs,
            mean_core=sum(t * obs[t] for t in range(A + 1)),
            max_core=max(t for t in range(A + 1) if hist[t]) if npairs else 0,
            p_ge_K_obs=tail(obs, K),
            pairs_ge_K=sum(hist[K:]),
            coord_freq=p,
            block_100=B100, block_99=B99, block_90=B90,
            null_block_residual=dict(
                L=len(B100), hist=n1, mean=sum(t * n1[t] for t in range(A + 1)),
                p_ge_K=tail(n1, K),
                pred_retention=isolated(tail(n1, K), M)),
            null_marginal_matched=dict(
                free=len(free), forced=forced, zero=zero, fit_err=cb_err,
                hist=n2, mean=sum(t * n2[t] for t in range(A + 1)),
                p_ge_K=tail(n2, K),
                pred_retention=isolated(tail(n2, K), M)),
        )
        if o in GREEDY_SPEC:
            seq, pref = GREEDY_SPEC[o]
            pi = greedy_pi(n, A, q, h, pref)
            gm = greedy_marginals(pi, n, A)
            gov = greedy_overlap(pi, n, A)
            # map model marginals (in processing order) back to exponent idx
            if seq == "exp-asc":
                perm = list(range(n))
            elif seq == "exp-desc":
                perm = list(range(n - 1, -1, -1))
            elif seq == "val-asc":
                perm = sorted(range(n), key=lambda i: rank[i])
            else:
                perm = sorted(range(n), key=lambda i: -rank[i])
            gmarg = [0.0] * n
            for step, i in enumerate(perm):
                gmarg[i] = gm[step]
            entry["null_greedy"] = dict(
                seq=seq, prefer_include=pref,
                marginals=gmarg,
                marg_L1=sum(abs(gmarg[i] - p[i]) for i in range(n)),
                hist=gov, mean=sum(t * gov[t] for t in range(A + 1)),
                p_ge_K=tail(gov, K),
                p_ge_K_truncated=sum(gov[K:A - m + 1]),
                pred_retention=isolated(tail(gov, K), M),
                pred_retention_trunc=isolated(sum(gov[K:A - m + 1]), M),
            )
        res["orders"][o] = entry
    return res


def main():
    out = {}
    for fn in sorted(os.listdir(_BANK)):
        if fn.startswith("k1_Q") and fn.endswith(".json"):
            r = analyse_case(os.path.join(_BANK, fn), {})
            out[r["case"]] = r
            print(f"[{r['case']}] n={r['n']} q={r['q']} K={r['K']} "
                  f"h={r['h']} A={r['A']} live={r['live']} "
                  f"meanW={r['mean_Wz']:.0f}")
            for o in ORDERS:
                if o not in r["orders"]:
                    continue
                e = r["orders"][o]
                g = e.get("null_greedy")
                print(f"   {o:20s} ret={e['retention_measured']:.3f} "
                      f"|B|={len(e['block_100'])}/{len(e['block_90'])} "
                      f"meancore={e['mean_core']:.2f} "
                      f"P>=K obs={e['p_ge_K_obs']:.4f} "
                      f"N0={r['null_uniform']['p_ge_K']:.2e} "
                      f"N1={e['null_block_residual']['p_ge_K']:.4f} "
                      f"N2={e['null_marginal_matched']['p_ge_K']:.4f}"
                      + (f" N3={g['p_ge_K']:.4f} "
                         f"predret={g['pred_retention']:.3f}" if g else ""))
    path = os.path.join(_HERE, "MINE.json")
    with open(path, "w") as fh:
        json.dump(out, fh, sort_keys=True)
    print("->", path)


if __name__ == "__main__":
    main()

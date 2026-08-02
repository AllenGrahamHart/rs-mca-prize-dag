"""exp_mc_occupancy.py -- does the MC construction populate N_{h-1}?

PRE-REGISTERED PREDICTIONS (written before any run; see REPORT section 2):

 P1  For every T in the MC family of u = X^(n-1) + c X^(k+w-1) the codeword
     P_T is divisible by X^(M-1).  In particular P_T(0) = 0 whenever M >= 2.
 P2  Hence g_T := P_T / X is a codeword of degree < k agreeing with
     v := u / X on H \\ T, so (P_T, g_T) is a codeword PAIR with joint
     agreement EXACTLY k+w = A-1, i.e. a depth-(h-1) band pair.
     #depth-(h-1) band pairs == |MC family| == C(N,m)/N.
 P3  zeta_{P_T}(i) = -x_i for every i in T (independent of T).
 P4  Consequently every forced slope lies in -H: the live-slope set of the
     MC shift pencil satisfies Gamma is a subset of {-x : x in H},
     so |Gamma| <= n.  (Contrast: the ledger budget is 13 n^3.)
 P5  No exact-A support contains two distinct depth-(h-1) cores
     (k-packing exclusivity), so each live slope is used by AT MOST ONE
     cascade-tier pair and N_{h-1} <= |Gamma| / 2 <= n/2.
 P6  Measured N_{h-1} under a deterministic first-match selection is
     O(1)-to-O(n), NOT the family size.  => MC does NOT refute the
     occupancy lemma at d = h-1.
 P7  For a shift v = u / X^j with 1 <= j <= M-1 we get zeta(i) = -x_i^j;
     the fibres of x -> x^j on H have size gcd(j,n), so the ray at a
     forced slope has agreement (k+w) + gcd(j,n).  Prediction: gcd(j,n) > 1
     BREAKS the tangent gate (agreement > A) -- the pair leaves the generic
     branch -- while gcd(j,n) = 1 reproduces the j = 1 picture.
 P8  A shift pencil whose MC excess w is strictly below h-1 has pencil-wide
     max agreement k+w+1 < A, hence ZERO live slopes: the whole structured
     family is invisible to the occupancy lemma (L_P = 0 for every member).
"""

import json
import os
import sys
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from mclib import (INF, Scan, codeword_from_T, make_domain, mc_c_from_gamma,
                   mc_family, poly_eval, trim)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "fixtures": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def shift_word(u, j, n, q):
    """v with v(x) = u(x)/x^j on H, given u as a coefficient list of len n."""
    v = [0] * n
    for e, a in enumerate(u):
        if a:
            v[(e - j) % n] = a          # X^(n) == beta is handled by caller
    return v


def run(n, k, w, M, q, j=1, t=None, verbose=True):
    """MC shift pencil: u = X^(n-1)+c X^(k+w-1), v = u / X^j (exponent shift).

    beta_exp = 0 so beta = 1 and dividing exponents by X^j is exact as long
    as every exponent of u is >= j (true for j <= k+w-1).
    """
    rp = n - k - w
    N, m = n // M, rp // M
    H, beta, omega = make_domain(q, n, beta_exp=0)
    assert beta == 1
    c = mc_c_from_gamma(H, q, n, k, w, M)
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 1 - j] = 1
    v[k + w - 1 - j] = (v[k + w - 1 - j] + c) % q
    tt = w + 1 if t is None else t
    A = k + tt
    h = tt

    uv = [poly_eval(u, x, q) for x in H]
    vv = [poly_eval(v, x, q) for x in H]
    # sanity: v(x) = u(x)/x^j on H
    for i, x in enumerate(H):
        assert (vv[i] * pow(x, j, q)) % q == uv[i]

    fam = mc_family(H, q, n, k, w, M, c)
    pred = comb(N, m) // N if gcd(m, N) == 1 else None

    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "j": j, "t": tt, "h": h,
           "A": A, "N": N, "m": m, "rp": rp, "mc_family": len(fam),
           "mc_formula": pred, "gcd_jn": gcd(j, n)}

    # ---- P1/P2: the pair structure of every MC member
    n_div, n_pairs, joint_sizes = 0, 0, set()
    for T in fam:
        P = codeword_from_T(u, T, H, k, n, q, beta)
        assert P is not None, ("MC member with no codeword", T)
        Pl = list(P)
        div = all(Pl[i] == 0 for i in range(min(j, k)))
        n_div += 1 if div else 0
        if div:
            g = tuple(Pl[j:] + [0] * j)[:k]
            ok = all(poly_eval(g, H[i], q) == vv[i]
                     for i in range(n) if i not in set(T))
            okf = all(poly_eval(P, H[i], q) == uv[i]
                      for i in range(n) if i not in set(T))
            if ok and okf:
                n_pairs += 1
                joint_sizes.add(n - len(T))
    rec["mc_members_with_X^j_dividing_P"] = n_div
    rec["mc_members_giving_a_codeword_pair"] = n_pairs
    rec["joint_agreement_sizes"] = sorted(joint_sizes)
    chk(n_div == len(fam), "P1 X^j | P_T for every MC member",
        (n, k, w, M, q, j, n_div, len(fam)))
    chk(n_pairs == len(fam), "P2 every MC member yields a codeword pair",
        (n, k, w, M, q, j, n_pairs, len(fam)))
    chk(joint_sizes == {k + w} or not fam,
        "P2 joint agreement is exactly k+w", (n, k, w, joint_sizes))

    # ---- exhaustive scan of the whole pencil
    sc = Scan(H, q, k, uv, vv, A)
    rec["gate_ok"] = sc.gate_ok()
    rec["over_agreeing"] = {str(z): a for z, a in sc.over_agreeing().items()}
    rec["pencil_max_agreement"] = max(sc.max_agr.values())
    rec["joint_explanation_max"] = sc.joint_max()
    live = sc.live()
    rec["n_live_slopes"] = len(live)
    negH = set((-x) % q for x in H)
    rec["live_in_minusH"] = all(z != INF and z in negH for z in live)
    rec["n_live_not_in_minusH"] = sum(1 for z in live
                                      if z == INF or z not in negH)

    bp = sc.band_pairs()
    depths = {}
    for P, d in bp.items():
        depths[d] = depths.get(d, 0) + 1
    rec["band_pairs_by_depth"] = {str(d): c for d, c in sorted(depths.items())}

    Nd, Nd_any, detail = sc.occupancy()
    rec["N_d_selected"] = {str(d): c for d, c in sorted(Nd.items())}
    rec["N_d_any_exactA_ray"] = {str(d): c for d, c in sorted(Nd_any.items())}
    Lvals = {}
    for P, (dep, ls, la) in detail.items():
        Lvals.setdefault(dep, []).append((ls, la))
    rec["L_P_profile"] = {str(d): {"max_selected": max(x[0] for x in v),
                                   "max_any": max(x[1] for x in v),
                                   "sum_selected": sum(x[0] for x in v),
                                   "count": len(v)}
                          for d, v in sorted(Lvals.items())}

    # ---- P3: zeta_{P_T}(i) = -x_i
    bad_zeta = 0
    for P, dd in sc.pairs.items():
        if len(dd["Z"]) != k + w:
            continue
        for i, z in dd["zeta"].items():
            if z != (-pow(H[i], j, q)) % q:
                bad_zeta += 1
    rec["zeta_violations_at_depth_w"] = bad_zeta
    chk(bad_zeta == 0, "P3 zeta(i) = -x_i^j on every depth-w pair",
        (n, k, w, M, q, j, bad_zeta))

    # ---- P5: exclusivity -- no exact-A support carries two depth-(h-1) cores
    cores = [dd["Z"] for P, dd in sc.pairs.items()
             if len(dd["Z"]) == A - 1]
    viol = 0
    for z in live:
        for S, _ in sc.rays[z]:
            inside = [Z for Z in cores if Z <= S]
            if len(inside) > 1:
                viol += 1
    rec["exclusivity_violations"] = viol
    chk(viol == 0, "P5 no exact-A support carries two cascade-tier cores",
        (n, k, w, M, q, j, viol))

    # ---- P4/P6
    if tt == w + 1:
        chk(rec["n_live_not_in_minusH"] == 0,
            "P4 every live slope lies in -H", (n, k, w, M, q, j, live[:5]))
        chk(len(live) <= n, "P4 |Gamma| <= n", (n, k, w, M, q, j, len(live)))
        nh = Nd.get(w, 0)
        chk(nh <= n // 2, "P6 N_{h-1} <= n/2",
            (n, k, w, M, q, j, nh, len(fam)))
        rec["N_hminus1_over_family"] = (float(nh) / len(fam)) if fam else None

    if verbose:
        print("  n=%d k=%d w=%d M=%d q=%d j=%d t=%d A=%d | MC=%d(pred %s) "
              "pairs@d=%d: %d | maxagr=%d joint_max=%d | live=%d (in -H: %s) "
              "| N_d(sel)=%s N_d(any)=%s"
              % (n, k, w, M, q, j, tt, A, len(fam), pred, w,
                 depths.get(w, 0), rec["pencil_max_agreement"],
                 rec["joint_explanation_max"], len(live),
                 rec["live_in_minusH"], rec["N_d_selected"],
                 rec["N_d_any_exactA_ray"]))
    return rec


print("=== A. MC shift pencil at the cascade tier d = h-1 (j = 1) ===")
for (n, k, w, M, q) in [(16, 4, 2, 2, 17), (16, 4, 2, 2, 97),
                        (16, 4, 2, 2, 113), (16, 4, 2, 2, 193),
                        (20, 4, 4, 4, 41), (20, 4, 4, 4, 101)]:
    out["fixtures"].append(run(n, k, w, M, q, j=1))

print()
print("=== B. shift exponent j: fibre size gcd(j,n) vs the tangent gate ===")
for (n, k, w, M, q, j) in [(20, 4, 4, 4, 41, 2), (20, 4, 4, 4, 41, 3),
                           (20, 4, 4, 4, 101, 2), (20, 4, 4, 4, 101, 3)]:
    r = run(n, k, w, M, q, j=j)
    r["expected_ray_agreement"] = (k + w) + gcd(j, n)
    chk(r["pencil_max_agreement"] >= (k + w) + gcd(j, n),
        "P7 forced ray agreement = k+w+gcd(j,n)",
        (n, k, w, q, j, r["pencil_max_agreement"], (k + w) + gcd(j, n)))
    chk((gcd(j, n) > 1) == (not r["gate_ok"]),
        "P7 gcd(j,n)>1 <=> tangent gate broken",
        (n, k, w, q, j, gcd(j, n), r["gate_ok"]))
    out["fixtures"].append(r)

print()
print("=== C. structured family strictly inside the band (w < h-1): "
      "no live slopes at all ===")
for (n, k, w, M, q, t) in [(16, 4, 2, 2, 97, 5), (16, 4, 2, 2, 193, 4),
                           (20, 4, 4, 4, 101, 7)]:
    r = run(n, k, w, M, q, j=1, t=t)
    chk(r["n_live_slopes"] == 0, "P8 no live slopes when w < h-1",
        (n, k, w, q, t, r["n_live_slopes"]))
    chk(r["pencil_max_agreement"] == k + w + 1,
        "P8 pencil ceiling is k+w+1 < A",
        (n, k, w, q, t, r["pencil_max_agreement"], k + t))
    out["fixtures"].append(r)

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "mc_occupancy.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

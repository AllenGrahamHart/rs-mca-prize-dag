"""exp_quotient_periodicity.py -- is the MC received pair QUOTIENT-PAID?

The banked first-match stratification (critical/nodes/
stratification_partition_thm/proof.md:49-52, 86) puts

    T3 quotient periodicity:  P3(u,v) := exists M > 1, M | gcd(n,k) such
    that the pencil folds through x -> x^M (syndromes descend)
    -> QUOTIENT-PAID at scale M

STRICTLY BEFORE the regime split, and the bridge's generic branch runs
under "the existing quotient-first convention".  The banked confinement
node (critical/nodes/confinement/statement.md:9, PROVED) says a
zeta-equivariant word with a K_M-stable support forces the completion to
fold, P_S = X^r G(X^M), and the slope to confine.

PRE-REGISTERED PREDICTIONS (written before any run):

 R1  u = X^(n-1) + c X^(k+w-1) with w = M | k satisfies
     u = X^(M-1) F(X^M)  --  every exponent of u is == -1 (mod M).
 R2  u is zeta-EQUIVARIANT: u(zeta x) = zeta^(M-1) u(x) for zeta in mu_M.
     v = u/X is equivariant with the conjugate character zeta^(M-2).
 R3  Every MC support T is K_M-stable (a union of mu_M-cosets) by
     construction, so the locator M_T = G(X^M) -- the support-side
     periodicity of the confinement node.
 R4  CONFINEMENT'S OWN CONCLUSION: the completion folds,
     P_T = X^(M-1) G_T(X^M) -- every exponent of P_T is == -1 (mod M).
     (Contains, and strictly strengthens, "X^(M-1) divides P_T".)
 R5  The whole pencil folds: w_z = u + z v = X^(M-2) (X + z) F(X^M).
 R6  mu_M acts on the family: T -> zeta.T maps the MC family to itself,
     and acts on the live-slope set Gamma = -H.
 R7  Hence P3 fires at scale M = w = h-1, and M | gcd(n,k) at all six
     official rows (checked in rows.py section 6).
"""

import json
import os
import sys
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from mclib import (INF, Scan, codeword_from_T, make_domain, mc_c_from_gamma,
                   mc_family, poly_eval)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "fixtures": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def run(n, k, w, M, q):
    rp = n - k - w
    N, m = n // M, rp // M
    H, beta, omega = make_domain(q, n, beta_exp=0)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 2] = 1
    v[k + w - 2] = (v[k + w - 2] + c) % q
    h, A = w + 1, k + w + 1
    uv = [poly_eval(u, x, q) for x in H]
    vv = [poly_eval(v, x, q) for x in H]
    fam = mc_family(H, q, n, k, w, M, c)

    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "h": h, "A": A,
           "gcd_n_k": gcd(n, k), "M_divides_gcd_nk": gcd(n, k) % M == 0,
           "mc_family": len(fam)}

    # R1
    exps_u = [e for e, a in enumerate(u) if a]
    exps_v = [e for e, a in enumerate(v) if a]
    chk(all(e % M == (M - 1) % M for e in exps_u),
        "R1 every exponent of u is == -1 mod M", (n, k, w, q, exps_u, M))
    chk(all(e % M == (M - 2) % M for e in exps_v),
        "R1 every exponent of v is == -2 mod M", (n, k, w, q, exps_v, M))
    rec["u_exponents"] = exps_u
    rec["v_exponents"] = exps_v

    # R2 equivariance: zeta = omega^(n/M) generates mu_M
    zeta = pow(omega, n // M, q)
    assert pow(zeta, M, q) == 1
    bad = 0
    for i, x in enumerate(H):
        y = (zeta * x) % q
        j = H.index(y)
        if uv[j] != (pow(zeta, M - 1, q) * uv[i]) % q:
            bad += 1
        if vv[j] != (pow(zeta, M - 2, q) * vv[i]) % q:
            bad += 1
    chk(bad == 0, "R2 (u,v) is mu_M-equivariant", (n, k, w, q, bad))
    rec["equivariance_violations"] = bad

    # R3 / R4
    cos = [set(i for i in range(n) if i % N == j) for j in range(N)]
    bad3 = bad4 = 0
    for T in fam:
        Ts = set(T)
        if not all((cl <= Ts) or not (cl & Ts) for cl in cos):
            bad3 += 1
        P = codeword_from_T(u, T, H, k, n, q, beta)
        eP = [e for e, a in enumerate(P) if a]
        if not all(e % M == (M - 1) % M for e in eP):
            bad4 += 1
    chk(bad3 == 0, "R3 every MC support is K_M-stable", (n, k, w, q, bad3))
    chk(bad4 == 0, "R4 CONFINEMENT: P_T = X^(M-1) G(X^M)",
        (n, k, w, q, bad4))
    rec["support_stability_violations"] = bad3
    rec["completion_folding_violations"] = bad4

    # R5 pencil folding: w_z(x) * x^2 / (x+z) depends only on x^M
    # (the single domain point x = -z, where the linear factor vanishes, is
    # skipped: w_z is zero there by construction, not a folding failure)
    bad5 = 0
    for z in (0, 1, 2, 3, 5, 7):
        if z >= q:
            continue
        vals = {}
        okz = True
        for i, x in enumerate(H):
            den = (x + z) % q
            if den == 0:
                continue
            val = ((uv[i] + z * vv[i]) * pow(x, 2, q) % q) * pow(den, q - 2, q) % q
            key = pow(x, M, q)
            if key in vals and vals[key] != val:
                okz = False
                break
            vals[key] = val
        if not okz:
            bad5 += 1
    chk(bad5 == 0, "R5 the pencil folds through x -> x^M",
        (n, k, w, q, bad5))
    rec["pencil_folding_violations"] = bad5

    # R6 mu_M acts on the family and on Gamma
    idx = {x: i for i, x in enumerate(H)}
    famset = set(fam)
    bad6 = 0
    for T in fam:
        T2 = tuple(sorted(idx[(zeta * H[i]) % q] for i in T))
        if T2 not in famset:
            bad6 += 1
    chk(bad6 == 0, "R6 mu_M permutes the MC family", (n, k, w, q, bad6))
    rec["family_action_violations"] = bad6

    sc = Scan(H, q, k, uv, vv, A)
    live = set(sc.live())
    bad6b = sum(1 for z in live
                if z == INF or (zeta * z) % q not in live)
    chk(bad6b == 0, "R6 mu_M permutes Gamma", (n, k, w, q, bad6b))
    rec["gamma"] = len(live)
    rec["gamma_action_violations"] = bad6b

    print("  n=%-3d k=%-3d w=M=%-2d q=%-4d | gcd(n,k)=%-4d M|gcd: %-5s | "
          "u exps %s (== -1 mod M) | MC=%-4d fold-viol=%d confinement-viol=%d"
          " | |Gamma|=%d"
          % (n, k, w, q, gcd(n, k), rec["M_divides_gcd_nk"], exps_u,
             len(fam), bad5, bad4, len(live)))
    return rec


print("=== the MC received pair is the QUOTIENT stratum (T3/P3) ===")
for job in [(16, 4, 2, 2, 17), (16, 4, 2, 2, 97), (16, 4, 2, 2, 193),
            (16, 4, 2, 2, 241), (18, 6, 2, 2, 19), (18, 6, 2, 2, 73),
            (18, 6, 2, 2, 181), (20, 4, 4, 4, 41), (20, 4, 4, 4, 101),
            (20, 4, 4, 4, 181), (16, 8, 4, 4, 17), (16, 8, 4, 4, 97),
            (16, 8, 4, 4, 193)]:
    out["fixtures"].append(run(*job))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "quotient_periodicity.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

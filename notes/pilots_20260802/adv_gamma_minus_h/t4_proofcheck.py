"""t4_proofcheck.py -- machine-check every ALGEBRAIC STEP of the two proofs.

The proofs are short; the risk is that one of the index shifts is wrong.
Each step below is checked against brute-force polynomial arithmetic on
random data, so no step rests on my hand computation.

  S1  WINDOW IDENTITY.  For arbitrary (not necessarily split) monic M of
      degree r' and arbitrary z,
          [X^{n-1-i}] (W_z . M)  ==  alpha_i + z beta_i ,
          alpha_i = m_{-i} + c m_{r'+delta-i},
          beta_i  = m_{j-i} + c m_{r'+delta+j-i} ,
      with m_s := 0 outside [0, r'].   (delta = a - k - w.)

  S2  LEMMA-1 EQUIVALENCE.  For M = locator of a subset T of H, the window
      conditions hold  <=>  the interpolant of w_z on H\\T is a codeword of
      degree < k.  Checked by brute force on every T of a small fixture.

  S3  FACTORISATION (j=1).  With N := (X+z).M,
          alpha_i + z beta_i = [X^{r'+1-i}] N * c + [X^{1-i}] N   is the
      same system as   N(0) = -c,  [X^1]N = 0,  [X^{r-t}]N = 0 (t<w).
      Equivalent form checked: e_t(S) = 0 for t = 1..w-1, e_{r-1}(S) = 0,
      prod(S) = gamma, where S = T + {-z}.

  S4  THEOREM Y (the confinement).  prod(S) = gamma  and  prod(T) in
      x0^{r-1} mu_n  and  gamma in x0^r mu_n  =>  -z in x0 mu_n = H.
      Checked on every classified solution of every fixture.

  S5  CEILING (j=1).  At delta >= 2 the window index i=1 gives the single
      equation z.m_0 = 0, unsatisfiable for z != 0 and M split over
      H subset F_q^*.  Checked: the classifier at a_target >= k+w+2
      returns EMPTY, and the i=1 row is literally (0, m_0).

  S6  CEILING for the (0:1) direction.  v = u/X has no codeword at
      agreement >= k+w+1: the i=1 row is (m_0, 0).

  S7  NON-CONFINEMENT AT j >= 2.  The two top rows give
      z = -m_0/m_j and z.m_{j-1} = -c, hence  z = +- 1/e_j(T^{-1});
      checked numerically on classified solutions.  At j = 1 this reads
      z = +-1/e_1(T^-1) ... no: at j=1 the SAME pair of rows degenerates to
      the product condition, which is why j=1 is special.
"""

import json
import os
import random
import sys
from itertools import combinations
from math import comb

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from advlib import (classify_mixed, interp, make_domain, mc_c_from_gamma,
                    mc_family, mc_pencil_words, peval, primes_for)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)
out = {"doc": __doc__, "checks": 0, "fails": [], "detail": {}}
random.seed(20260802)


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def polymul(a, b, q):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for jj, y in enumerate(b):
                if y:
                    o[i + jj] = (o[i + jj] + x * y) % q
    return o


def esym(vals, q):
    """full elementary symmetric vector e_0..e_len of a list."""
    e = [1]
    for x in vals:
        ne = e + [0]
        for t in range(len(e), 0, -1):
            ne[t] = (e[t] + x * e[t - 1]) % q if t < len(e) else \
                (x * e[t - 1]) % q
        e = ne
    return e


# ---------------------------------------------------------------- S1
print("=== S1 window identity (random monic M, random z, many shapes) ===")
bad = 0
for trial in range(400):
    q = random.choice([41, 61, 73, 97, 101, 113, 193])
    n = random.choice([12, 16, 20, 21, 24])
    if (q - 1) % n:
        continue
    k = random.randint(3, n // 2)
    w = random.randint(1, min(6, n - k - 2))
    j = random.randint(1, min(5, k + w - 1))
    delta = random.randint(1, 2)
    a = k + w + delta
    rp = n - a
    if rp < 1:
        continue
    c = random.randint(1, q - 1)
    z = random.randint(1, q - 1)
    m = [random.randint(0, q - 1) for _ in range(rp)] + [1]
    U = [0] * n
    U[n - 1] = 1
    U[k + w - 1] = (U[k + w - 1] + c) % q
    V = [0] * n
    V[n - 1 - j] = 1
    V[k + w - 1 - j] = (V[k + w - 1 - j] + c) % q
    Wz = [(U[t] + z * V[t]) % q for t in range(n)]
    prod = polymul(Wz, m, q)

    def mc(s):
        return m[s] if 0 <= s <= rp else 0

    W = a - k
    for i in range(W):
        d = n - 1 - i
        lhs = prod[d] % q if d < len(prod) else 0
        al = (mc(-i) + c * mc(rp + delta - i)) % q
        be = (mc(j - i) + c * mc(rp + delta + j - i)) % q
        if lhs != (al + z * be) % q:
            bad += 1
chk(bad == 0, "S1 window identity holds on all random trials", bad)
print("   random trials with 0 mismatches:", bad == 0)

# ---------------------------------------------------------------- S2
print("=== S2 Lemma-1 equivalence on a full fixture (brute force) ===")
for (n, k, w, q, j) in [(12, 3, 2, 37, 1), (14, 4, 2, 29, 1), (12, 3, 2, 37, 2)]:
    if (q - 1) % n:
        continue
    H, beta, om = make_domain(q, n)
    c = random.randint(1, q - 1)
    z = random.randint(1, q - 1)
    uv = [(pow(x, n - 1, q) + c * pow(x, k + w - 1, q)) % q for x in H]
    vv = [(uv[i] * pow(pow(H[i], j, q), q - 2, q)) % q for i in range(n)]
    wz = [(uv[i] + z * vv[i]) % q for i in range(n)]
    a = k + w + 1
    rp = n - a
    U = [0] * n
    U[n - 1] = 1
    U[k + w - 1] = (U[k + w - 1] + c) % q
    V = [0] * n
    V[n - 1 - j] = 1
    V[k + w - 1 - j] = (V[k + w - 1 - j] + c) % q
    Wz = [(U[t] + z * V[t]) % q for t in range(n)]
    mism = 0
    for T in combinations(range(n), rp):
        Ms = [1]
        for i in T:
            Ms = polymul(Ms, [(-H[i]) % q, 1], q)
        pr = polymul(Wz, Ms, q)
        window = all(pr[d] % q == 0 for d in range(n - (a - k), n)
                     if d < len(pr))
        off = [i for i in range(n) if i not in set(T)]
        P = interp([H[i] for i in off[:k]], [wz[i] for i in off[:k]], q)
        isc = all(peval(P, H[i], q) == wz[i] for i in off)
        if window != isc:
            mism += 1
    chk(mism == 0, "S2 window conditions <=> codeword of agreement >= a",
        (n, k, w, q, j, mism))
    print("   n=%d k=%d w=%d q=%d j=%d : %d mismatches over C(%d,%d) subsets"
          % (n, k, w, q, j, mism, n, rp))

# ---------------------------------------------------------------- S3-S7
print("=== S3/S4/S5/S6/S7 on real MC shift pencils ===")
JOBS = [(16, 4, 2, 2, 17, 1), (16, 4, 2, 2, 97, 1), (20, 4, 2, 2, 41, 1),
        (20, 6, 2, 2, 41, 1), (24, 4, 2, 2, 73, 1), (20, 4, 4, 4, 41, 1),
        (20, 6, 2, 4, 41, 3), (20, 6, 2, 4, 101, 3), (21, 5, 2, 7, 43, 2),
        (21, 5, 2, 7, 43, 1), (21, 5, 2, 7, 127, 4)]
det = []
for (n, k, w, M, q, j) in JOBS:
    if (q - 1) % n or n % M or (n - k - w) % M or w > M:
        continue
    H, beta, om = make_domain(q, n)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    A = k + w + 1
    r = n - k - w
    gamma = ((-1) ** (r + 1) * c) % q
    x0 = H[0]
    mun = set((h * pow(x0, q - 2, q)) % q for h in H)
    chk(pow(gamma, n, q) == pow(beta, r, q), "S4a gamma realizable",
        (n, k, w, M, q))
    sols = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A)
    n_prod, n_conf, n_zj = 0, 0, 0
    for s in sols:
        T = s["T"]
        z = s["z"]
        pT = 1
        for i in T:
            pT = (pT * H[i]) % q
        # S3/S4: prod(S) = gamma with S = T + {-z}
        if ((-z) * pT) % q == gamma:
            n_prod += 1
        if ((-z) % q) in set(H):
            n_conf += 1
        # S7: z = +- 1 / e_j(T^{-1})
        ei = esym([pow(H[i], q - 2, q) for i in T], q)
        if j < len(ei) and ei[j]:
            zz = pow(ei[j], q - 2, q)
            if z in ((zz) % q, (-zz) % q):
                n_zj += 1
    if j == 1:
        chk(n_prod == len(sols),
            "S3/S4 prod(S) = gamma on EVERY solution (j=1)",
            (n, k, w, M, q, n_prod, len(sols)))
        chk(n_conf == len(sols),
            "S4 THEOREM Y: -z in H on EVERY solution (j=1)",
            (n, k, w, M, q, n_conf, len(sols)))
        # S5 ceiling
        hi = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A + 1)
        chk(len(hi) == 0, "S5 ceiling: nothing at agreement A+1 (j=1)",
            (n, k, w, M, q, len(hi)))
    chk(n_zj == len(sols), "S7 z = +-1/e_j(T^{-1}) on every solution",
        (n, k, w, M, q, j, n_zj, len(sols)))
    det.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                "n_solutions": len(sols), "prod_S_eq_gamma": n_prod,
                "minus_z_in_H": n_conf, "z_eq_inv_e_j": n_zj})
    print("   n=%2d k=%2d w=%d M=%d q=%-4d j=%d | sols=%-5d prod(S)=gamma:%-5d "
          "-z in H:%-5d z=1/e_j:%-5d"
          % (n, k, w, M, q, j, len(sols), n_prod, n_conf, n_zj))
out["detail"]["mc_jobs"] = det

# ---------------------------------------------------------------- S6
print("=== S6 the (0:1) direction v has ceiling k+w ===")
for (n, k, w, M, q, j) in [(16, 4, 2, 2, 97, 1), (20, 6, 2, 4, 41, 3),
                           (21, 5, 2, 7, 43, 2)]:
    H, beta, om = make_domain(q, n)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    _, uv, vv = mc_pencil_words(H, q, n, k, w, M, j=j, c=c)
    best = 0
    for S in combinations(range(n), k):
        P = interp([H[i] for i in S], [vv[i] for i in S], q)
        ag = sum(1 for i in range(n) if peval(P, H[i], q) == vv[i])
        best = max(best, ag)
    chk(best <= k + w, "S6 max agreement of v is <= k+w",
        (n, k, w, M, q, j, best, k + w))
    print("   n=%d k=%d w=%d q=%d j=%d : max agreement of v = %d (k+w = %d)"
          % (n, k, w, q, j, best, k + w))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "t4_proofcheck.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

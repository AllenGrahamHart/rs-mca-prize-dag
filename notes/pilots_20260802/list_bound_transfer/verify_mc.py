"""verify_mc.py -- the MC (multiplicative-coset) large-list construction.

PRE-REGISTERED PREDICTIONS (written before any run):

  P1  For U = X^(n-1) + c X^(k+w-1) on H = x0*mu_n with r' = n-k-w,
      the codewords of agreement >= k+w are exactly indexed by
        {T subset H, |T| = r' : e_1(T)=...=e_(w-1)(T)=0, prod T = gamma},
      gamma = (-1)^(r'+1) c, and the map T -> P_T is injective.
  P2  CEILING: no codeword agrees with U in >= k+w+1 positions, for every
      w >= 1 (generalising PK1(A), which is the w = 1 case).
  P3  MC LOWER BOUND: whenever M | n, M | r', w <= M and gcd(r'/M, n/M) = 1,
      the above set contains the MC family of exact size C(N,m)/N with
      N = n/M, m = r'/M -- a q-FREE count.
  P4  At (n,k,w,M) = (16,8,2,2): MC count = C(8,3)/8 = 7, equal to the
      crossing pilot's measured large-q w=2 shell (30 at q=17, 7 at q>=241).
  P5  Accidental excess above the MC floor shrinks as q grows and vanishes
      for q large relative to C(n,r').

Everything is measured with the THEORY-FREE census (enumerate k-subsets,
interpolate, count agreement).
"""

import json
import os
import sys
from itertools import combinations
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from lbt_lib import (make_domain, primes_with_n_dividing_qm1, word_values,
                     full_list_census, mc_family, mc_count_formula,
                     codeword_from_T, poly_eval)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

results = {"predictions": {
    "P1": "shell(k+w) indexed exactly by T with e_1..e_{w-1}=0, prod T=gamma; injective",
    "P2": "ceiling: max agreement of U = X^{n-1}+cX^{k+w-1} is exactly k+w",
    "P3": "MC family of size C(N,m)/N is contained in the shell (N=n/M, m=r'/M)",
    "P4": "(16,8,2,2) -> 7, matching crossing pilot large-q w=2 shell",
    "P5": "accidental excess above MC floor shrinks with q",
}, "rows": [], "checks": 0, "fails": []}


def check(cond, label, extra=None):
    results["checks"] += 1
    if not cond:
        results["fails"].append({"label": label, "extra": extra})
        print("  FAIL", label, extra)
    return cond


# (n, k, w, M) toy rows.  brute census cost is C(n,k).
ROWS = [
    (16, 8, 2, 2),    # rate 1/2, matches crossing pilot's w=2 instance
    (16, 4, 2, 2),    # rate 1/4
    (16, 6, 2, 2),    # gcd(m,N) != 1 control
    (20, 4, 4, 4),    # M = 4, w = 4
    (20, 6, 2, 2),
    (24, 6, 3, 3),    # odd M = 3, w = 3
    (18, 4, 2, 2),
]

for (n, k, w, M) in ROWS:
    rp = n - k - w
    if n % M or rp % M or w > M:
        print("skip (divisibility)", (n, k, w, M))
        continue
    N, m = n // M, rp // M
    pred, uniform = mc_count_formula(n, k, w, M)
    qs = primes_with_n_dividing_qm1(n, count=5, lo=n)
    row = {"n": n, "k": k, "w": w, "M": M, "rp": rp, "N": N, "m": m,
           "gcd_m_N": gcd(m, N), "mc_formula": pred, "uniform": uniform,
           "n2": n * n, "fields": []}
    print("== row n=%d k=%d w=%d M=%d  r'=%d N=%d m=%d  formula=%s" %
          (n, k, w, M, rp, N, m, pred))
    for q in qs:
        H, beta, omega = make_domain(q, n, beta_exp=0)
        # choose c realizable: gamma must be an r'-fold subset product,
        # i.e. gamma^n = beta^{r'}.  Pick gamma = prod of an actual MC set.
        # coset j = {i : i % N == j}; take S = {0,1,...,m-1}
        cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
        best = None
        for S in combinations(range(N), m):
            T = [i for j in S for i in cosets[j]]
            pr = 1
            for i in T:
                pr = (pr * H[i]) % q
            best = pr
            break
        gamma = best
        c = (((-1) ** (rp + 1)) * gamma) % q   # gamma = (-1)^{r'+1} c  =>  c = (-1)^{r'+1} gamma
        if c == 0:
            continue
        U = [0] * n
        U[n - 1] = 1
        U[k + w - 1] = (U[k + w - 1] + c) % q
        Uvals = word_values(U, H, q)

        fam = mc_family(H, q, n, k, w, M, c)
        cen = full_list_census(Uvals, H, k, q, amin=k + w)
        prof = {}
        for P, a in cen.items():
            prof[a] = prof.get(a, 0) + 1
        maxagr = max(cen.values()) if cen else 0
        shell = prof.get(k + w, 0)
        total_ge = len(cen)

        # P3: each MC set really yields a codeword of agreement >= k+w
        ok_mc = True
        Pset = set()
        for T in fam:
            P = codeword_from_T(U, T, H, k, n, q, beta)
            if P is None:
                ok_mc = False
                break
            Pset.add(P)
            agr = sum(1 for i, x in enumerate(H)
                      if poly_eval(list(P), x, q) == Uvals[i])
            if agr != k + w:
                ok_mc = False
                break
        check(ok_mc, "MC family -> codewords of agreement exactly k+w",
              (n, k, w, M, q))
        check(len(Pset) == len(fam), "MC family injective T->P",
              (n, k, w, M, q, len(Pset), len(fam)))
        check(Pset <= set(cen.keys()), "MC codewords inside census",
              (n, k, w, M, q))
        check(maxagr <= k + w, "P2 ceiling", (n, k, w, M, q, maxagr))
        if uniform:
            check(len(fam) == pred, "P3 MC count formula",
                  (n, k, w, M, q, len(fam), pred))

        row["fields"].append({
            "q": q, "c": c, "gamma": gamma,
            "mc_family": len(fam), "shell_k_plus_w": shell,
            "total_agr_ge_k_plus_w": total_ge, "max_agreement": maxagr,
            "excess": total_ge - len(fam),
            "profile": {str(a): v for a, v in sorted(prof.items())},
        })
        print("   q=%-5d mc=%-6d shell=%-6d total>=%-6d max_agr=%d excess=%d"
              % (q, len(fam), shell, total_ge, maxagr, total_ge - len(fam)))
    results["rows"].append(row)

# P4 explicit
r = [x for x in results["rows"] if (x["n"], x["k"], x["w"], x["M"]) == (16, 8, 2, 2)]
if r:
    check(r[0]["mc_formula"] == 7, "P4 (16,8,2,2) formula = 7", r[0]["mc_formula"])

results["verdict"] = "MC_PASS" if not results["fails"] else "MC_FAIL"
with open(os.path.join(CHK, "mc.json"), "w") as f:
    json.dump(results, f, indent=1)
print("\nchecks=%d fails=%d -> %s" %
      (results["checks"], len(results["fails"]), results["verdict"]))

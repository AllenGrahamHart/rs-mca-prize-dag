"""verify_pencil.py -- does the MC blow-up survive the pencil min?

PRE-REGISTERED PREDICTIONS (written before any run):

  Q1  SHIFT PENCIL.  u = X^(n-1) + c X^(k+w-1),  v = X^(n-2) + c X^(k+w-2)
      (same c!).  Prediction: EVERY member w_z = u + z v (z in F_q) and
      w_inf = v admits the ENTIRE MC family, i.e.
          min_{z in P^1} L(w_z, >= k+w)  >=  C(N,m)/N.
      Reason: with M_T = g(X^M) the coefficients m_1 and m_{r'-1} vanish, so
      the two window conditions collapse to the SAME condition m_0 = -c for
      both components; the mixed member imposes nothing new.
  Q2  CEILING FOR MIXED MEMBERS.  For z != 0, inf the over-agreement
      analysis permits only agreement k+w+1 (delta >= 2 forces m_0 = 0).
      Prediction: max agreement over the whole pencil is k+w or k+w+1;
      I predict k+w+1 does occur for some mixed members (unproven).
  Q3  CONTROL -- SAME-WINDOW PENCIL.  u = X^(n-1)+c_1 X^j,
      v = X^(n-1)+c_2 X^j (c_1 != c_2): prediction min over P^1 is ZERO
      (the (0:1) direction is the pure monomial X^j, whose list is empty).
  Q4  NON-DEGENERACY.  span(u,v) meets C only in 0, so no pencil member is
      a codeword.
  Q5  GENERICITY.  max over (f,g) in C^2 of the joint explanation size
      |{x : u(x)=f(x), v(x)=g(x)}| is < A.  Measured, not predicted.

  INCIDENCE CONTROL (theorem attempt, see incidence.py): if v has no zero
  on H then sum_{z in F_q} agr(c, w_z) = n for EVERY codeword c, so at
  most floor(n/a) members can list a given c.  Prediction: verified
  exactly, and the lists of distinct members are pairwise DISJOINT once
  a > n/2.
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
                     pencil_members, joint_explanation_max, poly_eval)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": {
    "Q1": "shift pencil: every member lists the whole MC family; min >= C(N,m)/N",
    "Q2": "max agreement over pencil is k+w or k+w+1",
    "Q3": "same-window control pencil: min over P^1 = 0",
    "Q4": "span(u,v) cap C = 0",
    "Q5": "joint explanation max measured",
    "INC": "sum_z agr(c,w_z) = n for all c when v is nowhere zero; lists disjoint when a>n/2",
}, "experiments": [], "checks": 0, "fails": []}


def check(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": extra})
        print("   FAIL", label, extra)
    return cond


def mc_gamma_and_c(H, q, n, k, w, M):
    rp = n - k - w
    N, m = n // M, rp // M
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    T = [i for j in range(m) for i in cosets[j]]
    pr = 1
    for i in T:
        pr = (pr * H[i]) % q
    gamma = pr
    c = (((-1) ** (rp + 1)) * gamma) % q
    return gamma, c


def run_shift_pencil(n, k, w, M, q, zs=None):
    rp = n - k - w
    N, m = n // M, rp // M
    H, beta, omega = make_domain(q, n, beta_exp=0)
    gamma, c = mc_gamma_and_c(H, q, n, k, w, M)
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 2] = 1
    v[k + w - 2] = (v[k + w - 2] + c) % q
    fam = mc_family(H, q, n, k, w, M, c)
    pred, uniform = mc_count_formula(n, k, w, M)
    uvals = word_values(u, H, q)
    vvals = word_values(v, H, q)

    rec = {"kind": "shift", "n": n, "k": k, "w": w, "M": M, "q": q,
           "rp": rp, "N": N, "m": m, "mc": len(fam), "formula": pred,
           "a": k + w, "n2": n * n, "members": []}

    members = list(pencil_members(u, v, q))
    if zs is not None:
        members = [mm for mm in members if mm[0] in zs or mm[0] == "inf"]
    lists = {}
    for lbl, W in members:
        Wvals = word_values(W, H, q)
        if all(x == 0 for x in Wvals):
            rec["members"].append({"z": str(lbl), "zero_word": True})
            continue
        cen = full_list_census(Wvals, H, k, q, amin=k + w)
        maxall = full_list_census(Wvals, H, k, q, amin=k)
        mx = max(maxall.values()) if maxall else 0
        lists[str(lbl)] = set(cen.keys())
        rec["members"].append({"z": str(lbl), "list_ge_a": len(cen),
                               "max_agreement": mx})
    sizes = [mm["list_ge_a"] for mm in rec["members"] if "list_ge_a" in mm]
    rec["min_list"] = min(sizes) if sizes else None
    rec["max_list"] = max(sizes) if sizes else None
    rec["max_agreement_pencil"] = max(mm["max_agreement"]
                                      for mm in rec["members"] if "max_agreement" in mm)
    # Q1
    check(rec["min_list"] >= len(fam),
          "Q1 min over pencil >= MC family", (n, k, w, M, q, rec["min_list"], len(fam)))
    if uniform:
        check(rec["min_list"] >= pred, "Q1 min >= formula",
              (n, k, w, M, q, rec["min_list"], pred))
    # Q2
    check(rec["max_agreement_pencil"] <= k + w + 1,
          "Q2 pencil ceiling <= k+w+1", (n, k, w, M, q, rec["max_agreement_pencil"]))
    # Q4 non-degeneracy: no member is a codeword (would have max agr = n)
    check(rec["max_agreement_pencil"] < n, "Q4 no member is a codeword",
          (n, k, w, M, q))
    # INC: disjointness of lists when a > n/2
    if (k + w) * 2 > n:
        allp = []
        for s in lists.values():
            allp.extend(s)
        check(len(allp) == len(set(allp)), "INC lists pairwise disjoint (a>n/2)",
              (n, k, w, M, q, len(allp), len(set(allp))))
    # Q5 genericity
    if comb(n, k) <= 30000:
        je, _ = joint_explanation_max(uvals, vvals, H, k, q)
        rec["joint_explanation_max"] = je
    return rec


def run_same_window_control(n, k, w, M, q):
    """u = X^{n-1}+c1 X^{k+w-1}, v = X^{n-1}+c2 X^{k+w-1}."""
    rp = n - k - w
    H, beta, omega = make_domain(q, n, beta_exp=0)
    gamma, c1 = mc_gamma_and_c(H, q, n, k, w, M)
    # a second realizable target: multiply gamma by omega^{r'} (still in the
    # product coset)
    c2 = (c1 * pow(omega, rp, q)) % q
    if c1 == c2:
        c2 = (c1 * pow(omega, 2 * rp, q)) % q
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c1) % q
    v = [0] * n
    v[n - 1] = 1
    v[k + w - 1] = (v[k + w - 1] + c2) % q
    rec = {"kind": "same_window_control", "n": n, "k": k, "w": w, "M": M,
           "q": q, "c1": c1, "c2": c2, "a": k + w, "members": []}
    for lbl, W in pencil_members(u, v, q):
        Wvals = word_values(W, H, q)
        if all(x == 0 for x in Wvals):
            rec["members"].append({"z": str(lbl), "zero_word": True,
                                   "list_ge_a": None})
            continue
        cen = full_list_census(Wvals, H, k, q, amin=k + w)
        rec["members"].append({"z": str(lbl), "list_ge_a": len(cen)})
    sizes = [mm["list_ge_a"] for mm in rec["members"] if mm.get("list_ge_a") is not None]
    rec["min_list"] = min(sizes)
    rec["max_list"] = max(sizes)
    check(rec["min_list"] == 0, "Q3 control pencil min = 0",
          (n, k, w, M, q, rec["min_list"]))
    return rec


JOBS = [
    # (n, k, w, M, q)
    (16, 4, 2, 2, 17),
    (16, 4, 2, 2, 97),
    (16, 4, 2, 2, 113),
    (16, 4, 2, 2, 193),
    (20, 4, 4, 4, 41),
    (20, 4, 4, 4, 101),
    (20, 4, 4, 4, 181),
]

for (n, k, w, M, q) in JOBS:
    print("== shift pencil n=%d k=%d w=%d M=%d q=%d" % (n, k, w, M, q))
    rec = run_shift_pencil(n, k, w, M, q)
    print("   MC=%d  min=%d  max=%d  max_agr=%d  je=%s" %
          (rec["mc"], rec["min_list"], rec["max_list"],
           rec["max_agreement_pencil"], rec.get("joint_explanation_max")))
    out["experiments"].append(rec)

for (n, k, w, M, q) in [(16, 4, 2, 2, 97), (20, 4, 4, 4, 41)]:
    print("== control (same window) n=%d k=%d w=%d M=%d q=%d" % (n, k, w, M, q))
    rec = run_same_window_control(n, k, w, M, q)
    print("   min=%d max=%d" % (rec["min_list"], rec["max_list"]))
    out["experiments"].append(rec)

out["verdict"] = "PENCIL_PASS" if not out["fails"] else "PENCIL_FAIL"
with open(os.path.join(CHK, "pencil.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]), out["verdict"]))

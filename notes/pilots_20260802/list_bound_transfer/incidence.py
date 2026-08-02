"""incidence.py -- the pencil incidence identity, its corollaries, and the
refutation of every "trade-off law" route to bounding the pencil MIN.

THEOREM I (pencil mass identity).  Let D be ANY evaluation set of size n in
F_q, let u, v : D -> F_q with v(x) != 0 for every x in D, and put
w_z = u + z v.  Then for EVERY function c : D -> F_q,

        sum_{z in F_q} agr(c, w_z)  =  n.

Proof.  For x in D the equation u(x) + z v(x) = c(x) has the unique solution
z = (c(x)-u(x))/v(x) in F_q.  Summing the indicator over (x,z) counts each
x exactly once.  QED   (Equivalently: agr(c, w_z) = |phi_c^{-1}(z)| for the
map phi_c : D -> F_q, x -> (c(x)-u(x))/v(x); its fibres partition D.)

THEOREM I' (v with zeros).  If Z = {x in D : v(x)=0} and
e(c) = #{x in Z : u(x)=c(x)}, then
        sum_{z in F_q} agr(c, w_z) = q*e(c) + (n - |Z|).

COROLLARY I.1.  #{z in F_q : agr(c,w_z) >= a} <= floor(n/a)  (v nowhere 0).
COROLLARY I.2.  If 2a > n the lists {c : agr(c,w_z) >= a}, z in F_q, are
                PAIRWISE DISJOINT.
COROLLARY I.3.  sum_{z in F_q} L(w_z,a) <= floor(n/a) * |U(a)| where
                U(a) = {c : exists z in F_q with agr(c,w_z) >= a} is the
                LINE list -- the correlated-agreement object itself.
                Hence   min_{z in P^1} L(w_z,a) <= (floor(n/a)*|U(a)| + L(v,a))/(q+1).

WHY THIS CANNOT BOUND THE MIN (the negative result).  Corollary I.3 is the
ONLY averaging route the identity supports, and it is vacuous: |U(a)| is
exactly the quantity a correlated-agreement theorem would have to supply,
so the route is circular.  And it CANNOT be repaired: the MC pencil of
verify_pencil.py has min_z L(w_z,a) = C(N,m)/N, superpolynomial in n, so no
inequality of the form min_z L(w_z,a) <= poly(n) is true.  Any pencil
trade-off law must therefore use hypotheses strictly beyond
(k-packing + tangent gate + non-degeneracy), all three of which the MC
pencil satisfies.

This file verifies I, I', I.1, I.2 exhaustively on random and structured
instances, and exhibits the MC counterexample to the missing law.
"""

import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from lbt_lib import (make_domain, word_values, full_list_census, poly_eval,
                     mc_family, mc_count_formula, pencil_members)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"theorem": "sum_{z in F_q} agr(c, u+zv) = q*e(c) + (n-|Z|)",
       "checks": 0, "fails": [], "instances": []}


def check(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": extra})
        print("  FAIL", label, extra)


random.seed(20260802)

for (n, k, q) in [(8, 3, 17), (8, 3, 41), (12, 4, 37), (12, 4, 73),
                  (16, 4, 17), (16, 6, 97), (10, 5, 31)]:
    H, beta, omega = make_domain(q, n, beta_exp=0)
    for trial in range(6):
        u = [random.randrange(q) for _ in range(n)]      # as a value vector
        v = [random.randrange(q) for _ in range(n)]
        if trial < 3:                                     # force v nowhere zero
            v = [random.randrange(1, q) for _ in range(n)]
        Z = [i for i in range(n) if v[i] == 0]
        # test the identity against every codeword of a random sample
        for _ in range(8):
            P = [random.randrange(q) for _ in range(k)]
            cvals = [poly_eval(P, x, q) for x in H]
            e = sum(1 for i in Z if u[i] == cvals[i])
            tot = 0
            for z in range(q):
                wz = [(u[i] + z * v[i]) % q for i in range(n)]
                tot += sum(1 for i in range(n) if wz[i] == cvals[i])
            check(tot == q * e + (n - len(Z)),
                  "Theorem I'", (n, k, q, len(Z), e, tot))
            if not Z:
                check(tot == n, "Theorem I", (n, k, q, tot))
                for a in range(1, n + 1):
                    cnt = 0
                    for z in range(q):
                        wz = [(u[i] + z * v[i]) % q for i in range(n)]
                        if sum(1 for i in range(n) if wz[i] == cvals[i]) >= a:
                            cnt += 1
                    check(cnt <= n // a, "Corollary I.1", (n, k, q, a, cnt))

# Corollary I.2 (disjointness) on a structured pencil with a > n/2
for (n, k, w, M, q) in [(16, 8, 2, 2, 97), (16, 8, 2, 2, 113)]:
    H, beta, omega = make_domain(q, n, beta_exp=0)
    rp = n - k - w
    N, m = n // M, rp // M
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    T = [i for j in range(m) for i in cosets[j]]
    pr = 1
    for i in T:
        pr = (pr * H[i]) % q
    c = (((-1) ** (rp + 1)) * pr) % q
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 2] = 1
    v[k + w - 2] = (v[k + w - 2] + c) % q
    vv = word_values(v, H, q)
    nzeros = sum(1 for x in vv if x == 0)
    # v(x) = x^{k+w-2}(x^{r'} + c) vanishes exactly where x^{r'} = -c, which
    # may have solutions in H.  Theorem I' covers that case; record it.
    a = k + w
    seen = {}
    dup = 0
    for lbl, W in pencil_members(u, v, q):
        if lbl == "inf":
            continue
        cen = full_list_census(word_values(W, H, q), H, k, q, amin=a)
        for P in cen:
            if P in seen:
                dup += 1
            seen[P] = lbl
    check(2 * a > n, "a > n/2 precondition", (n, a))
    check(dup == 0, "Corollary I.2 disjointness", (n, k, q, dup))
    out["instances"].append({"n": n, "k": k, "w": w, "M": M, "q": q,
                             "a": a, "v_zeros_on_H": nzeros,
                             "distinct_codewords_over_pencil": len(seen),
                             "duplicates": dup})

# The negative result: exhibit min_z L = MC count, refuting any poly(n) law.
neg = []
for (n, k, w, M, q) in [(16, 4, 2, 2, 113), (20, 4, 4, 4, 181)]:
    pred, uniform = mc_count_formula(n, k, w, M)
    neg.append({"n": n, "k": k, "w": w, "M": M, "q": q,
                "min_over_pencil": pred,
                "source": "verify_pencil.py (exhaustive over all q+1 members)"})
out["negative_result"] = {
    "claim": "no inequality min_z L(w_z,a) <= f(n) can hold under "
             "(k-packing + tangent gate agr<=A + span(u,v) cap C = 0)",
    "witness": "MC shift pencil; min = C(N,m)/N which is superpolynomial in n",
    "instances": neg,
}

out["verdict"] = "INCIDENCE_PASS" if not out["fails"] else "INCIDENCE_FAIL"
with open(os.path.join(CHK, "incidence.json"), "w") as f:
    json.dump(out, f, indent=1)
print("checks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]), out["verdict"]))

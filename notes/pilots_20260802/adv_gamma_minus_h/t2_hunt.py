"""t2_hunt.py -- the adversarial hunt: does the confinement survive j >= 2?

THEOREM Y (proved in t1, advlib.predicted_coset_j1) closes the caveat for
the shift exponent j = 1: the window condition at index i = 1 reads
z * m_{j-1} = -c, which at j = 1 is z * m_0 = -c, i.e. a PURE PRODUCT
condition, and prod(T) lives in the coset x0^|T| mu_n -- so z is pinned to
one coset of mu_n.

For j >= 2 that same condition reads  z * prod(T) * e_{j-1}(T^-1) = +-c,
and combining it with the i = 0 condition gives

        z  =  +- 1 / e_j(T^{-1}) ,

a SUM of j-fold products of inverses -- NOT confined to any coset.  For the
MC-derived solutions T = T_MC \\ {x0} one has e_j(T^-1) = (-1)^j x0^{-j}
(coset-union e_t = 0 for t < M), reproducing MC-7's zeta = -x0^j; but the
system imposes nothing of the kind on a general solution.

PRE-REGISTERED PREDICTIONS.
 C1  The configuration (w = 2, M = 4, j = 3) is a GENUINE MC shift pencil:
     MC family non-empty, X^j | P_T for every member, and (P_T, P_T/X^j)
     is a codeword pair of joint agreement EXACTLY k+w = A-1.
     [MC-3 admits w <= M; M | k+w is what makes P_T = X^{M-1} G(X^M).]
 C2  At j = 1 the live slopes stay inside -H at EVERY q (Theorem Y).
 C3  At j = 3, once C(n,A)/q^w exceeds ~1, live slopes appear OUTSIDE
     -H^j.  ** This is the refutation. **
 C4  The number of exact-A rays tracks C(n,A)/q^w * (a constant), and the
     number OUTSIDE -H^j tracks (1 - n/(q-1)) times the number of
     non-MC-derived rays.
 C5  The tangent gate (no agreement >= A+1 anywhere on the pencil) can be
     kept intact by raising q, so the refutation is NOT an artefact of a
     pencil that has already left the generic branch.
"""

import json
import os
import sys
from itertools import combinations
from math import comb, gcd, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from advlib import (INF, Scan, classify_mixed, interp, make_domain,
                    mc_c_from_gamma, mc_family, mc_pencil_words, neg_H,
                    neg_Hj, peval, predicted_coset_j1, primes_for)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "runs": [], "checks": 0, "fails": [],
       "counterexamples": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def codeword_off_T(vals, T, H, k, q):
    """the unique deg<k codeword agreeing with `vals` off T, or None."""
    off = [i for i in range(len(H)) if i not in set(T)]
    if len(off) < k:
        return None
    xs = [H[i] for i in off[:k]]
    P = interp(xs, [vals[i] for i in off[:k]], q)
    for i in off:
        if peval(P, H[i], q) != vals[i]:
            return None
    return tuple(P)


def mc_pencil_is_genuine(H, q, n, k, w, M, j, c, fam, uv, vv):
    """C1: X^j | P_T and (P_T, P_T/X^j) is a codeword pair at joint
    agreement exactly k+w."""
    ok_div, ok_pair, joint = 0, 0, set()
    for T in fam:
        P = codeword_off_T(uv, T, H, k, q)
        if P is None:
            continue
        if any(P[t] for t in range(min(j, k))):
            continue
        ok_div += 1
        g = tuple(list(P[j:]) + [0] * j)[:k]
        if all(peval(g, H[i], q) == vv[i]
               for i in range(n) if i not in set(T)):
            ok_pair += 1
            joint.add(n - len(T))
    return ok_div, ok_pair, sorted(joint)


def probe(n, k, w, M, q, j, beta_exp=0, gate_depth=2, do_scan=None):
    H, beta, om = make_domain(q, n, beta_exp=beta_exp)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    _, uv, vv = mc_pencil_words(H, q, n, k, w, M, j=j, c=c)
    A = k + w + 1
    fam = mc_family(H, q, n, k, w, M, c)
    nhj = neg_Hj(H, q, j)

    ok_div, ok_pair, joint = mc_pencil_is_genuine(H, q, n, k, w, M, j, c,
                                                  fam, uv, vv)
    sols = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A)
    exactA = [s for s in sols if s["agreement"] == A]
    # gate: anything at agreement >= A+1 anywhere on the pencil?
    gate_break = []
    for d in range(1, gate_depth + 1):
        hi = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A + d)
        gate_break.append(len(hi))

    live = sorted(set(s["z"] for s in exactA))
    outside = [z for z in live if z not in nhj]
    mcd = set()
    for T in fam:
        for x0 in T:
            mcd.add(((-pow(H[x0], j, q)) % q, tuple(sorted(
                set(range(n)) - set(T) | {x0}))))
    extra = [s for s in exactA
             if (s["z"], tuple(sorted(s["Tc"]))) not in mcd]
    extra_out = [s for s in extra if s["z"] not in nhj]

    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
           "beta_exp": beta_exp, "A": A, "c": c,
           "mc_family": len(fam), "mc_Xj_divides_P": ok_div,
           "mc_gives_codeword_pair": ok_pair, "mc_joint_agreements": joint,
           "n_exactA_rays": len(exactA), "n_mc_derived_rays": len(mcd),
           "n_extra_rays": len(extra), "n_extra_rays_outside": len(extra_out),
           "n_live": len(live), "n_live_outside_minusHj": len(outside),
           "live_outside_sample": outside[:16],
           "gate_counts_at_A_plus_d": gate_break,
           "gate_ok": all(x == 0 for x in gate_break),
           "criticality_index": comb(n, A) / float(q) ** w,
           "size_minusHj": len(nhj), "q_minus_1": q - 1}
    if do_scan is None:
        do_scan = comb(n, k) <= 150000
    if do_scan:
        sc = Scan(H, q, k, uv, vv, A)
        rec["scan_live"] = len(sc.live())
        rec["scan_joint_max"] = sc.joint_max
        rec["scan_gate_ok"] = sc.gate_ok()
        rec["scan_max_agreement"] = max([sc.joint_max] + list(sc.hit.values()))
        chk(sorted(sc.live(), key=str) == sorted(live, key=str)
            or not rec["gate_ok"],
            "scan and classifier agree on the live set",
            (n, k, w, M, q, j, len(sc.live()), len(live)))
        chk(sc.joint_max <= A - 1, "MC-2 ceiling: joint_max <= A-1",
            (n, k, w, M, q, j, sc.joint_max))
    print("  n=%2d k=%2d w=%d M=%d q=%-4d j=%d | MC=%-4d (X^j|P:%-4d pair:%-4d "
          "joint%s) rays=%-5d extra=%-5d | live=%-3d OUTSIDE(-H^j)=%-3d "
          "| gate%s %s | X=%.4g"
          % (n, k, w, M, q, j, len(fam), ok_div, ok_pair, joint, len(exactA),
             len(extra), len(live), len(outside), gate_break,
             "OK" if rec["gate_ok"] else "BROKEN", rec["criticality_index"]))
    out["runs"].append(rec)
    if outside and rec["gate_ok"]:
        out["counterexamples"].append(rec)
    return rec


print("=== 0. C1 -- is (w=2, M=4) with j in {1,3} a genuine MC shift pencil? "
      "(n=20, k=6: 4|n, 4|r'=12, w=2<=M=4, M|k+w=8, gcd(3,20)=1) ===")
for q in (41, 61, 101):
    for j in (1, 3):
        r = probe(20, 6, 2, 4, q, j)
        chk(r["mc_family"] > 0, "C1 MC family non-empty", (q, j))
        chk(r["mc_Xj_divides_P"] == r["mc_family"],
            "C1 X^j | P_T for every MC member", (q, j, r["mc_Xj_divides_P"]))
        chk(r["mc_gives_codeword_pair"] == r["mc_family"],
            "C1 every MC member gives a codeword PAIR", (q, j))
        chk(r["mc_joint_agreements"] == [r["A"] - 1],
            "C1 joint agreement is exactly A-1 = k+w",
            (q, j, r["mc_joint_agreements"], r["A"] - 1))

print()
print("=== 1. the q-ladder at n=20, k=6, w=2, M=4: j=1 (control) vs j=3 ===")
for q in primes_for(20, count=7):
    for j in (1, 3):
        r = probe(20, 6, 2, 4, q, j)
        if j == 1:
            chk(r["n_live_outside_minusHj"] == 0,
                "C2 j=1 confinement (THEOREM Y) holds at q=%d" % q,
                (q, r["n_live_outside_minusHj"]))

print()
print("=== 2. beta != 1 (non-trivial coset domain) ===")
for be in (1, 3, 7):
    probe(20, 6, 2, 4, 41, 3, beta_exp=be)
    probe(20, 6, 2, 4, 101, 3, beta_exp=be)

print()
print("=== 3. ODD n, ODD M corner: n=21, k=5, w=2, M=7 "
      "(7|21, 7|r'=14, M|k+w=7); j in {1,2,4,5} are the units mod 21 ===")
for q in primes_for(21, count=4):
    for j in (1, 2, 4, 5):
        r = probe(21, 5, 2, 7, q, j)
        chk(r["mc_family"] > 0, "C1' MC family non-empty", (q, j))
        chk(r["mc_gives_codeword_pair"] == r["mc_family"],
            "C1' every MC member gives a codeword PAIR",
            (q, j, r["mc_gives_codeword_pair"], r["mc_family"]))
        if j == 1:
            chk(r["n_live_outside_minusHj"] == 0,
                "C2' j=1 confinement (THEOREM Y) at n=21, q=%d" % q,
                (q, r["n_live_outside_minusHj"]))

out["verdict"] = ("REFUTED_FOR_j_ge_2" if out["counterexamples"]
                  else "NO_COUNTEREXAMPLE")
out["n_counterexamples"] = len(out["counterexamples"])
with open(os.path.join(CHK, "t2_hunt.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d counterexamples(with gate intact)=%d -> %s"
      % (out["checks"], len(out["fails"]), len(out["counterexamples"]),
         out["verdict"]))

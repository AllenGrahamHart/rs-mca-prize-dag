"""t1_validate.py -- does THEOREM X (advlib docstring) classify the mixed
member's exact-A list, and does THEOREM Y (the j=1 confinement proof) hold?

PRE-REGISTERED PREDICTIONS (round 2; round 1's A1/A2 failed on an
off-by-one in the window length W and are re-registered here unchanged in
content.  Round 1's A3 -- "the banked fixtures are sub-critical" -- was
FALSIFIED by measurement: n=20/24 fixtures have C(n,A)/q^w up to 65 and
still show zero live slopes outside -H.  That falsification is what forced
the structural analysis, so the naive first-moment index is NOT the right
model at j = 1; predictions B1-B6 replace it.)

 B1  The locator classifier's exact-A solution set (T,z) is in exact
     bijection with the (support, slope) pairs of an independent
     theory-free pencil scan, on every fixture.  (mclib is asked as a
     third opinion on the banked six.)
 B2  Every MC-derived solution (T_MC minus x0, -x0^j) is recovered.
 B3  THEOREM Y (j=1): every exact-A solution has -z = gamma/prod(T), so
     Gamma lies in ONE coset of mu_n; with gamma realizable that coset is
     exactly -H.  Prediction: 0 violations, at EVERY fixture including the
     super-critical ones.
 B4  CEILING (j=1): no mixed member (z != 0) has a codeword at agreement
     >= k+w+2, and v (= z = infinity) has none at >= k+w+1.  So the
     tangent gate of an MC shift pencil at j=1 is UNCONDITIONAL.
     Prediction: max pencil agreement is exactly A on every j=1 fixture,
     with the classifier at a_target = A+1 returning the EMPTY set.
 B5  There ARE exact-A rays that are NOT MC-derived (the extras the
     adjudication never looked for) -- they exist already at n=20,24 --
     but B3 pins them inside -H, so |Gamma| <= n survives.
     Prediction: #extras > 0 at the super-critical fixtures.
 B6  DE-REALIZED CONTROL: if gamma is moved off the product coset
     (c -> c*g with g not an n-th power ratio) the MC family is empty and
     the live slopes move to a DIFFERENT coset of mu_n -- still of size
     <= n.  This isolates realizability as the exact hypothesis behind
     "Gamma subset -H".
"""

import json
import os
import sys
from math import comb, log2

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, os.pardir, "band_adjudication"))

from advlib import (INF, Scan, classify_mixed, make_domain, mc_family,
                    mc_pencil_words, mc_c_from_gamma, neg_H, neg_Hj,
                    predicted_coset_j1, primitive_root)

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "fixtures": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def run(n, k, w, M, q, j=1, beta_exp=0, use_mclib=False, c_twist=1,
        do_ceiling=True, tag=""):
    H, beta, om = make_domain(q, n, beta_exp=beta_exp)
    c0 = mc_c_from_gamma(H, q, n, k, w, M)
    c = (c0 * c_twist) % q
    _, uv, vv = mc_pencil_words(H, q, n, k, w, M, j=j, c=c)
    A = k + w + 1
    fam = mc_family(H, q, n, k, w, M, c)
    nh = neg_Hj(H, q, j)

    sols = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A)
    exactA = [s for s in sols if s["agreement"] == A]
    higher = [s for s in sols if s["agreement"] > A]
    cls_pairs = set((s["z"], tuple(sorted(s["Tc"]))) for s in exactA)

    sc = None
    if comb(n, k) <= 200000:
        sc = Scan(H, q, k, uv, vv, A)
        live = sc.live()
        # ---- B1 bijection
        scan_pairs = set()
        for z in live:
            if z == INF:
                continue
            for S in sc.exactA_supports(z):
                scan_pairs.add((z, tuple(sorted(S))))
        chk(scan_pairs == cls_pairs, "B1 classifier == theory-free scan",
            (tag, n, k, w, M, q, j, len(scan_pairs), len(cls_pairs),
             sorted(scan_pairs ^ cls_pairs)[:2]))
    else:
        live = sorted(set(s["z"] for s in exactA))
    outside = [z for z in live if z == INF or z not in nh]

    # ---- B2 MC-derived recovery
    missing = 0
    for T in fam:
        for x0 in T:
            z0 = (-pow(H[x0], j, q)) % q
            Tc = tuple(sorted(set(range(n)) - set(T) | {x0}))
            if (z0, Tc) not in cls_pairs:
                missing += 1
    chk(missing == 0 or not fam, "B2 MC-derived solutions all classified",
        (tag, n, k, w, M, q, j, missing, len(fam)))

    # ---- B3 THEOREM Y (j = 1 only)
    coset, gamma = predicted_coset_j1(H, q, n, k, w, c)
    if j == 1:
        bad = [s for s in exactA if s["z"] not in coset]
        chk(not bad, "B3 THEOREM Y: every exact-A slope in the predicted coset",
            (tag, n, k, w, M, q, [s["z"] for s in bad[:4]]))
        badlive = [z for z in live if z == INF or z not in coset]
        chk(not badlive, "B3b every LIVE slope in the predicted coset",
            (tag, n, k, w, M, q, badlive[:4]))

    # ---- B4 ceiling
    ceil_ok = None
    if do_ceiling:
        hi = classify_mixed(H, beta, q, n, k, w, c, j, a_target=A + 1)
        ceil_ok = (len(hi) == 0)
        rec_hi = len(hi)
        if j == 1:
            chk(ceil_ok, "B4 no mixed member reaches agreement A+1 (j=1)",
                (tag, n, k, w, M, q, rec_hi))
        if sc is not None:
            chk((max([sc.joint_max] + list(sc.hit.values())) <= A) == ceil_ok,
                "B4b scan agrees with the classifier on the ceiling",
                (tag, n, k, w, M, q))
    else:
        rec_hi = None

    n_mc_derived = len(fam) * (n - k - w)
    X = comb(n, A) / float(q) ** w
    rec = {"tag": tag, "n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
           "beta_exp": beta_exp, "c_twist": c_twist, "A": A, "c": c,
           "gamma": gamma, "gamma_realizable": pow(gamma, n, q) ==
           pow(beta, n - k - w, q),
           "mc_family": len(fam), "n_mc_derived_rays": n_mc_derived,
           "joint_max": sc.joint_max if sc else None,
           "gate_ok": sc.gate_ok() if sc else (rec_hi == 0),
           "max_agreement_pencil":
               max([sc.joint_max] + list(sc.hit.values())) if sc else None,
           "scanned": sc is not None,
           "joint_max_ceiling_note": "MC-2 forces joint_max <= A-1",
           "n_live": len(live), "n_live_outside_minusHj": len(outside),
           "live_outside_minusHj": [str(z) for z in outside[:12]],
           "n_exactA_rays": len(exactA),
           "n_extra_rays_beyond_MC": len(exactA) - n_mc_derived,
           "n_solutions_agreement_gt_A": len(higher),
           "classifier_at_A_plus_1": rec_hi,
           "predicted_coset_is_minusH": coset == neg_H(H, q),
           "criticality_index": X, "log2_criticality": log2(X) if X else None,
           "minusH_is_all_of_Fq_star": len(neg_H(H, q)) == q - 1}
    print("  %-14s n=%2d k=%2d w=%d M=%d q=%-4d j=%d tw=%-3d | MC=%-4d "
          "rays=%-5d (MC-derived %-5d, EXTRA %-5d) live=%-3d out(-H^j)=%-3d "
          "gate=%-5s | X=%.4g"
          % (tag, n, k, w, M, q, j, c_twist, len(fam), len(exactA),
             n_mc_derived, len(exactA) - n_mc_derived, len(live),
             len(outside), rec["gate_ok"], X))

    if use_mclib:
        import mclib
        sc2 = mclib.Scan(H, q, k, uv, vv, A)
        chk(sorted(map(str, sc2.live())) == sorted(map(str, live)),
            "B1b mclib live-slope set agrees", (n, q, j))
        rec["mclib_live"] = len(sc2.live())
    out["fixtures"].append(rec)
    return rec


print("=== 1. banked band_adjudication fixtures (independent replay) ===")
for (n, k, w, M, q) in [(16, 4, 2, 2, 17), (16, 4, 2, 2, 97),
                        (16, 4, 2, 2, 113), (16, 4, 2, 2, 193),
                        (20, 4, 4, 4, 41), (20, 4, 4, 4, 101)]:
    run(n, k, w, M, q, j=1, use_mclib=True, tag="banked")

print()
print("=== 2. SUPER-CRITICAL j=1 fixtures (X = C(n,A)/q^w up to ~10^2) ===")
for (n, k, w, M, q) in [(20, 4, 2, 2, 41), (20, 4, 2, 2, 101),
                        (20, 6, 2, 2, 41), (24, 4, 2, 2, 73),
                        (24, 6, 2, 2, 73), (16, 6, 2, 2, 97),
                        (28, 4, 2, 2, 113), (32, 4, 2, 2, 97)]:
    if n % M or (n - k - w) % M or w > M:
        continue
    run(n, k, w, M, q, j=1, tag="supercrit")

print()
print("=== 3. beta != 1 (non-trivial coset domain) ===")
for be in (1, 3, 5):
    run(20, 4, 2, 2, 41, j=1, beta_exp=be, tag="beta%d" % be)

print()
print("=== 4. B6 de-realized control: gamma pushed off the product coset ===")
for (n, k, w, M, q) in [(20, 4, 2, 2, 41), (24, 4, 2, 2, 73)]:
    g = primitive_root(q)
    r = run(n, k, w, M, q, j=1, c_twist=g, tag="derealized")
    chk(r["mc_family"] == 0, "B6 de-realized => MC family empty",
        (n, q, r["mc_family"]))
    chk(r["n_live"] <= n, "B6 de-realized => still |Gamma| <= n",
        (n, q, r["n_live"]))
    chk(not r["predicted_coset_is_minusH"],
        "B6 de-realized => predicted coset is NOT -H", (n, q))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "t1_validate.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))

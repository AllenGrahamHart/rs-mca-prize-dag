"""e7_highX.py -- push w = 3 to HIGH X.

Every one of the 18 banked counterexamples has w = 2.  e4/e6 found no excess
at w = 3 up to X = 4.44.  The banked calibration of record says the excess is
governed by X alone ("X < 1 -> zero extras; reliable escapes from X ~ 10").
That predicts an excess at w = 3, X ~ 14.  This tests it.

  n = 33, k = 3, w = M = 3, q = 67:  r = 27 = 9M, A = 7, r' = 26,
  X = C(33,7)/67^3 = 4272048/300763 = 14.20,  j in {1,2}, gcd(2,33) = 1.

Ground truth Scan is cheap here (C(33,3) = 5456).  Classification uses the
lean window classifier (verified identical to the full one).
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

JSEL = [int(t) for t in os.environ.get("JSEL", "1,2").split(",")]
FIX = [(33, 3, 3, 3, [67])]

L = G.Ledger()
rows = []
for (n, k, w, M, qs) in FIX:
    r = n - k - w
    A = k + w + 1
    rp = n - A
    assert n % M == 0 and r % M == 0 and w <= M
    js = [j for j in range(1, M) if j in JSEL]
    cnA = G.comb(n, A)
    for q in qs:
        H, beta, om = G.make_domain(q, n, 0)
        mu = G.mu_n_set(H, q)
        c = G.mc_c_from_gamma(H, q, n, k, w, M)
        fam = [set(t) for t in G.mc_family(H, q, n, k, w, M, c)]
        X = cnA / pow(q, w)
        print("n=%d k=%d w=M=%d q=%d  A=%d r'=%d  X=%.4g  C(n,r')=%d  "
              "MC family=%d  js=%s" % (n, k, w, q, A, rp, X,
                                       G.comb(n, rp), len(fam), js))
        allsol = G.classify_lean(H, q, n, k, w, c, js)
        for j in js:
            uv, vv = G.pencil_words(H, q, n, k, w, c, j)
            sc = G.Scan(H, q, k, uv, vv, A)
            gam = set(z for z in sc.live() if z != G.INF and z != 0)
            sols = allsol[j]
            struct = [s for s in sols
                      if any(set(s["Tidx"]) < F and len(F - set(s["Tidx"])) == 1
                             for F in fam)]
            classes = set(G.coset_rep(s["e_jm1_inv"], mu, q) for s in sols)
            Ej = len(classes)
            gate = sc.gate_ok()
            nHj = G.neg_Hj(H, q, j)
            outside = len([z for z in gam if z not in nHj])
            L.chk(len(gam) <= n * Ej, "(P4) |Gamma| <= n.E_j", (n, q, j))
            L.chk(set(s["z"] for s in sols) == gam or not gate,
                  "classifier == theory-free Gamma", (n, q, j))
            if j == 1:
                L.chk(Ej == 1, "j=1 => E_1 = 1 (THEOREM Y)", (Ej,))
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "A": A, "X": X, "gcd_j_n": math.gcd(j, n),
                         "gate_ok": gate, "Gamma": len(gam), "E_j": Ej,
                         "n_sols": len(sols), "n_structured": len(struct),
                         "n_sporadic": len(sols) - len(struct),
                         "outside_negHj": outside, "prize_shape": w == M})
            print("  j=%d g=%d | X=%7.3g gate=%-5s | |G|=%3d (%.2fn) E_j=%d "
                  "sols=%4d struct=%4d SPORADIC=%4d out=%2d %s" %
                  (j, math.gcd(j, n), X, gate, len(gam), len(gam) / n, Ej,
                   len(sols), len(struct), len(sols) - len(struct), outside,
                   "*** EXCESS ***" if Ej > 1 else ""))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
tag = "_".join(str(j) for j in JSEL)
with open(os.path.join(HERE, "checkpoints", "e7_highX_j%s.json" % tag), "w") as f:
    json.dump({"doc": __doc__, "rows": rows,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
ok = L.report("e7_highX")
print("OK" if ok else "FAILURES PRESENT")

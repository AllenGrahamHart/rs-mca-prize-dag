"""e3_razor.py -- FALSIFIER F2, run on the sharpest possible edge.

Take the two families that PRODUCED the 18 counterexamples and sweep q
straight through the gate threshold X = C(n,A)/q^w = 1, from X > 1 (where
the excess is banked and certified) down to X < 1.

F2 fires iff some gate-intact fixture with X < 1 has |Gamma_j| > n.

Family 1: n=20, k=6, w=2, M=4, j=3.  X = C(20,9)/q^2, X=1 at q = 409.8
Family 2: n=21, k=5, w=2, M=7, j in {2,4,5}. X = C(21,8)/q^2, X=1 at q=451.1
"""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

L = G.Ledger()
FAM = [
    # n, k, w, M, [j...], [q...], beta_exp
    (20, 6, 2, 4, [3], [281, 401, 421, 461, 521, 541, 601], 0),
    (20, 6, 2, 4, [3], [401, 421, 461, 521], 1),
    (20, 6, 2, 4, [3], [401, 421, 461, 521], 7),
    (21, 5, 2, 7, [2, 4, 5], [337, 379, 421, 463, 547, 631], 0),
]

rows = []
fired = []
for (n, k, w, M, js, qs, be) in FAM:
    A = k + w + 1
    rp = n - A
    cnA = G.comb(n, A)
    for q in qs:
        if (q - 1) % n or not G.is_prime(q):
            print("skip bad q", q)
            continue
        H, beta, om = G.make_domain(q, n, be)
        mu = G.mu_n_set(H, q)
        c = G.mc_c_from_gamma(H, q, n, k, w, M)
        allsol = G.classify_multi(H, q, n, k, w, c, js)
        X = cnA / pow(q, w)
        for j in js:
            uv, vv = G.pencil_words(H, q, n, k, w, c, j)
            sc = G.Scan(H, q, k, uv, vv, A)
            gam = set(z for z in sc.live() if z != G.INF and z != 0)
            sols = allsol[j]
            classes = set()
            for s in sols:
                inv = [pow(x, q - 2, q) for x in s["T"]]
                classes.add(G.coset_rep(G.esym(inv, q, j - 1)[j - 1], mu, q))
            Ej = len(classes)
            nHj = G.neg_Hj(H, q, j)
            outside = len([z for z in gam if z not in nHj])
            gate = sc.gate_ok()
            L.chk(len(gam) <= n * Ej, "(P4) |Gamma| <= n.E_j", (n, q, j))
            f2 = gate and X < 1 and len(gam) > n
            if f2:
                fired.append((n, k, w, M, q, j, be, len(gam), X))
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "beta_exp": be, "X": X, "X_lt_1": X < 1,
                         "gate_ok": gate, "Gamma": len(gam),
                         "Gamma_over_n": round(len(gam) / n, 3), "E_j": Ej,
                         "outside_negHj": outside, "n_sols": len(sols),
                         "F2_fired": f2})
            print("n=%2d w=%d M=%d q=%4d j=%d b=%d | X=%7.4f %-5s gate=%-5s | "
                  "|G|=%3d (%.2fn) E_j=%d outside=%2d  %s" %
                  (n, w, M, q, j, be, X, "X<1" if X < 1 else "X>=1", gate,
                   len(gam), len(gam) / n, Ej, outside,
                   "*** F2 FIRED ***" if f2 else ""))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "e3_razor.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows, "F2_fired": fired,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
print("\nF2 fired on %d fixtures" % len(fired))
sub = [r for r in rows if r["X_lt_1"] and r["gate_ok"]]
if sub:
    print("gate-intact X<1 fixtures: %d ; max |Gamma|/n = %.3f ; max E_j = %d"
          % (len(sub), max(r["Gamma_over_n"] for r in sub),
             max(r["E_j"] for r in sub)))
sup = [r for r in rows if not r["X_lt_1"] and r["gate_ok"]]
if sup:
    print("gate-intact X>=1 fixtures: %d ; max |Gamma|/n = %.3f ; max E_j = %d"
          % (len(sup), max(r["Gamma_over_n"] for r in sup),
             max(r["E_j"] for r in sup)))
ok = L.report("e3_razor")
print("OK" if ok else "FAILURES PRESENT")

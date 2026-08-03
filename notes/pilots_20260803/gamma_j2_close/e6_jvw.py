"""e6_jvw.py -- THE CONTROLLED DISCRIMINATOR: is the operative condition
`w = M` (prize-row shape) or `j < w` (the regime where the (X^j+z)
factorisation (P2) has non-empty content)?

Every prize-shape fixture has BOTH (w = M forces j <= M-1 = w-1).  Every
banked counterexample has NEITHER (w < M and j >= w).  To separate them we
need a fixture with  w < M  but  j < w  -- and, to be a real test, with
X > 1.

    n = 21, k = 4, w = 3, M = 7, q = 43:   r = 14 = 2M, A = 8, X = 2.559
    j runs 1..M-1 = 1..6, so j = 1,2 are j < w and j = 3..6 are j >= w,
    ALL AT THE SAME X, SAME FIXTURE, SAME PENCIL.

Prediction under (H-B) "j < w kills the excess":  E_j = 1 for j = 1,2 and
E_j >= 2 for some j in 3..6.
Prediction under "only w = M matters":  excess at every j >= 2.
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

L = G.Ledger()
FIX = [
    # n, k, w, M, [q...]   -- w < M but small j is BELOW w
    (21, 4, 3, 7, [43, 127]),
    (20, 5, 3, 4, [41, 101]),      # w=3 < M=4 : j=1,2 below w ; j=3 above
    (18, 5, 3, 6, [37, 73]),       # w=3 < M=6
]

rows = []
for (n, k, w, M, qs) in FIX:
    r = n - k - w
    A = k + w + 1
    rp = n - A
    if n % M or r % M or w > M or r < M:
        print("skip MC-3", (n, k, w, M), "r=", r)
        continue
    js = list(range(1, M))
    cnA = G.comb(n, A)
    for q in qs:
        if (q - 1) % n or not G.is_prime(q) or q <= n + 1:
            continue
        H, beta, om = G.make_domain(q, n, 0)
        mu = G.mu_n_set(H, q)
        c = G.mc_c_from_gamma(H, q, n, k, w, M)
        fam = [set(t) for t in G.mc_family(H, q, n, k, w, M, c)]
        if not fam:
            print("empty MC family", (n, k, w, M, q))
            continue
        X = cnA / pow(q, w)
        allsol = G.classify_multi(H, q, n, k, w, c, js)
        for j in js:
            uv, vv = G.pencil_words(H, q, n, k, w, c, j)
            sc = G.Scan(H, q, k, uv, vv, A)
            gam = set(z for z in sc.live() if z != G.INF and z != 0)
            sols = allsol[j]
            struct = [s for s in sols
                      if any(set(s["Tidx"]) < F and len(F - set(s["Tidx"])) == 1
                             for F in fam)]
            classes = set()
            for s in sols:
                inv = [pow(x, q - 2, q) for x in s["T"]]
                classes.add(G.coset_rep(G.esym(inv, q, j - 1)[j - 1], mu, q))
            Ej = len(classes)
            gate = sc.gate_ok()
            nHj = G.neg_Hj(H, q, j)
            outside = len([z for z in gam if z not in nHj])
            L.chk(len(gam) <= n * Ej, "(P4) |Gamma| <= n.E_j", (n, k, q, j))
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "X": X, "j_lt_w": j < w, "prize_shape": (w == M),
                         "gcd_j_n": math.gcd(j, n), "gate_ok": gate,
                         "Gamma": len(gam), "E_j": Ej,
                         "n_sols": len(sols), "n_structured": len(struct),
                         "n_sporadic": len(sols) - len(struct),
                         "outside_negHj": outside})
            print("n=%2d k=%2d w=%d M=%d q=%4d j=%d %-7s g=%d | X=%7.3g "
                  "gate=%-5s | |G|=%3d (%.2fn) E_j=%d spor=%4d out=%2d" %
                  (n, k, w, M, q, j, "j<w" if j < w else "j>=w",
                   math.gcd(j, n), X, gate, len(gam), len(gam) / n, Ej,
                   len(sols) - len(struct), outside))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "e6_jvw.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)

lo = [r for r in rows if r["j_lt_w"] and r["gate_ok"]]
hi = [r for r in rows if not r["j_lt_w"] and r["gate_ok"]]
print("\n--- w < M fixtures, split by j vs w ---")
print("j <  w : %2d rows, max E_j = %d, max |Gamma|/n = %.2f, max X = %.3g"
      % (len(lo), max(r["E_j"] for r in lo),
         max(r["Gamma"] / r["n"] for r in lo), max(r["X"] for r in lo)))
print("j >= w : %2d rows, max E_j = %d, max |Gamma|/n = %.2f, max X = %.3g"
      % (len(hi), max(r["E_j"] for r in hi),
         max(r["Gamma"] / r["n"] for r in hi), max(r["X"] for r in hi)))
ok = L.report("e6_jvw")
print("OK" if ok else "FAILURES PRESENT")

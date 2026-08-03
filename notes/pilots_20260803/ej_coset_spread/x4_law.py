"""x4_law.py -- the empirical boundary of E_j, and the OUT-OF-SAMPLE test of
the post-hoc hypothesis (S-G) of PREREG AMENDMENT 1.

Falsifiers: F-K (a gate-intact prize-shape fixture with j < w, gcd(j,n) = 1 and
E_j >= 2), F-I (E_j > 29.6 n), F-J (|Gamma_j| > n E_j), F-M (a gate-intact row
with sporadics, or a gate-broken row with none).

Every fixture here is DISJOINT from x1_identities.py's list, so (S-G) is being
tested out of sample.  It also reproduces the banked anomaly
(n=33, k=3, w=M=3, q=67, j=2) with E_j = 2 at j < w and checks the gate there.

BATCH=a  small/medium ladder (default)   BATCH=b  the n = 30, 33 tail
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ejlib as E                                                # noqa: E402

L = E.Ledger()
BATCH = os.environ.get("BATCH", "a")

FIX_A = [                       # (n, k, w, M, [q...])  -- all fresh
    (12, 6, 3, 3, [13, 37, 61]),
    (15, 6, 3, 3, [31, 61, 151]),
    (15, 5, 5, 5, [31, 61]),
    (18, 6, 3, 3, [19, 37, 73]),
    (21, 6, 3, 3, [43, 127]),
    (24, 3, 3, 3, [73, 97]),
    (24, 4, 4, 4, [73]),
    (18, 9, 3, 3, [19, 37, 73]),
]
FIX_B = [
    (27, 3, 3, 3, [109]),
    (30, 3, 3, 3, [31, 61]),
    (33, 3, 3, 3, [67]),          # <== reproduces the banked E_j = 2 anomaly
]
FIX = FIX_A if BATCH == "a" else FIX_B

rows, fired = [], []
for (n, k, w, M, qs) in FIX:
    if not E.mc3_ok(n, k, w, M):
        print("skip MC-3", (n, k, w, M))
        continue
    A = k + w + 1
    rp = n - A
    r = n - k - w
    js = list(range(1, M))
    cnA = E.comb(n, A)
    for q in qs:
        if (q - 1) % n or not E.is_prime(q) or q <= n + 1:
            continue
        H, beta, om = E.make_domain(q, n, 0)
        mu = E.mu_n_set(H, q)
        c = E.mc_c_from_gamma(H, q, n, k, w, M)
        structs, fam = E.structured_sets(H, q, n, k, w, M, c)
        if not fam:
            continue
        X = cnA / pow(q, w)
        allsol = E.G.classify_lean(H, q, n, k, w, c, js)
        for j in js:
            sols = allsol[j]
            cls = set(E.coset_rep(s["e_jm1_inv"], mu, q) for s in sols)
            Ej = len(cls)
            nstruct = sum(1 for s in sols
                          if frozenset(s["Tidx"]) in structs)
            spor = len(sols) - nstruct
            uv, vv = E.pencil_words(H, q, n, k, w, c, j)
            sc = E.Scan(H, q, k, uv, vv, A)
            gam = set(z for z in sc.live() if z != E.INF and z != 0)
            gate = sc.gate_ok()
            L.chk(len(gam) <= n * Ej, "F-J |Gamma_j| <= n.E_j",
                  (n, k, w, M, q, j, len(gam), n * Ej))
            L.chk(Ej <= 29.6 * n, "F-I E_j <= 29.6 n", (n, k, w, M, q, j, Ej))
            law = (spor > 0) == (not gate)
            if not law:
                fired.append(("F-M", n, k, w, M, q, j, spor, gate))
            L.chk(law, "F-M (S-G) sporadic <=> gate broken",
                  (n, k, w, M, q, j, spor, gate))
            f_k = gate and j < w and math.gcd(j, n) == 1 and Ej >= 2
            if f_k:
                fired.append(("F-K", n, k, w, M, q, j, Ej, X))
            L.chk(not f_k, "F-K gate-intact j<w gcd=1 has E_j=1",
                  (n, k, w, M, q, j, Ej))
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "A": A, "rp": rp, "r": r, "X": X,
                         "gcd_j_n": math.gcd(j, n), "j_lt_w": j < w,
                         "gate_ok": gate, "Gamma": len(gam), "E_j": Ej,
                         "n_sols": len(sols), "n_struct": nstruct,
                         "n_sporadic": spor, "sg_law": law,
                         "prize_shape": (w == M), "F_K": f_k})
            print("n=%2d k=%2d w=M=%d q=%4d j=%d g=%d | X=%9.3g gate=%-5s | "
                  "sols=%5d (spor %5d) E_j=%d |G|=%3d %s%s" %
                  (n, k, w, q, j, math.gcd(j, n), X, gate, len(sols), spor,
                   Ej, len(gam), "*** F-K ***" if f_k else "",
                   "" if law else "  <<< S-G VIOLATED"))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "x4_law_%s.json" % BATCH),
          "w") as f:
    json.dump({"doc": __doc__, "rows": rows, "fired": fired,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)

gi = [r for r in rows if r["gate_ok"]]
jw = [r for r in rows if r["j_lt_w"]]
print("\nrows %d | gate-intact %d | j<w %d | max E_j = %d (gate-intact max %d)"
      % (len(rows), len(gi), len(jw), max(r["E_j"] for r in rows),
         max([r["E_j"] for r in gi] + [0])))
print("E_j >= 2 rows:")
for r in rows:
    if r["E_j"] >= 2:
        print("   n=%d k=%d w=M=%d q=%d j=%d gcd=%d X=%.3g gate=%s spor=%d E_j=%d"
              % (r["n"], r["k"], r["w"], r["q"], r["j"], r["gcd_j_n"], r["X"],
                 r["gate_ok"], r["n_sporadic"], r["E_j"]))
ok = L.report("x4_law_%s" % BATCH)
print("OK" if ok else "FAILURES PRESENT")

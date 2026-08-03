"""e1_frame.py -- validate the re-derived frame (P1),(P2),(P3'),(P4),(P5)
against THEORY-FREE GROUND TRUTH, on prize-shape (w = M) and banked-shape
(w < M) fixtures.

Falsifier F8 lives here: any solution violating (P1)-(P3') fires it.
Falsifier F1 lives here: |Gamma_j| > n . E_j fires it.

Ground truth = Scan (Lagrange interpolation over all k-subsets, no theory).
"""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

L = G.Ledger()

# (n, k, w, M, q, beta_exp, [j...])   -- w == M  =>  PRIZE-ROW SHAPE
FIX = [
    # ---- prize-row shape: w = M, so j <= M-1 = w-1 (j < w always) ----
    (18, 6, 6, 6, 37, 0, [1, 5]),
    (18, 6, 6, 6, 73, 0, [1, 5]),
    (18, 6, 6, 6, 37, 1, [1, 5]),
    (15, 3, 3, 3, 31, 0, [1, 2]),
    (15, 5, 5, 5, 31, 0, [1, 2, 4]),
    (15, 5, 5, 5, 61, 2, [1, 2, 4]),
    (16, 4, 4, 4, 17, 0, [1, 3]),
    (16, 4, 4, 4, 97, 0, [1, 3]),
    (16, 4, 4, 4, 97, 3, [1, 3]),
    (20, 4, 4, 4, 41, 0, [1, 3]),
    (20, 8, 4, 4, 41, 0, [1, 3]),
    (21, 3, 3, 3, 43, 0, [1, 2]),
    # ---- banked shape (w < M): where the 18 counterexamples live ----
    (20, 6, 2, 4, 41, 0, [1, 3]),
    (20, 6, 2, 4, 101, 0, [1, 3]),
    (16, 4, 2, 4, 17, 0, [1, 3]),
    (16, 4, 2, 4, 97, 0, [1, 3]),
]

out = []
for (n, k, w, M, q, be, js) in FIX:
    r = n - k - w
    if r % M or n % M or w > M:
        print("skip (MC-3 violated)", (n, k, w, M))
        continue
    H, beta, om = G.make_domain(q, n, be)
    mu = G.mu_n_set(H, q)
    A = k + w + 1
    rp = n - A
    c = G.mc_c_from_gamma(H, q, n, k, w, M)
    fam = G.mc_family(H, q, n, k, w, M, c)
    gamma = ((-1) ** rp * c) % q          # gamma = (-1)^{r'} c,  r' = rp
    cnA, qw = G.X_index(n, A, q, w)
    for j in js:
        if j > M - 1:
            continue
        uv, vv = G.pencil_words(H, q, n, k, w, c, j)
        sc = G.Scan(H, q, k, uv, vv, A)
        sols = G.classify(H, q, n, k, w, c, j)

        # ---------- ground-truth agreement of the classifier ----------
        gam_scan = set(z for z in sc.live() if z != G.INF and z != 0)
        gam_cls = set(s["z"] for s in sols)
        gate = sc.gate_ok()
        if gate:
            L.chk(gam_scan == gam_cls,
                  "classifier == theory-free Gamma (%s j=%d)" % ((n, k, w, M, q, be), j),
                  (sorted(gam_scan)[:6], sorted(gam_cls)[:6]))

        # ---------- per-solution identity checks ----------
        classes = set()
        for s in sols:
            T, m, z = s["T"], s["m"], s["z"]
            P = G.prodT(T, q)
            inv = [pow(x, q - 2, q) for x in T]
            eT = G.esym(T, q, min(rp, max(w, j) + 2))
            eTi = G.esym(inv, q, min(rp, max(w, j) + 2))

            def mc(t):
                return m[t] if 0 <= t <= rp else 0

            # (P1) s-form  <=>  alpha/beta form
            ok = True
            for t in ([0] + list(range(rp + 1 - w, rp - j + 1))):
                if 0 <= t and t + j <= rp + 0 or t == 0:
                    if (mc(t) + z * mc(t + j)) % q:
                        ok = False
            L.chk(ok, "(P1-beta) m_s + z m_{s+j} = 0")
            ok = True
            for rho in range(max(0, j - w), j):
                lhs = mc(rho)
                rhs = (-c * pow(z, q - 2, q) * mc(rp - j + 1 + rho)) % q
                if (lhs - rhs) % q:
                    ok = False
            L.chk(ok, "(P1-alpha) m_rho = -(c/z) m_{r'-j+1+rho}")

            # (P3') z = (-1)^j gamma / e_{r'-j+1}(T)   [universal]
            e_top = G.esym(T, q, rp)[rp - j + 1] if rp - j + 1 <= rp else 0
            L.chk(e_top and (z * e_top - ((-1) ** j) * gamma) % q == 0,
                  "(P3') z = (-1)^j gamma / e_{r'-j+1}(T)",
                  (n, k, w, M, q, j, z))
            # and its factorisation through prod(T) . e_{j-1}(T^-1)
            L.chk((e_top - P * eTi[j - 1]) % q == 0,
                  "e_{r'-j+1}(T) = prod(T) e_{j-1}(T^-1)")

            # banked identity: z = (-1)^{j+1} / e_j(T^{-1})
            L.chk(eTi[j] and (z * eTi[j] - ((-1) ** (j + 1))) % q == 0,
                  "banked: z = (-1)^{j+1}/e_j(T^-1)")

            # (P2) (1+zY^j) E_T = G mod Y^w, deg G <= j-1
            # E_T coefficients: [Y^u] E_T = (-1)^u e_u(T)
            ok = True
            for u in range(j, w):
                lhs = (((-1) ** u) * eT[u] + z * ((-1) ** (u - j)) * eT[u - j]) % q
                if lhs:
                    ok = False
            L.chk(ok, "(P2) e_u(T) = lambda e_{u-j}(T), u=j..w-1")

            # prod(T) always in x0^{r'} mu_n  (the coset engine of P4)
            L.chk(G.coset_rep(P, mu, q) == G.coset_rep(pow(H[0], rp, q), mu, q),
                  "prod(T) in x0^{r'} mu_n")

            classes.add(G.coset_rep(eTi[j - 1], mu, q))

        Ej = len(classes)
        nGam = len(gam_scan)
        # ---------- (P4) THE REDUCTION THEOREM ----------
        L.chk(nGam <= n * Ej, "(P4) |Gamma| <= n . E_j",
              (n, k, w, M, q, be, j, nGam, Ej))
        if j == 1:
            L.chk(Ej <= 1, "(P4) j=1 => E_1 = 1 (THEOREM Y)", (Ej,))

        # ---------- (P5) structured solutions sit in -H^j ----------
        nHj = G.neg_Hj(H, q, j)
        struct = 0
        for TM in fam:
            TMset = set(TM)
            for y in TM:
                Ti = sorted(TMset - {y})
                zz = [s for s in sols if s["Tidx"] == Ti]
                if zz:
                    struct += 1
                    L.chk(zz[0]["z"] == (-pow(H[y], j, q)) % q,
                          "(P5) structured z = -y^j")
        out.append({
            "n": n, "k": k, "w": w, "M": M, "q": q, "beta_exp": be, "j": j,
            "A": A, "rp": rp, "c": c, "gamma": gamma,
            "prize_shape": (w == M), "j_lt_w": (j < w),
            "gcd_j_n": __import__("math").gcd(j, n),
            "gate_ok": gate, "joint_max": sc.joint_max,
            "Gamma": nGam, "Gamma_over_n": round(nGam / n, 4),
            "E_j": Ej, "n_sols": len(sols), "n_structured": struct,
            "outside_negHj": len([z for z in gam_scan if z not in nHj]),
            "mc_family": len(fam),
            "X_num_C(n,A)": cnA, "X_den_q^w": qw,
            "X_ge_1": cnA >= qw, "X_float": cnA / qw,
        })
        print("%-28s j=%d gate=%-5s |Gamma|=%3d (%.2fn) E_j=%d sols=%4d "
              "out=%2d X=%.3g %s" %
              ((n, k, w, M, q, be), j, gate, nGam, nGam / n, Ej, len(sols),
               out[-1]["outside_negHj"], cnA / qw,
               "PRIZE" if w == M else "w<M"))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "e1_frame.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": out,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
ok = L.report("e1_frame")
print("OK" if ok else "FAILURES PRESENT")

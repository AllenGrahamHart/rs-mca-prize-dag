"""x2_action.py -- CLAIM G: the mu_g action on the admissible set.
Falsifiers F-C (the action), F-D (the lower bound |Gamma_j| >= g' E_j),
F-E (gcd(n-k-w, n) = M at the three prize rows).

CLAIM G.  For zeta in mu_n, T -> zeta.T is a bijection of the rp-subsets of H
that sends z -> zeta^j z and multiplies the c-normalisation (Q8) by zeta^{r},
r = n-k-w.  Hence mu_g with g := gcd(r,n) acts on the ADMISSIBLE set, Gamma_j is
mu_{g'}-invariant with g' := g/gcd(j,g), and

        g' . E_j  <=  |Gamma_j|  <=  n . E_j          (G1)+(THEOREM D)

At the prize rows g = M exactly, so E_j and |Gamma_j|/n agree within the factor
N = n/M <= 512: the E_j reduction is a RE-COORDINATISATION, not a strictly
smaller object.  That is the claim this experiment is built to kill or bank.
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

# ---------------------------------------------------------- (1) prize rows
print("--- F-E: exact prize-row arithmetic (integers, no floats) ---")
prize = []
for (lab, n, k, w) in E.PRIZE_ROWS:
    M = w
    r = n - k - w
    rp = n - (k + w + 1)
    N = n // M
    m = r // M
    g = E.gcd(r, n)
    L.chk(n % M == 0, "M | n", lab)
    L.chk(r % M == 0, "M | r", lab)
    L.chk(w <= M, "w <= M", lab)
    L.chk(g == M, "F-E gcd(n-k-w, n) == M", (lab, g, M))
    L.chk(m % 2 == 1, "m odd (so gcd(r,n)=M)", (lab, m))
    prize.append({"row": lab, "n": n, "k": k, "w": w, "M": M, "r": r,
                  "rp": rp, "N": N, "m": m, "gcd_r_n": g, "g_eq_M": g == M})
    print("  row %-4s n=2^%d k=2^%d w=M=2^%d  r=M*%d (m %s)  gcd(r,n)=%d = M? %s"
          "  N=n/M=%d" % (lab, n.bit_length() - 1, k.bit_length() - 1,
                          M.bit_length() - 1, m, "odd" if m % 2 else "EVEN",
                          g, g == M, N))
print("  => for j odd, g' = g/gcd(j,g) = M, so  E_j <= N.|Gamma_j|/n  with "
      "N = %s" % [p["N"] for p in prize])

# ------------------------------------------------- (2) the action, toy scale
print("\n--- F-C / F-D: the action and the lower bound, toy scale ---")
FIX = [
    (12, 3, 3, 3, [13, 37]),
    (15, 3, 3, 3, [31, 61]),
    (18, 3, 3, 3, [19, 37]),
    (21, 3, 3, 3, [43, 127]),
    (12, 4, 4, 4, [13, 37]),
    (16, 4, 4, 4, [17, 97]),
    (20, 4, 4, 4, [41, 101]),
    (16, 8, 4, 4, [17, 97]),
    (20, 5, 5, 5, [41, 101]),
    (18, 6, 6, 6, [19, 37]),
    (21, 4, 3, 7, [43, 127]),
    (20, 5, 3, 4, [41, 101]),
    (20, 6, 2, 4, [41, 101, 401]),        # the banked counterexample shape
    (21, 5, 2, 7, [43, 127]),             # ditto
]
rows = []
for (n, k, w, M, qs) in FIX:
    if not E.mc3_ok(n, k, w, M):
        continue
    A = k + w + 1
    rp = n - A
    r = n - k - w
    g = E.gcd(r, n)
    js = list(range(1, M))
    for q in qs:
        if (q - 1) % n or not E.is_prime(q) or q <= n + 1:
            continue
        H, beta, om = E.make_domain(q, n, 0)
        mu = E.mu_n_set(H, q)
        idx = dict((H[i], i) for i in range(n))
        c = E.mc_c_from_gamma(H, q, n, k, w, M)
        if not E.mc_family(H, q, n, k, w, M, c):
            continue
        # mu_g as a subset of mu_n, acting on H by multiplication
        mug = sorted(set(pow(t, n // g, q) for t in mu))
        L.chk(len(mug) == g, "|mu_g| == g", (n, q, g, len(mug)))
        allsol = E.G.classify_lean(H, q, n, k, w, c, js)
        for j in js:
            sols = allsol[j]
            if not sols:
                continue
            S = set((tuple(sorted(s["Tidx"])), s["z"]) for s in sols)
            # F-C : mu_g preserves admissibility, with z -> zeta^j z
            for zeta in mug:
                for (Tc, z) in list(S):
                    Tz = tuple(sorted(idx[(zeta * H[i]) % q] for i in Tc))
                    L.chk((Tz, (pow(zeta, j, q) * z) % q) in S,
                          "F-C mu_g action closes", (n, k, w, M, q, j, zeta))
            # the action must FAIL for a zeta outside mu_g (sanity: the
            # constraint is exactly zeta^r = 1)
            outside = [t for t in mu if pow(t, r, q) != 1]
            if outside:
                bad = 0
                for zeta in outside:
                    for (Tc, z) in list(S)[:4]:
                        Tz = tuple(sorted(idx[(zeta * H[i]) % q] for i in Tc))
                        if (Tz, (pow(zeta, j, q) * z) % q) in S:
                            bad += 1
                L.chk(bad == 0, "action is EXACTLY mu_g (no larger)",
                      (n, k, w, M, q, j, bad))
            mu_g = g // math.gcd(j, g)
            zc = set(E.coset_rep(z, mu, q) for (_, z) in S)
            Ej = len(zc)
            zs = set(z for (_, z) in S)
            # F-D : the z-set is a union of mu_{g'}-cosets, so |z-set| >= g'.E_j
            mugp = sorted(set(pow(t, n // mu_g, q) for t in mu))
            inv_ok = all(((t * z) % q) in zs for z in zs for t in mugp)
            L.chk(inv_ok, "F-D z-set is mu_{g'}-invariant",
                  (n, k, w, M, q, j, mu_g))
            L.chk(len(zs) >= mu_g * Ej, "F-D |Z| >= g'.E_j",
                  (n, k, w, M, q, j, len(zs), mu_g * Ej))
            L.chk(len(zs) <= n * Ej, "THEOREM D |Z| <= n.E_j",
                  (n, k, w, M, q, j, len(zs), n * Ej))
            rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                         "r": r, "g": g, "g_prime": mu_g, "N": n // M,
                         "E_j": Ej, "nz": len(zs), "n_sols": len(S),
                         "ratio_nz_over_Ej": len(zs) / Ej})
            print("n=%2d k=%2d w=%d M=%d q=%4d j=%d | r=%2d g=%2d g'=%2d "
                  "| E_j=%d |Z|=%3d  g'E_j=%3d <= |Z| <= nE_j=%3d" %
                  (n, k, w, M, q, j, r, g, mu_g, Ej, len(zs), mu_g * Ej, n * Ej))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "x2_action.json"), "w") as f:
    json.dump({"doc": __doc__, "prize": prize, "rows": rows,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
if rows:
    print("\ntightness of the sandwich g'E_j <= |Z| <= nE_j:")
    print("  min |Z|/(g'E_j) = %.3f   max |Z|/(n E_j) = %.3f" % (
        min(r["nz"] / (r["g_prime"] * r["E_j"]) for r in rows),
        max(r["nz"] / (r["n"] * r["E_j"]) for r in rows)))
ok = L.report("x2_action")
print("OK" if ok else "FAILURES PRESENT")

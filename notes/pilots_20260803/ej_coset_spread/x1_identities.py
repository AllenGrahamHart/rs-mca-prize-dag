"""x1_identities.py -- falsifiers F-A, F-B, F-J.

(1) My reformulation (Q3),(Q5),(Q6),(Q8) of admissibility is EQUIVALENT to the
    banked window system (g2lib.classify_lean) at every j < w:  exact set
    equality of the solution sets, with matching z.                    [F-A]
(2) Every solution satisfies the identity ledger (Q1)-(Q10).           [F-A]
(3) E_j = #{ mu_n-coset classes of z over admissible (T,z) }, EXACTLY. [F-B]
(4) Against the theory-free Scan where affordable: Gamma_j (exact-A live
    slopes) has |Gamma_j| <= n E_j and #(Gamma_j / mu_n) = E_j.    [F-B, F-J]
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

# (n, k, w, M, [q...], scan?)   -- all prize shape (w = M) except where noted
FIX = [
    (12, 3, 3, 3, [13, 37], True),
    (15, 3, 3, 3, [31, 61], True),
    (18, 3, 3, 3, [19, 37], True),
    (21, 3, 3, 3, [43, 127], True),
    (12, 4, 4, 4, [13, 37], True),
    (16, 4, 4, 4, [17, 97], True),
    (20, 4, 4, 4, [41, 101], True),
    (16, 8, 4, 4, [17, 97], True),
    (18, 6, 6, 6, [19, 37], True),
    (20, 5, 5, 5, [41, 101], True),
    (21, 7, 7, 7, [43], False),
    (21, 4, 3, 7, [43, 127], True),        # w < M, j < w for j = 1,2
    (20, 5, 3, 4, [41, 101], True),        # w < M
    (18, 5, 3, 6, [37, 73], True),         # w < M
]

rows = []
for (n, k, w, M, qs, do_scan) in FIX:
    A = k + w + 1
    rp = n - A
    r = n - k - w
    if not E.mc3_ok(n, k, w, M):
        print("skip MC-3", (n, k, w, M))
        continue
    js = [j for j in range(1, min(M, w))]        # j < w AND j <= M-1
    if not js:
        continue
    for q in qs:
        if (q - 1) % n or not E.is_prime(q) or q <= n + 1:
            continue
        H, beta, om = E.make_domain(q, n, 0)
        mu = E.mu_n_set(H, q)
        c = E.mc_c_from_gamma(H, q, n, k, w, M)
        gam = ((-1) ** rp * c) % q
        fam = E.mc_family(H, q, n, k, w, M, c)
        if not fam:
            print("empty MC family", (n, k, w, M, q))
            continue
        banked = E.G.classify_lean(H, q, n, k, w, c, js)   # third opinion
        for j in js:
            mine = E.admissible_mine(H, q, n, k, w, c, j)
            b = banked[j]
            sm = set((tuple(s["Tidx"]), s["z"]) for s in mine)
            sb = set((tuple(s["Tidx"]), s["z"]) for s in b)
            L.chk(sm == sb, "F-A equivalence of classifiers",
                  (n, k, w, M, q, j, len(sm), len(sb)))

            IT = E.inv_table(q)
            for s in mine:
                T = [H[i] for i in s["Tidx"]]
                eT, eTi, pr, z = s["eT"], s["eTi"], s["prod"], s["z"]
                lam = eT[j]
                # (Q1)
                L.chk(z == (pow(-1, j + 1) * IT[eTi[j]]) % q, "Q1", (n, q, j))
                # (Q2) THEOREM C
                L.chk(z == (pow(-1, j) * gam * IT[(pr * eTi[j - 1]) % q]) % q,
                      "Q2", (n, q, j))
                # (Q4)
                L.chk(lam == (pow(-1, j + 1) * z) % q, "Q4", (n, q, j))
                # (Q5)
                L.chk(lam * eTi[j] % q == 1, "Q5", (n, q, j))
                # (Q7)
                L.chk(eT[j - 1] * eTi[j - 1] % q == 1, "Q7", (n, q, j))
                # (Q8)
                L.chk((-pr * eTi[j - 1] * lam) % q == gam, "Q8", (n, q, j))
                # (Q3)/(Q9): (1+zY^j) E_T = G mod Y^w, deg G <= j-1
                ET = [(pow(-1, t) * eT[t]) % q for t in range(w)]
                Gc = [(ET[t] + (z * ET[t - j] if t >= j else 0)) % q
                      for t in range(w)]
                L.chk(all(Gc[t] == 0 for t in range(j, w)), "Q9 deg G",
                      (n, q, j, Gc))
                L.chk(Gc[0] == 1, "Q9 G(0)=1", (n, q, j))
                # (Q6): E_{T^-1} = (-1)^{j-1} e_{j-1}(T^-1) . reversal(G) mod Y^j
                kap = (pow(-1, j - 1) * eTi[j - 1]) % q
                for rho in range(j):
                    lhs = (pow(-1, rho) * eTi[rho]) % q
                    L.chk(lhs == kap * Gc[j - 1 - rho] % q, "Q6", (n, q, j, rho))
                # (Q10): E_C . G = 1 + z Y^j mod Y^w,  C = H \ T
                Cset = [H[i] for i in range(n) if i not in set(s["Tidx"])]
                eC = E.esym(Cset, q, w - 1)
                EC = [(pow(-1, t) * eC[t]) % q for t in range(w)]
                for t in range(w):
                    acc = 0
                    for a in range(t + 1):
                        acc += EC[a] * Gc[t - a]
                    tgt = (1 if t == 0 else 0) + (z if t == j else 0)
                    L.chk(acc % q == tgt % q, "Q10", (n, q, j, t))

            Ej = E.Ej_from_sols(mine, mu, q, "ejm1_inv")
            zc = E.zcosets(mine, mu, q)
            L.chk(Ej == len(zc), "F-B  E_j == #z-cosets",
                  (n, k, w, M, q, j, Ej, len(zc)))

            # structured accounting
            structs, _ = E.structured_sets(H, q, n, k, w, M, c)
            nstruct = sum(1 for s in mine if frozenset(s["Tidx"]) in structs)
            L.chk(nstruct == len(structs), "F-L every structured T admissible",
                  (n, k, w, M, q, j, nstruct, len(structs)))
            nHj = E.neg_Hj(H, q, j)
            struct_z_ok = all(s["z"] in nHj for s in mine
                              if frozenset(s["Tidx"]) in structs)
            L.chk(struct_z_ok, "THEOREM E structured z in -H^j",
                  (n, k, w, M, q, j))

            row = {"n": n, "k": k, "w": w, "M": M, "q": q, "j": j, "A": A,
                   "rp": rp, "r": r, "gcd_j_n": math.gcd(j, n),
                   "X": E.comb(n, A) / pow(q, w),
                   "n_sols": len(mine), "n_struct": len(structs),
                   "n_sporadic": len(mine) - nstruct, "E_j": Ej,
                   "n_zcosets": len(zc), "prize_shape": (w == M)}

            if do_scan and E.comb(n, k) <= 30000:
                uv, vv = E.pencil_words(H, q, n, k, w, c, j)
                sc = E.Scan(H, q, k, uv, vv, A)
                gamm = set(z for z in sc.live() if z != E.INF and z != 0)
                gate = sc.gate_ok()
                L.chk(len(gamm) <= n * Ej, "F-J |Gamma_j| <= n E_j",
                      (n, k, w, M, q, j, len(gamm), n * Ej))
                gcos = set(E.coset_rep(z, mu, q) for z in gamm)
                # AMENDMENT (A1): equality only under an intact gate; the
                # inclusion is unconditional.
                L.chk(gcos <= zc, "F-B(uncond) Gamma cosets subset z-cosets",
                      (n, k, w, M, q, j, len(gcos), len(zc)))
                if gate:
                    L.chk(gcos == zc, "F-B Gamma cosets == z-cosets (gate ok)",
                          (n, k, w, M, q, j, len(gcos), len(zc)))
                row["spor_gate_law"] = ((row["n_sporadic"] > 0) == (not gate))
                row.update({"gate_ok": gate, "Gamma": len(gamm),
                            "Gamma_cosets": len(gcos),
                            "joint_max": sc.joint_max})
            rows.append(row)
            print("n=%2d k=%2d w=%d M=%d q=%4d j=%d | sols=%5d (str %4d spor %3d)"
                  " E_j=%d zc=%d %s" %
                  (n, k, w, M, q, j, len(mine), nstruct,
                   len(mine) - nstruct, Ej, len(zc),
                   ("|G|=%d gate=%s" % (row["Gamma"], row["gate_ok"]))
                   if "Gamma" in row else ""))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "x1_identities.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows, "checks": L.n,
               "failures": len(L.fail)}, f, indent=1)
ok = L.report("x1_identities")
print("rows:", len(rows), " max E_j =", max(r["E_j"] for r in rows))
print("OK" if ok else "FAILURES PRESENT")

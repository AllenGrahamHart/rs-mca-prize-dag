"""e2_replay18.py -- MANDATORY replay of the 18 banked gate-intact
counterexamples (adv_gamma_minus_h/checkpoints/t2_hunt.json) through:

  F7(i)  every one must have X = C(n,A)/q^w  >= 1
         (if any has X < 1 the conditional theorem is DEAD ON ARRIVAL)
  F7(ii) every one must satisfy |Gamma| <= n . E_j   (kills P4 if violated)
  D7     every one must have j >= w  (equivalently w < M), i.e. NONE of
         them lives in the prize-row shape w = M

Recomputed from scratch here (own domain, own classifier, own Scan).
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

BANK = os.path.join(os.path.dirname(os.path.dirname(HERE)), "pilots_20260802",
                    "adv_gamma_minus_h", "checkpoints", "t2_hunt.json")
ce = json.load(open(BANK))["counterexamples"]
print("banked counterexamples:", len(ce))

L = G.Ledger()
rows = []
for e in ce:
    n, k, w, M, q, j, be = e["n"], e["k"], e["w"], e["M"], e["q"], e["j"], e["beta_exp"]
    A = k + w + 1
    rp = n - A
    H, beta, om = G.make_domain(q, n, be)
    mu = G.mu_n_set(H, q)
    c = G.mc_c_from_gamma(H, q, n, k, w, M)
    uv, vv = G.pencil_words(H, q, n, k, w, c, j)
    sc = G.Scan(H, q, k, uv, vv, A)
    sols = G.classify(H, q, n, k, w, c, j)
    gam = set(z for z in sc.live() if z != G.INF and z != 0)
    classes = set()
    for s in sols:
        inv = [pow(x, q - 2, q) for x in s["T"]]
        classes.add(G.coset_rep(G.esym(inv, q, j - 1)[j - 1], mu, q))
    Ej = len(classes)
    cnA, qw = G.X_index(n, A, q, w)
    Xge1 = cnA >= qw

    # F7(i)
    L.chk(Xge1, "F7(i) counterexample has X >= 1",
          (n, k, w, M, q, j, be, cnA / qw))
    # F7(ii)
    L.chk(len(gam) <= n * Ej, "F7(ii) |Gamma| <= n.E_j",
          (n, k, w, M, q, j, be, len(gam), Ej))
    # D7
    L.chk(w < M, "D7 counterexample has w < M (not prize-row shape)",
          (n, k, w, M, j))
    L.chk(j >= w, "D7' counterexample has j >= w", (n, k, w, M, j))
    # reproduce the banked |Gamma| and outside-count
    L.chk(len(gam) == e["n_live"], "replay reproduces banked |Gamma|",
          (len(gam), e["n_live"]))
    nHj = G.neg_Hj(H, q, j)
    L.chk(len([z for z in gam if z not in nHj]) == e["n_live_outside_minusHj"],
          "replay reproduces banked outside-count")
    L.chk(sc.gate_ok(), "replay confirms gate intact")

    rows.append({
        "n": n, "k": k, "w": w, "M": M, "q": q, "j": j, "beta_exp": be,
        "A": A, "gcd_j_n": math.gcd(j, n),
        "prize_shape_w_eq_M": (w == M), "j_ge_w": (j >= w), "w_lt_M": (w < M),
        "Gamma": len(gam), "Gamma_over_n": round(len(gam) / n, 3),
        "E_j": Ej, "n_E_j": n * Ej, "bound_tight": (len(gam) == n * Ej),
        "X": cnA / qw, "X_ge_1": Xge1,
        "outside_negHj": len([z for z in gam if z not in nHj]),
        "gate_ok": sc.gate_ok(),
    })
    print("n=%2d k=%2d w=%d M=%d q=%4d j=%d b=%d | w<M %-5s j>=w %-5s | "
          "|G|=%3d (%.2fn) E_j=%d n.E_j=%3d %s | X=%9.3g %s" %
          (n, k, w, M, q, j, be, w < M, j >= w, len(gam), len(gam) / n, Ej,
           n * Ej, "TIGHT" if len(gam) == n * Ej else "     ",
           cnA / qw, "X>=1" if Xge1 else "*** X<1 ***"))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "e2_replay18.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows,
               "checks": L.n, "failures": len(L.fail),
               "min_X": min(r["X"] for r in rows),
               "max_E_j": max(r["E_j"] for r in rows),
               "any_prize_shape": any(r["prize_shape_w_eq_M"] for r in rows),
               "all_j_ge_w": all(r["j_ge_w"] for r in rows)}, f, indent=1)
print("\nmin X over the 18 = %.4g   max E_j = %d   any prize-shape = %s" %
      (min(r["X"] for r in rows), max(r["E_j"] for r in rows),
       any(r["prize_shape_w_eq_M"] for r in rows)))
ok = L.report("e2_replay18")
print("OK" if ok else "FAILURES PRESENT")

"""e4_prizeshape.py -- FALSIFIER F9 and the (H-A) vs (H-B) discriminator.

Every one of the 18 banked counterexamples has w < M and j >= w.  At the
prize rows w = M = h-1, so j <= M-1 = w-1 < w ALWAYS.  Two hypotheses:

  (H-A)  the excess is governed by X < 1 alone; the prize-row shape merely
         happens to have small X (w = M large  =>  q^w large  =>  X small).
  (H-B)  the prize-row shape j < w structurally forbids the excess,
         regardless of X.

They are separated by prize-shape fixtures with X > 1.  Those need w = M
SMALL and q small, i.e. M = 3 with n odd (gcd(j,n)=1 needs j odd when n is
even, and j <= M-1 then forces M >= 4, which drives X down).  n = 21,
M = w = 3, q = 43, j = 2 is the sweet spot: X = 1.46 / 4.44 / 2.56.

F9 fires iff some gate-intact PRIZE-SHAPE fixture has |Gamma_j| > n.
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
CFG = [
    (21, 3, [3, 6], [43, 127]),        # 0  X = 1.46 / 4.44 at q=43  <== KEY
    (18, 3, [3, 6], [19, 37]),         # 1  X = 4.64 / 6.38 at q=19  <== KEY
    (15, 3, [3, 6], [31, 61]),         # 2
    (12, 3, [3, 6], [13, 37]),         # 3
    (12, 4, [4], [13, 37]),            # 4
    (16, 4, [4, 8], [17, 97]),         # 5
    (20, 4, [4], [41, 101]),           # 6
    (15, 5, [5], [31, 61]),            # 7
    (18, 6, [6], [19, 37]),            # 8
    (20, 5, [5], [41]),                # 9
    (24, 3, [3], [73]),                # 10
    (21, 7, [7], [43]),                # 11 j up to 6 (needs its own batch)
    (24, 4, [4], [73]),                # 12
]
SCAN_CAP = int(os.environ.get("SCAN_CAP", "60000"))
CLS_CAP = int(os.environ.get("CLS_CAP", "400000"))

JSEL = set(int(t) for t in os.environ["JSEL"].split(",")) if os.environ.get("JSEL") else None
SEL = sys.argv[1] if len(sys.argv) > 1 else "all"
TAG = sys.argv[2] if len(sys.argv) > 2 else SEL
if SEL != "all":
    CFG = [CFG[i] for i in [int(t) for t in SEL.split(",")]]

rows, fired = [], []
for (n, M, ks, qs) in CFG:
    w = M                                   # PRIZE-ROW SHAPE: w = M
    if n % M:
        continue
    for k in ks:
        r = n - k - w
        A = k + w + 1
        rp = n - A
        if r < M or r % M or rp < 1 or A > n:
            continue
        if G.comb(n, k) > SCAN_CAP or G.comb(n, rp) > CLS_CAP:
            print("skip cost", (n, k, w, M), G.comb(n, k), G.comb(n, rp))
            continue
        js = [j for j in range(1, M)]
        if JSEL:
            js = [j for j in js if j in JSEL]
        if not js:
            continue
        cnA = G.comb(n, A)
        for q in qs:
            if (q - 1) % n or not G.is_prime(q) or q <= n + 1:
                continue
            H, beta, om = G.make_domain(q, n, 0)
            mu = G.mu_n_set(H, q)
            c = G.mc_c_from_gamma(H, q, n, k, w, M)
            fam = G.mc_family(H, q, n, k, w, M, c)
            if not fam:
                continue
            X = cnA / pow(q, w)
            allsol = G.classify_multi(H, q, n, k, w, c, js)
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
                gate = sc.gate_ok()
                nHj = G.neg_Hj(H, q, j)
                outside = len([z for z in gam if z not in nHj])
                L.chk(len(gam) <= n * Ej, "(P4) |Gamma| <= n.E_j", (n, k, q, j))
                f9 = gate and len(gam) > n
                if f9:
                    fired.append((n, k, w, M, q, j, len(gam), X))
                rows.append({
                    "n": n, "k": k, "w": w, "M": M, "q": q, "j": j,
                    "A": A, "gcd_j_n": math.gcd(j, n), "X": X,
                    "X_ge_1": X >= 1, "gate_ok": gate,
                    "joint_max": sc.joint_max, "Gamma": len(gam),
                    "Gamma_over_n": round(len(gam) / n, 3), "E_j": Ej,
                    "outside_negHj": outside, "n_sols": len(sols),
                    "mc_family": len(fam), "F9_fired": f9})
                print("n=%2d k=%2d w=M=%d q=%4d j=%d g=%d | X=%9.3g %-5s "
                      "gate=%-5s | |G|=%3d (%.2fn) E_j=%d out=%2d %s" %
                      (n, k, w, q, j, math.gcd(j, n), X,
                       "X>=1" if X >= 1 else "X<1", gate, len(gam),
                       len(gam) / n, Ej, outside,
                       "*** F9 FIRED ***" if f9 else ""))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints",
                       "e4_prizeshape_%s.json" % TAG), "w") as f:
    json.dump({"doc": __doc__, "rows": rows, "F9_fired": fired,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)

sup = [r for r in rows if r["X_ge_1"] and r["gate_ok"]]
cop = [r for r in rows if r["gate_ok"] and r["gcd_j_n"] == 1 and r["j"] >= 2]
print("\nF9 fired on %d fixtures" % len(fired))
print("prize-shape gate-intact rows: %d ; with X >= 1: %d" % (
    len([r for r in rows if r["gate_ok"]]), len(sup)))
if sup:
    print("  among X>=1 prize-shape: max |Gamma|/n = %.3f, max E_j = %d, "
          "max X = %.3g" % (max(r["Gamma_over_n"] for r in sup),
                            max(r["E_j"] for r in sup),
                            max(r["X"] for r in sup)))
if cop:
    print("  among gcd(j,n)=1, j>=2: max |Gamma|/n = %.3f, max E_j = %d" %
          (max(r["Gamma_over_n"] for r in cop), max(r["E_j"] for r in cop)))
ok = L.report("e4_prizeshape")
print("OK" if ok else "FAILURES PRESENT")

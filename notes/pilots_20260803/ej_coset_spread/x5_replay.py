"""x5_replay.py -- MANDATORY REPLAY + the toy-scale wall.

(1) Replay EVERY banked row of the gamma_j2_close pilot (179 rows across 10
    checkpoints) plus every row this pilot produced, through:
      THEOREM D   |Gamma_j| <= n . E_j                            [F-J]
      THEOREM G   |Gamma_j| >= g' . E_j,  g' = g/gcd(j,g), g = gcd(n-k-w, n)
      F-I         E_j <= 29.6 n
      F-K         gate-intact, prize shape (w=M), j<w, gcd(j,n)=1  =>  E_j = 1
(2) The toy-scale wall (PREREG D-7), computed exactly over the whole reachable
    grid: is there ANY fixture with X = C(n,A)/q^w >= 1, w >= 2j+1 (j >= 2), and
    C(n,A) <= B (the enumeration budget)?  Reported as a function of B.
"""
import glob
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ejlib as E                                                # noqa: E402

L = E.Ledger()
GAMMA_CP = os.path.join(os.path.dirname(HERE), "gamma_j2_close", "checkpoints")

allrows = []
for pat, tag in ((os.path.join(GAMMA_CP, "*.json"), "gamma"),
                 (os.path.join(HERE, "checkpoints", "*.json"), "ej")):
    for p in sorted(glob.glob(pat)):
        base = os.path.basename(p)
        if base.startswith("x5_"):
            continue
        d = json.load(open(p))
        for r in d.get("rows", []):
            if "E_j" not in r or "n" not in r:
                continue
            r = dict(r)
            r["_src"] = tag + "/" + base
            allrows.append(r)

print("replaying %d rows carrying an E_j (gamma pilot + this pilot)"
      % len(allrows))

nD = nG = nI = nK = 0
viol = []
for r in allrows:
    n, k, j, Ej = r["n"], r["k"], r["j"], r["E_j"]
    w = r.get("w")
    M = r.get("M")
    if w is None:
        continue
    rr = n - k - w
    g = E.gcd(rr, n)
    gp = g // math.gcd(j, g)
    r["g"], r["g_prime"] = g, gp
    if not L.chk(Ej <= 29.6 * n, "F-I E_j <= 29.6n", (r["_src"], n, k, w, j)):
        viol.append(("F-I", r))
    nI += 1
    if "Gamma" in r:
        G_ = r["Gamma"]
        if not L.chk(G_ <= n * Ej, "F-J THEOREM D |Gamma| <= n.E_j",
                     (r["_src"], n, k, w, j, G_, n * Ej)):
            viol.append(("F-J", r))
        nD += 1
        # THEOREM G lower bound applies to Gamma as a set of live slopes; it is
        # vacuous when the gate is broken (Gamma is then empty by definition).
        if r.get("gate_ok", True) and G_ > 0:
            if not L.chk(G_ >= gp * Ej, "THEOREM G |Gamma| >= g'.E_j",
                         (r["_src"], n, k, w, j, G_, gp * Ej)):
                viol.append(("G", r))
            nG += 1
    if (r.get("gate_ok") is True and M is not None and w == M and j < w
            and math.gcd(j, n) == 1):
        if not L.chk(Ej == 1, "F-K prize-shape gate-intact law",
                     (r["_src"], n, k, w, M, r.get("q"), j, Ej)):
            viol.append(("F-K", r))
        nK += 1

print("  F-I checked on %d rows, THEOREM D on %d, THEOREM G on %d, "
      "F-K on %d" % (nI, nD, nG, nK))
print("  max E_j over all replayed rows = %d" % max(r["E_j"] for r in allrows))
gi = [r for r in allrows if r.get("gate_ok") is True]
print("  max E_j over gate-intact rows  = %d" % max([r["E_j"] for r in gi] + [0]))
jlw = [r for r in allrows if r.get("w") and r["j"] < r["w"]]
print("  max E_j over j < w rows        = %d" % max([r["E_j"] for r in jlw] + [0]))
jlw_gi = [r for r in jlw if r.get("gate_ok") is True]
print("  max E_j over j < w AND gate-intact rows = %d  (%d rows)"
      % (max([r["E_j"] for r in jlw_gi] + [0]), len(jlw_gi)))

# --------------------------------------------------------- the toy-scale wall
print("\n--- PREREG D-7: the toy-scale wall, exact over the reachable grid ---")
wall = []
for B_exp in (6, 7, 8, 10, 12):
    B = 10 ** B_exp
    best = None
    hits = []
    for n in range(6, 61):
        for M in range(2, n + 1):
            if n % M:
                continue
            for w in range(2, M + 1):
                for k in range(1, n):
                    r_ = n - k - w
                    A = k + w + 1
                    if r_ <= 0 or r_ % M or r_ < M or n - A < 1:
                        continue
                    cnA = E.comb(n, A)
                    if cnA > B:
                        continue
                    q = n + 1
                    while True:
                        q += 1
                        if q % n == 1 and E.is_prime(q) and q > n + 1:
                            break
                    X = cnA / pow(q, w)
                    if X >= 1:
                        if best is None or w > best[0]:
                            best = (w, n, k, M, q, X, cnA)
                        if w >= 5:
                            hits.append((n, k, w, M, q, X))
    wall.append({"budget": B, "max_w_with_X_ge_1": (best[0] if best else None),
                 "witness": best, "w_ge_5_hits": len(hits)})
    print("  budget C(n,A) <= 1e%-2d : max w with X >= 1 is %s  (witness "
          "n=%s k=%s M=%s q=%s X=%.3g) ; fixtures with X>=1 AND w>=5 : %d"
          % (B_exp, best[0] if best else "-", best[1] if best else "-",
             best[2] if best else "-", best[3] if best else "-",
             best[4] if best else "-", best[5] if best else 0, len(hits)))
    # D-7 was registered as "incompatible at any ENUMERABLE scale".  Python
    # enumeration tops out near 5e6; 1e10 / 1e12 are hypothetical budgets and
    # are reported, not asserted.  The assertion is made only where the pilot
    # can actually enumerate.
    if B <= 10 ** 8:
        L.chk(len(hits) == 0,
              "D-7 wall: no X>=1 fixture with w>=5 under an ENUMERABLE budget",
              (B_exp, len(hits)))

cross = next((wl for wl in wall if wl["w_ge_5_hits"] > 0), None)
print("\n  D-7 VERDICT (corrected): the wall is a BUDGET wall, not a structural")
print("  one.  X >= 1 needs C(n,A) >= q^w >= (2n+1)^w while C(n,A) <= 2^n, so")
print("  w <= n/log2(2n+1); w >= 5 therefore needs n >= 5.log2(2n+1), i.e.")
print("  n >= 30 -- reachable in PRINCIPLE, just not by Python enumeration.")
if cross:
    print("  CROSSOVER: the first budget admitting X>=1 AND w>=5 is %g"
          % cross["budget"])
    print("  It is ~2000x beyond this pilot's ~5e6 enumeration budget, so a")
    print("  compiled or meet-in-the-middle search COULD test route (2)")
    print("  against a live excess.  Named target fixture for that run:")
    print("    n=35, k=10, w=M=5, q=71, A=16, C(n,A)=%d, X=2.25, j=2 (D=w-2j=1)"
          % E.comb(35, 16))
print("  => within THIS pilot, route (2) could not be tested against a live")
print("     excess; it was tested exhaustively on the band family instead.")

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "x5_replay.json"), "w") as f:
    json.dump({"doc": __doc__, "n_rows_replayed": len(allrows),
               "checked": {"F_I": nI, "THEOREM_D": nD, "THEOREM_G": nG,
                           "F_K": nK},
               "violations": len(viol), "wall": wall,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)
ok = L.report("x5_replay")
print("OK" if ok else "FAILURES PRESENT")

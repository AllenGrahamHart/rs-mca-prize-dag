"""e5_structure.py -- the MECHANISM, plus falsifiers F4 / F5 (rigidity).

Decompose the admissible set into STRUCTURED (T u {y} is an MC coset union,
which by (P5) forces z = -y^j in -H^j) and SPORADIC (everything else, which
is what creates E_j >= 2).  For every sporadic T measure

    d(T) := min over structured T' of |T \\ T'|

and test the pre-registered rigidity dichotomy (P6):

  F4 fires: two admissible T, T' with 2j-1 < d <= w-2j
  F5 fires: an admissible T and a STRUCTURED T' with 1 < d <= w-2j

Run on both shapes: the prize shape (w = M, j < w) and the banked shape
(w < M, j >= w) where the 18 counterexamples live.
"""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2lib as G                                              # noqa: E402

L = G.Ledger()
FIX = [
    # n, k, w, M, q, beta, [j...]
    (20, 6, 2, 4, 41, 0, [1, 3]),        # banked shape, EXCESS (E_j=2)
    (20, 6, 2, 4, 101, 0, [1, 3]),       # banked shape, EXCESS (E_j=4)
    (20, 6, 2, 4, 401, 0, [3]),          # banked shape, X=1.045, EXCESS
    (20, 6, 2, 4, 421, 0, [3]),          # banked shape, X=0.948, clean
    (21, 5, 2, 7, 43, 0, [2, 5]),        # banked shape, EXCESS
    (21, 3, 3, 3, 43, 0, [1, 2]),        # PRIZE shape, X=1.46
    (21, 6, 3, 3, 43, 0, [1, 2]),        # PRIZE shape, X=4.44
    (16, 4, 4, 4, 17, 0, [1, 3]),        # PRIZE shape
    (20, 4, 4, 4, 41, 0, [1, 3]),        # PRIZE shape
    (18, 6, 6, 6, 37, 0, [1, 5]),        # PRIZE shape
    (15, 5, 5, 5, 31, 0, [2, 4]),        # PRIZE shape
]

rows = []
for (n, k, w, M, q, be, js) in FIX:
    A = k + w + 1
    rp = n - A
    H, beta, om = G.make_domain(q, n, be)
    mu = G.mu_n_set(H, q)
    c = G.mc_c_from_gamma(H, q, n, k, w, M)
    fam = [set(t) for t in G.mc_family(H, q, n, k, w, M, c)]
    allsol = G.classify_multi(H, q, n, k, w, c, js)
    X = G.comb(n, A) / pow(q, w)
    for j in js:
        sols = allsol[j]
        struct, spor = [], []
        for s in sols:
            Ts = set(s["Tidx"])
            hit = None
            for F in fam:
                if Ts < F and len(F - Ts) == 1:
                    hit = F
                    break
            (struct if hit else spor).append(s)
        # distances from every sporadic solution to the structured ones
        dmin, dhist = None, {}
        for s in spor:
            Ts = set(s["Tidx"])
            d = min([len(Ts - set(t["Tidx"])) for t in struct] or [999])
            dhist[d] = dhist.get(d, 0) + 1
            dmin = d if dmin is None else min(dmin, d)
            # F5: vs a STRUCTURED T', d <= w-2j must force d <= 1
            if d <= w - 2 * j:
                L.chk(d <= 1, "F5 rigidity vs structured: d<=w-2j => d<=1",
                      (n, k, w, M, q, j, d))
        # F4: pairwise dichotomy  d <= 2j-1  or  d >= w-2j+1
        allT = [set(s["Tidx"]) for s in sols]
        checked = 0
        for a in range(min(len(allT), 60)):
            for b in range(a + 1, min(len(allT), 60)):
                d = len(allT[a] - allT[b])
                if d and d <= w - 2 * j:
                    checked += 1
                    L.chk(d <= 2 * j - 1,
                          "F4 dichotomy: d<=w-2j => d<=2j-1",
                          (n, k, w, M, q, j, d))
        classes = set()
        for s in sols:
            inv = [pow(x, q - 2, q) for x in s["T"]]
            classes.add(G.coset_rep(G.esym(inv, q, j - 1)[j - 1], mu, q))
        rows.append({"n": n, "k": k, "w": w, "M": M, "q": q, "beta": be,
                     "j": j, "X": X, "prize_shape": (w == M), "j_lt_w": j < w,
                     "n_sols": len(sols), "n_structured": len(struct),
                     "n_sporadic": len(spor), "E_j": len(classes),
                     "sporadic_dmin": dmin, "d_histogram": dhist,
                     "pairs_in_dichotomy_range": checked})
        print("n=%2d k=%2d w=%d M=%d q=%4d j=%d %-6s | X=%8.3g | sols=%4d "
              "struct=%3d SPORADIC=%4d E_j=%d | d_min=%s d_hist=%s" %
              (n, k, w, M, q, j, "PRIZE" if w == M else "w<M", X, len(sols),
               len(struct), len(spor), len(classes), dmin,
               dict(sorted(dhist.items())) if dhist else {}))

os.makedirs(os.path.join(HERE, "checkpoints"), exist_ok=True)
with open(os.path.join(HERE, "checkpoints", "e5_structure.json"), "w") as f:
    json.dump({"doc": __doc__, "rows": rows,
               "checks": L.n, "failures": len(L.fail)}, f, indent=1)

pz = [r for r in rows if r["prize_shape"]]
bk = [r for r in rows if not r["prize_shape"]]
print("\nPRIZE shape (w=M, j<w): %d rows, total sporadic = %d, max E_j = %d"
      % (len(pz), sum(r["n_sporadic"] for r in pz), max(r["E_j"] for r in pz)))
print("banked shape (w<M):      %d rows, total sporadic = %d, max E_j = %d"
      % (len(bk), sum(r["n_sporadic"] for r in bk), max(r["E_j"] for r in bk)))
ok = L.report("e5_structure")
print("OK" if ok else "FAILURES PRESENT")

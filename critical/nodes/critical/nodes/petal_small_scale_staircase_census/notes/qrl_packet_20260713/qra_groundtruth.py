#!/usr/bin/env python3
"""qra_groundtruth: from-scratch recomputation of the banked census records at
the exhaustively checkable p = 17 points, with INDEPENDENT enumeration,
stabilizer, classification and profile logic (only the word construction is
imported -- it is the definition of the record). Plus an independent
interleaving-descent check at (8,4,17).

States: max 17^4 = 83,521 polynomials per word (RAM law compliant)."""
import itertools
import json
import sys
from math import comb

from cg_petal_census import order_n_domain, build_word  # definitional only

FAIL = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAIL.append(label)

def cap(npr):
    return 63 * npr**6 // 64

# ---------------------------------------------------------------- my own kit
def my_ev(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v

def my_stab(S, n):
    """|{d in Z_n : S + d = S}| -- the FULL stabilizer subgroup order."""
    c = 0
    for d in range(n):
        if all(((x + d) % n) in S for x in S):
            c += 1
    return c

def my_contributors(n, k, p, dom, values):
    """ALL deg<k codewords with agreement >= k+1, by full enumeration."""
    found = {}
    for coeffs in itertools.product(range(p), repeat=k):
        S = frozenset(j for j in range(n)
                      if my_ev(coeffs, dom[j], p) == values[j])
        if len(S) >= k + 1:
            found[coeffs] = S
    return found

def my_tables(n, k, petals, contr):
    t = len(petals)
    psets = [frozenset(P) for P in petals]
    classes = {}
    for poly, S in contr.items():
        c = my_stab(S, n)
        assert c & (c - 1) == 0, "stabilizer order not a 2-power"
        if not (2 <= c <= t):
            continue
        e = classes.setdefault(S, dict(c=c, A=len(S), polys=0))
        e["polys"] += 1
        e["fp"] = all((S & P) in (frozenset(), P) for P in psets)
    allow = n**6 // comb(n + 6, 6)
    out = {}
    for fp in (0, 1):
        for bd in ("edge", "own", "all"):
            tab = {}
            for S, e in classes.items():
                if fp and not e["fp"]:
                    continue
                if bd == "edge" and e["A"] != k + 1:
                    continue
                if bd == "own" and e["A"] > k + 1 + e["c"] - 1:
                    continue
                cell = tab.setdefault((e["c"], e["A"]), [0, 0])
                cell[0] += 1
                cell[1] += e["polys"]
            fin = {}
            for (M, A), (cl, cw) in tab.items():
                h = A // M
                Q = comb(n // M - 1, h) if h <= n // M - 1 else 0
                fin[f"{M},{A}"] = dict(classes=cl, codewords=cw, Q=Q,
                                       B719=719 * Q, Bscaled=allow * Q,
                                       excess719=cl > 719 * Q)
            out[(fp, bd)] = fin
    nper = sum(1 for S in contr.values() if my_stab(S, n) >= 2)
    return classes, out, nper

# ------------------------------------------- 1: replay all p=17 records
print("== 1: from-scratch replay of ALL banked p=17 records")
gt = json.load(open("cg_petal_census_results.json"))
recs17 = [r for r in gt if r["p"] == 17]
print(f"   banked p=17 records: {len(recs17)} "
      f"(shapes {sorted({(r['n'], r['k']) for r in recs17})})")
ok_all = True
n_tabs = 0
for rec in recs17:
    n, k, p = rec["n"], rec["k"], 17
    dom = order_n_domain(p, n)
    values, core, petals, bg, scal = build_word(
        n, k, p, dom, rec["layout"], rec["scalars"], rec["seed"])
    contr = my_contributors(n, k, p, dom, values)
    classes, tabs, nper = my_tables(n, k, petals, contr)
    if nper != rec["n_periodic_contributors"]:
        ok_all = False
        print(f"   MISMATCH n_periodic: {nper} vs {rec['n_periodic_contributors']}"
              f" at {rec['layout']}/{rec['scalars']}")
    if len(classes) != rec["n_smallscale_classes"]:
        ok_all = False
        print(f"   MISMATCH n_classes at {rec['layout']}/{rec['scalars']}")
    for fp in (0, 1):
        for bd in ("edge", "own", "all"):
            mine = tabs[(fp, bd)]
            theirs = rec[f"fp{fp}_{bd}"]
            n_tabs += 1
            keysm = set(mine)
            keyst = set(theirs)
            if keysm != keyst:
                ok_all = False
                print(f"   CELL-SET MISMATCH fp{fp}_{bd} {rec['layout']}/"
                      f"{rec['scalars']}: {keysm} vs {keyst}")
                continue
            for key in mine:
                m, t_ = mine[key], theirs[key]
                if any(m[f] != t_[f] for f in
                       ("classes", "codewords", "Q", "B719", "Bscaled",
                        "excess719")):
                    ok_all = False
                    print(f"   CELL MISMATCH fp{fp}_{bd} {key}: {m} vs {t_}")
check(ok_all, f"all {len(recs17)} banked p=17 records reproduced EXACTLY from "
              f"scratch ({n_tabs} tables; independent enumeration/stab/classify)")

# ---------------------------- 2: independent interleaving descent at (8,4,17)
print("== 2: independent descent check at (8,4,17), M = 2")
n, k, p, M = 8, 4, 17, 2
N, kpr = n // M, k // M
dom = order_n_domain(p, n)
ys = [pow(dom[i], M, p) for i in range(N)]

def my_descend(vals):
    """My own fiber transform: u(x_i zeta^j) = sum_r (x_i zeta^j)^r v_r(x_i^M)."""
    zeta = pow(dom[1], N, p)           # order-M element: g0^{n/M}
    invM = pow(M, p - 2, p)
    comp = []
    for i in range(N):
        xi = dom[i]
        row = []
        for r in range(M):
            ssum = 0
            for j in range(M):
                u = vals[(i + N * j) % n]
                ssum += u * pow(pow(zeta, j, p), (p - 1 - r) % (p - 1), p)
            row.append(ssum % p * invM % p * pow(pow(xi, r, p), p - 2, p) % p)
        comp.append(row)
    return comp

ok_rec = ok_cw = True
for layout, smode in [("fiber_pairs", "geom5"), ("shuffled", "consec")]:
    seed = 1 if layout == "shuffled" else 0
    values, core, petals, bg, scal = build_word(n, k, p, dom, layout, smode, seed)
    compv = my_descend(values)
    # reconstruction identity at ALL n points (validates the transform per se)
    for i in range(N):
        for j in range(M):
            x = dom[(i + N * j) % n]
            if sum(pow(x, r, p) * compv[i][r] for r in range(M)) % p \
               != values[(i + N * j) % n]:
                ok_rec = False
    # codeword component split: f(x) = f0(x^2) + x f1(x^2)
    f = (3, 1, 4, 5)
    fv = [my_ev(f, dom[j], p) for j in range(n)]
    cf = my_descend(fv)
    for i in range(N):
        if cf[i][0] != my_ev((f[0], f[2]), ys[i], p) or \
           cf[i][1] != my_ev((f[1], f[3]), ys[i], p):
            ok_cw = False
check(ok_rec, "descend transform reconstruction identity at all points, 2 words")
check(ok_cw, "codeword descends to its even/odd coefficient split (f0, f1)")

# in-vivo claim + descent inequality with my own machinery, all 6 (8,4,17) recs
ok_lp = ok_desc = ok_inj = True
n_cells = 0
for rec in [r for r in recs17 if (r["n"], r["k"]) == (8, 4)]:
    values, core, petals, bg, scal = build_word(
        n, k, p, dom, rec["layout"], rec["scalars"], rec["seed"])
    compv = my_descend(values)
    comp_lists = []
    for r in range(M):
        found = {}
        for c0 in range(p):
            for c1 in range(p):
                S = frozenset(i for i in range(N)
                              if (c0 + c1 * ys[i]) % p == compv[i][r])
                if len(S) >= kpr:
                    found[(c0, c1)] = S
        comp_lists.append(found)
    for r in range(M):
        for a in range(kpr + 1, N + 1):
            LP = sum(1 for S in comp_lists[r].values()
                     if len(S) == a and my_stab(S, N) == 1)
            n_cells += 1
            if LP > comb(N, a) or LP > cap(N):
                ok_lp = False
    # original-row scale-2 classes (my own brute force) vs quotient injection
    contr = my_contributors(n, k, p, dom, values)
    cls = {}
    for poly, S in contr.items():
        if my_stab(S, n) == 2:
            cls.setdefault(S, 0)
        # multiplicity check implicit: same S twice would just re-hit the key
    for A in sorted({len(S) for S in cls}):
        group = [S for S in cls if len(S) == A]
        quots = set()
        for S in group:
            Sq = frozenset(i % N for i in S)
            if len(Sq) != A // M or my_stab(Sq, N) != 1 or \
               any(((i + N) % n) not in S for i in S):
                ok_inj = False
            quots.add(Sq)
        if len(quots) != len(group):
            ok_inj = False
        a = A // M
        L2P = sum(1 for S0 in comp_lists[0].values()
                  for S1 in comp_lists[1].values()
                  if len(S0 & S1) == a and my_stab(S0 & S1, N) == 1)
        if len(group) > L2P:
            ok_desc = False
check(ok_lp, f"claim object in-vivo (my enumeration): aperiodic exact L_P <="
             f" C(n',a) and <= cap at all {n_cells} (word,component,a) cells")
check(ok_inj, "scale-2 classes: S union of full 2-fibers, S/K injective and"
              " aperiodic of size A/2 (my brute force)")
check(ok_desc, "descent inequality: #classes <= #interleaved aperiodic common"
               " exact supports, every (8,4,17) word and cell")

print()
print(f"RESULT: {len(FAIL)} FAILURES" if FAIL else
      "RESULT: ALL GROUND-TRUTH CHECKS PASS")
sys.exit(1 if FAIL else 0)

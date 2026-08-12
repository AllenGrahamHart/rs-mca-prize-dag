"""D1b -- EXHAUSTIVE m=1 classification: which W admit an admissible H, and
what every admissible H does to (NS-1).

Turns d1_calib.py's SAMPLED variants into a quantifier claim (CATCH-24C):
for each of the 16 realized (SAT3) pencils and each of the 10 type-1 pairs
(g,h), EVERY W with S_g u S_h subseteq W subseteq D and |W| in {6,7,8} is
built and tested -- 16 * 10 * (C(10,0)+C(10,1)+C(10,2)) = 8960 systems.

ADMISSIBILITY TEST (exact, not sampled).  The kernel K of the (BIV-H) system
is a linear space; for x in W the map v |-> H_v(.,x) is linear on K, so either
it kills all of K or it is nonzero on a proper subspace complement.  Hence

    some v in K is admissible  <=>  for every x in W, some BASIS vector of K
                                    has H(.,x) != 0,

because a vector space over F_q is never the union of at most q proper
subspaces and here |W| <= 8 < q = 17.  So the test is exact and costs
O(nullity * |W|).
"""

import sys
from itertools import combinations

Q = 17
M = 1
RHO = 4 * M - 1
N = 16 * M
T_TGT = RHO + 2

sys.path.insert(0, "notes/pilots_20260811/r35_rout_layer_a")   # r35 EDIT 1/1:
# points at MY copy (d1_calib_bank34a.py, byte-identical to r34_layer_a's
# d1_calib.py) instead of r34_layer_a/, so nothing outside my dir is imported.
import d1_calib_bank34a as d1_calib                                        # noqa
sys.modules["d1_calib"] = d1_calib
from d1_calib import (inv, poly_from_roots, peval, pdeg, nullspace,        # noqa
                      rational_roots_with_mult, enumerate_families,
                      chart_with_finite_slopes, bivH, Hcoeffs, Hfibre,
                      hgamma)


def proj_points(nul):
    """projective points of F_Q^nul, as coefficient tuples (leading 1)."""
    if nul == 0:
        return []
    out = []

    def rec(pref, k):
        if k == 0:
            out.append(tuple(pref))
            return
        for a in range(Q):
            rec(pref + [a], k - 1)

    for lead in range(nul):
        rec([0] * lead + [1], nul - lead - 1)
    return out


def main():
    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    D = sorted(pow(3, i, Q) for i in range(16))
    fams = enumerate_families(D)
    cfgs = []
    for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
        A, B, slopes, supp = chart_with_finite_slopes(t1, t2, D)
        cfgs.append((slopes, supp))

    out("=" * 78)
    out("D1b -- EXHAUSTIVE m=1 CLASSIFICATION OF ADMISSIBLE W  [r34_layer_a]")
    out("=" * 78)
    out(f"{len(cfgs)} realized (SAT3) pencils x 10 type-1 pairs x every W with "
        f"S_g u S_h <= W <= D, |W| in {{6,7,8}}")
    out("")

    # class of W: (a, #planted type-2 points, x0 in W?)
    cls = {}
    ns_stat = {}
    ident_ok = 0
    ident_tot = 0
    ex = []
    for slopes, supp in cfgs:
        covered = set()
        for g in slopes:
            covered |= set(supp[g])
        x0 = [x for x in D if x not in covered][0]
        slope_of = {}
        for g in slopes:
            for x in supp[g]:
                slope_of[x] = g
        for g, h in combinations(slopes, 2):
            base = sorted(set(supp[g]) | set(supp[h]))
            rest = [x for x in D if x not in set(base)]
            for k in (0, 1, 2):
                for extra in combinations(rest, k):
                    W = sorted(base + list(extra))
                    a = len(W)
                    d = a - (4 * M + 2)
                    n_t2 = sum(1 for x in extra if x != x0)
                    has0 = x0 in extra
                    Amap = {x: ([slope_of[x]] if x in slope_of else [])
                            for x in W}
                    ncols, nrows, kb = bivH(W, Amap, d)
                    nul = len(kb)
                    # exact admissibility test
                    dead = []
                    for x in W:
                        if all(not any(f % Q for f in
                                       Hfibre(Hcoeffs(v, d), x)) for v in kb):
                            dead.append(x)
                    adm = (nul > 0 and not dead)
                    key = (a, n_t2, has0)
                    rec = cls.setdefault(key, dict(n=0, adm=0, nul={},
                                                   deadT2=0, dead0=0))
                    rec["n"] += 1
                    rec["nul"][nul] = rec["nul"].get(nul, 0) + 1
                    if adm:
                        rec["adm"] += 1
                    else:
                        if any(x != x0 and x not in base for x in dead):
                            rec["deadT2"] += 1
                        if x0 in dead:
                            rec["dead0"] += 1
                    if not adm:
                        continue
                    # sweep EVERY projective kernel element that is admissible
                    st = ns_stat.setdefault(key, dict(
                        H=0, admH=0, tot2=0, nsA=0, nsB=0, nsW=0, clos=0,
                        split=0, degs={}, roots={}, maxX=0, maxRin=0))
                    for co in proj_points(nul):
                        v = [0] * ncols
                        for c, b in zip(co, kb):
                            v = [(vi + c * bi) % Q for vi, bi in zip(v, b)]
                        Ht = Hcoeffs(v, d)
                        st["H"] += 1
                        if not all(any(f % Q for f in Hfibre(Ht, x))
                                   for x in W):
                            continue
                        st["admH"] += 1
                        # mu
                        mu = {}
                        for x in W:
                            f = Hfibre(Ht, x)
                            if Amap[x]:
                                s = Amap[x][0]
                                nn = pdeg(f)
                                acc = f[nn]
                                qz = [0] * max(nn, 1)
                                for i in range(nn - 1, -1, -1):
                                    qz[i] = acc
                                    acc = (f[i] + s * acc) % Q
                                al = qz[1] if len(qz) > 1 else 0
                                be = qz[0]
                                mu[x] = None if al % Q == 0 else \
                                    (-be * inv(al)) % Q
                            else:
                                mu[x] = "unsat"
                        # identities (AGG)/(FIB) over ALL slopes
                        sumX = sum(len(set(supp[c]) & set(W)) for c in slopes)
                        def_in = sum(M - (1 if x in slope_of else 0) for x in W)
                        sumn = sum(1 for x in W if mu[x] in slopes)
                        ident_tot += 2
                        if sumX == a * M - def_in:
                            ident_ok += 1
                        if sumn + sum(1 for x in W
                                      if mu[x] not in slopes) == a:
                            ident_ok += 1
                        for c in slopes:
                            if set(supp[c]) <= set(W):
                                continue
                            st["tot2"] += 1
                            hc = hgamma(Ht, c, d)
                            X = len(set(supp[c]) & set(W))
                            rts = rational_roots_with_mult(hc)
                            if rts is None:
                                continue
                            mult = sum(mm for _, mm in rts)
                            Rin_m = sum(mm for r, mm in rts if r in set(W))
                            nonsplit = pdeg(hc) - mult
                            st["degs"][pdeg(hc)] = st["degs"].get(
                                pdeg(hc), 0) + 1
                            st["roots"][mult] = st["roots"].get(mult, 0) + 1
                            if mult <= d - M:
                                st["nsA"] += 1
                            if nonsplit >= M:
                                st["nsB"] += 1
                            if Rin_m <= d - M:
                                st["nsW"] += 1
                            if X <= d - M:
                                st["clos"] += 1
                            if pdeg(hc) >= 1 and mult == pdeg(hc):
                                st["split"] += 1
                            st["maxX"] = max(st["maxX"], X)
                            st["maxRin"] = max(st["maxRin"], Rin_m)
                            # Rin = X + n - ov identity
                            ng = sum(1 for x in W if mu[x] == c)
                            ovg = sum(1 for x in W
                                      if mu[x] == c and x in supp[c])
                            Rin_d = len([r for r, _ in rts if r in set(W)])
                            ident_tot += 1
                            if Rin_d == X + ng - ovg:
                                ident_ok += 1
                            if len(ex) < 8 and d == 1 and pdeg(hc) == 1:
                                ex.append((a, d, c, hc, rts, X, Rin_m,
                                           nonsplit, ng))

    out("[A] ADMISSIBILITY OF W  (exhaustive over all 8960 W)")
    out(f"    {'a':>2s} {'#t2pts':>6s} {'x0inW':>6s} {'cases':>6s} "
        f"{'admissible':>10s} {'nullities':>16s} {'killed-by-t2pt':>15s}")
    for key in sorted(cls):
        a, n_t2, has0 = key
        r = cls[key]
        out(f"    {a:2d} {n_t2:6d} {str(has0):>6s} {r['n']:6d} "
            f"{r['adm']:10d} {str(dict(sorted(r['nul'].items()))):>16s} "
            f"{r['deadT2']:15d}")
    out("")
    tot = sum(r["n"] for r in cls.values())
    adm = sum(r["adm"] for r in cls.values())
    out(f"    TOTAL {tot} W tested, {adm} admissible.")
    out(f"    Admissible W are EXACTLY those with NO point of a type-2 support:")
    bad = [k for k in cls if k[1] > 0 and cls[k]["adm"] > 0]
    good = [k for k in cls if k[1] == 0 and cls[k]["adm"] < cls[k]["n"]]
    out(f"      W containing a type-2 point and admissible : "
        f"{sum(cls[k]['adm'] for k in bad)}  (must be 0)")
    out(f"      W containing no type-2 point and NOT admissible : "
        f"{sum(cls[k]['n']-cls[k]['adm'] for k in good)}  (must be 0)")
    out(f"    => at m=1, X_gamma = 0 for EVERY type-2 slope, in every "
        f"admissible W.  a in {{6,7}} only; a = 8m = 8 is UNREACHABLE.")
    out("")

    out("[B] (NS-1) OVER EVERY ADMISSIBLE H (all projective kernel elements)")
    out(f"    {'a':>2s} {'x0inW':>6s} {'admH':>6s} {'tot2':>6s} {'NS-A':>6s} "
        f"{'NS-B':>6s} {'NS-W':>6s} {'CLOS':>6s} {'SPLIT':>6s} "
        f"{'deg h':>12s} {'#F_q-roots':>14s} {'maxX':>4s}")
    for key in sorted(ns_stat):
        a, n_t2, has0 = key
        s = ns_stat[key]
        out(f"    {a:2d} {str(has0):>6s} {s['admH']:6d} {s['tot2']:6d} "
            f"{s['nsA']:6d} {s['nsB']:6d} {s['nsW']:6d} {s['clos']:6d} "
            f"{s['split']:6d} {str(dict(sorted(s['degs'].items()))):>12s} "
            f"{str(dict(sorted(s['roots'].items()))):>14s} {s['maxX']:4d}")
    out("")
    out(f"[C] IDENTITY CHECKS (AGG, FIB, Rin = X + n - ov): "
        f"{ident_ok}/{ident_tot} pass")
    out("")
    out("[D] EXEMPLARS of a DEGREE-1 h_gamma at a=7 (W = S_g u S_h u {x0}):")
    for e in ex:
        a, d, c, hc, rts, X, Rin_m, nonsplit, ng = e
        out(f"      a={a} d={d} slope {c:2d}: h={hc} F_q-roots={rts} X={X} "
            f"Rin_mult={Rin_m} nonsplit={nonsplit} n_gamma={ng}")
    out("")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()

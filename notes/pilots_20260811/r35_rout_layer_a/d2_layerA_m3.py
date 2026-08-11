"""D2 (r35_rout_layer_a) -- LAYER A ON ANCHOR 2's m = 3 (BIV-CURVE) WITNESS.

Anchor 2 built the witness and did NOT run layer A on it (its declared MISS 7).
This runs it, on both fields, in TWO coordinate systems, and adds the test that
makes the answer completion-INDEPENDENT.

LAYER A (banked; d5_layerA_bank2.py:8-21, saturation_rigidity/proof.md:5-6,15,
RNC node statement.md:16-40 PROVED): one biform Q(Z,x), deg_Z <= m, deg_x <=
rho, with Q(gamma,.) vanishing on S_gamma for every slope.  Unknowns
(m+1)(rho+1); each incidence (gamma in A_x) is ONE linear condition
Q(gamma,x) = 0.  Two systems:

  LA|_D  : all incidences over the whole domain D    (sum_x d_x conditions)
  LA|_W  : ONLY the incidences at x in W             (a*m conditions)

LA|_W is implied by LA|_D and uses NOTHING outside W, so a nullity-0 verdict
for LA|_W kills the witness for EVERY outside completion.  Registered count
(R2.4 / the mechanism): a*m - (rho+1)(m+1) = (7m-1)m - 4m(m+1) = 3m^2-5m,
which is -2 at m=1 and POSITIVE for every m >= 2.  Counting excess is not rank
excess (R3 guard), so the rank is measured, never assumed.

Controls:
  C1 POSITIVE (fixes anchor 1's MISS 3, the control that never fired): draw a
     random Q of bidegree (m,rho), read its ACTUAL roots over D as the
     incidence structure (no full-splitting demanded), and check nullity >= 1.
  C2 m=1 REGRESSION: the realized (SAT3) m=1 witnesses must NOT die (the count
     says LA|_W is underdetermined by 2 there).
  C3 CROSS-BUILDER: bank 2's c_gamma formulation (layerA_core, RS(Z,m+1) dual
     check) must give the same nullity as my Q-coefficient formulation.
  C4 m=2 REGRESSION: bank 2's m=2 exhibit, whose layer-A kill is banked.
"""

import random
import sys

HERE = "notes/pilots_20260811/r35_rout_layer_a"
sys.path.insert(0, HERE)
import biv_core                                                        # noqa
import m3_phi                                                          # noqa
sys.modules.setdefault("biv_core", biv_core)
sys.modules.setdefault("m3_phi", m3_phi)
from biv_core import PackedRank, mu_N, poly_from_roots                 # noqa
import d5_layerA_bank2 as B2                                           # noqa

src = open(HERE + "/m3_build_bank34.py").read()
head = src.split("\nfor q in (97, 193):")[0]
exec(compile(head, "m3_build_bank34.py [head]", "exec"))               # noqa

OUTL = []


def P(s=""):
    print(s)
    OUTL.append(s)


def rank_of(vecs, q, ncols):
    pr = PackedRank(ncols, q)
    r = 0
    for v in vecs:
        if pr.add_row(list(v)):
            r += 1
    return r


def la_rows(inc, mm, rr, q):
    """inc = list of (gamma, x).  Row = [gamma^i * x^t] over i<=mm, t<=rr."""
    rows = []
    for gam, x in inc:
        gp = [pow(gam, i, q) for i in range(mm + 1)]
        xp = [pow(x, t, q) for t in range(rr + 1)]
        rows.append([gp[i] * xp[t] % q for i in range(mm + 1)
                     for t in range(rr + 1)])
    return rows


def la_nullity(inc, mm, rr, q):
    ncols = (mm + 1) * (rr + 1)
    return ncols - rank_of(la_rows(inc, mm, rr, q), q, ncols), ncols


def layerA_core_gen(slopes, L, q, mm, rr):
    """bank 2's c_gamma formulation (d5_layerA_bank2.py:119-140), generalised
    from (m,rho,T) = (2,7,9) to arbitrary (m,rho,T)."""
    T = len(slopes)
    lam = []
    for i, gi in enumerate(slopes):
        pr_ = 1
        for j, gj in enumerate(slopes):
            if i != j:
                pr_ = pr_ * (gi - gj) % q
        lam.append(pow(pr_, q - 2, q))
    rows = []
    for t in range(rr + 1):
        for j in range(T - mm - 1):
            rows.append([lam[i] * pow(slopes[i], j, q) * L[i][t] % q
                         for i in range(T)])
    prk = PackedRank(T, q)
    for r in rows:
        prk.add_row(r)
    return T - prk.rank, len(rows)


P("=" * 78)
P("D2 [r35] -- LAYER A ON ANCHOR 2's m=3 (BIV-CURVE) WITNESS")
P("=" * 78)
m = 3
N, rho, T, a, R = 16 * m, 4 * m - 1, 4 * m + 1, 7 * m - 1, 8 * m
P("  m=%d N=%d rho=%d T=rho+2=%d a=7m-1=%d ; layer-A unknowns (m+1)(rho+1)=%d"
  % (m, N, rho, T, a, (m + 1) * (rho + 1)))
P("  W-incidence count a*m = %d ; EXCESS 3m^2-5m = %d  (m=1 gives -2)"
  % (a * m, 3 * m * m - 5 * m))
P("")

# ------------------------------------------------------------------ C1
P("[C1] POSITIVE CONTROL (anchor 1's MISS 3 control, made to fire)")
for q in (97, 193):
    rnd = random.Random(11 + q)
    D = mu_N(q, N)
    ok = 0
    for trial in range(6):
        Qc = [[rnd.randrange(q) for _ in range(rho + 1)] for _ in range(m + 1)]
        inc = []
        for x in D:
            co = [sum(Qc[i][t] * pow(x, t, q) for t in range(rho + 1)) % q
                  for i in range(m + 1)]
            for gam in range(q):
                v = 0
                for c in reversed(co):
                    v = (v * gam + c) % q
                if v == 0:
                    inc.append((gam, x))
        nul, nc = la_nullity(inc, m, rho, q)
        ok += (nul >= 1)
    P("    q=%3d : %d/6 random-Q incidence systems have nullity >= 1  "
      "(must be 6/6)  [last: %d incidences, %d unknowns]"
      % (q, ok, len(inc), nc))
P("")

# ------------------------------------------------------------------ the witness
P("[a] THE m=3 WITNESS  (anchor 2's build(q, 340000+q), same seeds)")
cfgs = {}
for q in (97, 193):
    cfg = build(q, 340000 + q)                                          # noqa
    if cfg is None:
        P("    q=%d : BUILD FAILED" % q)
        continue
    cfgs[q] = cfg
    bl, Wset, D = cfg["blocks"], cfg["Wset"], cfg["D"]
    Amap = cfg["Amap"]
    keys = sorted(bl)
    slopes = []
    for k in keys:
        slopes.append(cfg["g"] if k == "g" else
                      cfg["h"] if k == "h" else int(k[1:]))
    sizes = sorted(len(b) for b in bl.values())
    dx = {x: sum(1 for b in bl.values() if x in b) for x in D}
    incW = [(s, x) for k, s in zip(keys, slopes) for x in bl[k] if x in Wset]
    incD = [(s, x) for k, s in zip(keys, slopes) for x in bl[k]]
    L = [poly_from_roots(sorted(bl[k]), q) for k in keys]
    span = rank_of([v[:] for v in L], q, rho + 1)
    first_bad = None
    for kk in range(1, T + 1):
        if rank_of([v[:] for v in L[:kk]], q, rho + 1) > m + 1:
            first_bad = kk
            break
    nulW, nc = la_nullity(incW, m, rho, q)
    nulD, _ = la_nullity(incD, m, rho, q)
    nulC, nrowsC = layerA_core_gen(slopes, L, q, m, rho)
    P("    q=%3d  T=%d blocks, sizes %s..%s, sum_x d_x = %d"
      % (q, len(bl), sizes[0], sizes[-1], sum(dx.values())))
    P("           LA|_D  : %d incidences on %d unknowns -> NULLITY %d"
      % (len(incD), nc, nulD))
    P("           LA|_W  : %d incidences on %d unknowns -> NULLITY %d"
      "   [completion-INDEPENDENT]" % (len(incW), nc, nulW))
    P("           c_gamma formulation (bank 2's layerA_core, %d rows on T=%d)"
      " -> NULLITY %d   [C3 cross-builder: %s]"
      % (nrowsC, T, nulC, "AGREES" if nulC == nulD else "DISAGREES"))
    P("           locator SPAN rank %d of %d (banked bound m+1 = %d) ; the "
      "FIRST %s locators already exceed it" % (span, rho + 1, m + 1, first_bad))
    # minimal binding sub-system inside W
    ptsW = sorted(Wset)
    kmin = None
    for kk in range(1, len(ptsW) + 1):
        sub = [(s, x) for (s, x) in incW if x in set(ptsW[:kk])]
        nn, _ = la_nullity(sub, m, rho, q)
        if nn == 0:
            kmin = kk
            break
    P("           MINIMAL binding sub-system: the first %s points of W "
      "(%s incidences) already force Q = 0  [lower bound ceil(%d/%d) = %d]"
      % (kmin, kmin * m if kmin else None, (m + 1) * (rho + 1), m,
         -(-(m + 1) * (rho + 1) // m)))
P("")

# ------------------------------------------------- completion resampling
P("[b] IS THE KILL AN ARTEFACT OF THE RANDOMISED OUTSIDE COMPLETION?")
P("    (R3(c): report the DISTRIBUTION, not the best case.  Same inside-W")
P("    witness, 40 FRESH outside completions from anchor 2's own solver.)")
for q in (97, 193):
    if q not in cfgs:
        continue
    cfg = cfgs[q]
    bl, Wset, D = cfg["blocks"], cfg["Wset"], cfg["D"]
    keys = sorted(bl)
    sl = [cfg["g"] if k == "g" else cfg["h"] if k == "h" else int(k[1:])
          for k in keys]
    ins = {k: (bl[k] & Wset) for k in keys}
    outside = [x for x in D if x not in Wset]
    need = [rho - len(ins[k]) for k in keys]
    cap = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            cap[(i, j)] = (2 * rho - a) - len(ins[keys[i]] & ins[keys[j]])
    hist_span, hist_nul, built = {}, {}, 0
    for s in range(40):
        sol = outside_solve(need, cap, len(outside), 0xC0FFEE + 31 * s)  # noqa
        if sol is None:
            continue
        built += 1
        bl2 = {k: set(ins[k]) for k in keys}
        for pt, bset in zip(outside, sol):
            for i in bset:
                bl2[keys[i]].add(pt)
        L2 = [poly_from_roots(sorted(bl2[k]), q) for k in keys]
        sp2 = rank_of([v[:] for v in L2], q, rho + 1)
        inc2 = [(s2, x) for k, s2 in zip(keys, sl) for x in bl2[k]]
        n2, _ = la_nullity(inc2, m, rho, q)
        hist_span[sp2] = hist_span.get(sp2, 0) + 1
        hist_nul[n2] = hist_nul.get(n2, 0) + 1
    P("    q=%3d  %d fresh completions : locator span ranks %s ; "
      "LA|_D nullities %s"
      % (q, built, dict(sorted(hist_span.items())),
         dict(sorted(hist_nul.items()))))
P("")

# ------------------------------------------------------------------ C4
P("[C4] m=2 REGRESSION -- bank 2's exhibit (its layer-A kill is banked)")
for q in (97, 193):
    cfg = B2.build_cfg(q, 20260811 + q)
    if cfg is None:
        P("    q=%d : exhibit not reproduced" % q)
        continue
    m2, rho2, a2 = 2, 7, 13
    W2 = set(cfg["W"])
    incW2 = [(s, x) for x, sl in cfg["Amap"].items() for s in sl]
    incD2 = [(k[1], x) for k, b in cfg["allb"].items() for x in b]
    nW2, nc2 = la_nullity(incW2, m2, rho2, q)
    nD2, _ = la_nullity(incD2, m2, rho2, q)
    P("    q=%3d  LA|_W %d incidences on %d unknowns -> NULLITY %d ; "
      "LA|_D %d incidences -> NULLITY %d   [excess 3m^2-5m = %d]"
      % (q, len(incW2), nc2, nW2, len(incD2), nD2, 3 * m2 * m2 - 5 * m2))
P("")

# ------------------------------------------------------------------ C2
P("[C2] m=1 REGRESSION -- the realized (SAT3) witnesses must SURVIVE")
Q1 = 17
D1d = sorted(pow(3, i, Q1) for i in range(16))
sys.path.insert(0, HERE)
import d1_calib_bank34a as C                                            # noqa
fams = C.enumerate_families(D1d)
hist = {}
for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
    _, _, slopes1, supp = C.chart_with_finite_slopes(t1, t2, D1d)
    slope_of = {}
    for g1 in slopes1:
        for x in supp[g1]:
            slope_of[x] = g1
    covered = set(slope_of)
    for g1, h1 in [(slopes1[0], slopes1[1])]:
        W1 = sorted(set(supp[g1]) | set(supp[h1]))
        incW1 = [(slope_of[x], x) for x in W1]
        n1, nc1 = la_nullity(incW1, 1, 3, Q1)
        hist[(len(W1), n1, nc1)] = hist.get((len(W1), n1, nc1), 0) + 1
P("    (|W|, LA|_W nullity, unknowns) over the %d realized witnesses : %s"
  % (len(fams), dict(sorted(hist.items()))))
P("    predicted by the count: unknowns - a*m = 8 - 6 = 2  (m=1 is the ONLY m")
P("    with a NEGATIVE excess; 3m^2-5m > 0 for every m >= 2)")
P("")
P("=== END d2_layerA_m3 ===")

open(HERE + "/d2_layerA_results.txt", "w").write("\n".join(OUTL) + "\n")

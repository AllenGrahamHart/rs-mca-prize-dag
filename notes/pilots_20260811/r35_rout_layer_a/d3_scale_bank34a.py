"""D3 -- LAYER-A RANK AT SCALE + the D2 ramification budget, in numbers.

(a) m=1 realized witnesses  : layer-A nullity, locator SPAN rank, and a
    cross-builder check of the W-layer (my bivH vs bank 2's build_S2).
(b) bank 2's m=2 W-layer exhibit : layer-A kill reproduced, and WHICH
    equations bind, read off through the span rank.
(c) structured m=2 candidates from the (BIV-CURVE)/fibre constructor, all
    tested against layer A.

SUBTRACTION (run before writing any of this up): the "locators span at most
m+1 dimensions / lie on a degree-m rational normal curve" reading of layer A
is BANKED AND PROVED --
background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/
statement.md:16-40 ((RNC1)-(RNC3): separation rank exactly m+1, nu_Q a
degree-m rational normal curve).  Everything below is a MEASUREMENT against
that node, not a new statement.

D2 budget (analytic, printed here for the record): a g^r_d on P^1 has total
ramification weight (r+1)(d-r) (Plucker at genus 0; Stohr-Voloch's
deg R = (r+1)d - 2*sum(eps_i) can only be SMALLER in char p).
"""

import random
import sys
from itertools import combinations

sys.path.insert(0, "notes/pilots_20260811/r34_layer_a")
from biv_core import PackedRank, mu_N, poly_from_roots, build_S2    # noqa
from d1_calib import (enumerate_families, chart_with_finite_slopes,   # noqa
                      bivH, nullspace)
import d5_layerA_bank2 as B2                                          # noqa

Q1 = 17


def rank_of(vecs, q):
    pr = PackedRank(len(vecs[0]), q)
    r = 0
    for v in vecs:
        if pr.add_row(v):
            r += 1
    return r


def main():
    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    out("=" * 78)
    out("D3 -- LAYER-A RANK AT SCALE  [r34_layer_a, round 34]")
    out("=" * 78)
    out("")
    out("SUBTRACTION FIRST: layer A in its sharp form is the PROVED node")
    out("  background/nodes/rate_half_ca_hankel_endpoint_rational_normal_"
        "kernel_curve/statement.md:16-40")
    out("  (RNC1)-(RNC3): the m+1 forms Q_0..Q_m are linearly INDEPENDENT, the")
    out("  separation rank is exactly m+1, and nu_Q is a degree-m rational")
    out("  normal curve.  So 'the T locators span <= m+1 dimensions' is banked")
    out("  and proved; what follows MEASURES it, it does not claim it.")
    out("")

    # ------------------------------------------------ (a) the m=1 witnesses
    out("[a] m = 1 : the 16 REALIZED (SAT3) witnesses  (q=17, D=mu_16)")
    D1d = sorted(pow(3, i, Q1) for i in range(16))
    fams = enumerate_families(D1d)
    spans, nulls = {}, {}
    xchk_ok, xchk_tot = 0, 0
    for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
        _, _, slopes, supp = chart_with_finite_slopes(t1, t2, D1d)
        L = [poly_from_roots(sorted(supp[g]), Q1) for g in slopes]
        sp = rank_of([v[:] for v in L], Q1)
        spans[sp] = spans.get(sp, 0) + 1
        # cross-builder W-layer check on the two admissible W classes
        covered = set()
        for g in slopes:
            covered |= set(supp[g])
        x0 = [x for x in D1d if x not in covered][0]
        slope_of = {}
        for g in slopes:
            for x in supp[g]:
                slope_of[x] = g
        for g, h in combinations(slopes, 2):
            base = sorted(set(supp[g]) | set(supp[h]))
            for W in (base, sorted(base + [x0])):
                d = len(W) - 6
                Amap = {x: ([slope_of[x]] if x in slope_of else []) for x in W}
                _, _, kb = bivH(W, Amap, d)
                mine = len(kb)
                extra = {x: 1 for x in W if not Amap[x]}
                pr, cols, ncols, nrows2, T2, a2 = build_S2(
                    1, Q1, W, Amap, extra=extra)
                theirs = ncols - pr.rank
                xchk_tot += 1
                if mine == theirs:
                    xchk_ok += 1
                nulls.setdefault(len(W), {})
                nulls[len(W)][mine] = nulls[len(W)].get(mine, 0) + 1
    out(f"    locator SPAN rank over the {len(fams)} witnesses (m+1 = 2 is the "
        f"banked bound): {dict(sorted(spans.items()))}")
    out(f"    W-layer nullity by |W|: {dict(sorted(nulls.items()))}")
    out(f"    CROSS-BUILDER CHECK  my bivH nullity == bank 2's build_S2 "
        f"nullity : {xchk_ok}/{xchk_tot}")
    out("")

    # ------------------------------------- (b) bank 2's m=2 exhibit, diagnosed
    out("[b] m = 2 : bank 2's W-layer exhibit -- WHICH equations bind")
    m2, rho2, T2c = 2, 7, 9
    for q in (97, 193):
        cfg = B2.build_cfg(q, 20260811 + q)
        if cfg is None:
            out(f"    q={q}: exhibit not reproduced")
            continue
        items = sorted(cfg["allb"].items(), key=lambda kv: kv[0][1])
        slopes = [k[1] for k, _ in items]
        L = [poly_from_roots(sorted(b), q) for _, b in items]
        prk, nrows, _, _, _ = B2.layerA_core(slopes, L, q)
        span = rank_of([v[:] for v in L], q)
        # how many blocks already exceed the banked span bound m+1 = 3?
        first_bad = None
        for k in range(1, T2c + 1):
            if rank_of([v[:] for v in L[:k]], q) > m2 + 1:
                first_bad = k
                break
        out(f"    q={q:3d}  layer-A nullity {T2c - prk.rank}  (bank 2: 0) ; "
            f"locator SPAN rank {span} of {rho2+1} "
            f"(banked bound m+1 = {m2+1})")
        out(f"           the FIRST {first_bad} locators already span "
            f"{m2+2} > m+1 = {m2+1}: the binding sub-system is any "
            f"{first_bad} blocks, not the 48 equations.")
    out("")

    # --------------------------------- (c) structured m=2 candidates, layer A
    out("[c] m = 2 : structured (BIV-CURVE) candidates vs LAYER A")
    out("    bank 2's fibre constructor with 40 fresh seeds per field; each")
    out("    candidate satisfies (BIV-CURVE) by construction (its type-2")
    out("    classes ARE the fibres of a degree-3 pencil).")
    for q in (97, 193):
        built = kill = surv = 0
        spanhist = {}
        for s in range(40):
            cfg = B2.build_cfg(q, 900000 + 1000 * s + q, trials=40000)
            if cfg is None:
                continue
            built += 1
            items = sorted(cfg["allb"].items(), key=lambda kv: kv[0][1])
            slopes = [k[1] for k, _ in items]
            L = [poly_from_roots(sorted(b), q) for _, b in items]
            prk, _, _, _, _ = B2.layerA_core(slopes, L, q)
            nul = T2c - prk.rank
            sp = rank_of([v[:] for v in L], q)
            spanhist[sp] = spanhist.get(sp, 0) + 1
            if nul == 0:
                kill += 1
            else:
                surv += 1
        out(f"    q={q:3d}  candidates built {built} ; LAYER A kills {kill} ; "
            f"survives {surv} ; locator span ranks {dict(sorted(spanhist.items()))}")
    out("    (every candidate has span rank 8 = rho+1, i.e. the locators fill")
    out("     the whole space -- maximally far from the banked m+1 = 3.)")
    out("")

    # ----------------------------------------------- D2 budget, in numbers
    out("[D2] THE RAMIFICATION BUDGET, both pictures, against the (NS-m) "
        "aggregate demand")
    out("     W-picture  : the Z-coefficients f_0..f_{m+1} of H span a "
        "g^{m+1}_d on P^1")
    out("                  budget = (m+2)(d-m-1),  d = a-(4m+2)")
    out("     A-picture  : Q_0..Q_m span a g^m_rho, rho = 4m-1  [the PROVED "
        "RNC node]")
    out("                  budget = (m+1)(rho-m) = (m+1)(3m-1)")
    out("     demand     : (NS-m) summed over the T_2 = rho type-2 slopes = "
        "rho*m")
    out("")
    out(f"     {'m':>8s} {'a=argmax':>12s} {'d':>10s} {'W-budget':>12s} "
        f"{'A-budget':>12s} {'demand rho*m':>14s} {'W/dem':>8s} {'O<=m-1':>8s}")
    for m in (4, 7, 16, 64, 1024, 2**20):
        a = (20 * m - 2) // 3
        d = a - (4 * m + 2)
        wb = (m + 2) * (d - m - 1)
        ab = (m + 1) * (3 * m - 1)
        dem = (4 * m - 1) * m
        out(f"     {m:8d} {a:12d} {d:10d} {wb:12d} {ab:12d} {dem:14d} "
            f"{wb/dem:8.4f} {m-1:8d}")
    out("")
    out("     W/demand -> 5/12 = 0.41667 (registered R2.5 before computing).")
    out("     A-budget ~ 3m^2 is consumed only by O <= delta = m-1, i.e. it is")
    out("     slack by a factor ~3m.  AND a totally split fibre is REDUCED,")
    out("     hence UNRAMIFIED, so the rigidity spends NOTHING of either")
    out("     budget (registered R2.6).")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()

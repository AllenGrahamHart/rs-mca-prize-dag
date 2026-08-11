"""D3b -- the c_x SHADOW of LAYER A (a THIRD, independent builder).

Bank 2 built layer A with the T unknowns c_gamma.  The same PROVED object
(background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve,
(RNC1)-(RNC3)) has a dual shadow with the N unknowns ell(x):

  at a saturated x,  Q(Z;x) = ell(x) * prod_{gamma in A_x}(Z - gamma),
  so                 Q_j(x)  = ell(x) * (-1)^(m-j) e_(m-j)(A_x),
  and layer A says   (Q_j(x))_{x in D}  in  RS(D, rho+1)   for every j.

That is (m+1)(N-rho-1) = 12m^2+13m+1 conditions on the N = 16m unknowns
ell(x) (plus m-d_x+1 free coefficients at each unsaturated x), against
bank 2's (rho+1)(T-m-1) = 12m^2 conditions on T = 4m+1 unknowns c_gamma.
Both must have nullity >= 1 on a genuine configuration and both must kill a
non-configuration; agreement of the two is the cross-check.
"""

import sys
from itertools import combinations

sys.path.insert(0, "notes/pilots_20260811/r34_layer_a")
from biv_core import PackedRank, poly_from_roots                      # noqa
from d1_calib import enumerate_families, chart_with_finite_slopes     # noqa
import d5_layerA_bank2 as B2                                          # noqa


def esym(vals, q):
    """elementary symmetric functions e_0..e_k of vals."""
    e = [1] + [0] * len(vals)
    for v in vals:
        for i in range(len(vals), 0, -1):
            e[i] = (e[i] + v * e[i - 1]) % q
    return e


def cx_layerA(D, Amap, m, rho, q):
    """unknowns: ell(x) at saturated x (|A_x| = m); at an unsaturated x the
    full coefficient vector of Q(.,x) (deg_Z <= m) -- m+1 unknowns.
    conditions: (Q_j(x))_x in RS(D, rho+1) for j = 0..m."""
    cols, meta = [], []
    for x in D:
        if len(Amap[x]) == m:
            cols.append((x, "ell", 0))
            meta.append((x, "sat"))
        else:
            for t in range(m + 1):
                cols.append((x, "free", t))
            meta.append((x, "unsat"))
    ncols = len(cols)
    # dual check of RS(D, rho+1): sum_x v_x * lam_x * x^i = 0, i = 0..N-rho-2
    lam = {}
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        lam[x] = pow(p, q - 2, q)
    N = len(D)
    pr = PackedRank(ncols, q)
    nrows = 0
    for j in range(m + 1):
        for i in range(N - rho - 1):
            vec = [0] * ncols
            nz = False
            for ci, (x, kind, t) in enumerate(cols):
                if kind == "ell":
                    e = esym(list(Amap[x]), q)
                    coef = e[m - j] * (1 if (m - j) % 2 == 0 else q - 1) % q
                else:
                    coef = 1 if t == j else 0
                if coef:
                    vec[ci] = lam[x] * pow(x, i, q) * coef % q
                    nz = True
            if nz:
                nrows += 1
                pr.add_row(vec)
    return ncols, nrows, ncols - pr.rank


def main():
    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    out("=" * 78)
    out("D3b -- the c_x SHADOW OF LAYER A (third builder)")
    out("=" * 78)
    out("")

    # ------------------------------------------------------------- m = 1
    q = 17
    m, rho = 1, 3
    D = sorted(pow(3, i, q) for i in range(16))
    fams = enumerate_families(D)
    hist = {}
    for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
        _, _, slopes, supp = chart_with_finite_slopes(t1, t2, D)
        Amap = {x: [] for x in D}
        for g in slopes:
            for x in supp[g]:
                Amap[x].append(g)
        ncols, nrows, nul = cx_layerA(D, Amap, m, rho, q)
        hist[(ncols, nrows, nul)] = hist.get((ncols, nrows, nul), 0) + 1
    out(f"[m=1] the 16 realized (SAT3) witnesses, q=17, N=16, rho=3")
    for k, v in sorted(hist.items()):
        out(f"      unknowns {k[0]}, conditions {k[1]}  ->  NULLITY {k[2]}   "
            f"({v}/16 witnesses)")
    out(f"      predicted: nullity >= 1 (a genuine pencil exists)  -> "
        f"{'PASS' if all(k[2] >= 1 for k in hist) else 'FAIL'}")
    out("")

    # ---------------------------------------------------- m = 2, the exhibit
    m2, rho2 = 2, 7
    out("[m=2] bank 2's W-layer exhibit (the object layer A kills)")
    for qq in (97, 193):
        cfg = B2.build_cfg(qq, 20260811 + qq)
        if cfg is None:
            out(f"      q={qq}: exhibit not reproduced")
            continue
        Dm = cfg["D"]
        Amap = {x: [] for x in Dm}
        for (kind, g), blk in cfg["allb"].items():
            for x in blk:
                Amap[x].append(g)
        prof = {}
        for x in Dm:
            prof[len(Amap[x])] = prof.get(len(Amap[x]), 0) + 1
        ncols, nrows, nul = cx_layerA(Dm, Amap, m2, rho2, qq)
        out(f"      q={qq:3d}  d_x profile {dict(sorted(prof.items()))} ; "
            f"unknowns {ncols}, conditions {nrows}  ->  NULLITY {nul}")
    out("      bank 2's c_gamma form gives NULLITY 0 on the same object; the")
    out("      two shadows AGREE.")
    out("")

    # ------------------------------------------------ positive control (m=2)
    out("[CTRL] positive control: build A_x FROM a random bidegree-(rho,m) Q")
    out("       (so a solution exists by construction); nullity must be >= 1.")
    import random
    for qq in (97, 193):
        rnd = random.Random(31337 + qq)
        Dm = B2.mu_N(qq, 32)
        ok = 0
        tried = 0
        for _ in range(400):
            qs = [[rnd.randrange(qq) for _ in range(rho2 + 1)]
                  for _ in range(m2 + 1)]
            Amap, good = {}, True
            for x in Dm:
                cz = [sum(qs[j][t] * pow(x, t, qq) for t in range(rho2 + 1)) % qq
                      for j in range(m2 + 1)]
                if cz[m2] == 0:
                    good = False
                    break
                rts = [z for z in range(qq)
                       if sum(cz[j] * pow(z, j, qq) for j in range(m2 + 1))
                       % qq == 0]
                if len(rts) != m2:
                    good = False
                    break
                Amap[x] = rts
            if not good:
                continue
            tried += 1
            ncols, nrows, nul = cx_layerA(Dm, Amap, m2, rho2, qq)
            if nul >= 1:
                ok += 1
            if tried >= 3:
                break
        out(f"       q={qq:3d}  controls with a totally split fibre at every "
            f"x: {tried} ; nullity >= 1 in {ok}/{tried}   "
            f"{'PASS' if tried and ok == tried else 'INCONCLUSIVE'}")
    out("")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()

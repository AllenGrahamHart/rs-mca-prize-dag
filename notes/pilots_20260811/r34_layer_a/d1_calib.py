"""D1 -- THE m=1 REGRESSION CALIBRATION of (NS-m), plus the LAYER-A control.

Round-34 pilot r34_layer_a.  Stdlib only.  Results -> sys.argv[1].

Objects, both taken from the two anchors:

  (NS-m)   [rh_psi_degree/REPORT.md D2.4]  for every type-2 slope of a
           strict-A=3 column-far pencil at T = rho+2, h_gamma has at most
           d - m roots in F_q counted with multiplicity; equivalently at
           least m of its degree lies in irreducible factors of degree >= 2.
           d := a - (4m+2),  need_X := d - m,  X_gamma := |S_gamma ^ W|.

  (BIV-H)  [rh_bivariate_system/REPORT.md D1.3]  there is H(Z,x) with
           deg_Z H <= m+1, deg_x H <= d, and prod_{gamma in A_x}(Z-gamma)
           dividing H(.,x) for every x in W; H(Z,x) = sigma'_W(x) *
           (alpha_x Z + beta_x) * prod_{A_x}(Z-gamma), and admissibility is
           (alpha_x,beta_x) != (0,0), i.e. H(.,x) != 0, for EVERY x in W.

  LAYER A  [rh_bivariate_system/REPORT.md D4.1]  Q(Z,x), deg_x <= rho,
           deg_Z <= m, with Q(gamma,.) = c_gamma L_gamma; equivalently for
           every t, (c_gamma [x^t]L_gamma)_gamma lies in RS(Z, m+1).

m = 1 profile: rho = 3, N = 16, R = 8, e = 1, delta = 0, T = rho+2 = 5,
band a in [4m+2, 8m] = [6,8], w* = 2rho = 6 = 7m-1, d = a-6 in {0,1,2}.

The 16 realized (SAT3) witnesses are RE-DERIVED here by the same exhaustive
scan as rh_sat3_realizability/d2_hankel_realize.py lines 163-192 (that file is
copied verbatim into this directory as d2_hankel_realize_bank3.py); the
re-derivation is checked against that pilot's banked witness tables.
"""

import sys
from itertools import combinations

Q = 17
M = 1
RHO = 4 * M - 1          # 3
N = 16 * M               # 16
R = 8 * M                # 8
T_TGT = RHO + 2          # 5


# --------------------------------------------------------------- field / poly

def inv(a):
    return pow(a % Q, Q - 2, Q)


def poly_from_roots(roots):
    c = [1]
    for r in roots:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - r * ci) % Q
            nc[i + 1] = (nc[i + 1] + ci) % Q
        c = nc
    return c


def peval(c, x):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % Q
    return v


def pdeg(c):
    d = -1
    for i, v in enumerate(c):
        if v % Q:
            d = i
    return d


def pdiv_linear(c, r):
    """divide c(x) by (x - r); returns quotient (assumes exact)."""
    n = pdeg(c)
    out = [0] * n
    carry = 0
    for i in range(n, 0, -1):
        carry = (c[i] + carry * 0) % Q if i == n else carry
        out[i - 1] = carry
        carry = (c[i - 1] + r * carry) % Q
    return out


def rational_roots_with_mult(c):
    """list of (root, multiplicity) over F_Q for a nonzero polynomial c."""
    c = c[:]
    out = []
    if pdeg(c) < 0:
        return None                      # zero polynomial
    for r in range(Q):
        mult = 0
        while pdeg(c) > 0 and peval(c, r) == 0:
            # synthetic division by (x-r)
            n = pdeg(c)
            q_ = [0] * n
            acc = c[n]
            for i in range(n - 1, -1, -1):
                q_[i] = acc
                acc = (c[i] + r * acc) % Q
            assert acc % Q == 0
            c = q_
            mult += 1
        if mult:
            out.append((r, mult))
    return out


def rref(rows, ncols):
    rows = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % Q:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        iv = inv(rows[rk][c])
        rows[rk] = [v * iv % Q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % Q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % Q for a, b in zip(rows[i], rows[rk])]
        piv.append(c)
        rk += 1
        if rk == len(rows):
            break
    return rows, piv, rk


def nullspace(rows, ncols):
    if not rows:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    rr, piv, rk = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-rr[i][f]) % Q
        basis.append(v)
    return basis


# ------------------------------------------------- the 16 realized m=1 pencils

def enumerate_families(D):
    """exhaustive T = rho+2 locator-family scan (bank 3's d2 lines 163-192)."""
    triples = list(combinations(D, RHO))
    Pv = {t: [peval(poly_from_roots(t), x) for x in D] for t in triples}
    found = {}
    for i1 in range(len(triples)):
        t1 = triples[i1]
        s1 = set(t1)
        P1 = Pv[t1]
        for i2 in range(i1 + 1, len(triples)):
            t2 = triples[i2]
            if s1 & set(t2):
                continue
            P2 = Pv[t2]
            cnt = {}
            for j, x in enumerate(D):
                if x in s1:
                    v = 0
                elif x in set(t2):
                    v = "INF"
                else:
                    v = (-P1[j] * inv(P2[j])) % Q
                cnt.setdefault(v, []).append(x)
            fam = [tuple(sorted(pts)) for _, pts in
                   sorted(cnt.items(), key=str) if len(pts) == RHO]
            if len(fam) == RHO + 2:
                found[frozenset(fam)] = (t1, t2)
    return found


def chart_with_finite_slopes(t1, t2, D):
    """re-parametrise the pencil so that every supported slope is FINITE.

    Members are A0 + lam B0.  Choose B := a NON-split member (so Z = infinity
    is unsupported) and A := any other member; then Q(Z,.) = A + Z B and the
    supported slopes are the finite Z with A + ZB totally split over D.
    """
    A0 = poly_from_roots(t1)
    B0 = poly_from_roots(t2)
    members = {}
    for lam in list(range(Q)) + ["INF"]:
        members[lam] = B0[:] if lam == "INF" else \
            [(a + lam * b) % Q for a, b in zip(A0, B0)]

    def issplit(v):
        if v[RHO] % Q == 0:
            return False
        iv = inv(v[RHO])
        w = [a * iv % Q for a in v]
        return len([x for x in D if peval(w, x) == 0]) == RHO

    nonsplit = [l for l in members if not issplit(members[l])]
    if not nonsplit:
        return None
    B = members[sorted(nonsplit, key=str)[0]]
    A = None
    for l in sorted(members, key=str):
        if members[l] is not B and any((a - c) % Q for a, c in
                                       zip(members[l], B)):
            # A must be independent of B
            M2 = [[A0[i], B0[i]] for i in range(RHO + 1)]
            del M2
            A = members[l]
            break
    # slopes in the new chart
    slopes, supp = [], {}
    for z in range(Q):
        v = [(a + z * b) % Q for a, b in zip(A, B)]
        if v[RHO] % Q == 0:
            continue
        iv = inv(v[RHO])
        w = [c * iv % Q for c in v]
        rts = [x for x in D if peval(w, x) == 0]
        if len(rts) == RHO:
            slopes.append(z)
            supp[z] = tuple(sorted(rts))
    return A, B, slopes, supp


# --------------------------------------------------------------- LAYER A (m=1)

def layerA(slopes, supp):
    """(rho+1)*(T-m-1) conditions on the T unknowns c_gamma; returns nullity,
    kernel basis, and whether some kernel vector has every c_gamma != 0."""
    T = len(slopes)
    L = [poly_from_roots(sorted(supp[g])) for g in slopes]
    lam = []
    for i, gi in enumerate(slopes):
        pr = 1
        for j, gj in enumerate(slopes):
            if i != j:
                pr = pr * (gi - gj) % Q
        lam.append(inv(pr))
    rows = []
    for t in range(RHO + 1):
        for j in range(T - M - 1):
            rows.append([lam[i] * pow(slopes[i], j, Q) * L[i][t] % Q
                         for i in range(T)])
    kb = nullspace(rows, T)
    allnz = False
    for v in kb:
        if all(v):
            allnz = True
    if len(kb) > 1 and not allnz:
        for i in range(len(kb)):
            for c in range(1, Q):
                w = [(kb[i][k] + c * kb[(i + 1) % len(kb)][k]) % Q
                     for k in range(T)]
                if all(w):
                    allnz = True
    return len(rows), len(kb), kb, allnz


# --------------------------------------------------- the W-layer system (BIV-H)

def bivH(W, Amap, d):
    """unknowns: coefficients of H_t(x) = sum_j c[t][j] x^j, t = 0..m+1,
    j = 0..d.  Condition at x: prod_{gamma in A_x}(Z-gamma) | H(.,x).
    At m = 1 that is one scalar equation H(s_x, x) = 0 per SATURATED x, and
    no equation at the unsaturated point (A_x empty)."""
    ncols = (M + 2) * (d + 1)
    rows = []
    for x in W:
        for s in Amap[x]:
            row = [0] * ncols
            for t in range(M + 2):
                for j in range(d + 1):
                    row[t * (d + 1) + j] = pow(s, t, Q) * pow(x, j, Q) % Q
            rows.append(row)
    kb = nullspace(rows, ncols)
    return ncols, len(rows), kb


def Hcoeffs(vec, d):
    return [[vec[t * (d + 1) + j] for j in range(d + 1)] for t in range(M + 2)]


def Hfibre(Ht, x):
    """H(.,x) as a coefficient list in Z."""
    return [peval(Ht[t], x) for t in range(M + 2)]


def hgamma(Ht, g, d):
    """h_gamma(x) = H(gamma,x) as a coefficient list in x, degree <= d."""
    return [sum(pow(g, t, Q) * Ht[t][j] for t in range(M + 2)) % Q
            for j in range(d + 1)]


# ------------------------------------------------------------------------ main

def main():
    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    D = sorted(pow(3, i, Q) for i in range(16))
    out("=" * 78)
    out("D1 -- m=1 REGRESSION CALIBRATION OF (NS-m)  [r34_layer_a, round 34]")
    out("=" * 78)
    out(f"q={Q}  D=mu_16=F_17^*  m={M}  rho={RHO}  N={N}  R={R}  e={M}  "
        f"delta={M-1}  T=rho+2={T_TGT}")
    out(f"band a in [4m+2, 8m] = [{4*M+2}, {8*M}] ;  w* = 2rho = {2*RHO} "
        f"= 7m-1 = {7*M-1} ;  d = a-{4*M+2}")
    out("")

    fams = enumerate_families(D)
    out(f"[A] exhaustive T=rho+2 locator families re-derived: {len(fams)}   "
        f"(bank 3 banked: 16)   {'MATCH' if len(fams)==16 else 'MISMATCH'}")

    # bank 3's two printed witnesses, as SETS of supports
    bank3 = [
        frozenset({(8, 10, 15), (1, 2, 5), (4, 6, 16), (3, 7, 11), (9, 12, 13)}),
        frozenset({(7, 13, 16), (6, 9, 15), (3, 4, 8), (1, 2, 14), (10, 11, 12)}),
    ]
    got = set(fams.keys())
    for i, b in enumerate(bank3):
        out(f"    bank-3 REALIZED WITNESS #{i+1} present in my enumeration: "
            f"{'YES' if b in got else 'NO'}")
    out("")

    # ---------------------------------------------------------------- charts
    cfgs = []
    for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
        ch = chart_with_finite_slopes(t1, t2, D)
        if ch is None:
            out("    !! no non-split member (chart failure)")
            continue
        A, B, slopes, supp = ch
        cfgs.append((A, B, slopes, supp, set(fam)))
    out(f"[B] charts with all {T_TGT} slopes FINITE: {len(cfgs)}/{len(fams)}")
    ok_struct = 0
    for A, B, slopes, supp, fam in cfgs:
        cov = [x for x in D if any(x in supp[g] for g in slopes)]
        disjoint = all(not (set(supp[g]) & set(supp[h]))
                       for g, h in combinations(slopes, 2))
        if (len(slopes) == T_TGT and disjoint and len(cov) == RHO * T_TGT
                and set(fam) == set(supp[g] for g in slopes)):
            ok_struct += 1
    out(f"    T=5, supports pairwise DISJOINT, |covered| = rho*T = 15, "
        f"support set == banked family: {ok_struct}/{len(cfgs)}")
    out(f"    => at m=1, d_x <= e = 1 forces the supports disjoint, hence "
        f"X_gamma = |S_gamma ^ (S_g u S_h)| = 0 identically at the "
        f"canonical W.")
    out("")

    # ------------------------------------------------------------- LAYER A
    out("[C] LAYER-A CONTROL (the mandate's built-in control): Q(Z,x) of "
        "bidegree (deg_x<=rho, deg_Z<=m)")
    nul_hist = {}
    allnz_ok = 0
    pencil_ok = 0
    for A, B, slopes, supp in [(c[0], c[1], c[2], c[3]) for c in cfgs]:
        nrows, nul, kb, allnz = layerA(slopes, supp)
        nul_hist[nul] = nul_hist.get(nul, 0) + 1
        if allnz:
            allnz_ok += 1
        # the predicted kernel vector is c_gamma = lead(A + gamma B)
        pred = [(A[RHO] + g * B[RHO]) % Q for g in slopes]
        if all(pred):
            # is pred in the kernel span?
            if nul >= 1:
                rr, piv, rk = rref([b[:] for b in kb] + [pred], len(slopes))
                rr2, piv2, rk2 = rref([b[:] for b in kb], len(slopes))
                if rk == rk2:
                    pencil_ok += 1
    out(f"    conditions (rho+1)*(T-m-1) = {(RHO+1)*(T_TGT-M-1)} on T = "
        f"{T_TGT} unknowns c_gamma")
    out(f"    nullity histogram over the {len(cfgs)} realized witnesses: "
        f"{dict(sorted(nul_hist.items()))}")
    out(f"    kernel with EVERY c_gamma != 0 : {allnz_ok}/{len(cfgs)}")
    out(f"    predicted kernel vector c_gamma = lead(A + gamma B) lies in the "
        f"kernel: {pencil_ok}/{len(cfgs)}")
    out(f"    >>> LAYER-A CONTROL: "
        f"{'PASS' if allnz_ok == len(cfgs) and pencil_ok == len(cfgs) else 'FAIL'}"
        f"  (nullity >= 1 required on a realized pencil)")
    out("")

    # ------------------------------------------------- W-layer + (NS-m) verdict
    out("[D] W-LAYER (BIV-H) AND THE (NS-1) MEASUREMENT")
    out("    variants of W (all contain S_g u S_h for a type-1 pair (g,h)):")
    out("      a=6  CANON   W = S_g u S_h            (d=0)  [the REALIZED a*]")
    out("      a=7  +x0     W = S_g u S_h u {x0}     (d=1)  x0 = the "
        "unsaturated point")
    out("      a=7  +1t2    W = S_g u S_h u {1 pt of a type-2 support}  (d=1)")
    out("      a=8  +2t2    W = ... u {2 pts of ONE type-2 support}     (d=2)")
    out("      a=8  +1+1    W = ... u {1 pt each of TWO type-2 supports}(d=2)")
    out("      a=8  +x0+1   W = ... u {x0, 1 pt of a type-2 support}    (d=2)")
    out("")

    agg = {}
    exemplars = []
    for A, B, slopes, supp, fam in cfgs:
        covered = set()
        for g in slopes:
            covered |= set(supp[g])
        x0 = [x for x in D if x not in covered]
        assert len(x0) == 1
        x0 = x0[0]
        slope_of = {}
        for g in slopes:
            for x in supp[g]:
                slope_of[x] = g
        for g, h in combinations(slopes, 2):
            base = sorted(set(supp[g]) | set(supp[h]))
            t2 = [c for c in slopes if c not in (g, h)]
            variants = [("a6_CANON", base)]
            variants.append(("a7_+x0", sorted(base + [x0])))
            for c in t2[:1]:
                variants.append(("a7_+1t2", sorted(base + [supp[c][0]])))
                variants.append(("a8_+2t2",
                                 sorted(base + [supp[c][0], supp[c][1]])))
                variants.append(("a8_+x0+1", sorted(base + [x0, supp[c][0]])))
            if len(t2) >= 2:
                variants.append(("a8_+1+1",
                                 sorted(base + [supp[t2[0]][0],
                                                supp[t2[1]][0]])))
            for name, W in variants:
                a = len(W)
                d = a - (4 * M + 2)
                Amap = {x: ([slope_of[x]] if x in slope_of else []) for x in W}
                ncols, nrows, kb = bivH(W, Amap, d)
                nul = len(kb)
                # admissible kernel element?
                adm = None
                cand = []
                for b in kb:
                    cand.append(b)
                for i in range(len(kb)):
                    for c in range(1, Q):
                        cand.append([(kb[i][k] + c * kb[(i + 1) % len(kb)][k]) % Q
                                     for k in range(ncols)])
                for v in cand:
                    Ht = Hcoeffs(v, d)
                    if all(any(f % Q for f in Hfibre(Ht, x)) for x in W):
                        adm = v
                        break
                key = (name, a, d)
                rec = agg.setdefault(key, dict(n=0, nul={}, adm=0,
                                               nsA=0, nsB=0, nsW=0, clos=0,
                                               tot2=0, split=0, maxRinm=0,
                                               maxX=0))
                rec["n"] += 1
                rec["nul"][nul] = rec["nul"].get(nul, 0) + 1
                if adm is None:
                    continue
                rec["adm"] += 1
                Ht = Hcoeffs(adm, d)
                # mu(x) from H(.,x) = c (Z - s_x)(Z - mu(x))
                mu = {}
                for x in W:
                    f = Hfibre(Ht, x)
                    if Amap[x]:
                        s = Amap[x][0]
                        # divide the Z-poly f by (Z - s)
                        n_ = pdeg(f)
                        acc = f[n_]
                        qz = [0] * max(n_, 1)
                        for i in range(n_ - 1, -1, -1):
                            qz[i] = acc
                            acc = (f[i] + s * acc) % Q
                        alpha = qz[1] if len(qz) > 1 else 0
                        beta = qz[0]
                        mu[x] = None if alpha % Q == 0 else \
                            (-beta * inv(alpha)) % Q
                    else:
                        mu[x] = "unsat"
                for c in slopes:
                    if set(supp[c]) <= set(W):
                        continue                    # type-1
                    rec["tot2"] += 1
                    hc = hgamma(Ht, c, d)
                    X = len(set(supp[c]) & set(W))
                    rts = rational_roots_with_mult(hc)
                    if rts is None:
                        rec["clos"] += 1            # h == 0 : type-1-like
                        continue
                    mult_all = sum(mm for _, mm in rts)
                    Rin = [r for r, _ in rts if r in set(W)]
                    Rin_m = sum(mm for r, mm in rts if r in set(W))
                    nonsplit = pdeg(hc) - mult_all
                    ng = sum(1 for x in W if mu[x] == c)
                    ovg = sum(1 for x in W if mu[x] == c and x in supp[c])
                    if mult_all <= d - M:
                        rec["nsA"] += 1             # (NS-m) root-count form
                    if nonsplit >= M:
                        rec["nsB"] += 1             # (NS-m) irreducible form
                    if Rin_m <= d - M:
                        rec["nsW"] += 1             # W-local form
                    if X <= d - M:
                        rec["clos"] += 1            # closure X <= need_X
                    if pdeg(hc) >= 1 and mult_all == pdeg(hc):
                        rec["split"] += 1           # splits completely over F_q
                    rec["maxRinm"] = max(rec["maxRinm"], Rin_m)
                    rec["maxX"] = max(rec["maxX"], X)
                    if len(exemplars) < 6 and name in ("a6_CANON", "a7_+x0"):
                        exemplars.append(
                            (name, a, d, c, hc, pdeg(hc), rts, X, Rin, Rin_m,
                             nonsplit, ng, ovg))

    out("    key:  n = (family,pair,variant) cases;  adm = cases with an "
        "ADMISSIBLE H (H(.,x) != 0 for every x in W);")
    out("          tot2 = type-2 slopes measured;  (NS-A) = "
        "#F_q-roots(h) <= d-m;  (NS-B) = nonsplit degree >= m;")
    out("          (NS-W) = #roots in W <= d-m;  CLOS = X_gamma <= d-m; "
        "SPLIT = h splits completely over F_q.")
    out("")
    hdr = (f"    {'variant':10s} {'a':>2s} {'d':>2s} {'n':>4s} {'adm':>4s} "
           f"{'nullity':>18s} {'tot2':>5s} {'NS-A':>5s} {'NS-B':>5s} "
           f"{'NS-W':>5s} {'CLOS':>5s} {'SPLIT':>5s} {'maxX':>4s}")
    out(hdr)
    for key in sorted(agg, key=lambda k: (k[1], k[0])):
        name, a, d = key
        r = agg[key]
        out(f"    {name:10s} {a:2d} {d:2d} {r['n']:4d} {r['adm']:4d} "
            f"{str(dict(sorted(r['nul'].items()))):>18s} {r['tot2']:5d} "
            f"{r['nsA']:5d} {r['nsB']:5d} {r['nsW']:5d} {r['clos']:5d} "
            f"{r['split']:5d} {r['maxX']:4d}")
    out("")
    out("    EXEMPLARS (h_gamma printed as coefficient list, low degree first):")
    for e in exemplars:
        (name, a, d, c, hc, dh, rts, X, Rin, Rin_m, nonsplit, ng, ovg) = e
        out(f"      {name} a={a} d={d} type-2 slope {c:2d}: h = {hc}  "
            f"deg={dh}  F_q-roots(mult)={rts}  X={X}  Rin={Rin} "
            f"Rin_mult={Rin_m}  nonsplit={nonsplit}  n_gamma={ng} ov={ovg}")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

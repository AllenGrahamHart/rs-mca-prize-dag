"""r36_lawcount_geom D1/D2 ladder: can a saturated a=7m-1 configuration with
POSITIVE count excess have nullity > 0 while satisfying
  (H1) W = S_g u S_h, two degree-rho supports split over D, |S_g ^ S_h| = m-1
  (H2) the (OV) pair caps: every pairwise support intersection <= m-1 ?

Constructive search at m=2 (rho=7, T=9, a=13, excess +2), two fields.
Stdlib only. Writes d2_ladder_results.txt INSIDE THIS DIRECTORY ONLY.
"""
import sys, itertools, random

sys.path.insert(0, "notes/pilots_20260811/r36_lawcount_geom")

OUT = "notes/pilots_20260811/r36_lawcount_geom/d2_ladder_results.txt"
LINES = []


def emit(s=""):
    LINES.append(str(s))
    print(s)


def nullity(rows, ncols, q):
    M = [r[:] for r in rows]
    rank = 0
    nrows = len(M)
    for col in range(ncols):
        piv = None
        for r in range(rank, nrows):
            if M[r][col] % q:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], q - 2, q)
        M[rank] = [(v * inv) % q for v in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col] % q:
                f = M[r][col]
                M[r] = [(a - f * b) % q for a, b in zip(M[r], M[rank])]
        rank += 1
    return ncols - rank, rank


def pdeg(p, q):
    d = -1
    for i, c in enumerate(p):
        if c % q:
            d = i
    return d


def pmul(a, b, q):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x % q == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % q
    return r


def peval(p, x, q):
    v = 0
    for c in reversed(p):
        v = (v * x + c) % q
    return v


def from_roots(roots, q):
    p = [1]
    for r in roots:
        p = pmul(p, [(-r) % q, 1], q)
    return p


def zeta_of_order(n, q):
    t = q - 1
    fac = []
    d = 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return pow(g, (q - 1) // n, q)
    raise RuntimeError


def subgroup(z, n, q):
    out, v = [], 1
    for _ in range(n):
        out.append(v)
        v = (v * z) % q
    return out


def layerA_nullity(W, Amap, m, rho, q):
    rows = []
    for x in W:
        for g in Amap[x]:
            row = []
            gp = 1
            for i in range(m + 1):
                xp = 1
                for t in range(rho + 1):
                    row.append((gp * xp) % q)
                    xp = (xp * x) % q
                gp = (gp * g) % q
            rows.append(row)
    n, r = nullity(rows, (m + 1) * (rho + 1), q)
    return n, r, len(rows)


def lagrange_weights(pts, q):
    """w_z = 1/prod_{z' != z}(z - z')."""
    w = {}
    for z in pts:
        d = 1
        for z2 in pts:
            if z2 != z:
                d = (d * (z - z2)) % q
        w[z] = pow(d, q - 2, q)
    return w


def solve_lin(rows, rhs, ncols, q):
    """Solve rows*v = rhs over F_q; return one solution + kernel basis, or None."""
    M = [r[:] + [b] for r, b in zip(rows, rhs)]
    pivots, rank = [], 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(M)):
            if M[r][col] % q:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], q - 2, q)
        M[rank] = [(v * inv) % q for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] % q:
                f = M[r][col]
                M[r] = [(a - f * b) % q for a, b in zip(M[r], M[rank])]
        pivots.append(col)
        rank += 1
    for r in range(rank, len(M)):
        if M[r][ncols] % q:
            return None, None
    sol = [0] * ncols
    for i, pc in enumerate(pivots):
        sol[pc] = M[i][ncols] % q
    free = [c for c in range(ncols) if c not in pivots]
    ker = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-M[i][fc]) % q
        ker.append(v)
    return sol, ker


# ================= the H1 / H1^H2 construction at m = 2 =================
# Q(Z,X) = (Z-g)(Z-h)C(X) + a(Z-h)sigma_g(X) - b(Z-g)sigma_h(X)
#   Q(g,.) = a(g-h) sigma_g ,  Q(h,.) = b(g-h) sigma_h     -> H1 by construction
#   x in V = S_g\S_h :  A_x = {g, h + b*sigma_h(x)/C(x)}
#   y in U = S_h\S_g :  A_y = {h, g - a*sigma_g(y)/C(y)}
#   p in S_g^S_h     :  A_p = {g, h}

def build_config(S_g, S_h, g, h, C, a, b, q):
    """Return (W, Amap) or None if the configuration is degenerate."""
    sg = from_roots(S_g, q)
    sh = from_roots(S_h, q)
    W = sorted(set(S_g) | set(S_h))
    V = [x for x in S_g if x not in S_h]
    U = [y for y in S_h if y not in S_g]
    P = [p for p in S_g if p in S_h]
    Amap = {}
    for x in V:
        c = peval(C, x, q)
        if c == 0:
            return None
        s = (h + b * peval(sh, x, q) * pow(c, q - 2, q)) % q
        if s == g:
            return None
        Amap[x] = sorted({g, s})
    for y in U:
        c = peval(C, y, q)
        if c == 0:
            return None
        s = (g - a * peval(sg, y, q) * pow(c, q - 2, q)) % q
        if s == h:
            return None
        Amap[y] = sorted({h, s})
    for p in P:
        if peval(C, p, q) == 0:
            return None
        Amap[p] = sorted({g, h})
    if any(len(v) != 2 for v in Amap.values()):
        return None
    return W, Amap


def audit(W, Amap, m, rho, q, S_g, S_h, g, h, T=9):
    slopes = sorted({s for x in W for s in Amap[x]})
    supp = {s: set(x for x in W if s in Amap[x]) for s in slopes}
    maxint = 0
    for s1, s2 in itertools.combinations(slopes, 2):
        maxint = max(maxint, len(supp[s1] & supp[s2]))
    h1 = (len(set(S_g)) == rho and len(set(S_h)) == rho
          and set(S_g) | set(S_h) == set(W)
          and len(set(S_g) & set(S_h)) == m - 1)
    return {
        "nslopes": len(slopes),
        "maxint": maxint,
        "H1": h1,
        "H2": maxint <= m - 1,
        "Tok": len(slopes) <= T,
        "supp_sizes": sorted((len(v) for v in supp.values()), reverse=True),
    }


def search_H1_only(q, rnd, tries=400):
    """H1 WITHOUT H2: group V's 6 points into 4 classes and U's into 3.
    Every coincidence is a LINEAR condition on C -> an explicit family."""
    m, rho = 2, 7
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    found = []
    for _ in range(tries):
        pts = rnd.sample(D, 13)
        p = pts[0]
        S_g = sorted([p] + pts[1:7])
        S_h = sorted([p] + pts[7:13])
        V = [x for x in S_g if x != p]
        U = [y for y in S_h if y != p]
        g, h = rnd.sample([c for c in range(1, q)], 2)
        sg, sh = from_roots(S_g, q), from_roots(S_h, q)
        # V groups: {V0,V1} {V2,V3} {V4} {V5}   U groups: {U0,U1} {U2,U3} {U4,U5}
        Vg = [[V[0], V[1]], [V[2], V[3]], [V[4]], [V[5]]]
        Ug = [[U[0], U[1]], [U[2], U[3]], [U[4], U[5]]]
        rows = []
        for grp in Vg:
            for i in range(1, len(grp)):
                x0, x1 = grp[0], grp[i]
                r = [0] * 8
                A0, A1 = peval(sh, x0, q), peval(sh, x1, q)
                for t in range(8):
                    r[t] = (A0 * pow(x1, t, q) - A1 * pow(x0, t, q)) % q
                rows.append(r)
        for grp in Ug:
            for i in range(1, len(grp)):
                y0, y1 = grp[0], grp[i]
                r = [0] * 8
                A0, A1 = peval(sg, y0, q), peval(sg, y1, q)
                for t in range(8):
                    r[t] = (A0 * pow(y1, t, q) - A1 * pow(y0, t, q)) % q
                rows.append(r)
        sol, ker = solve_lin(rows, [0] * len(rows), 8, q)
        if not ker:
            continue
        for _try in range(12):
            coef = [rnd.randrange(q) for _ in ker]
            C = [0] * 8
            for cc, kv in zip(coef, ker):
                for t in range(8):
                    C[t] = (C[t] + cc * kv[t]) % q
            if pdeg(C, q) < 0:
                continue
            a = rnd.randrange(1, q)
            b = rnd.randrange(1, q)
            r = build_config(S_g, S_h, g, h, C, a, b, q)
            if r is None:
                continue
            W, Amap = r
            au = audit(W, Amap, m, rho, q, S_g, S_h, g, h)
            if not (au["H1"] and au["Tok"]):
                continue
            n, rk, nrows = layerA_nullity(W, Amap, m, rho, q)
            if n > 0:
                found.append((S_g, S_h, g, h, C, a, b, n, au))
                if len(found) >= 6:
                    return found, len(ker)
    return found, None


def search_H1_H2(q, rnd, outer=900):
    """H1 AND H2: pair each of 5 V-points with a U-point (a slope may then
    meet S_g and S_h in one point each), leaving 2 singletons; 7 new slopes.
    Free: t_i = C(x_i) (i=1..5) and b; a is forced; ONE scalar condition."""
    m, rho, T = 2, 7, 9
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    found = []
    scanned = 0
    for _ in range(outer):
        pts = rnd.sample(D, 13)
        p = pts[0]
        S_g = sorted([p] + pts[1:7])
        S_h = sorted([p] + pts[7:13])
        V = [x for x in S_g if x != p]
        U = [y for y in S_h if y != p]
        rnd.shuffle(V)
        rnd.shuffle(U)
        g, h = rnd.sample([c for c in range(1, q)], 2)
        sg, sh = from_roots(S_g, q), from_roots(S_h, q)
        px = V[:5]
        py = U[:5]
        Z10 = px + py
        if len(set(Z10)) != 10:
            continue
        w = lagrange_weights(Z10, q)
        SH = [peval(sh, x, q) for x in px]
        SG = [peval(sg, y, q) for y in py]
        if any(v == 0 for v in SH + SG):
            continue
        gh = (g - h) % q
        b = rnd.randrange(1, q)
        t = [rnd.randrange(1, q) for _ in range(5)]
        for t0 in range(1, q):
            scanned += 1
            t[0] = t0
            den = [(gh * t[i] - b * SH[i]) % q for i in range(5)]
            if any(d == 0 for d in den):
                continue
            F = [0, 0]
            G = [0, 0]
            bad = False
            for k in (0, 1):
                f = 0
                gg = 0
                for i in range(5):
                    f = (f + w[px[i]] * pow(px[i], k, q) * t[i]) % q
                    gg = (gg + w[py[i]] * pow(py[i], k, q) * SG[i] * t[i]
                          * pow(den[i], q - 2, q)) % q
                F[k], G[k] = f, gg
            if (F[0] * G[1] - F[1] * G[0]) % q:
                continue
            if G[0] % q == 0:
                continue
            a = (-F[0] * pow(G[0], q - 2, q)) % q
            if a == 0:
                continue
            # reconstruct C from its 10 prescribed values
            vals = {}
            for i in range(5):
                vals[px[i]] = t[i]
                vals[py[i]] = (a * SG[i] * t[i] * pow(den[i], q - 2, q)) % q
            rows, rhs = [], []
            for zz, vv in vals.items():
                rows.append([pow(zz, k, q) for k in range(8)])
                rhs.append(vv)
            C, ker = solve_lin(rows, rhs, 8, q)
            if C is None:
                continue
            r = build_config(S_g, S_h, g, h, C, a, b, q)
            if r is None:
                continue
            W, Amap = r
            au = audit(W, Amap, m, rho, q, S_g, S_h, g, h)
            if not (au["H1"] and au["H2"] and au["Tok"]):
                continue
            n, rk, nrows = layerA_nullity(W, Amap, m, rho, q)
            if n > 0:
                found.append((S_g, S_h, g, h, C, a, b, n, au, W, Amap))
                if len(found) >= 4:
                    return found, scanned
    return found, scanned


def control_H1H2_random(q, rnd, trials=60):
    """Distribution control (R3(c)): saturated configs of the SAME H1^H2 shape
    built WITHOUT solving the condition -> nullity histogram."""
    m, rho = 2, 7
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    hist = {}
    made = 0
    guard = 0
    while made < trials and guard < 4000:
        guard += 1
        pts = rnd.sample(D, 13)
        p = pts[0]
        S_g = sorted([p] + pts[1:7])
        S_h = sorted([p] + pts[7:13])
        V = [x for x in S_g if x != p]
        U = [y for y in S_h if y != p]
        g, h = rnd.sample([c for c in range(1, q)], 2)
        others = rnd.sample([c for c in range(1, q) if c not in (g, h)], 7)
        Amap = {p: sorted({g, h})}
        okc = True
        for i, x in enumerate(V):
            Amap[x] = sorted({g, others[i]})
        for i, y in enumerate(U):
            Amap[y] = sorted({h, others[i]})   # pairs (V_i,U_i) share a slope
        W = sorted(set(S_g) | set(S_h))
        au = audit(W, Amap, m, rho, q, S_g, S_h, g, h)
        if not (au["H2"] and au["Tok"]):
            continue
        n, rk, nrows = layerA_nullity(W, Amap, m, rho, q)
        hist[n] = hist.get(n, 0) + 1
        made += 1
    return hist, made


def O_budget(S_g, S_h, g, h, C, a, b, q):
    """(SAT2) global block completion: O = sum_gamma (rho - u_gamma) over the
    supported slopes, u_gamma = #distinct roots of Q(gamma,.) inside D."""
    rho = 7
    z = zeta_of_order(32, q)
    D = set(subgroup(z, 32, q))
    sg, sh = from_roots(S_g, q), from_roots(S_h, q)
    W = sorted(set(S_g) | set(S_h))
    slopes = set()
    r = build_config(S_g, S_h, g, h, C, a, b, q)
    W, Amap = r
    for x in W:
        slopes |= set(Amap[x])
    O = 0
    per = []
    for s in sorted(slopes):
        u = 0
        for x in D:
            v = ((s - g) * (s - h) % q * peval(C, x, q)
                 + a * (s - h) * peval(sg, x, q)
                 - b * (s - g) * peval(sh, x, q)) % q
            if v == 0:
                u += 1
        per.append(u)
        O += rho - u
    return O, per


def main():
    emit("=" * 78)
    emit("D1/D2 LADDER: does the endpoint geometry force nullity 0 at m=2?")
    emit("m=2: rho=7, T=9, a=13, 26 rows on 24 unknowns, count excess +2")
    emit("=" * 78)
    for q in (97, 193):
        emit()
        emit("### FIELD F_%d" % q)
        rnd = random.Random(20260811 + q)

        emit()
        emit("[RUNG H1 ALONE]  W = S_g u S_h, both supports degree-rho and")
        emit("                 split over D, |S_g ^ S_h| = m-1 = 1")
        f1, kdim = search_H1_only(q, rnd)
        if f1:
            emit("  COUNTEREXAMPLES FOUND: %d  (kernel dim of the coincidence")
            emit("  system on C = %s, so the family is >= %s-dimensional in C alone)"
                 % (kdim, kdim))
            emit("  nullity values: %s" % sorted({t[7] for t in f1}))
            S_g, S_h, g, h, C, a, b, n, au = f1[0]
            emit("  exhibit: S_g=%s" % S_g)
            emit("           S_h=%s" % S_h)
            emit("           g=%d h=%d a=%d b=%d C=%s" % (g, h, a, b, C))
            emit("           slopes=%d  max pair-int=%d (cap 1)  H1=%s H2=%s"
                 % (au["nslopes"], au["maxint"], au["H1"], au["H2"]))
            emit("           support sizes = %s" % au["supp_sizes"])
            emit("           LAYER-A NULLITY = %d  (count excess +2)" % n)
        else:
            emit("  none found")

        emit()
        emit("[RUNG H1 AND H2]  additionally every pairwise support")
        emit("                  intersection <= m-1 = 1 (the (OV) caps)")
        f2, scanned = search_H1_H2(q, rnd)
        emit("  scalar condition scanned at %d parameter points" % scanned)
        if f2:
            emit("  COUNTEREXAMPLES FOUND: %d" % len(f2))
            emit("  nullity values: %s" % sorted({t[7] for t in f2}))
            S_g, S_h, g, h, C, a, b, n, au, W, Amap = f2[0]
            emit("  EXHIBIT (H1 ^ H2, saturated, positive excess, nullity > 0):")
            emit("           S_g=%s" % S_g)
            emit("           S_h=%s" % S_h)
            emit("           S_g ^ S_h = %s   |W| = %d"
                 % (sorted(set(S_g) & set(S_h)), len(W)))
            emit("           g=%d h=%d a=%d b=%d" % (g, h, a, b))
            emit("           C = %s" % C)
            emit("           A_x: %s" % {x: Amap[x] for x in W})
            emit("           #slopes=%d (T=9)  max pair-int=%d (cap 1)  H1=%s H2=%s"
                 % (au["nslopes"], au["maxint"], au["H1"], au["H2"]))
            emit("           support sizes = %s" % au["supp_sizes"])
            emit("           LAYER-A NULLITY = %d" % n)
            O, per = O_budget(S_g, S_h, g, h, C, a, b, q)
            emit("           NEXT RUNG: O = sum(rho-u_gamma) = %d  [(SAT2) cap"
                 " m-1 = 1] -> %s" % (O, "VIOLATED" if O > 1 else "ok"))
            emit("           per-slope domain-root counts u_gamma = %s (rho=7)"
                 % per)
        else:
            emit("  none found")

        emit()
        emit("[CONTROL] same H1^H2 SHAPE, condition NOT solved (R3(c) distribution)")
        hist, made = control_H1H2_random(q, rnd)
        emit("  %d configs: nullity histogram %s" % (made, dict(sorted(hist.items()))))

    with open(OUT, "w") as f:
        f.write("\n".join(LINES) + "\n")


main()

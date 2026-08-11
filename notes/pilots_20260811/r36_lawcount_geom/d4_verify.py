"""r36_lawcount_geom D4 verification: independent second path on the
H1^H2 exhibit, and the honest count for the H1-only family.

Path 1 (d2/d3): nullity of E_I by Gaussian elimination.
Path 2 (here):  build the closed-form biform Q, check it satisfies H1 as
                polynomials and vanishes on every incidence, then check its
                24-vector is annihilated by E_I row by row.
Two fields. Stdlib only. Writes d4_verify_results.txt INSIDE THIS DIR ONLY.
"""
import itertools, random

OUT = "notes/pilots_20260811/r36_lawcount_geom/d4_verify_results.txt"
LINES = []


def emit(s=""):
    LINES.append(str(s))
    print(s)


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


def padd(a, b, q):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q
            for i in range(n)]


def pscale(a, c, q):
    return [(x * c) % q for x in a]


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


def pdeg(p, q):
    d = -1
    for i, c in enumerate(p):
        if c % q:
            d = i
    return d


def zeta_of_order(n, q):
    t, fac, d = q - 1, [], 2
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


def subgroup(z, n, q):
    out, v = [], 1
    for _ in range(n):
        out.append(v)
        v = (v * z) % q
    return out


def nullity(rows, ncols, q):
    M = [r[:] for r in rows]
    rank = 0
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
        rank += 1
    return ncols - rank, rank


def layerA_rows(W, Amap, m, rho, q):
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
    return rows


def solve_lin(rows, rhs, ncols, q):
    M = [r[:] + [b] for r, b in zip(rows, rhs)]
    piv, rank = [], 0
    for col in range(ncols):
        pr = None
        for r in range(rank, len(M)):
            if M[r][col] % q:
                pr = r
                break
        if pr is None:
            continue
        M[rank], M[pr] = M[pr], M[rank]
        iv = pow(M[rank][col], q - 2, q)
        M[rank] = [(v * iv) % q for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] % q:
                ff = M[r][col]
                M[r] = [(aa - ff * bb) % q for aa, bb in zip(M[r], M[rank])]
        piv.append(col)
        rank += 1
    if any(M[r][ncols] % q for r in range(rank, len(M))):
        return None, None
    sol = [0] * ncols
    for i, pc in enumerate(piv):
        sol[pc] = M[i][ncols] % q
    free = [c for c in range(ncols) if c not in piv]
    ker = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        ker.append(v)
    return sol, ker


def make_config(S_g, S_h, g, h, C, a, b, q):
    sg, sh = from_roots(S_g, q), from_roots(S_h, q)
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


def biform_coeffs(S_g, S_h, g, h, C, a, b, q):
    """Q(Z,X) = (Z-g)(Z-h)C + a(Z-h)sigma_g - b(Z-g)sigma_h,
    returned as P[i] = coefficient polynomial of Z^i (i = 0,1,2)."""
    sg, sh = from_roots(S_g, q), from_roots(S_h, q)
    P = [[0] * 8 for _ in range(3)]

    def add(i, poly, c):
        for t, v in enumerate(poly):
            P[i][t] = (P[i][t] + c * v) % q
    # (Z-g)(Z-h) = Z^2 - (g+h)Z + gh
    add(2, C, 1)
    add(1, C, -(g + h))
    add(0, C, g * h)
    # a(Z-h)sigma_g
    add(1, sg, a)
    add(0, sg, -a * h)
    # -b(Z-g)sigma_h
    add(1, sh, -b)
    add(0, sh, b * g)
    return P


def search_h1h2(q, seed, want):
    rho, m = 7, 2
    out = []
    rnd = random.Random(seed)
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    for _ in range(900):
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
        px, py = V[:5], U[:5]
        Z10 = px + py
        w = {}
        for zz in Z10:
            d = 1
            for z2 in Z10:
                if z2 != zz:
                    d = (d * (zz - z2)) % q
            w[zz] = pow(d, q - 2, q)
        SH = [peval(sh, x, q) for x in px]
        SG = [peval(sg, y, q) for y in py]
        if any(v == 0 for v in SH + SG):
            continue
        gh = (g - h) % q
        b = rnd.randrange(1, q)
        t = [rnd.randrange(1, q) for _ in range(5)]
        for t0 in range(1, q):
            t[0] = t0
            den = [(gh * t[i] - b * SH[i]) % q for i in range(5)]
            if any(d == 0 for d in den):
                continue
            F, G_ = [0, 0], [0, 0]
            for k in (0, 1):
                f = gg = 0
                for i in range(5):
                    f = (f + w[px[i]] * pow(px[i], k, q) * t[i]) % q
                    gg = (gg + w[py[i]] * pow(py[i], k, q) * SG[i] * t[i]
                          * pow(den[i], q - 2, q)) % q
                F[k], G_[k] = f, gg
            if (F[0] * G_[1] - F[1] * G_[0]) % q or G_[0] % q == 0:
                continue
            a = (-F[0] * pow(G_[0], q - 2, q)) % q
            if a == 0:
                continue
            vals = {}
            for i in range(5):
                vals[px[i]] = t[i]
                vals[py[i]] = (a * SG[i] * t[i] * pow(den[i], q - 2, q)) % q
            rows = [[pow(zz, k, q) for k in range(8)] for zz in vals]
            C, _ = solve_lin(rows, list(vals.values()), 8, q)
            if C is None:
                continue
            r = make_config(S_g, S_h, g, h, C, a, b, q)
            if r is None:
                continue
            W, Amap = r
            sl = sorted({s for x in W for s in Amap[x]})
            supp = {s: set(x for x in W if s in Amap[x]) for s in sl}
            mi = max(len(supp[s1] & supp[s2])
                     for s1, s2 in itertools.combinations(sl, 2))
            h1 = (len(set(S_g)) == 7 and len(set(S_h)) == 7
                  and set(S_g) | set(S_h) == set(W)
                  and len(set(S_g) & set(S_h)) == 1)
            if not (h1 and mi <= 1 and len(sl) == 9):
                continue
            n, _ = nullity(layerA_rows(W, Amap, 2, 7, q), 24, q)
            if n > 0:
                out.append((S_g, S_h, g, h, C, a, b, W, Amap, n))
                if len(out) >= want:
                    return out
    return out


def search_h1_only(q, seed, tries=400):
    """Honest count for the H1-only family (the d2 print was mangled)."""
    rho, m = 7, 2
    rnd = random.Random(seed)
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    found = 0
    kdims = set()
    nulls = {}
    for _ in range(tries):
        pts = rnd.sample(D, 13)
        p = pts[0]
        S_g = sorted([p] + pts[1:7])
        S_h = sorted([p] + pts[7:13])
        V = [x for x in S_g if x != p]
        U = [y for y in S_h if y != p]
        g, h = rnd.sample([c for c in range(1, q)], 2)
        sg, sh = from_roots(S_g, q), from_roots(S_h, q)
        Vg = [[V[0], V[1]], [V[2], V[3]], [V[4]], [V[5]]]
        Ug = [[U[0], U[1]], [U[2], U[3]], [U[4], U[5]]]
        rows = []
        for grp, base in ((Vg, sh), (Ug, sg)):
            for gp in grp:
                for i in range(1, len(gp)):
                    z0, z1 = gp[0], gp[i]
                    A0, A1 = peval(base, z0, q), peval(base, z1, q)
                    rows.append([(A0 * pow(z1, t, q) - A1 * pow(z0, t, q)) % q
                                 for t in range(8)])
        sol, ker = solve_lin(rows, [0] * len(rows), 8, q)
        if not ker:
            continue
        kdims.add(len(ker))
        for _try in range(12):
            C = [0] * 8
            for cc, kv in zip([rnd.randrange(q) for _ in ker], ker):
                for t in range(8):
                    C[t] = (C[t] + cc * kv[t]) % q
            if pdeg(C, q) < 0:
                continue
            a, b = rnd.randrange(1, q), rnd.randrange(1, q)
            r = make_config(S_g, S_h, g, h, C, a, b, q)
            if r is None:
                continue
            W, Amap = r
            sl = sorted({s for x in W for s in Amap[x]})
            if len(sl) > 9:
                continue
            h1 = (set(S_g) | set(S_h) == set(W)
                  and len(set(S_g) & set(S_h)) == 1)
            if not h1:
                continue
            n, _ = nullity(layerA_rows(W, Amap, 2, 7, q), 24, q)
            nulls[n] = nulls.get(n, 0) + 1
            if n > 0:
                found += 1
    return found, sum(nulls.values()), kdims, nulls


def main():
    emit("=" * 78)
    emit("D4 VERIFICATION: independent second path on the H1^H2 exhibit")
    emit("=" * 78)
    for q in (97, 193):
        emit()
        emit("### F_%d" % q)
        sols = search_h1h2(q, 20260811 + q, 1)
        if not sols:
            emit("  no exhibit re-derived")
            continue
        S_g, S_h, g, h, C, a, b, W, Amap, n = sols[0]
        P = biform_coeffs(S_g, S_h, g, h, C, a, b, q)
        sg, sh = from_roots(S_g, q), from_roots(S_h, q)
        # H1 as polynomial identities
        Qg = [0] * 8
        Qh = [0] * 8
        for i in range(3):
            for t in range(8):
                Qg[t] = (Qg[t] + P[i][t] * pow(g, i, q)) % q
                Qh[t] = (Qh[t] + P[i][t] * pow(h, i, q)) % q
        tgt_g = pscale(sg, a * (g - h), q)
        tgt_h = pscale(sh, b * (g - h), q)
        okg = all((Qg[t] - (tgt_g[t] if t < len(tgt_g) else 0)) % q == 0
                  for t in range(8))
        okh = all((Qh[t] - (tgt_h[t] if t < len(tgt_h) else 0)) % q == 0
                  for t in range(8))
        emit("  Q(g,.) == a(g-h)*sigma_g as polynomials : %s   (deg %d, roots"
             " = S_g, all in mu_32)" % (okg, pdeg(Qg, q)))
        emit("  Q(h,.) == b(g-h)*sigma_h as polynomials : %s   (deg %d, roots"
             " = S_h, all in mu_32)" % (okh, pdeg(Qh, q)))
        # incidences
        bad = 0
        for x in W:
            for s in Amap[x]:
                v = 0
                for i in range(3):
                    v = (v + peval(P[i], x, q) * pow(s, i, q)) % q
                if v:
                    bad += 1
        nI = sum(len(v) for v in Amap.values())
        emit("  Q vanishes on all %d incidences: %s (%d failures)"
             % (nI, bad == 0, bad))
        # kernel membership against E_I, row by row (independent path)
        vec = []
        for i in range(3):
            vec.extend(P[i])
        rows = layerA_rows(W, Amap, 2, 7, q)
        resid = max(sum(r[k] * vec[k] for k in range(24)) % q for r in rows)
        nz = any(c % q for c in vec)
        emit("  E_I * vec(Q) = 0 on all %d rows: %s ; Q nonzero: %s"
             % (len(rows), resid == 0, nz))
        emit("  nullity(E_I) from path 1 = %d ; a kernel element exhibited"
             " in closed form by path 2" % n)
        emit("  count excess = 26 - 24 = +2 (positive), saturation |A_x| = 2"
             " for all %d points" % len(W))
        emit()
        f, tot, kd, hist = search_h1_only(q, 90000 + q)
        emit("  [H1-ONLY family, honest count] %d nullity>0 out of %d admissible"
             " configurations built; nullity histogram %s"
             % (f, tot, dict(sorted(hist.items()))))
        emit("  coincidence-system kernel dim on C: %s (family dimension in C)"
             % sorted(kd))
    with open(OUT, "w") as f:
        f.write("\n".join(LINES) + "\n")


main()

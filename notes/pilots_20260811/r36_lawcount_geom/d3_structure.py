"""r36_lawcount_geom D3: the structure theorem for the layer-A failure locus.

(LA-PADE)  nullity(E_I) = dim of the simultaneous Pade/Hankel kernel
           K_j = {P in F[X]_{<=rho} : deg(E_j P mod sigma_W) <= rho},
           E_j = the interpolant on W of x -> e_j(A_x).
Verified here together with the reduced-basis degree formula
           dim K_j = max(0, 4m-d_j) + max(0, 4m-d'_j),  d_j + d'_j = a-1,
and applied to classify the binomial/invariant subfamily.

Stdlib only. Writes d3_structure_results.txt INSIDE THIS DIRECTORY ONLY.
"""
import itertools, random

OUT = "notes/pilots_20260811/r36_lawcount_geom/d3_structure_results.txt"
LINES = []


def emit(s=""):
    LINES.append(str(s))
    print(s)


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


def kernel_basis(rows, ncols, q):
    M = [r[:] for r in rows]
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
    free = [c for c in range(ncols) if c not in pivots]
    out = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-M[i][fc]) % q
        out.append(v)
    return out


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


def pmod(a, b, q):
    a = a[:]
    db = pdeg(b, q)
    inv = pow(b[db], q - 2, q)
    da = pdeg(a, q)
    while da >= db:
        f = (a[da] * inv) % q
        for i in range(db + 1):
            a[da - db + i] = (a[da - db + i] - f * b[i]) % q
        da = pdeg(a, q)
    return a[:db]


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


def interpolate(pts, q):
    xs = [x for x, _ in pts]
    sig = from_roots(xs, q)
    res = [0] * len(xs)
    for x, y in pts:
        quo = [0] * len(xs)
        rem = 0
        for i in range(len(sig) - 1, -1, -1):
            cur = (sig[i] + rem * x) % q
            if i > 0:
                quo[i - 1] = cur
            rem = cur
        f = (y * pow(peval(quo, x, q), q - 2, q)) % q
        for i in range(len(quo)):
            res[i] = (res[i] + f * quo[i]) % q
    return res


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


def layerA(W, Amap, m, rho, q):
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
    return n, rows


def esym_interpolants(W, Amap, m, q):
    out = []
    for j in range(1, m + 1):
        pts = []
        for x in W:
            e = 0
            for comb in itertools.combinations(Amap[x], j):
                t = 1
                for c in comb:
                    t = (t * c) % q
                e = (e + t) % q
            pts.append((x, e % q))
        out.append(interpolate(pts, q))
    return out


def K_rows(E, sig, rho, a, q):
    rows_by_t = []
    for t in range(rho + 1):
        prod = pmod(pmul(E, [0] * t + [1], q), sig, q)
        prod = prod + [0] * (a - len(prod))
        rows_by_t.append([prod[d] % q for d in range(rho + 1, a)])
    nc = a - rho - 1
    return [[rows_by_t[t][d] for t in range(rho + 1)] for d in range(nc)]


def pade_report(W, Amap, m, rho, q, tag):
    a = len(W)
    sig = from_roots(W, q)
    Es = esym_interpolants(W, Amap, m, q)
    allrows = []
    dims, dj_list = [], []
    for E in Es:
        rows = K_rows(E, sig, rho, a, q)
        allrows.extend(rows)
        dimK, _ = nullity(rows, rho + 1, q)
        dims.append(dimK)
        # minimal reduced-basis degree d_j
        dmin = None
        for d in range(0, a):
            r2 = []
            for t in range(d + 1):
                prod = pmod(pmul(E, [0] * t + [1], q), sig, q)
                prod = prod + [0] * (a - len(prod))
                r2.append([prod[k] % q for k in range(d + 1, a)])
            nc = a - d - 1
            mat = [[r2[t][k] for t in range(d + 1)] for k in range(nc)] if nc > 0 else []
            nn, _ = nullity(mat, d + 1, q) if mat else (d + 1, 0)
            if nn > 0:
                dmin = d
                break
        dj_list.append(dmin)
    joint, _ = nullity(allrows, rho + 1, q)
    direct, _ = layerA(W, Amap, m, rho, q)
    pred = []
    for d in dj_list:
        dp = a - d            # d_j + d'_j = deg sigma_W = a = 7m-1  (R2.2)
        pred.append(max(0, (rho + 1) - d) + max(0, (rho + 1) - dp))
    emit("  [%s] m=%d q=%d a=%d rho=%d" % (tag, m, q, a, rho))
    emit("       direct nullity(E_I) = %d ; (LA-PADE) joint kernel = %d ; AGREE %s"
         % (direct, joint, direct == joint))
    emit("       per-j: d_j = %s ; dim K_j measured = %s ; formula = %s ; AGREE %s"
         % (dj_list, dims, pred, dims == pred))
    return direct, joint, dims == pred


# ---------------- configurations ----------------

def cfg_fence(q):
    m, rho = 2, 7
    z = zeta_of_order(32, q)
    U = subgroup(pow(z, 2, q), 16, q)
    H = subgroup(pow(z, 4, q), 8, q)
    W = sorted(U)[:13]
    eta = next(c for c in range(2, q) if c not in H)
    G = sorted(set(H) | {eta})
    Amap = {x: [g for g in G if (pow(g, 2, q) - pow(x, 4, q)) % q == 0] for x in W}
    return W, Amap, m, rho


def cfg_genfence(m, q):
    N, rho = 16 * m, 4 * m - 1
    z = zeta_of_order(N, q)
    D = subgroup(z, N, q)
    fib = {}
    for x in D:
        fib.setdefault(pow(x, 2 * m, q), []).append(x)
    vals = sorted(fib)[:4]
    W = sorted(x for v in vals for x in fib[v])[: 7 * m - 1]
    G = sorted({g for v in vals for g in D if pow(g, m, q) == v})
    eta = next(c for c in range(2, q) if pow(c, m, q) not in vals)
    G = sorted(set(G) | {eta})
    Amap = {x: [g for g in G if (pow(g, m, q) - pow(x, 2 * m, q)) % q == 0] for x in W}
    return W, Amap, m, rho


def cfg_m1_banked(q=17):
    m, rho = 1, 3
    D = list(range(1, q))

    def Q(Y, X):
        return (pow(X, 3, q) + (9 + 4 * Y) * pow(X, 2, q) + 12 * Y * X + 7) % q

    supp = {Y: [x for x in D if Q(Y, x) == 0] for Y in range(q)}
    supp = {Y: v for Y, v in supp.items() if len(v) == 3}
    sl = sorted(supp)
    W = sorted(set(supp[sl[0]]) | set(supp[sl[1]]))
    Amap = {x: [g for g in sl if x in supp[g]] for x in W}
    return W, Amap, m, rho


def cfg_h1h2(q, seed, want=1):
    """Re-derive H1^H2 exhibits (same construction as d2_ladder)."""
    m, rho = 2, 7
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
            rhs = list(vals.values())
            M = [r[:] + [bb] for r, bb in zip(rows, rhs)]
            piv, rank = [], 0
            for col in range(8):
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
            if any(M[r][8] % q for r in range(rank, len(M))):
                continue
            C = [0] * 8
            for i, pc in enumerate(piv):
                C[pc] = M[i][8] % q
            W = sorted(set(S_g) | set(S_h))
            Amap = {}
            ok = True
            for x in V:
                c = peval(C, x, q)
                if c == 0:
                    ok = False
                    break
                s = (h + b * peval(sh, x, q) * pow(c, q - 2, q)) % q
                Amap[x] = sorted({g, s})
            if not ok:
                continue
            for y in U:
                c = peval(C, y, q)
                if c == 0:
                    ok = False
                    break
                s = (g - a * peval(sg, y, q) * pow(c, q - 2, q)) % q
                Amap[y] = sorted({h, s})
            if not ok:
                continue
            Amap[p] = sorted({g, h})
            if any(len(v) != 2 for v in Amap.values()):
                continue
            sl = sorted({s for x in W for s in Amap[x]})
            supp = {s: set(x for x in W if s in Amap[x]) for s in sl}
            mi = max(len(supp[s1] & supp[s2])
                     for s1, s2 in itertools.combinations(sl, 2))
            if len(sl) != 9 or mi > 1:
                continue
            n, _ = layerA(W, Amap, m, rho, q)
            if n > 0:
                out.append((W, Amap, m, rho, (S_g, S_h, g, h, C, a, b)))
                if len(out) >= want:
                    return out
    return out


def O_of(sol, q):
    """(SAT2) block-completion budget O = sum_gamma (rho - u_gamma)."""
    W, Amap, m, rho, (S_g, S_h, g, h, C, a, b) = sol
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    sg, sh = from_roots(S_g, q), from_roots(S_h, q)
    sl = sorted({s for x in W for s in Amap[x]})
    O = 0
    us = []
    for s in sl:
        u = 0
        for x in D:
            v = ((s - g) * (s - h) % q * peval(C, x, q)
                 + a * (s - h) * peval(sg, x, q)
                 - b * (s - g) * peval(sh, x, q)) % q
            if v == 0:
                u += 1
        us.append(u)
        O += rho - u
    return O, us


def binomial_family_table():
    """Which Q_0 = Z^m - c X^k support the fence construction, and at what
    nullity?  Need fibre size f = gcd(k,16m), #fibres F = ceil((7m-1)/f) <= 4
    (so that m*F <= T = 4m+1), and k <= rho = 4m-1; nullity = rho-k+1."""
    emit("  m   rho   admissible k (f=gcd(k,16m), F=#fibres, nullity=4m-k)")
    from math import gcd
    for m in range(2, 13):
        rho, T = 4 * m - 1, 4 * m + 1
        ok = []
        for k in range(1, rho + 1):
            f = gcd(k, 16 * m)
            F = -(-(7 * m - 1) // f)
            if F <= 4 and m * F <= T and f * F >= 7 * m - 1:
                ok.append((k, f, F, 4 * m - k))
        emit("  %-3d %-4d %s" % (m, rho, ok if ok else "NONE"))


def main():
    emit("=" * 78)
    emit("D3 STRUCTURE: the layer-A failure locus")
    emit("=" * 78)
    emit()
    emit("[A] (LA-PADE) + the reduced-basis degree formula, on every")
    emit("    configuration in this round")
    agree = []
    for q in (97, 193):
        W, A, m, rho = cfg_fence(q)
        agree.append(pade_report(W, A, m, rho, q, "Codex fence"))
    for m in (2, 3):
        for q in (97, 193):
            W, A, mm, rho = cfg_genfence(m, q)
            agree.append(pade_report(W, A, mm, rho, q, "genfence Z^%d-X^%d" % (m, 2 * m)))
    W, A, m, rho = cfg_m1_banked()
    agree.append(pade_report(W, A, m, rho, 17, "m=1 banked (BRS1)"))
    h1h2 = {}
    sols = {}
    for q in (97, 193):
        r = cfg_h1h2(q, 20260811 + q, want=6)
        sols[q] = r
        if r:
            W, A, m, rho, data = r[0]
            h1h2[q] = (W, A, data)
            agree.append(pade_report(W, A, m, rho, q, "H1^H2 exhibit"))
    emit("  formula agreement on all %d configurations: %s"
         % (len(agree), all(x[2] for x in agree)))
    emit("  direct == (LA-PADE) on all %d: %s"
         % (len(agree), all(x[0] == x[1] for x in agree)))
    emit()
    emit("[B] IS EVERY COUNTEREXAMPLE OF THE INVARIANT / SUBGROUP TYPE?")
    for q in (97, 193):
        if q not in h1h2:
            continue
        W, A, data = h1h2[q]
        m, rho = 2, 7
        n, rows = layerA(W, A, m, rho, q)
        kb = kernel_basis(rows, (m + 1) * (rho + 1), q)
        emit("  q=%d  nullity=%d  kernel biform coefficient blocks (P_0|P_1|P_2):"
             % (q, n))
        v = kb[0]
        P = [v[i * (rho + 1):(i + 1) * (rho + 1)] for i in range(m + 1)]
        for i, p in enumerate(P):
            emit("     P_%d = %s   (deg %d)" % (i, p, pdeg(p, q)))
        binom = (pdeg(P[1], q) < 0)
        emit("     P_1 == 0 (required for the binomial form A(X)(Z^m - cX^k))? %s"
             % binom)
        emit("     -> the exhibit is %s of invariant/subgroup type"
             % ("" if binom else "NOT"))
        sl = sorted({s for x in W for s in A[x]})
        z = zeta_of_order(32, q)
        D = set(subgroup(z, 32, q))
        emit("     slopes inside the domain mu_32: %d of %d"
             % (len([s for s in sl if s in D]), len(sl)))
    emit()
    emit("[C] THE BINOMIAL SUBFAMILY, CLASSIFIED")
    binomial_family_table()
    emit()
    emit("[D] THE NEXT RUNG: global block completion (SAT2), O <= m-1 = 1")
    emit("    O-budget DISTRIBUTION over the H1^H2 counterexamples found")
    for q in (97, 193):
        Os = []
        for s in sols.get(q, []):
            O, us = O_of(s, q)
            Os.append(O)
        emit("  q=%d  n=%d exhibits  O values = %s   min=%s  [cap 1]"
             % (q, len(Os), sorted(Os), min(Os) if Os else "-"))
        if sols.get(q):
            O, us = O_of(sols[q][0], q)
            emit("       per-slope domain-root counts u_gamma of exhibit #1 = %s"
                 " (rho = 7, need 7 for each)" % us)
    emit()
    emit("[E] CONTROL: the failure locus is thin - random saturated configs")
    for q in (97, 193):
        rnd = random.Random(7 + q)
        z = zeta_of_order(32, q)
        D = subgroup(z, 32, q)
        hist = {}
        for _ in range(60):
            W = sorted(rnd.sample(D, 13))
            G = rnd.sample([c for c in range(1, q)], 9)
            A = {x: sorted(rnd.sample(G, 2)) for x in W}
            n, _ = layerA(W, A, 2, 7, q)
            hist[n] = hist.get(n, 0) + 1
        emit("  q=%d  60 random saturated: nullity histogram %s"
             % (q, dict(sorted(hist.items()))))
    with open(OUT, "w") as f:
        f.write("\n".join(LINES) + "\n")


main()

"""r36_lawcount_geom D1/D2 core: layer-A nullity, the Pade reduction, the
fence replay, and the generalized fence Z^m - X^{2m} at m = 2..6.

Stdlib only. Writes d1_core_results.txt INSIDE THIS DIRECTORY ONLY.
"""
import sys, itertools

OUT = "notes/pilots_20260811/r36_lawcount_geom/d1_core_results.txt"
LINES = []


def emit(s=""):
    LINES.append(str(s))
    print(s)


# ---------- F_q linear algebra ----------

def nullity(rows, ncols, q):
    """Nullity of the matrix with the given rows over F_q."""
    M = [r[:] for r in rows]
    rank = 0
    piv_col = 0
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
        if rank == nrows:
            break
    return ncols - rank, rank


def kernel_basis(rows, ncols, q):
    """Basis of the kernel of the matrix (list of vectors in F_q^ncols)."""
    M = [r[:] for r in rows]
    nrows = len(M)
    pivots = []
    rank = 0
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
        pivots.append(col)
        rank += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis


# ---------- polynomials over F_q (coefficient lists, low degree first) ----------

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
    if db < 0:
        raise ZeroDivisionError
    inv = pow(b[db], q - 2, q)
    da = pdeg(a, q)
    while da >= db:
        f = (a[da] * inv) % q
        for i in range(db + 1):
            a[da - db + i] = (a[da - db + i] - f * b[i]) % q
        da = pdeg(a, q)
    return a[: db] if db > 0 else []


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
    """Lagrange interpolation through (x, y) pairs; returns coefficient list."""
    xs = [x for x, _ in pts]
    sig = from_roots(xs, q)
    res = [0] * len(xs)
    for x, y in pts:
        # sig / (X - x)
        quo = [0] * len(xs)
        rem = 0
        for i in range(len(sig) - 1, -1, -1):
            cur = (sig[i] + rem * x) % q
            if i > 0:
                quo[i - 1] = cur
            rem = cur
        den = peval(quo, x, q)
        f = (y * pow(den, q - 2, q)) % q
        for i in range(len(quo)):
            res[i] = (res[i] + f * quo[i]) % q
    return res


# ---------- layer-A machinery ----------

def layerA_nullity(W, Amap, m, rho, q):
    """Nullity of E_I on the (m+1)(rho+1) biform coefficients."""
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


def pade_nullity(W, Amap, m, rho, q):
    """nullity via the (LA-PADE) reduction: dim of the simultaneous
    Pade/Hankel kernel of the elementary symmetric data e_j(A_x)."""
    sig = from_roots(W, q)
    a = len(W)
    # rows of the joint condition matrix: for each j, kill coefficients
    # of degree rho+1 .. a-2 of (E_j * P mod sigma_W).
    cond = []
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
        E = interpolate(pts, q)
        for t in range(rho + 1):
            mono = [0] * t + [1]
            prod = pmod(pmul(E, mono, q), sig, q)
            prod = prod + [0] * (a - len(prod))
            for d in range(rho + 1, a):
                while len(cond) <= 0:
                    break
            cond.append((t, [prod[d] % q for d in range(rho + 1, a)]))
    # assemble: unknowns are the rho+1 coefficients of P
    nblocks = m
    rows = []
    per = rho + 1
    for b in range(nblocks):
        block = cond[b * per:(b + 1) * per]
        nc = len(block[0][1])
        for d in range(nc):
            rows.append([block[t][1][d] for t in range(per)])
    n, r = nullity(rows, rho + 1, q)
    return n


def zeta_of_order(n, q):
    for g in range(2, q):
        if pow(g, (q - 1) // 2, q) != 1:
            # g is a non-residue; use a full primitive-root search instead
            pass
    # explicit primitive root search
    fac = []
    t = q - 1
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
    raise RuntimeError("no primitive root")


def subgroup(z, n, q):
    out = []
    v = 1
    for _ in range(n):
        out.append(v)
        v = (v * z) % q
    return out


def diagnostics(W, Amap, m, rho, q, tag):
    """H1 / H2 / support diagnostics for a configuration."""
    slopes = sorted({g for x in W for g in Amap[x]})
    supp = {g: sorted(x for x in W if g in Amap[x]) for g in slopes}
    sizes = sorted((len(v) for v in supp.values()), reverse=True)
    inter = []
    for g1, g2 in itertools.combinations(slopes, 2):
        inter.append(len(set(supp[g1]) & set(supp[g2])))
    maxint = max(inter) if inter else 0
    # H1: is W the union of two supports of size rho meeting in m-1?
    h1 = False
    for g1, g2 in itertools.combinations(slopes, 2):
        s1, s2 = set(supp[g1]), set(supp[g2])
        if len(s1) == rho and len(s2) == rho and s1 | s2 == set(W) and len(s1 & s2) == m - 1:
            h1 = True
    emit("    [%s] |Gamma|=%d  support sizes(top5)=%s  max pair-int=%d (cap m-1=%d)"
         % (tag, len(slopes), sizes[:5], maxint, m - 1))
    emit("    [%s] H1 (W = two rho-supports, meet m-1): %s   H2 ((OV) cap met): %s"
         % (tag, "YES" if h1 else "NO", "YES" if maxint <= m - 1 else "NO"))
    return h1, maxint, sizes


# ---------- experiments ----------

def fence_replay(q):
    """Codex's fence: m=2, D=mu_32, W in mu_16 (13 pts), Gamma = mu_8 + eta."""
    m, rho = 2, 7
    z = zeta_of_order(32, q)
    D = subgroup(z, 32, q)
    U = subgroup(pow(z, 2, q), 16, q)
    H = subgroup(pow(z, 4, q), 8, q)
    W = sorted(U)[:13]
    eta = None
    for c in range(2, q):
        if c not in H:
            eta = c
            break
    Gamma = sorted(set(H) | {eta})
    Amap = {}
    ok = True
    for x in W:
        A = [g for g in Gamma if (pow(g, 2, q) - pow(x, 4, q)) % q == 0]
        Amap[x] = A
        if len(A) != m:
            ok = False
    emit("  q=%d  |D|=%d |U|=%d |H|=%d |W|=%d |Gamma|=%d  saturated: %s"
         % (q, len(D), len(U), len(H), len(W), len(Gamma), ok))
    n, r, nrows = layerA_nullity(W, Amap, m, rho, q)
    pn = pade_nullity(W, Amap, m, rho, q)
    emit("  E_I: %d rows x %d cols -> rank %d NULLITY %d   [(LAW3) says 4]"
         % (nrows, (m + 1) * (rho + 1), r, n))
    emit("  (LA-PADE) predicted nullity = %d   AGREE: %s" % (pn, pn == n))
    diagnostics(W, Amap, m, rho, q, "fence")
    # O-budget: how many roots of Q(gamma,.) lie in D?
    O = 0
    for g in Gamma:
        # Q(g,X) = g^2 - X^4
        u = len([x for x in D if (pow(g, 2, q) - pow(x, 4, q)) % q == 0])
        O += rho - u
    emit("  O = sum_gamma (rho - u_gamma) = %d   [(SAT2) cap is m-1 = %d]  -> %s"
         % (O, m - 1, "VIOLATED" if O > m - 1 else "ok"))
    return n


def gen_fence(m, q):
    """Generalized fence Q_0 = Z^m - X^{2m}: predicted nullity 2m."""
    N, rho, T = 16 * m, 4 * m - 1, 4 * m + 1
    if (q - 1) % N:
        emit("  m=%d q=%d: mu_%d not in F_q, skipped" % (m, q, N))
        return None
    z = zeta_of_order(N, q)
    D = subgroup(z, N, q)
    # fibres of x -> x^{2m} (image is mu_8, fibres of size 2m)
    fib = {}
    for x in D:
        fib.setdefault(pow(x, 2 * m, q), []).append(x)
    vals = sorted(fib.keys())[:4]
    pool = sorted(x for v in vals for x in fib[v])
    W = pool[: 7 * m - 1]
    Gamma = sorted({g for v in vals for g in D if pow(g, m, q) == v})
    eta = None
    for c in range(2, q):
        if pow(c, m, q) not in vals:
            eta = c
            break
    Gamma = sorted(set(Gamma) | {eta})
    Amap = {}
    ok = True
    for x in W:
        A = [g for g in Gamma if (pow(g, m, q) - pow(x, 2 * m, q)) % q == 0]
        Amap[x] = A
        if len(A) != m:
            ok = False
    emit("  m=%d q=%d  N=%d rho=%d T=%d  |fibres|=%d(size %d) |W|=%d(need %d) "
         "|Gamma|=%d(need T=%d) saturated:%s"
         % (m, q, N, rho, T, len(vals), len(fib[vals[0]]), len(W), 7 * m - 1,
            len(Gamma), T, ok))
    if not ok or len(W) != 7 * m - 1 or len(Gamma) != T:
        emit("  *** construction failed its own preconditions")
        return None
    n, r, nrows = layerA_nullity(W, Amap, m, rho, q)
    emit("  E_I: %d rows x %d cols -> rank %d NULLITY %d   [predicted 2m = %d]  %s"
         % (nrows, (m + 1) * (rho + 1), r, n, 2 * m,
            "HIT" if n == 2 * m else "MISS"))
    emit("  excess (7m-1)m - 4m(m+1) = %d" % (3 * m * m - 5 * m))
    if m <= 4:
        pn = pade_nullity(W, Amap, m, rho, q)
        emit("  (LA-PADE) predicted nullity = %d   AGREE: %s" % (pn, pn == n))
    diagnostics(W, Amap, m, rho, q, "genfence m=%d" % m)
    return n


def m1_banked_witness(q=17):
    """(BRS1): Q(Y;X) = X^3 + (9+4Y)X^2 + 12YX + 7 over F_17, PROVED witness
    in background/nodes/rate_half_bivariate_row_surplus_route_fence."""
    m, rho = 1, 3
    D = [x for x in range(1, q)]  # mu_16 = F_17^*

    def Q(Y, X):
        return (pow(X, 3, q) + (9 + 4 * Y) * pow(X, 2, q) + 12 * Y * X + 7) % q

    supp = {}
    for Y in range(q):
        roots = [x for x in D if Q(Y, x) == 0]
        if len(roots) == 3:
            supp[Y] = roots
    emit("  banked (BRS1) over F_%d: slopes with 3 distinct domain roots: %s"
         % (q, sorted(supp.keys())))
    for Y in sorted(supp):
        emit("     gamma=%2d  S_gamma=%s" % (Y, supp[Y]))
    covered = sorted({x for v in supp.values() for x in v})
    emit("  covered %d/%d domain points, missing %s"
         % (len(covered), len(D), [x for x in D if x not in covered]))
    slopes = sorted(supp)
    res = []
    for g1, g2 in itertools.combinations(slopes, 2):
        W = sorted(set(supp[g1]) | set(supp[g2]))
        if len(W) != 6:
            continue
        Amap = {x: [g for g in slopes if x in supp[g]] for x in W}
        if any(len(v) != m for v in Amap.values()):
            continue
        n, r, nrows = layerA_nullity(W, Amap, m, rho, q)
        pn = pade_nullity(W, Amap, m, rho, q)
        res.append((g1, g2, n, pn))
    emit("  the %d canonical W = S_g u S_h (H1 holds, |S_g ^ S_h| = m-1 = 0):"
         % len(res))
    ns = sorted({t[2] for t in res})
    emit("     layer-A nullity values over all %d: %s  (predicted 2 = -(3m^2-5m))"
         % (len(res), ns))
    emit("     (LA-PADE) agrees on all %d: %s"
         % (len(res), all(t[2] == t[3] for t in res)))
    g1, g2, n, pn = res[0]
    W = sorted(set(supp[g1]) | set(supp[g2]))
    Amap = {x: [g for g in slopes if x in supp[g]] for x in W}
    diagnostics(W, Amap, m, rho, q, "m=1 banked")
    return res


def random_saturated(m, q, trials, seed):
    """Control: random saturated a=7m-1 configurations -> nullity histogram."""
    import random
    rnd = random.Random(seed)
    N, rho, T = 16 * m, 4 * m - 1, 4 * m + 1
    z = zeta_of_order(N, q)
    D = subgroup(z, N, q)
    hist = {}
    for _ in range(trials):
        W = rnd.sample(D, 7 * m - 1)
        Gamma = rnd.sample([c for c in range(1, q)], T)
        Amap = {x: rnd.sample(Gamma, m) for x in W}
        n, r, nrows = layerA_nullity(W, Amap, m, rho, q)
        hist[n] = hist.get(n, 0) + 1
    emit("  m=%d q=%d  %d random saturated configs: nullity histogram %s"
         % (m, q, trials, dict(sorted(hist.items()))))
    return hist


def main():
    emit("=" * 78)
    emit("D1/D2 CORE  (r36_lawcount_geom)")
    emit("=" * 78)
    emit()
    emit("[A] FENCE REPLAY (anchor 2, (LAW1)-(LAW3)) - the mandatory regression")
    for q in (97, 193):
        fence_replay(q)
        emit()
    emit("[B] THE m=1 BANKED WITNESS (BRS1) - the sign-change regression")
    m1_banked_witness(17)
    emit()
    emit("[C] GENERALIZED FENCE  Q_0 = Z^m - X^{2m}  (registered R2.3)")
    for m in (2, 3, 4, 6):
        for q in (97, 193, 257, 449, 577):
            if (q - 1) % (16 * m) == 0:
                r = gen_fence(m, q)
                emit()
                if r is not None and m >= 4:
                    break
    emit("[D] CONTROL: random saturated configurations")
    for q in (97, 193):
        random_saturated(2, q, 40, 20260811 + q)
    emit()
    with open(OUT, "w") as f:
        f.write("\n".join(LINES) + "\n")


main()

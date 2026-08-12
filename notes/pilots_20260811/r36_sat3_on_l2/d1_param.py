"""r36_sat3_on_l2 D1: the exact rational parametrization of the (L2) stratum
at m=2, its certification against the ORIGINAL 36x32 system, the
det M(B)=0 <=> resultant equivalence, and T>=1 over mu_32 by construction.

Stdlib only.  Writes only d1_results.txt in this directory.
"""
import random, sys

OUT = "notes/pilots_20260811/r36_sat3_on_l2/d1_results.txt"
LOG = []


def say(s=""):
    LOG.append(str(s))


# ---------- F_q[x] ----------
def deg(a):
    d = len(a) - 1
    while d >= 0 and a[d] == 0:
        d -= 1
    return d


def trim(a):
    d = deg(a)
    return a[:d + 1] if d >= 0 else []


def padd(a, b, q):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q for i in range(n)])


def psub(a, b, q):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % q for i in range(n)])


def pmul(a, b, q):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[i + j] = (r[i + j] + ai * bj) % q
    return trim(r)


def pscal(a, c, q):
    return trim([(x * c) % q for x in a])


def pdivmod(a, b, q):
    a = trim(a)[:]
    b = trim(b)
    db = deg(b)
    assert db >= 0
    inv = pow(b[db], q - 2, q)
    da = deg(a)
    quo = [0] * max(1, da - db + 1)
    while da >= db:
        c = (a[da] * inv) % q
        quo[da - db] = c
        for i in range(db + 1):
            a[da - db + i] = (a[da - db + i] - c * b[i]) % q
        da = deg(a)
    return trim(quo), trim(a)


def pgcd(a, b, q):
    a, b = trim(a), trim(b)
    while trim(b):
        a, b = b, pdivmod(a, b, q)[1]
    if a:
        a = pscal(a, pow(a[deg(a)], q - 2, q), q)
    return a


def peval(a, x, q):
    r = 0
    for c in reversed(a):
        r = (r * x + c) % q
    return r


def frompts(pts, q):
    """monic prod (x - a)"""
    r = [1]
    for a in pts:
        r = pmul(r, [(-a) % q, 1], q)
    return r


def interp(xs, ys, q):
    """Lagrange interpolation, deg <= len-1"""
    n = len(xs)
    res = []
    for i in range(n):
        num = [1]
        den = 1
        for j in range(n):
            if j != i:
                num = pmul(num, [(-xs[j]) % q, 1], q)
                den = (den * (xs[i] - xs[j])) % q
        res = padd(res, pscal(num, (ys[i] * pow(den, q - 2, q)) % q, q), q)
    return res


# ---------- linear algebra over F_q ----------
def rank_nullity(M, ncols, q):
    M = [row[:] for row in M]
    r = 0
    piv = []
    for c in range(ncols):
        p = None
        for i in range(r, len(M)):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [(v * inv) % q for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return r, ncols - r, M, piv


def kernel_basis(M, ncols, q):
    r, nul, R, piv = rank_nullity(M, ncols, q)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-R[i][fc]) % q
        basis.append(v)
    return basis


# ---------- the m=2 objects ----------
def MB_matrix(f, g, h, k, q):
    """24x24 matrix of E1,E2 in the unknowns (Q_0,Q_1,Q_2) for fixed B."""
    def cf(p, i):
        return p[i] if 0 <= i < len(p) else 0
    rows = []
    for t in range(12):  # E1: Q_2 f - Q_1 g - Q_0 h = 0
        row = [0] * 24
        for j in range(8):
            row[0 + j] = (row[0 + j] - cf(h, t - j)) % q
            row[8 + j] = (row[8 + j] - cf(g, t - j)) % q
            row[16 + j] = (row[16 + j] + cf(f, t - j)) % q
        rows.append(row)
    for t in range(12):  # E2: Q_1 f - Q_0 g - Q_2 k = 0
        row = [0] * 24
        for j in range(8):
            row[0 + j] = (row[0 + j] - cf(g, t - j)) % q
            row[8 + j] = (row[8 + j] + cf(f, t - j)) % q
            row[16 + j] = (row[16 + j] - cf(k, t - j)) % q
        rows.append(row)
    return rows


def PhiB_matrix(Q0, Q1, Q2, q):
    """24x20 matrix of E1,E2 in the unknowns B=(f,g,h,k) for fixed curve."""
    def cf(p, i):
        return p[i] if 0 <= i < len(p) else 0
    rows = []
    for t in range(12):  # Q_2 f - Q_1 g - Q_0 h
        row = [0] * 20
        for j in range(5):
            row[0 + j] = (row[0 + j] + cf(Q2, t - j)) % q
            row[5 + j] = (row[5 + j] - cf(Q1, t - j)) % q
            row[10 + j] = (row[10 + j] - cf(Q0, t - j)) % q
        rows.append(row)
    for t in range(12):  # Q_1 f - Q_0 g - Q_2 k
        row = [0] * 20
        for j in range(5):
            row[0 + j] = (row[0 + j] + cf(Q1, t - j)) % q
            row[5 + j] = (row[5 + j] - cf(Q0, t - j)) % q
            row[15 + j] = (row[15 + j] - cf(Q2, t - j)) % q
        rows.append(row)
    return rows


def big_system(Q0, Q1, Q2, q):
    """36x32 matrix of M(Z)Q_Z = 0 in the unknowns (y_0,y_1) in F^16 x F^16."""
    def cf(p, i):
        return p[i] if 0 <= i < len(p) else 0
    rows = []
    blocks = [(Q0, None), (Q1, Q0), (Q2, Q1), (None, Q2)]
    for (A, B) in blocks:
        for a in range(9):
            row = [0] * 32
            for j in range(16):
                if A is not None:
                    row[j] = (row[j] + cf(A, j - a)) % q
                if B is not None:
                    row[16 + j] = (row[16 + j] + cf(B, j - a)) % q
            rows.append(row)
    return rows


def hankel(y, q):
    return [[y[a + b] for b in range(8)] for a in range(9)]


def matrank(M, q):
    if not M:
        return 0
    return rank_nullity(M, len(M[0]), q)[0]


def certify(Q0, Q1, Q2, q, want_e2=True):
    """Full certification against the ORIGINAL system.  Returns dict."""
    res = {}
    res["degs"] = (deg(Q0), deg(Q1), deg(Q2))
    gg = pgcd(pgcd(Q0, Q1, q), Q2, q)
    res["s"] = deg(gg)
    sep = [(Q0 + [0] * 8)[:8], (Q1 + [0] * 8)[:8], (Q2 + [0] * 8)[:8]]
    res["seprank"] = matrank(sep, q)
    M = big_system(Q0, Q1, Q2, q)
    r, nul, _, _ = rank_nullity(M, 32, q)
    res["nullity36x32"] = nul
    if nul == 0:
        return res
    kb = kernel_basis(M, 32, q)
    v = kb[0]
    y0, y1 = v[:16], v[16:]
    res["y0"], res["y1"] = y0, y1
    # entrywise re-check of M(Z)Q_Z = 0 from scratch
    ok = True
    M0, M1 = hankel(y0, q), hankel(y1, q)

    def mv(Mm, Q):
        Qp = (Q + [0] * 8)[:8]
        return [sum(Mm[a][b] * Qp[b] for b in range(8)) % q for a in range(9)]
    b0 = mv(M0, Q0)
    b1 = [(x + y) % q for x, y in zip(mv(M0, Q1), mv(M1, Q0))]
    b2 = [(x + y) % q for x, y in zip(mv(M0, Q2), mv(M1, Q1))]
    b3 = mv(M1, Q2)
    ok = all(all(v == 0 for v in b) for b in (b0, b1, b2, b3))
    res["MZQZ_zero"] = ok
    # generic rank + rank-drop divisor
    ranks = {}
    for z in range(q):
        Mz = [[(M0[a][b] + z * M1[a][b]) % q for b in range(8)] for a in range(9)]
        ranks[z] = matrank(Mz, q)
    rinf = matrank(M1, q)
    gr = max(list(ranks.values()) + [rinf])
    res["generic_rank"] = gr
    res["drops"] = sorted([z for z in ranks if ranks[z] < gr])
    res["drop_ranks"] = [ranks[z] for z in res["drops"]]
    res["rank_inf"] = rinf
    if want_e2:
        # kernel vectors of parameter degree <= 1:  (M0+ZM1)(P0+ZP1)=0
        # -> M0P0=0 ; M0P1+M1P0=0 ; M1P1=0   : 27 rows, 16 unknowns
        rows = []
        for a in range(9):
            row = [0] * 16
            for b in range(8):
                row[b] = M0[a][b]
            rows.append(row)
        for a in range(9):
            row = [0] * 16
            for b in range(8):
                row[b] = M1[a][b]
                row[8 + b] = M0[a][b]
            rows.append(row)
        for a in range(9):
            row = [0] * 16
            for b in range(8):
                row[8 + b] = M1[a][b]
            rows.append(row)
        _, nul1, _, _ = rank_nullity(rows, 16, q)
        res["deg_le_1_kernel_dim"] = nul1
    return res


# ---------- the parametrization ----------
def build_from_B(f, g, h, k, q):
    """L = gcd(f^2-kg, g^2+hf) must be linear (or the pair share a root).
    Returns (Q0,Q1,Q2,L) or None."""
    A = psub(pmul(f, f, q), pmul(k, g, q), q)
    C = padd(pmul(g, g, q), pmul(h, f, q), q)
    L = pgcd(A, C, q)
    if deg(L) != 1:
        return None
    Q0, r0 = pdivmod(A, L, q)
    Q2, r2 = pdivmod(C, L, q)
    Q1, r1 = pdivmod(padd(pmul(f, g, q), pmul(h, k, q), q), L, q)
    if r0 or r1 or r2:
        return None
    return Q0, Q1, Q2, L


def rand_poly(d, q, rng):
    return trim([rng.randrange(q) for _ in range(d + 1)])


def sqrt_table(q):
    t = {}
    for s in range(q):
        v = (s * s) % q
        if v not in t:
            t[v] = s
    return t


def mu_N(q, N):
    g = None
    for a in range(2, q):
        seen = set()
        x = 1
        for _ in range(q - 1):
            x = (x * a) % q
            seen.add(x)
        if len(seen) == q - 1:
            g = a
            break
    w = pow(g, (q - 1) // N, q)
    S = []
    x = 1
    for _ in range(N):
        S.append(x)
        x = (x * w) % q
    return sorted(set(S))


def construct_prescribed(S0, q, rng, sqt, D):
    """Prescribe Q_0 = prod_{a in S0}(x-a) (split over the domain D).
    Free: ell, the 4 roots of g, the sqrt signs, c in f = f_0 + c g, and h.
    Returns (f,g,h,k,L,Q0,Q1,Q2) or None."""
    Q0 = frompts(S0, q)
    bad = set(S0)
    cand = [x for x in range(q) if x not in bad]
    ell = rng.choice(cand)
    L = [(-ell) % q, 1]
    # pick 4 roots for g at which L*Q0 is a nonzero square
    pool = [x for x in cand if x != ell]
    rng.shuffle(pool)
    rs, ys = [], []
    for x in pool:
        v = (peval(L, x, q) * peval(Q0, x, q)) % q
        if v == 0 or v not in sqt:
            continue
        s = sqt[v]
        rs.append(x)
        ys.append(s if rng.randrange(2) else (-s) % q)
        if len(rs) == 4:
            break
    if len(rs) < 4:
        return None
    g = frompts(rs, q)
    f0 = interp(rs, ys, q)
    c = rng.randrange(q)
    f = padd(f0, pscal(g, c, q), q)
    A = psub(pmul(f, f, q), pmul(L, Q0, q), q)
    k, r = pdivmod(A, g, q)
    if r or deg(k) > 4:
        return None
    fe = peval(f, ell, q)
    if fe == 0:
        return None
    hell = (-(peval(g, ell, q) ** 2) * pow(fe, q - 2, q)) % q
    w = rand_poly(3, q, rng)
    h = padd([hell], pmul(L, w, q), q)
    if deg(h) > 4:
        return None
    C = padd(pmul(g, g, q), pmul(h, f, q), q)
    Q2, r2 = pdivmod(C, L, q)
    Q1, r1 = pdivmod(padd(pmul(f, g, q), pmul(h, k, q), q), L, q)
    if r1 or r2:
        return None
    return f, g, h, k, L, Q0, Q1, Q2


def T_over_domain(Q0, Q1, Q2, q, D):
    """supported slopes: z with Q_z having rho=7 DISTINCT roots all inside D."""
    Ds = set(D)
    cnt = {}
    for x in D:
        a0, a1, a2 = peval(Q0, x, q), peval(Q1, x, q), peval(Q2, x, q)
        # roots in z of a0 + a1 z + a2 z^2
        if a2 == 0 and a1 == 0:
            if a0 == 0:
                return None  # common root: s != 0
            continue
        if a2 == 0:
            z = (-a0 * pow(a1, q - 2, q)) % q
            cnt[z] = cnt.get(z, 0) + 1
            continue
        disc = (a1 * a1 - 4 * a2 * a0) % q
        if disc == 0:
            z = (-a1 * pow(2 * a2, q - 2, q)) % q
            cnt[z] = cnt.get(z, 0) + 1
        else:
            s = SQT[q].get(disc)
            if s is None:
                continue
            inv = pow(2 * a2, q - 2, q)
            for sg in (s, (-s) % q):
                z = ((-a1 + sg) * inv) % q
                cnt[z] = cnt.get(z, 0) + 1
    sup = sorted([z for z in cnt if cnt[z] == 7])
    # z = infinity: the member is Q_2
    infsup = (deg(Q2) == 7 and len([x for x in D if peval(Q2, x, q) == 0]) == 7)
    return sup, infsup, cnt


SQT = {}

# ================= MAIN =================
FIELDS = [97, 193]
say("# d1_results — r36_sat3_on_l2 — the (L2) parametrization at m=2")
say("")

for q in FIELDS:
    SQT[q] = sqrt_table(q)

# ---- PART A: (X1) the identity, on random B ----
say("## PART A — (X1) L*Q_0 = f^2-kg, L*Q_1 = fg+hk, L*Q_2 = g^2+hf")
say("   test: for random B with gcd(f^2-kg, g^2+hf) linear, the built curve")
say("   satisfies E1,E2 identically AND nullity(36x32) >= 1.")
for q in FIELDS:
    rng = random.Random(3620260811 + q)
    tried = built = e12ok = nulok = 0
    detzero_and_gcd = [0, 0, 0, 0]  # det=0&gcd, det=0&nogcd, det!=0&gcd, neither
    for _ in range(400):
        f, g, h, k = (rand_poly(4, q, rng) for _ in range(4))
        tried += 1
        A = psub(pmul(f, f, q), pmul(k, g, q), q)
        C = padd(pmul(g, g, q), pmul(h, f, q), q)
        Gc = pgcd(A, C, q)
        MB = MB_matrix(f, g, h, k, q)
        rk = matrank(MB, q)
        detz = (rk < 24)
        shar = (deg(Gc) >= 1) or (deg(A) <= 7 and deg(C) <= 7)
        detzero_and_gcd[0 if (detz and shar) else 1 if detz else 2 if shar else 3] += 1
        out = build_from_B(f, g, h, k, q)
        if out is None:
            continue
        Q0, Q1, Q2, L = out
        built += 1
        # E1,E2 identically zero?
        z1 = psub(psub(pmul(Q2, f, q), pmul(Q1, g, q), q), pmul(Q0, h, q), q)
        z2 = psub(psub(pmul(Q1, f, q), pmul(Q0, g, q), q), pmul(Q2, k, q), q)
        if not z1 and not z2:
            e12ok += 1
        _, nul, _, _ = rank_nullity(big_system(Q0, Q1, Q2, q), 32, q)
        if nul >= 1:
            nulok += 1
    say("q=%d  random B draws=%d  linear-L draws=%d  E1&E2 identically 0: %d/%d"
        % (q, tried, built, e12ok, built))
    say("      nullity(36x32)>=1 on those: %d/%d" % (nulok, built))
    say("      [det M(B)=0 & (shared root or both deg<=7)] = %d ; det=0 only = %d ;"
        % (detzero_and_gcd[0], detzero_and_gcd[1]))
    say("      shared only = %d ; neither = %d   (rate det=0: %.4f, 1/q=%.4f)"
        % (detzero_and_gcd[2], detzero_and_gcd[3],
           (detzero_and_gcd[0] + detzero_and_gcd[1]) / float(tried), 1.0 / q))
say("")

# ---- PART B: (X2) dimension bookkeeping ----
say("## PART B — (X2) dimension: fibre of B -> Q and of Q -> B")
for q in FIELDS:
    rng = random.Random(770000 + q)
    hist_MB, hist_Phi = {}, {}
    n = 0
    while n < 40:
        f, g, h, k = (rand_poly(4, q, rng) for _ in range(4))
        out = build_from_B(f, g, h, k, q)
        if out is None:
            continue
        Q0, Q1, Q2, L = out
        if deg(Q0) != 7 or deg(Q2) != 7:
            continue
        n += 1
        _, n1, _, _ = rank_nullity(MB_matrix(f, g, h, k, q), 24, q)
        _, n2, _, _ = rank_nullity(PhiB_matrix(Q0, Q1, Q2, q), 20, q)
        hist_MB[n1] = hist_MB.get(n1, 0) + 1
        hist_Phi[n2] = hist_Phi.get(n2, 0) + 1
    say("q=%d  nullity of M(B) (curve given B): %s   nullity of Phi (B given curve): %s"
        % (q, sorted(hist_MB.items()), sorted(hist_Phi.items())))
say("   parameter count: (f,g,h,k)=20 coords + ell=1, minus the 2 conditions at ell")
say("   = 19 affine = 18 projective, and the fibre is finite => image dim 18.")
say("")

# ---- PART C/D: (X3) prescribed split Q_0 over mu_32, certified ----
say("## PART C — (X3) Q_0 PRESCRIBED SPLIT OVER mu_32, full certification")
WIT = {}
for q in FIELDS:
    D = mu_N(q, 32)
    rng = random.Random(9110000 + q)
    made = 0
    good = []
    for _ in range(4000):
        S0 = rng.sample(D, 7)
        out = construct_prescribed(S0, q, rng, SQT[q], D)
        if out is None:
            continue
        f, g, h, k, L, Q0, Q1, Q2 = out
        if deg(Q0) != 7 or deg(Q1) != 7 or deg(Q2) != 7:
            continue
        made += 1
        c = certify(Q0, Q1, Q2, q)
        if c["s"] != 0 or c["nullity36x32"] < 1 or c["seprank"] != 3:
            continue
        if c["generic_rank"] != 7 or c.get("deg_le_1_kernel_dim", 9) != 0:
            continue
        if not c["MZQZ_zero"]:
            continue
        t = T_over_domain(Q0, Q1, Q2, q, D)
        if t is None:
            continue
        sup, infsup, cnt = t
        good.append((S0, f, g, h, k, L, Q0, Q1, Q2, c, sup, infsup))
        if len(good) >= 6:
            break
    say("q=%d  domain mu_32=%s" % (q, D[:6] + ["..."]))
    say("      constructions attempted (deg-3 filter passed): %d ; fully certified: %d"
        % (made, len(good)))
    if good:
        S0, f, g, h, k, L, Q0, Q1, Q2, c, sup, infsup = good[0]
        say("      HEADLINE WITNESS q=%d" % q)
        say("        S0 (subset of mu_32) = %s" % S0)
        say("        f=%s g=%s h=%s k=%s L=%s" % (f, g, h, k, L))
        say("        Q0=%s" % Q0)
        say("        Q1=%s" % Q1)
        say("        Q2=%s" % Q2)
        say("        degs=%s  s=%d  seprank=%d  nullity(36x32)=%d  M(Z)Q_Z==0: %s"
            % (c["degs"], c["s"], c["seprank"], c["nullity36x32"], c["MZQZ_zero"]))
        say("        generic rank=%d  drops at z=%s with ranks %s  rank at inf=%d"
            % (c["generic_rank"], c["drops"], c["drop_ranks"], c["rank_inf"]))
        say("        deg<=1 kernel dim=%d (0 <=> e=2 exactly)" % c["deg_le_1_kernel_dim"])
        say("        y0=%s" % c["y0"])
        say("        y1=%s" % c["y1"])
        say("        SUPPORTED FINITE SLOPES over mu_32: %s   (z=inf supported: %s)"
            % (sup, infsup))
        say("        T_fin=%d  T_P1=%d" % (len(sup), len(sup) + (1 if infsup else 0)))
    Tf = [len(x[10]) for x in good]
    say("      T over mu_32 across the certified objects: %s" % Tf)
    WIT[q] = good
say("")

# ---- control: does an UNPRESCRIBED object ever have T>=1 over mu_32? ----
say("## PART D — control: random (unprescribed) objects, T over mu_32")
for q in FIELDS:
    D = mu_N(q, 32)
    rng = random.Random(5150000 + q)
    n = 0
    tot_sup = 0
    fullsplit_Fq = 0
    members = 0
    while n < 60:
        f, g, h, k = (rand_poly(4, q, rng) for _ in range(4))
        out = build_from_B(f, g, h, k, q)
        if out is None:
            continue
        Q0, Q1, Q2, L = out
        if deg(Q0) != 7 or deg(Q2) != 7 or deg(Q1) != 7:
            continue
        if deg(pgcd(pgcd(Q0, Q1, q), Q2, q)) != 0:
            continue
        n += 1
        t = T_over_domain(Q0, Q1, Q2, q, D)
        if t is not None:
            tot_sup += len(t[0]) + (1 if t[1] else 0)
        # full F_q-splitting census over all finite z (the bespoke-domain currency)
        for z in range(q):
            Qz = padd(padd(Q0, pscal(Q1, z, q), q), pscal(Q2, (z * z) % q, q), q)
            members += 1
            if deg(Qz) != 7:
                continue
            rts = [x for x in range(q) if peval(Qz, x, q) == 0]
            if len(rts) == 7:
                fullsplit_Fq += 1
    say("q=%d  %d random parametrized objects: total supported slopes over mu_32 = %d"
        % (q, n, tot_sup))
    say("      members scanned=%d  fully F_q-split members=%d  rate=%.5f  (1/7!=%.5f)"
        % (members, fullsplit_Fq, fullsplit_Fq / float(members), 1.0 / 5040))
say("")

with open(OUT, "w") as fh:
    fh.write("\n".join(LOG) + "\n")
print("\n".join(LOG))

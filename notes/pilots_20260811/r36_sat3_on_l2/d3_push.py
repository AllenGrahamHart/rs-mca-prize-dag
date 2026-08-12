"""r36_sat3_on_l2 D2/D3: (a) Moebius normalisation of the T=2 mu_32 witnesses to
TWO FINITE supported slopes; (b) the bespoke-32-set push for T >= 3; (c) the
packing/occupancy measurements that name the obstruction.

Stdlib only.  Writes only d3_results.txt in this directory.
"""
import random, time

OUT = "notes/pilots_20260811/r36_sat3_on_l2/d3_results.txt"
LOG = []


def say(s=""):
    LOG.append(str(s))


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
    r = [1]
    for a in pts:
        r = pmul(r, [(-a) % q, 1], q)
    return r


def interp(xs, ys, q):
    n = len(xs)
    res = []
    for i in range(n):
        num, den = [1], 1
        for j in range(n):
            if j != i:
                num = pmul(num, [(-xs[j]) % q, 1], q)
                den = (den * (xs[i] - xs[j])) % q
        res = padd(res, pscal(num, (ys[i] * pow(den, q - 2, q)) % q, q), q)
    return res


def rank_nullity(M, ncols, q):
    M = [row[:] for row in M]
    r, piv = 0, []
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
                fq = M[i][c]
                M[i] = [(M[i][j] - fq * M[r][j]) % q for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return r, ncols - r, M, piv


def kernel_basis(M, ncols, q):
    r, nul, R, piv = rank_nullity(M, ncols, q)
    out = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-R[i][fc]) % q
        out.append(v)
    return out


def matrank(M, q):
    return rank_nullity(M, len(M[0]), q)[0] if M else 0


def big_system(Q0, Q1, Q2, q):
    def cf(p, i):
        return p[i] if 0 <= i < len(p) else 0
    rows = []
    for (A, B) in [(Q0, None), (Q1, Q0), (Q2, Q1), (None, Q2)]:
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


def certify(Q0, Q1, Q2, q):
    res = {"degs": (deg(Q0), deg(Q1), deg(Q2))}
    res["s"] = deg(pgcd(pgcd(Q0, Q1, q), Q2, q))
    res["seprank"] = matrank([(P + [0] * 8)[:8] for P in (Q0, Q1, Q2)], q)
    M = big_system(Q0, Q1, Q2, q)
    r, nul, _, _ = rank_nullity(M, 32, q)
    res["nullity36x32"] = nul
    if nul == 0:
        return res
    v = kernel_basis(M, 32, q)[0]
    y0, y1 = v[:16], v[16:]
    res["y0"], res["y1"] = y0, y1
    M0, M1 = hankel(y0, q), hankel(y1, q)

    def mv(Mm, Q):
        Qp = (Q + [0] * 8)[:8]
        return [sum(Mm[a][b] * Qp[b] for b in range(8)) % q for a in range(9)]
    b0 = mv(M0, Q0)
    b1 = [(x + y) % q for x, y in zip(mv(M0, Q1), mv(M1, Q0))]
    b2 = [(x + y) % q for x, y in zip(mv(M0, Q2), mv(M1, Q1))]
    b3 = mv(M1, Q2)
    res["MZQZ_zero"] = all(all(t == 0 for t in b) for b in (b0, b1, b2, b3))
    ranks = {z: matrank([[(M0[a][b] + z * M1[a][b]) % q for b in range(8)]
                         for a in range(9)], q) for z in range(q)}
    rinf = matrank(M1, q)
    gr = max(list(ranks.values()) + [rinf])
    res["generic_rank"] = gr
    res["drops"] = sorted([z for z in ranks if ranks[z] < gr])
    res["drop_ranks"] = [ranks[z] for z in res["drops"]]
    res["rank_inf"] = rinf
    rows = []
    for a in range(9):
        rows.append([M0[a][b] if b < 8 else 0 for b in range(16)])
    for a in range(9):
        rows.append([M1[a][b] if b < 8 else M0[a][b - 8] for b in range(16)])
    for a in range(9):
        rows.append([0 if b < 8 else M1[a][b - 8] for b in range(16)])
    res["deg_le_1_kernel_dim"] = rank_nullity(rows, 16, q)[1]
    return res


def mu_N(q, N):
    for a in range(2, q):
        x, seen = 1, set()
        for _ in range(q - 1):
            x = (x * a) % q
            seen.add(x)
        if len(seen) == q - 1:
            g = a
            break
    w = pow(g, (q - 1) // N, q)
    S, x = [], 1
    for _ in range(N):
        S.append(x)
        x = (x * w) % q
    return sorted(set(S))


def sqrt_table(q):
    t = {}
    for s in range(q):
        v = (s * s) % q
        if v not in t:
            t[v] = s
    return t


def slope_census(Q0, Q1, Q2, q, sqt, pts):
    """cnt[z] = #{x in pts : Q_z(x)=0} for finite z, via the quadratics q_x.
    Returns cnt, ninf (#roots of Q_2 in pts), occupancy (total root slots)."""
    cnt = {}
    occ = 0
    ninf = 0
    for x in pts:
        a0, a1, a2 = peval(Q0, x, q), peval(Q1, x, q), peval(Q2, x, q)
        if a2 == 0:
            ninf += 1
            if a1 == 0:
                if a0 == 0:
                    return None, None, None
                continue
            z = (-a0 * pow(a1, q - 2, q)) % q
            cnt[z] = cnt.get(z, 0) + 1
            occ += 2  # one finite root + the root at infinity
            continue
        disc = (a1 * a1 - 4 * a2 * a0) % q
        inv = pow(2 * a2, q - 2, q)
        if disc == 0:
            z = (-a1 * inv) % q
            cnt[z] = cnt.get(z, 0) + 1
            occ += 1
        else:
            s = sqt.get(disc)
            if s is None:
                continue
            for sg in (s, (-s) % q):
                cnt[((-a1 + sg) * inv) % q] = cnt.get(((-a1 + sg) * inv) % q, 0) + 1
            occ += 2
    return cnt, ninf, occ


def build_rate1(q, rng, S0=None):
    """rate-1 construction.  If S0 is given, Q_0 is prescribed split on S0."""
    if S0 is not None:
        Q0 = frompts(S0, q)
        sqt = SQT[q]
        ell = rng.choice([x for x in range(q) if x not in S0])
        L = [(-ell) % q, 1]
        pool = [x for x in range(q) if x not in S0 and x != ell]
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
        f = padd(interp(rs, ys, q), pscal(g, rng.randrange(1, q), q), q)
        if deg(f) != 4 or peval(f, ell, q) == 0:
            return None
        k, r = pdivmod(psub(pmul(f, f, q), pmul(L, Q0, q), q), g, q)
        if r or deg(k) > 4:
            return None
        hell = (-(peval(g, ell, q) ** 2) * pow(peval(f, ell, q), q - 2, q)) % q
        h = padd([hell], pmul(L, [rng.randrange(q) for _ in range(4)], q), q)
        if deg(h) > 4:
            return None
    else:
        ell = rng.randrange(q)
        L = [(-ell) % q, 1]
        f = [rng.randrange(q) for _ in range(5)]
        g = [rng.randrange(q) for _ in range(5)]
        if peval(f, ell, q) == 0 or peval(g, ell, q) == 0:
            return None
        h = padd([(-(peval(g, ell, q) ** 2) * pow(peval(f, ell, q), q - 2, q)) % q],
                 pmul(L, [rng.randrange(q) for _ in range(4)], q), q)
        k = padd([(peval(f, ell, q) ** 2 * pow(peval(g, ell, q), q - 2, q)) % q],
                 pmul(L, [rng.randrange(q) for _ in range(4)], q), q)
        if deg(h) > 4 or deg(k) > 4:
            return None
        Q0, r0 = pdivmod(psub(pmul(f, f, q), pmul(k, g, q), q), L, q)
        if r0:
            return None
    Q2, r2 = pdivmod(padd(pmul(g, g, q), pmul(h, f, q), q), L, q)
    Q1, r1 = pdivmod(padd(pmul(f, g, q), pmul(h, k, q), q), L, q)
    if r1 or r2:
        return None
    return f, g, h, k, L, Q0, Q1, Q2


SQT = {}
say("# d3_results — r36_sat3_on_l2 — Moebius normalisation, the bespoke push,")
say("#   and the packing measurements")
say("")

# ---------- (a) Moebius: two FINITE supported slopes ----------
say("## PART A — Moebius normalisation of the T=2 mu_32 witnesses")
say("   Z = W/(1-W) sends W=0 -> Z=0 and W=1 -> Z=infinity, and maps the Hankel")
say("   pencil to (y_0, y_1-y_0), Q'_0=Q_0, Q'_1=Q_1-2Q_0, Q'_2=Q_0-Q_1+Q_2.")
WIT2 = {
    97: ([78, 63, 82, 85, 33, 58, 77, 1],
         [75, 9, 93, 12, 8, 88, 15, 79],
         [46, 93, 4, 16, 76, 49, 28, 50]),
    193: ([67, 21, 188, 90, 184, 8, 67, 1],
          [39, 24, 181, 56, 109, 49, 177, 25],
          [168, 6, 179, 105, 108, 25, 184, 25]),
}
for q in (97, 193):
    SQT[q] = sqrt_table(q)
    D = mu_N(q, 32)
    Q0, Q1, Q2 = WIT2[q]
    R0 = Q0
    R1 = psub(Q1, pscal(Q0, 2, q), q)
    R2 = padd(psub(Q0, Q1, q), Q2, q)
    c = certify(R0, R1, R2, q)
    cnt, ninf, occ = slope_census(R0, R1, R2, q, SQT[q], D)
    sup = sorted([z for z in cnt if cnt[z] == 7])
    say("q=%d  Q'_0=%s" % (q, R0))
    say("      Q'_1=%s" % R1)
    say("      Q'_2=%s" % R2)
    say("      degs=%s s=%d seprank=%d nullity(36x32)=%d M(Z)Q_Z==0:%s gen.rank=%d"
        % (c["degs"], c["s"], c["seprank"], c["nullity36x32"], c["MZQZ_zero"], c["generic_rank"]))
    say("      drops z=%s ranks=%s rank_inf=%d deg<=1 kernel=%d"
        % (c["drops"], c["drop_ranks"], c["rank_inf"], c["deg_le_1_kernel_dim"]))
    say("      SUPPORTED FINITE SLOPES over mu_32: %s  (roots of Q'_2 in mu_32: %d)"
        % (sup, ninf))
    say("      => T_fin = %d  with BOTH slopes finite" % len(sup))
say("")

# ---------- (b) the bespoke push ----------
say("## PART B — bespoke 32-set push: how many members split completely over F_q?")
say("   objects: rate-1 construction with Q_0 prescribed split on a 7-set.")
say("   T_bespoke = #{z in P^1 : Q_z has 7 distinct F_q-roots}, admissible iff")
say("   |union of the root sets| <= 32.")
BUDGET = {97: 95.0, 193: 95.0}
for q in (97, 193):
    D = mu_N(q, 32)
    allpts = list(range(q))
    rng = random.Random(24680 + q)
    t0 = time.time()
    n = 0
    Th = {}
    best = None
    rec = 0
    while time.time() - t0 < BUDGET[q]:
        S0 = rng.sample(D, 7)
        out = build_rate1(q, rng, S0)
        if out is None:
            continue
        f, g, h, k, L, Q0, Q1, Q2 = out
        if deg(Q0) != 7 or deg(Q1) != 7 or deg(Q2) != 7:
            continue
        n += 1
        cnt, ninf, occ = slope_census(Q0, Q1, Q2, q, allpts, SQT[q]) if False else \
            slope_census(Q0, Q1, Q2, q, SQT[q], allpts)
        if cnt is None:
            continue
        sup = [z for z in cnt if cnt[z] == 7]
        T = len(sup) + (1 if ninf == 7 else 0)
        Th[T] = Th.get(T, 0) + 1
        if T > rec:
            rec = T
            union = set()
            for z in sup:
                Qz = padd(padd(Q0, pscal(Q1, z, q), q), pscal(Q2, (z * z) % q, q), q)
                union |= set(x for x in allpts if peval(Qz, x, q) == 0)
            if ninf == 7:
                union |= set(x for x in allpts if peval(Q2, x, q) == 0)
            best = (T, sorted(sup), ninf == 7, sorted(union), Q0, Q1, Q2, f, g, h, k, L, S0)
    say("q=%d  objects built=%d in %.0fs ; T_bespoke histogram=%s"
        % (q, n, time.time() - t0, sorted(Th.items())))
    exp1 = (q + 1 - 1) / 5040.0
    say("      predicted extra F_q-split members per object (X8) = (q)/7! = %.4f ; measured = %.4f"
        % (exp1, sum((t - 1) * c for t, c in Th.items()) / float(max(n, 1))))
    if best and best[0] >= 2:
        T, sup, isinf, union, Q0, Q1, Q2, f, g, h, k, L, S0 = best
        c = certify(Q0, Q1, Q2, q)
        say("      RECORD T_bespoke = %d  supported finite slopes=%s  z=inf supported=%s"
            % (T, sup, isinf))
        say("        |union of root sets| = %d  (must be <= 32)  D = %s" % (len(union), union))
        say("        Q_0=%s" % Q0)
        say("        Q_1=%s" % Q1)
        say("        Q_2=%s" % Q2)
        say("        f=%s g=%s h=%s k=%s L=%s" % (f, g, h, k, L))
        say("        degs=%s s=%d seprank=%d nullity=%d M(Z)Q_Z==0:%s gen.rank=%d drops=%s ranks=%s"
            % (c["degs"], c["s"], c["seprank"], c["nullity36x32"], c["MZQZ_zero"],
               c["generic_rank"], c["drops"], c["drop_ranks"]))
        say("        deg<=1 kernel dim=%d ; y_0=%s ; y_1=%s"
            % (c["deg_le_1_kernel_dim"], c["y0"], c["y1"]))
        say("        T over mu_32 for this object = %d"
            % (len([z for z in slope_census(Q0, Q1, Q2, q, SQT[q], D)[0]
                    if slope_census(Q0, Q1, Q2, q, SQT[q], D)[0][z] == 7])
               + (1 if slope_census(Q0, Q1, Q2, q, SQT[q], D)[1] == 7 else 0)))
say("")

# ---------- (c) the packing measurement ----------
say("## PART C — the packing/occupancy measurement over mu_32 (the D3 mechanism)")
say("   Each x in D gives the quadratic q_x(z)=Q_0(x)+zQ_1(x)+z^2Q_2(x) in P^1;")
say("   d_x = #roots <= m = 2, so sum_x d_x <= 2|D| = 64 and (SAT3) needs 7*9=63")
say("   of those 64 slots to sit on ONE 9-element slope set.")
for q in (97, 193):
    D = mu_N(q, 32)
    rng = random.Random(1357 + q)
    occs, spreads, maxc = [], [], []
    n = 0
    while n < 120:
        out = build_rate1(q, rng)
        if out is None:
            continue
        f, g, h, k, L, Q0, Q1, Q2 = out
        if deg(Q0) != 7 or deg(Q1) != 7 or deg(Q2) != 7:
            continue
        if deg(pgcd(pgcd(Q0, Q1, q), Q2, q)) != 0:
            continue
        cnt, ninf, occ = slope_census(Q0, Q1, Q2, q, SQT[q], D)
        if cnt is None:
            continue
        n += 1
        occs.append(occ)
        spreads.append(len(cnt) + (1 if ninf else 0))
        mx = max(list(cnt.values()) + [ninf])
        maxc.append(mx)
    say("q=%d  %d random objects:" % (q, n))
    say("      slot occupancy sum_x d_x out of 64: mean %.1f, max %d, min %d"
        % (sum(occs) / float(n), max(occs), min(occs)))
    say("      #distinct slopes carrying a root: mean %.1f, min %d (SAT3 needs <= 9 for 63 slots)"
        % (sum(spreads) / float(n), min(spreads)))
    hh = {}
    for v in maxc:
        hh[v] = hh.get(v, 0) + 1
    say("      max_z (#roots of Q_z in mu_32) histogram: %s   [7 = a supported slope]"
        % sorted(hh.items()))
say("")
say("## PART D — refined criterion: det M(B)=0 <=> the two ell-conditions,")
say("   EXCEPT where f(ell)=g(ell)=0 (then fg+hk need not vanish at ell).")
for q in (97, 193):
    rng = random.Random(999 + q)
    tab = {}
    for _ in range(600):
        f = [rng.randrange(q) for _ in range(5)]
        g = [rng.randrange(q) for _ in range(5)]
        h = [rng.randrange(q) for _ in range(5)]
        k = [rng.randrange(q) for _ in range(5)]
        A = psub(pmul(f, f, q), pmul(k, g, q), q)
        C = padd(pmul(g, g, q), pmul(h, f, q), q)
        E = padd(pmul(f, g, q), pmul(h, k, q), q)
        G3 = pgcd(pgcd(A, C, q), E, q)
        crit = (deg(G3) >= 1) or (deg(A) <= 7 and deg(C) <= 7 and deg(E) <= 7)
        rows = []

        def cf(p, i):
            return p[i] if 0 <= i < len(p) else 0
        for t in range(12):
            row = [0] * 24
            for j in range(8):
                row[j] = (row[j] - cf(h, t - j)) % q
                row[8 + j] = (row[8 + j] - cf(g, t - j)) % q
                row[16 + j] = (row[16 + j] + cf(f, t - j)) % q
            rows.append(row)
        for t in range(12):
            row = [0] * 24
            for j in range(8):
                row[j] = (row[j] - cf(g, t - j)) % q
                row[8 + j] = (row[8 + j] + cf(f, t - j)) % q
                row[16 + j] = (row[16 + j] - cf(k, t - j)) % q
            rows.append(row)
        detz = matrank(rows, q) < 24
        tab[(detz, crit)] = tab.get((detz, crit), 0) + 1
    say("q=%d  (det M(B)=0, refined criterion) joint histogram over 600 random B: %s"
        % (q, sorted(tab.items())))
say("")

with open(OUT, "w") as fh:
    fh.write("\n".join(LOG) + "\n")
print("\n".join(LOG))

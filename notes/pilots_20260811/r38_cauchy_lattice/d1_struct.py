"""r38_cauchy_lattice D1 - structure of the third prescription.

Verifies (X1) the pointwise third-member conditions, (X5) the Euclid /
continued-fraction characterisation of the first-minimum drop and its
blind rate, (P4) the sensitivity of the Euclid trajectory to a single
point move, and (X2)/(X3)/(X4) the scale-eliminated 2x5-Hankel-moment
(TEST) -- validated exhaustively at q=17 against a brute-force
(lambda,mu) rank scan and against from-scratch object reconstruction.

Stdlib only.  Results appended (never blind "w").
"""
import random
import time
import itertools

RES = "notes/pilots_20260811/r38_cauchy_lattice/d1_results.txt"
FH = open(RES, "a")


def out(s):
    print(s)
    FH.write(s + "\n")
    FH.flush()


# ---------------- polynomial helpers over F_q (low->high) ----------------
def ptrim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, q):
    n = max(len(a), len(b))
    r = [0] * n
    for i, c in enumerate(a):
        r[i] = c
    for i, c in enumerate(b):
        r[i] = (r[i] + c) % q
    return ptrim(r)


def psub(a, b, q):
    n = max(len(a), len(b))
    r = [0] * n
    for i, c in enumerate(a):
        r[i] = c
    for i, c in enumerate(b):
        r[i] = (r[i] - c) % q
    return ptrim(r)


def pmul(a, b, q):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                r[i + j] = (r[i + j] + ca * cb) % q
    return ptrim(r)


def pscal(a, c, q):
    return ptrim([x * c % q for x in a])


def pdivmod(a, b, q):
    a = [c % q for c in a]
    ptrim(a)
    b = [c % q for c in b]
    ptrim(b)
    db = len(b) - 1
    if not a or len(a) - 1 < db:
        return [], a
    ivl = pow(b[-1], q - 2, q)
    quo = [0] * (len(a) - db)
    while a and len(a) - 1 >= db:
        d = len(a) - 1 - db
        c = a[-1] * ivl % q
        quo[d] = c
        for j in range(db + 1):
            a[d + j] = (a[d + j] - c * b[j]) % q
        ptrim(a)
    ptrim(quo)
    return quo, a


def peval(a, x, q):
    r = 0
    for c in reversed(a):
        r = (r * x + c) % q
    return r


def pdeg(a):
    return len(a) - 1


def from_roots(S, q):
    p = [1]
    for r in S:
        p = pmul(p, [(-r) % q, 1], q)
    return p


def nullspace(rows, ncols, q):
    M = [[c % q for c in r] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(M)):
            if M[i][c]:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [x * iv % q for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis, len(piv)


def matrank(rows, ncols, q):
    return nullspace(rows, ncols, q)[1]


# ---------------- random (PAR) object ----------------
def rand_par(q, rnd):
    while True:
        ell = rnd.randrange(q)
        L = [(-ell) % q, 1]
        f = [rnd.randrange(q) for _ in range(5)]
        g = [rnd.randrange(q) for _ in range(5)]
        if f[4] == 0 or g[4] == 0:
            continue
        fe = peval(f, ell, q)
        ge = peval(g, ell, q)
        if fe == 0 or ge == 0:
            continue
        k = [rnd.randrange(q) for _ in range(5)]
        h = [rnd.randrange(q) for _ in range(5)]
        tk = fe * fe % q * pow(ge, q - 2, q) % q
        k[0] = (k[0] + tk - peval(k, ell, q)) % q
        th = (-ge * ge) % q * pow(fe, q - 2, q) % q
        h[0] = (h[0] + th - peval(h, ell, q)) % q
        n0 = psub(pmul(f, f, q), pmul(k, g, q), q)
        n1 = padd(pmul(f, g, q), pmul(h, k, q), q)
        n2 = padd(pmul(g, g, q), pmul(h, f, q), q)
        Qs = []
        ok = True
        for nu in (n0, n1, n2):
            qq, rr = pdivmod(nu[:], L, q)
            if rr:
                ok = False
                break
            Qs.append(qq)
        if not ok:
            continue
        return f, g, h, k, L, Qs[0], Qs[1], Qs[2]


# ---------------- Euclid / lattice first minimum ----------------
def euclid_profile(R, P, q):
    """remainder degrees, cofactor degrees, d1 = min_i max(deg r_i, deg v_i)."""
    rp, rc = P[:], R[:]
    vp, vc = [], [1]
    rdegs = [pdeg(rp), pdeg(rc)]
    prof = []
    best = None
    while rc:
        d1i = max(pdeg(rc), pdeg(vc))
        prof.append((pdeg(rc), pdeg(vc)))
        if best is None or d1i < best:
            best = d1i
        qq, rr = pdivmod(rp[:], rc, q)
        vn = psub(vp, pmul(qq, vc, q), q)
        rp, rc = rc, rr
        vp, vc = vc, vn
        rdegs.append(pdeg(rc))
    return best, prof, rdegs


def has_short_vector(R, P, q, bnd=4):
    """exists (f,g)!=0, deg<=bnd both, f == R g mod P -- by linear algebra."""
    n = pdeg(P)
    rows = []
    # f - R g == 0 mod P : write f = sum f_i x^i, g = sum g_j x^j,
    # residue of (f - R*g) mod P has n coefficients -> n rows.
    cols = 2 * (bnd + 1)
    mat = [[0] * cols for _ in range(n)]
    for i in range(bnd + 1):
        xi = [0] * i + [1]
        _, rr = pdivmod(xi, P, q)
        for t, c in enumerate(rr):
            mat[t][i] = c
    for j in range(bnd + 1):
        xj = [0] * j + [1]
        pr = pmul(xj, R, q)
        _, rr = pdivmod(pr, P, q)
        for t, c in enumerate(rr):
            mat[t][bnd + 1 + j] = (-c) % q
    bas, rk = nullspace(mat, cols, q)
    return len(bas) > 0, len(bas)


# ---------------- (TEST): scale-eliminated moment/rank criterion ----------
class PairCtx(object):
    def __init__(self, S0, Sinf, q):
        self.q = q
        self.S0 = list(S0)
        self.Sinf = list(Sinf)
        P0 = from_roots(S0, q)
        Pinf = from_roots(Sinf, q)
        self.P0 = P0
        self.Pinf = Pinf
        # weights w0[x] = Pinf(x)/P0'(x) for x in S0
        self.w0 = []
        for x in self.S0:
            d = 1
            for y in self.S0:
                if y != x:
                    d = d * ((x - y) % q) % q
            self.w0.append(peval(Pinf, x, q) * pow(d, q - 2, q) % q)
        self.w1 = []
        for x in self.Sinf:
            d = 1
            for y in self.Sinf:
                if y != x:
                    d = d * ((x - y) % q) % q
            self.w1.append(peval(P0, x, q) * pow(d, q - 2, q) % q)
        self.pinf_at0 = [peval(Pinf, x, q) for x in self.S0]
        self.p0_atinf = [peval(P0, x, q) for x in self.Sinf]
        self.pow0 = [[pow(x, j, q) for j in range(6)] for x in self.S0]
        self.powinf = [[pow(x, j, q) for j in range(6)] for x in self.Sinf]
        self.lb0 = self._lag(self.S0[:5])
        self.lbi = self._lag(self.Sinf[:5])

    def _lag(self, pts):
        q = self.q
        out = []
        for i, xi in enumerate(pts):
            num = [1]
            den = 1
            for j, xj in enumerate(pts):
                if j != i:
                    num = pmul(num, [(-xj) % q, 1], q)
                    den = den * ((xi - xj) % q) % q
            iv = pow(den, q - 2, q)
            c = [v * iv % q for v in num]
            while len(c) < 5:
                c.append(0)
            out.append(c)
        return out


def prefix_suffix(vals, q):
    n = len(vals)
    pre = [1] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] * vals[i] % q
    suf = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] * vals[i] % q
    return [pre[i] * suf[i + 1] % q for i in range(n)]


def run_test(ctx, S1, want_witness=False):
    """returns (hit, info).  info carries u,G,H and diagnostics."""
    q = ctx.q
    p10 = []
    for x in ctx.S0:
        v = 1
        for w in S1:
            v = v * ((x - w) % q) % q
        p10.append(v)
    p1i = []
    for x in ctx.Sinf:
        v = 1
        for w in S1:
            v = v * ((x - w) % q) % q
        p1i.append(v)
    if 0 in p10 or 0 in p1i:
        return False, {"deg": "P1 vanishes on S0/Sinf"}
    c0 = prefix_suffix(p10, q)
    c1 = prefix_suffix(p1i, q)
    m = [0] * 6
    for i in range(7):
        t = ctx.w0[i] * c0[i] % q
        pw = ctx.pow0[i]
        for j in range(6):
            m[j] = (m[j] + t * pw[j]) % q
    n = [0] * 6
    for i in range(7):
        t = ctx.w1[i] * c1[i] % q
        pw = ctx.powinf[i]
        for j in range(6):
            n[j] = (n[j] + t * pw[j]) % q
    M = [m[0:5], m[1:6], n[0:5], n[1:6]]
    bas, rk = nullspace(M, 5, q)
    if len(bas) != 1:
        return False, {"deg": "dim(A cap B)=%d" % len(bas)}
    u = bas[0]
    # G~ from S0, H~ from Sinf
    v0 = []
    for i in range(7):
        ux = 0
        pw = ctx.pow0[i]
        for j in range(5):
            ux = (ux + u[j] * pw[j]) % q
        v0.append(ctx.pinf_at0[i] * ux % q * c0[i] % q)
    vi = []
    for i in range(7):
        ux = 0
        pw = ctx.powinf[i]
        for j in range(5):
            ux = (ux + u[j] * pw[j]) % q
        vi.append(ctx.p0_atinf[i] * ux % q * c1[i] % q)
    G = [0] * 5
    for i in range(5):
        t = v0[i]
        if t:
            lb = ctx.lb0[i]
            for j in range(5):
                G[j] = (G[j] + t * lb[j]) % q
    H = [0] * 5
    for i in range(5):
        t = vi[i]
        if t:
            lb = ctx.lbi[i]
            for j in range(5):
                H[j] = (H[j] + t * lb[j]) % q
    if matrank([u, G, H], 5, q) > 2:
        return False, None
    # consistency: G must reproduce the two unused S0 values
    for i in (5, 6):
        ev = 0
        pw = ctx.pow0[i]
        for j in range(5):
            ev = (ev + G[j] * pw[j]) % q
        if ev != v0[i]:
            return False, {"deg": "G interp mismatch"}
        ev = 0
        pw = ctx.powinf[i]
        for j in range(5):
            ev = (ev + H[j] * pw[j]) % q
        if ev != vi[i]:
            return False, {"deg": "H interp mismatch"}
    return True, {"u": u, "G": G, "H": H}


def reconstruct(ctx, S1, info):
    """From a (TEST) hit build (f,g,L,h,k) and certify the (PAR) identities."""
    q = ctx.q
    u, G, H = info["u"], info["G"], info["H"]
    # solve u = c1*G + c2*H
    bas, rk = nullspace([[G[j], H[j], (-u[j]) % q] for j in range(5)], 3, q)
    sol = None
    for b in bas:
        if b[2] % q != 0:
            iv = pow(b[2], q - 2, q)
            sol = (b[0] * iv % q, b[1] * iv % q)
            break
    if sol is None:
        return None, "no (c1,c2)"
    c1, c2 = sol
    if c1 == 0 or c2 == 0:
        return None, "degenerate c"
    g = ptrim([c1 * x % q for x in G])
    f = ptrim([c2 * x % q for x in H])
    if pdeg(f) != 4 or pdeg(g) != 4:
        return None, "deg f=%d deg g=%d" % (pdeg(f), pdeg(g))
    P1 = from_roots(S1, q)
    Q0 = pscal(ctx.P0, c2, q)
    Q2 = pscal(ctx.Pinf, c1, q)
    Q1 = psub(P1, padd(Q0, Q2, q), q)
    num = padd(psub(pmul(Q0, pmul(g, g, q), q),
                    pmul(Q1, pmul(f, g, q), q), q),
               pmul(Q2, pmul(f, f, q), q), q)
    den = pmul(Q0, Q2, q)
    L, rr = pdivmod(num[:], den, q)
    if rr:
        return None, "CONIC not divisible"
    if pdeg(L) != 1:
        return None, "deg L = %d" % pdeg(L)
    k, r1 = pdivmod(psub(pmul(f, f, q), pmul(L, Q0, q), q), g, q)
    if r1:
        return None, "k not polynomial"
    h, r2 = pdivmod(psub(pmul(L, Q2, q), pmul(g, g, q), q), f, q)
    if r2:
        return None, "h not polynomial"
    chk = []
    chk.append(pmul(L, Q0, q) == psub(pmul(f, f, q), pmul(k, g, q), q))
    chk.append(pmul(L, Q1, q) == padd(pmul(f, g, q), pmul(h, k, q), q))
    chk.append(pmul(L, Q2, q) == padd(pmul(g, g, q), pmul(h, f, q), q))
    mem1 = padd(padd(Q0, Q1, q), Q2, q)
    chk.append(mem1 == P1)
    return {"f": f, "g": g, "h": h, "k": k, "L": L, "Q0": Q0, "Q1": Q1,
            "Q2": Q2, "c1": c1, "c2": c2, "checks": chk}, "ok"


def brute_triple(ctx, S1):
    """Ground truth: scan (lambda,mu) and rank the 14x10 system."""
    q = ctx.q
    P1 = from_roots(S1, q)
    p10 = [peval(P1, x, q) for x in ctx.S0]
    p1i = [peval(P1, x, q) for x in ctx.Sinf]
    found = 0
    for lam in range(1, q):
        for mu in range(1, q):
            rows = []
            ok = True
            for i, x in enumerate(ctx.S0):
                a = ctx.pinf_at0[i]
                b = (lam * p10[i] - ctx.pinf_at0[i]) % q
                pw = ctx.pow0[i]
                rows.append([a * pw[j] % q for j in range(5)]
                            + [(-b) * pw[j] % q for j in range(5)])
            for i, x in enumerate(ctx.Sinf):
                a = (mu * p1i[i] - ctx.p0_atinf[i]) % q
                b = ctx.p0_atinf[i]
                pw = ctx.powinf[i]
                rows.append([a * pw[j] % q for j in range(5)]
                            + [(-b) * pw[j] % q for j in range(5)])
            bas, rk = nullspace(rows, 10, q)
            for v in bas:
                f = ptrim(v[0:5][:])
                g = ptrim(v[5:10][:])
                if pdeg(f) == 4 and pdeg(g) == 4:
                    found += 1
                    ok = False
                    break
            if not ok:
                pass
    return found


# ============================== DRIVER ==============================
def main():
    t00 = time.time()
    out("")
    out("=== RUN d1_struct %s ===" % time.strftime("%Y-%m-%d %H:%M:%S"))

    # ---------- PART A: (X1) pointwise conditions + (CONIC) ----------
    out("[A] (X1)/(CONIC) on random (PAR) objects")
    for q in (97, 193):
        rnd = random.Random(38 * q + 1)
        nobj = 300
        conic_ok = 0
        s0_pts = s0_ok = 0
        s2_pts = s2_ok = 0
        for _ in range(nobj):
            f, g, h, k, L, Q0, Q1, Q2 = rand_par(q, rnd)
            lhs = padd(psub(pmul(Q0, pmul(g, g, q), q),
                            pmul(Q1, pmul(f, g, q), q), q),
                       pmul(Q2, pmul(f, f, q), q), q)
            rhs = pmul(L, pmul(Q0, Q2, q), q)
            if lhs == rhs:
                conic_ok += 1
            for x in range(q):
                if peval(Q0, x, q) == 0:
                    s0_pts += 1
                    if (peval(f, x, q) * peval(Q2, x, q) -
                            peval(g, x, q) * peval(Q1, x, q)) % q == 0:
                        s0_ok += 1
                if peval(Q2, x, q) == 0:
                    s2_pts += 1
                    if (peval(f, x, q) * peval(Q1, x, q) -
                            peval(g, x, q) * peval(Q0, x, q)) % q == 0:
                        s2_ok += 1
        out("  q=%d  (CONIC) %d/%d ; f*Q2==g*Q1 on roots(Q0): %d/%d ;"
            " f*Q1==g*Q0 on roots(Q2): %d/%d"
            % (q, conic_ok, nobj, s0_ok, s0_pts, s2_ok, s2_pts))

    # ---------- PART B: (X5) Euclid characterisation ----------
    out("[B] (X5) Euclid / continued-fraction characterisation of d1<=4")
    for q in (97, 193):
        rnd = random.Random(7 * q + 5)
        n = 200
        agree_skip = 0
        agree_lin = 0
        cons_v = 0
        for _ in range(n):
            S0 = rnd.sample(range(1, q), 7)
            Si = rnd.sample([z for z in range(1, q) if z not in S0], 7)
            P = pmul(from_roots(S0, q), from_roots(Si, q), q)
            R = [rnd.randrange(q) for _ in range(14)]
            ptrim(R)
            d1, prof, rdegs = euclid_profile(R, P, q)
            skip = any(dr <= 4 for dr in rdegs[1:]) and \
                all(not (5 <= dr <= 9) for dr in rdegs[1:] if dr >= 0)
            has, dim = has_short_vector(R, P, q, 4)
            if (d1 <= 4) == skip:
                agree_skip += 1
            if (d1 <= 4) == has:
                agree_lin += 1
            if all(dv == 14 - rdegs[i] for i, (dr, dv) in enumerate(prof)):
                cons_v += 1
        out("  q=%d  n=%d : d1<=4 <=> degree-window-skip %d/%d ;"
            " d1<=4 <=> short lattice vector exists %d/%d ;"
            " deg v_i = 14 - deg r_{i-1} %d/%d"
            % (q, n, agree_skip, n, agree_lin, n, cons_v, n))
    # constructed drops must be detected
    for q in (97, 193):
        rnd = random.Random(11 * q)
        n = 120
        det = 0
        wind = 0
        for _ in range(n):
            S0 = rnd.sample(range(1, q), 7)
            Si = rnd.sample([z for z in range(1, q) if z not in S0], 7)
            P = pmul(from_roots(S0, q), from_roots(Si, q), q)
            while True:
                f = [rnd.randrange(q) for _ in range(5)]
                g = [rnd.randrange(q) for _ in range(5)]
                if f[4] and g[4]:
                    gi, rr = pdivmod([1], [1], q)
                    # R = f * g^{-1} mod P
                    bas = None
                    # invert g mod P by extended euclid
                    r0, r1 = P[:], g[:]
                    s0v, s1v = [], [1]
                    while r1:
                        qq, rr2 = pdivmod(r0[:], r1, q)
                        s0v, s1v = s1v, psub(s0v, pmul(qq, s1v, q), q)
                        r0, r1 = r1, rr2
                    if pdeg(r0) != 0:
                        continue
                    iv = pow(r0[0], q - 2, q)
                    ginv = pscal(s0v, iv, q)
                    _, R = pdivmod(pmul(f, ginv, q), P, q)
                    break
            d1, prof, rdegs = euclid_profile(R, P, q)
            if d1 <= 4:
                det += 1
            if all(not (5 <= dr <= 9) for dr in rdegs[1:] if dr >= 0):
                wind += 1
        out("  q=%d  constructed f/g drops detected by d1<=4: %d/%d ;"
            " window-skip: %d/%d" % (q, det, n, wind, n))
    # blind rate at small q
    out("[B2] blind rate of d1<=4 over random R (predicted ~ q^-5)")
    for q in (3, 5, 7):
        rnd = random.Random(q * 991)
        P = None
        while P is None:
            cand = [rnd.randrange(q) for _ in range(14)] + [1]
            P = cand
        trials = 40000 if q == 3 else (20000 if q == 5 else 8000)
        hit = 0
        for _ in range(trials):
            R = [rnd.randrange(q) for _ in range(14)]
            ptrim(R)
            d1, prof, rdegs = euclid_profile(R, P, q)
            if d1 <= 4:
                hit += 1
        out("  q=%d  trials=%d  hits=%d  rate=%.3e  q^-5=%.3e  ratio=%.2f"
            % (q, trials, hit, hit / float(trials), q ** -5.0,
               (hit / float(trials)) / (q ** -5.0) if hit else 0.0))

    # ---------- PART B3: (P4) trajectory sensitivity to one point ----------
    out("[B3] (P4) Euclid trajectory under a one-point move of S_1")
    for q in (97, 193):
        rnd = random.Random(q + 313)
        n = 60
        same_prof = 0
        same_first = 0
        for _ in range(n):
            pts = rnd.sample(range(1, q), 22)
            S0, Si, S1 = pts[:7], pts[7:14], pts[14:21]
            alt = pts[21]
            P = pmul(from_roots(S0, q), from_roots(Si, q), q)
            profs = []
            for SS in (S1, S1[:-1] + [alt]):
                P1 = from_roots(SS, q)
                Pinf = from_roots(Si, q)
                P0 = from_roots(S0, q)
                # R = CRT of t(x) with lambda=mu=1
                pts_all = []
                vals = []
                bad = False
                for x in S0:
                    d = peval(Pinf, x, q)
                    num = (peval(P1, x, q) - d) % q
                    if d == 0:
                        bad = True
                        break
                    pts_all.append(x)
                    vals.append(num * pow(d, q - 2, q) % q)
                if bad:
                    break
                for x in Si:
                    d = (peval(P1, x, q) - peval(P0, x, q)) % q
                    if d == 0:
                        bad = True
                        break
                    pts_all.append(x)
                    vals.append(peval(P0, x, q) * pow(d, q - 2, q) % q)
                if bad:
                    break
                R = [0]
                for i, x in enumerate(pts_all):
                    bnum = [1]
                    bden = 1
                    for j, y in enumerate(pts_all):
                        if j != i:
                            bnum = pmul(bnum, [(-y) % q, 1], q)
                            bden = bden * ((x - y) % q) % q
                    R = padd(R, pscal(bnum, vals[i] * pow(bden, q - 2, q) % q,
                                      q), q)
                d1, prof, rdegs = euclid_profile(R, P, q)
                profs.append(rdegs)
            if len(profs) == 2:
                if profs[0] == profs[1]:
                    same_prof += 1
                if len(profs[0]) > 2 and len(profs[1]) > 2 and \
                        profs[0][2] == profs[1][2]:
                    same_first += 1
        out("  q=%d  n=%d : identical remainder-degree profile after moving"
            " ONE point of S_1: %d ; identical first quotient degree: %d"
            % (q, n, same_prof, same_first))

    out("=== END d1_struct  wall=%.1fs ===" % (time.time() - t00))


main()
FH.close()

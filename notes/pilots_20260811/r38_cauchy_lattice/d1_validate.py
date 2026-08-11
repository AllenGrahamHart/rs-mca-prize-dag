"""r38_cauchy_lattice D1b - exhaustive validation of the scale-eliminated
(TEST) at q=29, one (S_0,S_inf) pair, ALL C(29,7) subsets S_1.

Validates in BOTH directions:
  (a) every (TEST) hit reconstructs to a full certified (PAR) object with
      three split members whose root sets are exactly (S_0,S_1,S_inf);
  (b) (TEST) agrees with a brute-force (lambda,mu) scan of the 14x10
      rational-interpolation system on every sampled triple.
Also measures the hit rate against the predicted q^-3 per triple.

Stdlib only.  Results appended (never blind "w").  Helpers duplicated
per file: no import of any banked script.
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


def prefix_suffix(vals, q):
    n = len(vals)
    pre = [1] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] * vals[i] % q
    suf = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] * vals[i] % q
    return [pre[i] * suf[i + 1] % q for i in range(n)]


def lagrange_basis(pts, q):
    ba = []
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
        ba.append(c)
    return ba


class PairCtx(object):
    """Everything that depends only on (S_0, S_inf)."""

    def __init__(self, S0, Sinf, q):
        self.q = q
        self.S0 = list(S0)
        self.Sinf = list(Sinf)
        self.P0 = from_roots(S0, q)
        self.Pinf = from_roots(Sinf, q)
        self.a0 = [peval(self.Pinf, x, q) for x in self.S0]
        self.ai = [peval(self.P0, x, q) for x in self.Sinf]
        self.d0i = []
        for x in self.S0:
            d = 1
            for y in self.S0:
                if y != x:
                    d = d * ((x - y) % q) % q
            self.d0i.append(pow(d, q - 2, q))
        self.dii = []
        for x in self.Sinf:
            d = 1
            for y in self.Sinf:
                if y != x:
                    d = d * ((x - y) % q) % q
            self.dii.append(pow(d, q - 2, q))
        self.pw0 = [[pow(x, j, q) for j in range(6)] for x in self.S0]
        self.pwi = [[pow(x, j, q) for j in range(6)] for x in self.Sinf]
        self.tab0 = self._table(self.S0)
        self.tabi = self._table(self.Sinf)

    def _table(self, S):
        q = self.q
        tab = {}
        idx = range(7)
        for sz in (0, 1, 2):
            for D in itertools.combinations(idx, sz):
                rest = [i for i in idx if i not in D]
                adj = []
                for i in rest:
                    v = 1
                    for j in D:
                        v = v * ((S[i] - S[j]) % q) % q
                    adj.append(v)
                nmom = len(rest) - 5
                ipts = rest[:5]
                chk = rest[5:]
                lb = lagrange_basis([S[i] for i in ipts], q)
                tab[D] = (rest, adj, nmom, ipts, chk, lb)
        return tab


def side_rows(ctx, which, p1v, D):
    """condition rows on u from one side; returns (rows, ent, c) or None."""
    q = ctx.q
    if len(D) > 2:
        return [], None, None
    if which == 0:
        ent = ctx.tab0[tuple(D)]
        a, di, pw = ctx.a0, ctx.d0i, ctx.pw0
    else:
        ent = ctx.tabi[tuple(D)]
        a, di, pw = ctx.ai, ctx.dii, ctx.pwi
    rest, adj, nmom, ipts, chk, lb = ent
    c = prefix_suffix([p1v[i] for i in rest], q)
    rows = []
    if nmom > 0:
        nm = nmom + 4
        m = [0] * nm
        for t, i in enumerate(rest):
            w = a[i] * di[i] % q * adj[t] % q * c[t] % q
            pwi_ = pw[i]
            for j in range(nm):
                m[j] = (m[j] + w * pwi_[j]) % q
        for r in range(nmom):
            rows.append(m[r:r + 5])
    return rows, ent, c


def side_poly(ctx, which, u, p1v, ent, c):
    """degree-<=4 interpolant (scaled) of the side values; None if inconsistent."""
    q = ctx.q
    rest, adj, nmom, ipts, chk, lb = ent
    if which == 0:
        a, pw = ctx.a0, ctx.pw0
    else:
        a, pw = ctx.ai, ctx.pwi
    v = []
    for t, i in enumerate(rest):
        pwi_ = pw[i]
        ux = 0
        for j in range(5):
            ux = (ux + u[j] * pwi_[j]) % q
        v.append(a[i] * ux % q * c[t] % q)
    G = [0] * 5
    for t in range(5):
        tv = v[t]
        if tv:
            lbt = lb[t]
            for j in range(5):
                G[j] = (G[j] + tv * lbt[j]) % q
    for t in range(5, len(rest)):
        i = rest[t]
        pwi_ = pw[i]
        ev = 0
        for j in range(5):
            ev = (ev + G[j] * pwi_[j]) % q
        if ev != v[t]:
            return None
    return G


def run_test(ctx, S1):
    """(hit, tag, u, G, H).  tag records the branch taken."""
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
    D0 = [i for i in range(7) if p10[i] == 0]
    Di = [i for i in range(7) if p1i[i] == 0]
    rows = [ctx.pw0[i][:5] for i in D0] + [ctx.pwi[i][:5] for i in Di]
    r0, e0, c0 = side_rows(ctx, 0, p10, D0)
    ri, ei, ci = side_rows(ctx, 1, p1i, Di)
    rows = rows + r0 + ri
    bas, rk = nullspace(rows, 5, q)
    if len(bas) == 0:
        return False, "dim0", None, None, None
    if len(bas) > 1:
        return False, "dim%d" % len(bas), None, None, None
    if e0 is None or ei is None:
        return False, "overlap>2", None, None, None
    u = bas[0]
    G = side_poly(ctx, 0, u, p10, e0, c0)
    if G is None:
        return False, "Gfail", None, None, None
    H = side_poly(ctx, 1, u, p1i, ei, ci)
    if H is None:
        return False, "Hfail", None, None, None
    if nullspace([u, G, H], 5, q)[1] > 2:
        return False, "rank3", None, None, None
    return True, "hit", u, G, H


def reconstruct(ctx, S1, u, G, H):
    q = ctx.q
    bas, rk = nullspace([[G[j], H[j], (-u[j]) % q] for j in range(5)], 3, q)
    sol = None
    for b in bas:
        if b[2]:
            iv = pow(b[2], q - 2, q)
            sol = (b[0] * iv % q, b[1] * iv % q)
            break
    if sol is None:
        return None, "no(c1,c2)"
    c1, c2 = sol
    if c1 == 0 or c2 == 0:
        return None, "c1c2zero"
    g = ptrim([c1 * x % q for x in G])
    f = ptrim([c2 * x % q for x in H])
    if pdeg(f) != 4 or pdeg(g) != 4:
        return None, "deg f=%d g=%d" % (pdeg(f), pdeg(g))
    F = padd(f, g, q)
    P1 = from_roots(S1, q)
    gam = None
    for i, x in enumerate(ctx.S0):
        de = ctx.a0[i] * peval(F, x, q) % q
        if de:
            gam = peval(P1, x, q) * peval(g, x, q) % q * pow(de, q - 2, q) % q
            break
    alp = None
    for i, x in enumerate(ctx.Sinf):
        de = ctx.ai[i] * peval(F, x, q) % q
        if de:
            alp = peval(P1, x, q) * peval(f, x, q) % q * pow(de, q - 2, q) % q
            break
    if gam is None or alp is None or gam == 0 or alp == 0:
        return None, "scales"
    Q0 = pscal(ctx.P0, alp, q)
    Q2 = pscal(ctx.Pinf, gam, q)
    Q1 = psub(P1, padd(Q0, Q2, q), q)
    num = padd(psub(pmul(Q0, pmul(g, g, q), q), pmul(Q1, pmul(f, g, q), q), q),
               pmul(Q2, pmul(f, f, q), q), q)
    L, rr = pdivmod(num[:], pmul(Q0, Q2, q), q)
    if rr:
        return None, "CONICnondiv"
    if pdeg(L) != 1:
        return None, "degL=%d" % pdeg(L)
    k, r1 = pdivmod(psub(pmul(f, f, q), pmul(L, Q0, q), q), g, q)
    if r1:
        return None, "k_nonpoly"
    h, r2 = pdivmod(psub(pmul(L, Q2, q), pmul(g, g, q), q), f, q)
    if r2:
        return None, "h_nonpoly"
    ch = [pmul(L, Q0, q) == psub(pmul(f, f, q), pmul(k, g, q), q),
          pmul(L, Q1, q) == padd(pmul(f, g, q), pmul(h, k, q), q),
          pmul(L, Q2, q) == padd(pmul(g, g, q), pmul(h, f, q), q),
          padd(padd(Q0, Q1, q), Q2, q) == P1,
          pdeg(h) == 4 and pdeg(k) == 4]
    return {"f": f, "g": g, "h": h, "k": k, "L": L, "Q0": Q0, "Q1": Q1,
            "Q2": Q2, "alpha": alp, "gamma": gam, "checks": ch}, "ok"


def brute_triple(ctx, S1):
    q = ctx.q
    P1 = from_roots(S1, q)
    p10 = [peval(P1, x, q) for x in ctx.S0]
    p1i = [peval(P1, x, q) for x in ctx.Sinf]
    for lam in range(1, q):
        for mu in range(1, q):
            rows = []
            for i in range(7):
                a = ctx.a0[i]
                b = (lam * p10[i] - ctx.a0[i]) % q
                pw = ctx.pw0[i]
                rows.append([a * pw[j] % q for j in range(5)]
                            + [(-b) * pw[j] % q for j in range(5)])
            for i in range(7):
                a = (mu * p1i[i] - ctx.ai[i]) % q
                b = ctx.ai[i]
                pw = ctx.pwi[i]
                rows.append([a * pw[j] % q for j in range(5)]
                            + [(-b) * pw[j] % q for j in range(5)])
            bas, rk = nullspace(rows, 10, q)
            for v in bas:
                ff = ptrim(v[0:5][:])
                gg = ptrim(v[5:10][:])
                if pdeg(ff) == 4 and pdeg(gg) == 4:
                    return True
    return False


def main():
    from math import comb
    t00 = time.time()
    out("")
    out("=== RUN d1_validate %s ===" % time.strftime("%Y-%m-%d %H:%M:%S"))
    q = 23
    npairs = 2
    n_k2 = 0
    for i in range(3):
        for j in range(3):
            n_k2 += comb(7, i) * comb(7, j) * comb(q - 14, 7 - i - j)
    tot = comb(q, 7)
    out("q=%d  domain = all of F_q ; C(%d,7)=%d triples/pair ;"
        " predicted hits/pair: all-triples %.2f, |S1^S0|<=2 & |S1^Sinf|<=2"
        " subpopulation %d -> %.2f"
        % (q, q, tot, tot / float(q ** 3), n_k2, n_k2 / float(q ** 3)))
    allhits = []
    tags = {}
    ovhist = {}
    good = 0
    bad = {}
    ctxs = []
    for pr in range(npairs):
        rnd = random.Random(2300 + pr)
        S0 = sorted(rnd.sample(range(q), 7))
        Sinf = sorted(rnd.sample([z for z in range(q) if z not in S0], 7))
        ctx = PairCtx(S0, Sinf, q)
        ctxs.append(ctx)
        t0 = time.time()
        hits = []
        ntr = 0
        for S1 in itertools.combinations(range(q), 7):
            ntr += 1
            hit, tag, u, G, H = run_test(ctx, S1)
            tags[tag] = tags.get(tag, 0) + 1
            if hit:
                hits.append((S1, u, G, H))
        el = time.time() - t0
        out("pair %d  S_0=%s  S_inf=%s  triples=%d  hits=%d  %.1fs"
            "  (%.1f us/triple)"
            % (pr, S0, Sinf, ntr, len(hits), el, 1e6 * el / ntr))
        for S1, u, G, H in hits:
            obj, why = reconstruct(ctx, S1, u, G, H)
            if obj is not None and all(obj["checks"]):
                good += 1
                ov = (len(set(S1) & set(S0)), len(set(S1) & set(Sinf)))
                ovhist[ov] = ovhist.get(ov, 0) + 1
                if good <= 3:
                    out("  HIT pair%d S_1=%s ov=%s f=%s g=%s L=%s"
                        " alpha=%d gamma=%d PARchecks=%s"
                        % (pr, list(S1), ov, obj["f"], obj["g"], obj["L"],
                           obj["alpha"], obj["gamma"], obj["checks"]))
            else:
                bad[why] = bad.get(why, 0) + 1
        allhits.append((pr, hits))
    out("branch tags (both pairs): %s" % sorted(tags.items()))
    nh = sum(len(h) for _, h in allhits)
    out("reconstruction: %d/%d hits -> full certified (PAR) object;"
        " failures %s" % (good, nh, sorted(bad.items())))
    out("hit overlap histogram (|S1^S0|,|S1^Sinf|): %s" % sorted(ovhist.items()))
    out("OV4: max(|S1^S0|+|S1^Sinf|) over hits = %s (bound 4)"
        % (max([a + b for a, b in ovhist]) if ovhist else "n/a"))

    out("[cross-check] brute-force (lambda,mu) 14x10 rank scan vs (TEST)")
    allc = list(itertools.combinations(range(q), 7))
    rnd2 = random.Random(4242)
    agree = 0
    ntot = 0
    dis = []
    for pr, hits in allhits:
        ctx = ctxs[pr]
        sample = [tuple(h[0]) for h in hits]
        seen = set(sample)
        while len(sample) < len(hits) + 60:
            cand = allc[rnd2.randrange(len(allc))]
            if cand not in seen:
                seen.add(cand)
                sample.append(cand)
        for S1 in sample:
            bf = brute_triple(ctx, S1)
            tt = run_test(ctx, S1)[0]
            ntot += 1
            if bf == tt:
                agree += 1
            else:
                dis.append((pr, list(S1), bf, tt))
    out("agreement %d/%d ; disagreements %s" % (agree, ntot, dis[:6]))
    out("=== END d1_validate wall=%.1fs ===" % (time.time() - t00))


main()
FH.close()

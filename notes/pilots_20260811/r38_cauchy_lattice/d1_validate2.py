"""r38_cauchy_lattice D1c - bounded cross-check + diagnosis of the
degenerate branch found in d1_validate (rank[u;G;H]<=2 but u not in
span(G,H)).  Establishes the CORRECTED (TEST):

  hit  <=>  dim(A cap B) = 1, u = c1*G + c2*H with c1,c2 != 0,
            deg(c2*H) = deg(c1*G) = 4.

Brute-force (lambda,mu) 14x10 rank scan is the ground truth; sampled.

Stdlib only; append-mode results; helpers duplicated per file.
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


class Ctx(object):
    def __init__(self, S0, Sinf, q):
        self.q = q
        self.S0 = list(S0)
        self.Sinf = list(Sinf)
        self.P0 = from_roots(S0, q)
        self.Pinf = from_roots(Sinf, q)
        self.a0 = [peval(self.Pinf, x, q) for x in self.S0]
        self.ai = [peval(self.P0, x, q) for x in self.Sinf]
        self.d0i = [pow(self._der(self.S0, x), q - 2, q) for x in self.S0]
        self.dii = [pow(self._der(self.Sinf, x), q - 2, q) for x in self.Sinf]
        self.pw0 = [[pow(x, j, q) for j in range(6)] for x in self.S0]
        self.pwi = [[pow(x, j, q) for j in range(6)] for x in self.Sinf]
        self.t0 = self._tab(self.S0)
        self.ti = self._tab(self.Sinf)

    def _der(self, S, x):
        d = 1
        for y in S:
            if y != x:
                d = d * ((x - y) % self.q) % self.q
        return d

    def _tab(self, S):
        q = self.q
        tab = {}
        for sz in (0, 1, 2):
            for D in itertools.combinations(range(7), sz):
                rest = [i for i in range(7) if i not in D]
                adj = []
                for i in rest:
                    v = 1
                    for j in D:
                        v = v * ((S[i] - S[j]) % q) % q
                    adj.append(v)
                tab[D] = (rest, adj, len(rest) - 5,
                          lagrange_basis([S[i] for i in rest[:5]], q))
        return tab


def sideinfo(ctx, which, p1, D):
    q = ctx.q
    if which == 0:
        ent = ctx.t0[tuple(D)]
        a, di, pw = ctx.a0, ctx.d0i, ctx.pw0
    else:
        ent = ctx.ti[tuple(D)]
        a, di, pw = ctx.ai, ctx.dii, ctx.pwi
    rest, adj, nmom, lb = ent
    vals = [p1[i] for i in rest]
    n = len(vals)
    pre = [1] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] * vals[i] % q
    suf = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] * vals[i] % q
    c = [pre[i] * suf[i + 1] % q for i in range(n)]
    rows = []
    if nmom > 0:
        nm = nmom + 4
        m = [0] * nm
        for t in range(n):
            i = rest[t]
            w = a[i] * di[i] % q * adj[t] % q * c[t] % q
            for j in range(nm):
                m[j] = (m[j] + w * pw[i][j]) % q
        for r in range(nmom):
            rows.append(m[r:r + 5])
    return rows, c, ent


def sidepoly(ctx, which, u, ent, c):
    q = ctx.q
    rest, adj, nmom, lb = ent
    a, pw = (ctx.a0, ctx.pw0) if which == 0 else (ctx.ai, ctx.pwi)
    v = []
    for t, i in enumerate(rest):
        ux = 0
        for j in range(5):
            ux = (ux + u[j] * pw[i][j]) % q
        v.append(a[i] * ux % q * c[t] % q)
    G = [0] * 5
    for t in range(5):
        if v[t]:
            for j in range(5):
                G[j] = (G[j] + v[t] * lb[t][j]) % q
    for t in range(5, len(rest)):
        i = rest[t]
        ev = 0
        for j in range(5):
            ev = (ev + G[j] * pw[i][j]) % q
        if ev != v[t]:
            return None
    return G


def raw_test(ctx, S1):
    q = ctx.q
    p10 = [1] * 7
    p1i = [1] * 7
    for t, x in enumerate(ctx.S0):
        v = 1
        for w in S1:
            v = v * ((x - w) % q) % q
        p10[t] = v
    for t, x in enumerate(ctx.Sinf):
        v = 1
        for w in S1:
            v = v * ((x - w) % q) % q
        p1i[t] = v
    D0 = tuple(i for i in range(7) if p10[i] == 0)
    Di = tuple(i for i in range(7) if p1i[i] == 0)
    if len(D0) > 2 or len(Di) > 2:
        return None, "ovl>2"
    rows = [ctx.pw0[i][:5] for i in D0] + [ctx.pwi[i][:5] for i in Di]
    r0, c0, e0 = sideinfo(ctx, 0, p10, D0)
    ri, ci, ei = sideinfo(ctx, 1, p1i, Di)
    bas, rk = nullspace(rows + r0 + ri, 5, q)
    if len(bas) != 1:
        return None, "dim%d" % len(bas)
    u = bas[0]
    G = sidepoly(ctx, 0, u, e0, c0)
    H = sidepoly(ctx, 1, u, ei, ci)
    if G is None or H is None:
        return None, "interpfail"
    if nullspace([u, G, H], 5, q)[1] > 2:
        return None, "rank3"
    return (u, G, H), "rank<=2"


def full_criterion(ctx, u, G, H):
    q = ctx.q
    bas, rk = nullspace([[G[j], H[j], (-u[j]) % q] for j in range(5)], 3, q)
    for b in bas:
        if b[2]:
            iv = pow(b[2], q - 2, q)
            c1, c2 = b[0] * iv % q, b[1] * iv % q
            if c1 and c2:
                g = ptrim([c1 * x % q for x in G])
                f = ptrim([c2 * x % q for x in H])
                if pdeg(f) == 4 and pdeg(g) == 4:
                    return True, (f, g)
            return False, None
    return False, None


def brute(ctx, S1):
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
    t00 = time.time()
    out("")
    out("=== RUN d1_validate2 %s ===" % time.strftime("%Y-%m-%d %H:%M:%S"))
    q = 23
    genuine = []
    degen = []
    others = []
    ctxs = []
    diag = {}
    for pr in range(2):
        rnd = random.Random(2300 + pr)
        S0 = sorted(rnd.sample(range(q), 7))
        Sinf = sorted(rnd.sample([z for z in range(q) if z not in S0], 7))
        ctx = Ctx(S0, Sinf, q)
        ctxs.append(ctx)
        ng = nd = 0
        for S1 in itertools.combinations(range(q), 7):
            r, tag = raw_test(ctx, S1)
            if r is None:
                if len(others) < 200 and (hash(S1) & 1023) == 0:
                    others.append((pr, S1))
                continue
            u, G, H = r
            ok, fg = full_criterion(ctx, u, G, H)
            if ok:
                genuine.append((pr, S1, u, G, H, fg))
                ng += 1
            else:
                nd += 1
                rGH = nullspace([G, H], 5, q)[1]
                key = (rGH, pdeg(G), pdeg(H))
                diag[key] = diag.get(key, 0) + 1
                if len(degen) < 400:
                    degen.append((pr, S1, u, G, H))
        out("pair %d S_0=%s S_inf=%s : genuine=%d degenerate=%d"
            % (pr, S0, Sinf, ng, nd))
    out("degenerate diagnosis  (rank[G;H], degG, degH) -> count : %s"
        % sorted(diag.items()))
    out("total genuine=%d  (predicted 2 x 86766/23^3 = %.2f)"
        % (len(genuine), 2 * 86766 / float(23 ** 3)))
    rnd2 = random.Random(555)
    sample = [(p, s, "GEN") for p, s, _, _, _, _ in genuine]
    dsel = degen[:]
    rnd2.shuffle(dsel)
    sample += [(p, s, "DEG") for p, s, _, _, _ in dsel[:40]]
    rnd2.shuffle(others)
    sample += [(p, s, "OTH") for p, s in others[:60]]
    agree_full = 0
    agree_raw = 0
    tab = {}
    for pr, S1, cls in sample:
        ctx = ctxs[pr]
        bf = brute(ctx, S1)
        r, tag = raw_test(ctx, S1)
        raw = r is not None
        full = False
        if raw:
            full = full_criterion(ctx, r[0], r[1], r[2])[0]
        if bf == full:
            agree_full += 1
        if bf == raw:
            agree_raw += 1
        tab[(cls, bf, raw, full)] = tab.get((cls, bf, raw, full), 0) + 1
    out("brute-force cross-check on %d triples (%d genuine, %d degenerate,"
        " %d other):" % (len(sample), len(genuine), min(40, len(dsel)),
                         min(60, len(others))))
    out("  agreement with CORRECTED (TEST): %d/%d" % (agree_full, len(sample)))
    out("  agreement with raw rank<=2 only: %d/%d" % (agree_raw, len(sample)))
    out("  (class, brute, rank<=2, corrected) -> count : %s"
        % sorted([(str(k), v) for k, v in tab.items()]))
    out("=== END d1_validate2 wall=%.1fs ===" % (time.time() - t00))


main()
FH.close()

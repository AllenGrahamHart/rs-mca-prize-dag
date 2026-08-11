"""r36_sat3_on_l2 D2: T >= 2 over the REAL domain mu_32, by double prescription.

Prescribe Q_0 = prod_{a in S_0}(x-a) split over mu_32 (slope z=0) AND
Q_2 = beta*prod_{b in S_2}(x-b) split over mu_32 (slope z=infinity), by
solving  L*Q_2 == g^2  (mod f)  exactly, via meet-in-the-middle over the
C(32,7) subsets of mu_32 inside the ring F_q[x]/(f).

Stdlib only.  Writes only d2_results.txt in this directory.
"""
import random

OUT = "notes/pilots_20260811/r36_sat3_on_l2/d2_results.txt"
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


def pinv_mod(a, f, q):
    """inverse of a modulo f, or None"""
    r0, r1 = trim(f), trim(a)
    s0, s1 = [], [1]
    while trim(r1):
        qq, rr = pdivmod(r0, r1, q)
        r0, r1 = r1, rr
        s0, s1 = s1, psub(s0, pmul(qq, s1, q), q)
    if deg(r0) != 0:
        return None
    return pscal(s0, pow(r0[0], q - 2, q), q)


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
        num = [1]
        den = 1
        for j in range(n):
            if j != i:
                num = pmul(num, [(-xs[j]) % q, 1], q)
                den = (den * (xs[i] - xs[j])) % q
        res = padd(res, pscal(num, (ys[i] * pow(den, q - 2, q)) % q, q), q)
    return res


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
    ranks = {}
    for z in range(q):
        ranks[z] = matrank([[(M0[a][b] + z * M1[a][b]) % q for b in range(8)] for a in range(9)], q)
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
    g = None
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


def T_over_domain(Q0, Q1, Q2, q, D, sqt):
    Ds = set(D)
    cnt = {}
    for x in D:
        a0, a1, a2 = peval(Q0, x, q), peval(Q1, x, q), peval(Q2, x, q)
        if a2 == 0 and a1 == 0:
            if a0 == 0:
                return None
            continue
        if a2 == 0:
            z = (-a0 * pow(a1, q - 2, q)) % q
            cnt[z] = cnt.get(z, 0) + 1
            continue
        disc = (a1 * a1 - 4 * a2 * a0) % q
        inv = pow(2 * a2, q - 2, q)
        if disc == 0:
            z = (-a1 * inv) % q
            cnt[z] = cnt.get(z, 0) + 1
        else:
            s = sqt.get(disc)
            if s is None:
                continue
            for sg in (s, (-s) % q):
                z = ((-a1 + sg) * inv) % q
                cnt[z] = cnt.get(z, 0) + 1
    sup = sorted([z for z in cnt if cnt[z] == 7])
    infsup = (deg(Q2) == 7 and sum(1 for x in D if peval(Q2, x, q) == 0) == 7)
    return sup, infsup, cnt


def nrm(u, q):
    u = (u + [0] * 4)[:4]
    for c in u:
        if c:
            iv = pow(c, q - 2, q)
            return tuple((t * iv) % q for t in u)
    return None


def subset_products(pts, f, q, maxk):
    """all subsets of pts of size <= maxk with their product mod f (DFS)."""
    out = [dict() for _ in range(maxk + 1)]
    n = len(pts)

    def rec(i, k, cur, chosen):
        out[k][tuple(chosen)] = cur
        if k == maxk or i == n:
            return
        for j in range(i, n):
            nxt = pdivmod(pmul(cur, [(-pts[j]) % q, 1], q), f, q)[1]
            chosen.append(pts[j])
            rec(j + 1, k + 1, nxt, chosen)
            chosen.pop()
    rec(0, 0, [1], [])
    return out


# ================= MAIN =================
say("# d2_results — r36_sat3_on_l2 — T >= 2 over mu_32 by double prescription")
say("")
say("## method: Q_0 = prod_{S_0}(x-a) prescribed split over mu_32 (slope z=0);")
say("##   f^2 == L Q_0 (mod g) solved by square roots;  k = (f^2-LQ_0)/g;")
say("##   then L*Q_2 == g^2 (mod f) solved EXACTLY over all C(32,7)=3365856")
say("##   subsets S_2 of mu_32 by meet-in-the-middle in F_q[x]/(f);")
say("##   h = (L Q_2 - g^2)/f ;  Q_1 = (fg+hk)/L.  Slope z=infinity is Q_2.")
say("")

for q, NCFG in [(97, 10), (193, 22)]:
    D = mu_N(q, 32)
    sqt = sqrt_table(q)
    rng = random.Random(360000 + q)
    A, Bh = D[:16], D[16:]
    say("### q=%d   mu_32 = %s" % (q, D))
    ncfg = 0
    nsol = 0
    certified = []
    Thist = {}
    while ncfg < NCFG:
        S0 = rng.sample(D, 7)
        Q0 = frompts(S0, q)
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
            continue
        g = frompts(rs, q)
        f = padd(interp(rs, ys, q), pscal(g, rng.randrange(1, q), q), q)
        if deg(f) != 4 or peval(f, ell, q) == 0:
            continue
        if deg(pgcd(f, frompts(D, q), q)) != 0:
            continue
        kk, r = pdivmod(psub(pmul(f, f, q), pmul(L, Q0, q), q), g, q)
        if r or deg(kk) > 4:
            continue
        Linv = pinv_mod(L, f, q)
        if Linv is None:
            continue
        ncfg += 1
        v = pdivmod(pmul(pdivmod(pmul(g, g, q), f, q)[1], Linv, q), f, q)[1]
        vt = nrm(v, q)
        PA = subset_products(A, f, q, 7)
        PB = subset_products(Bh, f, q, 7)
        hits = []
        for j in range(8):
            small, big = (PA[j], PB[7 - j]) if len(PA[j]) <= len(PB[7 - j]) else (PB[7 - j], PA[j])
            tab = {}
            for sub, u in small.items():
                ui = pinv_mod(u, f, q)
                if ui is None:
                    continue
                key = nrm(pdivmod(pmul(v, ui, q), f, q)[1], q)
                tab.setdefault(key, []).append(sub)
            for sub2, u2 in big.items():
                key = nrm(u2, q)
                if key in tab:
                    for sub1 in tab[key]:
                        hits.append(tuple(sorted(set(sub1) | set(sub2))))
        hits = sorted(set([hh for hh in hits if len(hh) == 7]))
        nsol += len(hits)
        for S2 in hits:
            P2 = frompts(list(S2), q)
            LP2 = pdivmod(pmul(L, P2, q), f, q)[1]
            g2 = pdivmod(pmul(g, g, q), f, q)[1]
            # beta with beta*LP2 == g2 mod f
            bet = None
            for i in range(4):
                a_i = LP2[i] if i < len(LP2) else 0
                b_i = g2[i] if i < len(g2) else 0
                if a_i:
                    bet = (b_i * pow(a_i, q - 2, q)) % q
                    break
            if not bet:
                continue
            Q2 = pscal(P2, bet, q)
            num = psub(pmul(L, Q2, q), pmul(g, g, q), q)
            hh, rh = pdivmod(num, f, q)
            if rh or deg(hh) > 4:
                continue
            Q1, r1 = pdivmod(padd(pmul(f, g, q), pmul(hh, kk, q), q), L, q)
            if r1:
                continue
            if deg(Q0) != 7 or deg(Q1) != 7 or deg(Q2) != 7:
                continue
            c = certify(Q0, Q1, Q2, q)
            if (c["s"] != 0 or c["nullity36x32"] < 1 or c["seprank"] != 3
                    or c["generic_rank"] != 7 or not c.get("MZQZ_zero")
                    or c.get("deg_le_1_kernel_dim", 9) != 0):
                Thist["REJ:" + str((c["s"], c["nullity36x32"], c["seprank"],
                                    c.get("generic_rank"), c.get("deg_le_1_kernel_dim")))] = \
                    Thist.get("REJ:" + str((c["s"], c["nullity36x32"], c["seprank"],
                                            c.get("generic_rank"), c.get("deg_le_1_kernel_dim"))), 0) + 1
                continue
            t = T_over_domain(Q0, Q1, Q2, q, D, sqt)
            if t is None:
                continue
            sup, infsup, cnt = t
            TT = len(sup) + (1 if infsup else 0)
            Thist[TT] = Thist.get(TT, 0) + 1
            certified.append((S0, list(S2), f, g, hh, kk, L, Q0, Q1, Q2, c, sup, infsup, cnt))
    say("configs run: %d ; exact solutions S_2 found: %d ; expected C(32,7)/q^3 = %.2f per config"
        % (ncfg, nsol, 3365856.0 / q ** 3))
    say("fully certified doubly-prescribed objects: %d" % len(certified))
    say("T histogram (over mu_32, counting z=infinity): %s" % sorted(
        [(k, v) for k, v in Thist.items() if not isinstance(k, str)]))
    for kk_ in [k for k in Thist if isinstance(k, str)]:
        say("   rejected %s x%d" % (kk_, Thist[kk_]))
    if certified:
        (S0, S2, f, g, hh, kkp, L, Q0, Q1, Q2, c, sup, infsup, cnt) = certified[0]
        say("")
        say("HEADLINE T=2 WITNESS  q=%d" % q)
        say("  S_0 (subset of mu_32, roots of Q_0, slope z=0)      = %s" % sorted(S0))
        say("  S_2 (subset of mu_32, roots of Q_2, slope z=infty)  = %s" % sorted(S2))
        say("  |S_0 cap S_2| = %d" % len(set(S0) & set(S2)))
        say("  f=%s  g=%s  h=%s  k=%s  L=%s" % (f, g, hh, kkp, L))
        say("  Q_0=%s" % Q0)
        say("  Q_1=%s" % Q1)
        say("  Q_2=%s" % Q2)
        say("  degs=%s s=%d seprank=%d nullity(36x32)=%d M(Z)Q_Z==0:%s"
            % (c["degs"], c["s"], c["seprank"], c["nullity36x32"], c["MZQZ_zero"]))
        say("  generic rank=%d  finite rank-drop z=%s ranks=%s  rank at infinity=%d"
            % (c["generic_rank"], c["drops"], c["drop_ranks"], c["rank_inf"]))
        say("  deg<=1 kernel dim=%d  (0 <=> e = m = 2 exactly)" % c["deg_le_1_kernel_dim"])
        say("  y_0=%s" % c["y0"])
        say("  y_1=%s" % c["y1"])
        say("  supported FINITE slopes over mu_32: %s ; z=infinity supported: %s ; T=%d"
            % (sup, infsup, len(sup) + (1 if infsup else 0)))
        dh = {}
        for x in D:
            dd = 0
            if peval(Q0, x, q) == 0:
                dd += 1
            if peval(Q2, x, q) == 0:
                dd += 1
            dh[dd] = dh.get(dd, 0) + 1
        say("  d_x histogram over mu_32 at the 2 supported slopes: %s ; sum d_x = %d"
            % (sorted(dh.items()), sum(k * v for k, v in dh.items())))
        say("  root-count histogram of the members over mu_32 (all q+1 slopes): %s"
            % sorted({}.fromkeys([]) or
                     __import__("collections").Counter(cnt.values()).items()))
    say("")

with open(OUT, "w") as fh:
    fh.write("\n".join(LOG) + "\n")
print("\n".join(LOG))

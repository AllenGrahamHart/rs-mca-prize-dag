"""g5 -- two-field replication of the F-2 cap break at C3 (mu_26).
Fresh duplicate of every helper (anti-import pattern; no module import
anywhere, so the IMPORTED-SCRIPT audit rule is not triggered).
Results APPEND + flush.
"""
import sys, random, itertools

RES = "notes/pilots_20260811/r38_urate_genericity/g5_results.txt"
_F = open(RES, "a")


def emit(s):
    _F.write(s + "\n")
    _F.flush()
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def inv(a, q):
    return pow(a % q, q - 2, q)


def isprime(m):
    if m < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            return m == p
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def subgroup(nn, q):
    for h in range(2, q):
        g = pow(h, (q - 1) // nn, q)
        if g == 1:
            continue
        seen, x = [], 1
        for _ in range(nn):
            seen.append(x)
            x = x * g % q
        if x == 1 and len(set(seen)) == nn:
            return seen
    raise RuntimeError("no subgroup")


def rref(rows, ncols, q):
    M = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(M)):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                f, Mr = M[i][c], M[rk]
                M[i] = [(M[i][t] - f * Mr[t]) % q for t in range(ncols)]
        piv.append(c)
        rk += 1
        if rk == len(M):
            break
    return rk, piv, M


def kernel_from_rref(rk, piv, M, ncols, q):
    ps = set(piv)
    out = []
    for fc in [c for c in range(ncols) if c not in ps]:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        out.append(v)
    return out


def prodat(S, x, q):
    p = 1
    for y in S:
        p = p * (x - y) % q
    return p


def vvals(D, q):
    out = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        out.append(inv(p, q))
    return out


def syn(vals, D, vv, R, q):
    y = []
    for mm in range(R):
        s = 0
        for i, x in enumerate(D):
            e = vals.get(x, 0)
            if e:
                s = (s + e * vv[i] % q * pow(x, mm, q)) % q
        y.append(s % q)
    return y


def locpoly(S, q):
    c = [1]
    for s in S:
        c = [0] + c
        for i in range(len(c) - 1):
            c[i] = (c[i] - s * c[i + 1]) % q
    return c


def hank(y, sg, rho, q):
    return [sum(y[i + j] * sg[j] for j in range(len(sg))) % q for i in range(rho)]


def census(D, y0, y1, r, R, q):
    n, rho = len(D), R - r
    bad = set()
    stats = [0]

    def rec(start, depth, m0, m1):
        if depth == r - 1:
            a0, a1, a2 = m0[0], m0[1], m0[2]
            b0, b1, b2 = m1[0], m1[1], m1[2]
            A = (a0 * b1 - a1 * b0) % q
            B = (a2 * b0 - a0 * b2) % q
            C = (a1 * b2 - a2 * b1) % q
            for idx in range(start, n):
                s = D[idx]
                if ((A * s + B) * s + C) % q:
                    continue
                aa = [(m0[i + 1] - s * m0[i]) % q for i in range(rho)]
                bb = [(m1[i + 1] - s * m1[i]) % q for i in range(rho)]
                nz = -1
                for i in range(rho):
                    if bb[i]:
                        nz = i
                        break
                if nz < 0:
                    if not any(aa):
                        stats[0] += 1
                    continue
                g = (-aa[nz]) * inv(bb[nz], q) % q
                if all((aa[i] + g * bb[i]) % q == 0 for i in range(rho)):
                    bad.add(g)
            return
        lim = n - (r - depth)
        for idx in range(start, lim + 1):
            s = D[idx]
            rec(idx + 1, depth + 1,
                [(m0[i + 1] - s * m0[i]) % q for i in range(len(m0) - 1)],
                [(m1[i + 1] - s * m1[i]) % q for i in range(len(m1) - 1)])

    rec(0, 0, y0[:], y1[:])
    return bad, stats[0]


def fill_blocks(counts, jj, size, rng):
    rem = dict(counts)
    blocks = []
    for b in range(jj):
        left = jj - b
        forced = [p for p, c in rem.items() if c >= left]
        if len(forced) > size:
            return None
        cand = sorted([p for p in rem if rem[p] > 0 and p not in set(forced)],
                      key=lambda p: (-rem[p], rng.random()))
        blk = forced + cand[:size - len(forced)]
        if len(blk) < size:
            return None
        for p in blk:
            rem[p] -= 1
        blocks.append(blk)
    return blocks if all(c == 0 for c in rem.values()) else None


def run(n, k, r, q, seed, jj):
    R, rho = n - k, (n - k) - r
    cap = (2 * (r + 1) - 1) // rho
    a_par = R + 2
    faith = (a_par > R + 1, a_par - 1 > r, 4 * rho < R)
    emit("")
    emit("== F-2 REPLICATION n=%d R=%d r=%d rho=%d q=%d cap=%d target j=%d | FAITHFUL %s %s %s"
         % (n, R, r, rho, q, cap, jj, faith[0], faith[1], faith[2]))
    if not all(faith):
        emit("   ROW EXCLUDED (faithfulness)")
        return
    rng = random.Random(seed)
    D = subgroup(n, q)
    vv = vvals(D, q)
    rp1 = r + 1
    for _s in range(400):
        W = rng.sample(D, rp1)
        Ws = set(W)
        rest = [x for x in D if x not in Ws]
        Ast = W[:2]
        cls = {}
        for Pt in itertools.combinations(rest, rho):
            v0, v1 = prodat(Pt, Ast[0], q), prodat(Pt, Ast[1], q)
            if v0 == 0 or v1 == 0:
                continue
            cls.setdefault(v1 * inv(v0, q) % q, []).append(Pt)
        big = max(cls.values(), key=len)
        if len(big) < jj:
            continue
        others = [x for x in W if x not in set(Ast)]
        need = jj * (rho - 1)
        base, extra = divmod(need, len(others))
        if base + (1 if extra else 0) > jj:
            continue
        for _try in range(60):
            order = others[:]
            rng.shuffle(order)
            cnt = {p: base + (1 if i < extra else 0) for i, p in enumerate(order)}
            bl = fill_blocks(cnt, jj, rho - 1, rng)
            if bl is None:
                continue
            A = [list(Ast) + b for b in bl]
            P = [list(big[i]) for i in rng.sample(range(len(big)), jj)]
            gam = rng.sample(range(1, q), jj)
            zrest = {x: prodat(rest, x, q) for x in W}
            Zt, ok = [], True
            for i in range(jj):
                d = {}
                for x in W:
                    pv = prodat(P[i], x, q)
                    if pv == 0:
                        ok = False
                        break
                    d[x] = zrest[x] * inv(pv, q) % q
                if not ok:
                    break
                Zt.append(d)
            if not ok:
                continue
            pos = {x: i for i, x in enumerate(W)}
            nc = 2 * rp1 + jj
            M = []
            for i in range(jj):
                for x in A[i]:
                    row = [0] * nc
                    row[pos[x]] = 1
                    row[rp1 + pos[x]] = gam[i] % q
                    row[2 * rp1 + i] = Zt[i][x]
                    M.append(row)
            rk, piv, MR = rref(M, nc, q)
            kb = kernel_from_rref(rk, piv, MR, nc, q)
            if not kb:
                continue
            for _t in range(120):
                co = [rng.randrange(q) for _ in kb]
                vec = [sum(co[i] * kb[i][t] for i in range(len(kb))) % q for t in range(nc)]
                lam = vec[2 * rp1:]
                if not all(lam):
                    continue
                e0 = {W[i]: vec[i] for i in range(rp1)}
                e1 = {W[i]: vec[rp1 + i] for i in range(rp1)}
                if all(v == 0 for v in e1.values()):
                    continue
                chi, bd = [], False
                for x in W:
                    if e0[x] == 0 and e1[x] == 0:
                        bd = True
                        break
                    chi.append((1, e0[x] * inv(e1[x], q) % q) if e1[x] else (0, 0))
                if bd:
                    continue
                fib = {(-c[1]) % q for c in chi if c[0] == 1}
                gs = {g % q for g in gam}
                if gs & fib:
                    continue
                y0, y1 = syn(e0, D, vv, R, q), syn(e1, D, vv, R, q)
                okall = True
                for i in range(jj):
                    Ai = set(A[i])
                    S = [x for x in W if x not in Ai] + list(P[i])
                    if len(S) != r:
                        okall = False
                        break
                    sg = locpoly(S, q)
                    h0, h1 = hank(y0, sg, rho, q), hank(y1, sg, rho, q)
                    if any((h0[t] + gam[i] * h1[t]) % q for t in range(rho)):
                        okall = False
                        break
                if not okall:
                    continue
                emit("   m=2 class size %d ; j=%d CONSTRUCTED rank=%d dimker=%d |chi(W)|=%d collisions=%d"
                     % (len(big), jj, rk, len(kb), len(set(chi)), len(chi) - len(set(chi))))
                bad, ncom = census(D, y0, y1, r, R, q)
                emit("   FULL CENSUS C(%d,%d): T=%d T_fib=%d T_eng=%d/%d T_other=%d common=%d COLUMN-%s"
                     % (n, r, len(bad), len(bad & fib), len(bad & gs), jj,
                        len(bad - fib - gs), ncom, "FAR" if ncom == 0 else "CLOSE"))
                emit("   VERDICT: cap %s  (T=%d vs (r+1)+cap=%d)"
                     % ("BROKEN" if len(bad) > (r + 1) + cap else "HOLDS", len(bad), (r + 1) + cap))
                return
    emit("   j=%d not realised (SEARCH RESULT, not a maximum)" % jj)


if __name__ == "__main__":
    emit("################ g5 two-field replication ################")
    run(26, 13, 10, 500111, 5101, 9)
    run(26, 13, 10, 300301, 5102, 9)
    emit("################ g5 done ################")

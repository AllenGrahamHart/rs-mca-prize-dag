"""g1 -- R2b rank formula + contiguous j ladder (max attainable j).

Self-contained: no imports of any banked module (anti-import pattern).
Results file opened in APPEND mode, flushed after every emit.
"""
import sys, random

RES = "notes/pilots_20260811/r38_urate_genericity/g1_results.txt"
_F = open(RES, "a")


def emit(s):
    _F.write(s + "\n")
    _F.flush()
    sys.stdout.write(s + "\n")


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


def prime_for_subgroup(nn, lo):
    c = lo + (nn - lo % nn) % nn + 1
    while True:
        if isprime(c):
            return c
        c += nn


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
                f = M[i][c]
                Mr = M[rk]
                M[i] = [(M[i][t] - f * Mr[t]) % q for t in range(ncols)]
        piv.append(c)
        rk += 1
        if rk == len(M):
            break
    return rk, piv, M


def kernel_from_rref(rk, piv, M, ncols, q):
    free = [c for c in range(ncols) if c not in set(piv)]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis


def build_domain(kind, n, q):
    if kind == "intZ":
        m = n // 2
        return [(-x) % q for x in range(1, m + 1)] + [x % q for x in range(1, m + 1)]
    return subgroup(n, q)


def vvals(D, q):
    v = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        v.append(inv(p, q))
    return v


def prodat(S, x, q):
    p = 1
    for y in S:
        p = p * (x - y) % q
    return p


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


def hank(y, sg, rho, q):
    return [sum(y[i + j] * sg[j] for j in range(len(sg))) % q for i in range(rho)]


def locpoly(S, q):
    c = [1]
    for s in S:
        c = [0] + c
        for i in range(len(c) - 1):
            c[i] = (c[i] - s * c[i + 1]) % q
    return c


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


def make_design(kind, W, jj, rho, rng):
    rp1 = len(W)
    if kind == "m1":
        xs, rest = W[0], W[1:]
        need = jj * rho
        if need > jj * len(rest):
            return None
        base, extra = divmod(need, len(rest))
        if base + (1 if extra else 0) > jj:
            return None
        order = rest[:]
        rng.shuffle(order)
        cnt = {p: base + (1 if i < extra else 0) for i, p in enumerate(order)}
        bl = fill_blocks(cnt, jj, rho, rng)
        return None if bl is None else [[xs] + b for b in bl]
    if kind == "flat":
        tot = jj * (rho + 1)
        base, extra = divmod(tot, rp1)
        if base + (1 if extra else 0) > jj:
            return None
        order = W[:]
        rng.shuffle(order)
        cnt = {p: base + (1 if i < extra else 0) for i, p in enumerate(order)}
        return fill_blocks(cnt, jj, rho + 1, rng)
    return [rng.sample(W, rho + 1) for _ in range(jj)]


def phi_matrix(A, gam, Zt, W, jj, q):
    Ix = {x: [] for x in W}
    for i in range(jj):
        for x in A[i]:
            Ix[x].append(i)
    L = n0 = n1 = 0
    rows = []
    for x in W:
        d = len(Ix[x])
        if d == 0:
            n0 += 1
        elif d == 1:
            n1 += 1
        if d >= 3:
            a, b = Ix[x][0], Ix[x][1]
            for s in Ix[x][2:]:
                L += 1
                row = [0] * jj
                row[a] = Zt[a][x] * (gam[s] - gam[b]) % q
                row[b] = (-Zt[b][x] * (gam[s] - gam[a])) % q
                row[s] = Zt[s][x] * (gam[b] - gam[a]) % q
                rows.append(row)
    return rows, L, n0, n1


def run_cell(name, kind, n, k, r, q, tries, ktries, seed, extra=3):
    rng = random.Random(seed)
    R, rho = n - k, (n - k) - r
    a_par = R + 2
    faith = (a_par > R + 1, a_par - 1 > r, 4 * rho < R)
    emit("")
    emit("== CELL %s [%s] n=%d k=%d R=%d r=%d rho=%d q=%d | FAITHFUL a>R+1=%s a-1>r=%s 4rho<R=%s"
         % (name, kind, n, k, R, r, rho, q, faith[0], faith[1], faith[2]))
    if not all(faith):
        emit("   ROW EXCLUDED FROM CONCLUSIONS (faithfulness)")
        return
    cap_a, cap_m = (2 * (r + 1) - 1) // rho, (2 * r) // rho
    emit("   cap_anchor=%d  cap_mine(A-5)=%d  DISCRIMINATING=%s" % (cap_a, cap_m, cap_a != cap_m))
    D = build_domain(kind, n, q)
    vv = vvals(D, q)
    rp1 = r + 1
    best, fok, fbad, kok, kbad = 0, 0, 0, 0, 0
    for jj in range(1, cap_a + 1 + extra):
        found = None
        for att in range(tries):
            W = rng.sample(D, rp1)
            Ws = set(W)
            rest = [x for x in D if x not in Ws]
            dk = ["m1", "flat", "rand"][att % 3]
            A = make_design(dk, W, jj, rho, rng)
            if A is None:
                continue
            P = [rng.sample(rest, rho) for _ in range(jj)]
            if len({tuple(sorted(p)) for p in P}) < jj:
                continue
            gam = rng.sample(range(1, q), jj)
            zrest = {x: prodat(rest, x, q) for x in W}
            Zt = []
            ok = True
            for i in range(jj):
                d = {}
                for x in W:
                    pv = prodat(P[i], x, q)
                    if pv == 0 or zrest[x] == 0:
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
            Ph, L, n0, n1 = phi_matrix(A, gam, Zt, W, jj, q)
            rkp = rref(Ph, jj, q)[0] if Ph else 0
            pred = jj * (rho + 1) - L + rkp
            if pred == rk:
                fok += 1
            else:
                fbad += 1
                emit("   !! R2b-1 VIOLATED j=%d des=%s rank=%d pred=%d L=%d rkPhi=%d" % (jj, dk, rk, pred, L, rkp))
            kb = kernel_from_rref(rk, piv, MR, nc, q)
            if len(kb) == (jj - rkp) + 2 * n0 + n1:
                kok += 1
            else:
                kbad += 1
                emit("   !! R2b-2 VIOLATED j=%d dim=%d pred=%d" % (jj, len(kb), (jj - rkp) + 2 * n0 + n1))
            if not kb:
                continue
            for _t in range(ktries):
                co = [rng.randrange(q) for _ in kb]
                vec = [sum(co[i] * kb[i][t] for i in range(len(kb))) % q for t in range(nc)]
                lam = vec[2 * rp1:]
                if any(l == 0 for l in lam):
                    continue
                e0 = {W[i]: vec[i] for i in range(rp1)}
                e1 = {W[i]: vec[rp1 + i] for i in range(rp1)}
                if all(v == 0 for v in e1.values()):
                    continue
                chi, degen = [], False
                for x in W:
                    if e0[x] == 0 and e1[x] == 0:
                        degen = True
                        break
                    chi.append((1, e0[x] * inv(e1[x], q) % q) if e1[x] else (0, 0))
                if degen:
                    continue
                coll = len(chi) - len(set(chi))
                fib = {(-c[1]) % q for c in chi if c[0] == 1}
                if any(g % q in fib for g in gam):
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
                if okall:
                    found = (dk, coll, len(kb), L, rkp, n0, n1)
                    break
            if found:
                break
        if found:
            best = jj
            emit("   j=%2d REACHED des=%s chi-coll=%d dimker=%d L=%d rkPhi=%d n0=%d n1=%d"
                 % (jj, found[0], found[1], found[2], found[3], found[4], found[5], found[6]))
        else:
            emit("   j=%2d not found in %dx%d (SEARCH RESULT, not a maximum)" % (jj, tries, ktries))
    emit("   LARGEST j REACHED = %d  (cap_anchor=%d cap_mine=%d)" % (best, cap_a, cap_m))
    emit("   R2b-1: %d confirmed / %d violated ;  R2b-2: %d / %d" % (fok, fbad, kok, kbad))


CELLS = [("C1", 20, 10, 8), ("C7", 22, 11, 9), ("C2", 24, 12, 10),
         ("C3", 26, 13, 10), ("C6", 28, 14, 11), ("C11", 32, 16, 13),
         ("C4", 34, 17, 13), ("C9", 36, 18, 14)]

if __name__ == "__main__":
    emit("################ g1 rank/ladder run ################")
    sd = 12345
    for (nm, n, k, r) in CELLS:
        run_cell(nm, "intZ", n, k, r, 65537, 10, 25, sd)
        sd += 1
        qm = prime_for_subgroup(n, 200000)
        run_cell(nm, "mu", n, k, r, qm, 10, 25, sd)
        sd += 1
    emit("################ g1 done ################")

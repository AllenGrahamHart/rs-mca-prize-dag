"""g2 -- exhaustive C(n,r) censuses of the AT-CAP constructed pencils.

Self-contained (no imports of banked modules). Results APPEND + flush.
Cheap cells first so a wall-clock stop still banks them.
"""
import sys, random

RES = "notes/pilots_20260811/r38_urate_genericity/g2_results.txt"
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


def build_domain(kind, n, q):
    if kind == "intZ":
        m = n // 2
        return [(-x) % q for x in range(1, m + 1)] + [x % q for x in range(1, m + 1)]
    return subgroup(n, q)


def vvals(D, q):
    out = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        out.append(inv(p, q))
    return out


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


def construct(D, r, R, q, jj, rng, vv, tries=400):
    """m=1 design at j = jj. Returns dict or None."""
    rho = R - r
    rp1 = r + 1
    for _att in range(tries):
        W = rng.sample(D, rp1)
        Ws = set(W)
        rest = [x for x in D if x not in Ws]
        xs, others = W[0], W[1:]
        need = jj * rho
        base, extra = divmod(need, len(others))
        if base + (1 if extra else 0) > jj:
            return None
        order = others[:]
        rng.shuffle(order)
        cnt = {p: base + (1 if i < extra else 0) for i, p in enumerate(order)}
        bl = fill_blocks(cnt, jj, rho, rng)
        if bl is None:
            continue
        A = [[xs] + b for b in bl]
        P = [rng.sample(rest, rho) for _ in range(jj)]
        if len({tuple(sorted(p)) for p in P}) < jj:
            continue
        gam = rng.sample(range(1, q), jj)
        zrest = {x: prodat(rest, x, q) for x in W}
        Zt, ok = [], True
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
        kb = kernel_from_rref(rk, piv, MR, nc, q)
        if not kb:
            continue
        for _t in range(80):
            co = [rng.randrange(q) for _ in kb]
            vec = [sum(co[i] * kb[i][t] for i in range(len(kb))) % q for t in range(nc)]
            lam = vec[2 * rp1:]
            if any(l == 0 for l in lam):
                continue
            e0 = {W[i]: vec[i] for i in range(rp1)}
            e1 = {W[i]: vec[rp1 + i] for i in range(rp1)}
            if all(v == 0 for v in e1.values()):
                continue
            chi, bad = [], False
            for x in W:
                if e0[x] == 0 and e1[x] == 0:
                    bad = True
                    break
                chi.append((1, e0[x] * inv(e1[x], q) % q) if e1[x] else (0, 0))
            if bad:
                continue
            coll = len(chi) - len(set(chi))
            fib = {(-c[1]) % q for c in chi if c[0] == 1}
            if any(g % q in fib for g in gam):
                continue
            return dict(W=W, A=A, P=P, gam=[g % q for g in gam], e0=e0, e1=e1,
                        chi=chi, coll=coll, fib=fib, dimker=len(kb), rank=rk)
    return None


def census(D, y0, y1, r, R, q):
    """Exhaustive sweep of all C(n,r) split locators. Returns (bad set, ncommon, nleaf)."""
    n, rho = len(D), R - r
    bad = set()
    stats = [0, 0]  # common locators, leaves

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
                stats[1] += 1
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
    return bad, stats[0], stats[1]


def run(name, kind, n, k, r, q, seed):
    R, rho = n - k, (n - k) - r
    a_par = R + 2
    faith = (a_par > R + 1, a_par - 1 > r, 4 * rho < R)
    jj = (2 * (r + 1) - 1) // rho
    emit("")
    emit("== CENSUS %s [%s] n=%d k=%d R=%d r=%d rho=%d q=%d j=%d(cap) | FAITHFUL %s %s %s"
         % (name, kind, n, k, R, r, rho, q, jj, faith[0], faith[1], faith[2]))
    if not all(faith):
        emit("   ROW EXCLUDED (faithfulness)")
        return
    rng = random.Random(seed)
    D = build_domain(kind, n, q)
    vv = vvals(D, q)
    cfg = construct(D, r, R, q, jj, rng, vv)
    if cfg is None:
        emit("   no valid configuration found at j=%d (SEARCH RESULT)" % jj)
        return
    y0 = syn(cfg["e0"], D, vv, R, q)
    y1 = syn(cfg["e1"], D, vv, R, q)
    bad, ncommon, nleaf = census(D, y0, y1, r, R, q)
    fib = cfg["fib"]
    Tfib = len(bad & fib)
    eng = set(cfg["gam"])
    Teng = len(bad & eng)
    Tother = len(bad - fib - eng)
    cnr = 1
    for i in range(r):
        cnr = cnr * (n - i) // (i + 1)
    emit("   C(n,r)=%d  |chi(W)|=%d  chi-collisions=%d  dimker=%d" % (cnr, len(fib), cfg["coll"], cfg["dimker"]))
    emit("   T=%d  T_fib(present)=%d  T_eng=%d/%d  T_other=%d  | PREDICTED T=(r+1)+j=%d"
         % (len(bad), Tfib, Teng, jj, Tother, (r + 1) + jj))
    emit("   common locators=%d  => COLUMN-%s   (proportional-leaf hits=%d)"
         % (ncommon, "FAR" if ncommon == 0 else "CLOSE", nleaf))
    mu1 = float(cnr) / (float(q) ** rho)
    emit("   mu_1=C(n,r)/q^rho=%.6g  q*mu_1=%.6g  (ZP-3: descriptor only, zero power)" % (mu1, q * mu1))


if __name__ == "__main__":
    emit("################ g2 census run ################")
    run("C1", "mu", 20, 10, 8, prime_for_subgroup(20, 200000), 7001)
    run("C1", "mu", 20, 10, 8, prime_for_subgroup(20, 500000), 7002)
    run("C1", "intZ", 20, 10, 8, 65537, 7003)
    run("C7", "mu", 22, 11, 9, prime_for_subgroup(22, 200000), 7004)
    run("C7", "intZ", 22, 11, 9, 65537, 7005)
    run("C2", "mu", 24, 12, 10, prime_for_subgroup(24, 200000), 7006)
    run("C3", "mu", 26, 13, 10, 200201, 7007)
    emit("################ g2 done ################")

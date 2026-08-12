"""g3 -- (a) exhaustive projective sweep of the 4 side-conditions,
         (b) exhaustive rank-drop (Z_{P_i}|_{A*} proportional) search,
         (c) R2k coset identity Z_{cH}=X^d-c^d and its m<=2 consequence,
         (d) carrier exhaustiveness at odd r (R2l).
Self-contained. Results APPEND + flush.
"""
import sys, random, itertools

RES = "notes/pilots_20260811/r38_urate_genericity/g3_results.txt"
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


def prodat(S, x, q):
    p = 1
    for y in S:
        p = p * (x - y) % q
    return p


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


# ---------------- (a) exhaustive projective side-condition sweep -------------
def sweep(name, kind, n, k, r, q, seed):
    R, rho = n - k, (n - k) - r
    jj = (2 * (r + 1) - 1) // rho
    a_par = R + 2
    faith = (a_par > R + 1, a_par - 1 > r, 4 * rho < R)
    emit("")
    emit("== (a) PROJECTIVE SWEEP %s [%s] n=%d R=%d r=%d rho=%d q=%d j=%d | FAITHFUL %s %s %s"
         % (name, kind, n, R, r, rho, q, jj, faith[0], faith[1], faith[2]))
    if not all(faith):
        emit("   ROW EXCLUDED (faithfulness)")
        return
    rng = random.Random(seed)
    D = build_domain(kind, n, q)
    rp1 = r + 1
    for _att in range(200):
        W = rng.sample(D, rp1)
        Ws = set(W)
        rest = [x for x in D if x not in Ws]
        xs, others = W[0], W[1:]
        base, extra = divmod(jj * rho, len(others))
        if base + (1 if extra else 0) > jj:
            emit("   design infeasible")
            return
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
        if len(kb) != 2:
            continue
        b1, b2 = kb
        invs = [0] * q
        if q > 1:
            invs[1] = 1
        for i in range(2, q):
            invs[i] = (q - (q // i) * invs[q % i] % q) % q
        bad_lam = bad_chi = bad_fib = bad_supp = good = 0
        pts = [(1, t) for t in range(q)] + [(0, 1)]
        gset = {g % q for g in gam}
        for (c1, c2) in pts:
            lam = [(c1 * b1[t] + c2 * b2[t]) % q for t in range(2 * rp1, nc)]
            if not all(lam):
                bad_lam += 1
                continue
            vec = [(c1 * b1[t] + c2 * b2[t]) % q for t in range(2 * rp1)]
            e0 = vec[:rp1]
            e1 = vec[rp1:]
            if any(e0[i] == 0 and e1[i] == 0 for i in range(rp1)):
                bad_supp += 1
                continue
            chi = []
            for i in range(rp1):
                chi.append((1, e0[i] * invs[e1[i]] % q) if e1[i] else (0, 0))
            if len(set(chi)) < rp1:
                bad_chi += 1
                continue
            fib = {(-c[1]) % q for c in chi if c[0] == 1}
            if gset & fib:
                bad_fib += 1
                continue
            good += 1
        emit("   q+1=%d projective kernel points:  lambda_i=0 for %d  (R2e PREDICTS EXACTLY j=%d)"
             % (q + 1, bad_lam, jj))
        emit("   chi non-injective %d (R2g bound 2*C(r+1,2)=%d) ; gamma_i on fibre %d (R2f bound j(r+1)=%d) ; (e0,e1)=0 somewhere %d ; ALL FOUR OK %d"
             % (bad_chi, 2 * (rp1 * (rp1 - 1) // 2), bad_fib, jj * rp1, bad_supp, good))
        emit("   R2e VERDICT: %s" % ("EXACT HIT" if bad_lam == jj else "MISS (bad_lam=%d != j=%d)" % (bad_lam, jj)))
        return
    emit("   no dimker=2 design found (SEARCH RESULT)")


# ---------------- (b) exhaustive rank-drop search ---------------------------
def rankdrop(name, kind, n, k, r, q, seed):
    R, rho = n - k, (n - k) - r
    emit("")
    emit("== (b) RANK-DROP SEARCH %s [%s] n=%d r=%d rho=%d q=%d" % (name, kind, n, r, rho, q))
    rng = random.Random(seed)
    D = build_domain(kind, n, q)
    W = rng.sample(D, r + 1)
    Ws = set(W)
    rest = [x for x in D if x not in Ws]
    allP = list(itertools.combinations(rest, rho))
    emit("   |D\\W|=%d  #rho-subsets P enumerated EXHAUSTIVELY = %d" % (len(rest), len(allP)))
    for m in (2, 3, 4):
        if m > r + 1:
            continue
        Ast = W[:m]
        classes = {}
        for Pt in allP:
            vals = [prodat(Pt, x, q) for x in Ast]
            if any(v == 0 for v in vals):
                continue
            iv = inv(vals[0], q)
            key = tuple(v * iv % q for v in vals[1:])
            classes.setdefault(key, 0)
            classes[key] += 1
        mx = max(classes.values()) if classes else 0
        nsing = sum(1 for v in classes.values() if v == 1)
        emit("   m=%d |A*|=%d : %d distinct projective classes, LARGEST class = %d, singletons = %d"
             % (m, m, len(classes), mx, nsing))
    emit("   (B-11 predicts largest class small; a rank drop needs a class of size >= j)")


# ---------------- (c) coset identity ---------------------------------------
def coset_identity(n, lo):
    q = prime_for_subgroup(n, lo)
    D = subgroup(n, q)
    emit("")
    emit("== (c) R2k COSET IDENTITY on mu_%d < F_%d" % (n, q))
    g = D[1]
    okall = True
    for d in [d for d in range(2, n) if n % d == 0]:
        H = [pow(g, (n // d) * t, q) for t in range(d)]
        for c in (D[3], D[7 % n], D[1]):
            P = [c * h % q for h in H]
            for x in D:
                if x in set(P):
                    continue
                lhs = prodat(P, x, q)
                rhs = (pow(x, d, q) - pow(c, d, q)) % q
                if lhs != rhs:
                    okall = False
        emit("   d=%d (|H|=%d): Z_{cH}(X) = X^d - c^d  verified for 3 cosets x all x in mu_n : %s"
             % (d, d, okall))
    emit("   R2k CONSEQUENCE (m<=2 on coset families): identity holds = %s" % okall)


# ---------------- (d) carrier exhaustiveness -------------------------------
def carrier(n, k, r, q):
    R, rho = n - k, (n - k) - r
    a_par = R + 2
    faith = (a_par > R + 1, a_par - 1 > r, 4 * rho < R)
    m = n // 2
    D = [(-x) % q for x in range(1, m + 1)] + [x % q for x in range(1, m + 1)]
    emit("")
    emit("== (d) CARRIER EXHAUSTIVENESS n=%d k=%d R=%d r=%d(ODD=%s) rho=%d q=%d | FAITHFUL %s %s %s"
         % (n, k, R, r, r % 2 == 1, rho, q, faith[0], faith[1], faith[2]))
    if not all(faith):
        emit("   ROW EXCLUDED (faithfulness)")
        return
    Dset = set(D)
    nprop = ncar = nboth = nprop_only = ncar_only = 0
    tot = 0
    for S in itertools.combinations(D, r):
        tot += 1
        c = [1]
        for s in S:
            c = [0] + c
            for i in range(len(c) - 1):
                c[i] = (c[i] - s * c[i + 1]) % q
        se = c[0::2]
        so = c[1::2]
        L = max(len(se), len(so))
        se = se + [0] * (L - len(se))
        so = so + [0] * (L - len(so))
        dep = True
        for i in range(L):
            for jx in range(i + 1, L):
                if (se[i] * so[jx] - se[jx] * so[i]) % q:
                    dep = False
                    break
            if not dep:
                break
        Ss = set(S)
        lone = sum(1 for x in Ss if (-x) % q not in Ss)
        car = (lone == 1)
        if dep:
            nprop += 1
        if car:
            ncar += 1
        if dep and car:
            nboth += 1
        if dep and not car:
            nprop_only += 1
        if car and not dep:
            ncar_only += 1
    emit("   swept %d split locators of degree exactly r" % tot)
    emit("   #{sigma^e prop sigma^o} = %d ; #{(X-x_0)P(X^2) form} = %d ; both = %d" % (nprop, ncar, nboth))
    emit("   prop-but-NOT-carrier = %d ; carrier-but-NOT-prop = %d" % (nprop_only, ncar_only))
    emit("   R2l VERDICT: %s" % ("EXHAUSTIVE (excess 0 both ways)" if (nprop_only == 0 and ncar_only == 0)
                                 else "REFUTED -- a NEW carrier exists"))


if __name__ == "__main__":
    emit("################ g3 side-conditions / rank-drop / carrier ################")
    sweep("C1", "mu", 20, 10, 8, prime_for_subgroup(20, 200000), 8001)
    sweep("C1", "intZ", 20, 10, 8, 65537, 8002)
    sweep("C7", "mu", 22, 11, 9, prime_for_subgroup(22, 200000), 8003)
    sweep("C2", "mu", 24, 12, 10, prime_for_subgroup(24, 200000), 8004)
    rankdrop("C3", "mu", 26, 13, 10, 200201, 8005)
    rankdrop("C1", "mu", 20, 10, 8, prime_for_subgroup(20, 200000), 8006)
    rankdrop("C9", "intZ", 36, 18, 14, 65537, 8007)
    coset_identity(20, 200000)
    coset_identity(24, 500000)
    carrier(18, 9, 7, 65537)
    carrier(18, 9, 7, 999983)
    carrier(22, 11, 9, 65537)
    emit("################ g3 done ################")

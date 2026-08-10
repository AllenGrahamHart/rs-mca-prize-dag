"""D1/D3: test the registered apolar-origin characterization C.

C says a far-CA supported slope is a K-coset with a UNIQUE minimum-weight
D-representative, where K = {c in F^D : sum_x c_x x^i = 0, i < R} is the
[N, N-R, R+1] MDS kernel code.  Everything below is measured, not assumed.

Measured functionals (CATCH-19C):
  w(y)      = minimum weight of a D-representation of the syndrome y
              (= distance of the coset y+K to 0 in F^D).
  S_gamma   = support of the (unique when w<=rho) minimiser at slope gamma.
  w*        = min |S| over S supporting BOTH y_0 and y_1  (column-far <=> w*>r).
  n_gamma   = # x in W with c_{0,x}+gamma c_{1,x}=0, for a joint support W.
  T         = # finite supported slopes.
  T1,T2     = type-1 / type-2 counts of the registered dichotomy (C2).

Stdlib only.  Run under tools/ramguard.
"""
import itertools


def say(s=""):
    print(str(s), flush=True)


def subgroup(q, N):
    for cand in range(2, q):
        x, order = 1, 0
        while True:
            x = x * cand % q
            order += 1
            if x == 1:
                break
        if order == q - 1:
            g = cand
            break
    h = pow(g, (q - 1) // N, q)
    D, x = [], 1
    for _ in range(N):
        D.append(x)
        x = x * h % q
    return sorted(D)


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv, r = [], 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if M[i][c] % q:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [v * iv % q for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][t] - f * M[r][t]) % q for t in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def solve(A, b, q):
    """solve A z = b over F_q; return one solution or None."""
    rows = len(A)
    cols = len(A[0]) if rows else 0
    M = [A[i][:] + [b[i]] for i in range(rows)]
    Mr, piv = rref(M, q)
    if cols in piv:
        return None                       # inconsistent
    z = [0] * cols
    for i, c in enumerate(piv):
        z[c] = Mr[i][cols] % q
    return z


def moments(S, D, q, R):
    """columns = moment vectors x^0..x^{R-1} for x in S."""
    return [[pow(x, i, q) for x in S] for i in range(R)]


def min_support(y, D, q, R, cap):
    """min-weight D-representation of syndrome y, searching |S| <= cap.
    Returns (weight, support tuple) or (None, None)."""
    for wgt in range(0, cap + 1):
        for S in itertools.combinations(D, wgt):
            A = moments(S, D, q, R)
            z = solve(A, list(y), q)
            if z is not None and all(v % q for v in z):
                return wgt, S
    return None, None


def joint_min_support(y0, y1, D, q, R, cap):
    for wgt in range(0, cap + 1):
        for S in itertools.combinations(D, wgt):
            A = moments(S, D, q, R)
            if solve(A, list(y0), q) is None:
                continue
            if solve(A, list(y1), q) is None:
                continue
            return wgt, S
    return None, None


def analyse(name, y0, y1, q, N, R, r, e):
    D = subgroup(q, N)
    rho = r
    say("### %s : q=%d N=%d R=%d r=rho=%d e=%d  A=%d" % (name, q, N, R, r, e, R + 1 - 2 * r))
    say("    d(K)=R+1=%d   d(K')=R-r+1=%d   2rho=%d" % (R + 1, R - r + 1, 2 * rho))
    sup = {}
    unsup_w = []
    for g in range(q):
        y = [(y0[t] + g * y1[t]) % q for t in range(R)]
        wgt, S = min_support(y, D, q, R, rho)
        if wgt is not None:
            sup[g] = (wgt, S)
        else:
            # measure the true coset weight up to rho+3
            w2, S2 = min_support(y, D, q, R, min(rho + 3, N))
            unsup_w.append(w2 if w2 is not None else -1)
    T = len(sup)
    say("    T = %d supported finite slopes (target rho+1=%d, cap rho+2=%d)"
        % (T, rho + 1, rho + 2))
    for g in sorted(sup):
        say("      slope %-3d |S|=%d  S=%s" % (g, sup[g][0], sup[g][1]))
    if unsup_w:
        lo = min(x for x in unsup_w if x != -1) if any(x != -1 for x in unsup_w) else -1
        say("    unsupported slopes: min measured coset weight = %s "
            "(C predicts >= R-r+1+rho... i.e. >= %d)" % (lo, R - r + 1))
    # injectivity (C1)
    sets = [sup[g][1] for g in sorted(sup)]
    say("    (C1) injectivity of gamma|->S_gamma : %s"
        % ("HOLDS" if len(set(sets)) == len(sets) else "FAILS"))
    # pairwise unions
    pairs = []
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            u = len(set(sets[i]) | set(sets[j]))
            pairs.append((u, i, j))
    if pairs:
        amin = min(p[0] for p in pairs)
        amax = max(p[0] for p in pairs)
        say("    pairwise |S_i u S_j| in [%d, %d]" % (amin, amax))
    # joint minimal support
    wstar, Sstar = joint_min_support(y0, y1, D, q, R, min(2 * rho, N))
    say("    w* = %s   S* = %s   (column-far <=> w* > r=%d : %s)"
        % (wstar, Sstar, r, "YES" if (wstar or 0) > r else "NO"))
    if wstar is None:
        return
    # dichotomy on W = S*
    A = moments(Sstar, D, q, R)
    c0 = solve(A, list(y0), q)
    c1 = solve(A, list(y1), q)
    t1, t2 = [], []
    for g in sorted(sup):
        z = [(c0[t] + g * c1[t]) % q for t in range(wstar)]
        n_g = sum(1 for v in z if v % q == 0)
        zsupp = set(Sstar[t] for t in range(wstar) if z[t] % q)
        Sg = set(sup[g][1])
        if zsupp <= Sg:
            t1.append((g, n_g))
        else:
            t2.append((g, n_g, len(Sg - set(Sstar)), len(Sg & set(Sstar))))
    say("    (C2) type-1 slopes %s" % ([g for g, _ in t1],))
    say("         type-1 n_gamma = %s   (C predicts a-rho+o = %d each)"
        % ([n for _, n in t1], wstar - rho))
    say("         sum n over type-1 = %d <= a = %d"
        % (sum(n for _, n in t1), wstar))
    say("    (C2) type-2 slopes %s" % ([g for g, _, _, _ in t2],))
    for g, n_g, out, ins in t2:
        say("         slope %-3d n=%d |S\\W|=%d (C bound >= %d)  |S n W|=%d "
            "(C bound <= %d)" % (g, n_g, out, R + 1 - wstar + n_g, ins,
                                 wstar - n_g - (R - r + 1)))
    say("    T1=%d  T2=%d   (C3) cap T1 <= e+1 = %d : %s"
        % (len(t1), len(t2), e + 1, "OK" if len(t1) <= e + 1 else "VIOLATED"))
    say("    (AO1) = %d" % ao1(N, R, rho, e, wstar, 0))
    say()


def ao1(N, R, rho, e, a, O):
    t1 = min(e + 1, a // (a - rho) if a > rho else 10 ** 9, (a * e + O) // rho)
    if a >= R + 1:
        return None
    t2 = ((N - a) * e) // (R + 1 - a)
    return t1 + t2


# ---------------------------------------------------------------- fence
say("=== (1) the PROVED m=1 fence witness over F_17 (M1F2) ===")
analyse("m=1 fence",
        [1, 10, 16, 2, 14, 0, 3, 11],
        [0, 14, 9, 7, 13, 12, 15, 0],
        17, 16, 8, 3, 1)

# ------------------------------------------------------- cyclotomic real
say("=== (2) the realizable cyclotomic N=12 pencil (round-27 case (c)) ===")


def cyclo_pencil(q, N, R, rho):
    """rebuild the realizable pencil of round-27 case (c) from the
    Hankel realizability system, exactly as d1_realizability.py did."""
    D = subgroup(q, N)
    cubes = sorted({pow(x, rho, q) for x in D})
    sups = [tuple(sorted(x for x in D if pow(x, rho, q) == c)) for c in cubes]
    def pfr(S):
        c = [1]
        for x in S:
            nc = [0] * (len(c) + 1)
            for i, ci in enumerate(c):
                nc[i] = (nc[i] - x * ci) % q
                nc[i + 1] = (nc[i + 1] + ci) % q
            c = nc
        return c
    polys = [pfr(S) for S in sups]
    p0, p1 = polys[0], polys[1]
    direction = [(p1[i] - p0[i]) % q for i in range(rho + 1)]
    rows = []
    mrows = R - rho
    for deg in range(3):
        for i in range(mrows):
            row = [0] * (2 * R)
            for j in range(rho + 1):
                if deg == 0:
                    row[i + j] = (row[i + j] + p0[j]) % q
                elif deg == 1:
                    row[i + j] = (row[i + j] + direction[j]) % q
                    row[R + i + j] = (row[R + i + j] + p0[j]) % q
                else:
                    row[R + i + j] = (row[R + i + j] + direction[j]) % q
            rows.append(row)
    Mr, piv = rref(rows, q)
    free = [c for c in range(2 * R) if c not in piv]
    sols = []
    for f in free:
        v = [0] * (2 * R)
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        sols.append(v)
    return sols


sols = cyclo_pencil(13, 12, 6, 3)
say("    Hankel system nullity = %d" % len(sols))
for idx, s in enumerate(sols):
    analyse("cyclotomic N=12 sol%d" % idx, s[:6], s[6:], 13, 12, 6, 3, 1)
say("=== END part 1 ===")

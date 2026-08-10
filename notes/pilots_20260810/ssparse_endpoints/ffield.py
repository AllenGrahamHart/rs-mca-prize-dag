"""Shared exact F_q linear algebra + RS scaled-row helpers (stdlib only)."""


def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def primes_1_mod(n, count, start=2):
    out = []
    x = start - start % n + 1
    while len(out) < count:
        if x > start and is_prime(x):
            out.append(x)
        x += n
    return out


def subgroup(n, q):
    """the order-n subgroup of F_q^* (needs n | q-1)"""
    assert (q - 1) % n == 0
    fac = set()
    m = q - 1
    d = 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fac):
        g += 1
    h = pow(g, (q - 1) // n, q)
    S = [pow(h, i, q) for i in range(n)]
    assert len(set(S)) == n
    return S


def poly_from_roots(R, q):
    p = [1]
    for r in R:
        new = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            new[i] = (new[i] - c * r) % q
            new[i + 1] = (new[i + 1] + c) % q
        p = new
    return p                       # p[i] = coeff of X^i, monic of deg |R|


def poly_eval(p, x, q):
    v = 0
    for c in reversed(p):
        v = (v * x + c) % q
    return v


def rref(rows, ncols, q):
    """row-reduce a list of row vectors; returns (pivots, reduced rows)"""
    M = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        s = None
        for i in range(r, len(M)):
            if M[i][c]:
                s = i
                break
        if s is None:
            continue
        M[r], M[s] = M[s], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [(v * inv) % q for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return piv, [row for row in M[:r]]


def canon_subspace(basis, ncols, q):
    """canonical (hashable) RREF form of the span of `basis` (row vectors)"""
    if not basis:
        return ()
    _, rows = rref(basis, ncols, q)
    return tuple(tuple(r) for r in rows)


def colspace(M, nrows, ncols, q):
    """column space of M (given as list of rows) as a canonical row basis"""
    cols = [[M[i][j] for i in range(nrows)] for j in range(ncols)]
    return canon_subspace(cols, nrows, q)


def nullspace(rows, ncols, q):
    piv, R = rref(rows, ncols, q)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % q
        basis.append(v)
    return basis


def intersect(A, B, dim, q):
    """intersection of two subspaces given as canonical row bases"""
    if not A or not B:
        return ()
    a, b = len(A), len(B)
    rows = []
    for j in range(dim):
        rows.append([A[i][j] for i in range(a)] + [(-B[i][j]) % q for i in range(b)])
    ns = nullspace(rows, a + b, q)
    out = []
    for v in ns:
        w = [0] * dim
        for i in range(a):
            if v[i]:
                for j in range(dim):
                    w[j] = (w[j] + v[i] * A[i][j]) % q
        if any(w):
            out.append(w)
    return canon_subspace(out, dim, q)


def solve(rows, rhs, nunk, q):
    """solve rows*x = rhs; returns (particular, nullbasis) or None"""
    aug = [rows[i][:] + [rhs[i]] for i in range(len(rows))]
    piv, R = rref(aug, nunk + 1, q)
    if nunk in piv:
        return None
    x = [0] * nunk
    for i, c in enumerate(piv):
        x[c] = R[i][nunk]
    return x, nullspace([r[:nunk] for r in rows], nunk, q)

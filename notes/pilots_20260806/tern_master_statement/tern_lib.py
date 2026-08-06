"""tern_lib -- exact arithmetic for the ternary relation module T(P, Lambda).

Self-contained: Python stdlib only (no numpy, no sympy).  Every routine is
exact integer / finite-field arithmetic.  Round 19 pilot
notes/pilots_20260806/tern_master_statement/.

Conventions
-----------
n = 2h (h = n/2).  K = Q(zeta_n), O_K = Z[zeta_n], Phi_n(X) = X^h + 1.
The MASTER POINT SET is the half-system P = (xi^j)_{0<=j<h} of mu_n.
A ternary vector eps in {0,+-1}^h is identified with the integer polynomial
V(X) = sum_j eps_j X^j of degree < h.

T(P, Lambda) = { eps ternary : V(xi^l) = 0 in F_{p^delta} for all l in Lambda }
             = { eps ternary : G_Lambda(X) divides V(X) in F_p[X] }
where G_Lambda = prod_{s in Lambda^*} (X - xi^s), Lambda^* = <p>.Lambda.
"""

import random


# ---------------------------------------------------------------- F_p[X] ----

def pnorm(a, p):
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, p):
    r = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        r[i] = c
    for i, c in enumerate(b):
        r[i] = (r[i] + c) % p
    return pnorm(r, p)


def psub(a, b, p):
    r = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        r[i] = c % p
    for i, c in enumerate(b):
        r[i] = (r[i] - c) % p
    return pnorm(r, p)


def pmul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] = (r[i + j] + x * y) % p
    return pnorm(r, p)


def pmod(a, m, p):
    a = list(a)
    dm = len(m) - 1
    inv = pow(m[-1], -1, p)
    while len(a) - 1 >= dm and a:
        d = len(a) - 1 - dm
        c = (a[-1] * inv) % p
        if c:
            for i, y in enumerate(m):
                a[i + d] = (a[i + d] - c * y) % p
        pnorm(a, p)
    return pnorm(a, p)


def pgcd(a, b, p):
    a, b = list(a), list(b)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        inv = pow(a[-1], -1, p)
        a = [(c * inv) % p for c in a]
    return a


def ppowmod(a, e, m, p):
    r = [1]
    a = pmod(a, m, p)
    while e:
        if e & 1:
            r = pmod(pmul(r, a, p), m, p)
        a = pmod(pmul(a, a, p), m, p)
        e >>= 1
    return r


# ------------------------------------------- F_{p^delta} = F_p[X]/(f0) ------

def equal_degree_split(f, d, p, rng):
    """f in F_p[X] is a product of >=2 irreducibles all of degree d."""
    n = len(f) - 1
    while True:
        r = [rng.randrange(p) for _ in range(n)]
        r = pnorm(r, p)
        if not r:
            continue
        g = pgcd(r, f, p)
        if 1 <= len(g) - 1 < n:
            return g
        e = (pow(p, d) - 1) // 2
        h = psub(ppowmod(r, e, f, p), [1], p)
        g = pgcd(h, f, p)
        if 1 <= len(g) - 1 < n:
            return g


def irreducible_factor(f, d, p, seed=12345):
    """One irreducible factor of degree d of f (all factors have degree d)."""
    rng = random.Random(seed)
    cur = list(f)
    while len(cur) - 1 > d:
        cur = equal_degree_split(cur, d, p, rng)
    return cur


def ord_mod(a, n):
    a %= n
    o, x = 1, a
    while x != 1:
        x = (x * a) % n
        o += 1
        if o > n:
            raise ValueError("not invertible")
    return o


class ExtField:
    """F_{p^delta} = F_p[X]/(f0) with a designated xi of exact order n."""

    def __init__(self, p, n, seed=12345):
        assert n % 2 == 0
        h = n // 2
        self.p, self.n, self.h = p, n, h
        self.delta = ord_mod(p, n)
        f = [1] + [0] * (h - 1) + [1]           # X^h + 1
        self.f0 = irreducible_factor(f, self.delta, p, seed)
        assert len(self.f0) - 1 == self.delta
        self.xi = pmod([0, 1], self.f0, p)      # X mod f0, a root of X^h+1
        # exact order check
        assert self.pw(self.xi, n) == [1]
        for q in _prime_factors(n):
            assert self.pw(self.xi, n // q) != [1]

    def mul(self, a, b):
        return pmod(pmul(a, b, self.p), self.f0, self.p)

    def pw(self, a, e):
        return ppowmod(a, e, self.f0, self.p)

    def sub(self, a, b):
        return psub(a, b, self.p)

    def gen_poly(self, lam_star):
        """G(X) = prod_{s in Lambda^*} (X - xi^s); returns coeffs over F_p."""
        p = self.p
        G = [[1]]                                # poly in X with F_{p^d} coeffs
        for s in sorted(lam_star):
            root = self.pw(self.xi, s)
            new = [[0]] * (len(G) + 1)
            new = [[0] for _ in range(len(G) + 1)]
            for i, c in enumerate(G):
                new[i + 1] = padd(new[i + 1], c, p)
                new[i] = psub(new[i], self.mul(c, root), p)
            G = new
        out = []
        for c in G:
            c = pnorm(list(c), p)
            assert len(c) <= 1, "generator polynomial not over F_p"
            out.append(c[0] if c else 0)
        return pnorm(out, p)


def _prime_factors(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


def frob_closure(lam, p, n):
    """Lambda^* = <p>.Lambda inside Z/n."""
    out = set()
    for l in lam:
        s = l % n
        while s not in out:
            out.add(s)
            s = (s * p) % n
    return out


# --------------------------------------------------- Z[X]/(X^h + 1) --------

def zmul_neg(a, b, h):
    """Exact integer multiplication modulo X^h + 1."""
    r = [0] * h
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    k = i + j
                    if k < h:
                        r[k] += x * y
                    else:
                        r[k - h] -= x * y
    return r


def bareiss_det(M):
    """Exact integer determinant (fraction-free Gaussian elimination)."""
    M = [row[:] for row in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            piv = None
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    piv = i
                    break
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def cyclo_norm(v, h):
    """N_{K/Q}(V(zeta_n)) for K = Q(zeta_n), n = 2h, V of degree < h.

    Determinant of multiplication-by-V(zeta) on the Z-basis 1..zeta^{h-1}.
    """
    cols = []
    e = [0] * h
    e[0] = 1
    cur = list(v) + [0] * (h - len(v))
    for i in range(h):
        cols.append(cur[:])
        cur = zmul_neg(cur, [0, 1], h)          # multiply by zeta
    M = [[cols[j][i] for j in range(h)] for i in range(h)]
    return bareiss_det(M)


# ------------------------------------------------------ ternary machinery ---

def ternary_vectors(k):
    """All eps in {0,+-1}^k, as tuples."""
    if k == 0:
        yield ()
        return
    for rest in ternary_vectors(k - 1):
        for c in (0, 1, -1):
            yield rest + (c,)


def syndrome(v, G, p):
    """V mod G in F_p[X], returned as a length-(deg G) tuple."""
    g = len(G) - 1
    r = pmod([c % p for c in v], G, p)
    r = r + [0] * (g - len(r))
    return tuple(r[:g])


def ternary_codewords(h, G, p, cap=None):
    """All nonzero ternary V of degree < h divisible by G, by meet in middle."""
    g = len(G) - 1
    if g == 0:
        return None                              # code is everything
    lo = h // 2
    hi = h - lo
    # syndrome is F_p-linear in the coefficient vector
    basis = []
    for i in range(h):
        e = [0] * h
        e[i] = 1
        basis.append(syndrome(e, G, p))
    tab = {}
    for w in ternary_vectors(hi):
        s = [0] * g
        for i, c in enumerate(w):
            if c:
                b = basis[lo + i]
                for t in range(g):
                    s[t] = (s[t] + c * b[t]) % p
        tab.setdefault(tuple(s), []).append(w)
    out = []
    for u in ternary_vectors(lo):
        s = [0] * g
        for i, c in enumerate(u):
            if c:
                b = basis[i]
                for t in range(g):
                    s[t] = (s[t] + c * b[t]) % p
        key = tuple((-x) % p for x in s)
        for w in tab.get(key, ()):
            v = u + w
            if any(v):
                out.append(v)
                if cap is not None and len(out) >= cap:
                    return out
    return out


def wt(v):
    return sum(1 for c in v if c)

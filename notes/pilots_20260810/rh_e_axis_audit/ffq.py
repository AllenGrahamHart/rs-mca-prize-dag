"""Generic F_q arithmetic for q = p^e (stdlib only, exact).

Written fresh for this pilot.  The in-repo experimental layer
notes/pilots_20260810/ssparse_endpoints/ffield.py is PRIME-FIELD ONLY
(it inverts with pow(x, q-2, q) and reduces with `% q`), so no banked
script can represent an extension field; this module supplies what the
e-axis audit needs.

Elements of F_q are ints 0 <= a < q, read as base-p digit vectors =
coefficients of a polynomial over F_p modulo a PRIMITIVE monic g of
degree e (primitive => X generates F_q^*, so log/exp tables are direct).
"""


def _is_prime(x):
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


def factor_pe(q):
    """(p, e) with q = p^e, or None"""
    d = 2
    while d * d <= q:
        if q % d == 0:
            if not _is_prime(d):
                return None
            e, m = 0, q
            while m % d == 0:
                m //= d
                e += 1
            return (d, e) if m == 1 else None
        d += 1
    return (q, 1) if _is_prime(q) else None


class GF:
    def __init__(self, q):
        pe = factor_pe(q)
        if pe is None:
            raise ValueError("q must be a prime power")
        self.q, self.p, self.e = q, pe[0], pe[1]
        p, e = self.p, self.e
        if e == 1:
            self.EXP = self.LOG = None
            self.g = None
        else:
            self.g = self._find_primitive(p, e)
            self._tables()

    # ---- field construction -------------------------------------------
    @staticmethod
    def _polymulmod(a, b, g, p, e):
        """a, b: coeff lists len e; g: monic deg-e coeff list len e+1"""
        r = [0] * (2 * e - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        r[i + j] = (r[i + j] + ai * bj) % p
        for d in range(2 * e - 2, e - 1, -1):
            c = r[d]
            if c:
                r[d] = 0
                for i in range(e):
                    r[d - e + i] = (r[d - e + i] - c * g[i]) % p
        return r[:e]

    def _find_primitive(self, p, e):
        """monic g of degree e such that X is a generator of F_q^*.

        Order(X) = q-1 forces F_p[X]/g to be a field of size q, so such a g
        is automatically irreducible; no separate irreducibility test needed.
        """
        q = p ** e
        one = [1] + [0] * (e - 1)
        X = [0] * e
        X[1] = 1
        for code in range(p ** e):
            c, kk = [], code
            for _ in range(e):
                c.append(kk % p)
                kk //= p
            g = c + [1]
            if g[0] == 0:                      # X | g  => reducible
                continue
            cur = X[:]
            order = None
            for t in range(1, q):
                if cur == one:
                    order = t
                    break
                cur = self._polymulmod(cur, X, g, p, e)
            if order == q - 1:
                return g
        raise RuntimeError("no primitive polynomial found")

    def _tables(self):
        p, e, q, g = self.p, self.e, self.q, self.g
        EXP = [0] * (q - 1)
        LOG = [None] * q
        cur = [1] + [0] * (e - 1)
        X = [0] * e
        X[1] = 1
        for t in range(q - 1):
            v = 0
            for i in range(e - 1, -1, -1):
                v = v * p + cur[i]
            EXP[t] = v
            LOG[v] = t
            cur = self._polymulmod(cur, X, g, p, e)
        self.EXP, self.LOG = EXP, LOG

    # ---- arithmetic ----------------------------------------------------
    def add(self, a, b):
        if self.e == 1:
            return (a + b) % self.p
        p, e = self.p, self.e
        r, m = 0, 1
        for _ in range(e):
            r += ((a % p + b % p) % p) * m
            a //= p
            b //= p
            m *= p
        return r

    def sub(self, a, b):
        if self.e == 1:
            return (a - b) % self.p
        p, e = self.p, self.e
        r, m = 0, 1
        for _ in range(e):
            r += ((a % p - b % p) % p) * m
            a //= p
            b //= p
            m *= p
        return r

    def neg(self, a):
        return self.sub(0, a)

    def mul(self, a, b):
        if self.e == 1:
            return a * b % self.p
        if a == 0 or b == 0:
            return 0
        return self.EXP[(self.LOG[a] + self.LOG[b]) % (self.q - 1)]

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        if self.e == 1:
            return pow(a, self.p - 2, self.p)
        return self.EXP[(-self.LOG[a]) % (self.q - 1)]

    def pow(self, a, m):
        if a == 0:
            return 0 if m else 1
        if self.e == 1:
            return pow(a, m, self.p)
        return self.EXP[(self.LOG[a] * m) % (self.q - 1)]

    def frob(self, a):
        """the p-power Frobenius"""
        return self.pow(a, self.p)

    def in_subfield(self, a, d):
        """is a in the subfield F_(p^d)?  (d | e)"""
        return self.pow(a, self.p ** d) == a

    # ---- domains and polynomials --------------------------------------
    def subgroup(self, n):
        """the order-n subgroup of F_q^*, as a list (needs n | q-1)"""
        assert (self.q - 1) % n == 0
        if self.e == 1:
            m = self.q - 1
            fac = set()
            d = 2
            while d * d <= m:
                while m % d == 0:
                    fac.add(d)
                    m //= d
                d += 1
            if m > 1:
                fac.add(m)
            ggen = 2
            while any(pow(ggen, (self.q - 1) // f, self.q) == 1 for f in fac):
                ggen += 1
        else:
            ggen = self.EXP[1]
        h = self.pow(ggen, (self.q - 1) // n)
        S = [self.pow(h, i) for i in range(n)]
        assert len(set(S)) == n, "domain not of full order"
        return S

    def poly_from_roots(self, R):
        pol = [1]
        for r in R:
            new = [0] * (len(pol) + 1)
            for i, c in enumerate(pol):
                new[i] = self.sub(new[i], self.mul(c, r))
                new[i + 1] = self.add(new[i + 1], c)
            pol = new
        return pol

    def poly_eval(self, pol, x):
        v = 0
        for c in reversed(pol):
            v = self.add(self.mul(v, x), c)
        return v

    # ---- linear algebra -------------------------------------------------
    def rref(self, rows, ncols):
        M = [r[:] for r in rows]
        piv, r = [], 0
        for c in range(ncols):
            s = None
            for i in range(r, len(M)):
                if M[i][c]:
                    s = i
                    break
            if s is None:
                continue
            M[r], M[s] = M[s], M[r]
            iv = self.inv(M[r][c])
            M[r] = [self.mul(v, iv) for v in M[r]]
            for i in range(len(M)):
                if i != r and M[i][c]:
                    f = M[i][c]
                    M[i] = [self.sub(a, self.mul(f, b)) for a, b in zip(M[i], M[r])]
            piv.append(c)
            r += 1
            if r == len(M):
                break
        return piv, M[:r]

    def canon_subspace(self, basis, ncols):
        if not basis:
            return ()
        _, rows = self.rref(basis, ncols)
        return tuple(tuple(r) for r in rows)

    def colspace(self, M, nrows, ncols):
        cols = [[M[i][j] for i in range(nrows)] for j in range(ncols)]
        return self.canon_subspace(cols, nrows)

    def nullspace(self, rows, ncols):
        piv, R = self.rref(rows, ncols)
        free = [c for c in range(ncols) if c not in piv]
        out = []
        for f in free:
            v = [0] * ncols
            v[f] = 1
            for i, c in enumerate(piv):
                v[c] = self.neg(R[i][f])
            out.append(v)
        return out

    def intersect(self, A, B, dim):
        if not A or not B:
            return ()
        a, b = len(A), len(B)
        rows = []
        for j in range(dim):
            rows.append([A[i][j] for i in range(a)] + [self.neg(B[i][j]) for i in range(b)])
        ns = self.nullspace(rows, a + b)
        out = []
        for v in ns:
            w = [0] * dim
            for i in range(a):
                if v[i]:
                    for j in range(dim):
                        w[j] = self.add(w[j], self.mul(v[i], A[i][j]))
            if any(w):
                out.append(w)
        return self.canon_subspace(out, dim)

    def solve(self, rows, rhs, nunk):
        aug = [rows[i][:] + [rhs[i]] for i in range(len(rows))]
        piv, R = self.rref(aug, nunk + 1)
        if nunk in piv:
            return None
        x = [0] * nunk
        for i, c in enumerate(piv):
            x[c] = R[i][nunk]
        return x, self.nullspace([r[:nunk] for r in rows], nunk)

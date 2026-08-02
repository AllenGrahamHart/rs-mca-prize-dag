"""Exact finite-field library for the split-section packet pilot (2026-08-02).

All arithmetic is exact (integers mod p, or tuples over F_p for extension
fields).  No floats anywhere except in printed display strings.

Objects
-------
PrimeField(p)          F_p, elements are ints in [0,p)
ExtField(p, m)         F_{p^m}, elements are m-tuples of ints (low-to-high)
domain(F, n, beta)     the n roots of Z^n - beta, or None if it does not split
exact_shell_census     brute-force exact-agreement census of RS[F, H, k] against
                       one received word, by interpolating every k-subset

Conventions
-----------
* polynomials are coefficient lists, low degree first
* a received word is given by its interpolant U (degree < n) or by its values
* H is the evaluation domain, a list of n distinct nonzero field elements
"""
from __future__ import annotations

from itertools import combinations


# ---------------------------------------------------------------------------
# fields
# ---------------------------------------------------------------------------
class PrimeField:
    def __init__(self, p: int):
        self.p = p
        self.q = p
        self.char = p
        self.zero = 0
        self.one = 1
        self.name = f"F_{p}"

    def add(self, a, b):
        return (a + b) % self.p

    def sub(self, a, b):
        return (a - b) % self.p

    def mul(self, a, b):
        return (a * b) % self.p

    def neg(self, a):
        return (-a) % self.p

    def inv(self, a):
        assert a != 0
        return pow(a, self.p - 2, self.p)

    def power(self, a, e):
        return pow(a, e, self.p)

    def elements(self):
        return list(range(self.p))

    def units(self):
        return list(range(1, self.p))

    def key(self, a):
        return a


def _poly_mod_p(a, p):
    return [x % p for x in a]


class ExtField:
    """F_{p^m} as F_p[t]/(f), elements are tuples of length m."""

    def __init__(self, p: int, m: int, modulus=None):
        self.p = p
        self.m = m
        self.q = p ** m
        self.char = p
        if modulus is None:
            modulus = self._find_irreducible()
        self.modulus = tuple(modulus)  # monic, length m+1
        self.zero = tuple([0] * m)
        self.one = tuple([1] + [0] * (m - 1))
        self.name = f"F_{p}^{m}"

    def _find_irreducible(self):
        p, m = self.p, self.m
        # brute force: monic degree-m polynomials with no roots is not enough for
        # m>3, so test irreducibility by trial division against all monic polys
        # of degree <= m//2.
        def polymulmod(a, b):
            out = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                if x:
                    for j, y in enumerate(b):
                        out[i + j] = (out[i + j] + x * y) % p
            return out

        def polydivmod(a, b):
            a = list(a)
            db = len(b) - 1
            inv_lead = pow(b[-1], p - 2, p)
            qout = [0] * max(1, len(a) - db)
            for i in range(len(a) - 1, db - 1, -1):
                c = a[i] * inv_lead % p
                qout[i - db] = c
                if c:
                    for j in range(db + 1):
                        a[i - db + j] = (a[i - db + j] - c * b[j]) % p
            while len(a) > 1 and a[-1] == 0:
                a.pop()
            return qout, a

        def all_monic(deg):
            for tail in _tuples(p, deg):
                yield list(tail) + [1]

        divisors = []
        for d in range(1, m // 2 + 1):
            divisors.extend(all_monic(d))
        for tail in _tuples(p, m):
            cand = list(tail) + [1]
            ok = True
            for d in divisors:
                _, rem = polydivmod(cand, d)
                if len(rem) == 1 and rem[0] == 0:
                    ok = False
                    break
            if ok:
                return cand
        raise AssertionError("no irreducible found")

    def add(self, a, b):
        p = self.p
        return tuple((x + y) % p for x, y in zip(a, b))

    def sub(self, a, b):
        p = self.p
        return tuple((x - y) % p for x, y in zip(a, b))

    def neg(self, a):
        p = self.p
        return tuple((-x) % p for x in a)

    def mul(self, a, b):
        p, m = self.p, self.m
        out = [0] * (2 * m - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] = (out[i + j] + x * y) % p
        mod = self.modulus
        for i in range(2 * m - 2, m - 1, -1):
            c = out[i]
            if c:
                out[i] = 0
                for j in range(m):
                    out[i - m + j] = (out[i - m + j] - c * mod[j]) % p
        return tuple(out[:m])

    def inv(self, a):
        assert any(a)
        return self.power(a, self.q - 2)

    def power(self, a, e):
        result = self.one
        base = a
        while e > 0:
            if e & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            e >>= 1
        return result

    def elements(self):
        return [tuple(t) for t in _tuples(self.p, self.m)]

    def units(self):
        return [e for e in self.elements() if any(e)]

    def key(self, a):
        return a


def _tuples(p, m):
    if m == 0:
        yield ()
        return
    for head in range(p):
        for rest in _tuples(p, m - 1):
            yield (head,) + rest


# ---------------------------------------------------------------------------
# polynomials over a field F (coefficient lists, low degree first)
# ---------------------------------------------------------------------------
def poly_trim(F, a):
    a = list(a)
    while len(a) > 1 and a[-1] == F.zero:
        a.pop()
    return a


def poly_add(F, a, b):
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        x = a[i] if i < len(a) else F.zero
        y = b[i] if i < len(b) else F.zero
        out.append(F.add(x, y))
    return poly_trim(F, out)


def poly_sub(F, a, b):
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        x = a[i] if i < len(a) else F.zero
        y = b[i] if i < len(b) else F.zero
        out.append(F.sub(x, y))
    return poly_trim(F, out)


def poly_mul(F, a, b):
    out = [F.zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == F.zero:
            continue
        for j, y in enumerate(b):
            if y == F.zero:
                continue
            out[i + j] = F.add(out[i + j], F.mul(x, y))
    return poly_trim(F, out)


def poly_eval(F, a, x):
    out = F.zero
    for c in reversed(a):
        out = F.add(F.mul(out, x), c)
    return out


def poly_divmod(F, a, b):
    a = list(a)
    db = len(b) - 1
    inv_lead = F.inv(b[-1])
    if len(a) - 1 < db:
        return [F.zero], poly_trim(F, a)
    qout = [F.zero] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = F.mul(a[i], inv_lead)
        qout[i - db] = c
        if c != F.zero:
            for j in range(db + 1):
                a[i - db + j] = F.sub(a[i - db + j], F.mul(c, b[j]))
    return poly_trim(F, qout), poly_trim(F, a)


def locator(F, roots):
    """monic prod (X - x)."""
    out = [F.one]
    for x in roots:
        out = poly_mul(F, out, [F.neg(x), F.one])
    return out


def interpolate(F, xs, ys):
    """Lagrange interpolation, returns coefficient list of length <= len(xs)."""
    n = len(xs)
    out = [F.zero] * n
    for i in range(n):
        xi, yi = xs[i], ys[i]
        basis = [F.one]
        den = F.one
        for j in range(n):
            if i == j:
                continue
            xj = xs[j]
            nxt = [F.zero] * (len(basis) + 1)
            for a, c in enumerate(basis):
                nxt[a] = F.sub(nxt[a], F.mul(c, xj))
                nxt[a + 1] = F.add(nxt[a + 1], c)
            basis = nxt
            den = F.mul(den, F.sub(xi, xj))
        scale = F.mul(yi, F.inv(den))
        for a, c in enumerate(basis):
            out[a] = F.add(out[a], F.mul(scale, c))
    return poly_trim(F, out)


# ---------------------------------------------------------------------------
# domains
# ---------------------------------------------------------------------------
def multiplicative_generator(F):
    q = F.q
    order = q - 1
    factors = []
    t = order
    d = 2
    while d * d <= t:
        if t % d == 0:
            factors.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        factors.append(t)
    for g in F.units():
        if all(F.power(g, order // r) != F.one for r in factors):
            return g
    raise AssertionError("no generator")


def domain(F, n, beta):
    """Roots of Z^n - beta, ordered as x0*omega^i.  None if it does not split."""
    if (F.q - 1) % n != 0:
        return None
    g = multiplicative_generator(F)
    omega = F.power(g, (F.q - 1) // n)
    x0 = None
    for x in F.units():
        if F.power(x, n) == beta:
            x0 = x
            break
    if x0 is None:
        return None
    out = [x0]
    for _ in range(n - 1):
        out.append(F.mul(out[-1], omega))
    assert len(set(out)) == n
    return out, omega, x0


# ---------------------------------------------------------------------------
# exact shell census (brute force, independent of the packet theory)
# ---------------------------------------------------------------------------
def exact_shell_census(F, H, k, Uvals):
    """Return (shells, codewords).

    shells[b] = number of codewords of RS[F,H,k] agreeing with Uvals in
    exactly b positions, for b >= k.  codewords maps the coefficient tuple to
    the frozenset of agreeing indices.  Brute force over all k-subsets: every
    codeword with agreement >= k is the interpolant of some k-subset.
    """
    n = len(H)
    seen = {}
    for idxs in combinations(range(n), k):
        xs = [H[i] for i in idxs]
        ys = [Uvals[i] for i in idxs]
        P = tuple(interpolate(F, xs, ys))
        if P in seen:
            continue
        agree = frozenset(i for i in range(n)
                          if poly_eval(F, list(P), H[i]) == Uvals[i])
        seen[P] = agree
    shells = {}
    for P, agree in seen.items():
        b = len(agree)
        shells[b] = shells.get(b, 0) + 1
    return shells, seen


def word_from_window(F, H, n, k, terms):
    """Received word values for U = sum_{d: coeff} coeff * X^d."""
    U = [F.zero] * n
    for d, c in terms.items():
        U[d] = F.add(U[d], c)
    return [poly_eval(F, U, x) for x in H], U

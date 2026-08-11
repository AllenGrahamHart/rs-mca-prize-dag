"""biv_core.py -- round 33 pilot rh_bivariate_system.

Core machinery for THE OVERDETERMINED REALIZABILITY SYSTEM.

Setting (SAT1)-(SAT4), T = rho+2 = 4m+1, a = w* = a* = 7m-1:

  Psi(Z) = ( (c_{0,x} + Z c_{1,x}) Q(Z;x) )_{x in D}  in  K'[Z],
  deg_Z Psi <= e+1 = m+1                       ((C3), apolar_origin/PREREG.md:187-190)
  K' = {psi : sum_x psi_x x^i = 0, 0 <= i <= R-r-1 = 4m}, [16m, 12m-1, 4m+2] MDS.

c_0, c_1 are supported in W, so Psi is supported in W and each Z-coefficient
lies in the shortening K'|_W, whose parity check is the (4m+1) x a Vandermonde
V[i,x] = x^i, i = 0..4m.

At a parameter-saturated x (d_x = m; >= N-(1+O) of the N domain points,
saturation_rigidity/statement.md:56-69) Q(Z;x) = c_x prod_{gamma in A_x}(Z-gamma),
so

  Psi_x(Z) = (alpha_x Z + beta_x) * pi_x(Z),   pi_x(Z) = prod_{gamma in A_x}(Z-gamma)

with (alpha_x, beta_x) = c_x (c_{1,x}, c_{0,x}) != (0,0) for every x in W.

SYSTEM S2 (honest form, mu unknown):  for i = 0..4m,
  sum_{x in W} x^i (alpha_x Z + beta_x) pi_x(Z) == 0   in F_q[Z].
  (m+2)(4m+1) scalar equations, 2a unknowns.

SYSTEM S1 (mandate form, mu given as incidence data): alpha_x = lambda_x,
beta_x = -lambda_x mu(x); (m+2)(4m+1) equations, a unknowns.

Stdlib only.
"""

import random

# ----------------------------------------------------------------- field utils


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_one_mod(nn, count=2, start=None, limit=200000):
    """primes q with nn | q-1."""
    out = []
    k = 1 if start is None else start
    while len(out) < count and nn * k + 1 <= limit:
        q = nn * k + 1
        if is_prime(q):
            out.append(q)
        k += 1
    return out


def primitive_root(q):
    fac = []
    n = q - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise RuntimeError("no primitive root")


def mu_N(q, N):
    """the evaluation domain D = mu_N < F_q^*, as a list of N distinct elements."""
    assert (q - 1) % N == 0
    g = primitive_root(q)
    w = pow(g, (q - 1) // N, q)
    out, cur = [], 1
    for _ in range(N):
        out.append(cur)
        cur = cur * w % q
    assert len(set(out)) == N
    return out


# ------------------------------------------------------- packed modular rank


class PackedRank:
    """Row-echelon rank over F_q with rows packed into python big integers.

    Each row is sum_c v_c * 2^(B*c) with 0 <= v_c and B a multiple of 8 large
    enough that no limb overflows during a full pass of eliminations
    (growth < q^2 per elimination, at most ncols eliminations).
    """

    def __init__(self, ncols, q):
        self.n = ncols
        self.q = q
        need = q + (ncols + 2) * q * q
        b = 8
        while (1 << b) <= need:
            b += 8
        self.B = b
        self.nb = b // 8
        self.mask = (1 << b) - 1
        self.pivots = {}  # col -> packed normalized row (limbs reduced, 1 at col)
        self.order = []  # pivot columns in increasing order

    def pack(self, vec):
        return int.from_bytes(
            b"".join(int(v % self.q).to_bytes(self.nb, "little") for v in vec),
            "little",
        )

    def unpack(self, r):
        bs = r.to_bytes(self.nb * self.n + 8, "little")
        q = self.q
        nb = self.nb
        return [
            int.from_bytes(bs[i * nb : (i + 1) * nb], "little") % q
            for i in range(self.n)
        ]

    def add_row(self, vec):
        """returns True if the row increased the rank."""
        q = self.q
        r = self.pack(vec)
        B = self.B
        mask = self.mask
        for c in self.order:
            v = ((r >> (B * c)) & mask) % q
            if v:
                r += (q - v) * self.pivots[c]
        limbs = self.unpack(r)
        for c in range(self.n):
            if limbs[c]:
                inv = pow(limbs[c], q - 2, q)
                limbs = [x * inv % q for x in limbs]
                self.pivots[c] = self.pack(limbs)
                self.order.append(c)
                self.order.sort()
                return True
        return False

    @property
    def rank(self):
        return len(self.order)

    def kernel_basis(self):
        """kernel of the matrix whose ROWS were added (i.e. right nullspace)."""
        q = self.q
        # fully reduce pivot rows against each other
        rows = {c: self.unpack(self.pivots[c]) for c in self.order}
        for c in reversed(self.order):
            rc = rows[c]
            for c2 in self.order:
                if c2 >= c:
                    continue
                r2 = rows[c2]
                if r2[c]:
                    f = r2[c]
                    rows[c2] = [(a - f * b) % q for a, b in zip(r2, rc)]
        free = [c for c in range(self.n) if c not in self.pivots]
        basis = []
        for f in free:
            v = [0] * self.n
            v[f] = 1
            for c in self.order:
                v[c] = (-rows[c][f]) % q
            basis.append(v)
        return basis


# --------------------------------------------------------- polynomial helpers


def poly_from_roots(roots, q):
    p = [1]
    for r in roots:
        new = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            new[i] = (new[i] - r * c) % q
            new[i + 1] = (new[i + 1] + c) % q
        p = new
    return p


# ------------------------------------------------------------- system builders


def build_S2(m, q, Wvals, Amap, extra=None, verbose=False):
    """SYSTEM S2: unknowns (alpha_x, beta_x) for x in W (2a of them).

    Wvals : list of a distinct field elements (the embedded joint support W)
    Amap  : dict x -> list of slope field elements A_x
    extra : optional dict x -> k, giving k EXTRA unknown coefficients at an
            unsaturated point x (Q(Z;x) = c_x prod(Z-g) * g_x(Z), deg g_x <= k).
            Columns are then (alpha,beta) x (coefficients of g_x).
    returns (PackedRank object, column labels)
    """
    T = 4 * m + 1
    a = len(Wvals)
    extra = extra or {}
    # The unknown coordinate space at x is  pi_x(Z) * {polys of degree <= 1+k_x},
    # k_x = m - d_x  (k_x = 0 at a saturated point: exactly the pair
    # (alpha_x, beta_x)).  Columns Z^t * pi_x, t = 0 .. k_x+1.  NOTE: writing it
    # as (alpha,beta) x (g_x coefficients) DOUBLE COUNTS -- Z*(Z^t pi) and
    # Z^{t+1} pi are the same column -- which inflates the nullity by k_x.
    cols = []  # (x, 'c', t)
    polys = {}
    for x in Wvals:
        pi = poly_from_roots(Amap[x], q)
        k = extra.get(x, 0)
        for t in range(k + 2):
            polys[(x, t)] = [0] * t + pi
            cols.append((x, "c", t))
    ncols = len(cols)
    dz = m + 1  # deg_Z Psi <= e+1
    # precompute x^i
    pw = {x: [1] * (4 * m + 1) for x in Wvals}
    for x in Wvals:
        for i in range(1, 4 * m + 1):
            pw[x][i] = pw[x][i - 1] * x % q
    pr = PackedRank(ncols, q)
    rows = []
    for i in range(4 * m + 1):
        for j in range(dz + 1):
            vec = [0] * ncols
            nz = False
            for ci, (x, kind, t) in enumerate(cols):
                p = polys[(x, t)]
                if j < len(p) and p[j]:
                    vec[ci] = pw[x][i] * p[j] % q
                    nz = True
            if nz:
                rows.append(vec)
    random.Random(20260811).shuffle(rows)
    for vec in rows:
        if pr.rank == ncols:
            break
        pr.add_row(vec)
    return pr, cols, ncols, len(rows), T, a


def build_S1(m, q, Wvals, Amap, mumap):
    """SYSTEM S1 (mandate form): unknowns lambda_x, mu given.

    mumap : dict x -> mu(x) in F_q, or None for mu(x) = infinity
    """
    a = len(Wvals)
    cols = list(Wvals)
    polys = {}
    for x in Wvals:
        pi = poly_from_roots(Amap[x], q)
        mu = mumap[x]
        if mu is None:
            polys[x] = pi  # projective: mu(x) = infinity, degree drops to d_x
        else:
            polys[x] = poly_from_roots(list(Amap[x]) + [mu], q)
    pw = {x: [1] * (4 * m + 1) for x in Wvals}
    for x in Wvals:
        for i in range(1, 4 * m + 1):
            pw[x][i] = pw[x][i - 1] * x % q
    pr = PackedRank(a, q)
    rows = []
    for i in range(4 * m + 1):
        for j in range(m + 2):
            vec = [0] * a
            nz = False
            for ci, x in enumerate(cols):
                p = polys[x]
                if j < len(p) and p[j]:
                    vec[ci] = pw[x][i] * p[j] % q
                    nz = True
            if nz:
                rows.append(vec)
    random.Random(20260811).shuffle(rows)
    for vec in rows:
        if pr.rank == a:
            break
        pr.add_row(vec)
    return pr, cols, a, len(rows)

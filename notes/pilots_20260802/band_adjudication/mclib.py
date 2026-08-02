"""mclib -- exhaustive pencil scan for the band/cascade adjudication.

Self-contained engine.  For a received pair (u,v) on a multiplicative
domain H = x0*mu_n and a code C = RS[F_q,H,k] it computes, EXHAUSTIVELY
and theory-free:

  * every codeword PAIR (f,g) with joint agreement |Z| >= k
    (every such pair is the pair of Lagrange interpolants of (u,v) on any
     k-subset of Z, so enumerating k-subsets is complete);
  * for every pair, the direction map  zeta_P : D \\ Z -> P^1(F_q),
    zeta_P(i) = the unique z with (u_i - f(x_i)) + z (v_i - g(x_i)) = 0
    (z = inf when v_i = g(x_i));
  * for every z in P^1(F_q) the FULL list of codewords at agreement >= k
    against w_z = u + z v (w_inf = v), because
        interp_S(w_z) = interp_S(u) + z interp_S(v)
    so one pass over k-subsets resolves the whole pencil at once;
  * max agreement per pencil member, the live slopes (agreement exactly A),
    a deterministic first-match selection of one exact-A support per live
    slope, and the occupancy quantities L_P and N_d.

The scan covers z = inf (the (0:1) direction) as required by the banked
gate-completeness correction (xr_band_occupancy FABLE_AUDIT item 4).
"""

import sys
from itertools import combinations

sys.dont_write_bytecode = True

INF = "inf"


# ---------------------------------------------------------------- field
def is_prime(m):
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2
    return True


def primitive_root(q):
    m = q - 1
    fac, t, d = [], q - 1, 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in range(2, q):
        if all(pow(g, m // p, q) != 1 for p in fac):
            return g
    raise RuntimeError("no primitive root")


def make_domain(q, n, beta_exp=0):
    assert (q - 1) % n == 0
    g = primitive_root(q)
    omega = pow(g, (q - 1) // n, q)
    x0 = pow(g, beta_exp, q)
    H = [(x0 * pow(omega, i, q)) % q for i in range(n)]
    assert len(set(H)) == n
    beta = pow(x0, n, q)
    return H, beta, omega


# ---------------------------------------------------------- polynomials
def poly_eval(c, x, q):
    acc = 0
    for a in reversed(c):
        acc = (acc * x + a) % q
    return acc


def mulXminus(c, a, q):
    out = [0] * (len(c) + 1)
    for i, v in enumerate(c):
        if v:
            out[i + 1] = (out[i + 1] + v) % q
            out[i] = (out[i] - v * a) % q
    return out


def vanishing(pts, q):
    m = [1]
    for a in pts:
        m = mulXminus(m, a, q)
    return m


def interp(xs, ys, q):
    kk = len(xs)
    res = [0] * kk
    for i in range(kk):
        num, den, xi = [1], 1, xs[i]
        for j in range(kk):
            if j == i:
                continue
            num = mulXminus(num, xs[j], q)
            den = (den * (xi - xs[j])) % q
        s = (ys[i] * pow(den, q - 2, q)) % q
        for t in range(kk):
            res[t] = (res[t] + s * num[t]) % q
    return res


def trim(c):
    c = list(c)
    while c and c[-1] == 0:
        c.pop()
    return c


def divmod_poly(a, b, q):
    a, b = list(a), trim(b)
    out = [0] * max(0, len(a) - len(b) + 1)
    inv = pow(b[-1], q - 2, q)
    while len(trim(a)) >= len(b):
        a = trim(a)
        d = len(a) - len(b)
        f = (a[-1] * inv) % q
        out[d] = f
        for i, bb in enumerate(b):
            a[i + d] = (a[i + d] - f * bb) % q
        a = trim(a)
        if not a:
            break
    return out, trim(a)


# ------------------------------------------------- MC coset construction
def mc_cosets(n, M):
    N = n // M
    return [[i for i in range(n) if i % N == j] for j in range(N)]


def mc_family(H, q, n, k, w, M, c):
    """T ranging over unions of r'/M cosets of mu_M with prod T = gamma."""
    rp = n - k - w
    assert n % M == 0 and rp % M == 0 and w <= M
    N, m = n // M, rp // M
    cos = mc_cosets(n, M)
    gamma = ((-1) ** (rp + 1) * c) % q
    out = []
    for S in combinations(range(N), m):
        T = [i for j in S for i in cos[j]]
        pr = 1
        for i in T:
            pr = (pr * H[i]) % q
        if pr == gamma:
            out.append(tuple(sorted(T)))
    return out


def mc_c_from_gamma(H, q, n, k, w, M):
    rp = n - k - w
    N, m = n // M, rp // M
    cos = mc_cosets(n, M)
    T = [i for j in range(m) for i in cos[j]]
    pr = 1
    for i in T:
        pr = (pr * H[i]) % q
    gamma = pr
    return (((-1) ** (rp + 1)) * gamma) % q


def codeword_from_T(Ucoeffs, T_idx, H, k, n, q, beta):
    """The unique P with (U-P) vanishing off T, if deg P < k; else None."""
    Tp = [H[i] for i in T_idx]
    MT = vanishing(Tp, q)
    prod = [0] * (len(Ucoeffs) + len(MT) - 1)
    for i, a in enumerate(Ucoeffs):
        if not a:
            continue
        for j, b in enumerate(MT):
            if b:
                prod[i + j] = (prod[i + j] + a * b) % q
    red = [0] * n
    for d, cf in enumerate(prod):
        red[d % n] = (red[d % n] + cf * pow(beta, d // n, q)) % q
    Pq, rem = divmod_poly(trim(red), MT, q)
    if trim(rem) or len(trim(Pq)) > k:
        return None
    P = trim(Pq)
    return tuple(P + [0] * (k - len(P)))


# ------------------------------------------------------- the pencil scan
class Scan(object):
    """Exhaustive scan of a received pair over the whole pencil P^1(F_q)."""

    def __init__(self, H, q, k, uvals, vvals, A):
        self.H, self.q, self.k, self.A = H, q, k, A
        self.n = len(H)
        self.u, self.v = uvals, vvals
        self.pairs = {}          # (f,g) -> dict(Z=frozenset, zeta={i:z})
        self.max_agr = {}        # z -> max agreement over codewords
        self.rays = {}           # z -> list of (support_frozenset, codeword)
        self._scan()

    def _scan(self):
        n, k, q, H = self.n, self.k, self.q, self.H
        u, v = self.u, self.v
        maxagr = {}
        rays = {}
        for S in combinations(range(n), k):
            xs = [H[i] for i in S]
            f = tuple(interp(xs, [u[i] for i in S], q))
            g = tuple(interp(xs, [v[i] for i in S], q))
            if (f, g) in self.pairs:
                continue
            fa = [poly_eval(f, H[i], q) for i in range(n)]
            ga = [poly_eval(g, H[i], q) for i in range(n)]
            Z, zeta = [], {}
            for i in range(n):
                a = (u[i] - fa[i]) % q
                b = (v[i] - ga[i]) % q
                if a == 0 and b == 0:
                    Z.append(i)
                elif b == 0:
                    zeta[i] = INF
                else:
                    zeta[i] = (-a * pow(b, q - 2, q)) % q
            self.pairs[(f, g)] = {"Z": frozenset(Z), "zeta": zeta}
            # per-slope agreement of the ray f + z g against w_z
            base = len(Z)
            byz = {}
            for i, z in zeta.items():
                byz.setdefault(z, []).append(i)
            for z, extra in byz.items():
                a = base + len(extra)
                if a >= maxagr.get(z, 0):
                    if a > maxagr.get(z, 0):
                        maxagr[z] = a
                        rays[z] = []
                    sup = frozenset(Z) | frozenset(extra)
                    cw = f if z == INF else None
                    rays[z].append((sup, (f, g)))
            # slopes with no extra point still get agreement = base
            if base > 0:
                for z in list(range(q)) + [INF]:
                    if z not in byz:
                        if base > maxagr.get(z, 0):
                            maxagr[z] = base
                            rays[z] = [(frozenset(Z), (f, g))]
                        elif base == maxagr.get(z, 0):
                            rays[z].append((frozenset(Z), (f, g)))
        self.max_agr = maxagr
        # dedupe ray supports
        self.rays = {}
        for z, lst in rays.items():
            seen, out = set(), []
            for sup, pr in lst:
                if sup in seen:
                    continue
                seen.add(sup)
                out.append((sup, pr))
            self.rays[z] = sorted(out, key=lambda s: sorted(s[0]))

    # ---------------------------------------------------------- queries
    def gate_ok(self):
        """tangent gate (H3): no pencil member exceeds agreement A."""
        return all(a <= self.A for a in self.max_agr.values())

    def over_agreeing(self):
        return {z: a for z, a in self.max_agr.items() if a > self.A}

    def joint_max(self):
        return max((len(d["Z"]) for d in self.pairs.values()), default=0)

    def live(self):
        return sorted([z for z, a in self.max_agr.items() if a == self.A],
                      key=lambda z: (z == INF, z))

    def selected(self):
        """One exact-A support per live slope, fixed first-match order
        (lexicographically smallest support tuple)."""
        return {z: self.rays[z][0][0] for z in self.live()}

    def band_pairs(self):
        """{(f,g): depth} for pairs with joint agreement in [k+1, A]."""
        out = {}
        for P, d in self.pairs.items():
            j = len(d["Z"])
            if j >= self.k + 1:
                out[P] = j - self.k
        return out

    def occupancy(self):
        """N_d (selected) and N_d_any (any exact-A ray) per depth."""
        sel = self.selected()
        Nd, Nd_any, detail = {}, {}, {}
        for P, dep in self.band_pairs().items():
            Z = self.pairs[P]["Z"]
            Lsel = [z for z, S in sel.items() if Z <= S]
            Lany = [z for z in self.live()
                    if any(Z <= S for S, _ in self.rays[z])]
            detail[P] = (dep, len(Lsel), len(Lany))
            if len(Lsel) >= 2:
                Nd[dep] = Nd.get(dep, 0) + 1
            if len(Lany) >= 2:
                Nd_any[dep] = Nd_any.get(dep, 0) + 1
        return Nd, Nd_any, detail

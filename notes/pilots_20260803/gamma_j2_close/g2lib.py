"""g2lib -- independent engine for the j >= 2 Gamma cardinality close.

Self-contained: field arithmetic, domains, a theory-free pencil scan (ground
truth), and MY OWN classifier built from the window system re-derived from
scratch (see PREREG (P1)).  advlib is imported READ-ONLY in the experiments
only as a third opinion, never as the source of a claim.

--------------------------------------------------------------------------
THE FRAME (re-derived here, verified in e1_frame.py against ground truth).

H = x0 mu_n, |H| = n, Omega = X^n - beta, C = RS[F_q, H, k],
u <-> U = X^{n-1} + c X^{k+w-1},  v(x) = u(x)/x^j on H,  w_z = u + z v,
A = k+w+1,  r = n-k-w,  r' = r-1 = n-A,  gamma := (-1)^{r'} c.

Exact-A codewords of w_z <-> monic M | Omega, deg M = r', T := roots(M) c H,
m_s := [X^s]M, whose top-(w+1) window conditions are linear in z:

    alpha_i + z beta_i = 0,   i = 0..w,
    alpha_i = [i=0] m_0 + [i>=1] c m_{r'+1-i},
    beta_i  = [0 <= j-i <= r'] m_{j-i} + [i >= j+1] c m_{r'+1+j-i}.

Unwinding the indicator brackets gives the s-form (P1):

  (beta)  m_s + z m_{s+j} = 0        for s in {0} u [r'+1-w, r'-j]
  (alpha) m_rho = -(c/z) m_{r'-j+1+rho}   for rho in [max(0,j-w), j-1]

The (beta) band is non-empty only when j < w; the (alpha) band always
contains rho = j-1, which is what makes (P3') universal:

    m_{j-1} = -c/z          ==>      z = (-1)^j gamma / e_{r'-j+1}(T)
                                       = (-1)^j gamma / (prod(T) e_{j-1}(T^-1))

and since prod(T) in x0^{r'} mu_n for EVERY r'-subset T of H,

    |Gamma_j| <= n . E_j,   E_j := #{ e_{j-1}(T^-1) mu_n : T admissible }.

j = 1 gives e_0 = 1, E_1 = 1, |Gamma| <= n -- THEOREM Y recovered.
--------------------------------------------------------------------------
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
    t, fac, d = q - 1, [], 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in fac):
            return g
    raise RuntimeError("no primitive root")


def primes_for(n, count=8, lo=None, hi=400000):
    """primes q > n+1 with n | q-1 (q > n+1 keeps -H a PROPER subset)."""
    out, q = [], (n + 1 if lo is None else lo)
    while len(out) < count and q < hi:
        q += 1
        if q % n == 1 and is_prime(q) and q > n + 1:
            out.append(q)
    return out


def make_domain(q, n, beta_exp=0):
    assert (q - 1) % n == 0
    g = primitive_root(q)
    om = pow(g, (q - 1) // n, q)
    x0 = pow(g, beta_exp, q)
    H = [(x0 * pow(om, i, q)) % q for i in range(n)]
    assert len(set(H)) == n
    beta = pow(x0, n, q)
    return H, beta, om


def mu_n_set(H, q):
    """mu_n = H/H[0] as a set."""
    i0 = pow(H[0], q - 2, q)
    return sorted(set((x * i0) % q for x in H))


def coset_rep(v, mu, q):
    """canonical representative of the coset v.mu_n in F_q^* / mu_n."""
    if v % q == 0:
        return 0
    return min((v * t) % q for t in mu)


_ITC = {}


def inv_table(q):
    """inv[a] = a^{-1} mod q for a = 1..q-1 (q prime, small). Cached."""
    if q in _ITC:
        return _ITC[q]
    it = [0] * q
    if q > 1:
        it[1] = 1
        for a in range(2, q):
            it[a] = (-(q // a) * it[q % a]) % q
    _ITC[q] = it
    return it


# ------------------------------------------------------------ polynomials
def peval(cf, x, q):
    a = 0
    for t in reversed(cf):
        a = (a * x + t) % q
    return a


def interp(xs, ys, q):
    kk = len(xs)
    IT = inv_table(q)
    res = [0] * kk
    for i in range(kk):
        num, den, xi = [1], 1, xs[i]
        for jj in range(kk):
            if jj == i:
                continue
            nn = [0] * (len(num) + 1)
            for t, cc in enumerate(num):
                if cc:
                    nn[t + 1] = (nn[t + 1] + cc) % q
                    nn[t] = (nn[t] - cc * xs[jj]) % q
            num = nn
            den = (den * (xi - xs[jj])) % q
        s = (ys[i] * IT[den % q]) % q
        for t in range(kk):
            res[t] = (res[t] + s * num[t]) % q
    return res


def poly_from_roots(roots, q):
    """monic prod (X - x); returns coefficient list, index = degree."""
    cf = [1]
    for x in roots:
        nn = [0] * (len(cf) + 1)
        for t, c in enumerate(cf):
            if c:
                nn[t + 1] = (nn[t + 1] + c) % q
                nn[t] = (nn[t] - c * x) % q
        cf = nn
    return cf


def esym(vals, q, upto):
    """e_0..e_upto of the multiset vals."""
    e = [0] * (upto + 1)
    e[0] = 1
    for x in vals:
        for t in range(min(upto, len(e) - 1), 0, -1):
            e[t] = (e[t] + x * e[t - 1]) % q
    return e


# ------------------------------------------------- theory-free pencil scan
class Scan(object):
    """Ground truth: every codeword of agreement >= k against any member of
    {u + z v} is the interpolant of that member on some k-subset of its
    agreement set, and interp_S(u+zv) = interp_S(u) + z interp_S(v).
    One pass over the k-subsets resolves the whole pencil."""

    def __init__(self, H, q, k, uv, vv, A):
        self.H, self.q, self.k, self.A, self.n = H, q, k, A, len(H)
        self.joint_max = 0
        self.hit = {}
        self._run(uv, vv)

    def _run(self, uv, vv):
        n, k, q, H = self.n, self.k, self.q, self.H
        IT = inv_table(q)
        seen = set()
        for S in combinations(range(n), k):
            xs = [H[i] for i in S]
            f = tuple(interp(xs, [uv[i] for i in S], q))
            g = tuple(interp(xs, [vv[i] for i in S], q))
            if (f, g) in seen:
                continue
            seen.add((f, g))
            nz, zeta = 0, {}
            for i in range(n):
                a = (uv[i] - peval(f, H[i], q)) % q
                b = (vv[i] - peval(g, H[i], q)) % q
                if a == 0 and b == 0:
                    nz += 1
                elif b == 0:
                    zeta[i] = INF
                else:
                    zeta[i] = (-a * IT[b]) % q
            if nz > self.joint_max:
                self.joint_max = nz
            byz = {}
            for i, z in zeta.items():
                byz[z] = byz.get(z, 0) + 1
            for z, ex in byz.items():
                a = nz + ex
                if a > self.hit.get(z, -1):
                    self.hit[z] = a
        self.n_pairs = len(seen)

    def max_agr(self, z):
        return max(self.joint_max, self.hit.get(z, 0))

    def gate_ok(self):
        return (self.joint_max <= self.A
                and not any(a > self.A for a in self.hit.values()))

    def live(self):
        """slopes of max agreement EXACTLY A  ( == Gamma )."""
        if self.joint_max > self.A:
            return []
        if self.joint_max == self.A:
            allz = list(range(self.q)) + [INF]
            return [z for z in allz if self.max_agr(z) == self.A]
        return sorted([z for z, a in self.hit.items() if a == self.A],
                      key=lambda z: (z == INF, z))


# ----------------------------------------------- MY OWN window classifier
def pencil_words(H, q, n, k, w, c, j):
    uv = [(pow(x, n - 1, q) + c * pow(x, k + w - 1, q)) % q for x in H]
    vv = [(uv[i] * pow(pow(H[i], j, q), q - 2, q)) % q for i in range(n)]
    return uv, vv


def classify(H, q, n, k, w, c, j):
    """ALL (T, z), z in F_q^*, solving the exact-A window system, by direct
    enumeration of T (own derivation, no series inversion).  Returns a list
    of dicts with T (indices), m (coefficients of M), z."""
    A = k + w + 1
    rp = n - A
    if rp < 0:
        return []
    out = []
    IT = inv_table(q)

    def leaf(Tc, m):
        T = [H[i] for i in Tc]

        def mc(s):
            return m[s] if 0 <= s <= rp else 0

        al, be = [], []
        for i in range(w + 1):
            a_i = (mc(0) if i == 0 else c * mc(rp + 1 - i)) % q
            b_i = 0
            if 0 <= j - i <= rp:
                b_i = (b_i + mc(j - i)) % q
            if i >= j + 1:
                b_i = (b_i + c * mc(rp + 1 + j - i)) % q
            al.append(a_i % q)
            be.append(b_i % q)
        z = None
        bad = False
        for i in range(w + 1):
            if be[i]:
                zz = (-al[i] * IT[be[i]]) % q
                if z is None:
                    z = zz
                elif z != zz:
                    bad = True
                    break
            elif al[i]:
                bad = True
                break
        if bad or z is None or z == 0:
            return
        out.append({"Tidx": list(Tc), "T": T, "m": m, "z": z})

    # depth-first enumeration of the rp-subsets, sharing polynomial prefixes
    def rec(pos, cf, chosen):
        if len(chosen) == rp:
            leaf(tuple(chosen), cf)
            return
        need = rp - len(chosen)
        for p in range(pos, n - need + 1):
            x = H[p]
            nn = [0] * (len(cf) + 1)
            for t, cc in enumerate(cf):
                if cc:
                    nn[t + 1] = (nn[t + 1] + cc) % q
                    nn[t] = (nn[t] - cc * x) % q
            chosen.append(p)
            rec(p + 1, nn, chosen)
            chosen.pop()

    rec(0, [1], [])
    return out


def classify_multi(H, q, n, k, w, c, js):
    """Same window system, but ONE enumeration of T shared across all shift
    exponents j in js (c does not depend on j).  Returns {j: [sol,...]}."""
    A = k + w + 1
    rp = n - A
    res = dict((j, []) for j in js)
    if rp < 0:
        return res
    IT = inv_table(q)

    def leaf(Tc, m):
        def mc(s):
            return m[s] if 0 <= s <= rp else 0
        for j in js:
            z = None
            bad = False
            for i in range(w + 1):
                a_i = (mc(0) if i == 0 else c * mc(rp + 1 - i)) % q
                b_i = 0
                if 0 <= j - i <= rp:
                    b_i = (b_i + mc(j - i)) % q
                if i >= j + 1:
                    b_i = (b_i + c * mc(rp + 1 + j - i)) % q
                b_i %= q
                if b_i:
                    zz = (-a_i * IT[b_i]) % q
                    if z is None:
                        z = zz
                    elif z != zz:
                        bad = True
                        break
                elif a_i % q:
                    bad = True
                    break
            if bad or z is None or z == 0:
                continue
            res[j].append({"Tidx": list(Tc), "T": [H[i] for i in Tc],
                           "m": m, "z": z})

    def rec(pos, cf, chosen):
        if len(chosen) == rp:
            leaf(tuple(chosen), cf)
            return
        need = rp - len(chosen)
        for p in range(pos, n - need + 1):
            x = H[p]
            nn = [0] * (len(cf) + 1)
            for t, cc in enumerate(cf):
                if cc:
                    nn[t + 1] = (nn[t + 1] + cc) % q
                    nn[t] = (nn[t] - cc * x) % q
            chosen.append(p)
            rec(p + 1, nn, chosen)
            chosen.pop()

    rec(0, [1], [])
    return res


def e_jm1_inv(T, q, j):
    """e_{j-1}(T^{-1})."""
    inv = [pow(x, q - 2, q) for x in T]
    return esym(inv, q, j - 1)[j - 1]


def prodT(T, q):
    p = 1
    for x in T:
        p = (p * x) % q
    return p


# ------------------------------------------------------------ MC family
def mc_cosets(n, M):
    N = n // M
    return [[i for i in range(n) if i % N == jj] for jj in range(N)]


def mc_c_from_gamma(H, q, n, k, w, M):
    rp = n - k - w
    N, m = n // M, rp // M
    cos = mc_cosets(n, M)
    T = [i for jj in range(m) for i in cos[jj]]
    pr = 1
    for i in T:
        pr = (pr * H[i]) % q
    return (((-1) ** (rp + 1)) * pr) % q


def mc_family(H, q, n, k, w, M, c):
    rp = n - k - w
    N, m = n // M, rp // M
    cos = mc_cosets(n, M)
    g = ((-1) ** (rp + 1) * c) % q
    out = []
    for S in combinations(range(N), m):
        T = [i for jj in S for i in cos[jj]]
        pr = 1
        for i in T:
            pr = (pr * H[i]) % q
        if pr == g:
            out.append(tuple(sorted(T)))
    return out


def neg_Hj(H, q, j):
    return set((-pow(x, j, q)) % q for x in H)


# ------------------------------------------------------------- bookkeeping
class Ledger(object):
    def __init__(self):
        self.n = 0
        self.fail = []

    def chk(self, cond, label, extra=None):
        self.n += 1
        if not cond:
            self.fail.append((label, extra))
        return cond

    def report(self, name):
        print("\n[%s] %d checks, %d FAILURES" % (name, self.n, len(self.fail)))
        for lab, ex in self.fail[:40]:
            print("   FAIL:", lab, "" if ex is None else ex)
        return len(self.fail) == 0


def comb(a, b):
    if b < 0 or b > a:
        return 0
    r = 1
    for i in range(b):
        r = r * (a - i) // (i + 1)
    return r


def X_index(n, A, q, w):
    """the gate index X = C(n,A)/q^w, as an exact Fraction-free ratio pair."""
    return comb(n, A), pow(q, w)


def classify_lean(H, q, n, k, w, c, js):
    """Same window system as classify_multi, but tracking ONLY the coefficient
    windows the equations actually touch:

        m_{r'-t} = (-1)^t e_t(T)              for t = 0..w-1     (top)
        m_s      = (-1)^{r'-s} prod(T) e_s(T^-1)  for s = 0..max(js)  (bottom)

    so the per-node cost is O(w + max j) instead of O(r').  Lets n = 33 with
    r' = 26 run.  Returns {j: [ {Tidx, z, e_jm1_inv, prod} ... ]}.
    """
    A = k + w + 1
    rp = n - A
    res = dict((j, []) for j in js)
    if rp < 0:
        return res
    IT = inv_table(q)
    JM = max(js)
    TOP = max(w, 1)                      # need e_0..e_{w-1}(T)
    BOT = JM + 1                         # need e_0..e_JM(T^-1)
    invH = [IT[x] for x in H]
    sgn_rp = [pow(-1, rp - s) for s in range(BOT + 1)]

    def leaf(Tc, eT, eTi, pr):
        # m_{r'-t} = (-1)^t eT[t] ; m_s = (-1)^{r'-s} pr eTi[s]
        def mc(s):
            if s < 0 or s > rp:
                return 0
            if s <= BOT - 1:
                return (sgn_rp[s] * pr * eTi[s]) % q
            t = rp - s
            if t <= TOP - 1:
                return (pow(-1, t) * eT[t]) % q
            raise RuntimeError("coefficient m_%d outside both windows" % s)

        for j in js:
            z = None
            bad = False
            for i in range(w + 1):
                a_i = (mc(0) if i == 0 else c * mc(rp + 1 - i)) % q
                b_i = 0
                if 0 <= j - i <= rp:
                    b_i = (b_i + mc(j - i)) % q
                if i >= j + 1:
                    b_i = (b_i + c * mc(rp + 1 + j - i)) % q
                b_i %= q
                if b_i:
                    zz = (-a_i * IT[b_i]) % q
                    if z is None:
                        z = zz
                    elif z != zz:
                        bad = True
                        break
                elif a_i % q:
                    bad = True
                    break
            if bad or z is None or z == 0:
                continue
            res[j].append({"Tidx": list(Tc), "z": z,
                           "e_jm1_inv": eTi[j - 1], "prod": pr})

    def rec(pos, eT, eTi, pr, chosen):
        if len(chosen) == rp:
            leaf(tuple(chosen), eT, eTi, pr)
            return
        need = rp - len(chosen)
        for p in range(pos, n - need + 1):
            x, xi = H[p], invH[p]
            e2 = eT[:]
            for t in range(TOP - 1, 0, -1):
                e2[t] = (e2[t] + x * e2[t - 1]) % q
            i2 = eTi[:]
            for t in range(BOT - 1, 0, -1):
                i2[t] = (i2[t] + xi * i2[t - 1]) % q
            chosen.append(p)
            rec(p + 1, e2, i2, (pr * x) % q, chosen)
            chosen.pop()

    rec(0, [1] + [0] * (TOP - 1), [1] + [0] * (BOT - 1), 1, [])
    return res

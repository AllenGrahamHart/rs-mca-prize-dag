"""advlib -- INDEPENDENT engine for the adversarial attack on

        Gamma  subset  -H        ("every exact-A live slope of an MC
                                   shift-pencil received pair lies in -H")

Nothing is imported from the pilots under attack; the only cross-import is
band_adjudication.mclib, used READ-ONLY in t1_validate.py as a third opinion.

Contents
  * prime-field arithmetic, multiplicative-coset domains H = x0*mu_n
  * a theory-free pencil scan (ground truth: enumerate k-subsets)
  * the LOCATOR CLASSIFIER for a mixed pencil member (Theorem X below),
    which enumerates *complements* T^c of size a-... and solves for z
  * the MC coset family

--------------------------------------------------------------------------
THEOREM X (classification of the exact-A list of a mixed member).

Setting: H = {x : x^n = beta}, Omega = X^n - beta, C = RS[F_q,H,k],
u  <-> U = X^(n-1) + c X^(k+w-1),  v <-> V = X^(n-1-j) + c X^(k+w-1-j)
(so v(x) = u(x)/x^j on H), w_z = u + z v, A = k+w+1, r = n-k-w, r' = r-1.

By the banked locator normal form (crossing_packet Lemma 1 = (CT1)-(CT5)),
codewords of agreement >= A against w_z are in bijection with monic
M | Omega of degree r' whose coefficients kill the top-(w+1) window of
W_z * M.  Writing i = n-1-d for the window index i = 0..w, the conditions
are LINEAR IN z:

    alpha_i + z * beta_i = 0,     i = 0..w,
    alpha_i = [i=0] m_0 + [i>=1] c m_{r'+1-i},
    beta_i  = [0<=j-i<=r'] m_{j-i} + [i>=j+1] c m_{r'+1+j-i}.

For j = 1 this collapses to the clean form used throughout this pilot:

    m_{r'-t} = (-z)^t  (t = 0..w-1),   m_0 = -c/z,   m_1 = c/z,   (*)

equivalently, setting N := (X+z) * M (monic of degree r):

    [X^{r-t}] N = 0  (t = 1..w-1),   [X^1] N = 0,   N(0) = -c.

i.e. with S := T u {-z} regarded as a multiset of r points, r-1 of which
lie in H and one of which (namely -z) is FREE:

    e_1(S) = ... = e_{w-1}(S) = 0,   e_{r-1}(S) = 0,   prod(S) = gamma.

COMPARE MC-1 (the list of the *pure* member u at agreement k+w):
    S subset H, |S| = r,  e_1(S) = ... = e_{w-1}(S) = 0,  prod(S) = gamma.

So the mixed member's list is *exactly* MC-1's system with one point
allowed to leave H, plus the single extra equation e_{r-1}(S) = 0.

CONSEQUENCE (the attack).  "Gamma subset -H" is EQUIVALENT to the assertion
that the free point -z of every solution S happens to land back in H.  The
MC-derived solutions do that for a structural reason (S = T_MC, a mu_M-coset
union, which satisfies e_{r-1} = 0 for free), but the system itself imposes
NO such constraint.  Gamma subset -H is therefore a COUNTING statement, not
a structural one:  #solutions ~ C(n,A) / q^w  (w equations after z has been
eliminated), and it can only hold while that quantity is < 1.

Complement form actually used by the classifier (cheap: A < r' at low rate).
With E_S(Y) := prod_{x in S}(1-xY) one has E_T . E_{T^c} = 1 - beta Y^n, so
for t < n the top window of T is read off T^c by series inversion, and
    prod(T) = prod(H)/prod(T^c),  sum_T x^-1 = -sum_{T^c} x^-1 .
--------------------------------------------------------------------------
"""

import sys
from itertools import combinations

sys.dont_write_bytecode = True

INF = "inf"


# ------------------------------------------------------------------ field
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


def primes_for(n, count=8, lo=None, hi=200000):
    """primes q > n+1 with n | q-1 (q > n+1 so that -H is a PROPER subset
    of F_q^*, otherwise the confinement claim is vacuous)."""
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
    assert all(pow(x, n, q) == beta for x in H)
    return H, beta, om


# ------------------------------------------------------------ polynomials
def peval(c, x, q):
    a = 0
    for t in reversed(c):
        a = (a * x + t) % q
    return a


def interp(xs, ys, q):
    kk = len(xs)
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
        s = (ys[i] * pow(den, q - 2, q)) % q
        for t in range(kk):
            res[t] = (res[t] + s * num[t]) % q
    return res


# --------------------------------------------- theory-free pencil scan
class Scan(object):
    """Exhaustive, theory-free scan of the pencil {u + z v : z in P^1}.

    Every codeword of agreement >= k against any member is the interpolant
    of that member on some k-subset of its agreement set, and
    interp_S(u+zv) = interp_S(u) + z interp_S(v); so one pass over the
    k-subsets resolves the whole pencil.  Independent re-implementation
    (own interpolation, own bookkeeping) of the same complete enumeration
    the banked pilots use.
    """

    def __init__(self, H, q, k, uv, vv, A):
        self.H, self.q, self.k, self.A, self.n = H, q, k, A, len(H)
        self.uv, self.vv = uv, vv
        self.pairs = {}
        self.joint_max = 0
        self.hit = {}     # z -> max over pairs of (|Z| + #zeta^-1(z))
        self.sup = {}     # z -> {support frozenset: (f,g)} at that max
        self._run()

    def _run(self):
        n, k, q, H, uv, vv = self.n, self.k, self.q, self.H, self.uv, self.vv
        for S in combinations(range(n), k):
            xs = [H[i] for i in S]
            f = tuple(interp(xs, [uv[i] for i in S], q))
            g = tuple(interp(xs, [vv[i] for i in S], q))
            if (f, g) in self.pairs:
                continue
            Z, zeta = [], {}
            for i in range(n):
                a = (uv[i] - peval(f, H[i], q)) % q
                b = (vv[i] - peval(g, H[i], q)) % q
                if a == 0 and b == 0:
                    Z.append(i)
                elif b == 0:
                    zeta[i] = INF
                else:
                    zeta[i] = (-a * pow(b, q - 2, q)) % q
            Zf = frozenset(Z)
            self.pairs[(f, g)] = (Zf, zeta)
            if len(Z) > self.joint_max:
                self.joint_max = len(Z)
            byz = {}
            for i, z in zeta.items():
                byz.setdefault(z, []).append(i)
            for z, ex in byz.items():
                a = len(Z) + len(ex)
                cur = self.hit.get(z, -1)
                if a > cur:
                    self.hit[z] = a
                    self.sup[z] = {Zf | frozenset(ex): (f, g)}
                elif a == cur:
                    self.sup[z][Zf | frozenset(ex)] = (f, g)

    def max_agr(self, z):
        return max(self.joint_max, self.hit.get(z, 0))

    def all_slopes(self):
        return list(range(self.q)) + [INF]

    def over_agreeing(self):
        """slopes whose max agreement EXCEEDS A (tangent-gate breakers)."""
        return {z: a for z, a in self.hit.items() if a > self.A}

    def gate_ok(self):
        return self.joint_max <= self.A and not self.over_agreeing()

    def live(self):
        """slopes of max agreement EXACTLY A (== Gamma)."""
        if self.joint_max > self.A:
            return []
        if self.joint_max == self.A:
            return [z for z in self.all_slopes() if self.max_agr(z) == self.A]
        return sorted([z for z, a in self.hit.items() if a == self.A],
                      key=lambda z: (z == INF, z))

    def exactA_supports(self, z):
        if self.hit.get(z, 0) != self.A:
            return {}
        return self.sup[z]


# ---------------------------------------------------- series helpers
def ser_mul(a, b, L, q):
    out = [0] * L
    for i, ai in enumerate(a):
        if ai:
            for jj in range(0, L - i):
                if b[jj]:
                    out[i + jj] = (out[i + jj] + ai * b[jj]) % q
    return out


def ser_inv(a, L, q):
    """1/a mod Y^L, a[0] must be 1."""
    assert a[0] % q == 1
    out = [0] * L
    out[0] = 1
    for i in range(1, L):
        s = 0
        for jj in range(1, i + 1):
            if jj < len(a) and a[jj]:
                s += a[jj] * out[i - jj]
        out[i] = (-s) % q
    return out


# ------------------------------------------------- the LOCATOR CLASSIFIER
def classify_mixed(H, beta, q, n, k, w, c, j, a_target=None, want_cw=True):
    """ALL (T, z) with z in F_q, z != 0, such that some codeword agrees with
    w_z = u + z v in >= a_target positions off T, |T| = n - a_target.

    Implements THEOREM X: enumerate the complement T^c (size a_target),
    recover the needed coefficients of M = prod_{x in T}(X-x) by series
    inversion, build (alpha_i, beta_i) for i = 0..W (W = a_target-k), and
    solve alpha_i + z beta_i = 0.

    Returns a list of dicts {T (indices), z, agreement, codeword}.
    """
    if a_target is None:
        a_target = k + w + 1
    W = a_target - k          # window length (= w+1 at the exact-A target)
    A_ = a_target
    rp = n - A_               # |T| = deg M
    if rp < 0:
        return []
    prodH = 1
    for x in H:
        prodH = (prodH * x) % q
    inv = [pow(x, q - 2, q) for x in H]
    uv = [(pow(x, n - 1, q) + c * pow(x, k + w - 1, q)) % q for x in H]
    vv = [(uv[i] * pow(inv[i], j, q)) % q for i in range(n)]

    delta = a_target - (k + w)
    Ltop = max(W, w, 1)  # need e_0..e_{w-1}(T) at least
    Lbot = j + 1         # need e_0..e_j(T^{-1})
    res = []

    # depth-first enumeration of A_-subsets carrying the two truncated
    # series of the COMPLEMENT plus its product
    def rec(pos, cnt, Es, Ei, pr, chosen):
        if cnt == A_:
            _leaf(Es, Ei, pr, chosen)
            return
        if n - pos < A_ - cnt:
            return
        for p in range(pos, n - (A_ - cnt) + 1):
            x, xi = H[p], inv[p]
            Es2 = [0] * Ltop
            for t in range(Ltop):
                Es2[t] = Es[t]
            for t in range(Ltop - 1, 0, -1):
                Es2[t] = (Es2[t] - x * Es[t - 1]) % q
            Ei2 = [0] * Lbot
            for t in range(Lbot):
                Ei2[t] = Ei[t]
            for t in range(Lbot - 1, 0, -1):
                Ei2[t] = (Ei2[t] - xi * Ei[t - 1]) % q
            chosen.append(p)
            rec(p + 1, cnt + 1, Es2, Ei2, (pr * x) % q, chosen)
            chosen.pop()

    def _leaf(Es, Ei, pr, chosen):
        # E_T = (1 - beta Y^n)/E_{T^c} == 1/E_{T^c} mod Y^Ltop (Ltop <= n)
        ET = ser_inv(Es, Ltop, q)
        ETi = ser_inv(Ei, Lbot, q)
        prodT = (prodH * pow(pr, q - 2, q)) % q
        # m_{rp-t} = (-1)^t e_t(T) = [Y^t] E_T
        # m_s      = (-1)^{rp-s} e_{rp-s}(T) = (-1)^{rp-s} prodT e_s(T^{-1})
        #          = (-1)^{rp} prodT [Y^s] E_T^{-1}   (signs cancel)
        def mtop(s):                      # s in [rp-Ltop+1, rp]
            t = rp - s
            if t < 0 or t >= Ltop:
                return None
            return ET[t]

        def mbot(s):                      # s in [0, Lbot-1]
            if s < 0 or s >= Lbot:
                return None
            return (pow(-1, rp) * prodT * ETi[s]) % q

        def mcoef(s):
            if s < 0 or s > rp:
                return 0
            r1 = mbot(s)
            if r1 is not None:
                return r1
            r2 = mtop(s)
            if r2 is not None:
                return r2
            raise RuntimeError("coefficient m_%d outside both windows" % s)

        al, be = [], []
        for i in range(W):
            a_i = (mcoef(-i) + c * mcoef(rp + delta - i)) % q
            b_i = (mcoef(j - i) + c * mcoef(rp + delta + j - i)) % q
            al.append(a_i)
            be.append(b_i)
        # solve alpha_i + z beta_i = 0 for all i
        z = None
        for i in range(W):
            if be[i] % q:
                zz = (-al[i] * pow(be[i], q - 2, q)) % q
                if z is None:
                    z = zz
                elif z != zz:
                    return
            else:
                if al[i] % q:
                    return
        if z is None or z == 0:
            return
        T = [p for p in range(n) if p not in set(chosen)]
        rec_out = {"T": T, "Tc": list(chosen), "z": z}
        if want_cw:
            wz = [(uv[i] + z * vv[i]) % q for i in range(n)]
            xs = [H[i] for i in chosen[:k]]
            P = interp(xs, [wz[i] for i in chosen[:k]], q)
            agr = sum(1 for i in range(n) if peval(P, H[i], q) == wz[i])
            rec_out["agreement"] = agr
            rec_out["codeword"] = tuple(P)
        res.append(rec_out)

    rec(0, 0, [1] + [0] * (Ltop - 1), [1] + [0] * (Lbot - 1), 1, [])
    return res


# --------------------------------------------------------- the MC family
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
    gamma = ((-1) ** (rp + 1) * c) % q
    out = []
    for S in combinations(range(N), m):
        T = [i for jj in S for i in cos[jj]]
        pr = 1
        for i in T:
            pr = (pr * H[i]) % q
        if pr == gamma:
            out.append(tuple(sorted(T)))
    return out


def mc_pencil_words(H, q, n, k, w, M, j=1, c=None):
    """the MC shift-pencil received pair (u, v), v = u/X^j on H."""
    if c is None:
        c = mc_c_from_gamma(H, q, n, k, w, M)
    uv = [(pow(x, n - 1, q) + c * pow(x, k + w - 1, q)) % q for x in H]
    vv = [(uv[i] * pow(pow(H[i], j, q), q - 2, q)) % q for i in range(n)]
    return c, uv, vv


def neg_H(H, q):
    return set((-x) % q for x in H)


def neg_Hj(H, q, j):
    """-H^j = {-x^j : x in H}; equals -H when gcd(j,n) = 1 (H a coset of
    mu_n and x -> x^j then permutes mu_n up to the coset shift)."""
    return set((-pow(x, j, q)) % q for x in H)


def predicted_coset_j1(H, q, n, k, w, c):
    """THEOREM Y (this pilot).  For j = 1 every exact-A live slope of the
    shift pencil satisfies  -z = gamma / prod(T)  with  gamma = (-1)^(r+1) c
    and prod(T) in x0^(r-1) mu_n; hence

        Gamma  subset  - gamma * x0^{-(r-1)} * mu_n ,

    ONE multiplicative coset of mu_n -- so |Gamma| <= n unconditionally, and
    the coset equals -H exactly when gamma is realizable (gamma in x0^r mu_n,
    i.e. the PK1/(H3) condition that makes the MC family non-empty).
    """
    r = n - k - w
    gamma = ((-1) ** (r + 1) * c) % q
    x0 = H[0]
    base = (gamma * pow(pow(x0, r - 1, q), q - 2, q)) % q
    mu = set(pow(x, n, q) for x in H)          # sanity: {beta}
    assert len(mu) == 1
    # mu_n as a set
    munset = set((H[i] * pow(H[0], q - 2, q)) % q for i in range(n))
    return set((-base * t) % q for t in munset), gamma

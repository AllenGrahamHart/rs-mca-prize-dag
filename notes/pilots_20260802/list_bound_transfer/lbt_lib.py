"""lbt_lib -- exact machinery for the list-bound transfer pilot.

Domain: H = {x in F_q : x^n = beta}, n | q-1, gcd(n,q) = 1 (split
multiplicative coset -- the official prize shape).  C = RS[F_q, H, k].

Everything here is exact integer arithmetic mod a prime q (prime fields
only; extension fields handled by ext_field.py if needed).

Primary list census is THEORY-FREE: every codeword P with agreement >= k
against a word U is the Lagrange interpolant of U on some k-subset of its
agreement set, so enumerating all k-subsets and interpolating yields the
complete list.  No use is made of the locator/Toeplitz theory when
computing a census -- that theory is what we are testing.
"""

import sys
from itertools import combinations

sys.dont_write_bytecode = True


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


def primes_with_n_dividing_qm1(n, count=6, lo=3, hi=100000):
    """Primes q > lo with n | q-1 and q odd (so Omega = X^n - beta is squarefree)."""
    out = []
    q = lo
    while len(out) < count and q < hi:
        q += 1
        if q % n != 1:
            continue
        if is_prime(q):
            out.append(q)
    return out


def primitive_root(q):
    """A generator of F_q^*."""
    m = q - 1
    fac = []
    t, d = m, 2
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
    """H = x0 * mu_n where x0 = g^beta_exp, so beta = x0^n.

    Returns (H, beta, omega) with omega a generator of mu_n; H is listed as
    x0*omega^i for i = 0..n-1.
    """
    assert (q - 1) % n == 0
    g = primitive_root(q)
    omega = pow(g, (q - 1) // n, q)
    x0 = pow(g, beta_exp, q)
    H = [(x0 * pow(omega, i, q)) % q for i in range(n)]
    assert len(set(H)) == n
    beta = pow(x0, n, q)
    assert all(pow(x, n, q) == beta for x in H)
    return H, beta, omega


# ---------------------------------------------------------- polynomials
def poly_eval(coeffs, x, q):
    """coeffs[i] = coefficient of X^i."""
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % q
    return acc


def poly_mulX_minus_a(coeffs, a, q):
    """(sum coeffs) * (X - a)."""
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        if c:
            out[i + 1] = (out[i + 1] + c) % q
            out[i] = (out[i] - c * a) % q
    return out


def vanishing_poly(pts, q):
    m = [1]
    for a in pts:
        m = poly_mulX_minus_a(m, a, q)
    return m


def interpolate(xs, ys, q):
    """Lagrange interpolation; returns coefficient list of length len(xs)."""
    kk = len(xs)
    res = [0] * kk
    for i in range(kk):
        # basis poly prod_{j!=i} (X - xs[j]) / (xs[i]-xs[j])
        num = [1]
        den = 1
        xi = xs[i]
        for j in range(kk):
            if j == i:
                continue
            num = poly_mulX_minus_a(num, xs[j], q)
            den = (den * (xi - xs[j])) % q
        s = (ys[i] * pow(den, q - 2, q)) % q
        for t in range(kk):
            res[t] = (res[t] + s * num[t]) % q
    return res


def trim(coeffs):
    c = list(coeffs)
    while c and c[-1] == 0:
        c.pop()
    return c


# ------------------------------------------------------------ the word
def word_values(Ucoeffs, H, q):
    return [poly_eval(Ucoeffs, x, q) for x in H]


def agreement(Pcoeffs, Uvals, H, q):
    return sum(1 for i, x in enumerate(H) if poly_eval(Pcoeffs, x, q) == Uvals[i])


# ------------------------------------------------- THEORY-FREE census
def full_list_census(Uvals, H, k, q, amin=None):
    """Return {P_tuple: agreement} for every codeword of agreement >= max(k, amin).

    Complete by construction: any P with agr >= k interpolates U on some
    k-subset of its agreement set.
    """
    n = len(H)
    if amin is None:
        amin = k
    seen = {}
    idx = range(n)
    for S in combinations(idx, k):
        xs = [H[i] for i in S]
        ys = [Uvals[i] for i in S]
        P = tuple(interpolate(xs, ys, q))
        if P in seen:
            continue
        a = agreement(list(P), Uvals, H, q)
        seen[P] = a
    return {P: a for P, a in seen.items() if a >= amin}


def shell_profile(Uvals, H, k, q):
    cen = full_list_census(Uvals, H, k, q)
    prof = {}
    for P, a in cen.items():
        prof[a] = prof.get(a, 0) + 1
    return prof


# ------------------------------------------- the MC coset construction
def mc_family(H, q, n, k, w, M, c):
    """The multiplicative-coset (MC) family for the word

        U = X^(n-1) + c*X^(k+w-1)        (r' = n-k-w)

    T ranges over unions of r'/M cosets of mu_M inside H whose product is
    gamma = (-1)^(r'+1) * c.

    Returns the list of T (as tuples of domain INDICES) that satisfy the
    product condition.  Requires M | n, M | r', w <= M.
    """
    rp = n - k - w
    assert n % M == 0 and rp % M == 0 and w <= M, (n, rp, M, w)
    N = n // M
    m = rp // M
    # index i of H corresponds to x0*omega^i; the mu_M-cosets are the
    # residue classes of i modulo N (since omega^N generates mu_M).
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    assert all(len(cl) == M for cl in cosets)
    gamma = ((-1) ** (rp + 1) * c) % q
    out = []
    for S in combinations(range(N), m):
        T = [i for j in S for i in cosets[j]]
        prod = 1
        for i in T:
            prod = (prod * H[i]) % q
        if prod == gamma:
            out.append(tuple(sorted(T)))
    return out


def mc_count_formula(n, k, w, M):
    """Exact predicted size of the MC family when gcd(r'/M, n/M) = 1:
    C(N, m)/N with N = n/M, m = r'/M."""
    from math import comb, gcd
    rp = n - k - w
    N, m = n // M, rp // M
    if gcd(m, N) == 1:
        return comb(N, m) // N, True
    return None, False


def codeword_from_T(Ucoeffs, T_idx, H, k, n, q, beta):
    """P such that (U - P) vanishes off T, if deg P < k; else None.

    P = (U*M mod Omega)/M with M the vanishing polynomial of T.
    """
    Tpts = [H[i] for i in T_idx]
    M = vanishing_poly(Tpts, q)
    # U*M
    prod = [0] * (len(Ucoeffs) + len(M) - 1)
    for i, a in enumerate(Ucoeffs):
        if not a:
            continue
        for j, b in enumerate(M):
            if b:
                prod[i + j] = (prod[i + j] + a * b) % q
    # reduce mod X^n - beta
    red = [0] * n
    for d, cf in enumerate(prod):
        red[d % n] = (red[d % n] + cf * pow(beta, d // n, q)) % q
    red = trim(red)
    # divide by M exactly
    Pq, rem = poly_divmod(red, M, q)
    if trim(rem):
        return None
    if len(trim(Pq)) > k:
        return None
    P = trim(Pq) + [0] * (k - len(trim(Pq)))
    return tuple(P[:k])


def poly_divmod(a, b, q):
    a = list(a)
    b = trim(b)
    if not b:
        raise ZeroDivisionError
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


# --------------------------------------------------------------- pencil
def pencil_members(U1, U2, q):
    """Yield (label, coefficient-list) for the q+1 members of the pencil
    spanned by U1 and U2: w_z = U1 + z*U2 for z in F_q, plus w_inf = U2."""
    L = max(len(U1), len(U2))
    a = U1 + [0] * (L - len(U1))
    b = U2 + [0] * (L - len(U2))
    for z in range(q):
        yield (z, [(a[i] + z * b[i]) % q for i in range(L)])
    yield ("inf", list(b))


def joint_explanation_max(u_vals, v_vals, H, k, q):
    """max over (f,g) in C^2 of |{x : u(x)=f(x) and v(x)=g(x)}|.

    Any joint set of size >= k determines (f,g); enumerate k-subsets.
    """
    n = len(H)
    best = 0
    best_pair = None
    for S in combinations(range(n), k):
        xs = [H[i] for i in S]
        f = interpolate(xs, [u_vals[i] for i in S], q)
        g = interpolate(xs, [v_vals[i] for i in S], q)
        cnt = 0
        for i, x in enumerate(H):
            if poly_eval(f, x, q) == u_vals[i] and poly_eval(g, x, q) == v_vals[i]:
                cnt += 1
        if cnt > best:
            best, best_pair = cnt, (tuple(f), tuple(g))
    return best, best_pair

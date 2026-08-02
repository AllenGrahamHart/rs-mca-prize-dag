"""Exact relation-lattice machinery for the WCL count-bound pilot.

Everything is exact: integers and Fractions only.  No floats anywhere in any
emitted certificate field.

OBJECT OF RECORD
----------------
Fix an odd prime q, an even order M = 2h with M | q - 1, and omega in F_q of
exact order M.  Write the ambient ring as Z[x]/(x^h + 1) = Z[zeta_M], with the
coefficient (power) basis 1, x, ..., x^{h-1}; a vector a in Z^h denotes
alpha = sum_i a_i x^i.  For a set U of odd residues mod M with |U| = o define

    L_{q,M,U} = { a in Z^h : sum_i a_i omega^{u i} = 0 in F_q  for all u in U }.

This is the coefficient-embedding image of the ideal I = prod_{u in U} p_u,
where p_u = ker( Z[zeta_M] -> F_q, zeta_M |-> omega^u ) is a degree-one prime
above q.  Facts used throughout (proved in the report):

  * det L = N(I) = q^o                                (index of I in Z[zeta_M])
  * a reduced signed weight-w relation is exactly a lattice point of L with
    coefficients in {0,+1,-1} and squared Euclidean length w
  * multiplication by x is a NEGACYCLIC SHIFT, an isometry of Z^h preserving L
  * hence lambda_1(L) = lambda_2(L) = ... = lambda_h(L)   (all minima equal)
  * L <= Z^h, so lambda_1(L)^2 is a positive INTEGER.
"""

from fractions import Fraction
from math import isqrt


# ----------------------------------------------------------------- field ---

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


def element_of_exact_order(q, M):
    """Smallest g in F_q^* of exact order M (M | q-1).  Deterministic."""
    assert (q - 1) % M == 0
    e = (q - 1) // M
    # prime factors of M (M is small here)
    fac, m, d = [], M, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for base in range(2, q):
        g = pow(base, e, q)
        if g == 0:
            continue
        if all(pow(g, M // p, q) != 1 for p in fac):
            return g
    raise RuntimeError("no element of exact order %d mod %d" % (M, q))


def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


# --------------------------------------------------------------- lattice ---

def relation_lattice_basis(q, M, U, omega=None):
    """Row basis (list of h integer vectors) of L_{q,M,U}; det = q^{|U|}.

    Construction: reduce the |U| x h check matrix A[u][i] = omega^{u i} to
    reduced row echelon form over F_q; free columns give unit vectors, pivot
    columns give q e_p.  Exact, no reduction algorithm needed for correctness.
    """
    h = M // 2
    if omega is None:
        omega = element_of_exact_order(q, M)
    A = [[pow(omega, (u * i) % M, q) for i in range(h)] for u in U]
    # rref over F_q
    piv = []
    r = 0
    for c in range(h):
        pr = None
        for rr in range(r, len(A)):
            if A[rr][c] % q:
                pr = rr
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], q - 2, q)
        A[r] = [(v * inv) % q for v in A[r]]
        for rr in range(len(A)):
            if rr != r and A[rr][c] % q:
                f = A[rr][c]
                A[rr] = [(A[rr][k] - f * A[r][k]) % q for k in range(h)]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    assert len(piv) == len(U), "check matrix rank %d != %d" % (len(piv), len(U))
    free = [c for c in range(h) if c not in piv]
    basis = []
    for f in free:
        v = [0] * h
        v[f] = 1
        for j, p in enumerate(piv):
            v[p] = (-A[j][f]) % q
        basis.append(v)
    for p in piv:
        v = [0] * h
        v[p] = q
        basis.append(v)
    return basis, omega


def in_lattice(a, q, M, U, omega):
    return all(sum(a[i] * pow(omega, (u * i) % M, q) for i in range(len(a))) % q == 0
               for u in U)


def negacyclic_shift(a):
    """coefficient vector of x * alpha in Z[x]/(x^h+1)."""
    return [-a[-1]] + list(a[:-1])


# ------------------------------------------------------------------- LLL ---

def _gram_schmidt(B):
    n = len(B)
    mu = [[Fraction(0)] * n for _ in range(n)]
    Bs = []          # squared GS norms, Fractions
    Bstar = []
    for i in range(n):
        v = [Fraction(x) for x in B[i]]
        for j in range(i):
            if Bs[j] == 0:
                mu[i][j] = Fraction(0)
                continue
            num = sum(Fraction(B[i][k]) * Bstar[j][k] for k in range(len(v)))
            mu[i][j] = num / Bs[j]
            v = [v[k] - mu[i][j] * Bstar[j][k] for k in range(len(v))]
        Bstar.append(v)
        Bs.append(sum(x * x for x in v))
    return mu, Bs, Bstar


def det_int(B):
    """Exact fraction-free Bareiss determinant of a square integer matrix."""
    A = [row[:] for row in B]
    n = len(A)
    sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            for r in range(k + 1, n):
                if A[r][k]:
                    A[k], A[r] = A[r], A[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def fast_lll(B, delta=0.99):
    """Float-GUIDED LLL.  All row operations are exact integer operations, so
    the output always spans the SAME lattice as the input; floats only steer
    the search.  Callers must (and this pilot does) verify the output by an
    exact determinant + membership check -- see `certify_basis`.  Enumeration
    downstream re-derives Gram-Schmidt exactly in Fractions, so no result ever
    depends on the floating-point path.
    """
    import numpy as np
    B = [list(map(int, b)) for b in B]
    n = len(B)

    def gs():
        M = np.array(B, dtype=float)
        mu = np.zeros((n, n))
        Bst = np.zeros_like(M)
        Bs = np.zeros(n)
        for i in range(n):
            v = M[i].copy()
            for j in range(i):
                if Bs[j] > 0:
                    mu[i][j] = float(np.dot(M[i], Bst[j])) / Bs[j]
                    v -= mu[i][j] * Bst[j]
            Bst[i] = v
            Bs[i] = float(np.dot(v, v))
        return mu, Bs

    mu, Bs = gs()
    k = 1
    guard = 0
    while k < n:
        guard += 1
        if guard > 4000 * n:
            break
        for j in range(k - 1, -1, -1):
            if abs(mu[k][j]) > 0.5:
                r = int(round(mu[k][j]))
                if r:
                    for t in range(len(B[k])):
                        B[k][t] -= r * B[j][t]
                    mu, Bs = gs()
        if Bs[k] >= (delta - mu[k][k - 1] ** 2) * Bs[k - 1]:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            mu, Bs = gs()
            k = max(k - 1, 1)
    return B


def certify_basis(R, q, M, U, omega):
    """Exact certificate that R is a basis of L_{q,M,U}: right determinant and
    every row in the lattice."""
    if abs(det_int(R)) != q ** len(U):
        return False
    return all(in_lattice(v, q, M, U, omega) for v in R)


def lll(B, delta=Fraction(99, 100)):
    """Exact rational LLL.  Returns a reduced basis (list of int vectors)."""
    B = [list(map(int, b)) for b in B]
    n = len(B)
    mu, Bs, Bstar = _gram_schmidt(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            if abs(mu[k][j]) > Fraction(1, 2):
                r = int(mu[k][j] + Fraction(1, 2)) if mu[k][j] > 0 else \
                    -int(-mu[k][j] + Fraction(1, 2))
                # round-half-away, then correct
                if abs(mu[k][j] - r) > Fraction(1, 2):
                    r += 1 if mu[k][j] > r else -1
                B[k] = [B[k][t] - r * B[j][t] for t in range(len(B[k]))]
                mu, Bs, Bstar = _gram_schmidt(B)
        if Bs[k] >= (delta - mu[k][k - 1] ** 2) * Bs[k - 1]:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            mu, Bs, Bstar = _gram_schmidt(B)
            k = max(k - 1, 1)
    return B


# --------------------------------------------------------- enumeration -----

def enumerate_short(B, bound_sq):
    """ALL v in L(B), v != 0, with ||v||^2 <= bound_sq (an integer).

    Exact Fincke-Pohst on the rational Gram-Schmidt.  Returns a list of integer
    vectors, one per +/- pair (the first nonzero coordinate of the returned
    representative in the GS ordering is positive).
    """
    n = len(B)
    mu, Bs, _ = _gram_schmidt(B)
    bound = Fraction(bound_sq)
    out = []
    x = [0] * n
    # partial sums:  c[i] = sum_{j>i} mu[j][i] x_j ;  rho[i] = tail cost
    def rec(i, rho):
        if i < 0:
            if any(x):
                v = [sum(x[j] * B[j][t] for j in range(n)) for t in range(len(B[0]))]
                out.append(v)
            return
        if Bs[i] == 0:
            return
        c = -sum(mu[j][i] * x[j] for j in range(i + 1, n))
        # (x_i - c)^2 * Bs[i] <= bound - rho
        room = bound - rho
        if room < 0:
            return
        # |x_i - c| <= sqrt(room / Bs[i])
        t = room / Bs[i]
        # integer range
        lim_num = t.numerator
        lim_den = t.denominator
        s = Fraction(isqrt(lim_num * lim_den) + 1, lim_den)
        lo = c - s
        hi = c + s
        xi_lo = -((-lo.numerator) // lo.denominator) if lo >= 0 else -((-lo.numerator + lo.denominator - 1) // lo.denominator)
        # simpler: ceil(lo)
        xi_lo = -((-lo.numerator) // lo.denominator)
        xi_hi = hi.numerator // hi.denominator
        for xi in range(xi_lo, xi_hi + 1):
            d = (Fraction(xi) - c) ** 2 * Bs[i]
            if d > room:
                continue
            x[i] = xi
            rec(i - 1, rho + d)
        x[i] = 0

    # break the +/- symmetry on the top coordinate
    def rec_top():
        i = n - 1
        room = bound
        t = room / Bs[i]
        s = Fraction(isqrt(t.numerator * t.denominator) + 1, t.denominator)
        hi = s.numerator // s.denominator
        for xi in range(0, hi + 1):
            d = Fraction(xi) ** 2 * Bs[i]
            if d > room:
                continue
            x[i] = xi
            if xi == 0:
                rec_pos(i - 1, d)
            else:
                rec(i - 1, d)
        x[i] = 0

    def rec_pos(i, rho):
        """same as rec but the leading nonzero coordinate must be > 0"""
        if i < 0:
            return
        if Bs[i] == 0:
            return
        c = -sum(mu[j][i] * x[j] for j in range(i + 1, n))
        room = bound - rho
        if room < 0:
            return
        t = room / Bs[i]
        s = Fraction(isqrt(t.numerator * t.denominator) + 1, t.denominator)
        lo, hi = c - s, c + s
        xi_lo = -((-lo.numerator) // lo.denominator)
        xi_hi = hi.numerator // hi.denominator
        for xi in range(max(xi_lo, 0), xi_hi + 1):
            d = (Fraction(xi) - c) ** 2 * Bs[i]
            if d > room:
                continue
            x[i] = xi
            if xi == 0:
                rec_pos(i - 1, rho + d)
            else:
                rec(i - 1, rho + d)
        x[i] = 0

    rec_top()
    return out


def sq_norm(v):
    return sum(t * t for t in v)


def is_ternary(v):
    return all(t in (-1, 0, 1) for t in v)


def weight(v):
    return sum(1 for t in v if t)


def lambda1_sq(B, start=1, cap=None):
    """Exact squared first minimum, by widening exact enumeration."""
    b = start
    if cap is None:
        cap = min(sq_norm(v) for v in B)
    while True:
        vs = enumerate_short(B, b)
        if vs:
            return min(sq_norm(v) for v in vs)
        if b >= cap:
            return cap
        b = min(cap, 2 * b) if b > 1 else 2


# --------------------------------------------------------------- fences ---

def amgm_fence(q, h, o):
    """min E in Z_{>0} with E^h >= q^{2o}: the AM-GM lower bound on lambda_1^2.

    Any nonzero alpha in I has q^o <= |Norm(alpha)| <= (sum a_i^2)^{h/2}.
    """
    target = q ** (2 * o)
    lo, hi = 1, 1
    while hi ** h < target:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** h >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ------------------------------------------------------------- self-test ---

def _selftest():
    res = {}
    # 1. determinant of the relation lattice is exactly q^o
    checks = []
    for (q, M, U) in [(97, 32, (1,)), (97, 32, (1, 3)), (193, 32, (1, 3)),
                      (577, 32, (1,)), (257, 64, (1, 3)), (449, 32, (1, 3, 5))]:
        B, om = relation_lattice_basis(q, M, U)
        d = abs(det_int(B))
        checks.append((q, M, list(U), d, q ** len(U), d == q ** len(U)))
    res["det_eq_q_pow_o"] = checks
    res["det_all_ok"] = all(c[-1] for c in checks)

    # 2. negacyclic shift preserves the lattice and the norm
    B, om = relation_lattice_basis(97, 32, (1,))
    ok = True
    for b in B:
        s = b
        for _ in range(16):
            s = negacyclic_shift(s)
            if not in_lattice(s, 97, 32, (1,), om) or sq_norm(s) != sq_norm(b):
                ok = False
    res["shift_is_lattice_isometry"] = ok

    # 3. LLL preserves the lattice (determinant + membership)
    R = lll(B)
    res["lll_preserves_det"] = abs(det_int(R)) == 97
    res["lll_members"] = all(in_lattice(v, 97, 32, (1,), om) for v in R)

    # 4. enumeration completeness cross-check against brute force on a
    #    small lattice: h=8 (M=16), all 3^8 ternary vectors.
    q, M, U = 17, 16, (1,)
    B, om = relation_lattice_basis(q, M, U)
    R = lll(B)
    brute = []
    import itertools
    for a in itertools.product((-1, 0, 1), repeat=8):
        if any(a) and in_lattice(list(a), q, M, U, om) and sq_norm(a) <= 4:
            brute.append(tuple(a))
    enum = enumerate_short(R, 4)
    enum_t = set()
    for v in enum:
        if is_ternary(v):
            enum_t.add(tuple(v))
            enum_t.add(tuple(-t for t in v))
    res["enum_vs_brute_n_brute"] = len(brute)
    res["enum_vs_brute_match"] = set(brute) == enum_t
    res["enum_vs_brute_sample"] = sorted(brute)[:3]

    # 5. all successive minima equal: 16 independent shifts of a minimal vector
    q, M, U = 97, 32, (1,)
    B, om = relation_lattice_basis(q, M, U)
    R = lll(B)
    l1 = lambda1_sq(R, start=1, cap=16)
    vs = [v for v in enumerate_short(R, l1) if sq_norm(v) == l1]
    v0 = vs[0]
    orb = [v0]
    s = v0
    for _ in range(15):
        s = negacyclic_shift(s)
        orb.append(s)
    res["lambda1_sq_97_ell1_M32"] = l1
    res["orbit_all_same_norm"] = all(sq_norm(o) == l1 for o in orb)
    res["orbit_rank"] = abs(det_int(orb)) != 0
    res["amgm_fence_97_h16_o1"] = amgm_fence(97, 16, 1)

    # 6. fast_lll agrees with exact lll: same lattice, and identical short-vector
    #    multiset at radius^2 = 6 on three lattices.
    agree = []
    for (q, M, U) in [(97, 32, (1,)), (353, 32, (1,)), (97, 32, (1, 3))]:
        B, om = relation_lattice_basis(q, M, U)
        Rx = lll(B)
        Rf = fast_lll(B)
        cert = certify_basis(Rf, q, M, U, om)
        sx = sorted(sq_norm(v) for v in enumerate_short(Rx, 6))
        sf = sorted(sq_norm(v) for v in enumerate_short(Rf, 6))
        agree.append((q, list(U), cert, sx == sf, len(sx)))
    res["fast_lll_agrees"] = agree
    res["fast_lll_ok"] = all(a[2] and a[3] for a in agree)

    res["selftest_pass"] = (res["det_all_ok"] and res["shift_is_lattice_isometry"]
                            and res["lll_preserves_det"] and res["lll_members"]
                            and res["enum_vs_brute_match"]
                            and res["orbit_all_same_norm"] and res["orbit_rank"]
                            and res["fast_lll_ok"])
    return res


if __name__ == "__main__":
    import json, sys
    r = _selftest()
    print(json.dumps(r, indent=1, default=str))
    sys.exit(0 if r["selftest_pass"] else 1)

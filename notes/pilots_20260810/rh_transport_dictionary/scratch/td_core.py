"""td_core.py -- shared exact arithmetic for the (t,M) transport dictionary.

Setting (round-31 rh_transport_dictionary, matches the banked razor object):
  D = mu_n subset F_q (q prime, q = 1 mod n), C = RS[n,k] = evals of deg < k,
  k = n/2, excess sigma >= 1, agreement threshold a = k + sigma, m = n - a.
  F_LIST(y) = #{ f in C : agree(y,f) >= a }.

Banked qcore count (background/nodes/ww_lower_witnesses/proof.md):
  M | k, M | n, 1 <= sigma < M, N = n/M, count = C(N-1, k/M).

stdlib only.
"""
from math import comb, gcd


def is_prime(p):
    if p < 2:
        return False
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        if p % d == 0:
            return p == d
    i = 37
    while i * i <= p:
        if p % i == 0:
            return False
        i += 2
    return True


def primes_1_mod_n(n, count=4, start=2):
    out = []
    p = start
    while len(out) < count:
        p += 1
        if p % n == 1 and is_prime(p):
            out.append(p)
    return out


def primitive_root(q):
    fac = []
    r = q - 1
    d = 2
    while d * d <= r:
        if r % d == 0:
            fac.append(d)
            while r % d == 0:
                r //= d
        d += 1
    if r > 1:
        fac.append(r)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise RuntimeError("no primitive root")


def mu(n, q):
    """The n-th roots of unity in F_q, as [g^0, g^1, ..., g^(n-1)]."""
    assert (q - 1) % n == 0
    g = pow(primitive_root(q), (q - 1) // n, q)
    out = [1] * n
    for i in range(1, n):
        out[i] = out[i - 1] * g % q
    assert out[n - 1] * g % q == 1
    return out


def divisors(x):
    return [d for d in range(1, x + 1) if x % d == 0]


def qcore_family(n, k, sigma):
    """All admissible (M, N, k/M, count) for the banked qcore construction."""
    out = []
    for M in divisors(gcd(n, k)):
        if not (1 <= sigma < M):
            continue
        N = n // M
        km = k // M
        if km > N - 1:
            continue
        out.append((M, N, km, comb(N - 1, km)))
    return out


def qcore_count(n, k, sigma):
    fam = qcore_family(n, k, sigma)
    if not fam:
        return 0, None
    best = max(fam, key=lambda z: z[3])
    return best[3], best


def qcore_signature(n, q, k, sigma, M):
    """(e_1..e_sigma) of the banked qcore agreement set T0 u U_A.

    T0 = a sigma-subset of the order-M coset containing 1 (namely the first
    sigma elements of mu_M), U_A = union of k/M other order-M cosets.
    Returns (key_tuple, one explicit agreement set as a tuple of exponents).
    """
    xs = mu(n, q)
    N = n // M
    # cosets of mu_M inside mu_n: exponent classes  {j, j+N, j+2N, ...}
    # (mu_M = {g^(N*i)} since g^N has order M)
    cos = [[(j + N * i) % n for i in range(M)] for j in range(N)]
    T0 = cos[0][:sigma]
    U = [e for j in range(1, 1 + k // M) for e in cos[j]]
    A = sorted(T0 + U)
    assert len(A) == k + sigma
    return elem_sym([xs[i] for i in A], sigma, q), tuple(A)


def elem_sym(vals, sigma, q):
    """(e_1, ..., e_sigma) mod q of the multiset vals."""
    e = [0] * (sigma + 1)
    e[0] = 1
    for x in vals:
        for i in range(min(sigma, len(e) - 1), 0, -1):
            e[i] = (e[i] + x * e[i - 1]) % q
    return tuple(e[1:])

"""low_w_lib.py -- exact machinery for the LOW-w CROSSING CORE (round 18).

Self-contained.  No repo imports, no external deps beyond the stdlib.
Everything is exact integer / finite-field arithmetic; no floats decide
anything.

Conventions (matching es_coprimality/PROOFS.md sec 0 and es_g_lanes
PROOFS.md sec 3.1):

  n = 2^m,  h = n/2,  K = Q(zeta_n),  O_K = Z[zeta_n] = Z[X]/(X^h + 1)
  S <= Z/n,  |S| = r'
  x_s(S) = sum_{i in S} zeta_n^{s i}
  W_w = { S : |S| = r',  x_s(S) = 0 for s = 1..w-1 }
  strat(S) = max{ a >= 0 : S + n/2^a = S }
  structural  <=>  strat(S) >= log2 M,  M = least 2-power >= w
"""

from itertools import combinations
from math import comb, gcd

# --------------------------------------------------------------------------
# char-0 arithmetic in O_K = Z[X]/(X^h + 1)
# --------------------------------------------------------------------------


def cyc_monomial_add(v, e, h, c=1):
    """v += c * X^e  in Z[X]/(X^h+1).  e is reduced mod 2h first."""
    e %= (2 * h)
    if e < h:
        v[e] += c
    else:
        v[e - h] -= c


def power_sum_char0(S, s, n):
    """x_s(S) in Z[X]/(X^{n/2}+1), exact."""
    h = n // 2
    v = [0] * h
    for i in S:
        cyc_monomial_add(v, (s * i) % n, h)
    return v


def cyc_scale(v, c):
    return [c * a for a in v]


def cyc_embed(v_small, a, n_small, n_big):
    """iota : Z[Y]/(Y^{n_small/2}+1) -> Z[X]/(X^{n_big/2}+1),  Y |-> X^{2^a}.

    Requires n_big = n_small * 2^a.
    """
    assert n_big == n_small * (1 << a)
    hb = n_big // 2
    out = [0] * hb
    for e, c in enumerate(v_small):
        if c:
            cyc_monomial_add(out, e * (1 << a), hb, c)
    return out


# --------------------------------------------------------------------------
# finite-field arithmetic:  a primitive n-th root of unity in F_p (delta = 1)
# --------------------------------------------------------------------------


def root_of_unity(p, n):
    """theta in F_p with exact multiplicative order n.  n must be a power of
    two dividing p-1.  Returns the smallest one found from g = 2 upwards."""
    assert n & (n - 1) == 0 and n >= 2, "n must be a power of two >= 2"
    assert (p - 1) % n == 0, "n does not divide p-1"
    e = (p - 1) // n
    g = 2
    while g < p:
        t = pow(g, e, p)
        # n is a power of two, so ord(t) | n; ord(t) = n iff t^{n/2} != 1
        if t != 1 and pow(t, n // 2, p) != 1:
            return t
        g += 1
    raise RuntimeError("no primitive %d-th root of unity mod %d" % (n, p))


def ord_mod(p, m):
    """multiplicative order of p mod m, for m a power of two (so the order is
    a power of two): exact, by repeated squaring on the exponent."""
    assert m & (m - 1) == 0 and m >= 1
    assert gcd(p, m) == 1
    if m == 1:
        return 1
    d = 1
    while d <= m:
        if pow(p, d, m) == 1:
            return d
        d *= 2
    raise RuntimeError("order of %d mod %d is not a power of two" % (p, m))


def power_sum_fp(S, s, n, theta, p):
    """x_s(S) in F_p, by DIRECT summation (no lemma used)."""
    acc = 0
    for i in S:
        acc += pow(theta, (s * i) % n, p)
    return acc % p


# --------------------------------------------------------------------------
# strata
# --------------------------------------------------------------------------


def strat(S, n):
    """max{a >= 0 : S + n/2^a = S}.  S given as a set of residues mod n."""
    Sset = set(x % n for x in S)
    a = 0
    while True:
        step = n >> (a + 1)          # n / 2^{a+1}
        if step == 0:
            return a
        if all(((x + step) % n) in Sset for x in Sset):
            a += 1
        else:
            return a


def lift(Sp, a, n_a, n):
    """S = preimage of S' <= Z/n_a under Z/n -> Z/n_a.  |S| = 2^a |S'|."""
    assert n == n_a * (1 << a)
    return sorted({(j + n_a * t) % n for j in Sp for t in range(1 << a)})


def reduce_set(S, n_a):
    return sorted({i % n_a for i in S})


# --------------------------------------------------------------------------
# the ternary collapse (X2)
# --------------------------------------------------------------------------


def eps_of(Sp, L):
    """eps_j = [j in S'] - [j+L in S'], j = 0..L-1, for S' <= Z/2L."""
    Sset = set(Sp)
    return tuple((1 if j in Sset else 0) - (1 if (j + L) in Sset else 0)
                 for j in range(L))


def fibre_size(eps, r_a, L):
    """#{ S' <= Z/2L : |S'| = r_a, eps(S') = eps }."""
    U = sum(1 for e in eps if e != 0)
    if (r_a - U) % 2 or r_a < U:
        return 0
    return comb(L - U, (r_a - U) // 2)


def fibre_sum_closed(L, r_a):
    """sum over ALL eps in {0,+-1}^L of fibre_size, in closed form:
       sum_U C(L,U) 2^U C(L-U, (r_a-U)/2)."""
    tot = 0
    for U in range(0, min(L, r_a) + 1):
        if (r_a - U) % 2:
            continue
        tot += comb(L, U) * (2 ** U) * comb(L - U, (r_a - U) // 2)
    return tot


def eps_eval_fp(eps, theta, p):
    """sum_j eps_j theta^j in F_p."""
    acc = 0
    for j, e in enumerate(eps):
        if e:
            acc += e * pow(theta, j, p)
    return acc % p


def build_Sprime(eps, r_a, L, zero_pairs_pick=None):
    """Assemble S' <= Z/2L with |S'| = r_a realising the ternary vector eps.

    eps_j = +1 -> j in S', j+L not in S'
    eps_j = -1 -> j+L in S', j not in S'
    eps_j =  0 -> pair j is 'both' or 'neither'; exactly B = (r_a-U)/2 of the
                  zero-pairs are 'both'.
    """
    U = sum(1 for e in eps if e != 0)
    assert (r_a - U) % 2 == 0 and r_a >= U, "eps incompatible with r_a"
    B = (r_a - U) // 2
    zeros = [j for j in range(L) if eps[j] == 0]
    assert B <= len(zeros), "not enough zero-pairs"
    if zero_pairs_pick is None:
        zero_pairs_pick = zeros[:B]
    assert len(zero_pairs_pick) == B and all(eps[j] == 0 for j in zero_pairs_pick)
    Sp = []
    for j in range(L):
        if eps[j] == 1:
            Sp.append(j)
        elif eps[j] == -1:
            Sp.append(j + L)
    for j in zero_pairs_pick:
        Sp.append(j)
        Sp.append(j + L)
    Sp = sorted(Sp)
    assert len(Sp) == r_a
    return Sp


# --------------------------------------------------------------------------
# shape bookkeeping:  the deep stratum of a crossing shape
# --------------------------------------------------------------------------


def deep_shape(n, v):
    """The deepest stratum a = v-1 of the crossing shape (n, w=2^v,
    r' = n/2 - 2^v).  Returns a dict of exact integers."""
    w = 1 << v
    rp = n // 2 - w
    a = v - 1
    n_a = n >> a
    L = n_a // 2
    r_a = rp >> a
    return dict(n=n, v=v, w=w, M=w, rp=rp, a=a, n_a=n_a, L=L, r_a=r_a)

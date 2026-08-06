#!/usr/bin/env python3
"""Round 18 -- E_floor SPARSITY pilot: exact machinery.

All arithmetic is EXACT INTEGER / F_p arithmetic.  Floats appear only in
printed log2 diagnostics, never in a decision path.

OBJECT (unchanged from round 17, es_coprimality/PROOFS.md:12-18):
  n = 2^m, h = n/2 = [K:Q], K = Q(zeta_n), O_K = Z[zeta_n],
  S <= Z/n, x_s = sum_{i in S} zeta^{si}, I_S = (x_1,...,x_{w-1}).

NEW HERE (round 18).  For a FIXED odd prime p we split the banked census
identity (es_lib.py:23-28) prime-by-prime:

    p | N(I_S)  <=>  EXISTS an irreducible factor g of Phi_n over F_p
                     with  f_S(X^s) = 0 mod g  for s = 1..w-1,

where f_S(X) = sum_{i in S} X^i.  Each factor g is one prime P | p of O_K.
For fixed g the condition is F_p-LINEAR in the 0/1 indicator of S, so the
bad set is a constant-weight count in a cyclic code (LEMMA Y, BANKED round
14, mun_anticoncentration/PREREG.md:53-61 -- cited, not claimed).  That
linearity is what makes an EXACT meet-in-the-middle census possible:
n = 32 over ALL 2^32 subsets by weight, n = 64 for r' <= 6.

Independent oracle: cop_lib.ideal_norm (integer Hermite normal form), a
completely different computation, used to falsify this route in stage
`self`.
"""

import os
import sys

sys.dont_write_bytecode = True  # never write __pycache__ outside my dir

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "es_coprimality"))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "es_boundary_adversary"))

import cop_lib  # noqa: E402  (banked round-17 machinery, read-only source)


# --------------------------------------------------------------------------
# polynomials over F_p  (extends cop_lib.pnorm/pgcd with mul/div/powmod)
# --------------------------------------------------------------------------

pnorm = cop_lib.pnorm
pgcd = cop_lib.pgcd


def padd(a, b, p):
    n = max(len(a), len(b))
    r = [0] * n
    for i, c in enumerate(a):
        r[i] = c % p
    for i, c in enumerate(b):
        r[i] = (r[i] + c) % p
    return pnorm(r, p)


def pmul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return pnorm(r, p)


def prem(a, m, p):
    """a mod m in F_p[X]; m must be nonzero."""
    a = pnorm(list(a), p)
    m = pnorm(list(m), p)
    assert m, "division by zero polynomial"
    inv = pow(m[-1], p - 2, p)
    while len(a) >= len(m):
        c = a[-1] * inv % p
        off = len(a) - len(m)
        for i, mc in enumerate(m):
            a[off + i] = (a[off + i] - c * mc) % p
        a = pnorm(a, p)
    return a


def pdivexact(a, m, p):
    """quotient of a by m, assuming m | a."""
    a = pnorm(list(a), p)
    m = pnorm(list(m), p)
    inv = pow(m[-1], p - 2, p)
    q = [0] * max(1, len(a) - len(m) + 1)
    while len(a) >= len(m):
        c = a[-1] * inv % p
        off = len(a) - len(m)
        q[off] = c
        for i, mc in enumerate(m):
            a[off + i] = (a[off + i] - c * mc) % p
        a = pnorm(a, p)
    assert not a, "pdivexact: nonzero remainder"
    return pnorm(q, p)


def ppowmod(a, e, m, p):
    r = [1]
    a = prem(a, m, p)
    while e:
        if e & 1:
            r = prem(pmul(r, a, p), m, p)
        a = prem(pmul(a, a, p), m, p)
        e >>= 1
    return r


def pmonic(a, p):
    a = pnorm(list(a), p)
    if not a:
        return a
    inv = pow(a[-1], p - 2, p)
    return [c * inv % p for c in a]


# --------------------------------------------------------------------------
# splitting Phi_n = X^{n/2} + 1 over F_p into its e = n/(2 delta) primes
# --------------------------------------------------------------------------

def phi_factors(n, p, seed=20260806):
    """The distinct monic irreducible factors of X^{n/2}+1 over F_p.

    p odd, n = 2^m, so X^n - 1 is separable mod p and all factors of Phi_n
    have the same degree delta = ord_n(p): equal-degree (Cantor-Zassenhaus)
    splitting applies.  Each factor <-> one prime P | p of O_K.
    """
    import random
    assert p % 2 == 1 and n & (n - 1) == 0
    d = cop_lib.mult_order(p, n)
    f0 = cop_lib.phi_n_poly(n)          # X^{n/2} + 1
    rng = random.Random(seed + p * 1000003 + n)
    out = []
    stack = [pmonic(f0, p)]
    while stack:
        f = stack.pop()
        if len(f) - 1 == d:
            out.append(f)
            continue
        while True:
            a = pnorm([rng.randrange(p) for _ in range(len(f) - 1)], p)
            if not a:
                continue
            g = pgcd(f, a, p)
            if 1 <= len(g) - 1 < len(f) - 1:
                break
            b = ppowmod(a, (p ** d - 1) // 2, f, p)
            b = padd(b, [p - 1], p)      # b - 1
            if not b:
                continue
            g = pgcd(f, b, p)
            if 1 <= len(g) - 1 < len(f) - 1:
                break
        g = pmonic(g, p)
        stack.append(g)
        stack.append(pmonic(pdivexact(f, g, p), p))
    out.sort()
    assert len(out) == (n // 2) // d, "wrong number of factors"
    return out


def condition_reps(n, w, p):
    """s in {1..w-1}, one per <p>-orbit (f(xi^{ps}) = f(xi^s)^p is free)."""
    seen = set()
    reps = []
    for s in range(1, w):
        if s % n in seen:
            continue
        reps.append(s)
        c = s % n
        while c not in seen:
            seen.add(c)
            c = c * p % n
    return reps


# --------------------------------------------------------------------------
# <p>-cosets in (Z/n)^*  and the SP-COVER threshold
# --------------------------------------------------------------------------

def p_cosets(n, p):
    """The cosets of <p> in (Z/n)^*, as sorted tuples of representatives."""
    units = [s for s in range(1, n, 2)]
    sub = set()
    c = 1
    while c not in sub:
        sub.add(c)
        c = c * p % n
    left = set(units)
    out = []
    while left:
        u = min(left)
        cos = tuple(sorted((u * t) % n for t in sub))
        out.append(cos)
        left -= set(cos)
    return out


def w_cover(n, p):
    """w_cov(p,n) = 1 + max over <p>-cosets of the least element.

    For w >= w_cov, the odd s in [1,w-1] meet every coset (THEOREM
    SP-COVER's hypothesis).  All elements of (Z/n)^* are odd (n = 2^m).
    """
    return 1 + max(min(c) for c in p_cosets(n, p))


# --------------------------------------------------------------------------
# packed F_p vectors:  L digits, b bits each, carry-free add
# --------------------------------------------------------------------------

class Packer(object):
    def __init__(self, p, L):
        assert p >= 2 and L >= 1
        b = 1
        while (1 << (b - 1)) < p:
            b += 1
        self.p, self.L, self.b = p, L, b
        ones = 0
        for i in range(L):
            ones |= 1 << (b * i)
        self.ones = ones
        self.G = ones * ((1 << (b - 1)) - p)

    def reduce(self, v):
        f = ((v + self.G) >> (self.b - 1)) & self.ones
        return v - self.p * f

    def add(self, x, y):
        return self.reduce(x + y)

    def pack(self, digits):
        assert len(digits) == self.L
        v = 0
        for i, d in enumerate(digits):
            v |= (d % self.p) << (self.b * i)
        return v

    def unpack(self, v):
        m = (1 << self.b) - 1
        return [(v >> (self.b * i)) & m for i in range(self.L)]

    def neg(self, v):
        return self.reduce(self.p * self.ones - v)


# --------------------------------------------------------------------------
# the syndrome map:  coordinate i  ->  (X^{s i mod n} mod g)_{s,g}
# --------------------------------------------------------------------------

def syndrome_columns(n, p, w, factors, slist=None):
    """Packed syndrome column for every coordinate i in Z/n.

    S satisfies ALL conditions of ALL listed factors  <=>  sum of its
    columns is 0.  Length L = sum over factors g of deg(g) * #reps.
    """
    reps = condition_reps(n, w, p) if slist is None else list(slist)
    blocks = []
    for g in factors:
        dg = len(g) - 1
        xp = [None] * n
        cur = [1]
        for e in range(n):
            xp[e] = cur + [0] * (dg - len(cur))
            cur = prem([0] + cur, g, p)   # multiply by X, reduce mod g
        blocks.append((dg, xp))
    L = sum(dg * len(reps) for dg, _ in blocks)
    pk = Packer(p, L)
    cols = []
    for i in range(n):
        digits = []
        for dg, xp in blocks:
            for s in reps:
                digits.extend(xp[(s * i) % n])
        cols.append(pk.pack(digits))
    return pk, cols, reps, L


def syndrome_of(S, pk, cols):
    v = 0
    for i in S:
        v = pk.add(v, cols[i])
    return v


def is_bad_for_factor(S, pk, cols):
    return syndrome_of(S, pk, cols) == 0


# --------------------------------------------------------------------------
# EXACT meet-in-the-middle census (knapsack DP over syndromes)
# --------------------------------------------------------------------------

def half_table(cols, idxs, kmax, pk, negate=False):
    """tab[k][syn] = #subsets of `idxs` of size k with that syndrome."""
    tab = [dict() for _ in range(kmax + 1)]
    tab[0][0] = 1
    done = 0
    for i in idxs:
        c = pk.neg(cols[i]) if negate else cols[i]
        done += 1
        top = min(kmax, done) - 1
        for k in range(top, -1, -1):
            src = tab[k]
            if not src:
                continue
            dst = tab[k + 1]
            add = pk.add
            for syn, cnt in src.items():
                s2 = add(syn, c)
                if s2 in dst:
                    dst[s2] += cnt
                else:
                    dst[s2] = cnt
    return tab


def census_by_weight(n, p, w, factors, kmax=None, slist=None):
    """EXACT #{S <= Z/n : |S| = k, all conditions hold} for every k <= kmax.

    Exhaustive over all 2^n subsets when kmax = n (no sampling anywhere).
    """
    if kmax is None:
        kmax = n
    pk, cols, reps, L = syndrome_columns(n, p, w, factors, slist)
    lo = list(range(0, n // 2))
    hi = list(range(n // 2, n))
    tl = half_table(cols, lo, min(kmax, len(lo)), pk, negate=False)
    th = half_table(cols, hi, min(kmax, len(hi)), pk, negate=True)
    out = [0] * (kmax + 1)
    for k2, d2 in enumerate(th):
        for k1, d1 in enumerate(tl):
            if k1 + k2 > kmax:
                break
            if not d1 or not d2:
                continue
            a, b = (d1, d2) if len(d1) <= len(d2) else (d2, d1)
            tot = 0
            for syn, cnt in a.items():
                c2 = b.get(syn)
                if c2:
                    tot += cnt * c2
            out[k1 + k2] += tot
    return out, L, reps


def periodic_census_by_weight(n, p, w, factors, kmax=None, slist=None):
    """Same count restricted to strat(S) >= 1, i.e. S = T u (T + n/2)."""
    if kmax is None:
        kmax = n
    pk, cols, reps, L = syndrome_columns(n, p, w, factors, slist)
    h = n // 2
    pcols = [pk.add(cols[i], cols[i + h]) for i in range(h)]
    tab = half_table(pcols, list(range(h)), min(kmax // 2, h), pk)
    out = [0] * (kmax + 1)
    for k, d in enumerate(tab):
        if 2 * k <= kmax:
            out[2 * k] += d.get(0, 0)
    return out


# --------------------------------------------------------------------------
# adversarial family generators (S2)
# --------------------------------------------------------------------------

def fam_shift(n, rp, j):
    """F1/F2: S = T u (T + n/2^j), disjointly; kills x_s for v_2(s) = j-1."""
    L = n // (2 ** j)
    out = set()
    for T in _subsets_of_size(range(n), rp // 2):
        Ts = set(T)
        Sh = set((t + L) % n for t in T)
        if Ts & Sh:
            continue
        S = tuple(sorted(Ts | Sh))
        if len(S) == rp:
            out.add(S)
    return sorted(out)


def fam_symmetric(n, rp):
    """F3: S = -S."""
    pairs = []
    fixed = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        j = (-i) % n
        seen.add(i)
        seen.add(j)
        if i == j:
            fixed.append(i)
        else:
            pairs.append((i, j))
    out = []
    for nf in range(min(len(fixed), rp) + 1):
        if (rp - nf) % 2:
            continue
        npairs = (rp - nf) // 2
        if npairs > len(pairs):
            continue
        for F in _subsets_of_size(fixed, nf):
            for P in _subsets_of_size(range(len(pairs)), npairs):
                S = list(F)
                for k in P:
                    S.extend(pairs[k])
                out.append(tuple(sorted(S)))
    return sorted(set(out))


def fam_mult_invariant(n, rp, u):
    """F4: uS = S for a fixed odd u."""
    orbs = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        o = set()
        c = i
        while c not in o:
            o.add(c)
            c = c * u % n
        seen |= o
        orbs.append(tuple(sorted(o)))
    out = []

    def rec(k, cur, sz):
        if sz == rp:
            out.append(tuple(sorted(cur)))
            return
        if k == len(orbs) or sz > rp:
            return
        rec(k + 1, cur, sz)
        rec(k + 1, cur + list(orbs[k]), sz + len(orbs[k]))

    rec(0, [], 0)
    return sorted(set(out))


def fam_ap(n, rp, near=0):
    """F5: arithmetic progressions, and APs with `near` elements displaced."""
    base = set()
    for a in range(n):
        for d in range(1, n):
            S = sorted(set((a + j * d) % n for j in range(rp)))
            if len(S) == rp:
                base.add(tuple(S))
    if near == 0:
        return sorted(base)
    out = set()
    for S in base:
        for x in S:
            for y in range(n):
                if y in S:
                    continue
                T = tuple(sorted(set(S) - {x} | {y}))
                out.add(T)
    return sorted(out)


def fam_coset_near(n, rp, M, near=1):
    """F6: unions of mu_M-cosets, symmetric-differenced with `near` points."""
    L = n // M
    cosets = [tuple(sorted((i + j * L) % n for j in range(M)))
              for i in range(L)]
    base = set()
    for k in range(0, L + 1):
        if k * M > rp + near or k * M < rp - near:
            continue
        for C in _subsets_of_size(range(L), k):
            S = set()
            for c in C:
                S |= set(cosets[c])
            base.add(tuple(sorted(S)))
    out = set()
    for S in base:
        Ss = set(S)
        if len(Ss) == rp:
            out.add(tuple(sorted(Ss)))
        if near >= 1:
            for x in list(Ss):
                for y in range(n):
                    if y in Ss:
                        continue
                    T = (Ss - {x}) | {y}
                    if len(T) == rp:
                        out.add(tuple(sorted(T)))
            for y in range(n):
                if y not in Ss and len(Ss) + 1 == rp:
                    out.add(tuple(sorted(Ss | {y})))
            for x in list(Ss):
                if len(Ss) - 1 == rp:
                    out.add(tuple(sorted(Ss - {x})))
    return sorted(out)


def fam_antipodal(n, rp, apairs):
    """F7: exactly `apairs` antipodal pairs (a_{n/2}(S) = 2*apairs)."""
    h = n // 2
    out = []
    for P in _subsets_of_size(range(h), apairs):
        rest = rp - 2 * apairs
        if rest < 0:
            continue
        avail = [i for i in range(h) if i not in P]
        for R in _subsets_of_size(avail, rest):
            for signs in range(1 << rest):
                S = []
                for k in P:
                    S.extend([k, k + h])
                for t, i in enumerate(R):
                    S.append(i + h * ((signs >> t) & 1))
                S = tuple(sorted(S))
                if len(S) == rp and cop_lib.antipodal_pairs(list(S), n) == 2 * apairs:
                    out.append(S)
    return sorted(set(out))


def _subsets_of_size(pool, k):
    import itertools
    return itertools.combinations(list(pool), k)


# --------------------------------------------------------------------------
# oracle helpers (round-17 banked route, used as the independent check)
# --------------------------------------------------------------------------

def odd_norm(S, n, w):
    """(N(I_S), odd part) via the banked exact HNF ideal norm."""
    N = cop_lib.ideal_norm(list(S), n, w)
    if N == 0:
        return 0, 0
    Nod = N
    while Nod % 2 == 0:
        Nod //= 2
    return N, Nod


def strat0(S, n):
    return cop_lib.strat(list(S), n) == 0


def vanishing_conditions(S, n, w):
    """#{s in [1,w-1] : x_s = 0 in char 0} -- the 'killed conditions'."""
    return sum(1 for s in range(1, w)
               if not any(cop_lib.coord_vector(list(S), s, n)))


def odd_reps(n, w, p):
    """odd s in [1,w-1], one per <p>-orbit == one per <p>-coset of (Z/n)^*."""
    seen = set()
    reps = []
    for s in range(1, w, 2):
        if s % n in seen:
            continue
        reps.append(s)
        c = s % n
        while c not in seen:
            seen.add(c)
            c = c * p % n
    return reps

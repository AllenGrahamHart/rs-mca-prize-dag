#!/usr/bin/env python3
"""RESSIEVE core -- round 26, umin_spike_hunt.  Registered in PREREG section U0.

THEOREM RS (registered before implementation):  for N with 2N a 2-power,
p prime with 2N | p-1 and theta of order 2N in F_p^*, the M4/I2-RSET cell
[theta^j]_{j<N} has a ternary kernel vector of weight U  IFF  some ternary
f of degree < N and weight U has  p | Res(Phi_2N, f).

So ONE enumeration over low-weight f decides EVERY prime in the band.
This file is the instrument; it REUSES zcore (round 24) for primes /
elt_of_order and is used together with the round-25 bbm.py / wenum.py.

Run ONLY via  tools/ramguard tiny|local -- python3 ...  from repo root.
Stdlib only.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z24 = os.path.abspath(os.path.join(HERE, "..", "..", "pilots_20260808",
                                   "z_ceiling_assault"))
Z25 = os.path.abspath(os.path.join(HERE, "..", "z_n32_band"))
for _p in (Z25, Z24):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from zcore import primes_upto, is_prime, elt_of_order   # noqa: E402


# ------------------------------------------------------------------ modulus
def find_q(bits, M):
    """least prime q >= 2^bits with M | q-1 (M a 2-power)."""
    q = (1 << bits) + 1
    q += (-(q - 1)) % M
    while not is_prime(q):
        q += M
    return q


def find_w(q, M):
    """element of exact order M in F_q^* (M a 2-power dividing q-1)."""
    e = (q - 1) // M
    a = 2
    while True:
        w = pow(a, e, q)
        if pow(w, M // 2, q) == q - 1:      # order exactly M (M a 2-power)
            return w
        a += 1


def build_roots(N, q, w):
    """W[j] = (w^{jk} mod q)_{k odd, 0<k<2N};  Wn[j] = its negation."""
    M = 2 * N
    ks = [k for k in range(1, M, 2)]
    W, Wn = [], []
    for j in range(N):
        row = tuple(pow(w, (j * k) % M, q) for k in ks)
        W.append(row)
        Wn.append(tuple(q - x for x in row))
    return W, Wn


# ------------------------------------------------------------------ necklaces
def _canon(g, m, U):
    """g is lex-min among its cyclic rotations (only rotations starting at a
    minimal gap can beat it, so only those are tested)."""
    for i in range(1, U):
        if g[i] == m and g[i:] + g[:i] < g:
            return False
    return True


def necklaces(N, U):
    """One support tuple (0 = s0 < s1 < ... < s_{U-1}) per mu_2N shift-orbit.

    Completeness (registered): every orbit has a rotation putting a MINIMAL
    gap first; among those the lex-min gap sequence is unique, so exactly one
    representative per orbit is produced."""
    if U < 1 or U > N:
        return
    if U == 1:
        yield (0,)
        return
    g = [0] * U

    def rec(i, rem, m):
        if i == U - 1:
            if rem >= m:
                g[i] = rem
                if _canon(g, m, U):
                    s, out = 0, [0]
                    for t in range(U - 1):
                        s += g[t]
                        out.append(s)
                    yield tuple(out)
            return
        hi = rem - m * (U - 1 - i)
        for v in range(m, hi + 1):
            g[i] = v
            yield from rec(i + 1, rem - v, m)

    for m in range(1, N // U + 1):
        g[0] = m
        yield from rec(1, N - m, m)


# ------------------------------------------------------------------ primality
_MRB = (2, 3, 5, 7, 11, 13)          # deterministic for n < 3.47e12


def mr(n):
    if n < 2:
        return False
    for b in (2, 3, 5, 7, 11, 13):
        if n % b == 0:
            return n == b
    d, r = n - 1, 0
    while not d & 1:
        d >>= 1
        r += 1
    for a in _MRB:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primorial(B):
    """product of all primes <= B, by product tree (keeps intermediates small)."""
    ps = primes_upto(B)
    while len(ps) > 1:
        nxt = [ps[i] * ps[i + 1] for i in range(0, len(ps) - 1, 2)]
        if len(ps) & 1:
            nxt.append(ps[-1])
        ps = nxt
    return ps[0] if ps else 1


# ------------------------------------------------------------------ the sieve
def sieve_U(N, U, plo, phi, q, W, Wn, shard=0, nshard=1, out=None,
            progress=None, collect=True):
    """EXHAUSTIVE over the band: every prime p in [plo, phi] that carries a
    weight-U ternary kernel orbit is emitted (with the witness f).

    Registered band-extraction proof: Res <= U^{N/2}; strip every prime factor
    <= Bmax = U^{N/2}//plo; a band prime divides Res IFF the remainder R is a
    prime in [plo, phi] (the cofactor is then forced to 1), and at most one
    band prime can occur since plo^2 > U^{N/2}."""
    from math import gcd, isqrt
    cap = U ** (N // 2)
    assert cap < q, "modulus too small to recover Res exactly"
    bmax = cap // plo
    # REGIME A (bmax < plo): stripping every prime <= bmax cannot touch a band
    #   prime, and any band prime's cofactor is <= bmax, so the remainder IS
    #   the band prime.  REGIME B (bmax >= plo): strip only below plo, then the
    #   remainder's factors are all >= plo and there are at most
    #   log_plo(cap) of them -- resolved by trial division up to isqrt.
    regime_b = bmax >= plo
    bstrip = min(bmax, plo - 1)
    PRIM = primorial(bstrip) if bstrip >= 2 else 1
    SMALL = primes_upto(isqrt(cap) + 1) if regime_b else None
    hits = []
    nleaf = 0
    ncand = 0
    ngcd = 0
    nhit = 0
    for idx, S in enumerate(necklaces(N, U)):
        if idx % nshard != shard:
            continue
        cur = [W[0]]
        for j in S[1:]:
            A = W[j]
            B = Wn[j]
            cur = ([[x + y for x, y in zip(v, A)] for v in cur] +
                   [[x + y for x, y in zip(v, B)] for v in cur])
        nleaf += len(cur)
        for t, v in enumerate(cur):
            r = 1
            for x in v:
                r = r * x % q
            if r < plo:
                continue
            ncand += 1
            g = gcd(r, PRIM)
            ngcd += 1
            if g > 1:
                r //= g
                while True:
                    h = gcd(r, g)
                    if h == 1:
                        break
                    r //= h
            if plo <= r <= phi and mr(r):
                found = [r]
            elif regime_b and r > phi:
                found = []
                rr = r
                for sp in SMALL:
                    if sp * sp > rr:
                        break
                    while rr % sp == 0:
                        rr //= sp
                        if plo <= sp <= phi:
                            found.append(sp)
                if rr > 1 and plo <= rr <= phi:
                    found.append(rr)
            else:
                found = []
            for pf in found:
                nhit += 1
                if collect:
                    hits.append((pf, U, S, t))
                if out:
                    out.write("%d\t%d\t%s\t%d\n" %
                              (pf, U, ",".join(map(str, S)), t))
        if progress and (idx % progress == 0):
            print("   U=%d idx=%d leaves=%d cand=%d hits=%d"
                  % (U, idx, nleaf, ncand, nhit), flush=True)
            if out:
                out.flush()
    return hits, nleaf, ncand, nhit


def sieve_U_sq(N, U, plo, phi, q, W, Wn, shard=0, nshard=1, out=None,
               progress=None):
    """kappa=2 (M2, Lambda={1,3}) arm.  A weight-U kernel vector needs TWO of
    the 32 factors f(theta^k) to vanish, so p^2 | Res is NECESSARY; candidates
    are then re-verified exactly by verify_hit(kappa=2).  Same strip proof with
    plo -> plo^2: the remainder must be exactly p^2."""
    from math import gcd, isqrt
    cap = U ** (N // 2)
    assert cap < q
    lo2 = plo * plo
    bmax = cap // lo2
    assert bmax < plo, "strip bound would eat band primes"
    PRIM = primorial(bmax) if bmax >= 2 else 1
    hits, nleaf, nhit = [], 0, 0
    for idx, S in enumerate(necklaces(N, U)):
        if idx % nshard != shard:
            continue
        cur = [W[0]]
        for j in S[1:]:
            A, B = W[j], Wn[j]
            cur = ([[x + y for x, y in zip(v, A)] for v in cur] +
                   [[x + y for x, y in zip(v, B)] for v in cur])
        nleaf += len(cur)
        for t, v in enumerate(cur):
            r = 1
            for x in v:
                r = r * x % q
            if r < lo2:
                continue
            g = gcd(r, PRIM)
            if g > 1:
                r //= g
                while True:
                    h = gcd(r, g)
                    if h == 1:
                        break
                    r //= h
            if r < lo2:
                continue
            s = isqrt(r)
            if s * s == r and plo <= s <= phi and mr(s):
                nhit += 1
                hits.append((s, U, S, t))
                if out:
                    out.write("%d\t%d\t%s\t%d\n"
                              % (s, U, ",".join(map(str, S)), t))
        if progress and idx % progress == 0:
            print("   sq U=%d idx=%d leaves=%d hits=%d" % (U, idx, nleaf, nhit),
                  flush=True)
    return hits, nleaf, nhit


def sieve_targets(N, U, targets, q, W, Wn, shard=0, nshard=1, out=None,
                  progress=None):
    """Targeted arm: same exhaustive enumeration over weight-U ternary f, but
    only asks 'does Res hit one of THESE primes?'.  No primorial, no primality
    test -- one gcd against the product of the targets.  Used for the brief's
    power control (fire on the known UMIN=9 cells, stay silent on the UMIN=11
    cells) at weights the full census does not reach."""
    from math import gcd
    T = 1
    for p in targets:
        T *= p
    assert U ** (N // 2) < q
    found, nleaf = [], 0
    for idx, S in enumerate(necklaces(N, U)):
        if idx % nshard != shard:
            continue
        cur = [W[0]]
        for j in S[1:]:
            A, B = W[j], Wn[j]
            cur = ([[x + y for x, y in zip(v, A)] for v in cur] +
                   [[x + y for x, y in zip(v, B)] for v in cur])
        nleaf += len(cur)
        for t, v in enumerate(cur):
            r = 1
            for x in v:
                r = r * x % q
            if gcd(r, T) > 1:
                for p in targets:
                    if r % p == 0:
                        found.append((p, U, S, t))
                        if out:
                            out.write("%d\t%d\t%s\t%d\n"
                                      % (p, U, ",".join(map(str, S)), t))
        if progress and idx % progress == 0:
            print("   tgt U=%d idx=%d leaves=%d found=%d"
                  % (U, idx, nleaf, len(found)), flush=True)
    return found, nleaf


# ------------------------------------------------------------------ witness
def unpack(S, t):
    """(support, leaf index) -> the ternary coefficient list eps[0..?]."""
    U = len(S)
    eps = {S[0]: 1}
    for i in range(1, U):
        eps[S[i]] = -1 if (t >> (i - 1)) & 1 else 1
    return eps


def verify_hit(N, p, S, t, kappa=1, lam=None):
    """Independent arithmetic re-verification of a sieve hit AT p.

    Recomputes theta = elt_of_order(p, 2N) from scratch and finds the odd k
    with f(theta^k) = 0 mod p (THEOREM RS's Galois twist).  Returns the twisted
    support/signs, i.e. an actual kernel vector of the cell as built by
    rows_M4 / rows_M2, or None."""
    M = 2 * N
    if (p - 1) % M:
        return None
    eps = unpack(S, t)
    th = elt_of_order(p, M)
    if lam is None:
        lam = [2 * j - 1 for j in range(1, kappa + 1)]
    for k in range(1, M, 2):
        ok = True
        for l in lam:
            s = 0
            for j, e in eps.items():
                s += e * pow(th, (j * k * l) % M, p)
            if s % p:
                ok = False
                break
        if ok:
            # twist to a genuine kernel vector g(x) = f(x^k) mod x^N+1
            g = {}
            for j, e in eps.items():
                jj = j * k
                sg = -e if (jj // N) & 1 else e
                g[jj % N] = sg
            return k, g
    return None


# ------------------------------------------------------------------ orbits
def expand_orbit(N, eps):
    """full mu_2N negacyclic orbit of a ternary vector, as a set of tuples.
    The generator is v -> (-v[N-1], v[0], ..., v[N-2]); it has order 2N and
    shift^N = -identity, so the global sign is INSIDE the group."""
    v = list(eps)
    out = set()
    for _ in range(2 * N):
        v = [-v[N - 1]] + v[:N - 1]
        out.add(tuple(v))
    return out


def au_from_reps(N, reps):
    """exact AU[U] (VECTOR counts) from a list of (U, eps-dict) reps."""
    seen = {}
    for U, eps in reps:
        vec = [0] * N
        for j, e in eps.items():
            vec[j] = e
        seen.setdefault(U, set()).update(expand_orbit(N, vec))
    return {U: len(s) for U, s in seen.items()}


# ------------------------------------------------------------------ targeted
def direct_AU(N, p, umax, kappa=1, lam=None, shard=0, nshard=1):
    """Second, INDEPENDENT algorithm for AU[U], U <= umax, at ONE prime:
    enumerate the same mu_2N necklace representatives but evaluate the row(s)
    at theta directly mod p.  No resultants, no modulus q, no primorial --
    it shares no arithmetic with sieve_U beyond the necklace generator.
    Returns AU (orbit-count * 64 convention is NOT applied: raw orbit counts)."""
    M = 2 * N
    th = elt_of_order(p, M)
    if lam is None:
        lam = [2 * j - 1 for j in range(1, kappa + 1)]
    rows = [[pow(th, (l * j) % M, p) for j in range(N)] for l in lam]
    orb = [0] * (umax + 1)
    for U in range(1, umax + 1):
        for idx, S in enumerate(necklaces(N, U)):
            if idx % nshard != shard:
                continue
            cur = [[0] * len(lam)]
            for i, j in enumerate(S):
                col = [rows[a][j] for a in range(len(lam))]
                if i == 0:
                    cur = [[c % p for c in col]]
                    continue
                nxt = []
                for v in cur:
                    nxt.append([(v[a] + col[a]) % p for a in range(len(lam))])
                    nxt.append([(v[a] - col[a]) % p for a in range(len(lam))])
                cur = nxt
            for v in cur:
                if not any(v):
                    orb[U] += 1
    return orb

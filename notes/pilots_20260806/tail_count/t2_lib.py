#!/usr/bin/env python3
"""Round 20 -- LEAD 2: the p=7, w=4 CREATION mechanism.  Self-contained.

The cell (tern_small_scale_laws/PROOFS.md:327 and ssl_lib.py:10):

    I3(n,p,w) = CT(n/2, p, <p>-closure of {odd s in [1,w-1]}),
    CT(N,p,T) = { v in {0,+-1}^N : sum_{i<N} v_i omega^{s i} = 0, s in T },
    omega a primitive 2N-th root of unity in characteristic p.

Everything here is built from scratch (own field construction, own census)
so that reproducing the banked 288 / {7,14} is an INDEPENDENT replication.
"""

import sys

sys.dont_write_bytecode = True


# --------------------------------------------------------------------------
# F_p[X] arithmetic and F_{p^k} = F_p[X]/(f)
# --------------------------------------------------------------------------

def pnorm(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return pnorm(out, p)


def pmod(a, f, p):
    a = list(a)
    df = len(f) - 1
    inv = pow(f[-1], p - 2, p)
    while len(a) - 1 >= df and any(a):
        d = len(a) - 1 - df
        c = a[-1] * inv % p
        if c:
            for i, y in enumerate(f):
                a[i + d] = (a[i + d] - c * y) % p
        a.pop()
        a = pnorm(a, p)
        if len(a) - 1 < df:
            break
    return pnorm(a, p)


def pgcd(a, b, p):
    a, b = pnorm(a, p), pnorm(b, p)
    while any(b):
        a, b = b, pmod(a, b, p)
    if any(a):
        inv = pow(a[-1], p - 2, p)
        a = [x * inv % p for x in a]
    return a


def ppowmod(a, e, f, p):
    r, base = [1], pmod(a, f, p)
    while e:
        if e & 1:
            r = pmod(pmul(r, base, p), f, p)
        base = pmod(pmul(base, base, p), f, p)
        e >>= 1
    return r


def find_irreducible(k, p):
    """Least monic irreducible of degree k over F_p (lexicographic search)."""
    from itertools import product
    for coeffs in product(range(p), repeat=k):
        f = list(coeffs) + [1]
        if not any(f[:k]):
            continue
        # irreducible iff X^{p^k} = X mod f and gcd(X^{p^d}-X, f)=1 for d|k, d<k
        ok = ppowmod([0, 1], p ** k, f, p) == [0, 1]
        if not ok:
            continue
        for d in range(1, k):
            if k % d:
                continue
            g = ppowmod([0, 1], p ** d, f, p)
            g = pnorm([(g[i] if i < len(g) else 0) - (1 if i == 1 else 0)
                       for i in range(max(len(g), 2))], p)
            if len(pgcd(g, f, p)) > 1:
                ok = False
                break
        if ok:
            return f
    raise AssertionError("no irreducible of degree %d over F_%d" % (k, p))


class GF(object):
    """F_{p^k} = F_p[X]/(f), elements are coefficient tuples of length k."""

    def __init__(self, p, k):
        self.p, self.k = p, k
        self.f = [0, 1] if k == 1 else find_irreducible(k, p)
        self.one = tuple([1] + [0] * (k - 1))
        self.zero = tuple([0] * k)

    def fix(self, a):
        a = pnorm(list(a), self.p)
        return tuple((a + [0] * self.k)[:self.k])

    def mul(self, a, b):
        return self.fix(pmod(pmul(list(a), list(b), self.p), self.f, self.p))

    def pw(self, a, e):
        r, b = self.one, a
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def order(self, a):
        n, o = self.p ** self.k - 1, 1
        x = a
        while x != self.one:
            x = self.mul(x, a)
            o += 1
            if o > n:
                raise AssertionError("not invertible")
        return o


def primitive_root_of_unity(p, M):
    """(gf, omega) with omega of exact order M in F_{p^k}, k = ord_M(p)."""
    k, t = 1, p % M
    while t != 1:
        t = t * p % M
        k += 1
    gf = GF(p, k)
    n = p ** k - 1
    assert n % M == 0
    for cand in range(2, min(n + 1, 20000)):
        a = gf.fix([cand % p] + [(cand // p ** j) % p for j in range(1, k)])
        if a == gf.zero:
            continue
        x = gf.pw(a, n // M)
        if x != gf.one and gf.order(x) == M:
            return gf, x
    raise AssertionError("no primitive %d-th root in F_{%d^%d}" % (M, p, k))


# --------------------------------------------------------------------------
# the census
# --------------------------------------------------------------------------

def p_closure(T, M, p):
    out = set()
    for s in T:
        c = s % M
        while c not in out:
            out.add(c)
            c = c * p % M
    return out


def condition_columns(N, p, T, gf, omega):
    """cols[i] = F_p-coordinate vector of (omega^{s i})_{s in sorted T}."""
    M = 2 * N
    pw = [gf.pw(omega, s) for s in range(M)]
    cols = []
    for i in range(N):
        v = []
        for s in sorted(T):
            v.extend(pw[(s * i) % M])
        cols.append(tuple(x % p for x in v))
    return cols


def census(N, p, cols, want_vectors=False, cap=4000000):
    """EXACT ternary census over 3^N (meet in the middle).  Fail-closed."""
    dim = len(cols[0])
    lo, hi = list(range(N // 2)), list(range(N // 2, N))

    def half(idxs):
        cur = {(0,) * dim: ([((), 0)] if want_vectors else {0: 1})}
        for i in idxs:
            c = cols[i]
            cm = tuple((-x) % p for x in c)
            nd = {}
            for syn, payload in cur.items():
                for delta, val in ((None, 0), (c, 1), (cm, -1)):
                    s2 = syn if delta is None else tuple(
                        (a + b) % p for a, b in zip(syn, delta))
                    if want_vectors:
                        lst = nd.setdefault(s2, [])
                        for vec, w in payload:
                            lst.append((vec + (val,), w + (1 if val else 0)))
                    else:
                        dd = nd.setdefault(s2, {})
                        for w, cnt in payload.items():
                            ww = w + (1 if val else 0)
                            dd[ww] = dd.get(ww, 0) + cnt
            cur = nd
        return cur

    A, B = half(lo), half(hi)
    W = {}
    vecs = []
    for syn, pa in A.items():
        nsyn = tuple((-x) % p for x in syn)
        pb = B.get(nsyn)
        if not pb:
            continue
        if want_vectors:
            if len(vecs) + len(pa) * len(pb) > cap:
                raise MemoryError("kernel exceeds cap")
            for va, wa in pa:
                for vb, wb in pb:
                    v = va + vb
                    if any(v):
                        vecs.append(v)
                        W[wa + wb] = W.get(wa + wb, 0) + 1
        else:
            for wa, ca in pa.items():
                for wb, cb in pb.items():
                    if wa + wb:
                        W[wa + wb] = W.get(wa + wb, 0) + ca * cb
    return W, vecs


def rot_neg(v):
    return (-v[-1],) + v[:-1]


def orbits(vecs, gens):
    S = set(vecs)
    seen, out = set(), []
    for v in S:
        if v in seen:
            continue
        orb, stack = {v}, [v]
        while stack:
            x = stack.pop()
            for g in gens:
                y = g(x)
                if y not in S:
                    return None          # not closed under the group
                if y not in orb:
                    orb.add(y)
                    stack.append(y)
        seen |= orb
        out.append(sorted(orb))
    return out

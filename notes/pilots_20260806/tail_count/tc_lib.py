#!/usr/bin/env python3
"""Round 20 -- THE TAIL-COUNT CRITERION: self-contained core.

Objects (notation of notes/pilots_20260806/tern_route_b/PROOFS.md:47-61):

    p prime, e_p = v_2(p-1), S = 2^{e_p-1}, zeta of exact order 2S in F_p^*,
    Y = {zeta^s : s < S} (half-system), H = Y u (-Y), |H| = 2S,
    Lambda = {1,3,...,2R-1}   (the official window: 0 NEVER occurs),
    f_u(X) = sum_{r<R} u_r X^{2r+1},  c_s(u) = f_u(zeta^s) in F_p,
    P(u) = prod_{s<S} (1 + cos(2 pi c_s(u) / p)),
    n_c(u) = #{s : c_s(u) = c}.

NEW here:
    d(c)    = -2 log2|cos(pi c / p)| >= 0        (local cost; d(0) = 0)
    cost(u) = sum_s d(c_s(u))
    C*      = {(f_u(zeta^s))_s : u} <= F_p^S     (the value code; MDS)

Nothing outside this directory is imported or written.  Exact integer /
rational arithmetic wherever a decision is made; floats only where an
archimedean magnitude is genuinely being measured (and then with a stated
tolerance).
"""

import math
import sys

sys.dont_write_bytecode = True


# ---------------------------------------------------------------------------
# field / row setup
# ---------------------------------------------------------------------------

def v2(x):
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def root_of_order(p, m):
    """An element of F_p^* of EXACT order m (m | p-1).  Fail-closed."""
    assert (p - 1) % m == 0, "m does not divide p-1"
    for g in range(2, p):
        t = pow(g, (p - 1) // m, p)
        if t == 1:
            continue
        ok = True
        for q in prime_divisors(m):
            if pow(t, m // q, p) == 1:
                ok = False
                break
        if ok:
            return t
    raise AssertionError("no element of order %d in F_%d" % (m, p))


def prime_divisors(x):
    out, d = set(), 2
    while d * d <= x:
        while x % d == 0:
            out.add(d)
            x //= d
        d += 1
    if x > 1:
        out.add(x)
    return sorted(out)


class Row(object):
    """One toy row (p, S, R).  S is FORCED by p: S = 2^{v_2(p-1)-1}."""

    def __init__(self, p, R, saturated=None):
        assert is_prime(p) and p % 2 == 1
        self.p = p
        self.ep = v2(p - 1)
        self.S = 1 << (self.ep - 1)
        self.R = R
        self.zeta = root_of_order(p, 2 * self.S)
        assert pow(self.zeta, self.S, p) == p - 1, "zeta^S != -1"
        self.Lam = [2 * r + 1 for r in range(R)]
        assert 0 not in self.Lam, "shift-0 cell (CATCH-19B integer layer)"
        self.L = math.log2(p)
        self.Rsat = max(1, round(self.S / self.L))
        self.saturated = (R == self.Rsat) if saturated is None else saturated
        # M[s][r] = (zeta^s)^{2r+1}
        self.M = [[pow(pow(self.zeta, s, p), l, p) for l in self.Lam]
                  for s in range(self.S)]
        self.Delta = R * self.L - self.S      # the row's saturation constant

    def tag(self):
        return "p=%d S=%d R=%d%s" % (self.p, self.S, self.R,
                                     "" if self.saturated else " [off-sat]")

    def values(self, u):
        """(c_s(u))_{s<S} in F_p^S -- the codeword of C* attached to u."""
        p = self.p
        return [sum(uu * m for uu, m in zip(u, self.M[s])) % p
                for s in range(self.S)]


# ---------------------------------------------------------------------------
# the local weight and the cost function
# ---------------------------------------------------------------------------

def cos_table(p):
    """cos(2 pi c / p) for c in F_p."""
    return [math.cos(2.0 * math.pi * c / p) for c in range(p)]


def log2_local_table(p):
    """log2(1 + cos(2 pi c / p)) for c in F_p (-inf only if p even)."""
    out = []
    for c in range(p):
        v = 1.0 + math.cos(2.0 * math.pi * c / p)
        out.append(math.log2(v) if v > 0 else float("-inf"))
    return out


def cost_table(p):
    """d(c) = -2 log2|cos(pi c / p)|  >= 0,  d(0) = 0."""
    return [-2.0 * math.log2(abs(math.cos(math.pi * c / p))) for c in range(p)]


def enumerate_tuples(p, R):
    """All u in F_p^R, lexicographic."""
    if R == 1:
        for a in range(p):
            yield (a,)
        return
    idx = [0] * R
    while True:
        yield tuple(idx)
        i = R - 1
        while i >= 0:
            idx[i] += 1
            if idx[i] < p:
                break
            idx[i] = 0
            i -= 1
        if i < 0:
            return


# ---------------------------------------------------------------------------
# exact ternary census (independent control on Z_1)
# ---------------------------------------------------------------------------

def ternary_mass_exact(row):
    """Z_1 = sum_{eps in {0,+-1}^S, A eps = 0} 2^{-wt(eps)} as an exact
    Fraction-free pair (numerator, 2^S): meet-in-the-middle over syndromes.

    A[r][s] = (zeta^s)^{2r+1}; the eps = 0 term is included.
    """
    p, S, R = row.p, row.S, row.R
    cols = [tuple(row.M[s][r] for r in range(R)) for s in range(S)]

    def half(idxs):
        tab = {(0,) * R: [1]}          # syndrome -> counts by weight
        for i in idxs:
            c = cols[i]
            cm = tuple((-x) % p for x in c)
            nd = {}
            for syn, wd in tab.items():
                for delta, extra in ((None, 0), (c, 1), (cm, 1)):
                    s2 = syn if delta is None else tuple(
                        (a + b) % p for a, b in zip(syn, delta))
                    cur = nd.get(s2)
                    if cur is None:
                        cur = [0] * (len(wd) + 1)
                        nd[s2] = cur
                    elif len(cur) < len(wd) + 1:
                        cur.extend([0] * (len(wd) + 1 - len(cur)))
                    for w, cnt in enumerate(wd):
                        if cnt:
                            cur[w + extra] += cnt
            tab = nd
        return tab

    A = half(list(range(0, S // 2)))
    B = half(list(range(S // 2, S)))
    W = [0] * (S + 1)
    for syn, wa in A.items():
        nsyn = tuple((-x) % p for x in syn)
        wb = B.get(nsyn)
        if not wb:
            continue
        for i, ca in enumerate(wa):
            if not ca:
                continue
            for j, cb in enumerate(wb):
                if cb:
                    W[i + j] += ca * cb
    num = sum(W[w] * (1 << (S - w)) for w in range(S + 1))
    return num, (1 << S), W          # Z_1 = num / 2^S

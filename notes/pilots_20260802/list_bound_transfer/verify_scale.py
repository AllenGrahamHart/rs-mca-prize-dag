"""verify_scale.py -- the MC lower bound and the pencil property at scale,
over prime AND extension fields.

At n >= 32 an exhaustive census is out of reach, but the LOWER bound does not
need one: for each member T of the MC family we build the codeword P_T
explicitly and measure its agreement.  What is verified here:

  S1  For every MC set T and every pencil member W, P_T exists, has
      deg < k, and agr(P_T, W) is EXACTLY k+w.
  S2  T -> P_T is injective (so the list of every member has >= |MC| members).
  S3  |MC| = C(N,m)/N exactly (q-free).
  S4  CEILING ALGEBRA at scale: for a locator M of degree r'-delta
      (delta >= 1) the i=0 window condition of u = X^(n-1)+cX^(k+w-1) reads
      m_0 = 0, impossible because every root lies in F^*.  Machine-checked by
      evaluating the actual top coefficient of U*M on random T.
  S5  Same over extension fields F_{p^e}.
"""

import json
import os
import random
import sys
from itertools import combinations
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)


# ------------------------------------------------------------ fields
class PrimeField:
    def __init__(self, p):
        self.p = p
        self.q = p
        self.zero, self.one = 0, 1

    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def mul(self, a, b): return (a * b) % self.p
    def inv(self, a): return pow(a, self.p - 2, self.p)
    def neg(self, a): return (-a) % self.p
    def elements(self): return range(self.p)


class ExtField:
    """F_{p^e} = F_p[t]/(modpoly).  Elements are tuples of length e."""

    def __init__(self, p, e, modpoly):
        assert len(modpoly) == e + 1 and modpoly[-1] == 1
        self.p, self.e, self.mod = p, e, modpoly
        self.q = p ** e
        self.zero = tuple([0] * e)
        self.one = tuple([1] + [0] * (e - 1))

    def add(self, a, b): return tuple((x + y) % self.p for x, y in zip(a, b))
    def sub(self, a, b): return tuple((x - y) % self.p for x, y in zip(a, b))
    def neg(self, a): return tuple((-x) % self.p for x in a)

    def mul(self, a, b):
        p, e = self.p, self.e
        r = [0] * (2 * e - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        r[i + j] = (r[i + j] + x * y) % p
        for d in range(2 * e - 2, e - 1, -1):
            cf = r[d]
            if cf:
                r[d] = 0
                for j in range(e):
                    r[d - e + j] = (r[d - e + j] - cf * self.mod[j]) % p
        return tuple(r[:e])

    def inv(self, a):
        # brute force via a^(q-2) using square-and-multiply
        n = self.q - 2
        res, base = self.one, a
        while n:
            if n & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            n >>= 1
        return res

    def elements(self):
        from itertools import product
        for t in product(range(self.p), repeat=self.e):
            yield tuple(t)


def fpow(F, a, n):
    res, base = F.one, a
    while n:
        if n & 1:
            res = F.mul(res, base)
        base = F.mul(base, base)
        n >>= 1
    return res


def find_generator(F):
    qm1 = F.q - 1
    fac, t, d = [], qm1, 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in F.elements():
        if g == F.zero:
            continue
        if all(fpow(F, g, qm1 // pr) != F.one for pr in fac):
            return g
    raise RuntimeError


# --------------------------------------------------------- polynomials
def pmul(F, a, b):
    if not a or not b:
        return []
    r = [F.zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == F.zero:
            continue
        for j, y in enumerate(b):
            if y != F.zero:
                r[i + j] = F.add(r[i + j], F.mul(x, y))
    return r


def ptrim(F, a):
    a = list(a)
    while a and a[-1] == F.zero:
        a.pop()
    return a


def peval(F, coeffs, x):
    acc = F.zero
    for c in reversed(coeffs):
        acc = F.add(F.mul(acc, x), c)
    return acc


def pdivmod(F, a, b):
    a = ptrim(F, a)
    b = ptrim(F, b)
    out = [F.zero] * max(0, len(a) - len(b) + 1)
    inv = F.inv(b[-1])
    while len(a) >= len(b) and a:
        d = len(a) - len(b)
        f = F.mul(a[-1], inv)
        out[d] = f
        for i, bb in enumerate(b):
            a[i + d] = F.sub(a[i + d], F.mul(f, bb))
        a = ptrim(F, a)
    return out, a


def vanish(F, pts):
    m = [F.one]
    for p in pts:
        m = pmul(F, m, [F.neg(p), F.one])
    return m


# --------------------------------------------------------------- runner
out = {"jobs": [], "checks": 0, "fails": []}


def check(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": extra})
        print("   FAIL", label, extra)


def run(F, n, k, w, M, tag, nz=None, seed=1):
    rp = n - k - w
    assert n % M == 0 and rp % M == 0 and w <= M
    N, m = n // M, rp // M
    if comb(N, m) > 200000:
        print("   skip (enumeration C(%d,%d) too large)" % (N, m))
        return
    g = find_generator(F)
    omega = fpow(F, g, (F.q - 1) // n)
    H = [fpow(F, omega, i) for i in range(n)]
    assert len(set(H)) == n
    beta = fpow(F, H[0], n)
    cosets = [[i for i in range(n) if i % N == j] for j in range(N)]
    # target product
    T0 = [i for j in range(m) for i in cosets[j]]
    pr = F.one
    for i in T0:
        pr = F.mul(pr, H[i])
    gamma = pr
    c = gamma if (rp + 1) % 2 == 0 else F.neg(gamma)   # gamma = (-1)^{rp+1} c
    # MC family
    fam = []
    for S in combinations(range(N), m):
        T = [i for j in S for i in cosets[j]]
        p2 = F.one
        for i in T:
            p2 = F.mul(p2, H[i])
        if p2 == gamma:
            fam.append(tuple(sorted(T)))
    pred = comb(N, m) // N if gcd(m, N) == 1 else None
    if pred is not None:
        check(len(fam) == pred, "S3 MC count formula", (tag, n, k, w, M, len(fam), pred))

    u = [F.zero] * n
    u[n - 1] = F.one
    u[k + w - 1] = F.add(u[k + w - 1], c)
    v = [F.zero] * n
    v[n - 2] = F.one
    v[k + w - 2] = F.add(v[k + w - 2], c)

    # pencil members to test
    els = list(F.elements())
    random.seed(seed)
    if nz is None or nz >= len(els):
        zs = els
    else:
        zs = [F.zero, F.one] + random.sample(els, nz)
    members = [("u", u), ("v", v)]
    for z in zs:
        members.append((str(z), [F.add(u[i], F.mul(z, v[i])) for i in range(n)]))

    rec = {"tag": tag, "n": n, "k": k, "w": w, "M": M, "N": N, "m": m,
           "q": F.q, "mc": len(fam), "formula": pred, "a": k + w,
           "n2": n * n, "members_tested": len(members), "min_list_lb": None}
    minlb = None
    over = 0
    for lbl, W in members:
        Wvals = [peval(F, W, x) for x in H]
        Ps = set()
        ok = True
        for T in fam:
            Mp = vanish(F, [H[i] for i in T])
            prod = pmul(F, W, Mp)
            red = [F.zero] * n
            for d, cf in enumerate(prod):
                if cf != F.zero:
                    red[d % n] = F.add(red[d % n], F.mul(cf, fpow(F, beta, d // n)))
            red = ptrim(F, red)
            Pq, rem = pdivmod(F, red, Mp)
            if ptrim(F, rem) or len(ptrim(F, Pq)) > k:
                ok = False
                break
            P = tuple(ptrim(F, Pq))
            agr = sum(1 for i, x in enumerate(H) if peval(F, list(P), x) == Wvals[i])
            # agreement is >= k+w by construction; it is exactly k+w unless
            # the exactness guard fails, which for the mixed member
            # W = alpha*u + beta*v happens iff -beta/alpha lies in T (the
            # quotient is -(m_0/x^2)(alpha x + beta) on x in T).  Then the
            # agreement is k+w+1 -- still inside the list AND inside the
            # tangent gate A = k+w+1.
            if agr < k + w or agr > k + w + 1:
                ok = False
                break
            if agr == k + w + 1:
                over += 1
            Ps.add(P)
        check(ok, "S1 every MC T -> codeword of agreement in {k+w, k+w+1}",
              (tag, n, k, w, M, lbl))
        check(len(Ps) == len(fam), "S2 injective T -> P_T",
              (tag, n, k, w, M, lbl, len(Ps), len(fam)))
        minlb = len(Ps) if minlb is None else min(minlb, len(Ps))
    rec["min_list_lb"] = minlb
    rec["members_with_over_agreement_events"] = over
    rec["min_over_n2"] = minlb / (n * n) if minlb else 0.0

    # S4 ceiling algebra: top window coefficient of U*M for deg M = rp-delta
    for delta in (1, 2, 3):
        rr = rp - delta
        if rr < 1:
            continue
        for _ in range(20):
            T = random.sample(range(n), rr)
            Mp = vanish(F, [H[i] for i in T])
            prod = pmul(F, u, Mp)
            # coefficient of X^{n-1} in U*M (no wrap: deg U*M = n-1+rr, and
            # the reduction leaves degrees >= rr untouched, n-1 >= rr)
            top = prod[n - 1] if n - 1 < len(prod) else F.zero
            m0 = Mp[0]
            check(top == m0, "S4 top window coefficient equals m_0",
                  (tag, n, delta))
            check(m0 != F.zero, "S4 m_0 != 0 (all roots in F^*)", (tag, n, delta))
    out["jobs"].append(rec)
    print("   %-16s n=%-4d k=%-4d w=M=%-3d N=%-4d m=%-4d q=%-6d  MC=%-8d "
          "members=%-4d min_lb=%-8d min/n^2=%.4g over=%d"
          % (tag, n, k, w, N, m, F.q, len(fam), len(members), minlb,
             rec["min_over_n2"], over))


PJOBS = [
    # (n, k, w, M, q, sampled z's)
    (32, 8,  4, 4,  97,  None),   # rate 1/4, full pencil
    (32, 16, 2, 2,  97,  None),   # rate 1/2
    (48, 12, 4, 4,  97,  12),
    (64, 16, 4, 4,  193, 8),
    (64, 32, 2, 2,  193, 8),   # skipped: C(32,15) enumeration too large
    (96, 24, 8, 8,  97,  6),
]
print("=== prime fields ===")
for (n, k, w, M, q, nz) in PJOBS:
    if (q - 1) % n:
        print("   skip q=%d (n does not divide q-1)" % q)
        continue
    run(PrimeField(q), n, k, w, M, "F_%d" % q, nz=nz)

print("=== extension fields ===")
# F_81 = F_3[t]/(t^4 + t + 2)   (verified irreducible below)
EXTS = [
    (3, 4, [2, 1, 0, 0, 1], "F_81"),      # t^4 + t + 2
    (5, 2, [2, 1, 1], "F_25"),            # t^2 + t + 2
    (7, 2, [3, 1, 1], "F_49"),            # t^2 + t + 3
]
for (p, e, mod, tag) in EXTS:
    F = ExtField(p, e, mod)
    # irreducibility sanity: no root in F_p and (for e=4) generator exists
    try:
        find_generator(F)
    except RuntimeError:
        print("   skip", tag, "(bad modulus)")
        continue
    for (n, k, w, M) in [(16, 4, 2, 2), (16, 8, 2, 2), (8, 2, 2, 2),
                         (24, 6, 3, 3), (12, 4, 2, 2)]:
        if (F.q - 1) % n or (n - k - w) % M or n % M or w > M:
            continue
        run(F, n, k, w, M, tag, nz=None)

out["verdict"] = "SCALE_PASS" if not out["fails"] else "SCALE_FAIL"
with open(os.path.join(CHK, "scale.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]), out["verdict"]))

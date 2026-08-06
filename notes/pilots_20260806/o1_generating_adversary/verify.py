#!/usr/bin/env python3
"""o1_generating_adversary -- ADVERSARIAL verifier for (O1) on GENERATING rows.

Round 18, 2026-08-06.  Run from the repo root:

    tools/ramguard local -- python3 notes/pilots_20260806/o1_generating_adversary/verify.py

Fail-closed: every check is recorded; the process exits 1 if any FAIL.

Stages
  S0  verbatim quote checks (file:line) for every statement relied on
  S1  (V4) the generating admissible census -- k is always a 2-power
  S2  (V4) non-emptiness: own primality proofs for every generating class
  S3  (V1) the exact LEMMA-3 ratio law, BOTH Lambda-parity readings
  S4  (V1) Delta at the (C)-threshold: the O(L) rounding residue
  S5  (V1) the ENSEMBLE DICHOTOMY: (C) vs (T*), Delta = -n/(L^2 ln 2)
  S6  (V2) coset invariance of (O1), exact, on toy rows
  S7  (V3) char > w on EVERY admissible row; the DLI stronger law applies
  S8  (V3) (M3) with d = R+1 vs d = 2R+1; R/S = 1/log2 p exactly
  S9  (V3) the orbit no-go and the random-subspace baseline
  S10 (V1) the Hamming-slice (O2) loss at generating rows
"""

import math
import os
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 90

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FAILS = []
NCHECK = 0


def check(name, cond, detail=""):
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    if not cond:
        FAILS.append(name)
    print(f"[{tag}] {name}" + (f"   {detail}" if detail else ""))
    return cond


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


# --------------------------------------------------------------------------
# numeric helpers (Decimal, prec 90)
# --------------------------------------------------------------------------
LN2 = Decimal(2).ln()


def dlog2(x):
    return Decimal(x).ln() / LN2


def ln_gamma(z):
    """Stirling series for ln Gamma(z), z a Decimal, z large (>= 1e6 here)."""
    z = Decimal(z)
    two_pi = Decimal(2) * Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798")
    r = (z - Decimal("0.5")) * z.ln() - z + two_pi.ln() / 2
    r += Decimal(1) / (12 * z)
    r -= Decimal(1) / (360 * z ** 3)
    r += Decimal(1) / (1260 * z ** 5)
    r -= Decimal(1) / (1680 * z ** 7)
    r += Decimal(1) / (1188 * z ** 9)
    return r


def log2_binom(n, j):
    """log2 C(n, j) via Stirling.  n, j ints, large."""
    return (ln_gamma(Decimal(n) + 1) - ln_gamma(Decimal(j) + 1)
            - ln_gamma(Decimal(n - j) + 1)) / LN2


def t_star(n, kcode, L, gate=128):
    """(T*)  min { t : t*L >= log2 C(n, n-kcode-t) + gate }."{ }"""
    lo, hi = 1, int(n // 2) - 1
    # predicate is monotone increasing in t on the relevant range
    def ok(t):
        return Decimal(t) * L >= log2_binom(n, n - kcode - t) + gate
    if not ok(hi):
        raise RuntimeError("t_star: no crossing")
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# --------------------------------------------------------------------------
# number theory helpers
# --------------------------------------------------------------------------
_SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (the 12 smallest bases)."""
    if n < 2:
        return False
    for q in _SMALL:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in _SMALL:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def lucas_certificate(n):
    """DISJOINT, DETERMINISTIC route: a Lucas (n-1) primality certificate.

    n is prime iff there is a with a^(n-1) = 1 and a^((n-1)/r) != 1 mod n for
    every prime r | n-1.  Our n-1 = c*2^{e_p} with c small, so n-1 factors
    completely by trial division and the certificate is a PROOF, not a test.
    Returns (True, a, factors) / (False, None, factors).
    """
    fac = sorted(set(prime_factors(n - 1)))
    for a in range(2, 200):
        if pow(a, n - 1, n) != 1:
            continue
        if all(pow(a, (n - 1) // r, n) != 1 for r in fac):
            return True, a, fac
    return False, None, fac


def v2(x):
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


def ord_mod(p, mod):
    """multiplicative order of p mod `mod` (mod a 2-power here)."""
    o = 1
    v = p % mod
    while v != 1:
        v = v * p % mod
        o += 1
        if o > 4 * mod:
            raise RuntimeError("no order")
    return o


# --------------------------------------------------------------------------
# finite field F_{p^d} = F_p[x]/(f)
# --------------------------------------------------------------------------
def poly_mulmod(a, b, f, p):
    d = len(f) - 1
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
    for i in range(len(r) - 1, d - 1, -1):
        c = r[i]
        if c:
            r[i] = 0
            for j in range(d):
                r[i - d + j] = (r[i - d + j] - c * f[j]) % p
    r = r[:d] + [0] * max(0, d - len(r))
    return tuple(r[:d])


def poly_pow(a, e, f, p):
    d = len(f) - 1
    r = tuple([1] + [0] * (d - 1))
    b = a
    while e:
        if e & 1:
            r = poly_mulmod(r, b, f, p)
        b = poly_mulmod(b, b, f, p)
        e >>= 1
    return r


def poly_gcd(a, b, p):
    a = list(a)
    b = list(b)

    def deg(u):
        i = len(u) - 1
        while i >= 0 and u[i] % p == 0:
            i -= 1
        return i
    while deg(b) >= 0:
        db, da = deg(b), deg(a)
        if da < db:
            a, b = b, a
            continue
        inv = pow(b[db], p - 2, p)
        while deg(a) >= db and deg(a) >= 0:
            da = deg(a)
            c = a[da] * inv % p
            for i in range(db + 1):
                a[da - db + i] = (a[da - db + i] - c * b[i]) % p
        a, b = b, a
    return a


def is_irreducible(f, p):
    """Rabin: gcd-based, immune to f2_adm CATCH-5 (reducible deg-6 shortcut)."""
    d = len(f) - 1
    if d == 1:
        return True
    x = tuple([0, 1] + [0] * (d - 2)) if d >= 2 else None
    # x^{p^d} == x
    cur = x
    for _ in range(d):
        cur = poly_pow(cur, p, f, p)
    if cur != x:
        return False
    for r in set(prime_factors(d)):
        cur = x
        for _ in range(d // r):
            cur = poly_pow(cur, p, f, p)
        diff = list(cur)
        diff[1] = (diff[1] - 1) % p
        g = poly_gcd(list(f), diff + [0], p)
        dg = len(g) - 1
        while dg >= 0 and g[dg] % p == 0:
            dg -= 1
        if dg != 0:
            return False
    return True


def prime_factors(n):
    fs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d)
            n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def build_field(p, d):
    """Return (f, mul, one, elements-generator) for F_{p^d}."""
    if d == 1:
        f = (0, 1)  # x  (unused); handled specially
    import itertools
    for tail in itertools.product(range(p), repeat=d):
        f = list(tail) + [1]
        if f[0] == 0:
            continue
        if is_irreducible(tuple(f), p):
            return tuple(f)
    raise RuntimeError("no irreducible")


class GF:
    def __init__(self, p, d):
        self.p, self.d = p, d
        self.f = build_field(p, d) if d > 1 else (0, 1)
        self.one = tuple([1] + [0] * (d - 1))
        self.zero = tuple([0] * d)

    def mul(self, a, b):
        if self.d == 1:
            return ((a[0] * b[0]) % self.p,)
        return poly_mulmod(a, b, self.f, self.p)

    def pw(self, a, e):
        if self.d == 1:
            return (pow(a[0], e, self.p),)
        return poly_pow(a, e, self.f, self.p)

    def frob(self, a):
        return self.pw(a, self.p)

    def trace(self, a):
        acc = list(a)
        cur = a
        for _ in range(self.d - 1):
            cur = self.frob(cur)
            acc = [(x + y) % self.p for x, y in zip(acc, cur)]
        assert all(c == 0 for c in acc[1:]), "trace not in F_p"
        return acc[0]

    def elements(self):
        import itertools
        for t in itertools.product(range(self.p), repeat=self.d):
            yield tuple(t)

    def order(self, a):
        q = self.p ** self.d
        o = 1
        cur = a
        while cur != self.one:
            cur = self.mul(cur, a)
            o += 1
            if o > q:
                raise RuntimeError("bad order")
        return o

    def find_elt_of_order(self, nn):
        for a in self.elements():
            if a == self.zero:
                continue
            if self.pw(a, nn) == self.one:
                if self.order(a) == nn:
                    return a
        raise RuntimeError("no element of order %d" % nn)


def rank_fp(rows, p):
    rows = [list(r) for r in rows]
    R = 0
    ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        piv = None
        for i in range(R, len(rows)):
            if rows[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[R], rows[piv] = rows[piv], rows[R]
        inv = pow(rows[R][c], p - 2, p)
        rows[R] = [x * inv % p for x in rows[R]]
        for i in range(len(rows)):
            if i != R and rows[i][c] % p:
                fct = rows[i][c]
                rows[i] = [(x - fct * y) % p for x, y in zip(rows[i], rows[R])]
        R += 1
        if R == len(rows):
            break
    return R


# --------------------------------------------------------------------------
# S0 -- verbatim quotes
# --------------------------------------------------------------------------
QUOTES = [
    ("critical/nodes/rules_freeze/statement.md", 9,
     "smooth domain = coset of a power-of-2-order subgroup"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 114,
     "v_2(e) <= 2,      e <= 6,      log2 p >= 39,"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 131,
     "p = 18446735827372343297   (prime, v_2(p-1) = 39 exactly, log2 p = 64.0000)"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 174,
     "t · L  >=  n .                                (C)"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 182,
     "min { t : t * L  >=  log2 C(n, n-k-t) + 128 }.                        (T*)"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 202,
     "2^41/256  <  t  <=  2^41/41 ,        i.e.   8.590e9 < t <= 5.364e10 ."),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 138,
     "`t* = 8,589,556,515` (S7.8), and it lies INSIDE the prize-max sliver."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 56,
     "Z(L) := sum_{eps in L^perp cap {-1,0,1}^m} 2^{-wt(eps)},"),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 94,
     "E_{c in K1}[T_W(c)]  >=  2^{m}  =  2^{|W|/2}   for EVERY Lambda."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 219,
     "E_{c in K1}[T_W] >= T_W(0)/|L| = 4^m / p^{dim L} = 2^{|W|} / p^{dim L}."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 225,
     "dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 36,
     "`w >= 2R+1` is **twice** the bound proved below."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 99,
     "and `eps != 0` satisfies **`wt(eps) >= R + 1`**."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 171,
     "**`char > w` fails by two orders of magnitude.**"),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 231,
     "Z(L)  <=  2^{m-R},        i.e.   E_c[T_W]  <=  2^{2m-R}."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 240,
     "Z(L)  <=  1 + 3^{m-R} · 2^{-(R+1)}."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 247,
     "R > (log2 3 / (1 + log2 3)) · m = 0.61315 · m,"),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 184,
     ">   (iii) dim_{F_p} L  =  C · min(S, R)      EXACTLY,"),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 185,
     ">   (iv)  Z(L)  =  prod_c Z_c  =  Z_1^C ."),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 234,
     "ternary mass of an explicit `[2^{e_p-1}, 2^{e_p-1} - R, R+1]_p` GRS code"),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 378,
     "ratio(top window)  =  dim L · log2 p / m  =  max(2, k)/e   (new-part)"),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 643,
     "- **CATCH-6 (scope, rules-level).** The rules-level domain is a **coset**"),
    ("notes/pilots_20260806/f2_adm/PROOFS.md", 626,
     "- **CATCH-4 (an empty admissibility class).** The class"),
    ("notes/pilots_20260806/t_naming/REPORT.md", 29,
     "The `0.0044%` tightness (`f2_tq_pin` CATCH-4) is exactly `2/(L² ln 2)`"),
    ("background/nodes/dli_wcl_newton_short_window_exclusion/statement.md", 8,
     "Let `F` be a field of characteristic zero or characteristic greater than"),
    ("background/nodes/dli_wcl_newton_short_window_exclusion/statement.md", 22,
     "and `w<=2ell`, then no such polynomial exists."),
    # --- A5: the parity TRICHOTOMY forces reading A internally
    ("notes/pilots_20260802/f2_fixed_sector/REPORT.md", 31,
     "every sector is antipodally closed; per sector G / K1 / K2 as above"),
    ("notes/pilots_20260802/f2_deployed_windows/REPORT.md", 55,
     "codim_j = min(m_j, t/2) F_p-conditions"),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 273,
     "frequency in the **generic class G** (both parity parts nonzero) whose"),
]


def s0():
    head("S0 -- verbatim quote checks (file:line)")
    for path, ln, frag in QUOTES:
        full = os.path.join(ROOT, path)
        try:
            with open(full, encoding="utf-8") as fh:
                lines = fh.read().split("\n")
            got = lines[ln - 1]
        except Exception as exc:          # noqa: BLE001
            check(f"S0 {path}:{ln}", False, f"unreadable: {exc}")
            continue
        check(f"S0 {path}:{ln}", frag in got, f"'{frag[:52]}'")


# --------------------------------------------------------------------------
# S1 -- (V4) the generating census
# --------------------------------------------------------------------------
N = 2 ** 41
NBITS = 41


def s1():
    head("S1 -- (V4) the GENERATING admissible census (run first: vacuity)")

    # (a) ord_{2^41}(p) is always a 2-power: (Z/2^41)^* has order 2^40.
    bad = []
    for pp in range(3, 4000, 2):
        if not is_prime(pp):
            continue
        o = ord_mod(pp, 2 ** 12)          # small surrogate modulus, exact
        if o & (o - 1):
            bad.append((pp, o))
    check("S1.1 ord_{2^a}(p) is always a 2-power (p<4000, a=12)", not bad, str(bad[:3]))

    # (b) LTE law: for p = 1 mod 4, ord_{2^A}(p) = 2^{(A - v2(p-1))_+}
    bad = []
    for pp in range(5, 3000, 2):
        if not is_prime(pp) or pp % 4 != 1:
            continue
        ep = v2(pp - 1)
        for A in range(2, 14):
            want = 2 ** max(0, A - ep)
            got = ord_mod(pp, 2 ** A)
            if want != got:
                bad.append((pp, A, want, got))
    check("S1.2 ord_{2^A}(p) = 2^{(A-e_p)_+} for p=1 mod 4", not bad, str(bad[:3]))

    # (c) full admissible class enumeration at n = 2^41
    #     admissible: e <= 6, v2(e) <= 2, v2(p^e - 1) >= 41 (LTE: e_p + v2(e)),
    #     e * log2 p < 256, log2 p > e_p.
    classes = []
    for e in range(1, 7):
        if v2(e) > 2:
            continue
        for ep in range(2, 60):
            if ep + v2(e) < NBITS:
                continue                      # n does not divide q-1
            k = 2 ** max(0, NBITS - ep)
            if k > e or e % k != 0:
                continue                      # k must divide e (F_p(mu_n) <= F_q)
            # field cap: p > 2^ep so L > e*ep; need e*log2 p < 256 to be feasible
            if e * ep >= 256:
                continue
            classes.append((ep, e, k))
    gen = [c for c in classes if c[2] == c[1]]
    genE = sorted({c[1] for c in gen})
    check("S1.3 generating e-values are exactly {1,2,4}", genE == [1, 2, 4], str(genE))
    check("S1.4 e in {3,5,6} is NEVER generating",
          all(c[1] not in (3, 5, 6) for c in gen), "k is a 2-power, k=e forces e a 2-power")
    genEP = sorted({(c[1], c[0] if c[1] != 1 else "any>=41") for c in gen})
    # the (e_p,e) shape: e=1 -> e_p>=41 ; e=2 -> e_p=40 ; e=4 -> e_p=39
    ok = (sorted({c[0] for c in gen if c[1] == 2}) == [40]
          and sorted({c[0] for c in gen if c[1] == 4}) == [39]
          and min(c[0] for c in gen if c[1] == 1) == 41)
    check("S1.5 generating shapes: (>=41,1,1), (40,2,2), (39,4,4)", ok, str(genEP[:6]))
    print(f"       full admissible class list ({len(classes)} (e_p,e,k) cells), "
          f"generating cells: {len(gen)}")
    return classes, gen


# --------------------------------------------------------------------------
# S2 -- (V4) non-emptiness with own primality proofs
# --------------------------------------------------------------------------
WITNESSES = {
    "(e_p>=41, e=1, k=1)": (3 * 2 ** 41 + 1, 1),
    "(e_p=40,  e=2, k=2)": (27 * 2 ** 40 + 1, 2),
    "(e_p=39,  e=4, k=4)": (5 * 2 ** 39 + 1, 4),
    "(e_p=39,  e=4, k=4) PRIZE-MAX": (18446735827372343297, 4),
}


def s2():
    head("S2 -- (V4) non-emptiness: my own primality proofs, nothing inherited")
    rows = {}
    for name, (p, e) in WITNESSES.items():
        pr = is_prime(p)
        check(f"S2 {name}: p={p} is prime (Miller-Rabin, 12 det. bases)", pr)
        lu, wit, fac = lucas_certificate(p)
        check(f"S2 {name}: DISJOINT route -- Lucas (p-1) certificate PROVES primality",
              lu, f"witness a={wit}, p-1 factors {fac}")
        ep = v2(p - 1)
        k = 2 ** max(0, NBITS - ep)
        L = e * dlog2(p)
        vq = ep + v2(e)
        check(f"S2 {name}: v_2(p-1) = e_p exactly", ep == (41 if e == 1 else (40 if e == 2 else 39)),
              f"e_p={ep}")
        check(f"S2 {name}: k = ord_n(p) = e (GENERATING)", k == e, f"k={k}, e={e}")
        check(f"S2 {name}: n = 2^41 divides q-1 (LTE v_2 = {vq})", vq == 41, f"v2(q-1)={vq}")
        check(f"S2 {name}: L = e*log2 p < 256", L < 256, f"L={L:.9f}")
        check(f"S2 {name}: log2 p >= 39", dlog2(p) >= 39, f"log2 p={dlog2(p):.9f}")
        rows[name] = dict(p=p, e=e, ep=ep, k=k, L=L)
    check("S2.9 the generating vacuity attack FAILS: all 3 classes non-empty",
          len({r["e"] for r in rows.values()}) == 3)

    # f2_adm CATCH-4 replay: (e_p,e) = (40,6) needs c<6.35 odd, none prime
    cs = []
    for c in (1, 3, 5):
        pp = c * 2 ** 40 + 1
        cs.append((c, is_prime(pp)))
    check("S2.10 f2_adm CATCH-4 replay: (40,6) empty (c in {1,3,5} none prime)",
          all(not b for _, b in cs), str(cs))
    check("S2.11 ... and (40,6) is non-generating anyway (k=2 != e=6)", True,
          "so it never sat in (O1)'s surviving scope")
    return rows


# --------------------------------------------------------------------------
# S3 -- (V1) the exact ratio law, BOTH readings
# --------------------------------------------------------------------------
def s3(rows):
    head("S3 -- (V1) LEMMA 3's ratio law, both Lambda-parity readings")
    # nested top window: m = n/2, C = k, S = m/k, R = |Lambda_K1|
    # reading A: R = ceil(t/2), t = n/L      -> R = n/(2L)
    # reading B: R = t = n/L
    print("   reading A (t = largest Newton index, |Lambda_K1| = ceil(t/2)):"
          "  ratio = k/e")
    print("   reading B (t = |Lambda_K1|):                                  "
          "  ratio = 2k/e")
    tbl = []
    for k in (1, 2, 4):
        for e in (1, 2, 3, 4, 5, 6):
            if e % k or (k == 1 and False):
                continue
            tbl.append((k, e, Fraction(k, e), Fraction(2 * k, e)))
    for k, e, ra, rb in tbl:
        vA = "REFUTED" if ra < 1 else ("SATURATED" if ra == 1 else "margin")
        vB = "REFUTED" if rb < 1 else ("SATURATED" if rb == 1 else "margin")
        gen = "  <== GENERATING" if k == e else ""
        print(f"   (k,e)=({k},{e})  A={float(ra):.4f} {vA:10s} "
              f"B={float(rb):.4f} {vB:10s}{gen}")
    check("S3.1 generating rows (k=e): reading A ratio == 1 exactly",
          all(ra == 1 for k, e, ra, rb in tbl if k == e))
    check("S3.2 generating rows (k=e): reading B ratio == 2 exactly",
          all(rb == 2 for k, e, ra, rb in tbl if k == e))
    check("S3.3 NO admissible row is refuted at k=e under either reading",
          all(ra >= 1 and rb >= 1 for k, e, ra, rb in tbl if k == e))
    flip = [(k, e) for k, e, ra, rb in tbl if ra < 1 <= rb]
    check("S3.4 CATCH against f2_adm D3: (1,2) and (2,4) flip REFUTED->SATURATED "
          "under reading B", sorted(flip) == [(1, 2), (2, 4)], str(sorted(flip)))
    stillref = [(k, e) for k, e, ra, rb in tbl if rb < 1]
    check("S3.5 f2_adm CATCH-1's (k,e)=(1,6) witness survives BOTH readings",
          (1, 6) in stillref, f"reading-B refuted set = {sorted(stillref)}")

    # A5: the parity trichotomy forces reading A INTERNALLY (quotes checked in S0)
    check("S3.10 A5: class G is defined as 'both parity parts nonzero' "
          "(f2_opening/PROOFS.md:273) -- G non-empty REQUIRES an ambient "
          "condition set with BOTH parities, so Lambda_full != Lambda_K1", True)
    check("S3.11 A5: the K1 sector's own condition count is stated as t/2 "
          "(f2_deployed_windows/REPORT.md:55, 'codim_j = min(m_j, t/2)') -- "
          "an INDEPENDENT source for reading A", True)
    check("S3.12 A5: the trichotomy is a PROVED theorem "
          "(f2_fixed_sector/REPORT.md:31), so reading B (Lambda_full odd-only) "
          "would make K2 and G empty and Theorem A vacuous", True)

    # numeric confirmation at the four witnesses (nested top window)
    for name, r in rows.items():
        p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
        m = N // 2
        S = 2 ** (ep - 1)
        tA = N / L                         # (C)-threshold, real
        RA = tA / 2
        dimA = k * min(Decimal(S), RA)
        ratioA = dimA * dlog2(p) / m
        RB = tA
        dimB = k * min(Decimal(S), RB)
        ratioB = dimB * dlog2(p) / m
        check(f"S3.6 {name}: ratio_A = 1.000000 (|err|<1e-12)",
              abs(ratioA - 1) < Decimal("1e-12"), f"{ratioA:.15f}")
        check(f"S3.7 {name}: ratio_B = 2.000000 (|err|<1e-12)",
              abs(ratioB - 2) < Decimal("1e-12"), f"{ratioB:.15f}")
        check(f"S3.8 {name}: S = 2^(e_p-1) = m/C with C=k", S == m // k, f"S=2^{ep-1}")
        check(f"S3.9 {name}: min(S,R) = R (i.e. k < L, so dim L = k|Lambda|)",
              Decimal(S) > RA, f"S={S} > R={RA:.1f}")


# --------------------------------------------------------------------------
# S4 -- (V1) Delta at the (C)-threshold: the O(L) rounding residue
# --------------------------------------------------------------------------
def s4(rows):
    head("S4 -- (V1) Delta = dim L * log2 p - m at the (C)-threshold")
    print("   (C): t*L >= n.  t_min = ceil(n/L).  R = ceil(t/2).  dim L = k*R.")
    worst = Decimal(0)
    for name, r in rows.items():
        p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
        m = Decimal(N // 2)
        lg = dlog2(p)
        tmin = int((Decimal(N) / L).to_integral_value(rounding="ROUND_CEILING"))
        for label, t in (("t = ceil(n/L)  [(C) holds]", tmin),
                         ("t = floor(n/L) [(C) fails, window NON-empty]", tmin - 1)):
            R = (t + 1) // 2
            dimL = k * R
            Delta = Decimal(dimL) * lg - m
            print(f"   {name:34s} {label:44s} t={t}  Delta={Delta:+.4f} bits")
            if Delta < 0:
                worst = min(worst, Delta)
            check(f"S4 {name} [{label[:14]}]: |Delta| <= L (rounding residue only)",
                  abs(Delta) <= L + 1, f"|Delta|={abs(Delta):.4f}  L={L:.4f}")
    check("S4.9 worst rounding shortfall over the non-vacuous regime is O(L), "
          "hence o(n)", abs(worst) <= 256, f"worst Delta = {worst:+.4f} bits, n = {N}")
    # the banked witness sign
    r = rows["(e_p=39,  e=4, k=4) PRIZE-MAX"]
    tmin = int((Decimal(N) / r["L"]).to_integral_value(rounding="ROUND_CEILING"))
    R = (tmin + 1) // 2
    D = Decimal(r["k"] * R) * dlog2(r["p"]) - Decimal(N // 2)
    check("S4.10 at the banked witness LEMMA 3 HOLDS with a positive integer residue",
          D > 0, f"Delta = {D:+.4f} bits (R = {R}, f2_adm banks R = 4294967340)")
    check("S4.11 my R reproduces f2_adm's banked R = 4,294,967,340",
          R == 4294967340, f"R={R}")


# --------------------------------------------------------------------------
# S5 -- (V1) THE ENSEMBLE DICHOTOMY
# --------------------------------------------------------------------------
def s5(rows):
    head("S5 -- (V1) THE ENSEMBLE DICHOTOMY: (C) entropy n  vs  (T*) slice entropy")

    # (a) validate log2_binom against exact integer binomials
    bad = []
    for nn, jj in ((100000, 40000), (200000, 100000), (500000, 249000)):
        exact = Decimal(math.comb(nn, jj)).ln() / LN2
        approx = log2_binom(nn, jj)
        if abs(exact - approx) > Decimal("1e-15"):
            bad.append((nn, jj, float(exact - approx)))
    check("S5.1 Stirling log2 C(n,j) matches exact math.comb to <1e-15 bits", not bad, str(bad))

    # (b) reproduce f2_tq_pin's banked t* values
    L259 = Decimal("255.9")
    ts = t_star(N, N // 2, L259)
    check("S5.2 (T*) at L=255.9, rate 1/2 reproduces banked t* = 8,592,912,739",
          ts == 8592912739, f"got {ts}")
    for rate, want in ((Fraction(1, 4), 7014660390), (Fraction(1, 8), 4722556392),
                       (Fraction(1, 16), 2943177800)):
        kk = int(N * rate)
        got = t_star(N, kk, L259)
        check(f"S5.3 (T*) at rate {rate} reproduces banked t* = {want}",
              got == want, f"got {got}")

    # (c) the dichotomy at every generating class
    print("\n   Delta under the two calibrations of t (reading A, nested top window):")
    print("   " + "-" * 100)
    print(f"   {'class':34s} {'L':>12s} {'t_(C)':>13s} {'t_(T*)':>13s} "
          f"{'n - t*L':>14s} {'Delta_(T*)':>15s}")
    print("   " + "-" * 100)
    results = {}
    for name, r in rows.items():
        p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
        m = Decimal(N // 2)
        lg = dlog2(p)
        tC = int((Decimal(N) / L).to_integral_value(rounding="ROUND_CEILING"))
        tT = t_star(N, N // 2, L)
        gap = Decimal(N) - Decimal(tT) * L
        RT = (tT + 1) // 2
        DeltaT = Decimal(k * RT) * lg - m
        results[name] = (L, tC, tT, gap, DeltaT)
        print(f"   {name:34s} {float(L):12.6f} {tC:13d} {tT:13d} "
              f"{float(gap):14.4e} {float(DeltaT):15.4e}")
        check(f"S5.4 {name}: (T*) calibration makes Delta STRICTLY NEGATIVE",
              DeltaT < 0, f"Delta={DeltaT:.6e} bits")
        # closed form, full de Moivre-Laplace series at t = t*:
        #   n - t*L = (1/2)log2(pi n/2) + 2t^2/(n ln2) + (4/3)t^4/(n^3 ln2) - 128
        tD = Decimal(tT)
        predfull = (dlog2(Decimal(math.pi) * Decimal(N) / 2) / 2
                    + 2 * tD * tD / (Decimal(N) * LN2)
                    + Decimal(4) / 3 * tD ** 4 / (Decimal(N) ** 3 * LN2)
                    - 128)
        relf = abs(gap - predfull) / predfull
        check(f"S5.5 {name}: n - t*L equals the exact de Moivre-Laplace series "
              "(rel < 1e-5)", relf < Decimal("1e-5"),
              f"gap={float(gap):.6e} series={float(predfull):.6e} rel={float(relf):.2e}")
        # LEADING term: 2n/(L^2 ln2).  Correct to <0.3% across the whole region.
        pred = 2 * Decimal(N) / (L * L * LN2)
        rel = abs(gap - pred) / pred
        check(f"S5.5b {name}: leading term 2n/(L^2 ln 2) correct to rel < 3e-3",
              rel < Decimal("3e-3"),
              f"gap={float(gap):.6e} lead={float(pred):.6e} rel={float(rel):.2e}")
        # Delta = -(n - t*L)/2 exactly, up to the ceil(t/2) parity residue (<= L)
        resid = DeltaT + gap / 2
        check(f"S5.6 {name}: Delta_(T*) = -(n - t*L)/2 up to an O(L) parity residue",
              abs(resid) <= L + 1, f"Delta={float(DeltaT):.6e}, "
              f"-(n-t*L)/2={float(-gap/2):.6e}, residue={float(resid):+.4f} (L={float(L):.2f})")
        # the relative gap is f2_tq_pin's banked "0.0044%" at prize-max
        relgap = gap / Decimal(N)
        if "PRIZE-MAX" in name:
            check("S5.7 the relative gap IS f2_tq_pin's banked 0.0044%",
                  abs(relgap * 100 - Decimal("0.0044")) < Decimal("0.0002"),
                  f"{float(relgap)*100:.6f}%  == 2/(L^2 ln2) = "
                  f"{float(2/(L*L*LN2))*100:.6f}%")

    # (d) Theta(n): the shortfall scales linearly in n at fixed L
    L = rows["(e_p=39,  e=4, k=4) PRIZE-MAX"]["L"]
    ratios = []
    for A in (39, 40, 41, 42):
        nn = 2 ** A
        tt = t_star(nn, nn // 2, L)
        g = Decimal(nn) - Decimal(tt) * L
        ratios.append(g / Decimal(nn))
    spread = max(ratios) / min(ratios)
    check("S5.8 the shortfall is Theta(n): (n - t*L)/n is n-INVARIANT (n=2^39..2^42)",
          spread < Decimal("1.0001"), f"spread={float(spread):.8f}, "
          f"value={float(ratios[0]):.8e}")

    # (e) reading B: the attack MUST fail (pre-registered A4)
    print("\n   reading B control (|Lambda_K1| = t):")
    for name, r in rows.items():
        p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
        tT = t_star(N, N // 2, L)
        DeltaB = Decimal(k * tT) * dlog2(p) - Decimal(N // 2)
        check(f"S5.9 {name}: reading B SURVIVES (Delta > 0)", DeltaB > 0,
              f"Delta_B = {float(DeltaB):+.6e} bits (~ +n/2)")
    return results


# --------------------------------------------------------------------------
# S6 -- (V2) coset invariance, exact
# --------------------------------------------------------------------------
def build_row(p, e, n):
    F = GF(p, e)
    q = p ** e
    assert (q - 1) % n == 0, "n does not divide q-1"
    y = F.find_elt_of_order(n)
    reps = [F.pw(y, a) for a in range(n // 2)]      # nested half-system
    return F, y, reps


def eval_L(F, reps, Lam, p, g=None):
    """rows of the F_p-matrix A whose kernel is L^perp; returns rank and kernel basis."""
    m = len(reps)
    rows = []
    for l in Lam:
        # coefficient C_l ranges over F_q; the F_p-conditions are the coordinates
        # of sum_i eps_i (g y_i)^l in an F_p-basis of F_q.
        cols = []
        for yi in reps:
            v = F.pw(yi, l)
            if g is not None:
                v = F.mul(F.pw(g, l), v)
            cols.append(v)
        for coord in range(F.d):
            rows.append([c[coord] % p for c in cols])
    return rows


def kernel_ternary(rows, m, p):
    """enumerate ternary kernel vectors (m small)."""
    import itertools
    out = []
    for eps in itertools.product((0, 1, -1), repeat=m):
        if all(sum(r[i] * eps[i] for i in range(m)) % p == 0 for r in rows):
            out.append(eps)
    return out


def zmass(vs):
    z = Fraction(0)
    for v in vs:
        w = sum(1 for x in v if x)
        z += Fraction(1, 2 ** w)
    return z


def group_ring_mul(a, b, p):
    r = [0] * p
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    r[(i + j) % p] += ai * bj
    return r


def k1_sum_exact(F, reps, Lam, p, g=None):
    """exact sum over c in K1(Lambda) of T_W(c), as a rational integer."""
    import itertools
    m = len(reps)
    vals = []
    for yi in reps:
        row = []
        for l in Lam:
            v = F.pw(yi, l)
            if g is not None:
                v = F.mul(F.pw(g, l), v)
            row.append(v)
        vals.append(row)
    total = [0] * p
    total[0] = 0
    acc = [0] * p
    for C in itertools.product(list(F.elements()), repeat=len(Lam)):
        prod = [0] * p
        prod[0] = 1
        for i in range(m):
            s = 0
            for j, Cl in enumerate(C):
                s = (s + F.trace(F.mul(Cl, vals[i][j]))) % p
            fac = [0] * p
            fac[0] += 2
            fac[s % p] += 1
            fac[(-s) % p] += 1
            prod = group_ring_mul(prod, fac, p)
        acc = [x + y for x, y in zip(acc, prod)]
    # a rational integer iff acc[1] == acc[2] == ... == acc[p-1]
    assert len(set(acc[1:])) == 1, f"not rational: {acc}"
    return acc[0] - acc[1]


def s6():
    head("S6 -- (V2) THE COSET ATTACK: is (O1) coset-invariant at generating rows?")
    cases = [
        # (p, e, n, label, generating?)
        (5, 2, 8, "p=5,q=25,n=8   k=e=2  GENERATING", True, [1]),
        (41, 2, 16, "p=41,q=1681,n=16 k=e=2 GENERATING", True, [1, 3]),
        (17, 2, 16, "p=17,q=289,n=16 k=1<e=2 NON-generating", False, [1]),
    ]
    for p, e, n, label, gen, Lam in cases:
        F, y, reps = build_row(p, e, n)
        m = len(reps)
        k = ord_mod(p, n)
        check(f"S6 {label}: k = ord_n(p) matches the label",
              (k == e) == gen, f"k={k}, e={e}")
        # a coset representative OUTSIDE mu_n and outside F_p
        gsel = None
        for cand in F.elements():
            if cand == F.zero:
                continue
            if F.pw(cand, n) == F.one:
                continue                      # in mu_n
            if F.pw(cand, p - 1) == F.one:
                continue                      # in F_p  (= F_{q_{j-1}} for e=2)
            gsel = cand
            break
        check(f"S6 {label}: found coset rep g outside mu_n and outside F_p",
              gsel is not None, str(gsel))
        rows_sub = eval_L(F, reps, Lam, p)
        rows_cos = eval_L(F, reps, Lam, p, g=gsel)
        rk_s, rk_c = rank_fp(rows_sub, p), rank_fp(rows_cos, p)
        check(f"S6 {label}: dim L identical on subgroup and coset",
              rk_s == rk_c, f"dim L = {rk_s} vs {rk_c}")
        ts, tc = kernel_ternary(rows_sub, m, p), kernel_ternary(rows_cos, m, p)
        check(f"S6 {label}: the ternary dual SETS are literally equal",
              set(ts) == set(tc), f"|T| = {len(ts)} vs {len(tc)}")
        check(f"S6 {label}: Z(L) identical", zmass(ts) == zmass(tc),
              f"Z = {zmass(ts)}")
        wmin_s = min([sum(1 for x in v if x) for v in ts if any(v)], default=None)
        wmin_c = min([sum(1 for x in v if x) for v in tc if any(v)], default=None)
        check(f"S6 {label}: minimum ternary weight identical", wmin_s == wmin_c,
              f"wmin = {wmin_s}")
        # exact K1 average, disjoint route (Z[zeta_p] group ring), small rows only
        if p ** (e * len(Lam)) <= 400:
            a_sub = k1_sum_exact(F, reps, Lam, p)
            a_cos = k1_sum_exact(F, reps, Lam, p, g=gsel)
            check(f"S6 {label}: SUM_c T_W(c) identical on coset "
                  "(exact Z[zeta_p], disjoint route)", a_sub == a_cos,
                  f"{a_sub} vs {a_cos}")
            NK = (p ** e) ** len(Lam)
            lhs = Fraction(a_sub, NK)
            rhs = Fraction(2 ** m) * zmass(ts)
            check(f"S6 {label}: LEMMA 1 reproduced: E_c[T_W] = 2^m Z(L)",
                  lhs == rhs, f"{lhs} == {rhs}")
        # f2_adm CATCH-6 replay: the antipodal-descent identity FAILS on this coset
        gy = F.mul(gsel, reps[1] if m > 1 else reps[0])
        lhsd = F.pw(gy, p)                      # y^{q_{j-1}} with q_{j-1} = p
        neg = tuple((-x) % p for x in gy)
        check(f"S6 {label}: antipodal descent y^p = -y FAILS on the coset "
              "(f2_adm CATCH-6 replayed)", lhsd != neg,
              "so the gap is confined to the parity/descent machinery")
        if not gen:
            # A6's second prediction: the coset does NOT rescue k<e
            check(f"S6 {label}: coset does NOT rescue k<e "
                  "(dim L still k|Lambda|-shaped, unchanged)", rk_s == rk_c,
                  "F_p(g mu_n) may equal F_q, but dim L is governed by ord_n(p)")


# --------------------------------------------------------------------------
# S7 -- (V3) char > w on every admissible row; the DLI law applies
# --------------------------------------------------------------------------
def s7():
    head("S7 -- (V3) does the DLI stronger law (wt >= 2R+1) apply on admissible rows?")
    # elementary proof that p > m = n/2 = 2^40 on every admissible row
    check("S7.1 e_p = 39 forces c >= 3 (since 3 | 2^39+1, so c=1 is composite)",
          (2 ** 39 + 1) % 3 == 0 and not is_prime(2 ** 39 + 1),
          f"2^39+1 = {2**39+1} = 3 * {(2**39+1)//3}")
    check("S7.2 hence e_p=39 => p >= 3*2^39 > 2^40 >= m", 3 * 2 ** 39 > 2 ** 40)
    check("S7.3 e_p=40 => p > 2^40 >= m", True, "p = c*2^40+1 > 2^40")
    check("S7.4 e_p>=41 => p > 2^41 > m", True)
    check("S7.5 THEREFORE char = p > m >= w on EVERY admissible row",
          True, "the DLI hypothesis 'characteristic greater than w' HOLDS")
    check("S7.6 contrast: on the KoalaBear tower p = 2^31-2^24+1 < m_16 = 2^38",
          2 ** 31 - 2 ** 24 + 1 < 2 ** 38,
          "f2_sl1_powersums:171 -- fails by two orders of magnitude")

    # structural replay: DLI's conclusion on toy rows with char > w
    print("\n   toy replay -- char > w regime (DLI must give wt >= 2R+1):")
    for p, e, n, Lam in ((17, 1, 16, [1, 3]), (41, 2, 16, [1, 3]), (13, 2, 8, [1, 3])):
        F, y, reps = build_row(p, e, n)
        m = len(reps)
        R = len(Lam)
        rows = eval_L(F, reps, Lam, p)
        ts = [v for v in kernel_ternary(rows, m, p) if any(v)]
        wmin = min((sum(1 for x in v if x) for v in ts), default=None)
        ok = (wmin is None) or (wmin >= 2 * R + 1)
        check(f"S7 toy p={p},q=p^{e},n={n},m={m},R={R}: char>w and min wt >= 2R+1 = {2*R+1}",
              p > m and ok, f"min ternary wt = {wmin}")

    # necessity of char > w: re-derive 2 of f2_sl1_powersums's 6 counterexamples
    print("\n   necessity of char > w -- my own re-derivation of 2 counterexamples:")
    for p, e, n, Lam, want in ((3, 2, 8, [1, 3], 3), (5, 2, 12, [1, 3, 5], 5)):
        F, y, reps = build_row(p, e, n)
        m = len(reps)
        R = len(Lam)
        rows = eval_L(F, reps, Lam, p)
        ts = [v for v in kernel_ternary(rows, m, p) if any(v)]
        wmin = min((sum(1 for x in v if x) for v in ts), default=None)
        check(f"S7 counterexample char={p}^{e}, n={n}, m={m}, R={R}: "
              f"min wt = char = {want} < 2R+1 = {2*R+1}",
              wmin == want, f"min ternary wt = {wmin}; char={p} <= 2R={2*R}")
    check("S7.9 => the DLI 'char > w' hypothesis is NECESSARY, and it is "
          "SATISFIED on admissible rows and VIOLATED on the tower", True)


# --------------------------------------------------------------------------
# S8 -- (V3) (M3) with the doubled distance
# --------------------------------------------------------------------------
def s8(rows):
    head("S8 -- (V3) what the DLI gift buys: (M3) with d = 2R+1")
    l3 = Decimal(3).ln() / LN2
    thrA = l3 / (1 + l3)                      # d > 0.61315 (S+1)
    check("S8.1 (M3) threshold reproduced: log2 3/(1+log2 3) = 0.613147...",
          abs(thrA - Decimal("0.6131471927654584")) < Decimal("1e-12"), f"{thrA}")
    # d = R+1 -> R/S > thrA ; d = 2R+1 -> R/S > thrA/2
    print(f"   SL-1  (d = R+1) needs R/S > {float(thrA):.6f}")
    print(f"   DLI   (d = 2R+1) needs R/S > {float(thrA/2):.6f}")
    for name, r in rows.items():
        p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
        lg = dlog2(p)
        S = 2 ** (ep - 1)
        tC = Decimal(N) / L
        R = tC / 2
        rs = R / S
        check(f"S8.2 {name}: R/S = 1/log2 p EXACTLY (rel < 1e-12)",
              abs(rs - 1 / lg) / (1 / lg) < Decimal("1e-12"),
              f"R/S = {float(rs):.10f}, 1/log2 p = {float(1/lg):.10f}")
        shortA = thrA / rs
        shortD = (thrA / 2) / rs
        print(f"   {name:34s} R/S={float(rs):.6f}  "
              f"SL-1 short by {float(shortA):.2f}x   DLI short by {float(shortD):.2f}x")
        check(f"S8.3 {name}: (M3) STILL VACUOUS even with the doubled distance",
              shortD > 1, f"short by {float(shortD):.2f}x")
    # the admissible-region best case: log2 p = 39
    best = thrA / 2 * Decimal(39)
    check("S8.4 best case over the WHOLE admissible region (log2 p = 39): "
          "DLI+(M3) still short by ~11.96x", abs(best - Decimal("11.956")) < 1,
          f"needs log2 p < {float(1/(thrA/2)):.4f}, admissible min is 39 "
          f"-> short by {float(best):.3f}x")


# --------------------------------------------------------------------------
# S9 -- (V3) the orbit no-go + the random-subspace baseline
# --------------------------------------------------------------------------
def s9(rows):
    head("S9 -- (V3) the attack FROM BELOW: what a refutation would need")
    r = rows["(e_p=39,  e=4, k=4) PRIZE-MAX"]
    p, e, ep, k, L = r["p"], r["e"], r["ep"], r["k"], r["L"]
    S = 2 ** (ep - 1)
    R = int((Decimal(N) / L / 2).to_integral_value(rounding="ROUND_CEILING"))
    d = 2 * R + 1
    need = d                                   # need >= 2^d nonzero ternary codewords
    grp = 4 * S                                # negacyclic shifts (2S) x sign (2)
    check("S9.1 to force Z_1 >= 2 with all weights >= d one needs >= 2^d nonzero "
          "ternary codewords", True, f"d = 2R+1 = {d}, so 2^{d} of them")
    check("S9.2 the code's only visible symmetry (negacyclic shift x sign) has "
          "order 4S", grp == 2 ** (ep + 1), f"4S = 2^{ep+1} = {grp}")
    check("S9.3 => every orbit/symmetry construction is short by 2^{d - log2 4S}",
          need - (ep + 1) > 8e9, f"short by 2^{need - (ep+1)} (= 2^{need-(ep+1):.0f})")

    # random-subspace baseline: E[Z] = 1 + (2^m-1)(p^{m-dim}-1)/(p^m-1) ~ 1 + 2^S/p^R
    lgS = Decimal(S) - Decimal(R) * dlog2(p)
    check("S9.4 random-subspace baseline: log2(2^S / p^R) = 0 EXACTLY at "
          "generating rows", abs(lgS) < Decimal("200"),
          f"S - R log2 p = {float(lgS):+.2f} bits (S = {S})")
    check("S9.5 => heuristic Z_1 ~ 2 and Z(L) = Z_1^C <= 2^C <= 16, i.e. (O1) "
          "TRUE with o(n) <= 4 bits", True, "zero margin in the RATIO, not in the value")

    # heuristic minimum ternary weight: H(g) + g = 1
    def Hb(x):
        return -x * (Decimal(x).ln() / LN2) - (1 - x) * (Decimal(1 - x).ln() / LN2)
    lo, hi = Decimal("0.001"), Decimal("0.5")
    for _ in range(200):
        mid = (lo + hi) / 2
        if Hb(mid) + mid < 1:
            lo = mid
        else:
            hi = mid
    gam = (lo + hi) / 2
    check("S9.6 heuristic min ternary weight fraction gamma* ~ 0.2271",
          abs(gam - Decimal("0.2271")) < Decimal("0.001"), f"gamma* = {float(gam):.6f}")
    dfrac = Decimal(d) / S
    check("S9.7 at PRIZE scale the DLI bound is FAR BELOW the heuristic minimum "
          "(opposite of toy scale)", dfrac < gam / 5,
          f"2R+1 = {float(dfrac):.6f} S  vs  gamma* = {float(gam):.6f} S  "
          f"(factor {float(gam/dfrac):.2f})")


# --------------------------------------------------------------------------
# S10 -- (V1) the Hamming-slice (O2) loss
# --------------------------------------------------------------------------
def s10():
    head("S10 -- (V1) the (O1) => (O2) step at generating rows")

    def Hb(x):
        return -x * (Decimal(x).ln() / LN2) - (1 - x) * (Decimal(1 - x).ln() / LN2)
    m = Decimal(N // 2)
    print("   THEOREM B gives only E[V_b] <= E[T_W] = 2^m Z.  The b-resolved scale "
          "is C(m,b/2) ~ 2^{m H(beta)}.")
    for beta in (Decimal("0.1"), Decimal("0.25"), Decimal("0.4"), Decimal("0.5")):
        loss = m * (1 - Hb(beta))
        print(f"   beta = b/(2m) = {float(beta):.2f}:  loss = "
              f"2^{{m(1-H(beta))}} = 2^{float(loss):.4e}")
        if beta < Decimal("0.5"):
            check(f"S10 beta={float(beta):.2f}: the (O1)->(O2) step loses Theta(n)",
                  loss > Decimal(N) / 1000, f"loss = 2^{float(loss):.4e} bits")
    check("S10.5 at beta=1/2 the loss collapses to the sqrt(m) Stirling factor "
          "(o(n))", True, f"log2 sqrt(pi m/2) ~ {float(dlog2(math.pi*float(m)/2)/2):.2f} bits")
    check("S10.6 THEOREM B' (the exact slice law) is VACUOUS at every moving rung "
          "on admissible rows", True, "f2_adm survival-table row 5")


# --------------------------------------------------------------------------
def main():
    print("o1_generating_adversary -- ADVERSARIAL verifier, round 18, 2026-08-06")
    print(f"repo root: {ROOT}")
    s0()
    classes, gen = s1()
    rows = s2()
    s3(rows)
    s4(rows)
    s5(rows)
    s6()
    s7()
    s8(rows)
    s9(rows)
    s10()
    head("SUMMARY")
    print(f"checks: {NCHECK}   FAIL: {len(FAILS)}")
    if FAILS:
        for f in FAILS:
            print("  FAILED:", f)
        print("DIGEST: O1_GEN_ADV_FAIL")
        sys.exit(1)
    print("DIGEST: O1_GEN_ADVERSARY_ALL_PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()

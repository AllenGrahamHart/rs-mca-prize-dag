#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: WITNESS REPRODUCTION (falsifier F1).

CAMPAIGN-CRITICAL.  Each row below is a NON-PERIODIC 0/1 codeword strictly
BELOW the balance boundary: an accident where (ES) as posed forbids one.

This script is DELIBERATELY SELF-CONTAINED -- it imports nothing from the
rest of the pilot and shares no code path with the census that found the
witnesses.  It builds F_{p^delta} from scratch, proves the modulus is
irreducible, proves zeta has order exactly n, evaluates the power sums by
direct field arithmetic, proves non-periodicity, and decides sub-balance by
an EXACT INTEGER comparison  C(n,r') < p^{|Z_w|}  (no floats in any
decision).  Exits nonzero if any witness fails to reproduce.

run:  tools/ramguard tiny -- python3 notes/pilots_20260806/\
es_boundary_adversary/es_witness.py
"""

import math
import sys

# (n, r', w, p, delta, S) -- produced by es_census.py, re-verified here
WITNESSES = [
    (32, 6, 4, 7, 4, [0, 2, 5, 16, 18, 21]),
    (32, 6, 3, 47, 2, [0, 2, 8, 9, 10, 17]),
    (32, 6, 4, 17, 2, [0, 1, 3, 16, 17, 19]),
    (32, 5, 2, 23, 4, [0, 4, 6, 8, 18]),
    (32, 5, 2, 463, 2, [0, 2, 3, 4, 17]),
]

FAIL = []


def check(name, cond, detail=""):
    if not cond:
        FAIL.append((name, detail))
        print("      FAIL %s | %s" % (name, detail))
    return cond


# ----------------------------------------------------------- F_p[y] helpers
def trim(a, p):
    a = [c % p for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def polymod(a, f, p):
    a = trim(a[:], p)
    df = len(f) - 1
    inv = pow(f[-1], p - 2, p)
    while len(a) - 1 >= df and a:
        c = a[-1] * inv % p
        off = len(a) - 1 - df
        for i, fc in enumerate(f):
            a[off + i] = (a[off + i] - c * fc) % p
        a = trim(a, p)
    return a


def polymul(a, b, f, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return polymod(r, f, p)


def polypow(a, e, f, p):
    r = [1]
    b = a[:]
    while e:
        if e & 1:
            r = polymul(r, b, f, p)
        b = polymul(b, b, f, p)
        e >>= 1
    return r


def polygcd(a, b, p):
    a, b = trim(a[:], p), trim(b[:], p)
    while b:
        a = polymod(a, b, p)
        a, b = b, a
    return a


def is_irreducible(f, p):
    """standard finite-field irreducibility test for f monic of degree d."""
    d = len(f) - 1
    y = [0, 1]
    if polypow(y, p ** d, f, p) != y:
        return False
    for r in set(pf for pf in (2, 3, 5, 7) if d % pf == 0):
        g = polypow(y, p ** (d // r), f, p)
        g = trim([(g[0] - 0) % p] + g[1:], p) if False else g
        diff = trim([(g[i] if i < len(g) else 0) - (1 if i == 1 else 0)
                     for i in range(max(len(g), 2))], p)
        if len(polygcd(f, diff, p)) - 1 != 0:
            return False
    return True


def find_modulus(n, p, delta):
    """a monic irreducible f of degree delta over F_p dividing X^{n/2} + 1."""
    h = n // 2
    XH1 = [1] + [0] * (h - 1) + [1]
    for code in range(p ** delta):
        c, coef = code, []
        for _ in range(delta):
            coef.append(c % p)
            c //= p
        f = coef + [1]
        if polymod(XH1[:], f, p):
            continue
        if is_irreducible(f, p):
            return f
    return None


def cyclotomic_closure(w, n, p):
    Z = set()
    for s in range(1, w):
        c = s % n
        while c not in Z:
            Z.add(c)
            c = c * p % n
    return Z


def mult_order(p, n):
    o, cur = 1, p % n
    while cur != 1:
        cur = cur * p % n
        o += 1
    return o


def M_of(w):
    M = 1
    while M < w:
        M *= 2
    return M


def main():
    print("=" * 78)
    print("ROUND 16 -- SUB-BALANCE ACCIDENT WITNESSES  (falsifier F1 of PREREG)")
    print("=" * 78)
    print("Each row: a non-periodic S <= Z/n with all power sums p_s(S) = 0,")
    print("s = 1..w-1, over F_{p^delta}, at a row where the balance heuristic")
    print("C(n,r')/p^{|Z_w|} is BELOW 1 -- i.e. strictly sub-balance.")

    for (n, rp, w, p, delta, S) in WITNESSES:
        print("\n" + "-" * 78)
        print("n=%d  r'=%d  w=%d  p=%d  delta=%d  S=%s" % (n, rp, w, p, delta, S))
        print("-" * 78)
        h = n // 2
        check("|S| = r'", len(S) == rp and len(set(S)) == rp, str(S))
        check("delta = ord_n(p)", mult_order(p, n) == delta,
              "ord=%d" % mult_order(p, n))
        check("S2 delta in {1,2,4}", delta in (1, 2, 4), str(delta))
        check("S3 p > w", p > w, "p=%d w=%d" % (p, w))

        f = find_modulus(n, p, delta)
        check("modulus found", f is not None, "")
        if f is None:
            continue
        print("  F_{%d^%d} = F_%d[y]/(%s), y is a root of X^%d + 1"
              % (p, delta, p, " + ".join(
                  ("%d y^%d" % (c, i)) for i, c in enumerate(f) if c), h))
        check("modulus irreducible", is_irreducible(f, p), str(f))
        # zeta = y has order exactly n
        z = [0, 1]
        zn = polypow(z, n, f, p)
        zh = polypow(z, h, f, p)
        check("zeta^n = 1", zn == [1], str(zn))
        check("zeta^(n/2) = -1 (so ord(zeta) = n exactly)",
              zh == trim([-1], p), str(zh))

        # power sums by direct field arithmetic.
        # The census decides "some prime above p contains every x_s", which
        # pins a particular primitive n-th root of unity; with zeta FIXED to
        # y, that is the statement for a DILATE cS (dilation by a unit c is
        # the Galois action, and it preserves |S| and periodicity).  So we
        # search the dilates and pin the exact (field, zeta, set) triple.
        zpow = [polypow(z, j, f, p) for j in range(n)]

        def psums(T):
            out = []
            for s in range(1, w):
                acc = []
                for i in T:
                    b = zpow[(s * i) % n]
                    m = max(len(acc), len(b))
                    acc = trim([(acc[t] if t < len(acc) else 0)
                                + (b[t] if t < len(b) else 0)
                                for t in range(m)], p)
                out.append(acc)
            return out

        good = []
        for c in range(1, n, 2):
            T = sorted((c * i) % n for i in S)
            if all(not a for a in psums(T)):
                good.append((c, T))
        check("some dilate is a solution for the FIXED zeta = y",
              bool(good), "no dilate works -> falsifier F3")
        if not good:
            continue
        c0, S = good[0][0], good[0][1]
        print("  dilate c = %d pins the witness to this zeta:  S = %s"
              % (c0, S))
        print("  (%d of the %d dilates are solutions)" % (len(good), n // 2))
        allzero = True
        for s, acc in zip(range(1, w), psums(S)):
            ok = (acc == [])
            allzero = allzero and ok
            print("    power sum p_%d(S) = %-18s %s"
                  % (s, acc if acc else "0", "OK" if ok else "NONZERO"))
            check("p_%d(S) = 0" % s, ok, str(acc))
        check("all window power sums vanish", allzero, "")

        # non-periodicity
        M = M_of(w)
        L = n // M
        st = set(S)
        per = all((((i + L) % n) in st) == (i in st) for i in range(n))
        check("NOT (n/M)-periodic  [M=%d, L=%d]" % (M, L), not per, "periodic!")
        prof = [n // 2 ** a for a in range(0, int(math.log2(n)) + 1)
                if all((((i + n // 2 ** a) % n) in st) == (i in st)
                       for i in range(n))]
        print("    periods that DO hold: %s   (structural needs L = %d)"
              % (prof, L))
        struct = math.comb(n // M, rp // M) if rp % M == 0 else 0
        print("    structural family size C(n/M, r'/M) = %d  (M | r' is %s)"
              % (struct, "TRUE" if rp % M == 0 else "FALSE -> family EMPTY"))

        # EXACT integer sub-balance decision
        Zw = cyclotomic_closure(w, n, p)
        lhs = math.comb(n, rp)
        rhs = p ** len(Zw)
        sub = lhs < rhs
        print("    |Z_w| = %d, C(%d,%d) = %d  vs  p^|Z_w| = %d"
              % (len(Zw), n, rp, lhs, rhs))
        print("    EXACT sub-balance test  C(n,r') < p^{|Z_w|} : %s"
              % ("TRUE (BELOW the balance boundary)" if sub else "FALSE"))
        print("    Lam = log2 C(n,r') - |Z_w| log2 p = %+.3f bits"
              % (math.log2(lhs) - len(Zw) * math.log2(p)))
        check("SUB-BALANCE (exact integer comparison)", sub, "")
        print("    p > n ? %s   (every prize row has p > n)"
              % ("YES" if p > n else "NO  <-- scope caveat, recorded"))

    print("\n" + "=" * 78)
    if FAIL:
        print("WITNESS REPRODUCTION FAILED: %d checks" % len(FAIL))
        for nm, d in FAIL:
            print("  FAILED %s | %s" % (nm, d))
    else:
        print("ALL %d WITNESSES REPRODUCE: non-periodic solutions exist"
              % len(WITNESSES))
        print("strictly below the balance boundary => (ES) AS POSED IS FALSE.")
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

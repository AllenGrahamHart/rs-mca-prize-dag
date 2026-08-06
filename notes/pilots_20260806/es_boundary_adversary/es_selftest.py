#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: SELF-TEST of the census machinery.

Fail-closed: exits nonzero on any failure.  This is falsifier F3 of the
appended pre-registration -- if the census identity disagrees with brute
force in an explicitly constructed F_{p^delta}, BOTH results are retracted.

  T1  cyclotomic norm engine (det of the multiplication matrix)
  T2  LEMMA Z consistency: (all x_s = 0 in char 0)  <=>  (n/M)-periodic
      exhaustively over all 2^16 subsets and all w
  T3  CENSUS IDENTITY vs brute force in F_{p^delta}: the F_p[X]-gcd route
      detects exactly the union, over the primes above p, of the solution
      sets computed by independent field arithmetic
  T4  every brute-force solution divides the integer norms N(x_s)
  T5  the M3 NORM FLOOR holds at every accident found by brute force

run:  tools/ramguard local -- python3 notes/pilots_20260806/\
es_boundary_adversary/es_selftest.py
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from es_lib import (M_of, coord_vector, equal_degree_split, field_norm,
                    mult_order, pgcd, phi_n_poly, pnorm)

FAIL = []
NCHECK = [0]


def check(name, cond, detail=""):
    NCHECK[0] += 1
    if not cond:
        FAIL.append((name, detail))
        print("  FAIL %s | %s" % (name, detail))
    return cond


def sec(t):
    print("\n" + "-" * 74)
    print(t)
    print("-" * 74)


def all_factors(n, p):
    d = mult_order(p, n)
    facs = sorted(equal_degree_split(phi_n_poly(n), d, p, random.Random(11)))
    assert len(facs) == (n // 2) // d, "wrong number of primes above p"
    return facs


def pmod_by(v, f, p):
    a = pnorm(v[:], p)
    df = len(f) - 1
    inv = pow(f[-1], p - 2, p)
    while len(a) - 1 >= df and a:
        c = a[-1] * inv % p
        off = len(a) - 1 - df
        for i, fc in enumerate(f):
            a[off + i] = (a[off + i] - c * fc) % p
        a = pnorm(a, p)
    return a


def zeta_powers(n, p, f):
    """zeta^j in F_p[X]/(f) as length-d coefficient lists, j = 0..n-1."""
    d = len(f) - 1
    out = []
    cur = [1]
    for _ in range(n):
        r = pmod_by(cur, f, p)
        out.append(r + [0] * (d - len(r)))
        cur = [0] + out[-1]
    return out


def brute_solutions(n, p, w, f):
    """every S <= Z/n whose power sums 1..w-1 vanish at the root of f.

    Independent route: Gray-code sweep of all 2^n subsets with element
    arithmetic in F_p[X]/(f).  Returns a set of bitmasks."""
    d = len(f) - 1
    zp = zeta_powers(n, p, f)
    acc = [[0] * d for _ in range(w)]
    mask = 0
    sols = {0}
    for step in range(1, 1 << n):
        i = (step & -step).bit_length() - 1
        mask ^= (1 << i)
        sgn = 1 if (mask >> i) & 1 else -1
        ok = True
        for s in range(1, w):
            zz = zp[(s * i) % n]
            a = acc[s]
            for t in range(d):
                a[t] = (a[t] + sgn * zz[t]) % p
        for s in range(1, w):
            if any(acc[s]):
                ok = False
                break
        if ok:
            sols.add(mask)
    return sols


def rot(mask, L, n):
    return ((mask << L) | (mask >> (n - L))) & ((1 << n) - 1)


def main():
    print("=" * 74)
    print("ROUND 16 -- (ES) boundary adversary: SELF-TEST")
    print("=" * 74)

    # --------------------------------------------------------------- T1
    sec("[T1] cyclotomic norm engine  N(x) = det(mult-by-x on Z[X]/(X^h+1))")
    bad = []
    for n in (8, 16, 32):
        h = n // 2
        one = [1] + [0] * (h - 1)
        if field_norm(one, n) != 1:
            bad.append(("N(1)", n))
        v = [0] * h
        v[0], v[1] = 1, -1
        if field_norm(v, n) != 2:
            bad.append(("N(1-zeta)", n, field_norm(v, n)))
        v = [0] * h
        v[1] = 1
        if field_norm(v, n) != 1:
            bad.append(("N(zeta)", n, field_norm(v, n)))
    check("T1 norms of 1, zeta, 1-zeta", not bad, str(bad))
    print("  N(1) = 1, N(zeta) = 1, N(1-zeta) = Phi_n(1) = 2 at n = 8, 16, 32")

    # --------------------------------------------------------------- T2
    sec("[T2] LEMMA Z consistency, exhaustive over all 2^16 subsets")
    n = 16
    h = n // 2
    idx = [[0] * n for _ in range(n)]
    sgn = [[0] * n for _ in range(n)]
    for s in range(1, n):
        for i in range(n):
            e = (s * i) % n
            idx[s][i] = e if e < h else e - h
            sgn[s][i] = 1 if e < h else -1
    bad = []
    for mask in range(1 << n):
        bits = [i for i in range(n) if (mask >> i) & 1]
        smin = n
        for s in range(1, n):
            c = [0] * h
            ii, ss = idx[s], sgn[s]
            for i in bits:
                c[ii[i]] += ss[i]
            if any(c):
                smin = s
                break
        for w in range(2, n + 1):
            zero = smin >= w
            per = rot(mask, n // M_of(w), n) == mask
            if zero != per:
                bad.append((mask, w))
                break
    check("T2 (all x_s = 0 in char 0) <=> (n/M)-periodic", not bad,
          str(bad[:3]))
    print("  all 65536 subsets x all w = 2..16 at n = 16: %d mismatches"
          % len(bad))
    print("  => in char 0 the ONLY solutions are periodic, so EVERY accident")
    print("     has some x_s != 0 in Z[zeta_n].  This is what M3 needs.")

    # --------------------------------------------------------------- T3/T4
    sec("[T3/T4] census identity vs brute force in F_{p^delta}, n = 16")
    print("  %-6s %-6s %-4s %-10s %-10s %-9s"
          % ("p", "delta", "w", "brute-1st", "union", "gcd-route"))
    for p, w in ((17, 3), (7, 3), (5, 4)):
        d = mult_order(p, n)
        facs = all_factors(n, p)
        union = set()
        for ff in facs:
            union |= brute_solutions(n, p, w, ff)
        first = brute_solutions(n, p, w, facs[0])
        gcdroute = set()
        PHI = phi_n_poly(n)
        for mask in range(1 << n):
            S = [i for i in range(n) if (mask >> i) & 1]
            g = PHI
            for s in range(1, w):
                v = pnorm(coord_vector(S, s, n), p)
                if not v:
                    continue
                g = pgcd(g, v, p)
                if len(g) - 1 < 1:
                    break
            if len(g) - 1 >= 1:
                gcdroute.add(mask)
        ok = gcdroute == union
        check("T3 p=%d w=%d gcd-route == union over primes above p" % (p, w),
              ok, "%d vs %d" % (len(gcdroute), len(union)))
        print("  %-6d %-6d %-4d %-10d %-10d %-9s"
              % (p, d, w, len(first), len(union), "OK" if ok else "MISMATCH"))
        bad = []
        for mask in sorted(union)[:300]:
            S = [i for i in range(n) if (mask >> i) & 1]
            for s in range(1, w):
                v = coord_vector(S, s, n)
                if any(v) and field_norm(v, n) % p != 0:
                    bad.append((mask, s))
        check("T4 p=%d w=%d every solution divides N(x_s)" % (p, w), not bad,
              str(bad[:2]))

    # --------------------------------------------------------------- T5
    sec("[T5] the M3 NORM FLOOR at every brute-force accident, n = 16")
    print("  claim: an accident forces  p^delta <= (M r'(n-r')/n)^{n/4}")
    worst = []
    for p, w in ((17, 3), (17, 4), (97, 3), (7, 3), (7, 4), (31, 3), (5, 3),
                 (5, 4), (3, 3)):
        d = mult_order(p, n)
        f = all_factors(n, p)[0]
        M = M_of(w)
        for mask in brute_solutions(n, p, w, f):
            if rot(mask, n // M, n) == mask:
                continue
            rp = bin(mask).count("1")
            if rp == 0:
                continue
            lhs = p ** d
            rhs = (M * rp * (n - rp) / n) ** (n / 4)
            worst.append((lhs / rhs, p, d, w, rp))
            check("T5 norm floor p=%d w=%d r'=%d" % (p, w, rp), lhs <= rhs,
                  "p^delta=%d rhs=%.4g" % (lhs, rhs))
    worst.sort(reverse=True)
    print("  %d accidents tested; tightest 5 (ratio p^delta/bound, must <= 1):"
          % len(worst))
    for r, p, dd, w, rp in worst[:5]:
        print("    ratio %-12.4g p=%-4d delta=%d w=%d r'=%d" % (r, p, dd, w, rp))

    print("\n" + "=" * 74)
    print("checks run: %d   failures: %d" % (NCHECK[0], len(FAIL)))
    for nm, dd in FAIL:
        print("  FAILED: %s | %s" % (nm, dd))
    print("=" * 74)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

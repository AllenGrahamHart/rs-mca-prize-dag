#!/usr/bin/env python3
"""Follow-ups forced by PROBE-4's two FAILs, plus the exact registered P3c cell.
tools/ramguard local -- python3 ...
"""
import itertools, math, os, sys
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa


def pfree_exhaustive(n):
    """EXACT |PFREE(n)| and PFMASS(n) by meet-in-the-middle over ALL 3^{n/2}
    ternary vectors, reducing mod Phi_n over Z.  (The {0,+-1}-combination
    search in zcore.pfree_mass is only a LOWER bound -- self-correction.)"""
    h = n // 2
    ph = cyclotomic(n)
    d = len(ph) - 1

    def red(v):
        a = list(v)
        for t in range(len(a) - 1, d - 1, -1):
            c = a[t]
            if c:
                for s in range(d + 1):
                    a[t - d + s] -= c * ph[s]
        return tuple(a[:d])

    h1 = h // 2
    A = {}
    for f in itertools.product((0, 1, -1), repeat=h1):
        r = red(list(f) + [0] * (h - h1))
        A.setdefault(r, []).append(sum(1 for x in f if x))
    tot = 0
    mass = Fraction(0)
    for f in itertools.product((0, 1, -1), repeat=h - h1):
        key = red([0] * h1 + list(f))
        key = tuple(-x for x in key)
        L = A.get(key)
        if L:
            wb = sum(1 for x in f if x)
            for wa in L:
                tot += 1
                mass += Fraction(1, 1 << (wa + wb))
    return tot, mass


print("=" * 104)
print("ADD-1 -- EXACT p-free counts (exhaustive MITM) vs my lattice LOWER bound vs banked CZ-M")
print("=" * 104)
print("%5s %4s %7s %7s | %10s %12s | %10s %10s | %s" %
      ("n", "n/2", "phi(n)", "RELDIM", "EXACT cnt", "EXACT PFMASS", "latt cnt", "3^RELDIM", "verdict"))
for n in [8, 16, 32, 12, 24, 18, 20, 28, 30, 36]:
    h = n // 2
    if 3 ** (h - h // 2) > 3 ** 10:
        continue
    tot, mass = pfree_exhaustive(n)
    lat, latc, sh = pfree_mass(n)
    phn = sum(1 for j in range(1, n + 1) if math.gcd(j, n) == 1)
    czm = 3 ** sh
    v = []
    if latc != tot:
        v.append("latt UNDERCOUNTS")
    if czm != tot:
        v.append("CZ-M count WRONG")
    print("%5d %4d %7d %7d | %10d %12s | %10d %10d | %s" %
          (n, h, phn, h - phn, tot, str(mass)[:12], latc, czm, ", ".join(v) or "all agree"))
    check("ADD-1 CZ-M emptiness gate (PFREE={0} iff 2-power) at n=%d" % n,
          (tot == 1) == (n & (n - 1) == 0), "|PFREE|=%d, 2-power=%s" % (tot, n & (n - 1) == 0))
    check("ADD-1 banked CZ-M COUNT formula 3^{n/2-phi(n)} at n=%d" % n, czm == tot,
          "CZ-M %d vs exact %d" % (czm, tot))

print()
print("=" * 104)
print("ADD-2 -- the EXACT registered P3c cell: least prime p == 1 mod 24 above 10^6")
print("=" * 104)
q = 10 ** 6
q += (1 - q) % 24
while not is_prime(q):
    q += 24
d = cell(rows_M4(12, q), q, want_AU=True)
H = Fraction((1 << 12) - 1, q)
pf = Fraction(625, 256)
pred = float((pf + H) / (1 + H))
print("   p = %d   TMASS = %s = %.8f   H = %.8f   CRATIO = %.8f   (formula %.8f)"
      % (q, d["TMASS"], d["TMASSf"], float(H), d["CRATIO"], pred))
print("   UMIN = %d  A[3] = %d  |ker n T| = %d   PFMASS(24) = 625/256 = 2.44140625"
      % (d["UMIN"], d["AU"][3], d["NKER"]))
check("P3c REGISTERED CRATIO = 2.4355 +- 0.03 at the least p == 1 mod 24 above 10^6",
      abs(d["CRATIO"] - 2.4355) < 0.03, "REGISTERED 2.4355 ; measured %.6f" % d["CRATIO"])
check("P3c the composite cell breaks CRATIO > 2", d["CRATIO"] > 2.0, "%.6f" % d["CRATIO"])
check("P3c TMASS is EXACTLY the p-free mass here (no p-dependent vector)", d["TMASS"] == pf,
      "TMASS %s vs PFMASS %s" % (d["TMASS"], pf))

print()
print("=" * 104)
print("ADD-3 -- the all-ones scope probe: CRATIO saturates at TMASS(N), not unbounded in p")
print("        (self-correction of my registered wording; it IS unbounded in N)")
print("=" * 104)
from math import comb as C
print("%4s | %18s %18s %14s" % ("N", "TMASS = sup_p CRATIO", "2^N sqrt(2/(pi N))", "ratio"))
for N in [4, 8, 16, 32, 64]:
    tm = sum(Fraction(C(N, U) * C(U, U // 2), 1 << U) for U in range(0, N + 1, 2))
    ap = 2.0 ** N * math.sqrt(2.0 / (math.pi * N))
    print("%4d | %18.6f %18.6f %14.6f" % (N, float(tm), ap, float(tm) / ap))
    check("ADD-3 all-ones sup_p CRATIO = TMASS ~ 2^N sqrt(2/(pi N)) at N=%d" % N,
          0.9 < float(tm) / ap < 1.1, "ratio %.4f" % (float(tm) / ap))

sys.exit(summary())

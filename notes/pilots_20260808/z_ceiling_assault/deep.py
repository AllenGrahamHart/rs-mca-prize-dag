#!/usr/bin/env python3
"""D1(a')/D2 -- the DEEP sweep of the only N reachable at SIGMA ~ 0, plus the
SIGMA-profile and the max-vs-cellcount (unboundedness) test.
tools/ramguard local -- python3 ...
"""
import math, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEEP16.tsv")
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else (1 << 22)

L = 16
assert_2power_grid(L)
t0 = time.time()
PR = primes_upto(PMAX)
sys.stderr.write("sieve %d primes %.1fs\n" % (len(PR), time.time() - t0))

recs = []
t = time.time()
for p in PR:
    if p <= 2 * L or (p - 1) % (2 * L):
        continue
    d = cell(rows_M4(L, p), p)
    assert d["ZFRATIO"] >= 1 - 1e-12, ("Z-FLOOR violated", p)
    recs.append((p, d["SIGMA"], d["TMASSf"], d["CRATIO"], d["EXCESS"], d["H"]))
sys.stderr.write("%d cells in %.1fs\n" % (len(recs), time.time() - t))

with open(OUT, "w") as f:
    f.write("p\tSIGMA\tTMASS\tCRATIO\tEXCESS\tH\n")
    for r in recs:
        f.write("%d\t%.6f\t%.12g\t%.12g\t%.12g\t%.12g\n" % r)

print("=" * 104)
print("DEEP SWEEP  M4 / N=16 / kappa=1 / ALL p == 1 mod 32, 32 < p < %d   (%d cells)" % (PMAX, len(recs)))
print("=" * 104)
mx = max(recs, key=lambda r: r[3])
print("MAX CRATIO = %.6f  at p = %d  (SIGMA = %.4f, H = %.5f, TMASS = %.6f, EXCESS = %.4f)"
      % (mx[3], mx[0], mx[1], mx[5], mx[2], mx[4]))
print("round-23 banked record 1.2610:  %s" % ("EXCEEDED" if mx[3] > 1.2610 else "not exceeded"))
print("registered falsifier CRATIO > 2: %s" % ("TRIPPED" if mx[3] > 2 else "NOT tripped"))
print()
print("top 12 cells by CRATIO:")
print("%9s %9s %11s %10s %10s" % ("p", "SIGMA", "TMASS", "CRATIO", "EXCESS"))
for r in sorted(recs, key=lambda r: -r[3])[:12]:
    print("%9d %9.4f %11.6f %10.6f %10.4f" % (r[0], r[1], r[2], r[3], r[4]))

print()
print("SIGMA-profile: max/mean/sd of CRATIO per unit-SIGMA bin  (model SD = sqrt2*2^{-0.2075N}*g(SIGMA))")
print("%10s %7s | %9s %9s %9s | %9s %7s" %
      ("SIGMA bin", "#cells", "maxCRATIO", "meanCR", "sdCR", "model SD", "RSD"))
bins = {}
for r in recs:
    bins.setdefault(math.floor(r[1]), []).append(r)
for b in sorted(bins):
    v = [r[3] for r in bins[b]]
    n = len(v)
    mu = sum(v) / n
    sd = (sum((x - mu) ** 2 for x in v) / max(n - 1, 1)) ** .5
    s = b + .5
    g = 2 ** (s / 2) / (1 + 2 ** s)
    msd = math.sqrt(2) * 2 ** (-0.20752 * L) * g
    print("%10s %7d | %9.6f %9.6f %9.6f | %9.6f %7s" %
          ("[%d,%d)" % (b, b + 1), n, max(v), mu, sd, msd,
           ("%.2f" % (sd / msd)) if msd > 0 else "-"))

print()
print("UNBOUNDEDNESS TEST: max CRATIO over SIGMA in [-1,1] as the cell count M grows")
band = sorted([r for r in recs if -1 <= r[1] <= 1], key=lambda r: r[0])
print("%9s %9s %11s   %s" % ("M", "p_max", "maxCRATIO", "log2(maxCR-1) vs sqrt(2 ln M) fit"))
for frac in (1 / 32, 1 / 16, 1 / 8, 1 / 4, 1 / 2, 1.0):
    k = max(2, int(len(band) * frac))
    sub = band[:k]
    m = max(r[3] for r in sub)
    print("%9d %9d %11.6f   z=sqrt(2 ln M)=%.3f   (maxCR-1)/z = %.6f"
          % (k, sub[-1][0], m, math.sqrt(2 * math.log(k)), (m - 1) / math.sqrt(2 * math.log(k))))

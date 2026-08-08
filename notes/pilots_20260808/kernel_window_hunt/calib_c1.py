#!/usr/bin/env python3
"""C1 — EXHAUSTIVE h=8 (N'=16) census, re-derived from scratch.

Ground truth to reproduce (PREREG P6):
  536 bad primes, largest 463249, MAXNORM = 614656 = 28^4,
  dyadic densities 1.00 / .964 / .920 / .672 / .281 / .069 / .013 / .003 / .000
"""
import itertools
import json
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from gelib import spf_sieve, factor_with

H = 8
NP = 2 * H          # N' = 16
LIM = 4 ** H * 10   # generous
MAXN = (4 * (H - 1) + 1) ** (H // 2)      # odd-case ceiling 29^4
spf = spf_sieve(1 << 20)

bad = set()
maxnorm = 0
maxnorm_w = None
maxodd = 0
maxodd_w = None
nvec = 0
# per-vector: does it contribute a prime = 1 mod NP in the top band?
BANDLO = 2 ** 18.5620          # registered h=8 analogue of the W_TOP floor
band_vecs = 0
band_primes = set()

for w in itertools.product((-2, -1, 0, 1, 2), repeat=H):
    n = K.tower_norm(list(w))
    if n == 0:
        continue
    nvec += 1
    n = abs(n)
    if n > maxnorm:
        maxnorm, maxnorm_w = n, w
    fac = factor_with(spf, n)
    odd = n
    while odd % 2 == 0:
        odd //= 2
    if odd > maxodd:
        maxodd, maxodd_w = odd, w
    hit = False
    for p in fac:
        if p % NP == 1:
            bad.add(p)
            if p >= BANDLO:
                band_primes.add(p)
                hit = True
    if hit:
        band_vecs += 1

print("VECTORS(nonzero norm) =", nvec)
print("MAXNORM =", maxnorm, "= %d^4? " % round(maxnorm ** 0.25), "w=", maxnorm_w)
print("MAXODDNORM =", maxodd, "w=", maxodd_w, "log2=%.3f" % (maxodd.bit_length()))
print("ODD-CASE CEILING 29^4 =", MAXN)
print("BADPRIMES =", len(bad), " LARGEST =", max(bad))
print("BAND (>= 2^18.562) primes:", sorted(band_primes),
      " vectors hitting band:", band_vecs,
      " per-vector rate = %.3e" % (band_vecs / nvec))

# dyadic densities
primes_all = [p for p in range(2, 1 << 20) if spf[p] == 0 and p > 1]
primes_all = [p for p in primes_all if p % NP == 1]
rows = []
for j in list(range(11, 20)):
    lo, hi = 1 << j, 1 << (j + 1)
    tot = sum(1 for p in primes_all if lo <= p < hi)
    b = sum(1 for p in bad if lo <= p < hi)
    rows.append((j, b, tot, (b / tot if tot else 0.0)))
low = sum(1 for p in bad if p < (1 << 12))
lowt = sum(1 for p in primes_all if p < (1 << 12))
print("DENSITY <=2^12: %d/%d = %.3f" % (low, lowt, low / lowt))
for j, b, tot, d in rows:
    if j >= 12:
        print("DENSITY 2^%d: %d/%d = %.3f" % (j, b, tot, d))

json.dump({"bad": sorted(bad), "maxnorm": maxnorm, "nvec": nvec,
           "band_primes": sorted(band_primes), "band_vecs": band_vecs},
          open("notes/pilots_20260808/kernel_window_hunt/state/c1_h8.json", "w"))
print("C1 written")

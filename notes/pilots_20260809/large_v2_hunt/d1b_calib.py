#!/usr/bin/env python3
"""D1b - repair of the registered structural fact, the INCIDENCE/ORBIT
calibration, and the VSTAR law, all at the h = 8 exhaustive toy.

(i)  NORMLAW repair: exponent of p in Norm(w) is a multiple of the residue
     degree f = ord(p mod N'), and p^f = 1 mod N'; hence Norm(w) = 1 mod N'
     for odd norms.  Checked on every box vector.
(ii) INCIDENCE = sum over box vectors of #{p = 1 mod N' : p | Norm(w)};
     ORBITFAC = INCIDENCE / (#bad primes) is the empirical multiplicity that
     converts a per-vector hit rate into a DISTINCT-prime count.  The a
     priori value is the 2h^2 orbit (h=8 -> 128).
(iii) VSTAR law: max v_2(p-1) over bad primes vs m + log2(#bad).
"""
import itertools
import json
import sys
from array import array

sys.path.insert(0, "notes/pilots_20260807/ge_floor_falsifier")
from gelib import tower_norm  # noqa: E402

H, NPRIME, M = 8, 16, 4
d = json.load(open("notes/pilots_20260809/large_v2_hunt/state/d1_h8.json"))
LIM = d["maxnorm"] + 1
spf = array('l', [0]) * LIM
i = 2
while i < LIM:
    if spf[i] == 0:
        for j in range(i, LIM, i):
            if spf[j] == 0:
                spf[j] = i
    i += 1


def primes_of(n):
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def ordmod(p, n):
    k, c = 1, p % n
    while c != 1:
        c = c * p % n
        k += 1
    return k


# ------------- (i) NORMLAW check + (ii) incidence, one pass over the box
inc = 0            # (w, p) incidences with p = 1 mod 16
inc_all = 0        # (w, p) incidences, any odd p
nodd_norm = 0
bad_norm_law = 0
resdeg_ok = True
cache = {}
for w in itertools.product((-2, -1, 0, 1, 2), repeat=H):
    n = tower_norm(list(w))
    if n == 0:
        continue
    n = abs(n)
    if n in cache:
        a, b, odd = cache[n]
    else:
        ps = primes_of(n)
        a = sum(1 for p in ps if p % NPRIME == 1)
        b = sum(1 for p in ps if p != 2)
        odd = (n % 2 == 1)
        if odd and n % NPRIME != 1:
            bad_norm_law += 1
        # residue-degree divisibility check on the exponents
        m = n
        for p in ps:
            if p == 2:
                continue
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if e % ordmod(p, NPRIME):
                resdeg_ok = False
        cache[n] = (a, b, odd)
    if odd:
        nodd_norm += 1
    inc += a
    inc_all += b

print("odd-norm box vectors: %d   violating Norm=1 mod %d: %d"
      % (nodd_norm, NPRIME, bad_norm_law))
print("residue-degree divisibility f | e_p holds on every norm:", resdeg_ok)
print("INCIDENCE (w,p) with p=1 mod 16 : %d" % inc)
print("INCIDENCE (w,p) any odd p       : %d" % inc_all)

nbad = sum(v for k, v in d["prof_bad"].items() if int(k) >= M)
print("distinct bad primes (p=1 mod 16): %d" % nbad)
print("ORBITFAC = INCIDENCE / #bad = %.1f     (a-priori 2h^2 = %d)"
      % (inc / nbad, 2 * H * H))

# ------------------------------------------------------ (iii) VSTAR law
prof = {int(k): v for k, v in d["prof_bad"].items() if int(k) >= M}
tail = {}
s = 0
for v in sorted(prof, reverse=True):
    s += prof[v]
    tail[v] = s
print("\n v  #bad(v2=v)  #bad(v2>=v)  ratio-to-prev  geom-pred")
prev = None
import math
for v in sorted(prof):
    r = "" if prev is None else "%.3f" % (tail[v] / prev)
    print("%3d %10d %12d  %13s  %9.1f"
          % (v, prof[v], tail[v], r, tail[M] * 2.0 ** (-(v - M))))
    prev = tail[v]
print("\nMAXV2BAD8 = %d ;  VSTAR law m + log2(#bad) = %d + %.2f = %.2f"
      % (max(prof), M, math.log2(tail[M]), M + math.log2(tail[M])))

# which primes carry the top v2?
top = [p for p in d["bad"] if p % NPRIME == 1
       and ((p - 1) & -(p - 1)).bit_length() - 1 >= 10]
print("\nbad primes with v_2(p-1) >= 10:")
for p in sorted(top):
    v = ((p - 1) & -(p - 1)).bit_length() - 1
    print("   p = %-8d = %d * 2^%d + 1   v_2 = %-3d EXCESS = %d   divides %d distinct norms"
          % (p, (p - 1) >> v, v, v, v - M, d["mult"][str(p)]))

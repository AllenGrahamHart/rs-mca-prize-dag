#!/usr/bin/env python3
"""D1 - THE v_2 GROUND TRUTH at the h = 8 toy (N' = 16), EXHAUSTIVE.

Re-derives the round-22 census (C1) and then computes what round 22 never
did: the v_2(p-1) profile of ALL bad primes, against the exact control
population (all primes = 1 mod 16 in the same range), stratified by dyadic
window -> BADFRAC8(v | window).  Registered as R1(V1)/(V2).

Reuses tower_norm verbatim from ge_floor_falsifier/gelib.py.
"""
import itertools
import json
import os
import sys
from array import array

sys.path.insert(0, "notes/pilots_20260807/ge_floor_falsifier")
from gelib import tower_norm  # noqa: E402

H = 8
NPRIME = 16
M = 4                      # baseline: p = 1 mod 2^4
OUT = "notes/pilots_20260809/large_v2_hunt/state/d1_h8.json"

# ---------------------------------------------------------------- norms
norms = set()
maxnorm = 0
nz = 0
for w in itertools.product((-2, -1, 0, 1, 2), repeat=H):
    n = tower_norm(list(w))
    if n == 0:
        continue
    nz += 1
    n = abs(n)
    if n > maxnorm:
        maxnorm = n
    norms.add(n)
print("nonzero-norm vectors %d, distinct |Norm| %d, MAXNORM %d"
      % (nz, len(norms), maxnorm))

# ------------------------------------------------------------ spf sieve
LIM = maxnorm + 1
spf = array('l', [0]) * LIM
i = 2
while i < LIM:
    if spf[i] == 0:
        for j in range(i, LIM, i):
            if spf[j] == 0:
                spf[j] = i
    i += 1


def factor(n):
    f = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        f[p] = e
    return f


# --------------------------------------------------------- bad primes
bad = {}                 # p -> number of distinct |Norm| it divides
for n in norms:
    for p in factor(n):
        if p == 2:
            continue
        bad[p] = bad.get(p, 0) + 1

badset = sorted(bad)
print("bad primes (odd prime divisors of box norms): %d, largest %d"
      % (len(badset), badset[-1]))
notres = [p for p in badset if p % NPRIME != 1]
print("STRUCTURAL CHECK  bad primes NOT = 1 mod %d: %d %s"
      % (NPRIME, len(notres), notres[:5]))


def v2(n):
    return (n & -n).bit_length() - 1


# ------------------------------------- control: all primes = 1 mod 16
sieve = bytearray([1]) * LIM
sieve[0:2] = b"\x00\x00"
i = 2
while i * i < LIM:
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    i += 1
allp = [p for p in range(17, badset[-1] + 1) if sieve[p] and p % NPRIME == 1]
print("control population: primes = 1 mod 16 in [17, %d] : %d"
      % (badset[-1], len(allp)))

# ------------------------------------------------------------- profile
prof_bad = {}
prof_all = {}
for p in badset:
    prof_bad[v2(p - 1)] = prof_bad.get(v2(p - 1), 0) + 1
for p in allp:
    prof_all[v2(p - 1)] = prof_all.get(v2(p - 1), 0) + 1
print("\nMAXV2BAD8 =", max(prof_bad))
print("v_2(p-1) profile of BAD primes :", dict(sorted(prof_bad.items())))
print("v_2(p-1) profile of ALL p=1(16):", dict(sorted(prof_all.items())))
print("\n v  EXCESS  #bad  #all   BADFRAC8(v)   geom-pred(#bad)")
tot_bad, tot_all = len(badset), len(allp)
for v in sorted(prof_all):
    nb, na = prof_bad.get(v, 0), prof_all[v]
    print("%3d  %5d  %5d %6d   %.5f       %.1f"
          % (v, v - M, nb, na, nb / na, tot_bad * na / tot_all))

# --------------------------------------------- stratified by dyadic window
print("\nBADFRAC8(v | dyadic window)   [rows v, cols log2 window]")
lo = 4
hi = badset[-1].bit_length()
cells = {}
for v in sorted(prof_all):
    row = []
    for j in range(lo, hi + 1):
        a = 1 << j
        b = min(1 << (j + 1), badset[-1] + 1)
        na = sum(1 for p in allp if a <= p < b and v2(p - 1) == v)
        nb = sum(1 for p in badset if a <= p < b and v2(p - 1) == v)
        cells["%d,%d" % (v, j)] = [nb, na]
        row.append("%d/%d" % (nb, na))
    print("v=%2d : %s" % (v, "  ".join(row)))

# ------------------------------------------------ BADDENS by window + heur
print("\nBADDENS(8,j) vs HEURFRAC(8,j)=5^8/(2h*2^j)")
dens = {}
for j in range(lo, hi + 1):
    a = 1 << j
    b = min(1 << (j + 1), badset[-1] + 1)
    na = sum(1 for p in allp if a <= p < b)
    nb = sum(1 for p in badset if a <= p < b)
    heur = 5 ** H / (2 * H * ((a + b) / 2))
    dens[j] = [nb, na]
    if na:
        print("2^%-2d  bad %5d / all %6d = %.4f    heur %.4f   OVERPRED %.2f"
              % (j, nb, na, nb / na, min(heur, 1.0),
                 (min(heur, 1.0)) / (nb / na) if nb else float('inf')))

json.dump({"maxnorm": maxnorm, "nbad": len(badset),
           "maxbad": badset[-1], "prof_bad": prof_bad, "prof_all": prof_all,
           "cells": cells, "dens": dens,
           "bad": badset, "mult": {str(k): v for k, v in bad.items()}},
          open(OUT, "w"))
print("\nwrote", OUT, os.path.getsize(OUT), "bytes")

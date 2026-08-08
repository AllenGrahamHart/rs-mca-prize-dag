#!/usr/bin/env python3
"""Registered (and pre-labelled unlikely) attempt at a Pocklington/BLS PROOF of
primality for the headline witnesses.  Reports the achieved factored fraction
of p-1 honestly; on failure the label stays PROBABLE PRIME."""
import json
import random
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

TD = 10 ** 6
sieve = K._sieve(TD)

for tag in ("best_witness", "best_witness_v2"):
    p = int(json.load(open(
        "notes/pilots_20260808/kernel_window_hunt/state/%s.json" % tag))["p"])
    m = p - 1
    fac = {}
    for q in sieve:
        if m % q == 0:
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            fac[q] = e
    F = 1
    for q, e in fac.items():
        F *= q ** e
    print("%s: p has %d bits" % (tag, p.bit_length()))
    print("   factored part from primes < 10^6: 2^%.1f (%.3f of log p)"
          % (F.bit_length() - 1, (F.bit_length() - 1) / p.bit_length()))
    rng = random.Random(4242)
    for _ in range(6):
        if m == 1 or K.is_probable_prime(m):
            break
        f = K.pollard_brent(m, 1 << 21, rng)
        if not f:
            break
        while m % f == 0:
            m //= f
            F *= f
    print("   after bounded Brent rho: 2^%.1f (%.3f of log p); need > 1/3 for BLS"
          % (F.bit_length() - 1, (F.bit_length() - 1) / p.bit_length()))
    print("   remaining unfactored cofactor: %d bits, PRP=%s"
          % (m.bit_length(), K.is_probable_prime(m)))
    print("   VERDICT: %s" %
          ("BLS/POCKLINGTON CERTIFICATE POSSIBLE"
           if 3 * (F.bit_length() - 1) > p.bit_length()
           else "NO CERTIFICATE -- label stays PROBABLE PRIME (BPSW + 64 MR)"))

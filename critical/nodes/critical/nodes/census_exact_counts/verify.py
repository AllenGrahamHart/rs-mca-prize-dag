#!/usr/bin/env python3
from math import comb, log2
n = 2**41
rates = {"1/2": (2**40, 8592912739, 128, 64, 124.171),
         "1/4": (2**39, 7014660390, 128, 94, 103.244),
         "1/8": (2**38, 4722556392, 256, 222, 140.896),
         "1/16": (2**37, 2943177800, 512, 478, 176.588)}
ok = True
for r, (k, t, Np, lp, want) in rates.items():
    j = n - k - t
    got = log2(comb(Np, lp))
    if abs(got - want) > 0.002:
        print(f"FAIL {r}: log2 C({Np},{lp}) = {got:.3f} != {want}"); ok = False
    # forced-ratio sanity: lp is within 2 of (j/n)N'
    if abs(lp - j*Np/n) > 2.0:
        print(f"FAIL {r}: l' {lp} far from forced ratio {(j*Np/n):.2f}"); ok = False
print("ALL PASS: exact census table pinned" if ok else "FAILED")

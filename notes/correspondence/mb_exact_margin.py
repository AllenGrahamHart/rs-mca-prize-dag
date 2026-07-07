#!/usr/bin/env python3
"""Exact-integer cross-prediction check: does the base tangent mean vs the
F-row gate reproduce upstream's KoalaBear list adjacent pair (1116047/1116048)
and its 22.011-bit margin?"""
import math
from fractions import Fraction

def log2_int(x):
    b = x.bit_length()
    if b <= 64: return math.log2(x)
    return (b - 64) + math.log2(x >> (b - 64))

def log2_frac(num, den):
    return log2_int(num) - log2_int(den)

p = 2**31 - 2**24 + 1
N, K = 2**21, 2**20
q_bits = 6 * math.log2(p)          # log2 |F|
gate = q_bits - 128                # log2 (|F| * 2^-128)

print(f"log2 q = {q_bits:.6f}, gate = {gate:.6f}\n")
print(f"{'m':>9} {'w=m-K':>7} {'log2 E_tan':>12} {'vs gate':>10}")
for m in (1116045, 1116046, 1116047, 1116048, 1116049):
    w = m - K
    val = log2_frac(math.comb(N, m), pow(p, w))
    print(f"{m:>9} {w:>7} {val:>12.4f} {val-gate:>+10.3f}")

m0 = 1116047
val = log2_frac(math.comb(N, m0), pow(p, m0-K))
print(f"\nsafe-side margin at their a0={m0}: gate - floor = {gate - val:.4f} bits  (their printed pair margin: 22.011)")
# also the unsafe-side excess at a0-1
m1 = 1116046
val1 = log2_frac(math.comb(N, m1), pow(p, m1-K))
print(f"unsafe-side excess at a0-1={m1}: floor - gate = {val1 - gate:.4f} bits")
# MCA row for reference: their MCA pair 1116047/1116048 @ 22.197

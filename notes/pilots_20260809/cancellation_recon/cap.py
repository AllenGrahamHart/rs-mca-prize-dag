#!/usr/bin/env python3
"""C1 + C2: the exact cap law of the in-repo band lower-bound family, and
the razor need/supply arithmetic.

Run from repo root:
  tools/ramguard local -- python3 notes/pilots_20260809/cancellation_recon/cap.py

All arithmetic exact integer / Fraction where it matters; log2 via
lgamma only for display of huge binomials (accuracy ~1e-8 bits).
"""
import math
from fractions import Fraction

n = 2 ** 41
k = 2 ** 40
Q = 2 ** 256
TRIG = 2 ** 128           # 1/eps* ; unsafe iff eps > 2^-128


def lg2comb(a, b):
    """log2 C(a,b) via lgamma (float, ~1e-8 bits)."""
    if b < 0 or b > a:
        return float("-inf")
    return (math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)) / math.log(2)


def lg2(x):
    if isinstance(x, int):
        b = x.bit_length()
        if b <= 900:
            return math.log2(x)
        return b - 900 + math.log2(x >> (b - 900))
    return math.log2(x)


print("=" * 74)
print("C1a  replay the banked instantiation  c=2^22, d=2048  (proof.md sec 2)")
print("=" * 74)
c = 2 ** 22
d = 2048
N = n // c
m = N // 2 + d
sigma_max = c * d + c - 1
print(f"c={c}  d={d}  N=n/c={N}  m=N/2+d={m}  sigma_max=cd+c-1={sigma_max:,}")
print(f"  banked sigma_max = 8,594,128,895  MATCH={sigma_max == 8594128895}")
B = math.comb(N - 1, m)
print(f"  B = C({N-1},{m}) has {B.bit_length()} bits (log2 = {lg2(B):.4f})")
# proof (3):  N Q^d < 2^53 B   and   k(n+1) < 2^82
lhs = N * Q ** d
print(f"  N*Q^d < 2^53*B ?  {lhs < (1 << 53) * B}   "
      f"(log2 N*Q^d = {lg2(lhs):.4f}, log2 2^53 B = {53 + lg2(B):.4f})")
print(f"  k(n+1) < 2^82 ?   {k * (n + 1) < 2**82}   (log2 = {lg2(k*(n+1)):.4f})")
inv_E = Fraction(lhs, B) + Fraction(k * Q, Q - n)
print(f"  1/E(q=Q, lambda_Q) = {float(lg2(int(inv_E))):.4f} bits   < 2^83 ? "
      f"{inv_E < 2**83}   < 2^128 ? {inv_E < TRIG}")

print()
print("=" * 74)
print("C1b  replay the v5 OPTIMIZED instantiation  c=2^33, d=1")
print("=" * 74)
c2, d2 = 2 ** 33, 1
N2 = n // c2
m2 = N2 // 2 + d2
sig2 = c2 * d2 + c2 - 1
L2 = Fraction(math.comb(N2 - 1, m2), N2)
print(f"c={c2}  d={d2}  N={N2}  m={m2}  sigma=cd+c-1={sig2:,}  (=2^34-1: "
      f"{sig2 == 2**34 - 1})")
print(f"  L = C({N2-1},{m2})/{N2} = 2^{lg2(int(L2)):.4f}   "
      f"banked 'field-independent list 2^242.65'")
inv_E2 = Fraction(N2 * Q ** d2, math.comb(N2 - 1, m2)) + Fraction(k * Q, Q - n)
print(f"  1/E = 2^{lg2(int(inv_E2)):.4f}  < 2^128 ? {inv_E2 < TRIG}  "
      f"-> unsafe for every q < 2^256")

print()
print("=" * 74)
print("C1c  EXACT OPTIMIZATION of the whole family: max reach over (c|n, d)")
print("=" * 74)
print("admissibility: 1/E = N q^d / C(N-1,N/2+d) + k q/(q-n) < 2^128, worst q")
best = None
rows = []
for i in range(1, 42):                      # c = 2^i must divide n = 2^41
    cc = 2 ** i
    NN = n // cc
    if NN < 4:
        continue
    lgB_by_d = {}
    dmax = 0
    for dd in range(1, min(NN // 2, 4096) + 1):
        mm = NN // 2 + dd
        lgB = lg2comb(NN - 1, mm)
        # 1/E dominated by N q^d / B ; require < 2^127 (leave a bit for k q/(q-n))
        lhs_lg = lg2(NN) + dd * 256.0 - lgB
        if lhs_lg < 127.0:
            dmax = dd
            lgB_by_d[dd] = lgB
        else:
            break
    if dmax:
        reach = cc * dmax + cc - 1
        rows.append((i, cc, NN, dmax, reach, lgB_by_d[dmax]))
        if best is None or reach > best[4]:
            best = rows[-1]
print(f"{'i':>3} {'c=2^i':>14} {'N=n/c':>9} {'d_max':>6} {'reach sigma':>18} "
      f"{'log2 C(N-1,m)':>14}")
for r in rows:
    mark = "  <== MAX" if best and r[4] == best[4] else ""
    print(f"{r[0]:>3} {r[1]:>14,} {r[2]:>9} {r[3]:>6} {r[4]:>18,} "
          f"{r[5]:>14.4f}{mark}")
print()
print(f"FAMILY MAX REACH  sigma = {best[4]:,} = 2^{math.log2(best[4]+1):.4f} "
      f"at (c,d) = (2^{best[0]}, {best[3]})")
print(f"  vs banked forward-facing floor 2^34-1 = {2**34-1:,}   "
      f"MATCH={best[4] == 2**34 - 1}")
print(f"  naive first-moment / volume-exhaustion line n/log2(q) = "
      f"{n/256:,.0f} = 2^33")
print(f"  ratio reach / (n/log2 q) = {best[4]/(n/256):.4f}   (P4: predicted 2)")

print()
print("=" * 74)
print("C2  the razor need/supply arithmetic (the banked 4.73-4.83 bit deficit)")
print("=" * 74)
c127 = math.comb(127, 64)
print(f"log2 C(127,64) = {lg2(c127):.4f}   banked 123.1714  "
      f"MATCH={abs(lg2(c127)-123.1714) < 5e-4}")
for lgq in (255.900, 255.95, 256.0):
    need = lgq - 128.0
    print(f"  log2 q = {lgq:8.3f} -> need log2(q/2^128) = {need:8.4f}  "
          f"deficit vs C(127,64) = {need - lg2(c127):6.4f} bits "
          f"(x{2**(need-lg2(c127)):.2f})")
print()
print("rung table (d=1): reach = 2c-1, supply L = C(N-1,N/2+1)/N vs need q/2^128")
for j in range(6, 12):
    NN = 2 ** j
    cc = n // NN
    L = Fraction(math.comb(NN - 1, NN // 2 + 1), NN)
    reach = 2 * cc - 1
    lgL = lg2(int(L)) if int(L) > 0 else float("-inf")
    print(f"  N={NN:>5}  c=n/N=2^{int(math.log2(cc)):<2}  reach=2c-1="
          f"{reach:>16,} = 2^{math.log2(reach+1):.2f}   log2 L={lgL:8.4f}   "
          f"need 128.00  {'OK' if lgL >= 128 else 'SHORT by %.4f bits' % (128-lgL)}")

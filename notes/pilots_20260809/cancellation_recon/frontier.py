#!/usr/bin/env python3
"""The exact LB frontier at the razor rows: both in-repo mechanisms, all rungs.
Run: tools/ramguard tiny -- python3 notes/pilots_20260809/cancellation_recon/frontier.py
"""
import math
from fractions import Fraction

n, k = 2 ** 41, 2 ** 40


def lg2(x):
    x = int(x)
    if x <= 0:
        return float("-inf")
    b = x.bit_length()
    return math.log2(x) if b <= 900 else b - 900 + math.log2(x >> (b - 900))


print("M1  tangent / direct-value family (rs_tangent_flexible_budget_unsafe_floor):")
print("    B_mca(a) >= n-a ; unsafe iff n-a > B* = floor(q/2^128)")
print("    at agreement a = k+sigma:  n-a = k-sigma <= 2^40")
for lgq in (167, 168, 169, 170, 256):
    Bstar = 2 ** lgq // 2 ** 128
    print(f"      log2 q = {lgq:>3}: B* = 2^{lg2(Bstar):.2f}  vs  n-a <= k = 2^40  "
          f"-> {'ALIVE' if Bstar < k else 'DEAD (budget exceeds the whole payload)'}")
print("    => M1 is dead for every q >= 2^168; it is what determines the")
print("       crossing in the banked 'q < 2^167' determined range.")
print()
print("M2  counting family, both variants, all rungs, at the worst row q=2^256:")
print("    rotated prefix (CR1): L = C(N-1, N/2+d)/(N q^{d-1}),  reach = c(d+1)-1")
print("    fixed tail   (FT1): L = C(N-1, k/c+d)/q^d,           reach = c*d + c-1"
      "  (s=c-1)")
Q = 2 ** 256
NEED = Fraction(Q, 2 ** 128)      # L must exceed q/2^128
print(f"    need L > q/2^128 = 2^{lg2(int(NEED)):.4f}")
print()
print(f"{'N':>6} {'c=n/N':>16} {'variant':>9} {'d':>3} {'reach sigma':>18} "
      f"{'log2 L':>10} {'verdict':>26}")
best = (-1, None)
for j in range(5, 13):
    N = 2 ** j
    c = n // N
    for d in (0, 1, 2):
        # rotated prefix needs d >= 1
        if d >= 1:
            m = N // 2 + d
            L = Fraction(math.comb(N - 1, m), N * Q ** (d - 1))
            reach = c * d + c - 1
            ok = L > NEED
            print(f"{N:>6} {c:>16,} {'rotated':>9} {d:>3} {reach:>18,} "
                  f"{lg2(int(L)) if L >= 1 else lg2(1):>10.4f} "
                  f"{('ADMISSIBLE' if ok else 'short %.4f bits' % (lg2(int(NEED))-lg2(max(int(L),1)))):>26}")
            if ok and reach > best[0]:
                best = (reach, (N, c, "rotated", d))
        # fixed tail
        m2 = k // c + d
        if m2 <= N - 1:
            L2 = Fraction(math.comb(N - 1, m2), Q ** d)
            reach2 = c * d + c - 1
            ok2 = L2 > NEED
            print(f"{N:>6} {c:>16,} {'fixedtail':>9} {d:>3} {reach2:>18,} "
                  f"{lg2(int(L2)) if L2 >= 1 else lg2(1):>10.4f} "
                  f"{('ADMISSIBLE' if ok2 else 'short %.4f bits' % (lg2(int(NEED))-lg2(max(int(L2),1)))):>26}")
            if ok2 and reach2 > best[0]:
                best = (reach2, (N, c, "fixedtail", d))
print()
print(f"BEST ADMISSIBLE REACH over both variants and all rungs: sigma = {best[0]:,} "
      f"= 2^{math.log2(best[0]+1):.4f}  at {best[1]}")
print(f"  banked forward-facing floor: 2^34-1 = {2**34-1:,}  MATCH={best[0]==2**34-1}")
print()
print("first rung that would IMPROVE on 2^34-1, and its exact deficit:")
for N, var, d in ((128, "rotated", 1), (64, "fixedtail", 0), (128, "fixedtail", 1)):
    c = n // N
    if var == "rotated":
        m = N // 2 + d
        L = Fraction(math.comb(N - 1, m), N * Q ** (d - 1))
    else:
        m = k // c + d
        L = Fraction(math.comb(N - 1, m), Q ** d)
    reach = c * d + c - 1
    print(f"  N={N:>4} {var:>9} d={d}: reach = {reach:,} = 2^{math.log2(reach+1):.2f}"
          f"   log2 L = {lg2(max(int(L),1)):.4f}   SHORT by "
          f"{lg2(int(NEED)) - lg2(max(int(L),1)):.4f} bits")
print()
print("idealisation ceiling (the banked x28.4 figure): no-normalizer, m=N/2")
c127 = math.comb(127, 64)
print(f"  C(127,64) = 2^{lg2(c127):.4f}  vs need 2^128 -> short "
      f"{128 - lg2(c127):.4f} bits (x{2**(128-lg2(c127)):.2f})")
print("  and that idealisation only TIES the current reach (fixed tail d=0,")
print(f"  c=2^34 gives reach c-1 = {2**34-1:,} = 2^34-1).")

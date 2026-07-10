#!/usr/bin/env python3
"""AMBER AUDIT petal_growth: exact machine-check of the budget arithmetic.

Checks (all exact big-int / high-precision):
  A. 5005 = C(15,6), 38760 = C(20,6)  (F4-A1 ladder constant, F4-A2 c-sweep step)
  B. At the four official maximal rows n = 2^41..2^44:
       C(n+6,6) <= n^6 (exact), exponent log_n C(n+6,6) to 4 dp
       vs banked 5.7685/5.7740/5.7793/5.7843 and cap 5.785,
       slack bits = 246|252|258|264 - log2 C(n+6,6)  ~ 9.5
  C. c-sweep column keeps degree 6: C(n+14,6) <= n^6 exact, exponent <= 5.785
  D. Slack composition: slack = log2(6!) - log2(prod(1+i/n)) exactly
  E. v13 corrective consequence: bits of C(n/2-1, n/4) at n=2^10, 2^16
     (banked: 507 and 32760 bits) >> 100-160 bits of an n^10 budget
  F. v13 dyadic crossing table: bits of C(N-1, rho*N) for
     rho in {1/2,1/4,1/8,1/16}, N in {128,256,512}; first crossings over 2^128
"""
from math import comb, log2
from fractions import Fraction
import decimal

decimal.getcontext().prec = 60
D = decimal.Decimal

def bits(x):  # exact bit length
    return x.bit_length()

def log2_exact(x, prec=50):
    """log2 of a positive big int via Decimal ln."""
    return D(x).ln() / D(2).ln()

fails = []

# A
assert comb(15, 6) == 5005, "C(15,6) != 5005"
assert comb(20, 6) == 38760, "C(20,6) != 38760"
print("A. C(15,6)=5005 OK ; C(20,6)=38760 OK")

# B, C, D
banked = {41: "5.7685", 42: "5.7740", 43: "5.7793", 44: "5.7843"}
print("\nB/C/D. official maximal rows:")
for e in (41, 42, 43, 44):
    n = 1 << e
    col6 = comb(n + 6, 6)
    col14 = comb(n + 14, 6)
    n6 = n ** 6
    ok6 = col6 <= n6
    ok14 = col14 <= n6
    l2 = log2_exact(col6)
    expo = l2 / e
    l2_14 = log2_exact(col14)
    expo14 = l2_14 / e
    slack = D(6 * e) - l2
    # composition: n^6 / C(n+6,6) = 720 / prod_{i=1..6}(1+i/n)
    prod = Fraction(1)
    for i in range(1, 7):
        prod *= Fraction(n + i, n)
    comp = D(720) / (D(prod.numerator) / D(prod.denominator))
    comp_bits = comp.ln() / D(2).ln()
    match = (D(banked[e]) - expo).copy_abs() < D("0.00005")
    print(f"  n=2^{e}: C(n+6,6)<=n^6: {ok6}; exponent={expo:.6f} "
          f"(banked {banked[e]}, match={match}, <=5.785: {expo <= D('5.785')}); "
          f"slack={slack:.4f} bits (composition check {comp_bits:.4f}); "
          f"c=14 col: <=n^6 {ok14}, exponent={expo14:.6f} <=5.785: {expo14 <= D('5.785')}")
    if not (ok6 and ok14 and match and expo <= D("5.785") and expo14 <= D("5.785")):
        fails.append(e)
    # slack ~9.5 bits sanity
    if not (D("9.4") < slack < D("9.5")):
        fails.append(("slack", e))
print(f"  log2(6!) = {log2_exact(720):.6f}  (the slack ceiling)")

# E
print("\nE. v13 corrective consequence (M=2, k=n/2 planted column bits):")
for m in (10, 16):
    n = 1 << m
    c = comb(n // 2 - 1, n // 4)
    b = bits(c)
    budget_bits = 10 * m  # n^10
    print(f"  n=2^{m}: bits C(n/2-1,n/4) = {b} (banked endpoints 507/32760); "
          f"n^10 budget = {budget_bits} bits; super-budget: {b > budget_bits}")
    if (m == 10 and b != 507) or (m == 16 and b != 32760):
        fails.append(("v13bits", m))

# F
print("\nF. v13 dyadic crossing table (bits of C(N-1, rho N)):")
table = {}
for rho_num, rho_den in ((1, 2), (1, 4), (1, 8), (1, 16)):
    row = {}
    for N in (128, 256, 512, 1024):
        kk = N * rho_num // rho_den
        row[N] = bits(comb(N - 1, kk))
    table[f"1/{rho_den}"] = row
    print(f"  rho=1/{rho_den}: " + ", ".join(f"N={N}:{b}b" for N, b in row.items()))
banked_F = {"1/2": (128, 124, 256, 251), "1/4": (128, 100, 256, 204),
            "1/8": (128, 67, 256, 136), "1/16": (256, 83, 512, 169)}
for rho, (Np, bp, Nf, bf) in banked_F.items():
    ok = table[rho][Np] == bp and table[rho][Nf] == bf and bp <= 128 < bf
    print(f"  banked {rho}: prev N={Np} bits {bp}, first N={Nf} bits {bf} -> {ok}")
    if not ok:
        fails.append(("crossing", rho))

print("\nVERDICT:", "ALL EXACT CHECKS PASS" if not fails else f"FAILURES: {fails}")

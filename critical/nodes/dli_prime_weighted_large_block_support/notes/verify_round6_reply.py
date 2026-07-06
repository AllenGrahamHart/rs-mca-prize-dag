#!/usr/bin/env python3
"""
INDEPENDENT verification of Pro's DLI-CLOSE-4 fulfilment (round-6 reply).
Written from scratch against the claims in the note; does not reuse Pro's
checker logic.  All aggregate inequalities are checked in EXACT rational
arithmetic (product vs 2^100), no floats on the decision path.

Claims verified:
  V1  q=65537 prime (Pocklington, q-1 = 2^16), q ≡ 1 (mod 512), 2^256 >= q.
  V2  2 is NOT a primitive root mod q; 3 IS -> smallest primitive root g=3.
  V3  omega = 3^((q-1)/512) = 15028; ord(omega) = 512 exactly (omega^256 = -1).
  V4  1 + omega^95 - omega^146 == 0 (mod q); exponents reduced (< N=256);
      relation PRIMITIVE (no proper subsum vanishes); weight 3 = L+2 minimal
      (weight 2 impossible in reduced form since omega^d = ±1 forces N | d).
  V5  Gross K cap: 2^3 * C(256,3) = 22,108,160; exact RHS of the printed bound
      = 65537 * 2829844481 / 2^256 = 185459517751297 / 2^256 < 1.
      With E >= 1 (lambda=0 term of the D3 identity, pinned file D3 display),
      the printed bound E <= (q^L/2^N)(1 + K*2N*2^-(L+1)) is FALSE.
  V6  Aggregate constants: exact rational check that
        prod_{L=1..34} (1 + M*256L/2^L)  vs  2^100
      brackets the threshold M* in [13.290784077959, 13.290784077960],
      S(13) < 100 < S(14), and S(1), S(5), S(10) match Pro's table to 1e-9.
  V7  Pro's inequality (2):  min(1, 2^(256L)/2^N) * N * 2^-L <= 256L * 2^-L
      for all L in 1..34, N in 1..20000 (exact rational sweep), i.e. the
      per-generator ledger cap 256L*2^-L is valid whenever q < 2^256,
      2^N >= q^L.
  V8  Consistency: S(1) equals our round-5 "fantasy stack" arithmetic
      sum log2(1 + 512L*2^-(L+1)) = 51.16997... (pinned file said 51.2).
"""
from fractions import Fraction
from math import comb, log2

q = 65537
NP = 512          # n'
N = 256           # n'/2
L = 1

fails = []
def check(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        fails.append(name)

# ---- V1: primality + admissibility -------------------------------------
# Pocklington with F = 2^16 = q-1 (F^2 > q, sole prime factor 2, witness 3)
pock = (q - 1 == 2**16
        and pow(3, q - 1, q) == 1
        and pow(3, (q - 1) // 2, q) != 1)  # gcd(3^((q-1)/2) - 1, q) = 1 since q prime candidate; nontrivial check below
import math
pock = pock and math.gcd(pow(3, (q - 1) // 2, q) - 1, q) == 1
check("V1 Pocklington certificate for 65537", pock)
check("V1 q ≡ 1 (mod n'=512)", (q - 1) % NP == 0)
check("V1 admissible volume 2^N >= q^L", 2**N >= q**L)
check("V1 q < 2^256", q < 2**256)

# ---- V2: smallest primitive root ----------------------------------------
# q-1 = 2^16, so g primitive iff g^(2^15) == -1 (mod q).
check("V2 g=2 NOT primitive (2^16 == -1 -> ord(2)=32)",
      pow(2, 2**15, q) != q - 1 and pow(2, 32, q) == 1)
check("V2 g=3 primitive", pow(3, 2**15, q) == q - 1)

# ---- V3: pinned embedding -----------------------------------------------
omega = pow(3, (q - 1) // NP, q)
check("V3 omega == 15028", omega == 15028)
check("V3 omega^512 == 1", pow(omega, NP, q) == 1)
check("V3 omega^256 == -1 (exact order 512)", pow(omega, N, q) == q - 1)

# ---- V4: the weight-3 relation ------------------------------------------
t0, t1, t2 = 1, pow(omega, 95, q), (-pow(omega, 146, q)) % q
check("V4 relation 1 + w^95 - w^146 == 0 (mod q)", (t0 + t1 + t2) % q == 0)
check("V4 exponents reduced (< N)", 0 <= 95 < N and 0 <= 146 < N)
subsums = [t0, t1, t2, (t0 + t1) % q, (t0 + t2) % q, (t1 + t2) % q]
check("V4 primitive (no proper subsum vanishes)", all(s != 0 for s in subsums))
# weight-2 impossibility in reduced form: omega^d = ±1 requires 256 | d
w2 = all(pow(omega, d, q) not in (1, q - 1) for d in range(1, N))
check("V4 no weight-2 relation exists (minimal weight is 3 = L+2)", w2)

# ---- V5: the printed bound fails ----------------------------------------
K_gross = 8 * comb(N, 3)
check("V5 gross K cap = 22,108,160", K_gross == 22_108_160)
rhs = Fraction(q, 2**N) * (1 + Fraction(K_gross * 2 * N, 2**(L + 1)))
check("V5 exact RHS numerator = 185459517751297 (den 2^256)",
      rhs == Fraction(185459517751297, 2**256))
check("V5 RHS < 1  (while E >= 1 from lambda=0)", rhs < 1)
rhs_log2 = log2(185459517751297) - 256
check("V5 RHS ~ 2^-208.60", abs(rhs_log2 + 208.598) < 0.01)

# ---- V6: aggregate constants, EXACT rational ----------------------------
def agg_product(M: Fraction) -> Fraction:
    p = Fraction(1)
    for l in range(1, 35):
        p *= 1 + M * 256 * l / Fraction(2**l)
    return p

def S_bits(M: Fraction) -> float:
    p = agg_product(M)
    # high-precision log2 of a Fraction via bit lengths
    n, d = p.numerator, p.denominator
    return (n.bit_length() + log2(n / (1 << n.bit_length())) ) - \
           (d.bit_length() + log2(d / (1 << d.bit_length())) )

Mlo = Fraction(13290784077959, 10**12)
Mhi = Fraction(13290784077960, 10**12)
check("V6 threshold bracket: S(13.290784077959) <= 100 (exact)",
      agg_product(Mlo) <= 2**100)
check("V6 threshold bracket: S(13.290784077960) > 100 (exact)",
      agg_product(Mhi) > 2**100)
check("V6 S(13) < 100 < S(14) (exact)",
      agg_product(Fraction(13)) < 2**100 < agg_product(Fraction(14)))
for M, want in [(1, 51.169972398501), (5, 79.702150945630),
                (10, 93.865052872155), (13, 99.516255311986)]:
    got = S_bits(Fraction(M))
    check(f"V6 S({M}) = {want} (to 1e-9)", abs(got - want) < 1e-9)

# ---- V7: the per-generator cap (2) --------------------------------------
ok = True
for l in range(1, 35):
    for n in range(1, 20001):
        r_cap = min(Fraction(1), Fraction(2**(256 * l), 2**n)) if n <= 256*l + 64 \
                else Fraction(1, 2**(n - 256 * l))
        if r_cap * n > 256 * l:      # both sides share the 2^-L factor
            ok = False
            print(f"  (2) FAILS at L={l}, N={n}")
            break
    if not ok:
        break
check("V7 r*N*2^-L <= 256L*2^-L for all L<=34, N<=20000 (exact sweep)", ok)

# ---- V8: consistency with our round-5 fantasy arithmetic ----------------
fantasy = sum(log2(1 + 512 * l * 2.0**-(l + 1)) for l in range(1, 35))
check("V8 round-5 fantasy stack == S(1) == 51.16997...",
      abs(fantasy - 51.169972398501) < 1e-9)

print()
print("ALL PASS" if not fails else f"FAILURES: {fails}")

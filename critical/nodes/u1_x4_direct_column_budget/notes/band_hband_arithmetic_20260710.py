#!/usr/bin/env python3
"""band_hband_arithmetic.py — exact arithmetic for the u1_x4 h-band audit (catch #38).

All exact integer / Fraction arithmetic. Local, tiny.
Sections:
  1. F-3 ledger at s=13: h=2 (CP import), h=3 (H3-ACT(4096) compiler), remainder.
  2. Strata counts under the derived outer cap H_max = min(A, n/2), A = k+t,
     for rates {1/2,1/4,1/8,1/16} and t-conventions {n/256, n/512, n/1024}.
  3. Per-stratum average allowance under n^3 and 16n^3.
  4. Unconditional per-h cap (proved fiber cap n/h): C(n,h)*(floor(n/h)-1)/2 vs n^3
     -> shows no budget cutoff (ii) is derivable from proved caps.
  5. Heuristic Poisson/first-moment vacancy threshold per row s = 13..41:
     min h with n^2/(2 h!^2) < 1, and the tail sum — the ONLY object that
     yields a small h cap, and it is heuristic + row-dependent.
  6. In-house h=2 chain crossover (22111-optimized Stepanov) vs n^3 and 16n^3.
"""
from fractions import Fraction
from math import comb, factorial, isqrt

def sec(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)

# ---------------------------------------------------------------- section 1
sec("1. F-3 ledger at the binding row s=13 (n = 8192), budget n^3")
s = 13
n = 2 ** s
n3 = n ** 3
print(f"n = {n}, n^3 = {n3}")

# h=2, CP import as banked in F3_FLIP brief: 'CP import (2/3) n^{5/2}'.
# n^{5/2} = n^2 * sqrt(n); sqrt(8192) = 64*sqrt(2) irrational -> bound with rational envelope
# n^{5/2} exactly: 8192^2 * 8192^{1/2}. Use integer sqrt on n^5.
n5 = n ** 5
r = isqrt(n5)          # floor sqrt
h2_cp_num = 2 * (r + 1)  # ceil-safe: T_2 <= (2/3) n^{5/2} < (2/3)(r+1)
h2_cp = Fraction(h2_cp_num, 3)
print(f"h=2 CP spend  <= (2/3) n^(5/2) < {float(h2_cp):.6e}  = {float(h2_cp/n3)*100:.4f}% of n^3")

# h=3, H3-ACT(4096) compiler: T_3 <= [3|n] C(n/3,2) + n^2/72 + 4096 n^2
toral3 = comb(n // 3, 2) if n % 3 == 0 else 0
h3 = Fraction(toral3) + Fraction(n * n, 72) + 4096 * n * n
print(f"h=3 ACT(4096) spend <= toral({toral3}) + n^2/72 + 4096 n^2 = {float(h3):.10e}")
print(f"  exact fraction of n^3 = {float(h3 / n3) * 100:.5f}%   (dag notes print '50.002%')")
print(f"  4096 = n/2 at s=13 -> the 'exact factor-2.0 first-row margin'")

rem_n3 = Fraction(n3) - h2_cp - h3
print(f"remainder for ALL h >= 4 strata under n^3: {float(rem_n3):.6e} = {float(rem_n3/n3)*100:.4f}% of n^3")
print(f"  in n^2 units: {float(rem_n3 / (n*n)):.2f} n^2")
rem_16n3 = 16 * Fraction(n3) - h2_cp - h3
print(f"remainder under the consumer's PROVED 16 n^3 tolerance: {float(rem_16n3):.6e}")
print(f"  in n^2 units: {float(rem_16n3 / (n*n)):.2f} n^2 ; ACT(4096)-grade strata that still fit: "
      f"{float(rem_16n3 / (4096*n*n)):.2f}")

# ---------------------------------------------------------------- section 2
sec("2. Strata counts under outer cap H_max = min(A, n/2), A = k + t (s=13)")
print(f"{'rate':>6} {'k':>6} | " + " | ".join(f"t={t:>3}: A, H_max, #strata(h in [2,H_max])" for t in (32, 16, 8)))
for num, den in ((1, 2), (1, 4), (1, 8), (1, 16)):
    k = n * num // den
    cells = []
    for t in (32, 16, 8):
        A = k + t
        H = min(A, n // 2)
        strata = H - 1  # h = 2..H
        cells.append(f"A={A:>5} H={H:>5} strata={strata:>5}")
    print(f"{num}/{den:>3} {k:>6} | " + " | ".join(cells))

# ---------------------------------------------------------------- section 3
sec("3. Per-stratum average allowance for h >= 4 at s=13")
for num, den, t in ((1, 2, 16), (1, 16, 8)):
    k = n * num // den
    H = min(k + t, n // 2)
    strata_ge4 = H - 3  # h = 4..H
    print(f"rate {num}/{den}, t={t}: H_max={H}, strata h>=4: {strata_ge4}")
    print(f"   n^3 budget:  avg {float(rem_n3 / strata_ge4 / (n*n)):9.3f} n^2 per stratum")
    print(f"   16n^3:       avg {float(rem_16n3 / strata_ge4 / (n*n)):9.3f} n^2 per stratum")

# ---------------------------------------------------------------- section 4
sec("4. Proved per-h caps (fiber cap floor(n/h)) vs n^3 at s=13 — cutoff (ii)?")
print("cap(h) = C(n,h) * (floor(n/h)-1) / 2   [PROVED: F3_IDENTIFICATION sec.2]")
for h in (2, 3, 4, 5, 8, 16, 64, 520, 2048, 4096):
    if 2 * h > n:
        continue
    cap = comb(n, h) * (n // h - 1) // 2
    bits = cap.bit_length() - n3.bit_length()
    print(f"  h={h:>5}: log2(cap) ~ {cap.bit_length()-1:>7}  = n^3 x 2^{bits:>+8}  "
          f"{'<= n^3  (PAYS)' if cap <= n3 else '> n^3   (fails)'}")
print("General h=2 identity: C(n,2)(n/2-1)/2 = n(n-1)(n-2)/8 < n^3/8 at EVERY row (12.5%).")
print("Monotone growth: cap(h) > n^3 for every 3 <= h <= n/2 at s=13 -> no proved tail cutoff.")

# ---------------------------------------------------------------- section 5
sec("5. HEURISTIC first-moment (Poisson) vacancy threshold per official row")
print("mean_h = C(n,h)^2 / (2 q^{h-1}) <= n^2/(2 h!^2) at q >= n^2  [F3_SHALLOW_LADDER sec.3]")
print("H_vac(s) = min h such that n^2/(2 h!^2) < 1 (per-stratum mean < 1);")
print("tail(s)  = sum_{h >= H_vac} n^2/(2 h!^2)")
for s_ in range(13, 42, 2):
    n_ = 2 ** s_
    h = 2
    while Fraction(n_ * n_, 2 * factorial(h) ** 2) >= 1:
        h += 1
    tail = sum(Fraction(n_ * n_, 2 * factorial(j) ** 2) for j in range(h, h + 40))
    print(f"  s={s_:>2}: H_vac = {h:>2}   tail sum = {float(tail):.4f}")

# ---------------------------------------------------------------- section 6
sec("6. In-house h=2 chain (E <= 22111 n^{5/2}, T_2 <= E/8) crossovers")
c = Fraction(22111, 8)
# T_2 <= c n^{5/2} < n^3  <=>  sqrt(n) > c  <=> n > c^2
n_cross = float(c) ** 2
print(f"T_2 <= {float(c):.1f} n^(5/2) < n^3  <=>  n > {n_cross:.3e}  <=> s >= {int(n_cross).bit_length()}")
n_cross16 = (float(c) / 16) ** 2
print(f"          < 16 n^3               <=>  n > {n_cross16:.3e}  <=> s >= {int(n_cross16).bit_length()}")
print("At s=13 the h=2 payment under n^3 rests on the CP import constant, not the in-house chain.")

# ---------------------------------------------------------------- extra check
sec("7. Cross-check: two ACT(4096) strata bust n^3 at s=13")
two = 2 * (Fraction(n * n, 72) + 4096 * n * n)
print(f"2 x (n^2/72 + 4096 n^2) = {float(two):.6e} vs n^3 = {n3}  -> "
      f"{'OVER' if two > n3 else 'under'} by {float(two - n3):.3e}")

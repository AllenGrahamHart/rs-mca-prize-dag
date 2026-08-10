#!/usr/bin/env python3
"""D3: independent exact re-derivation of the Haboeck rate-half ladder.

Everything is derived from the IMPORT's (HJ1) form only --
    |E_m| <= (ell_m**7 / 3) * (rho*n)**2,  ell_m = (m + 1/2)/sqrt(rho),
    gamma_m = 1 - (1 + 1/(2m))*sqrt(rho),
-- never from the consumer's banked closed forms N_m/D or (2m a)^2.
The banked closed forms are then compared as a separate cross-check.

Exact rationals + math.isqrt only. No float anywhere.
"""

from fractions import Fraction
from math import isqrt

N = 1 << 41
K = 1 << 40            # repository dimension: RS[F,D,K] = {deg < K}
D_DEG = K - 1          # Haboeck's degree bound d = K-1
RHO = Fraction(D_DEG, N)
CAP = (1 << 256) - 1                  # strict prize cap q < 2^256
BSTAR_MAX = CAP >> 128                # max attainable B* = floor(q/2^128)


def floor_sqrt_frac(x: Fraction) -> int:
    """floor(sqrt(x)) for a positive rational x."""
    return isqrt(x.numerator // x.denominator) if x.denominator == 1 else \
        isqrt(int(x))  # int() truncates toward zero; x > 0 so == floor


def ceil_sqrt_frac(x: Fraction) -> int:
    """ceil(sqrt(x)) for a positive rational x, exact."""
    c = isqrt(int(x))
    while Fraction(c * c) < x:
        c += 1
    while c > 0 and Fraction((c - 1) * (c - 1)) >= x:
        c -= 1
    return c


def bound_squared(m: int) -> Fraction:
    """((ell_m**7/3) * (rho*n)**2)**2, exact -- sqrt(rho) never materialised."""
    # ell^7 = ((2m+1)/2)^7 * rho^(-7/2); squaring kills the half-power.
    return (Fraction(2 * m + 1, 2) ** 14) * (RHO ** -7) * (RHO * N) ** 4 / 9


def threshold_squared(m: int) -> Fraction:
    """((1-gamma_m)*n)**2 = ((1+1/(2m))*sqrt(rho)*n)**2, exact."""
    return (Fraction(2 * m + 1, 2 * m) ** 2) * RHO * Fraction(N) ** 2


def Q(m: int) -> int:
    return floor_sqrt_frac(bound_squared(m))


def A(m: int) -> int:
    return ceil_sqrt_frac(threshold_squared(m))


def ilog2_frac(x: int, prec: int = 64, P: int = 256) -> Fraction:
    """log2(x) to `prec` fractional bits by integer fixed-point squaring.

    Truncating, so the result is a lower bound within 2^-prec + tiny.
    """
    b = x.bit_length() - 1
    acc = Fraction(b)
    mant = (x << P) >> b          # scaled mantissa in [2^P, 2^(P+1))
    weight = Fraction(1, 2)
    for _ in range(prec):
        mant = (mant * mant) >> P
        if mant >= (1 << (P + 1)):
            mant >>= 1
            acc += weight
        weight /= 2
    return acc


def main() -> None:
    global RHO
    print(f"n={N} k={K} d=k-1={D_DEG} rho={RHO}")
    print(f"3n/4 = {3 * N // 4}   sqrt(n(k-1)) floor = {isqrt(N * D_DEG)}")
    print(f"B*max (q<2^256) = {BSTAR_MAX} = 2^128-1 -> {BSTAR_MAX == (1 << 128) - 1}")
    print()

    # ---- cross-check the consumer's closed forms against (HJ1) -------------
    closed_ok = True
    for m in range(3, 97):
        n_m = (2 * m + 1) ** 14 * N ** 7
        den = 384 ** 2 * (K - 1) ** 3
        if bound_squared(m) != Fraction(n_m, den):
            closed_ok = False
            print(f"  RHJ1 CLOSED-FORM MISMATCH at m={m}")
        # (RHJ2): least a with (2m a)^2 >= (2m+1)^2 n (k-1)
        a_closed = ceil_sqrt_frac(
            Fraction((2 * m + 1) ** 2 * N * (K - 1), (2 * m) ** 2))
        if a_closed != A(m):
            closed_ok = False
            print(f"  RHJ2 CLOSED-FORM MISMATCH at m={m}: {a_closed} vs {A(m)}")
    print(f"CLOSED_FORM_AGREES_WITH_HJ1 {closed_ok}")
    print()

    # ---- the ladder -------------------------------------------------------
    three_n_4 = 3 * N // 4
    rows = {m: (Q(m), A(m)) for m in range(3, 98)}

    first_improve = min(m for m in range(3, 97) if rows[m][1] < three_n_4)
    print(f"FIRST_m_WITH_a_m<3n/4 = {first_improve}")
    print(f"  a_8={rows[8][1]}  (>3n/4? {rows[8][1] > three_n_4})")
    print(f"  a_9={rows[9][1]}  (<3n/4? {rows[9][1] < three_n_4})")
    print(f"  Q_9={rows[9][0]}")
    print()

    affordable = [m for m in range(3, 98) if rows[m][0] <= BSTAR_MAX]
    print(f"MAX_AFFORDABLE_m (Q_m<=2^128-1) = {max(affordable)}")
    print(f"  Q_95={rows[95][0]}  <=2^128-1? {rows[95][0] <= (1 << 128) - 1}")
    print(f"  Q_96={rows[96][0]}  >2^128-1?  {rows[96][0] > (1 << 128) - 1}")
    print(f"  a_95={rows[95][1]}  n-a_95={N - rows[95][1]}")
    print(f"  Q_94={rows[94][0]}  a_94={rows[94][1]}")
    nondecr = all(rows[m][0] <= rows[m + 1][0] for m in range(3, 97))
    a_decr = all(rows[m][1] >= rows[m + 1][1] for m in range(3, 97))
    print(f"  Q_m nondecreasing: {nondecr}   a_m nonincreasing: {a_decr}")
    print()

    # ---- razor-slice thresholds, exact -----------------------------------
    # X < 2^255.9  <=>  X^10 < 2^2559
    for m in (93, 94, 95, 96):
        x = rows[m][0] << 128
        print(f"  m={m}: Q_m*2^128 < 2^255.9 ? {x ** 10 < 1 << 2559}"
              f"   < 2^256 ? {x < 1 << 256}")
    print()

    # ---- m=9 field entry point -------------------------------------------
    lg = ilog2_frac(rows[9][0] << 128, 80)
    print(f"log2(Q_9*2^128) ~ {float(lg):.9f}   (claim 232.650531)")
    lo = Fraction(232650530, 10 ** 6)
    hi = Fraction(232650532, 10 ** 6)
    print(f"  in [{lo}, {hi}] ? {lo <= lg <= hi}")
    print()

    # ---- D2 counterfactual: what if the code were dim k+1 (d=k)? ---------
    saved = RHO
    RHO = Fraction(K, N)
    print("COUNTERFACTUAL rho=k/n (i.e. if RS[F,D,k] meant deg<=k):")
    for m in (9, 94, 95):
        a_alt = A(m)
        print(f"  m={m}: a_m would be {a_alt}, banked {rows[m][1]}, "
              f"banked SAFE? {rows[m][1] >= a_alt}")
        q_alt = Q(m)
        print(f"        Q_m would be {q_alt}, banked {rows[m][0]}, "
              f"banked >= true? {rows[m][0] >= q_alt}")
    RHO = saved
    print()

    # ---- Johnson-radius sanity -------------------------------------------
    john = isqrt(N * D_DEG)
    print(f"a_95={rows[95][1]} > floor(sqrt(n(k-1)))={john} ? "
          f"{rows[95][1] > john}")
    print(f"a_96 would be {rows[96][1]}; a_inf -> {john}")
    print()

    # ---- gamma_m > 0 admissibility ---------------------------------------
    bad = [m for m in range(3, 97)
           if threshold_squared(m) >= Fraction(N) ** 2]
    print(f"m with (1-gamma_m)n >= n (gamma_m<=0): {bad}")

    print()
    print("LADDER m,Q_m,a_m (m=3..96)")
    for m in range(3, 97):
        print(f"  {m},{rows[m][0]},{rows[m][1]}")


if __name__ == "__main__":
    main()

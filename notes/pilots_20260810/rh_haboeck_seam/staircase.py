#!/usr/bin/env python3
"""The sub-razor Haboeck staircase the consumer node does not record.

rate_half_band_crossing_location's obligation is 2^167 < q < 2^256.
Its shard + addendum transport only the m=94 / m=95 razor members.
This prints the full proved staircase over the whole q-range where the
banked bracket node's own (RHJ4) already bites, so the coordinator can
see exactly how much proved content is not transported.
"""

from fractions import Fraction
from math import isqrt

N = 1 << 41
K = 1 << 40
DEG = K - 1
RHO = Fraction(DEG, N)
THREE_N_4 = 3 * N // 4


def ilog2(x: int, prec: int = 64, P: int = 256) -> float:
    b = x.bit_length() - 1
    acc = Fraction(b)
    mant = (x << P) >> b
    w = Fraction(1, 2)
    for _ in range(prec):
        mant = (mant * mant) >> P
        if mant >= (1 << (P + 1)):
            mant >>= 1
            acc += w
        w /= 2
    return float(acc)


def ceil_sqrt(x: Fraction) -> int:
    c = isqrt(int(x))
    while Fraction(c * c) < x:
        c += 1
    while c > 0 and Fraction((c - 1) * (c - 1)) >= x:
        c -= 1
    return c


def main() -> None:
    print("m  log2(q threshold)  a_m           gain vs 3n/4")
    prev = None
    for m in range(9, 96):
        q2 = ((Fraction(2 * m + 1, 2) ** 14) * (RHO ** -7)
              * (RHO * N) ** 4 / 9)
        Qm = isqrt(int(q2))
        am = ceil_sqrt((Fraction(2 * m + 1, 2 * m) ** 2) * RHO
                       * Fraction(N) ** 2)
        thr = ilog2(Qm << 128)
        mark = ""
        if m in (9, 94, 95):
            mark = "  <-- banked"
        if prev is not None and am == prev:
            mark += "  [a_m unchanged]"
        prev = am
        print(f"{m:3d}  {thr:18.6f}  {am}  {THREE_N_4 - am:>13d}{mark}")

    print()
    print(f"3n/4 = {THREE_N_4}")
    print("razor slice starts at log2 q = 255.900000")
    print("=> the window log2 q in [232.650530, 255.900000] carries "
          "m = 9..94 and is now recorded on the consumer node.")


if __name__ == "__main__":
    main()

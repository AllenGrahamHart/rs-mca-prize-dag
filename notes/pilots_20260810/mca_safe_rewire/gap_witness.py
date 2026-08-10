#!/usr/bin/env python3
"""D2: exhibit explicit admissible rate-half rows inside the coverage gap.

Admissibility (rules_freeze + the rate_half_band_closure master statement):
  n = 2^41, k = 2^40, q prime power with n | q-1 and q < 2^256.
Gap of record: 2^167 < q < 2^169 (above the wave-10 staircase's determined
range, below HD1's field floor).

Deterministic Miller-Rabin over the first 20 primes is a proof of primality
for n < 3.3e24 only, so the witnesses below are certified by 64 rounds of
strong-probable-prime testing (error < 4^-64) and reported as such.

Read-only.  stdlib only.
"""
from __future__ import annotations

import random

N = 1 << 41
K = 1 << 40


def is_probable_prime(m: int, rounds: int = 64) -> bool:
    if m < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            return m == p
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    rng = random.Random(20260810)
    for _ in range(rounds):
        a = rng.randrange(2, m - 1)
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def first_admissible_above(lo: int, want: int = 3) -> list[int]:
    """Smallest q > lo with q = 1 mod N and q probably prime."""
    out = []
    t = lo // N + 1
    while len(out) < want:
        q = t * N + 1
        if q > lo and is_probable_prime(q):
            out.append(q)
        t += 1
    return out


def report(q: int, label: str) -> None:
    bstar = q >> 128
    r_from_staircase = bstar - 1           # a_RH = n - B + 1  =>  sigma = ...
    print(f"\n{label}")
    print(f"  q            = {q}")
    print(f"  log2 q       ~ {q.bit_length() - 1} (bit_length {q.bit_length()})")
    print(f"  q = 1 mod n  : {(q - 1) % N == 0}   ((q-1)/n = {(q-1)//N})")
    print(f"  q < 2^256    : {q < (1 << 256)}")
    print(f"  B* = q>>128  = {bstar}")
    print(f"  B* vs 2^39   : {bstar} vs {1 << 39}  (B* >= 2^39: {bstar >= 1 << 39})")
    print(f"  B* vs n=2^41 : {bstar} vs {N}  (HD1 needs n <= B*: {N <= bstar})")
    print(f"  staircase a_RH = n-B*+1 would be {N - bstar + 1}; "
          f"needs r = B*-1 <= (n-k)/2 = {(N-K)//2}: "
          f"{r_from_staircase <= (N - K) // 2}")
    print(f"  FA1 safe point a = n = {N}: B_mca(n) = 1 <= B* -> "
          f"{1 <= bstar}")
    print(f"  HD1 safe point a = 3n/4 = {3*N//4}: needs n <= B* -> "
          f"{N <= bstar}")


def main() -> None:
    lo, hi = 1 << 167, 1 << 169
    print("GAP WITNESS SEARCH: admissible rate-half rows with 2^167 < q < 2^169")
    print(f"  n = {N} = 2^41, k = {K} = 2^40")
    print(f"  arithmetic progression 1 mod n has "
          f"{(hi - lo)//N} terms in the gap")

    ws = first_admissible_above(lo, 3)
    for i, q in enumerate(ws):
        assert lo < q < hi
        report(q, f"WITNESS {i+1} (smallest admissible q above 2^167, #{i+1})")

    # the boundary sliver named by the D4 cross-link
    print("\n--- D4 CROSS-LINK SLIVER ---")
    sliver_hi = (1 << 39) * (1 << 128) + (1 << 128)   # (2^39+1)*2^128
    print(f"  budget 2^39+1 needs q >= (2^39+1)*2^128 = {sliver_hi}")
    print(f"  that is > 2^167 by {sliver_hi - (1 << 167)} = 2^128")
    sl = first_admissible_above(1 << 167, 1)[0]
    print(f"  smallest admissible q above 2^167 = {sl}")
    print(f"  is it inside the sliver [2^167, (2^39+1)*2^128)?  "
          f"{(1 << 167) <= sl < sliver_hi}")
    print(f"  its B* = {sl >> 128} (== 2^39: {(sl >> 128) == (1 << 39)})")


if __name__ == "__main__":
    main()

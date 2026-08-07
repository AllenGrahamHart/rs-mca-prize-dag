#!/usr/bin/env python3
"""E6: D4 -- the clause-(b) shape extrapolated, plus the cost of the cells
this pilot could NOT fit locally (Modal request lines).

The measured law (this pilot, 11 cells) is
    RET(sigma=1) = (1-1/q)^{n-k-1} * N_{k+1}/q * (1 + O(1/q)),
i.e. RATIOSHELL := RET/(N_{k+1}/q) is FLAT in ell and equals the exactness
factor.  Extrapolating the SAME law to a general agreement threshold
k+sigma gives
    MASS(n,ell,sigma) = sum_{r>=sigma} N_{k+r}(ell) q^{-r} (1-1/q)^{n-k-r}.
This script evaluates that at official-row scale.
"""
from math import comb, log2, lgamma
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cf_cells import cells, shells                     # noqa: E402


def lcomb(n, r):
    if r < 0 or r > n:
        return float("-inf")
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / log2(2.718281828459045) / 1.0 * 0 + \
        (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / 0.6931471805599453


def log2_mass(n, ell, sigma, log2q):
    """log2 of the dominant term of MASS: N_{k+sigma} q^{-sigma}, with
    N_{k+sigma} ~ C(k-1,Lambda) C(b,b) C(t*ell, Lambda+1-sigma)."""
    k, t, b, C, Lam = cells(n, ell)
    if sigma > Lam or t < 2:
        return None, (t, b, Lam)
    om = Lam + 1 - sigma
    return (lcomb(C, Lam) + lcomb(t * ell, om) + b
            - sigma * log2q), (t, b, Lam)


print("=" * 100)
print("D4-a  the measured law re-expressed: MASS(sigma) at the measured cells")
print("=" * 100)
Q = 97
for n, ell in ((24, 2), (24, 4), (32, 3), (32, 5)):
    N = shells(n, ell)
    k = n // 2
    row = []
    for s in sorted(N)[:6]:
        m = sum(v * Q ** (-r) * (1 - 1.0 / Q) ** (n - k - r)
                for r, v in N.items() if r >= s)
        row.append(f"sigma={s}: {m:,.2f}")
    print(f"  n={n} ell={ell}: " + "   ".join(row))

print()
print("=" * 100)
print("D4-b  EXTRAPOLATION to the consumer regime (label: EXTRAPOLATED from")
print("      the measured law; NOT measured, NOT proved)")
print("=" * 100)
print("Rows: n = 2^e at rate 1/2; ell chosen so that t = (k+1)/ell is the")
print("stated value; sigma taken AT the listing bound sigma = ell-1 (the")
print("largest threshold this chart can serve) and at sigma = Lambda.")
print()
print(f"{'n':>10} {'log2 q':>7} {'t':>5} {'ell':>10} {'Lambda':>10} "
      f"{'log2 MASS(sig=1)':>18} {'log2 MASS(sig=ell-1)':>22} "
      f"{'log2 MASS(sig=Lam)':>20}")
for e in (13, 20, 31, 41):
    n = 2 ** e
    k = n // 2
    for log2q in (31.0, 128.0):
        for tt in (3, 8, e):
            ell = max(2, (k + 1) // tt)
            kk, t, b, C, Lam = cells(n, ell)
            if t < 2:
                continue
            m1 = log2_mass(n, ell, 1, log2q)[0]
            m2 = log2_mass(n, ell, min(ell - 1, Lam), log2q)[0]
            m3 = log2_mass(n, ell, Lam, log2q)[0]
            print(f"{n:>10,} {log2q:>7.0f} {t:>5} {ell:>10,} {Lam:>10,} "
                  f"{m1:>18,.0f} {m2:>22,.0f} {m3:>20,.0f}")

print()
print("=" * 100)
print("D4-c  cells NOT fitted locally -- exact cost + Modal request lines")
print("=" * 100)
LOCAL_RATE = 1_606_481_810 / 81.0     # measured: n=32 ell=5, 81 s per word
for n, ell in ((32, 6), (32, 8), (64, 2), (64, 3), (64, 4), (64, 5),
               (48, 3), (48, 4)):
    try:
        k, t, b, C, Lam = cells(n, ell)
    except AssertionError:
        continue
    if b >= ell or t < 2:
        print(f"  n={n} ell={ell}: illegal chart (t={t}, b={b})")
        continue
    N = shells(n, ell)
    box = sum(N.values())
    secs = box / LOCAL_RATE
    print(f"  n={n:>3} ell={ell}: t={t:>2} b={b:>2} Lambda={Lam:>3} "
          f"BOX={box:>22,}  1 word ~ {secs:>12,.0f} s "
          f"({secs/3600:>9,.2f} CPU-h)  "
          f"{'LOCAL' if secs < 280 else 'MODAL'}")
print()
print("Modal request lines (for the coordinator; this pilot launched none):")
for n, ell, words in ((64, 2, 20), (64, 3, 8), (64, 4, 4)):
    N = shells(n, ell)
    box = sum(N.values())
    secs = box / LOCAL_RATE * words
    print(f"  L1-N10-ELL-{n}-{ell}: n={n}, q=193, LAYOUT-A, ell={ell}, "
          f"{words} words (consec, geom5, mindeg, {words-3} random), "
          f"BOX={box:,}, ~{secs/3600:.2f} CPU-h at the measured local rate "
          f"({LOCAL_RATE/1e6:.1f}e6 candidates/s/word), 1 GiB")

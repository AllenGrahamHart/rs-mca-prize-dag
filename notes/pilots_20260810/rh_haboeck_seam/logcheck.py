#!/usr/bin/env python3
"""Validate the fixed-point ilog2 and pin log2(Q_9*2^128) to 9 decimals.

Two independent routes:
  (a) fixed-point binary-logarithm squaring at two precisions;
  (b) a purely integer bracket X^p vs 2^e for p = 10**4 and p = 10**5,
      which needs no logarithm at all.
"""

from fractions import Fraction

Q9 = 31838208335176550182206428283836
X = Q9 << 128


def ilog2(x: int, prec: int, P: int) -> Fraction:
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
    return acc


def log_interval(num: int, den: int, terms: int = 64) -> tuple[Fraction, Fraction]:
    """Exact interval for log(num/den) from 2*atanh((x-1)/(x+1))."""
    z = Fraction(num - den, num + den)
    assert 0 < z < 1
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lower, lower + tail


def log2_interval(x: int, terms: int = 64) -> tuple[Fraction, Fraction]:
    exponent = x.bit_length() - 1
    log_y_lo, log_y_hi = log_interval(x, 1 << exponent, terms)
    log_2_lo, log_2_hi = log_interval(2, 1, terms)
    return (
        Fraction(exponent) + log_y_lo / log_2_hi,
        Fraction(exponent) + log_y_hi / log_2_lo,
    )


def main() -> None:
    # (a) self-validation on known constants
    for val, name, ref in [(3, "log2(3)", "1.584962500721156"),
                           (10, "log2(10)", "3.321928094887362"),
                           (7, "log2(7)", "2.807354922057604")]:
        v = ilog2(val, 96, 384)
        print(f"  {name} = {float(v):.15f}   reference {ref}")

    # (a) two precisions on the target
    v64 = ilog2(X, 64, 256)
    v128 = ilog2(X, 128, 512)
    print(f"\nlog2(Q_9*2^128) prec64  = {float(v64):.12f}")
    print(f"log2(Q_9*2^128) prec128 = {float(v128):.12f}")
    print(f"agree to 1e-12: {abs(float(v64) - float(v128)) < 1e-12}")

    # (b) integer-only bracket: no logs, just big powers.
    for p in (10 ** 4, 10 ** 5):
        xp = X ** p
        e = xp.bit_length() - 1          # 2^e <= X^p < 2^(e+1)
        lo = Fraction(e, p)
        hi = Fraction(e + 1, p)
        print(f"\n  p={p}: {lo} <= log2(X) < {hi}")
        print(f"         = [{float(lo):.9f}, {float(hi):.9f})")

    # Exact rational interval with a proved atanh-series tail bound.
    lo, hi = log2_interval(X)
    lower_printed = Fraction(232650530, 10**6)
    upper_old = Fraction(232650531, 10**6)
    print("\n  exact atanh-series interval (64 terms):")
    print(f"         [{float(lo):.12f}, {float(hi):.12f}]")
    print(f"  width < 1e-18 ? {hi - lo < Fraction(1, 10**18)}")
    print(f"  log2(X) > 232.650530 ? {lo > lower_printed}")
    print(f"  log2(X) < 232.650531 ? {hi < upper_old}")


if __name__ == "__main__":
    main()

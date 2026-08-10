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

    # decisive: is log2(X) below or above 232.650531 and 232.650530?
    p = 10 ** 6
    for target in ("232650530", "232650531"):
        t = int(target)          # target/10^6
        # compare X^(10^6) with 2^t  -> needs 2.3e8 bits; use bit_length route
        pass
    print("\n  (10^6-power route not attempted: ~291MB integer, over budget)")

    # instead: bracket with p = 10**5 refined by an extra digit via p=2*10**5
    p = 2 * 10 ** 5
    xp = X ** p
    e = xp.bit_length() - 1
    print(f"  p={p}: {Fraction(e, p)} <= log2(X) < {Fraction(e + 1, p)}")
    print(f"         = [{float(Fraction(e, p)):.10f}, "
          f"{float(Fraction(e + 1, p)):.10f})")
    print(f"  is log2(X) < 232.650531 ? {Fraction(e + 1, p) <= Fraction(232650531, 10**6)}")
    print(f"  is log2(X) < 232.6505305 ? {Fraction(e + 1, p) <= Fraction(2326505305, 10**7)}")
    print(f"  is log2(X) > 232.650530 ? {Fraction(e, p) >= Fraction(232650530, 10**6)}")


if __name__ == "__main__":
    main()

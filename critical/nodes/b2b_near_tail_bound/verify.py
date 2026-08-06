#!/usr/bin/env python3
"""Exact arithmetic replay for the official exact-slice near-tail theorem."""

from fractions import Fraction


N = 1 << 41
ROWS = (
    ("1/2", 63, 128, Fraction(4999, 5000), 257, 15),
    ("1/4", 1, 4, Fraction(507, 625), 316, 14),
    ("1/8", 1, 8, Fraction(1087, 2000), 472, 13),
    ("1/16", 1, 16, Fraction(843, 2500), 760, 12),
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    print(f"PASS {label}")


def entropy_exceeds(a: int, b: int, bound: Fraction) -> bool:
    """Check H_2(a/b)>bound by exponentiating an exact integer inequality."""
    c, d = bound.numerator, bound.denominator
    lhs = pow(b, b * d)
    rhs = pow(a, a * d) * pow(b - a, (b - a) * d) * pow(2, b * c)
    return lhs > rhs


def main() -> None:
    require(N + 1 < 1 << 42, "type-class logarithmic loss is below 42 bits")
    t0_floor = (N >> 8) - 1
    require(2 * t0_floor * t0_floor > 385 * N, "uniform corridor comparison margin")
    for rate, a, b, entropy_floor, constant, width in ROWS:
        require(entropy_exceeds(a, b, entropy_floor), f"rate {rate} entropy floor")
        require(entropy_floor > Fraction(256, constant), f"rate {rate} depth constant")
        require(
            2 * pow(constant, width + 1) < (constant - 1) * (1 << 122),
            f"rate {rate} two-sided near-tail budget",
        )
    print("B2B_EXACT_SLICE_NEAR_TAIL_PASS rows=4")


if __name__ == "__main__":
    main()

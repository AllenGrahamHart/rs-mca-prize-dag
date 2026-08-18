#!/usr/bin/env python3
"""Independent two-fiber audit of the conjugate-band no-go."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def main() -> None:
    n, r, q, zeta = 16, 2, 97, 8
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) == q - 1
    first = (2, 10)
    second = (6, 14)
    count_a = count_b = joint = owner = 0
    for word in product((0, 1), repeat=n):
        a = all(sum(word[i] * pow(zeta, f * i, q) for i in range(n)) % q == 0
                for f in first)
        b = all(sum(word[i] * pow(zeta, f * i, q) for i in range(n)) % q == 0
                for f in second)
        assert a == b
        count_a += a
        count_b += b
        joint += a and b
        owner += a and b and all(
            word[i] == word[i + n // 2] for i in range(n // 2)
        )
    assert (count_a, count_b, joint, owner) == (36**r, 36**r, 36**r, 4**r)
    primitive = joint - owner
    ratio = Fraction(primitive * (1 << n), count_a * count_b)
    assert ratio == Fraction(64, 9) ** r * (1 - Fraction(1, 9) ** r)
    print(
        "DLI_CYCLIC_CONJUGATE_PRIMITIVE_NO_GO_AUDIT_PASS "
        f"n=16 marginal={count_a} owner={owner} primitive={primitive} "
        f"ratio={ratio.numerator}/{ratio.denominator}"
    )


if __name__ == "__main__":
    main()

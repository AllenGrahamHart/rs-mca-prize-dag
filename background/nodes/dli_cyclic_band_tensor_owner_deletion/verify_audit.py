#!/usr/bin/env python3
"""Independent order-16 audit of cyclic-band localization."""

from __future__ import annotations

from itertools import product


def main() -> None:
    r, n, q, zeta = 4, 16, 17, 3
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) == q - 1
    first = (1, 5, 9, 13)
    second = (2, 6, 10, 14)
    e1 = e2 = joint = primitive = 0
    for word in product((0, 1), repeat=n):
        a = all(sum(word[i] * pow(zeta, f * i, q) for i in range(n)) % q == 0
                for f in first)
        b = all(sum(word[i] * pow(zeta, f * i, q) for i in range(n)) % q == 0
                for f in second)
        e1 += a
        e2 += b
        joint += a and b
        primitive += a and b and any(
            word[i] != word[i + n // 2] for i in range(n // 2)
        )
    assert (e1, e2, joint, primitive) == (4**r, 6**r, 2**r, 0)
    assert joint * (1 << n) * 3**r == e1 * e2 * 4**r
    print(
        "DLI_CYCLIC_BAND_TENSOR_OWNER_AUDIT_PASS "
        "n=16 counts=256,1296,16 ratio=256/81 primitive_joint=0"
    )


if __name__ == "__main__":
    main()

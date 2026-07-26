#!/usr/bin/env python3
"""Independent finite-field audit of the two coefficient equations."""

from __future__ import annotations


def equations(h: int, x: int, y: int, p: int, constant_shift: int = 0) -> tuple[int, int]:
    e2 = -h * x * x - h * x * y - 2 * x - y + 1
    e3 = (
        -3 * h * h * x**3
        - 3 * h * h * x * x * y
        + 2 * h * x**3
        - 9 * h * x * x
        - 2 * h * x * y * y
        - 6 * h * x * y
        + 3 * h * x
        + 6 * x * x
        - 12 * x
        - 2 * y * y
        - 3 * y
        + 5
        + constant_shift
    )
    return e2 % p, e3 % p


def solutions(h: int, p: int, constant_shift: int = 0) -> set[tuple[int, int]]:
    return {
        (x, y)
        for x in range(p)
        for y in range(1, p)
        if equations(h, x, y, p, constant_shift) == (0, 0)
    }


def main() -> None:
    checks = 0
    for h, primes in ((7, (11, 13, 17, 19)), (15, (17, 19, 23, 29))):
        for p in primes:
            got = solutions(h, p)
            want = {(0, 1), (1, p - 1)}
            assert got == want, (h, p, got)
            derived = {((1 + h * x) * pow(y, -1, p)) % p for x, y in got}
            assert derived == {1, (-(h + 1)) % p}
            checks += 1

    mutations = 0
    for h, p in ((7, 17), (15, 19)):
        mutations += solutions(h, p, constant_shift=1) != {(0, 1), (1, p - 1)}
    assert mutations == 2

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_LINEAR_COLOR_EXCLUSION_AUDIT_PASS "
        f"finite_fields={checks} mutations={mutations}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent guard audit for the three product-base certificates."""


PRIMES = (13, 17, 29)


def admissible_cell14(prime, c, r):
    return c not in (0, 1, prime - 1) and pow(c, 2, prime) != 1 \
        and r != 0 and pow(r, 2, prime) not in (1, prime - 1)


def main():
    checked = 0
    for prime in PRIMES:
        for c in range(prime):
            for r in range(prime):
                if not admissible_cell14(prime, c, r):
                    continue
                checked += 1
                assert (-(pow(c, 2, prime) - 1)
                        * (pow(r, 4, prime) - 1)) % prime != 0
    assert checked > 0
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_THREE_ORBIT_AUDIT_PASS "
        f"cell14_guard_points={checked} primes={len(PRIMES)}"
    )


if __name__ == "__main__":
    main()

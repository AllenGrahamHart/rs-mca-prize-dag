#!/usr/bin/env python3
"""Independent cell-5 eliminant audit."""


def main():
    checked = 0
    for prime in (13, 17, 29):
        for r_value in range(prime):
            for t_value in range(prime):
                for c_value in range(prime):
                    s_value = (r_value + t_value) % prime
                    b_value = ((r_value + 1) * (t_value + 1)) % prime
                    c_factor = ((r_value - 1) * (t_value - 1)) % prime
                    left = (
                        (c_value * b_value + c_factor)
                        * (c_value * c_factor + b_value)
                        - 4 * c_value * s_value * s_value
                    ) % prime
                    right = (b_value * c_factor
                             * (c_value + 1) ** 2) % prime
                    assert left == right
                    checked += 1
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_FIVE_ORBIT_AUDIT_PASS "
        f"cell5_identity_points={checked}"
    )


if __name__ == "__main__":
    main()

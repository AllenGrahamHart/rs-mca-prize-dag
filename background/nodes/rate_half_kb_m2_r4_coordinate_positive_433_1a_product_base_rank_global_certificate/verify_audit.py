#!/usr/bin/env python3
"""Independent audit of the cell-3 factor identities and guard map."""


def main():
    identity_checks = 0
    guard_checks = 0
    for prime in (13, 17, 29):
        inverse_three = pow(3, -1, prime)
        for r_value in range(prime):
            for t_value in range(prime):
                u_value = (-r_value * r_value - 3 * r_value * t_value
                           + 3 * r_value + t_value) % prime
                v_value = (-r_value * r_value + r_value * t_value
                           - r_value + t_value) % prime
                expected = (8 * r_value * (t_value - 1)
                            * (r_value - 1) * (r_value + t_value)) % prime
                assert (u_value * u_value - v_value * v_value) % prime == expected
                identity_checks += 1
                guard = (r_value * t_value * (r_value - 1) * (r_value + 1)
                         * (t_value - 1) * (t_value + 1)
                         * (t_value - r_value) * (t_value + r_value)) % prime
                if guard:
                    guard_checks += 1
        assert inverse_three * 3 % prime == 1
    assert guard_checks > 0
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_GLOBAL_AUDIT_PASS "
        f"cell3_identity_points={identity_checks} source_guard_points={guard_checks}"
    )


if __name__ == "__main__":
    main()

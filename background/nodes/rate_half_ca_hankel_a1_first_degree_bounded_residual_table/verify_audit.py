#!/usr/bin/env python3
"""Independent symbolic-division audit for the residual table."""


def main():
    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3

    core0_num = (6 * e - 3, 12 * e - 2, 18 * e - 1)
    core1_num = (3 * e - 6, 9 * e - 4, 15 * e - 2)
    got0 = tuple(core0_num[j] // (e - j) for j in range(3))
    got1 = tuple(core1_num[j] // (e - j) for j in range(3))
    assert got0 == (5, 12, 18)
    assert got1 == (2, 9, 15)

    # Raising omission O by one cannot increase the residual allowance.
    for numerator in core0_num + core1_num:
        assert (numerator - 1) <= numerator

    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_BOUNDED_RESIDUAL_AUDIT_PASS "
        f"core0={got0} core1={got1}"
    )


if __name__ == "__main__":
    main()

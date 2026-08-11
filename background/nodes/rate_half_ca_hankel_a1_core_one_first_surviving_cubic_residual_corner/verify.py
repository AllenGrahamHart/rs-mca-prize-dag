#!/usr/bin/env python3
"""Exact official arithmetic for the first cubic-residual corner."""


def main():
    m = 1 << 37
    rho = 4 * m
    e = (16 * m) // 13
    d = rho - 1
    delta = d - 2 * e
    quotient, residue = divmod(delta, 5)
    slack_max = 4 * e - rho - 1
    slack_min = e - 3 - quotient
    pole_min = 5 * quotient
    slopes = 4 * e + 1 - slack_max
    clean = slopes - delta

    assert 16 * m == 13 * e + 6
    assert e == 169155635042
    assert d == 549755813887
    assert delta == 211444543803
    assert (quotient, residue) == (42288908760, 3)
    assert slack_min == slack_max == 126866726279
    assert slopes == rho + 2 == 549755813890
    assert pole_min == delta - 3 == 211444543800
    assert clean == 2 * e + 3 == 338311270087

    for pole in range(pole_min, delta + 1):
        assert 0 <= delta - pole <= 3
        assert pole // 5 + slack_max + 3 >= e

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_FIRST_CUBIC_CORNER_PASS "
        f"e={e} slack={slack_max} pole_min={pole_min} clean={clean}"
    )


if __name__ == "__main__":
    main()

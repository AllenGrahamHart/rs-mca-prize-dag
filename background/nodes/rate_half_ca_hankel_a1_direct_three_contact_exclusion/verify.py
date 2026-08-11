#!/usr/bin/env python3
"""Exact official arithmetic for direct three-contact exclusion."""


def ceil_div(a, b):
    return -(-a // b)


def main():
    checked = 0
    for m in range(8, 1000):
        rho = 4 * m
        first = ceil_div(rho - 1, 3)
        for e in range(m + 1, first):
            for s, beta in ((0, 0), (1, 1)):
                ell_max = 4 * e + beta - rho - 2
                ell_min = e - 3 + beta
                assert ell_min > ell_max
                checked += 1

    m = 1 << 37
    rho = 4 * m
    first = ceil_div(rho - 1, 3)
    assert first == 183251937963
    assert 3 * first == rho + 1

    expected = {
        0: (first - 3, first - 2, first - 1),
        1: (first - 2, first - 1, first),
    }
    for s, beta in ((0, 0), (1, 1)):
        ell_min = first - 3 + beta
        ell_max = 4 * first + beta - rho - 2
        slacks = tuple(range(ell_min, ell_max + 1))
        slopes = tuple(4 * first + beta - ell for ell in slacks)
        assert slacks == expected[s]
        assert slopes == (rho + 4, rho + 3, rho + 2)

    print(
        "RATE_HALF_CA_HANKEL_A1_DIRECT_THREE_CONTACT_EXCLUSION_PASS "
        f"checked={checked} official_first={first}"
    )


if __name__ == "__main__":
    main()

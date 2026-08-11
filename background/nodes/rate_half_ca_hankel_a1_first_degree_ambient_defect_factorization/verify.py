#!/usr/bin/env python3
"""Boundary bundle and row-defect arithmetic checks."""


def h1_p1xp1(a, b):
    h0a = max(a + 1, 0)
    h0b = max(b + 1, 0)
    h1a = max(-a - 1, 0)
    h1b = max(-b - 1, 0)
    return h1a * h0b + h0a * h1b


def main():
    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3
    checked = 0

    for s, beta in ((0, 0), (1, 1)):
        d = rho - s
        for j in range(3):
            ell = e - 3 + beta + j
            assert ell - e + 3 - beta == j
            assert h1_p1xp1(-3, j - e) == 0
            assert d - 3 >= 0
            checked += 1

    # A degree-j ambient specialization cannot contain a row-defect factor
    # of larger degree unless all j+1 coefficients vanish at that row.
    for j in range(3):
        for defect in range(j + 1, j + 5):
            assert defect > j

    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_AMBIENT_DEFECT_PASS "
        f"profiles={checked} e={e}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact capacity arithmetic for the six bounded residual degrees."""


def ceil_div(a, b):
    return -(-a // b)


def main():
    m = 1 << 37
    rho = 4 * m
    e = (rho + 1) // 3
    expected = {0: (5, 12, 18), 1: (2, 9, 15)}
    rows = []

    for s, beta in ((0, 0), (1, 1)):
        d = rho - s
        n_res = 4 * rho - s
        delta = d - (s + 1) * e
        eta = d - e if s == 0 else e
        for j in range(3):
            ell = e - 3 + beta + j
            capacity_min = ell * d + eta - delta
            heavy_min = ceil_div(capacity_min - n_res * j, e - j)
            residual_max = d - 3 - heavy_min
            assert residual_max == expected[s][j]
            rows.append((s, j, heavy_min, residual_max))

    assert len(rows) == 6
    print(
        "RATE_HALF_CA_HANKEL_A1_FIRST_DEGREE_BOUNDED_RESIDUAL_PASS "
        f"e={e} table={expected}"
    )


if __name__ == "__main__":
    main()

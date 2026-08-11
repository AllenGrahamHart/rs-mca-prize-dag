#!/usr/bin/env python3
"""Official arithmetic replay for residual-pole interpolation."""


def check(m):
    assert m % 2 == 0 and m >= 6
    rho = 4 * m - 1
    n_domain = 16 * m
    n_slopes = 4 * m + 1
    ell = m // 2 - 1

    h0_interpolants = 2 * (ell + 1)
    assert h0_interpolants == m > m - 1

    forney = (-rho - 3, m + 1)
    grid = (n_domain + 1, ell - n_slopes)
    target = (4 * forney[0] + grid[0], 4 * forney[1] + grid[1])
    assert target == (-7, ell + 3)

    kernel = (target[0] - rho, target[1] - m)
    assert kernel == (-rho - 7, 2 - m // 2)
    assert kernel[0] < 0 and kernel[1] < 0
    return rho, ell


def main():
    profiles = 0
    for m in range(6, 128, 2):
        check(m)
        profiles += 1

    official_m = 1 << 37
    official_rho, official_ell = check(official_m)
    profiles += 1

    # Mutation controls: one fewer interpolation coordinate or three Forney
    # copies no longer proves the required target.
    m = 20
    ell = m // 2 - 1
    assert 2 * ell <= m - 1
    rho = 4 * m - 1
    three_copy = (
        3 * (-rho - 3) + 16 * m + 1,
        3 * (m + 1) + ell - (4 * m + 1),
    )
    assert three_copy != (-7, ell + 3)

    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_RESIDUAL_POLE_INTERPOLATION_EXCLUSION_PASS "
        f"profiles={profiles} official_m={official_m} "
        f"official_rho={official_rho} official_ell={official_ell}"
    )


if __name__ == "__main__":
    main()

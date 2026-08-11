#!/usr/bin/env python3
"""Degree replay for the strict A=3 Forney contact section."""


def check(m, e):
    rho = 4 * m - 1
    assert m <= e <= rho // 3
    delta = rho - 3 * e
    contact = 2 * rho + 2
    residual = (rho - 1 - contact, e + 1)
    assert residual == (-rho - 3, e + 1)
    degree = residual[0] * e + residual[1] * rho
    assert degree == delta
    assert contact == 8 * m
    assert 3 * e + 2 > e
    return rho, delta


def main():
    profiles = 0
    for m in range(2, 96):
        rho = 4 * m - 1
        for e in range(m, rho // 3 + 1):
            check(m, e)
            profiles += 1

    official_m = 1 << 37
    official_e = (4 * official_m - 1) // 3
    official_rho, official_delta = check(official_m, official_e)
    profiles += 1

    rho, _ = check(13, 14)
    mutated = (rho - 1 - (2 * rho + 1), 15)
    assert mutated != (-rho - 3, 15)

    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_FORNEY_INFINITY_CONTACT_SECTION_PASS "
        f"profiles={profiles} official_m={official_m} official_e={official_e} "
        f"official_rho={official_rho} official_delta={official_delta}"
    )


if __name__ == "__main__":
    main()

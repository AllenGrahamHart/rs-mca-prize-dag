#!/usr/bin/env python3
"""Degree replay for the universal Forney contact section."""


def check(m):
    rho = 4 * m - 1
    contact = 2 * rho + 2
    residual = (rho - 1 - contact, m + 1)
    assert residual == (-rho - 3, m + 1)
    degree = residual[0] * m + residual[1] * rho
    assert degree == m - 1
    assert contact == 8 * m
    return rho


def main():
    profiles = 0
    for m in range(2, 96):
        check(m)
        profiles += 1
    official_m = 1 << 37
    official_rho = check(official_m)
    profiles += 1

    rho = check(13)
    mutated = (rho - 1 - (2 * rho + 1), 14)
    assert mutated != (-rho - 3, 14)

    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_FORNEY_INFINITY_CONTACT_SECTION_PASS "
        f"profiles={profiles} official_m={official_m} official_rho={official_rho}"
    )


if __name__ == "__main__":
    main()

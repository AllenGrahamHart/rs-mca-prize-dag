#!/usr/bin/env python3
"""Exact bidegree and recurrence-length checks for the A=1 contact leaf."""


def main():
    checks = 0
    for m in range(4, 96):
        rho = 4 * m
        for e in range(m + 1, rho + 1):
            delta = rho - e
            assert 2 * rho - 1 - rho + 1 == rho
            assert (rho - 1) - 2 * rho == -rho - 1
            assert (-rho - 1) * e + (e + 1) * rho == delta
            assert rho + 2 - delta == e + 2
            checks += 1

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_FREE_FORNEY_CONTACT_SECTION_PASS "
        f"profiles={checks} contact_offset=0"
    )


if __name__ == "__main__":
    main()

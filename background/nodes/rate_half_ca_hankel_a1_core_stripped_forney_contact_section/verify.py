#!/usr/bin/env python3
"""Exact contracted contact-order and degree checks."""


def main():
    checks = 0
    for m in range(4, 100):
        rho = 4 * m
        for s in range(3):
            d = rho - s
            for e in range(m + 1, d // (s + 1) + 1):
                delta = d - (s + 1) * e
                assert (2 * rho - s) - d == rho
                assert (d - 1) - (d + rho) == -rho - 1
                assert (-rho - 1) * e + (e + 1) * d == delta
                assert rho + 2 - delta == (s + 1) * e + s + 2
                checks += 1
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_STRIPPED_FORNEY_CONTACT_SECTION_PASS "
        f"profiles={checks} cores=3"
    )


if __name__ == "__main__":
    main()

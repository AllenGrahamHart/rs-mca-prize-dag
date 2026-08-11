#!/usr/bin/env python3
"""Mutation audit for contracted row and contact counts."""


def main():
    rho, s, e = 40, 2, 11
    d = rho - s
    contact = d + rho
    assert contact == 78
    assert (d - 1) - contact == -rho - 1
    assert (-rho - 1) * e + (e + 1) * d == d - 3 * e
    mutated = 2 * d
    assert mutated != contact
    assert (d - 1) - mutated != -rho - 1
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_STRIPPED_FORNEY_CONTACT_SECTION_AUDIT_PASS "
        "mutation=two_residual_degrees_detected"
    )


if __name__ == "__main__":
    main()

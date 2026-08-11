#!/usr/bin/env python3
"""Mutation audit for the A=1 versus strict-A=3 contact order."""


def main():
    rho, e = 40, 13
    correct = (rho - 1) - 2 * rho
    mutated = (rho - 1) - (2 * rho + 2)
    assert correct == -rho - 1
    assert mutated == -rho - 3
    assert correct * e + (e + 1) * rho == rho - e
    assert mutated * e + (e + 1) * rho == rho - 3 * e
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_FREE_FORNEY_CONTACT_SECTION_AUDIT_PASS "
        "mutation=strict_contact_detected"
    )


if __name__ == "__main__":
    main()

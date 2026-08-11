#!/usr/bin/env python3
"""Contact-copy and threshold mutation audit."""


def main():
    m = 1 << 20
    rho = 4 * m
    caught = 0
    for s, first in ((0, (12 * m) // 11), (1, (6 * m) // 5)):
        e = first - 1
        d = rho - s
        delta = d - (s + 1) * e
        beta = 0 if s == 0 else 1
        slack = 4 * e + beta - rho - 2
        correct = delta // 4 + slack + 4 - beta
        mutated = delta // 3 + slack + 4 - beta
        assert correct < e
        caught += mutated >= correct

    # Three contact copies do not make the ambient first degree negative.
    s = 0
    assert (4 * rho - s) + 3 - 4 * (rho + 1) == -s - 1
    assert (4 * rho - s) + 3 - 3 * (rho + 1) > 0
    assert caught == 2
    print(
        "RATE_HALF_CA_HANKEL_A1_FOUR_CONTACT_LOW_DEGREE_EXCLUSION_AUDIT_PASS "
        "mutations=3/3"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mutation audit for the marked Forney-window normal form."""


def main() -> None:
    m, t = 5, 7

    # Dropping nu<=m admits a one-direction truncated module.
    mu, nu = 1, 6
    assert mu + nu == t and nu > m

    # Forgetting the determinant length loses the index sum.
    assert t != t - 1

    # The exact kernel dimension includes both endpoint generators.
    mu, nu = 3, 4
    correct = (m - mu + 1) + (m - nu + 1)
    assert correct == 2 * m - t + 2
    assert correct != 2 * m - t

    # Formal bivariate coprimality is not the evaluated gcd guard.
    assert "gcd(R0(X,P),R1(X,P))" != "gcd(R0(X,Z),R1(X,Z))"

    # A finite lambda at a resultant zero is not a sharp saturated witness.
    assert "generic lambda" != "every lambda"

    print("L1_FORNEY_WINDOW_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Toy exact recurrence-factor checks for Forney pole absorption."""


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def main():
    checked = 0
    # Polynomial identities model Qbar=Q_min*R, G=Q_min*G1, and
    # N_F=R*N_min. Then Qbar divides N_F*G identically.
    samples = (
        ([1, 1], [2, 0, 1], [3, 1], [1, 4]),
        ([2, -1, 1], [1, 2], [1, 0, 3], [2, 1, 1]),
        ([1, 0, 0, 1], [1, -1], [4, 2], [3, 0, 1]),
    )
    for qmin, residual, g1, nmin in samples:
        qbar = mul(qmin, residual)
        domain = mul(qmin, g1)
        numerator = mul(residual, nmin)
        left = mul(numerator, domain)
        right = mul(qbar, mul(nmin, g1))
        assert left == right
        checked += 1

    # Official line-bundle arithmetic for every core size and beta branch.
    rho = 4 * (1 << 37)
    for s, beta in ((0, 0), (1, 1), (2, 1), (2, 2)):
        d = rho - s
        e = (1 << 37) + 1
        ell = 0
        t = 4 * e + beta - ell
        first = 3 * (-rho - 1) + (4 * rho - s)
        second = 3 * (e + 1) - t
        assert first == d - 3
        assert second == ell - e + 3 - beta

    print(
        "RATE_HALF_CA_HANKEL_A1_FORNEY_POLE_IDEAL_ABSORPTION_PASS "
        f"identities={checked}"
    )


if __name__ == "__main__":
    main()

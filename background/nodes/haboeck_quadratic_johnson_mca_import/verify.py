#!/usr/bin/env python3
"""Replay the exact algebra in the Haboeck theorem convention bridge."""

from fractions import Fraction


def main() -> None:
    for n, dimension, m in [(32, 16, 3), (8192, 4096, 9), (1 << 41, 1 << 40, 95)]:
        d = dimension - 1
        rho = Fraction(d, n)

        # Square the source expression to avoid introducing a numerical
        # square root: ((ell^7/3)*(rho*n)^2)^2.
        source_squared = (
            Fraction(2 * m + 1, 2) ** 14
            * rho ** -7
            * (rho * n) ** 4
            / 9
        )
        specialized_squared = Fraction(
            (2 * m + 1) ** 14 * n**7,
            384**2 * d**3,
        )
        assert source_squared == specialized_squared

        # The agreement threshold is
        # (1+1/(2m))*sqrt(rho)*n.
        agreement_squared = Fraction((2 * m + 1) ** 2 * n * d, (2 * m) ** 2)
        source_agreement_squared = (
            Fraction(2 * m + 1, 2 * m) ** 2 * rho * n**2
        )
        assert agreement_squared == source_agreement_squared

    print("HABOECK_QUADRATIC_JOHNSON_MCA_IMPORT_PASS")


if __name__ == "__main__":
    main()

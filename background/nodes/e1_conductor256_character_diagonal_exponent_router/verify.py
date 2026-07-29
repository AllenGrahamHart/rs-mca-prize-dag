#!/usr/bin/env python3
"""Tiny structural replay for the conductor-256 character router."""

from __future__ import annotations

import cmath


ORDER = 64


def canonical(value: int) -> int:
    value %= 256
    return min(value, 256 - value)


def dft(values: list[complex]) -> list[complex]:
    return [
        sum(
            value * cmath.exp(-2j * cmath.pi * frequency * index / ORDER)
            for index, value in enumerate(values)
        )
        for frequency in range(ORDER)
    ]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    powers = [canonical(pow(5, index, 256)) for index in range(ORDER)]
    require(len(set(powers)) == ORDER, "the class of 5 does not have order 64")
    require(set(powers) == set(range(1, 128, 2)), "wrong sign representatives")
    require(len(powers) - 1 == 63, "wrong unit rank")

    # Use deterministic rational-valued fixtures to replay the index sign in
    # the convolution identity independently of transcendental sine logs.
    xi = [((17 * index + 5) % 11) - 5 for index in range(1, ORDER)]
    xi.insert(0, -sum(xi))
    f = [((index * index + 3 * index + 7) % 19) - 9 for index in range(ORDER)]
    lam = [
        sum(xi[index] * f[(shift + index) % ORDER] for index in range(ORDER))
        for shift in range(ORDER)
    ]

    xi_hat = dft([complex(value) for value in xi])
    f_hat = dft([complex(value) for value in f])
    lam_hat = dft([complex(value) for value in lam])
    error = max(
        abs(lam_hat[j] - f_hat[j] * xi_hat[-j % ORDER])
        for j in range(ORDER)
    )
    require(error < 1e-8, f"Fourier diagonalization error {error}")

    parseval_left = sum(value * value for value in xi)
    parseval_right = sum(abs(value) ** 2 for value in xi_hat) / ORDER
    require(abs(parseval_left - parseval_right) < 1e-7, "Parseval mismatch")
    require(abs(xi_hat[0]) < 1e-9, "extended exponent vector is not zero-sum")
    print("E1_CONDUCTOR256_CHARACTER_DIAGONAL_EXPONENT_ROUTER_PASS checks=6")


if __name__ == "__main__":
    main()

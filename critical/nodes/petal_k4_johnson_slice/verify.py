#!/usr/bin/env python3
"""Exact arithmetic and tiny-field replay of the K4 Johnson slice."""

from itertools import product


def bound(ell: int, d: int, agreement: int) -> int:
    gap = agreement * agreement - d * ell
    if gap <= 0:
        raise ValueError("outside the strict Johnson regime")
    return ell * (agreement - d) // gap


def eval_poly(coeffs: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coeff in reversed(coeffs):
        value = (value * x + coeff) % prime
    return value


def brute_cell(prime: int, ell: int, d: int, agreement: int) -> int:
    domain = range(ell)
    codewords = [
        tuple(eval_poly(coeffs, x, prime) for x in domain)
        for coeffs in product(range(prime), repeat=d + 1)
    ]
    worst = 0
    for word in product(range(prime), repeat=ell):
        size = sum(
            sum(a == b for a, b in zip(codeword, word)) >= agreement
            for codeword in codewords
        )
        worst = max(worst, size)
    return worst


def main() -> None:
    arithmetic_rows = 0
    for ell in range(2, 65):
        for d in range(ell):
            for agreement in range(1, ell + 1):
                if agreement * agreement <= d * ell:
                    continue
                value = bound(ell, d, agreement)
                if value < 1 or value > ell * ell:
                    raise AssertionError((ell, d, agreement, value))
                arithmetic_rows += 1

    brute_rows = 0
    for prime, ell in ((3, 3), (5, 4)):
        for d in range(min(3, ell)):
            for agreement in range(1, ell + 1):
                if agreement * agreement <= d * ell:
                    continue
                actual = brute_cell(prime, ell, d, agreement)
                if actual > bound(ell, d, agreement):
                    raise AssertionError(
                        (prime, ell, d, agreement, actual, bound(ell, d, agreement))
                    )
                brute_rows += 1

    try:
        bound(4, 1, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("non-strict Johnson mutation was accepted")

    print(
        "PETAL_K4_JOHNSON_SLICE_PASS "
        f"arithmetic_rows={arithmetic_rows} brute_rows={brute_rows}"
    )


if __name__ == "__main__":
    main()

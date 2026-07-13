#!/usr/bin/env python3
"""Finite-field replay of retained-zero factorization and support preservation."""

from itertools import product


def eval_poly(coeffs: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coeff in reversed(coeffs):
        value = (value * x + coeff) % prime
    return value


def multiply(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return tuple(out)


def locator(points: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = multiply(out, ((-point) % prime, 1), prime)
    return out


def main() -> None:
    prime = 7
    retained = (4, 5)
    domain = (0, 1, 2, 3)
    degree = 3
    effective = degree - len(retained)
    loc = locator(retained, prime)
    factors = [tuple(c) for c in product(range(prime), repeat=effective + 1)]
    rows = 0

    for word in product(range(prime), repeat=len(domain)):
        transformed = tuple(
            value * pow(eval_poly(loc, x, prime), -1, prime) % prime
            for x, value in zip(domain, word)
        )
        for agreement in range(len(domain) + 1):
            left: list[tuple[int, ...]] = []
            right: list[tuple[int, ...]] = []
            for quotient in factors:
                poly = multiply(loc, quotient, prime)
                support_g = tuple(
                    x for x, value in zip(domain, word)
                    if eval_poly(poly, x, prime) == value
                )
                support_q = tuple(
                    x for x, value in zip(domain, transformed)
                    if eval_poly(quotient, x, prime) == value
                )
                if support_g != support_q:
                    raise AssertionError((word, quotient, support_g, support_q))
                if len(support_g) >= agreement:
                    left.append(poly)
                    right.append(quotient)
            if len(left) != len(right) or len(set(left)) != len(left):
                raise AssertionError((word, agreement, len(left), len(right)))
            rows += 1

    try:
        pow(eval_poly(locator((0,), prime), 0, prime), -1, prime)
    except ValueError:
        pass
    else:
        raise AssertionError("overlapping retained/evaluation sets were accepted")

    print(
        "PETAL_RETAINED_ZERO_EFFECTIVE_DEGREE_PASS "
        f"rows={rows} quotients={len(factors)} exact_support=preserved"
    )


if __name__ == "__main__":
    main()

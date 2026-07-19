#!/usr/bin/env python3
"""Audit canonical-span extraction and full-equality rejection."""

from __future__ import annotations


PRIME = 1009


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return trim(answer)


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def main() -> None:
    cases = mutations = 0
    for h in range(4, 65):
        b_poly = [1] + [((5 * index + h) % 17) - 8 for index in range(1, 2 * h - 2)]
        c_poly = [1] + [((7 * index + h) % 11) - 5 for index in range(1, h - 2)]
        alpha = (3 * h + 1) % PRIME or 1
        beta = (5 * h + 2) % PRIME
        gamma = (7 * h + 3) % PRIME

        b2 = multiply(b_poly, b_poly)
        c2 = multiply(c_poly, c_poly)
        c3 = multiply(c2, c_poly)
        c4 = multiply(c2, c2)
        rbar = add(
            scale(multiply(b2, c2), alpha),
            scale(shift(multiply(b_poly, c3), h), beta),
        )
        rbar = add(rbar, scale(shift(c4, 2 * h), gamma))
        s_poly = add(rbar, scale(multiply(b2, c2), -alpha))
        x_poly = shift(multiply(b_poly, c3), h)
        y_poly = shift(c4, 2 * h)
        got_beta = s_poly[h]
        after_beta = add(s_poly, scale(x_poly, -got_beta))
        got_gamma = after_beta[2 * h]
        assert got_beta == beta
        assert got_gamma == gamma
        assert add(after_beta, scale(y_poly, -got_gamma)) == [0]

        mutated = rbar.copy()
        mutated[-1] = (mutated[-1] + 1) % PRIME
        mutated_s = add(mutated, scale(multiply(b2, c2), -alpha))
        mutation_beta = mutated_s[h]
        mutation_after_beta = add(mutated_s, scale(x_poly, -mutation_beta))
        mutation_gamma = mutation_after_beta[2 * h]
        assert add(mutation_after_beta, scale(y_poly, -mutation_gamma)) != [0]
        cases += 1
        mutations += 1

    print(
        "AUDIT_RATE_HALF_ANTIPODAL_GENERIC_CANONICAL_SPAN_PASS "
        f"prime={PRIME} exact_profiles={cases} full_equality_mutations={mutations}"
    )


if __name__ == "__main__":
    main()

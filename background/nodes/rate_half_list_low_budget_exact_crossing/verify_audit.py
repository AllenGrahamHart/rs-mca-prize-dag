#!/usr/bin/env python3
"""Independent audit of the budget-two quarter-coset construction."""

from __future__ import annotations


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in coefficients[::-1]:
        value = (value * x + coefficient) % prime
    return value


def convolve(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return tuple(answer)


def product_of_roots(roots: tuple[int, ...], prime: int) -> tuple[int, ...]:
    answer = (1,)
    for root in roots:
        answer = convolve(answer, ((-root) % prime, 1), prime)
    return answer


def replay(multiplier_offset: int) -> tuple[int, ...]:
    prime, length, primitive, coset = 97, 16, 5, 5
    quarter = length // 4
    zeta = pow(primitive, (prime - 1) // length, prime)
    fourth_root = pow(zeta, quarter, prime)
    domain = tuple(coset * pow(zeta, j, prime) % prime for j in range(length))
    scale = pow(pow(coset, quarter, prime), -1, prime)
    y_values = tuple(pow(x, quarter, prime) * scale % prime for x in domain)
    minus_i = (-fourth_root) % prime
    roots = tuple(x for x, y in zip(domain, y_values, strict=True) if y == minus_i)[1:]
    common = product_of_roots(roots, prime)
    first_factor = (prime - 1,) + (0,) * (quarter - 1) + (scale,)
    multiplier = (fourth_root + multiplier_offset) % prime
    second_factor = (multiplier,) + (0,) * (quarter - 1) + (multiplier * scale % prime,)
    polys = ((0,), convolve(common, first_factor, prime), convolve(common, second_factor, prime))
    words = tuple(tuple(evaluate(poly, x, prime) for x in domain) for poly in polys)
    received = tuple(words[1][j] if y == fourth_root else 0 for j, y in enumerate(y_values))
    return tuple(sum(x == y for x, y in zip(word, received, strict=True)) for word in words)


def main() -> None:
    valid = replay(0)
    mutated = replay(1)
    assert valid == (12, 11, 11)
    assert min(mutated) < 11
    print(
        "AUDIT_RATE_HALF_LIST_LOW_BUDGET_EXACT_CROSSING_PASS "
        f"valid={valid} mutation_rejected={mutated}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replay the H3 line-star identity and its two exclusion guards."""

from __future__ import annotations

from collections import Counter


ROWS = ((97, 32), (4289, 64))


def prime_factors(value: int) -> tuple[int, ...]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return tuple(factors)


def subgroup(prime: int, order: int) -> tuple[int, ...]:
    factors = prime_factors(prime - 1)
    generator = next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )
    step = pow(generator, (prime - 1) // order, prime)
    roots = tuple(pow(step, exponent, prime) for exponent in range(order))
    if len(set(roots)) != order:
        raise AssertionError((prime, order, "subgroup order"))
    return roots


def replay(prime: int, order: int) -> tuple[int, int]:
    shifted = tuple((1 - root) % prime for root in subgroup(prime, order) if root != 1)
    shifted_set = set(shifted)

    product: Counter[int] = Counter()
    quotient: Counter[int] = Counter()
    diagonal: Counter[int] = Counter()
    for left in shifted:
        diagonal[left * left % prime] += 1
        inverse = pow(left, -1, prime)
        for right in shifted:
            product[left * right % prime] += 1
            quotient[right * inverse % prime] += 1

    expected_q = Counter(
        {
            target: multiplicity * (multiplicity - 2) + diagonal[target]
            for target, multiplicity in product.items()
        }
    )
    emitted: Counter[int] = Counter()
    include_source_identity = Counter()
    include_source_diagonal = Counter()
    for slope in range(1, prime):
        fiber = tuple(value for value in shifted if slope * value % prime in shifted_set)
        if len(fiber) != quotient[slope]:
            raise AssertionError((prime, order, slope, "fiber"))
        for left in fiber:
            for right in fiber:
                target = slope * left * right % prime
                if slope != 1 and left != right:
                    emitted[target] += 1
                if left != right:
                    include_source_identity[target] += 1
                if slope != 1:
                    include_source_diagonal[target] += 1

    if emitted != expected_q:
        raise AssertionError((prime, order, "LS1"))
    if include_source_identity == expected_q:
        raise AssertionError((prime, order, "m=1 guard"))
    if include_source_diagonal == expected_q:
        raise AssertionError((prime, order, "a=a' guard"))

    direct = sum(expected_q[target] * quotient[target] for target in expected_q if target != 1)
    line_star = sum(emitted[target] * quotient[target] for target in emitted if target != 1)
    if direct != line_star:
        raise AssertionError((prime, order, direct, line_star, "LS2"))
    return direct, max(quotient.values())


def main() -> None:
    results = tuple(replay(*row) for row in ROWS)
    print(
        "H3_LINE_STAR_MOMENT_IDENTITY_PASS "
        f"rows={len(ROWS)} moments={','.join(str(result[0]) for result in results)}"
    )


if __name__ == "__main__":
    main()


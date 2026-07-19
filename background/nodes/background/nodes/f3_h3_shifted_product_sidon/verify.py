#!/usr/bin/env python3
"""Replay the dyadic shifted-product Sidon theorem and finite collisions."""

from __future__ import annotations

from collections import defaultdict


def folded_alpha(order: int, x: int, y: int, u: int, v: int) -> tuple[int, ...]:
    """Coefficient vector modulo Phi_{2^s}(X)=X^(n/2)+1."""
    half = order // 2
    coefficients = [0] * half
    for exponent, coefficient in (
        (x + y, 1),
        (x, -1),
        (y, -1),
        (u + v, -1),
        (u, 1),
        (v, 1),
    ):
        exponent %= order
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        coefficients[exponent] += coefficient
    return tuple(coefficients)


def exact_char_zero_replay(order: int) -> int:
    checked = 0
    for x in range(1, order):
        for y in range(1, order):
            for u in range(1, order):
                for v in range(1, order):
                    if any(folded_alpha(order, x, y, u, v)):
                        continue
                    if sorted((x, y)) != sorted((u, v)):
                        raise AssertionError((order, x, y, u, v))
                    checked += 1
    return checked


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


def subgroup_with_exponents(prime: int, order: int) -> tuple[tuple[int, int], ...]:
    generator = next(
        candidate
        for candidate in range(2, prime)
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in prime_factors(prime - 1)
        )
    )
    root = pow(generator, (prime - 1) // order, prime)
    return tuple((exponent, pow(root, exponent, prime)) for exponent in range(1, order))


def finite_collision_replay(prime: int, order: int) -> tuple[int, int, int]:
    roots = subgroup_with_exponents(prime, order)
    shifted = tuple((exponent, (1 - root) % prime) for exponent, root in roots)
    products: dict[int, list[tuple[int, int]]] = defaultdict(list)
    quotient: dict[int, int] = defaultdict(int)
    diagonal: dict[int, int] = defaultdict(int)
    for left_exp, left in shifted:
        diagonal[left * left % prime] += 1
        inverse = pow(left, -1, prime)
        for right_exp, right in shifted:
            products[left * right % prime].append((left_exp, right_exp))
            quotient[right * inverse % prime] += 1

    collisions = 0
    for representations in products.values():
        for first in representations:
            for second in representations:
                if second == first or second == first[::-1]:
                    continue
                if not any(folded_alpha(order, *first, *second)):
                    raise AssertionError((prime, order, first, second))
                collisions += 1

    q_value = {
        target: len(representations) * (len(representations) - 2)
        + diagonal[target]
        for target, representations in products.items()
    }
    if collisions != sum(q_value.values()):
        raise AssertionError((prime, order, "Q total"))
    quotient_excess = sum(
        multiplicity * (multiplicity - 1)
        for target, multiplicity in quotient.items()
        if target != 1
    )
    if collisions != quotient_excess:
        raise AssertionError((prime, order, collisions, quotient_excess))

    direct = sum(
        q_value.get(target, 0) * multiplicity
        for target, multiplicity in quotient.items()
        if target != 1
    )
    single = sum(
        q_value.get(target, 0)
        for target, multiplicity in quotient.items()
        if target != 1 and multiplicity > 0
    )
    double = sum(
        q_value.get(target, 0) * (multiplicity - 1)
        for target, multiplicity in quotient.items()
        if target != 1
    )
    if direct != single + double:
        raise AssertionError((prime, order, direct, single, double))
    return collisions, single, double


def main() -> None:
    exact = sum(exact_char_zero_replay(order) for order in (4, 8, 16, 32))
    finite = tuple(
        finite_collision_replay(prime, order)
        for prime, order in ((97, 32), (257, 16), (4289, 64))
    )
    if not any(row[0] for row in finite):
        raise AssertionError("finite-characteristic mutation had no collisions")
    print(
        "H3_SHIFTED_PRODUCT_SIDON_PASS "
        f"char0_equalities={exact} "
        f"finite_collisions={','.join(str(row[0]) for row in finite)} "
        f"double_accidents={','.join(str(row[2]) for row in finite)}"
    )


if __name__ == "__main__":
    main()

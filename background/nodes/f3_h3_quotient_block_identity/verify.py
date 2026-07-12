#!/usr/bin/env python3
"""Replay the quotient coefficient-coset block identity."""

from __future__ import annotations

from collections import Counter, defaultdict


ROWS = ((97, 32), (4_289, 64), (7_937, 64))


def factors(value: int) -> tuple[int, ...]:
    out: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            out.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        out.append(value)
    return tuple(out)


def verify(prime: int, order: int) -> None:
    group_order = prime - 1
    primitive = next(
        value
        for value in range(2, prime)
        if all(pow(value, group_order // q, prime) != 1 for q in factors(group_order))
    )
    logs = [0] * prime
    value = 1
    for exponent in range(group_order):
        logs[value] = exponent
        value = value * primitive % prime
    root_generator = pow(primitive, group_order // order, prime)
    roots = tuple(pow(root_generator, exponent, prime) for exponent in range(order))
    shifted = tuple((1 - root) % prime for root in roots if root != 1)
    quotient = Counter(
        left * pow(right, -1, prime) % prime
        for left in shifted
        for right in shifted
    )

    index = group_order // order
    blocks: dict[tuple[int, int], list[int]] = defaultdict(list)
    for parameter in range(2, prime):
        u = pow((1 - parameter) % prime, -1, prime)
        v = -parameter * u % prime
        blocks[(logs[u] % index, logs[v] % index)].append(parameter)

    collision_sum = 0
    for parameters in blocks.values():
        multiplicity = len(parameters) - 1
        if any(quotient[parameter] != multiplicity for parameter in parameters):
            raise AssertionError((prime, order, parameters[:3], multiplicity))
        collision_sum += len(parameters) * multiplicity
    if collision_sum != (order - 1) * (order - 2):
        raise AssertionError((prime, order, collision_sum))


def main() -> None:
    for row in ROWS:
        verify(*row)
    print(f"H3_QUOTIENT_BLOCK_IDENTITY_PASS rows={len(ROWS)}")


if __name__ == "__main__":
    main()

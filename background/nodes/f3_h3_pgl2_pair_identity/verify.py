#!/usr/bin/env python3
"""Verify the paired PGL2 fiber identities and the constant compiler."""

from __future__ import annotations

from collections import Counter


ROWS = ((97, 32), (4_289, 64), (7_937, 64))


def factors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        result.append(value)
    return tuple(result)


def check_row(prime: int, order: int) -> int:
    primitive = next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // q, prime) != 1 for q in factors(prime - 1))
    )
    generator = pow(primitive, (prime - 1) // order, prime)
    subgroup = tuple(pow(generator, exponent, prime) for exponent in range(order))
    subgroup_set = frozenset(subgroup)
    shifted = tuple((1 - value) % prime for value in subgroup if value != 1)
    products = Counter(a * b % prime for a in shifted for b in shifted)
    quotients = Counter(a * pow(b, -1, prime) % prime for a in shifted for b in shifted)

    checks = 0
    for parameter in range(2, prime):
        inv_count = sum(
            (1 + parameter * pow((x - 1) % prime, -1, prime)) % prime in subgroup_set
            for x in subgroup
            if x != 1
        )
        aff_count = sum(
            (1 + parameter * (z - 1)) % prime in subgroup_set
            for z in subgroup
        )
        if products[parameter] != inv_count:
            raise AssertionError((prime, order, parameter, products[parameter], inv_count))
        if quotients[parameter] != aff_count - 1:
            raise AssertionError((prime, order, parameter, quotients[parameter], aff_count))
        checks += 1
    return checks


def main() -> None:
    checks = sum(check_row(*row) for row in ROWS)
    for inv_count in range(40):
        for aff_count in range(2, 40):
            if inv_count + 2 * aff_count <= 39 and inv_count > 35:
                raise AssertionError((inv_count, aff_count))

    # Mutation: threshold 40 permits I_inv=36, I_aff=2 and no longer proves M35.
    if not (36 + 2 * 2 <= 40 and 36 > 35):
        raise AssertionError("threshold-40 mutation did not activate")
    print(
        "H3_PGL2_PAIR_IDENTITY_PASS "
        f"rows={len(ROWS)} parameters={checks} mutation=threshold-40-rejected"
    )


if __name__ == "__main__":
    main()


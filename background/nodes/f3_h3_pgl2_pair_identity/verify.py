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
    c_roots = frozenset(
        x * pow((x - 1) % prime, -1, prime) % prime
        for x in subgroup
        if x != 1
    )
    d_roots = subgroup_set
    if len(c_roots) != order - 1:
        raise AssertionError((prime, order, "C_n not squarefree"))
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
        a_roots = frozenset(
            (root - 1 + parameter) * pow(parameter, -1, prime) % prime
            for root in subgroup
        )
        if len(a_roots) != order:
            raise AssertionError((prime, order, parameter, "A_t not squarefree"))
        if products[parameter] != inv_count:
            raise AssertionError((prime, order, parameter, products[parameter], inv_count))
        if quotients[parameter] != aff_count - 1:
            raise AssertionError((prime, order, parameter, quotients[parameter], aff_count))
        if len(a_roots & c_roots) != inv_count:
            raise AssertionError((prime, order, parameter, "C gcd", inv_count))
        if len(a_roots & d_roots) != aff_count:
            raise AssertionError((prime, order, parameter, "D gcd", aff_count))
        checks += 1
    return checks


def main() -> None:
    checks = sum(check_row(*row) for row in ROWS)
    for inv_count in range(40):
        for aff_count in range(2, 40):
            if inv_count + 2 * aff_count <= 39 and inv_count > 35:
                raise AssertionError((inv_count, aff_count))

    for inv_count in range(19, 60):
        for aff_count in range(2, 40):
            if inv_count + 2 * aff_count <= 56 and aff_count - 1 > 17:
                raise AssertionError((inv_count, aff_count))

    # Threshold 57 admits the first forbidden rich/deep rectangle profile.
    if not (19 + 2 * 19 <= 57 and 19 >= 19 and 19 - 1 >= 18):
        raise AssertionError("threshold-57 mutation did not activate")
    if not (17 * 17 < 300):
        raise AssertionError("critical constant comparison failed")

    # Mutation: threshold 40 permits I_inv=36, I_aff=2 and no longer proves M35.
    if not (36 + 2 * 2 <= 40 and 36 > 35):
        raise AssertionError("threshold-40 mutation did not activate")
    print(
        "H3_PGL2_PAIR_IDENTITY_PASS "
        f"rows={len(ROWS)} parameters={checks} "
        "gcd_normal_form=checked "
        "mutations=threshold-40,threshold-57-rejected"
    )


if __name__ == "__main__":
    main()

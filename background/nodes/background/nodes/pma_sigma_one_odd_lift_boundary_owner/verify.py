#!/usr/bin/env python3
"""Replay the scale-two odd-lift owner on the official symbolic grid."""

from __future__ import annotations

from math import comb


def main() -> None:
    checks = 0
    mutation_trips = 0

    for exponent in range(13, 45):
        n = 1 << exponent
        quotient = n // 2
        for denominator in (2, 4, 8, 16):
            k = n // denominator
            h = k // 2 + 1

            # Pascal plus the exact ratio to Q_2; no giant binomial is built.
            if not 0 < h < quotient:
                raise AssertionError((exponent, denominator, h, quotient))
            if not 3 * (quotient - h) > quotient:
                raise AssertionError((exponent, denominator, "three-unit cap"))
            checks += 2

            # Replacing three units by two is false on every rate-half row.
            mutated = 2 * (quotient - h) > quotient
            if denominator == 2:
                if mutated:
                    raise AssertionError((exponent, "mutation did not trip"))
                mutation_trips += 1

    # Exact smallest-row columns independently verify the symbolic identity.
    n = 1 << 13
    quotient = n // 2
    for denominator in (2, 4, 8, 16):
        k = n // denominator
        h = k // 2 + 1
        q2 = comb(quotient - 1, h)
        owner = comb(quotient - 1, h - 1) + q2
        if owner != comb(quotient, h) or not owner < 3 * q2:
            raise AssertionError((denominator, owner, q2))
        checks += 1

    if mutation_trips != 32:
        raise AssertionError(mutation_trips)

    print(
        "PMA_ODD_LIFT_BOUNDARY_OWNER_PASS "
        f"checks={checks} rows={32 * 4} mutation_trips={mutation_trips}"
    )


if __name__ == "__main__":
    main()

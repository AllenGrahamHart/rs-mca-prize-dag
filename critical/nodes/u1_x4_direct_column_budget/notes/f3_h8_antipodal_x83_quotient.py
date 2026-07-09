#!/usr/bin/env python3
"""Verify the antipodal h=8 x83 quotient reduction."""

from __future__ import annotations

import random

from f3_h8_n64_x83_obstruction_interface import (
    forced_obstructions,
    h4_anchored_trades,
    is_square_mod,
    locator_from_exponents,
    root_table,
)


def antipodal_lift_support(quotient: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(quotient + tuple(e + 32 for e in quotient)))


def check_quotient_relation(p: int, quotient: tuple[int, ...]) -> tuple[bool, bool]:
    vals64 = root_table(p, 64)
    vals32 = root_table(p, 32)
    support = antipodal_lift_support(quotient)

    locator64 = locator_from_exponents(support, vals64, p)
    locator32 = locator_from_exponents(quotient, vals32, p)

    if len(locator64) != 17 or len(locator32) != 9:
        raise AssertionError((p, quotient, len(locator64), len(locator32)))
    for degree, coeff in enumerate(locator64):
        if degree % 2:
            if coeff % p:
                raise AssertionError(("odd locator coefficient", p, quotient, degree, coeff))
        elif coeff % p != locator32[degree // 2] % p:
            raise AssertionError(
                ("quotient locator mismatch", p, quotient, degree, coeff, locator32[degree // 2])
            )

    root64, obs64, lambda64 = forced_obstructions(locator64, p, 8)
    root32, obs32, lambda32 = forced_obstructions(locator32, p, 4)

    if len(root64) != 9 or len(root32) != 5:
        raise AssertionError((p, quotient, len(root64), len(root32)))
    for degree, coeff in enumerate(root64):
        if degree % 2:
            if coeff % p:
                raise AssertionError(("odd forced-root coefficient", p, quotient, degree, coeff))
        elif coeff % p != root32[degree // 2] % p:
            raise AssertionError(
                ("quotient forced-root mismatch", p, quotient, degree, coeff, root32[degree // 2])
            )

    expected_obs64 = [0, obs32[0], 0, obs32[1], 0, obs32[2], 0]
    if obs64 != expected_obs64:
        raise AssertionError(("obstruction mismatch", p, quotient, obs64, expected_obs64))
    if lambda64 != lambda32:
        raise AssertionError(("lambda mismatch", p, quotient, lambda64, lambda32))

    full64 = all(value == 0 for value in obs64) and lambda64 != 0 and is_square_mod(lambda64, p)
    full32 = all(value == 0 for value in obs32) and lambda32 != 0 and is_square_mod(lambda32, p)
    if full64 != full32:
        raise AssertionError(("full-zero mismatch", p, quotient, full64, full32))
    return full64, full32


def verify_paid_h4_lifts() -> None:
    expected = {193: 15, 4289: 7, 262337: 7}
    for p, expected_count in expected.items():
        count = 0
        for left4, right4, _ in h4_anchored_trades(p):
            quotient = tuple(sorted(set(left4) | set(right4)))
            if len(quotient) != 8:
                raise AssertionError(("bad h4 quotient support", p, left4, right4, quotient))
            full64, full32 = check_quotient_relation(p, quotient)
            if not (full64 and full32):
                raise AssertionError(("paid h4 quotient not full-zero", p, left4, right4))
            count += 1
        if count != expected_count:
            raise AssertionError((p, count, expected_count))


def verify_random_antipodal_supports() -> None:
    rng = random.Random(20260708)
    for p in (193, 4289, 262337):
        for _ in range(200):
            quotient = tuple(sorted(rng.sample(range(32), 8)))
            check_quotient_relation(p, quotient)


def main() -> None:
    verify_paid_h4_lifts()
    verify_random_antipodal_supports()
    print("antipodal locator identity: L_R(X) = M_A(X^2)")
    print("forced-root and obstruction vectors commute with Y=X^2")
    print("paid h4 quotient lifts verified at p in {193,4289,262337}")
    print("H8_ANTIPODAL_X83_QUOTIENT_PASS")


if __name__ == "__main__":
    main()

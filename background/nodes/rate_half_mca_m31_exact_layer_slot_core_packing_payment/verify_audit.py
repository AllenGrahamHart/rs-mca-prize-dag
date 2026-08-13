#!/usr/bin/env python3
"""Independent audit of the M31 exact-layer slot-core payment."""

from __future__ import annotations

from fractions import Fraction


N, M, C, BUDGET = 1048582, 67454, 5, 16777215

ROWS = (
    (130226, 65516, 342025, 12064635, 64785, 14, 60540, 181605),
    (130227, 65516, 1217008, 11189097, 64786, 5, 49340, 148005),
    (130228, 65517, 342446, 12618406, 64787, 13, 60126, 180363),
    (130229, 65517, 1305245, 11654992, 64788, 4, 43948, 131829),
    (130230, 65518, 342865, 13232329, 64789, 11, 59048, 177129),
    (130231, 65518, 1412234, 12162277, 64790, 4, 43949, 131832),
    (130232, 65519, 343295, 13916749, 64791, 9, 57431, 172278),
    (130233, 65520, 301252, 14727874, 64792, 7, 54736, 164193),
    (130234, 65520, 343725, 14684553, 64793, 7, 54736, 164193),
    (130235, 65521, 301391, 15595686, 64794, 4, 43951, 131838),
    (130236, 65521, 344160, 15551952, 64795, 4, 43951, 131838),
)


def capped_charge(e: int, lower: list[int], cap: int) -> int:
    count = len(lower)
    if count == 0:
        return 0
    budget = min(count * cap, e + count * (count + 1) * C // 2)
    values = sorted(lower, reverse=True)
    excess = budget - sum(values)
    for index, value in enumerate(values):
        addition = min(excess, cap - value)
        values[index] += addition
        excess -= addition
        if excess == 0:
            break
    assert excess == 0
    rational = sum((Fraction(N - value, M - value) for value in values),
                   Fraction())
    return rational.numerator // rational.denominator


def main() -> None:
    checks = 0
    for e, cutoff, groups, base, cap, expected_threshold, expected_u, expected_packing in ROWS:
        lowers: list[int] = []
        for _ in range(3):
            target = BUDGET - capped_charge(e, lowers, cap)
            threshold = (target - base + 1 + groups - 1) // groups
            assert threshold == expected_threshold
            inside = ((threshold * (cutoff + 1) - e
                       + threshold - 2) // (threshold - 1))
            assert inside == expected_u
            lowers.append(inside)
            checks += 4
        packing = sum(lowers) - len(lowers) * (len(lowers) - 1) * C // 2
        assert packing == expected_packing > e
        checks += 4

    e, cutoff, groups, base, cap, lower, lines = (
        130237, 65521, 1933560, 13961576, 64796, 807, 7583)
    assert 2 * (cutoff + 1) - e == lower
    max_packing = max(s * lower - s * (s - 1) * C // 2
                      for s in range(1, 1000))
    assert max_packing == 65529 < e
    budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    lower_sum = lines * lower
    full, remainder = divmod(budget - lower_sum, cap - lower)
    rational = full * Fraction(N - cap, M - cap)
    rational += Fraction(N - (lower + remainder), M - (lower + remainder))
    rational += (lines - full - 1) * Fraction(N - lower, M - lower)
    charge = rational.numerator // rational.denominator
    assert (budget, lower_sum, full, remainder) == (
        143903917, 6119481, 2153, 16119)
    assert charge == 882245
    target = BUDGET - charge
    assert target == 15894970
    assert (target - base + 1 + groups - 1) // groups == 1
    print("m31-exact-layer-slot-core-packing-audit: PASS "
          f"({checks + 17} checks; exact rational replay)")


if __name__ == "__main__":
    main()

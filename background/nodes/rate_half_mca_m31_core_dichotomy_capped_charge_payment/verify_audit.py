#!/usr/bin/env python3
"""Independent endpoint audit of the M31 core-dichotomy payment."""

from __future__ import annotations

from fractions import Fraction


N, M, C = 1048582, 67454, 5
BUDGET, LINE = 16777215, N - M + 1


def charge(e: int, lower: list[int], cap: int) -> tuple[int, list[int], int]:
    count = len(lower)
    if count == 0:
        return 0, [], 0
    budget = min(count * cap, e + count * (count + 1) * C // 2)
    allocation = sorted(lower, reverse=True)
    excess = budget - sum(allocation)
    assert excess >= 0
    for index, value in enumerate(allocation):
        addition = min(excess, cap - value)
        allocation[index] += addition
        excess -= addition
        if excess == 0:
            break
    assert excess == 0
    rational = sum((Fraction(N - value, M - value)
                    for value in allocation), Fraction())
    return rational.numerator // rational.denominator, allocation, budget


def core(threshold: int) -> tuple[int, int]:
    numerator = threshold * M - N
    total = (0 if numerator <= 0 else
             (numerator + threshold - 2) // (threshold - 1))
    return total, max(total - C, 0)


def audit_paid(e: int, cap: int, base: int, groups: int,
               threshold: int, lines: int, packing: int,
               absorption_prefix: int) -> int:
    assert absorption_prefix + LINE < BUDGET
    cores: list[int] = []
    insides: list[int] = []
    for _ in range(lines):
        old_charge = charge(e, cores, cap)[0]
        target = BUDGET - old_charge
        forced = (target - base + 1 + groups - 1) // groups
        assert forced == threshold
        total, inside = core(threshold)
        cores.append(total)
        insides.append(inside)
    got_packing = (sum(insides)
                   - len(insides) * (len(insides) - 1) * C // 2)
    assert got_packing == packing > e
    final_charge, _, _ = charge(e, cores[:-1], cap)
    if lines == 14:
        assert final_charge == 235
    else:
        assert lines == 70 and final_charge == 1104
    return 9 + 4 * lines


def main() -> None:
    checks = 0
    checks += audit_paid(130222, 64781, 12148280, 260580,
                         18, 14, 135849, 4180178)
    checks += audit_paid(130223, 64782, 12138824, 269480,
                         18, 14, 135849, 4180156)
    checks += audit_paid(130224, 64783, 12702685, 260602,
                         16, 70, 130795, 4180145)
    checks += audit_paid(130225, 64784, 12693152, 269520,
                         16, 70, 130795, 4180124)

    e, cap, lines = 130226, 64785, 14763
    budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    full, remainder = divmod(budget, cap)
    rational = full * Fraction(N - cap, M - cap)
    rational += Fraction(N - remainder, M - remainder)
    rational += (lines - full - 1) * Fraction(N, M)
    wall_charge = rational.numerator // rational.denominator
    assert (budget, full, remainder) == (545032556, 8412, 61136)
    assert wall_charge == 3199542
    target = BUDGET - wall_charge
    assert target == 13577673
    assert (target - 13317279 + 1 + 260627 - 1) // 260627 == 1
    assert core(14) == (0, 0)
    assert 4180114 + LINE == 5161243 < BUDGET
    print("m31-core-dichotomy-capped-charge-audit: PASS "
          f"({checks + 15} checks; exact rational replay)")


if __name__ == "__main__":
    main()

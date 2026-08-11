#!/usr/bin/env python3
"""Exact arithmetic replay of the type-2 FR spend calibration."""

from __future__ import annotations


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def calibrate(m: int) -> tuple[int, int, int, int]:
    capacity = (9 * m + 1) * m
    allowed_type2 = 4 * m - 2
    required = capacity // (allowed_type2 + 1) + 1
    cap_at_required = capacity // required
    cap_one_below = capacity // (required - 1)
    return capacity, required, cap_at_required, cap_one_below


def main() -> None:
    for m in (4, 8, 16, 64, 1024, 2**20, 2**37):
        capacity, required, cap, prior_cap = calibrate(m)
        check(required == 9 * m // 4 + 1, f"closed form at m={m}")
        check(cap <= 4 * m - 2, f"required spend fails at m={m}")
        check(prior_cap >= 4 * m - 1, f"one-less spend unexpectedly closes at m={m}")
        check(capacity == (16 * m - (7 * m - 1)) * m, "outside capacity")
        check((4 * m - 1) - required == 7 * m // 4 - 2, "intersection translation")

    m = 2**37
    capacity, required, cap, _ = calibrate(m)
    old_spend = 2 * m + 2
    old_cap = capacity // old_spend
    check(required == 309237645313, "official required spend")
    check((4 * m - 1) - required == 240518168574, "official intersection")
    check(old_cap == 618475290620, "official old cap")
    check(old_cap + 2 == 618475290622, "official old total")
    check(4 * m == 549755813888, "official target")
    check(required - old_spend == m // 4 - 1, "missing spend gap")
    check(cap <= 4 * m - 2, "official closure threshold")

    print(
        "RH_TYPE2_FR_EXACT_SPEND_CALIBRATION_PASS "
        f"m={m} p_req={required} intersection_max={(4*m-1)-required} "
        f"old_total={old_cap+2} target={4*m}"
    )


if __name__ == "__main__":
    main()

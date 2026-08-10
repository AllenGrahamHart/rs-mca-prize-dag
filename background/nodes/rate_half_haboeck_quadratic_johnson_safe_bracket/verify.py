#!/usr/bin/env python3
"""Replay the exact Haboeck-Johnson rate-half budget staircase."""

from math import isqrt, log2


N = 1 << 41
K = 1 << 40
BOUND_DENOMINATOR = 384**2 * (K - 1) ** 3


def budget_floor(m: int) -> int:
    numerator = (2 * m + 1) ** 14 * N**7
    return isqrt(numerator // BOUND_DENOMINATOR)


def agreement_ceiling(m: int) -> int:
    numerator = (2 * m + 1) ** 2 * N * (K - 1)
    denominator = (2 * m) ** 2
    return isqrt((numerator - 1) // denominator) + 1


def check_floor(m: int, q_m: int) -> None:
    numerator = (2 * m + 1) ** 14 * N**7
    assert BOUND_DENOMINATOR * q_m**2 <= numerator
    assert numerator < BOUND_DENOMINATOR * (q_m + 1) ** 2


def check_ceiling(m: int, a_m: int) -> None:
    threshold = (2 * m + 1) ** 2 * N * (K - 1)
    assert (2 * m * (a_m - 1)) ** 2 < threshold
    assert threshold <= (2 * m * a_m) ** 2


def main() -> None:
    values = []
    for m in range(3, 97):
        q_m = budget_floor(m)
        a_m = agreement_ceiling(m)
        check_floor(m, q_m)
        check_ceiling(m, a_m)
        values.append((m, q_m, a_m))

    assert all(values[i][1] <= values[i + 1][1] for i in range(len(values) - 1))
    assert all(values[i][2] >= values[i + 1][2] for i in range(len(values) - 1))

    expected = {
        8: (14615573564915989387247529921134, 1652128271987),
        9: (31838208335176550182206428283836, 1641330047987),
        94: (306835809425699384690368974701937497457, 1563215236073),
        95: (330298791207625937408605578064099942258, 1563128173124),
        96: (355283122119774852268896123596088746233, 1563042923987),
    }
    for m, pair in expected.items():
        assert (budget_floor(m), agreement_ceiling(m)) == pair

    half_endpoint = 3 * N // 4
    assert agreement_ceiling(8) > half_endpoint
    assert agreement_ceiling(9) < half_endpoint
    assert half_endpoint - agreement_ceiling(95) == 86139268540
    assert N - agreement_ceiling(95) == 635895082428

    cap_budget = (1 << 128) - 1
    assert budget_floor(95) <= cap_budget < budget_floor(96)

    q94 = budget_floor(94) << 128
    q95 = budget_floor(95) << 128
    assert q94**10 < 1 << 2559
    assert q95**10 > 1 << 2559

    print(
        "RATE_HALF_HABOECK_QUADRATIC_JOHNSON_SAFE_BRACKET_PASS "
        f"m_first=9 log2_q_first={128 + log2(budget_floor(9)):.12f} "
        f"m_cap=95 log2_q95={128 + log2(budget_floor(95)):.12f} "
        f"a95={agreement_ceiling(95)}"
    )


if __name__ == "__main__":
    main()

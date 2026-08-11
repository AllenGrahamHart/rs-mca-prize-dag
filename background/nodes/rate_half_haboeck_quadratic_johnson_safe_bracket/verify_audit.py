#!/usr/bin/env python3
"""Independent binary-search audit of the complete printed staircase."""


def floor_sqrt_ratio(numerator: int, denominator: int) -> int:
    """Return floor(sqrt(numerator/denominator)) without math.isqrt."""
    low = 0
    high = 1
    while denominator * high * high <= numerator:
        high *= 2
    while high - low > 1:
        middle = (low + high) // 2
        if denominator * middle * middle <= numerator:
            low = middle
        else:
            high = middle
    return low


def agreement_ceiling(m: int) -> int:
    """Find the least integer agreement by monotone binary search."""
    n = 2**41
    k = 2**40
    threshold = (2 * m + 1) ** 2 * n * (k - 1)
    low = 0
    high = n
    while high - low > 1:
        middle = (low + high) // 2
        if (2 * m * middle) ** 2 >= threshold:
            high = middle
        else:
            low = middle
    return high


def reconstruct(m: int) -> tuple[int, int, int]:
    n = 2**41
    k = 2**40
    bound_num = (2 * m + 1) ** 14 * n**7
    bound_den = 384**2 * (k - 1) ** 3
    return m, floor_sqrt_ratio(bound_num, bound_den), agreement_ceiling(m)


def check(m: int, q_m: int, a_m: int) -> None:
    n = 2**41
    k = 2**40
    bound_num = (2 * m + 1) ** 14 * n**7
    bound_den = 384**2 * (k - 1) ** 3
    assert bound_den * q_m**2 <= bound_num < bound_den * (q_m + 1) ** 2

    agreement_num = (2 * m + 1) ** 2 * n * (k - 1)
    assert (2 * m * (a_m - 1)) ** 2 < agreement_num
    assert agreement_num <= (2 * m * a_m) ** 2


def main() -> None:
    rows = [reconstruct(m) for m in range(3, 97)]
    assert all(rows[i][1] < rows[i + 1][1] for i in range(len(rows) - 1))
    assert all(rows[i][2] > rows[i + 1][2] for i in range(len(rows) - 1))
    for row in rows:
        check(*row)

    expected_landmarks = [
        (8, 14615573564915989387247529921134, 1652128271987),
        (9, 31838208335176550182206428283836, 1641330047987),
        (94, 306835809425699384690368974701937497457, 1563215236073),
        (95, 330298791207625937408605578064099942258, 1563128173124),
        (96, 355283122119774852268896123596088746233, 1563042923987),
    ]
    by_m = {row[0]: row for row in rows}
    for expected in expected_landmarks:
        assert by_m[expected[0]] == expected

    # At every adjacent boundary, the current row is simultaneously the
    # largest affordable member and the first member meeting its support.
    for current, following in zip(rows, rows[1:]):
        affordable = [row for row in rows if row[1] <= following[1] - 1]
        admissible = [row for row in rows if row[2] <= current[2]]
        assert affordable[-1] == current
        assert admissible[0] == current

    cap = 2**128 - 1
    assert by_m[95][1] <= cap < by_m[96][1]
    assert (by_m[94][1] * 2**128) ** 10 < 2**2559
    assert (by_m[95][1] * 2**128) ** 10 > 2**2559
    print(
        "RATE_HALF_HABOECK_QUADRATIC_JOHNSON_SAFE_BRACKET_AUDIT_PASS "
        "rows=94 dual_optimizers=certified"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent adjacent-inequality audit of the printed landmarks."""


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
    landmarks = [
        (8, 14615573564915989387247529921134, 1652128271987),
        (9, 31838208335176550182206428283836, 1641330047987),
        (94, 306835809425699384690368974701937497457, 1563215236073),
        (95, 330298791207625937408605578064099942258, 1563128173124),
        (96, 355283122119774852268896123596088746233, 1563042923987),
    ]
    for row in landmarks:
        check(*row)

    cap = 2**128 - 1
    assert landmarks[3][1] <= cap < landmarks[4][1]
    assert (landmarks[2][1] * 2**128) ** 10 < 2**2559
    assert (landmarks[3][1] * 2**128) ** 10 > 2**2559
    print("RATE_HALF_HABOECK_QUADRATIC_JOHNSON_SAFE_BRACKET_AUDIT_PASS")


if __name__ == "__main__":
    main()

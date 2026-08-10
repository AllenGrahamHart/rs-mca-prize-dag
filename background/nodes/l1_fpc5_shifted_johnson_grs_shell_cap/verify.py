#!/usr/bin/env python3
"""Exact official-row replay of the FPC5 shifted-Johnson shell cap."""

from math import comb, isqrt


Q_CAP = (1 << 256) - 1
SOUNDNESS_SCALE = 1 << 128


def pf6_values(rate_den: int, scale: int, touched: int) -> list[int]:
    n = 1 << 13
    k = n // rate_den
    core = k - 1
    ell, background = divmod((rate_den - 1) * k + 1, scale)
    h = touched * ell
    lower = (h + 1) // 2
    upper = min(
        ell * (scale - 2) - 1,
        core,
        (touched - 1) * ell + background,
        (core + (touched - 2) * ell + background) // 2,
    )
    if lower > upper or h > core:
        return []
    lower = max(lower, core - isqrt(core * (core - h)))
    values = []
    for defect in range(lower, upper + 1):
        u = defect - (touched - 1) * ell
        r = 2 * defect - h
        joint = (
            background * defect * defect
            + core * u * u
            - core * background * r
        )
        if u < 0 or background == 0 or joint <= 0:
            values.append(defect)
    return values


def covered(core: int, dimension: int, agreement: int, m: int) -> bool:
    return (2 * m * agreement) ** 2 >= (
        (2 * m + 1) ** 2 * core * (dimension - 1)
    )


def first_m(core: int, dimension: int, agreement: int) -> int | None:
    if agreement * agreement <= core * (dimension - 1):
        return None
    lower = 3
    upper = 3
    while not covered(core, dimension, agreement, upper):
        upper *= 2
    while lower < upper:
        middle = (lower + upper) // 2
        if covered(core, dimension, agreement, middle):
            upper = middle
        else:
            lower = middle + 1
    return lower


def haboeck_floor(core: int, dimension: int, m: int) -> int:
    numerator = (2 * m + 1) ** 14 * core**7
    denominator = 384**2 * (dimension - 1) ** 3
    return isqrt(numerator // denominator)


def list_bound(q: int, core: int, dimension: int, budget: int) -> int | None:
    denominator = q - core - dimension * budget
    if denominator <= 0:
        return None
    numerator = budget * (q - core)
    return (numerator + denominator - 1) // denominator


def paid(q: int, core: int, dimension: int, budget: int, charts: int) -> bool:
    bound = list_bound(q, core, dimension, budget)
    return bound is not None and charts * bound <= q // SOUNDNESS_SCALE


def payment_threshold(
    core: int, dimension: int, budget: int, charts: int
) -> int | None:
    lower = core + dimension * budget + 1
    upper = Q_CAP
    if not paid(upper, core, dimension, budget, charts):
        return None
    while lower < upper:
        middle = (lower + upper) // 2
        if paid(middle, core, dimension, budget, charts):
            upper = middle
        else:
            lower = middle + 1
    return lower


def classify(rate_den: int, scale: int) -> tuple[int, list[tuple[int, ...]], int]:
    n = 1 << 13
    k = n // rate_den
    core = k - 1
    ell, background = divmod((rate_den - 1) * k + 1, scale)
    pf6_count = 0
    shifted = []
    already_johnson = 0
    for touched in range(2, scale + 1):
        for defect in pf6_values(rate_den, scale, touched):
            pf6_count += 1
            u = defect - (touched - 1) * ell
            if u < 0:
                endpoint = touched * ell
                charts = 1
                j_fix = None
            else:
                endpoint = defect + ell
                charts = comb(background, u)
                j_fix = defect * defect - core * (defect - ell)
            dimension = core - endpoint
            if dimension < 2:
                continue
            agreement = core - defect
            m = first_m(core, dimension, agreement)
            if m is None:
                continue
            if j_fix is not None and j_fix > 0:
                already_johnson += 1
                continue
            budget = haboeck_floor(core, dimension, m)
            threshold = payment_threshold(core, dimension, budget, charts)
            if m > 3:
                assert not covered(core, dimension, agreement, m - 1)
            assert covered(core, dimension, agreement, m)
            shifted.append(
                (
                    touched,
                    defect,
                    u,
                    dimension,
                    -1 if j_fix is None else j_fix,
                    m,
                    budget.bit_length(),
                    charts.bit_length(),
                    -1 if threshold is None else threshold.bit_length(),
                )
            )
    return pf6_count, shifted, already_johnson


def main() -> None:
    expected = {
        (2, 5): (328, [(4, 2264, -193, 819, -1, 1176, 98, 1, 226)], 0),
        (4, 13): (43, [(3, 911, -33, 631, -1, 1456, 97, 1, 225)], 0),
        (8, 29): (15, [(3, 486, -8, 282, -1, 318, 80, 1, 208)], 0),
        (16, 57): (19, [], 19),
        (16, 58): (10, [], 10),
        (16, 59): (4, [], 4),
        (16, 61): (
            57,
            [
                (3, 248, -2, 136, -1, 376, 80, 1, 208),
                (3, 286, 36, 100, -475, 1406, 94, 50, -1),
                (3, 287, 37, 99, -413, 512, 83, 49, -1),
                (3, 288, 38, 98, -349, 307, 78, 48, 254),
                (3, 289, 39, 97, -283, 216, 75, 47, 249),
                (3, 290, 40, 96, -215, 165, 72, 46, 245),
                (3, 291, 41, 95, -145, 132, 70, 44, 242),
                (3, 292, 42, 94, -73, 109, 68, 43, 238),
            ],
            12,
        ),
    }
    for key, value in expected.items():
        assert classify(*key) == value

    print(
        "L1_FPC5_SHIFTED_JOHNSON_GRS_SHELL_CAP_PASS "
        "frontier_cells=11 cap_paid=9 cap_blocked=2"
    )


if __name__ == "__main__":
    main()

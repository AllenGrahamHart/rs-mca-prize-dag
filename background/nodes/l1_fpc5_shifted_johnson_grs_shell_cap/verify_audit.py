#!/usr/bin/env python3
"""Independent direct-inequality audit of the shifted-Johnson landmarks."""

from math import comb, isqrt


SCALE = 1 << 128

LANDMARKS = (
    (2, 5, 4, 2264, -193, 819, 1176, 226),
    (4, 13, 3, 911, -33, 631, 1456, 225),
    (8, 29, 3, 486, -8, 282, 318, 208),
    (16, 61, 3, 248, -2, 136, 376, 208),
    (16, 61, 3, 286, 36, 100, 1406, 0),
    (16, 61, 3, 287, 37, 99, 512, 0),
    (16, 61, 3, 288, 38, 98, 307, 254),
    (16, 61, 3, 289, 39, 97, 216, 249),
    (16, 61, 3, 290, 40, 96, 165, 245),
    (16, 61, 3, 291, 41, 95, 132, 242),
    (16, 61, 3, 292, 42, 94, 109, 238),
)


def direct_pf6(rate_den: int, scale: int, touched: int, defect: int) -> bool:
    n = 1 << 13
    k = n // rate_den
    core = k - 1
    ell, background = divmod((rate_den - 1) * k + 1, scale)
    h = touched * ell
    r = 2 * defect - h
    u = defect - (touched - 1) * ell
    joint = background * defect**2 + core * u**2 - core * background * r
    return (
        r >= 0
        and u <= background
        and 2 * defect <= core + (touched - 2) * ell + background
        and defect**2 <= core * r
        and (u < 0 or background == 0 or joint <= 0)
        and defect <= min(ell * (scale - 2) - 1, core)
    )


def budget(core: int, dimension: int, m: int) -> int:
    numerator = (2 * m + 1) ** 14 * core**7
    denominator = 384**2 * (dimension - 1) ** 3
    value = isqrt(numerator // denominator)
    assert denominator * value**2 <= numerator
    assert numerator < denominator * (value + 1) ** 2
    return value


def local_bound(q: int, core: int, dimension: int, q_m: int, charts: int) -> int | None:
    denominator = q - core - dimension * q_m
    if denominator <= 0:
        return None
    value = (q_m * (q - core) + denominator - 1) // denominator
    return charts * value


def main() -> None:
    for rate_den, scale, touched, defect, u, dimension, m, bit_gate in LANDMARKS:
        n = 1 << 13
        k = n // rate_den
        core = k - 1
        ell, background = divmod((rate_den - 1) * k + 1, scale)
        assert direct_pf6(rate_den, scale, touched, defect)
        assert u == defect - (touched - 1) * ell
        endpoint = touched * ell if u < 0 else defect + ell
        assert dimension == core - endpoint
        agreement = core - defect
        rhs = (2 * m + 1) ** 2 * core * (dimension - 1)
        assert (2 * m * agreement) ** 2 >= rhs
        if m > 3:
            assert (2 * (m - 1) * agreement) ** 2 < (
                (2 * (m - 1) + 1) ** 2 * core * (dimension - 1)
            )
        q_m = budget(core, dimension, m)
        charts = 1 if u < 0 else comb(background, u)
        if bit_gate:
            q = 1 << bit_gate
            total = local_bound(q, core, dimension, q_m, charts)
            assert total is not None and total <= q // SCALE
        else:
            q = (1 << 256) - 1
            total = local_bound(q, core, dimension, q_m, charts)
            assert total is not None and total > q // SCALE

    print(
        "L1_FPC5_SHIFTED_JOHNSON_GRS_SHELL_CAP_AUDIT_PASS "
        f"landmarks={len(LANDMARKS)}"
    )


if __name__ == "__main__":
    main()

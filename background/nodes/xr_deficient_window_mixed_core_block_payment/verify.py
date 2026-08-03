#!/usr/bin/env python3
"""Verify the official mixed core/block payment arithmetic."""

from math import prod


ROWS = (
    (
        "1/4", 2**41, 2**39, 2**33 + 1, 10,
        5_809_347_492, 5_767_985_277,
        3_288_278_233_653_601_276_869_020,
        3_288_278_228_033_288_972_798_440,
        747_618_070_831_366_029_933_789,
        732_194_370_222_112_484_701_579,
    ),
    (
        "1/8", 2**41, 2**38, 2**33 + 1, 10,
        6_787_763_913, 6_257_193_488,
        3_288_278_231_095_806_578_696_610,
        3_288_278_226_285_629_384_991_152,
        1_094_070_037_805_154_915_828_409,
        985_869_572_620_074_284_318_171,
    ),
    (
        "1/16", 2**41, 2**37, 2**32 + 1, 9,
        3_889_759_269, 3_376_535_400,
        3_288_278_235_812_617_761_960_026,
        3_288_278_228_233_027_003_914_950,
        1_176_340_468_015_061_167_222_396,
        2_247_266_833_636_175_323_939_571,
    ),
)


def ratio_floor(numerator, denominator):
    assert denominator > 0
    return numerator // denominator


checks = 0
for (
    name, n, k, h, s, threshold, split,
    affine_before_pin, affine_at_pin,
    mixed_low_pin, mixed_high_pin,
) in ROWS:
    redundancy = n - k
    d0 = (2 * h + 3) // 3
    x0 = d0 + 1
    budget = (17 * n * n - 25 * (n - 4)) // 25
    assert budget == 3_288_278_229_349_592_331_945_250
    assert split == (x0 + threshold - 1) // 2
    assert threshold < h

    def affine_upper(x):
        return ratio_floor(
            prod(redundancy - 2 * h + 2 * x - 1 + j
                 for j in range(1, s + 1)),
            prod(x + j for j in range(1, s + 1)),
        )

    assert affine_upper(threshold - 1) == affine_before_pin > budget
    assert affine_upper(threshold) == affine_at_pin <= budget
    assert all(j + 1 <= redundancy - 2 * h for j in range(1, s + 1))

    def a_num(x):
        return (x - 3) * (x - 4)

    def a_den(x):
        return prod(x + j for j in range(2, s + 1))

    def b_den(x):
        return (h - x) * (h - x + 1)

    low_num = n ** (s - 1) * a_num(x0)
    low_den = a_den(x0) * b_den(split)
    high_num = n ** (s - 1) * a_num(split)
    high_den = a_den(split) * b_den(threshold - 1)
    assert ratio_floor(low_num, low_den) == mixed_low_pin < budget
    assert ratio_floor(high_num, high_den) == mixed_high_pin < budget
    assert low_num < budget * low_den
    assert high_num < budget * high_den
    assert (s - 3) * x0 >= 4 * s

    # The good-pair identity and its two nearest mutations.
    r, ell = 19, 7
    assert r * (r - ell) // 2 == r * (r - 1) // 2 - r * (ell - 1) // 2
    assert r * (r - ell) // 2 > 0
    assert r * (r - (r + 1)) // 2 < 0
    checks += 14

print(
    "XR_DEFICIENT_WINDOW_MIXED_CORE_BLOCK_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)

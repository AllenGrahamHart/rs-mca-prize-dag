#!/usr/bin/env python3
"""Independent rounded-gate audit for the first-layout aggregate."""

from math import comb, isqrt


SCALE = 1 << 128


def q_m(core: int, dimension: int, m: int) -> int:
    numerator = (2 * m + 1) ** 14 * core**7
    denominator = 384**2 * (dimension - 1) ** 3
    value = isqrt(numerator // denominator)
    assert denominator * value**2 <= numerator
    assert numerator < denominator * (value + 1) ** 2
    return value


def total(
    q: int,
    source_scale: int,
    touched: int,
    core: int,
    cells: tuple[tuple[int, int, int], ...],
) -> int:
    subtotal = 0
    for dimension, m, charts in cells:
        budget = q_m(core, dimension, m)
        denominator = q - core - dimension * budget
        assert denominator > 0
        local = (budget * (q - core) + denominator - 1) // denominator
        subtotal += charts * local
    return comb(source_scale, touched) * subtotal + source_scale


def main() -> None:
    paid = (
        (5, 4, 4095, ((819, 1176, 1),), 228),
        (13, 3, 2047, ((631, 1456, 1),), 233),
        (29, 3, 1023, ((282, 318, 1),), 220),
        (
            61,
            3,
            511,
            ((136, 376, 1), (94, 109, comb(56, 42))),
            254,
        ),
    )
    for source_scale, touched, core, cells, bits in paid:
        q = 1 << bits
        assert total(q, source_scale, touched, core, cells) <= q // SCALE

    blocked = (
        (100, 1406, comb(56, 36)),
        (99, 512, comb(56, 37)),
        (98, 307, comb(56, 38)),
        (97, 216, comb(56, 39)),
        (96, 165, comb(56, 40)),
        (95, 132, comb(56, 41)),
    )
    q = (1 << 256) - 1
    for cell in blocked:
        assert total(q, 61, 3, 511, (cell,)) > q // SCALE

    print(
        "L1_FPC5_SHIFTED_JOHNSON_FIRST_LAYOUT_PAYMENT_AUDIT_PASS "
        "rounded_gates=4 blocked=6"
    )


if __name__ == "__main__":
    main()

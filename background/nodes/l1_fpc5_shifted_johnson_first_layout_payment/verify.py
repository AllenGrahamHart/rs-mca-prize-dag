#!/usr/bin/env python3
"""Exact aggregate thresholds for shifted-Johnson first-layout cells."""

from math import comb, isqrt


Q_CAP = (1 << 256) - 1
SCALE = 1 << 128


def haboeck_floor(core: int, dimension: int, m: int) -> int:
    return isqrt(
        ((2 * m + 1) ** 14 * core**7)
        // (384**2 * (dimension - 1) ** 3)
    )


def list_bound(q: int, core: int, dimension: int, budget: int) -> int | None:
    denominator = q - core - dimension * budget
    if denominator <= 0:
        return None
    return (budget * (q - core) + denominator - 1) // denominator


def aggregate(
    q: int,
    source_scale: int,
    touched: int,
    core: int,
    cells: tuple[tuple[int, int, int], ...],
) -> int | None:
    # Cells are (dimension, Haboeck m, background-chart count).
    subtotal = 0
    for dimension, m, charts in cells:
        value = list_bound(q, core, dimension, haboeck_floor(core, dimension, m))
        if value is None:
            return None
        subtotal += charts * value
    return comb(source_scale, touched) * subtotal + source_scale


def threshold(
    source_scale: int,
    touched: int,
    core: int,
    cells: tuple[tuple[int, int, int], ...],
) -> int | None:
    lower = core + 1
    for dimension, m, _ in cells:
        lower = max(
            lower,
            core + dimension * haboeck_floor(core, dimension, m) + 1,
        )

    def paid(q: int) -> bool:
        value = aggregate(q, source_scale, touched, core, cells)
        return value is not None and value <= q // SCALE

    if not paid(Q_CAP):
        return None
    upper = Q_CAP
    while lower < upper:
        middle = (lower + upper) // 2
        if paid(middle):
            upper = middle
        else:
            lower = middle + 1
    assert paid(lower)
    assert lower == 0 or not paid(lower - 1)
    return lower


def main() -> None:
    rows = (
        # rate denominator, M, t, core, cells, threshold bit length
        (2, 5, 4, 4095, ((819, 1176, 1),), 228),
        (4, 13, 3, 2047, ((631, 1456, 1),), 233),
        (8, 29, 3, 1023, ((282, 318, 1),), 220),
        (
            16,
            61,
            3,
            511,
            (
                (136, 376, 1),
                (94, 109, comb(56, 42)),
            ),
            254,
        ),
    )
    for _, source_scale, touched, core, cells, expected_bits in rows:
        value = threshold(source_scale, touched, core, cells)
        assert value is not None and value.bit_length() == expected_bits
        assert value < 1 << expected_bits

    # The other six M=61 cells fail after the touched-triple multiplier.
    failures = (
        (100, 1406, comb(56, 36)),
        (99, 512, comb(56, 37)),
        (98, 307, comb(56, 38)),
        (97, 216, comb(56, 39)),
        (96, 165, comb(56, 40)),
        (95, 132, comb(56, 41)),
    )
    for cell in failures:
        assert threshold(61, 3, 511, (cell,)) is None

    print(
        "L1_FPC5_SHIFTED_JOHNSON_FIRST_LAYOUT_PAYMENT_PASS "
        "paid_slices=4 aggregate_blocked_cells=6"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the six extended WCL divisor endpoint ledgers."""

from __future__ import annotations

import math


ROWS = [
    # ell, w, signed order M, base vars, s, k, vars, eqs, raw, orbit lower
    (1, 7, 512, 5, 2, 6, 76, 78, 842_360_690_688_000, 6_426_702_047),
    (1, 8, 512, 7, 2, 6, 89, 90, 52_436_952_995_328_000, 400_062_202_418),
    (2, 8, 1024, 6, 2, 7, 103, 105, 14_189_981_600_607_887_360, 27_065_242_005_554),
    (2, 9, 1024, 6, 3, 6, 99, 102, 1_589_277_939_268_083_384_320, 3_031_307_104_622_047),
    (4, 10, 2048, 6, 3, 7, 129, 133, 171_144_124_159_294_538_557_161_472, 81_607_877_807_280_797_271),
    (4, 11, 2048, 6, 3, 7, 142, 147, 31_552_753_072_277_211_290_356_678_656, 15_045_525_108_469_586_987_666),
]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], value: int) -> list[int]:
    return [value * coefficient for coefficient in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def in_x_squared(poly: list[int], shift: int = 0) -> list[int]:
    out = [0] * (2 * (len(poly) - 1) + shift + 1)
    for index, value in enumerate(poly):
        out[2 * index + shift] = value
    return out


def shift(poly: list[int], amount: int = 1) -> list[int]:
    return [0] * amount + poly


def check_parity_identity(ell: int, w: int) -> None:
    r = w // 2
    if w % 2:
        a = [2 + 3 * index for index in range(r)] + [1]
        b = [1] + [5 + 2 * index for index in range(r - ell)]
        f = add(in_x_squared(a, 1), scale(in_x_squared(b), -1))
        g = add(shift(multiply(a, a)), scale(multiply(b, b), -1))
        f_at_minus_x = [value if index % 2 == 0 else -value for index, value in enumerate(f)]
        squared = scale(multiply(f, f_at_minus_x), -1)
    else:
        e = [2 + 3 * index for index in range(r)] + [1]
        b = [5 + 2 * index for index in range(r - ell)]
        f = add(in_x_squared(e), scale(in_x_squared(b, 1), -1))
        g = add(multiply(e, e), scale(shift(multiply(b, b)), -1))
        f_at_minus_x = [value if index % 2 == 0 else -value for index, value in enumerate(f)]
        squared = multiply(f, f_at_minus_x)

    assert len(f) == w + 1 and f[-1] == 1
    for odd_index in range(1, 2 * ell, 2):
        assert f[w - odd_index] == 0
    assert squared == in_x_squared(g)


def check_antipodal_base_case() -> None:
    for order in (2, 4, 8, 16):
        half = order // 2
        for mask in range(1, 1 << order):
            antipodal_free = all(
                not ((mask >> point) & 1 and (mask >> (point + half)) & 1)
                for point in range(half)
            )
            if not antipodal_free:
                continue
            reduced = [
                ((mask >> point) & 1) - ((mask >> (point + half)) & 1)
                for point in range(half)
            ]
            assert any(reduced)


def verify_row(row: tuple[int, ...]) -> None:
    ell, w, order, base, s, k, variables, equations, raw, orbit_lower = row
    squared_order = order // 2
    m = squared_order.bit_length() - 1
    assert squared_order == 1 << m
    assert s == (w - 1).bit_length() - 1
    assert k == m - s
    expected_base = w - 1 - ell if w % 2 else w - ell
    assert base == expected_base
    assert variables == base + k * (2 * w - 1) - w
    assert equations == k * (2 * w - 1)
    expected_raw = math.comb(order // 2, w) * 2 ** (w - 1)
    group_order = order * (order // 2)
    assert raw == expected_raw
    assert orbit_lower == (raw + group_order - 1) // group_order
    check_parity_identity(ell, w)


def main() -> None:
    for row in ROWS:
        verify_row(row)

    check_antipodal_base_case()
    print("DLI_WCL_EXTENDED_SIX_ENDPOINTS_PASS rows=6")


if __name__ == "__main__":
    main()

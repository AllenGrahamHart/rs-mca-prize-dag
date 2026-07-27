#!/usr/bin/env python3
"""Exact arithmetic verifier for the budget-three rank-flat route fence."""


TYPE_DATA = {
    "pendant": (0, (-2, -1, -1, 0), (0, 0, 0, 0, 1, 1)),
    "cycle": (0, (-1, -1, -1, -1), (1, 0, 0, 0, 0, 1)),
    "k4_minus_edge": (1, (-2, -2, -1, -1), (0, 0, 0, 0, 0, 1)),
    "k4": (2, (-2, -2, -2, -2), (0, 0, 0, 0, 0, 0)),
    "path_singleton": (0, (-1, -1, 0, -1), (0, 0, 0, 0, 0, 1)),
    "triangle_singleton": (1, (-1, -1, -1, -2), (0, 0, 0, 0, 0, 0)),
}


def main() -> None:
    for full, t_offsets, deltas in TYPE_DATA.values():
        assert 0 in deltas
        assert max(full + offset for offset in t_offsets) >= -1

    for d in range(3, 257):
        x0 = 2 * d + 3
        f0 = 8 * d * d + 22 * d + 6
        fp0 = 4 * d * d + 24 * d + 11
        assert f0 > 0 and fp0 > 0
        for x in range(x0, 4 * d + 1):
            numerator = x * (x - 1) * (x - 2)
            denominator_upper = 2 * d * d * (x - d - 1)
            assert numerator > 4 * denominator_upper

    official_d = 1 << 39
    for x in (2 * official_d + 3, 4 * official_d):
        numerator = x * (x - 1) * (x - 2)
        denominator_upper = 2 * official_d * official_d * (x - official_d - 1)
        assert numerator // denominator_upper >= 4

    print(
        "RATE_HALF_LIST_CHAMBER_RANK_FLAT_FENCE_PASS "
        f"types={len(TYPE_DATA)} d_range=3..256 official_d={official_d}"
    )


if __name__ == "__main__":
    main()

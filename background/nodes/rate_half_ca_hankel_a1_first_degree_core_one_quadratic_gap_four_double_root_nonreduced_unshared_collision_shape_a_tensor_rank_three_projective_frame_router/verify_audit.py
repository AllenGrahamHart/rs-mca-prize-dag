#!/usr/bin/env python3
"""Independent arithmetic audit for the rank-three projective frame."""


def main():
    e = 183251937963
    m = e - 2
    n = (3 * e - 7) // 2
    rows = (9 * e - 7) // 2
    slopes = 3 * e
    assert rows - 3 * n == 7
    assert 4 * m - slopes == e - 8
    assert (e - 8 + 5) // 6 == 30541989660
    assert 6 * 30541989659 < e - 8 <= 6 * 30541989660
    print(
        "RATE_HALF_SHAPE_A_TENSOR_RANK_THREE_FRAME_AUDIT_PASS "
        "general_position_reserve=7 pair_floor=30541989660"
    )


if __name__ == "__main__":
    main()

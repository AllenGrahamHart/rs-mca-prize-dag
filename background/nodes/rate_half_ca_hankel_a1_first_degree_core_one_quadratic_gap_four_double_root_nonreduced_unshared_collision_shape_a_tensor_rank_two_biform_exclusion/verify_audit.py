#!/usr/bin/env python3
"""Independent count audit for the rank-two row-type contradiction."""


def main():
    e = 183251937963
    gamma = 3 * e
    m = e - 2
    n = (3 * e - 7) // 2
    rows = (9 * e - 7) // 2
    max_types = gamma // m
    assert max_types == 3
    assert 4 * m - gamma == e - 8 > 0
    assert rows == 3 * n + 7
    assert max_types * n == rows - 7
    print(
        "RATE_HALF_SHAPE_A_TENSOR_RANK_TWO_BIFORM_EXCLUSION_AUDIT_PASS "
        f"gamma={gamma} max_types={max_types} row_deficit=7"
    )


if __name__ == "__main__":
    main()

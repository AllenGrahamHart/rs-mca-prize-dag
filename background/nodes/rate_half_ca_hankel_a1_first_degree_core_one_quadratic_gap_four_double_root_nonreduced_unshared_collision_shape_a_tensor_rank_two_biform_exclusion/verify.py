#!/usr/bin/env python3
"""Replay the exact arithmetic in the tensor-rank-two exclusion."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def replay(mutation=None):
    official_e = 183251937963
    e_values = list(range(7, 102, 2)) + [official_e]
    first_valid = None
    for e in e_values:
        m = e - 2
        n = (3 * e - 7) // 2
        rows = (9 * e - 7) // 2
        require(2 * n == 3 * e - 7, "fiber degree")
        require(rows == 3 * n + 7, "seven-row surplus")
        if 4 * m > 3 * e and first_valid is None:
            first_valid = e
        if e >= 9:
            require(4 * m > 3 * e, "at most three row types")
            require(rows > 3 * n, "row-type contradiction")
    require(first_valid == 9, "sharp onset")

    e = official_e
    m = e - 2
    n = (3 * e - 7) // 2
    rows = (9 * e - 7) // 2
    if mutation == "types":
        require(4 * m <= 3 * e, "mutated type packing")
    if mutation == "surplus":
        require(rows == 3 * n, "mutated row count")
    require(m == 183251937961, "official parameter degree")
    require(n == 274877906941, "official fiber degree")
    require(rows == 824633720830, "official row count")
    return rows - 3 * n


def tamper_selftest():
    rejected = 0
    for mutation in ("types", "surplus"):
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == 2, "hostile mutations")
    return rejected


if __name__ == "__main__":
    surplus = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_TENSOR_RANK_TWO_BIFORM_EXCLUSION_PASS "
        f"onset=9 official_surplus={surplus} mutations={mutations}/2"
    )

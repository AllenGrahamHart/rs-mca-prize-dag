#!/usr/bin/env python3
"""Replay the rank-three projective-frame integer and incidence ledger."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def replay(mutation=None):
    e = 183251937963
    m = e - 2
    n = (3 * e - 7) // 2
    rows = (9 * e - 7) // 2
    gamma = 3 * e
    require(rows == 3 * n + 7, "projective-frame reserve")
    require(m == 183251937961, "official row degree")
    require(gamma == 549755813889, "official slope count")

    if mutation == "reserve":
        require(rows <= 3 * n, "mutated fourth-row reserve")

    minimum_double = 4 * m - gamma
    require(minimum_double == e - 8, "double-incidence floor")
    pair_floor = (minimum_double + 5) // 6
    require(pair_floor == 30541989660, "official pair floor")

    if mutation == "multiplicity":
        maximum_membership = 3
    else:
        maximum_membership = 2
    patterns = [
        bits
        for bits in range(16)
        if bits.bit_count() <= maximum_membership
    ]
    require(all(bits.bit_count() <= 2 for bits in patterns), "triple-free")
    require(
        sum(bits.bit_count() == 2 for bits in patterns) == 6,
        "six pair patterns",
    )

    if mutation == "pair_floor":
        require(6 * (pair_floor - 1) >= minimum_double, "mutated pigeonhole")
    require(6 * pair_floor >= minimum_double, "pigeonhole upper cover")
    require(6 * (pair_floor - 1) < minimum_double, "pigeonhole sharpness")
    return rows - 3 * n, minimum_double, pair_floor


def tamper_selftest():
    rejected = 0
    for mutation in ("reserve", "multiplicity", "pair_floor"):
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == 3, "hostile mutations")
    return rejected


if __name__ == "__main__":
    reserve, repeated, pair_floor = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_TENSOR_RANK_THREE_FRAME_PASS "
        f"reserve={reserve} repeated={repeated} pair_floor={pair_floor} "
        f"mutations={mutations}/3"
    )

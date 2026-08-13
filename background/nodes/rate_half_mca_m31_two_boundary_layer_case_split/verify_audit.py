#!/usr/bin/env python3
"""Independent arithmetic audit for the residue-two boundary split."""

from __future__ import annotations


R = 1048576
D = 67448
K = 6
E = 98231
BUDGET = 16777215


def raw_cap(h: int) -> int:
    outside_length = R + K - E
    agreement = D + K - h
    c = K - 1
    denominator = agreement * agreement - outside_length * c
    if denominator > 0:
        return outside_length * (agreement - c) // denominator
    gap = -denominator
    tangent = ((outside_length - agreement) ** 2
               - (outside_length - 1) * gap)
    assert 2 * agreement * agreement >= outside_length * c
    assert tangent > 0
    return ((outside_length - 1) * outside_length ** 2 * (agreement - c)
            // (agreement * tangent))


def independently_truncated(end: int) -> tuple[int, int, int]:
    values = [raw_cap(h) for h in range(1, end + 1)]
    suffix = values[-1]
    profile = [0] * end
    for index in range(end - 1, -1, -1):
        suffix = min(suffix, values[index])
        profile[index] = suffix
    previous = 0
    total = 0
    changes = 0
    for h, value in enumerate(profile, 1):
        if value != previous:
            changes += 1
            total += (value - previous) * (E // h)
            previous = value
    return total, changes, profile[-1]


def main() -> None:
    s, residue = divmod(E - K, 3)
    H = E - s - 1
    assert (s, residue, H) == (32741, 2, 65489)
    assert E - 2 * s - (s + 2) == K
    assert E - s - 2 * (s + 1) == K
    assert E - (3 * (s + 1) - 1) == K
    assert 2 * (s + 2) < E

    p2 = independently_truncated(H - 2)
    p1 = independently_truncated(H - 1)
    assert p2 == (15505282, 1670, 14129968)
    assert p1 == (16433719, 1671, 15058405)

    total_line = R + K - (D + K) + 1
    outside_length = R + K - E
    outside_agreement = D + K - H
    outside_line = ((outside_length - (K - 1))
                    // (outside_agreement - (K - 1)))
    disjoint = E // (s + 1)
    assert (total_line, outside_agreement, outside_line, disjoint) == (
        981129, 1965, 484, 3
    )
    cases = (
        p2[0] + total_line,
        p1[0] + outside_line + 1,
        p1[0] + 2,
        p1[0] + outside_line,
        p1[0] + disjoint,
    )
    assert cases == (16486411, 16434204, 16433721, 16434203, 16433722)
    assert max(cases) == 16486411
    assert BUDGET - max(cases) == 290804
    assert (98232 - K) % 3 == 0
    print(
        "RATE_HALF_MCA_M31_TWO_BOUNDARY_LAYER_CASE_SPLIT_AUDIT_PASS "
        "cases=5 bound=16486411 slack=290804 adjacent_residue=0"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify low-multiplicity six-support orbit counts by exact Burnside DP."""

from __future__ import annotations


def permutation_cycles(modulus: int, unit: int, shift: int) -> list[list[int]]:
    seen = [False] * modulus
    cycles = []
    for start in range(modulus):
        if seen[start]:
            continue
        cycle = []
        value = start
        while not seen[value]:
            seen[value] = True
            cycle.append(value)
            value = (unit * value + shift) % modulus
        cycles.append(cycle)
    return cycles


def cycle_dp(
    cycles: list[list[int]], max_mu: int, parity: int | None = None
) -> list[int]:
    mask_count = 1 << (max_mu + 1)
    dp = [[0] * mask_count for _ in range(7)]
    dp[0][0] = 1
    for cycle in cycles:
        length = len(cycle)
        if length > 6:
            continue
        if parity is not None and any(value % 2 != parity for value in cycle):
            continue
        cycle_mask = 0
        for derivative in range(max_mu + 1):
            hasse = sum(
                (derivative & ~value) == 0 for value in cycle
            ) % 2
            cycle_mask |= hasse << derivative
        for size in range(6 - length, -1, -1):
            for mask, count in enumerate(dp[size]):
                if count:
                    dp[size + length][mask ^ cycle_mask] += count
    return dp[6]


def exact_count(mask_counts: list[int], mu: int) -> int:
    lower_mask = (1 << (mu + 1)) - 1
    target = 1 << mu
    return sum(
        count for mask, count in enumerate(mask_counts)
        if mask & lower_mask == target
    )


def burnside(modulus: int, max_mu: int) -> tuple[dict[int, int], dict[int, int]]:
    fixed = {mu: 0 for mu in range(1, max_mu + 1)}
    imprimitive = {mu: 0 for mu in range(1, max_mu + 1)}
    for unit in range(1, modulus, 2):
        for shift in range(modulus):
            cycles = permutation_cycles(modulus, unit, shift)
            all_counts = cycle_dp(cycles, max_mu)
            even_counts = cycle_dp(cycles, max_mu, parity=0)
            odd_counts = cycle_dp(cycles, max_mu, parity=1)
            for mu in fixed:
                fixed[mu] += exact_count(all_counts, mu)
                imprimitive[mu] += (
                    exact_count(even_counts, mu) + exact_count(odd_counts, mu)
                )
    group_order = modulus * (modulus // 2)
    assert all(value % group_order == 0 for value in fixed.values())
    assert all(value % group_order == 0 for value in imprimitive.values())
    return (
        {mu: value // group_order for mu, value in fixed.items()},
        {mu: value // group_order for mu, value in imprimitive.items()},
    )


def main() -> None:
    orbits_128, imprimitive_128 = burnside(128, 4)
    orbits_64, imprimitive_64 = burnside(64, 2)
    orbits_32, _ = burnside(32, 1)

    assert orbits_128 == {1: 331359, 2: 177599, 3: 79360, 4: 49919}
    assert imprimitive_128[1] == 0
    assert imprimitive_128[2] == 18383
    assert imprimitive_128[3] == 0
    assert imprimitive_128[4] == 9983
    assert orbits_128[2] - imprimitive_128[2] == 159216
    assert orbits_128[4] - imprimitive_128[4] == 39936

    assert orbits_64 == {1: 18383, 2: 9983}
    assert imprimitive_64 == {1: 0, 2: 903}
    assert orbits_64[2] - imprimitive_64[2] == 9080
    assert orbits_32 == {1: 903}

    # Recursive parity division agrees exactly across ambient moduli.
    assert imprimitive_128[2] == orbits_64[1]
    assert imprimitive_128[4] == orbits_64[2]
    assert imprimitive_64[2] == orbits_32[1]

    # The identity fixes all 650,117,120 multiplicity-three supports. Since
    # 79,360*8,192 equals that number, every nonidentity fixed count is zero.
    assert orbits_128[3] * 8192 == 650117120

    print(
        "E1_PROFILE_36_AFFINE_BURNSIDE_ORBITS_PASS "
        "m2=331359 m4=159216+18383 m8=79360 "
        "m16=39936+9080+903 free_mu3_action=true"
    )


if __name__ == "__main__":
    main()

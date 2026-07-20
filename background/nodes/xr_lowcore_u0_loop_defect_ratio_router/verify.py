#!/usr/bin/env python3
"""Independent finite replay for the arbitrary-v loop-defect router."""

from __future__ import annotations

from itertools import combinations
from math import comb


def ratio_fixture(v: int, reserve: int = 2) -> tuple[int, int, int]:
    """Build two exact fibers meeting at the permitted 4+(v-1) points."""
    zero_count = v - 1
    core = tuple(range(4))
    zeros = tuple(range(4, 4 + zero_count))
    left = tuple(range(4 + zero_count, 4 + zero_count + reserve + 1))
    right = tuple(
        range(4 + zero_count + reserve + 1, 4 + zero_count + 2 * (reserve + 1))
    )
    domain = core + zeros + left + right
    q = {x: 0 if x in core + zeros else (1 if x in left else 2) for x in domain}
    gamma, eta = 3, 5
    received = {
        x: 0 if x in core + zeros else (gamma * q[x] if x in left else eta * q[x])
        for x in domain
    }
    agree_gamma = {x for x in domain if received[x] == gamma * q[x]}
    agree_eta = {x for x in domain if received[x] == eta * q[x]}
    assert agree_gamma == set(core + zeros + left)
    assert agree_eta == set(core + zeros + right)
    assert len(agree_gamma & agree_eta) == 3 + v
    assert sum(q[x] == 0 for x in agree_gamma if x not in core) == v - 1
    assert all(received[x] // q[x] == gamma for x in left)
    assert all(received[x] // q[x] == eta for x in right)

    # One extra zero forces an intersection above the load-bearing P-B cap.
    x = left[0]
    q[x] = received[x] = 0
    mutated_gamma = {y for y in domain if received[y] == gamma * q[y]}
    mutated_eta = {y for y in domain if received[y] == eta * q[y]}
    assert len(mutated_gamma & mutated_eta) == 4 + v
    return len(domain), len(left), len(right)


def peel(family: tuple[frozenset[int], ...], core_size: int, rich: int) -> bool:
    active = list(family)
    while active:
        multiplicity: dict[tuple[int, ...], int] = {}
        for block in active:
            for core in combinations(sorted(block), core_size):
                multiplicity[core] = multiplicity.get(core, 0) + 1
        choice = next(
            (
                block
                for block in active
                if sum(
                    multiplicity[core] >= 2
                    for core in combinations(sorted(block), core_size)
                )
                < rich
            ),
            None,
        )
        if choice is None:
            return True
        active.remove(choice)
    return False


def exhaustive_peeling() -> int:
    # Small exact analogue: N=6, m=5, four-cores, B_v=4, r=2 gives D_r=2.
    blocks = tuple(frozenset(block) for block in combinations(range(6), 5))
    checked = 0
    for size in range(4, len(blocks) + 1):
        for family in combinations(blocks, size):
            assert peel(family, 4, 2)
            checked += 1
    return checked


def row_profiles() -> tuple[tuple[int, int, int, int], ...]:
    budget = 8 * 1024**3
    rows = ((4, 256, 1, 2), (8, 256, 2, 3), (16, 512, 6, 7))
    output = []
    for rate_denominator, scale_denominator, residual_v, first_closed_v in rows:
        n = 1024
        redundancy = n - n // rate_denominator
        reserve = n // scale_denominator + 1
        length = redundancy + 4
        line_cap = redundancy // (reserve + 1)

        def terminal_degree(v: int) -> int:
            retained = budget + 1 - v
            block = 4 + reserve + v
            return comb(block, 4) - (
                line_cap * comb(length, 4)
            ) // retained

        assert terminal_degree(residual_v) <= 0
        assert terminal_degree(first_closed_v) > 0
        output.append(
            (rate_denominator, residual_v, first_closed_v, line_cap)
        )
    return tuple(output)


def main() -> None:
    fixtures = tuple(ratio_fixture(v) for v in (1, 2, 3))
    peel_cases = exhaustive_peeling()
    profiles = row_profiles()
    print(
        "XR_LOWCORE_U0_LOOP_DEFECT_RATIO_ROUTER_PASS "
        f"fixtures={fixtures} peel_cases={peel_cases} profiles={profiles}"
    )


if __name__ == "__main__":
    main()

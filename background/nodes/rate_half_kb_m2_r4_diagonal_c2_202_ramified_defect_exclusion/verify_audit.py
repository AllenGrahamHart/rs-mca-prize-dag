#!/usr/bin/env python3
"""Exhaust the six-vertex occupancy floor independently."""


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def defect(weights: tuple[int, ...]) -> int:
    return sum(weight * (weight - 1) // 2 for weight in weights)


def main() -> None:
    profiles = list(compositions(8, 6))
    costs = [defect(profile) for profile in profiles]
    minimizers = {tuple(sorted(profile, reverse=True))
                  for profile, cost in zip(profiles, costs) if cost == min(costs)}
    assert len(profiles) == 1287
    assert min(costs) == 2
    assert minimizers == {(2, 2, 1, 1, 1, 1)}
    assert 2 + min(costs) == 4 > 3
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_202_RAMIFIED_DEFECT_EXCLUSION_AUDIT_PASS "
        "occupancies=1287 minimum=2 minimizer=2,2,1,1,1,1 total=4"
    )


if __name__ == "__main__":
    main()

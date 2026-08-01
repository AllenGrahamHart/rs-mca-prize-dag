#!/usr/bin/env python3
"""Independent arithmetic audit of the positive residual workboard."""

import itertools
import math


def cost(multiplicity):
    return min(
        2 * math.comb(left, 2)
        + 2 * math.comb(multiplicity - left, 2)
        for left in range(multiplicity + 1)
    )


def main():
    assert tuple(cost(value) for value in range(1, 5)) == (0, 0, 2, 4)
    common = {
        "442-0a": (0, (3, 1, 1)),
        "442-1a": (1, (4, 0, 0)),
        "442-1b": (1, (2, 2, 0)),
        "433-0": (0, (2, 2, 1)),
        "433-1a": (1, (3, 1, 0)),
        "433-1b": (1, (1, 1, 2)),
    }
    debits = {
        name: loops + sum(cost(value) for value in multiplicities)
        for name, (loops, multiplicities) in common.items()
    }
    assert debits == {
        "442-0a": 2,
        "442-1a": 5,
        "442-1b": 1,
        "433-0": 0,
        "433-1a": 3,
        "433-1b": 1,
    }

    counts = {0: 0, 1: 0}
    for r in itertools.product(range(3), repeat=3):
        if sum(r) != 2:
            continue
        for loops in itertools.product(range(2), repeat=3):
            if sum(loops) > 1:
                continue
            for m01, m02, m12 in itertools.product(range(6), repeat=3):
                if sum(loops) + m01 + m02 + m12 != 5:
                    continue
                degrees = (
                    r[0] + 2 * loops[0] + m01 + m02,
                    r[1] + 2 * loops[1] + m01 + m12,
                    r[2] + 2 * loops[2] + m02 + m12,
                )
                if degrees == (4, 4, 4):
                    counts[sum(loops)] += 1
    assert counts == {0: 6, 1: 18}
    print(
        "RATE_HALF_KB_POSITIVE_RESIDUAL_LOOP_WORKBOARD_AUDIT_PASS "
        "cross_costs=0,0,2,4 outside_raw=6,18"
    )


if __name__ == "__main__":
    main()

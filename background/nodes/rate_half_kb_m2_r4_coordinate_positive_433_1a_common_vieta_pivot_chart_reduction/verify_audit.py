#!/usr/bin/env python3
"""Independent finite audit of the pivot-chart rank criterion."""

import itertools


PRIME = 29
VECTORS = ((0, 0), (1, 0), (0, 1), (1, 1), (2, 1))


def wedge(left, right):
    return (left[0] * right[1] - left[1] * right[0]) % PRIME


def quotient_rank(vectors):
    if all(vector == (0, 0) for vector in vectors):
        return 0
    pivot = next(vector for vector in vectors if vector != (0, 0))
    return 1 if all(wedge(pivot, vector) == 0 for vector in vectors) else 2


def main():
    configurations = 0
    chart_checks = 0
    zero_branches = 0
    for vectors in itertools.product(VECTORS, repeat=4):
        configurations += 1
        expected = quotient_rank(vectors) <= 1
        if all(vector == (0, 0) for vector in vectors):
            zero_branches += 1
            assert expected
        for pivot_index, pivot in enumerate(vectors):
            if pivot == (0, 0):
                continue
            chart_checks += 1
            observed = all(
                wedge(pivot, vector) == 0
                for index, vector in enumerate(vectors)
                if index != pivot_index
            )
            assert observed == expected
    assert configurations == len(VECTORS) ** 4
    assert zero_branches == 1
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_COMMON_VIETA_PIVOT_CHART_AUDIT_PASS "
        f"configurations={configurations} chart_checks={chart_checks} "
        f"zero_branches={zero_branches}"
    )


if __name__ == "__main__":
    main()

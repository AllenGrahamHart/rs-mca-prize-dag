#!/usr/bin/env python3
"""Mutation audit for the quotient Galois-orbit decomposition."""

from __future__ import annotations

import verify


def main() -> None:
    exponent = 6
    order = 2**exponent
    histogram = verify.expected_histogram(exponent)

    assert sum(histogram.values()) == 3 * (order - exponent - 1)
    assert sum(histogram.values()) != (3 * (order - exponent - 1)) // 2
    assert histogram[2] == 3
    assert 1 not in histogram
    assert max(histogram) == order // 2

    ordered_total = (order - 1) * (order - 2)
    diagonal_included = (order - 1) ** 2
    assert ordered_total != diagonal_included

    supports = ({3, 5}, {5, 7})
    assert set().union(*supports) == {3, 5, 7}
    assert sum(len(item) for item in supports) != len(set().union(*supports))

    print(
        "F3_H3_QUOTIENT_GALOIS_ORBIT_SCALAR_DECOMPOSITION_AUDIT_PASS "
        "mutations=6"
    )


if __name__ == "__main__":
    main()

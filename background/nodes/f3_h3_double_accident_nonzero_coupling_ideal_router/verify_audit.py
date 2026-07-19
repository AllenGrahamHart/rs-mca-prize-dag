#!/usr/bin/env python3
"""Independent arithmetic audit for the nonzero-coupling selection."""

from __future__ import annotations

import itertools
from collections import defaultdict


def valuation_patterns() -> int:
    checked = 0
    for levels in itertools.combinations_with_replacement(range(8), 3):
        total = sum(1 << level for level in levels)
        if total & (total - 1):
            continue
        output_level = total.bit_length() - 1
        assert levels == (levels[0], levels[0], levels[0] + 1)
        assert output_level == levels[0] + 2
        checked += 1
    assert checked == 7
    return checked


def anchor_audit(n: int) -> tuple[int, int]:
    anchors: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for q in range(1, n):
        if 4 * q % n == 0:
            continue
        roots = (q, (q + n // 2) % n, (2 * q + n // 2) % n)
        output = 4 * q % n
        for denominator_index in range(3):
            denominator = roots[denominator_index]
            product_pair = tuple(
                sorted(value for index, value in enumerate(roots) if index != denominator_index)
            )
            anchors.add((product_pair, (denominator, output)))
    assert len(anchors) == 3 * (n - 4) // 2

    by_product: dict[tuple[int, int], int] = defaultdict(int)
    for product_pair, _ in anchors:
        by_product[product_pair] += 1
    assert max(by_product.values()) == 1
    return len(anchors), max(by_product.values())


def main() -> None:
    patterns = valuation_patterns()
    anchors = [anchor_audit(n) for n in (8, 16, 32, 64, 128)]
    for quotient_multiplicity in range(2, 101):
        assert quotient_multiplicity - 1 >= 1
    for n in (8, 8192, 1 << 41):
        assert 17 * (n - 1) ** 2 < 300 * n * n
    print(
        "AUDIT_F3_H3_DOUBLE_ACCIDENT_NONZERO_COUPLING_IDEAL_ROUTER_PASS "
        f"valuation_patterns={patterns} anchors={','.join(str(row[0]) for row in anchors)}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent pole-profile and quartic-defect audit."""

from itertools import product


def defect(weight_histogram: tuple[int, ...]) -> int:
    return sum(weight * (weight - 1) // 2 for weight in weight_histogram)


def main() -> None:
    rows = []
    for inner in (2, 3, 4, 5, 6, 10, 12, 15, 20, 30):
        outer = 60 // inner
        for a, b in product(range(outer + 1), repeat=2):
            if 5 * a + b != outer:
                continue
            ramification = b * (4 * inner // 5) if inner % 5 == 0 else None
            if b == 0 or (inner % 5 == 0 and ramification <= 2 * inner - 2):
                rows.append((inner, outer, a, b))
    assert [row[0] for row in rows] == [2, 3, 4, 5, 6, 10, 12, 30]

    nonsimple = set()
    for twos in range(4):
        weights = (2,) * twos + (1,) * (24 - 2 * twos)
        if defect(weights) <= 3:
            nonsimple.add((twos, 0, defect(weights)))
    weights = (3,) + (1,) * 21
    assert defect(weights) == 3
    nonsimple.add((0, 1, 3))
    assert nonsimple == {(0, 0, 0), (1, 0, 1), (2, 0, 2), (3, 0, 3), (0, 1, 3)}
    print("RATE_HALF_KB_Q6_U2_PRIMITIVE_SUBDEGREE4_ROUTE_CUT_AUDIT_PASS")


if __name__ == "__main__":
    main()

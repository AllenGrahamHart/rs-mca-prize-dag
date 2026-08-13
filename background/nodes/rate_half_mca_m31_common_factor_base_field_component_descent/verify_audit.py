#!/usr/bin/env python3
"""Independent degree-partition audit of base-field component descent."""

from __future__ import annotations


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def main() -> None:
    records = []
    partition_checks = 0
    for degree in range(2, 44):
        captured = 7583 - (52 - degree) ** 2
        retained = captured - degree**2
        per_component = (retained + degree - 1) // degree
        records.append((degree, captured, retained, per_component))
        for partition in partitions(degree):
            assert sum(partition) == degree
            assert sum(part * part for part in partition) <= degree**2
            partition_checks += 2

    assert min(record[2] for record in records) == 5079
    assert min(record[3] for record in records) == 132
    assert records[0] == (2, 5083, 5079, 2540)
    assert records[-1] == (43, 7502, 5653, 132)

    pairs, core, intersection, support = 5079, 807, 5, 130237
    numerator = pairs * core * core
    denominator = core + intersection * (pairs - 1)
    points, remainder = divmod(numerator, denominator)
    if remainder:
        points += 1
    assert points == 126263
    assert support - points == 3974
    checks = partition_checks + 7 * len(records) + 23
    print("m31-common-factor-base-field-component-descent-audit: PASS "
          f"({checks} checks; degree_partitions=2..43)")


if __name__ == "__main__":
    main()

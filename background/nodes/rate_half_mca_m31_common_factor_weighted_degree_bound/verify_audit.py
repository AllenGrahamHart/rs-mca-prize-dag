#!/usr/bin/env python3
"""Independent exhaustive audit of the weighted-degree threshold."""


def count_weighted_monomials(degree: int) -> int:
    count = 0
    for y_degree in range(degree // 5 + 1):
        for z_degree in range(degree // 5 - y_degree + 1):
            count += degree - 5 * (y_degree + z_degree) + 1
    return count


def main() -> None:
    dimension = 938
    table = [count_weighted_monomials(degree) for degree in range(265)]
    assert table[46] == 935 < dimension
    assert table[47] == 990 >= dimension
    assert all(value < dimension for value in table[:47])
    assert all(table[index] < table[index + 1] for index in range(264))

    factor_weight = 264 - next(
        index for index, value in enumerate(table) if value >= dimension)
    assert factor_weight == 217
    assert factor_weight // 5 == 43

    e, forced, ambient, core, intersection = 130237, 7583, 52, 807, 5
    records = []
    for degree in range(2, 44):
        on_factor = forced - (ambient - degree) ** 2
        numerator = on_factor * core * core
        denominator = core + intersection * (on_factor - 1)
        points = (numerator + denominator - 1) // denominator
        records.append((degree, on_factor, points, e - points))
    assert len(records) == 42
    assert records[0] == (2, 5083, 126266, 3971)
    assert all(records[index][1] < records[index + 1][1]
               for index in range(len(records) - 1))
    assert all(records[index][2] <= records[index + 1][2]
               for index in range(len(records) - 1))
    assert max(record[3] for record in records) == 3971
    checks = len(table) + 6 * len(records) + 31
    print("m31-common-factor-weighted-degree-bound-audit: PASS "
          f"({checks} checks; quotient_degrees=0..264; "
          "nonlinear_degrees=2..43)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact finite-field rank replay for the connected weld dichotomy."""

Q = 101


def rank(rows: list[list[int]], columns: int) -> int:
    pivots: dict[int, list[int]] = {}
    for source in rows:
        row = [value % Q for value in source]
        for column, pivot in pivots.items():
            if row[column]:
                factor = row[column]
                row = [
                    (left - factor * right) % Q
                    for left, right in zip(row, pivot)
                ]
        for column, value in enumerate(row):
            if value:
                inverse = pow(value, -1, Q)
                pivots[column] = [entry * inverse % Q for entry in row]
                break
    return len(pivots)


def row_poly(x: int, t: int) -> int:
    return (t + 3) * (t - x) * (t - (x - 1)) % Q


def fiber_poly(t: int, x: int) -> int:
    return (x - t) * (x - (t + 1)) % Q


def weld_rows() -> tuple[list[list[int]], int]:
    xset = list(range(5, 11))
    zset = [1, 2, 3, 4]
    rows = []
    for t in zset:
        nonincident = [x for x in xset if fiber_poly(t, x) != 0]
        anchor = nonincident[0]
        for x in nonincident[1:]:
            row = [0] * len(xset)
            row[xset.index(x)] = row_poly(x, t) * fiber_poly(t, anchor) % Q
            row[xset.index(anchor)] = (
                -row_poly(anchor, t) * fiber_poly(t, x)
            ) % Q
            rows.append(row)
    return rows, len(xset)


def main() -> None:
    rows, columns = weld_rows()
    assert rank(rows, columns) == columns - 1

    tampered = [row[:] for row in rows]
    tampered[-1][0] = (tampered[-1][0] + 1) % Q
    assert rank(tampered, columns) == columns
    print("PASS connected scalar-weld rank dichotomy tamper=1/1")


if __name__ == "__main__":
    main()

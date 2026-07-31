#!/usr/bin/env python3
"""Independent finite-field audit of the 433 minor formulas."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
P = 101


def determinant(rows):
    total = 0
    for column in range(4):
        minor = [row[:column] + row[column+1:] for row in rows[1:]]
        value = (
            minor[0][0]*(minor[1][1]*minor[2][2]-minor[1][2]*minor[2][1])
            - minor[0][1]*(minor[1][0]*minor[2][2]-minor[1][2]*minor[2][0])
            + minor[0][2]*(minor[1][0]*minor[2][1]-minor[1][1]*minor[2][0])
        )
        total += (-1 if column % 2 else 1)*rows[0][column]*value
    return total % P


def row(k, product):
    return [-product % P, -product*k % P, 1, k % P]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    m, r, b, c = 2, 7, 3, 5
    products = (-1, -c*c, b, -b, b*c)
    x1 = (-m, m, 1, m*m, -m*m)
    actual = determinant([row(x1[i], products[i]) for i in (0,1,2,3)])
    expected = -2*m*(b-c)*(b+c)*(m-1)*(m+1) % P
    require(actual == expected != 0, "X1 numeric minor")

    x2 = (-m*m, m, 1, m*m, -m)
    actual = determinant([row(x2[i], products[i]) for i in (1,2,3,4)])
    expected = 2*b*m*(b+c**3)*(m-1)*(m+1) % P
    require(actual == expected, "X2 numeric minor")
    statement = (NODE / "statement.md").read_text()
    require("six cells" in statement and "other seven" in statement, "frontier")
    print(f"RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_PRODUCT_CUT_AUDIT_PASS minors={actual}/{expected}")


if __name__ == "__main__":
    main()

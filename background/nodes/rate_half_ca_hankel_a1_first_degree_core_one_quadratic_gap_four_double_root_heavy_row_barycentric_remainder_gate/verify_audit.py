#!/usr/bin/env python3
"""Independent hard-coded audit of the barycentric heavy-row fixture."""


P = 101
WEIGHTS = [1, 96, 10, 91, 5]
ROWS = [
    [36, 83, 45, 1],
    [38, 88, 54, 1],
    [40, 93, 63, 1],
    [42, 98, 72, 1],
    [44, 2, 81, 1],
]
HEAVY = [46, 7, 90, 1]
REMAINDER_COLUMNS = [
    [74, 52],
    [7, 95],
    [40, 9],
    [7, 95],
    [74, 52],
]


def main() -> None:
    extrapolated = [
        sum(weight * row[index] for weight, row in zip(WEIGHTS, ROWS)) % P
        for index in range(4)
    ]
    assert extrapolated == HEAVY

    # HEAVY=(t-7)^2(t+3) in ascending coefficient order.
    assert HEAVY == [49 * 3 % P, (49 + 87 * 3) % P, (87 + 3) % P, 1]
    assert [
        sum(column[index] for column in REMAINDER_COLUMNS) % P
        for index in range(2)
    ] == [0, 0]

    mutated = ROWS[0][:]
    mutated[0] = (mutated[0] + 1) % P
    changed = [
        (sum(weight * row[index] for weight, row in zip(WEIGHTS, ROWS))
         + WEIGHTS[0] * (1 if index == 0 else 0)) % P
        for index in range(4)
    ]
    assert changed != HEAVY
    assert mutated[0] == 37
    print("RATE_HALF_HEAVY_ROW_BARYCENTRIC_REMAINDER_GATE_AUDIT_PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent truncated-series audit of the two obstruction jets."""


def order(coefficients: list[int]) -> int:
    for index, coefficient in enumerate(coefficients):
        if coefficient:
            return index
    return len(coefficients)


def main() -> None:
    x_star = 3
    q_row_h = [0, 0, 0, 0, 0, 0, 5]
    expected = {(0, 0): 4, (4, 0): 2, (0, 7): 3, (4, 7): 2}

    for jets, expected_order in expected.items():
        kappa_2, kappa_3 = jets
        f_i = [0, 0, kappa_2, kappa_3, 9, 1, 0]
        f_next = [
            x_star * left - right
            for left, right in zip(f_i, q_row_h)
        ]
        assert order(f_i) == expected_order
        assert order(f_next) == expected_order
        assert f_next[2] == x_star * kappa_2
        assert f_next[3] == x_star * kappa_3

    print("RATE_HALF_NONREDUCED_UNSHARED_TWO_JET_AUDIT_PASS branches=4")


if __name__ == "__main__":
    main()

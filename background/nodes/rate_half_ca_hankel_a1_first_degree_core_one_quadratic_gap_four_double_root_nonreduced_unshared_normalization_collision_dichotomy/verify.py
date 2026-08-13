#!/usr/bin/env python3
"""Exhaust the degree-two normalization valuation equation."""


def main() -> None:
    solutions = []

    # B=2b: e*s=4 with the previously proved s>=2.
    for ramification in range(1, 5):
        for base_order in range(2, 5):
            if ramification * base_order == 4:
                solutions.append(((2,), (ramification,), base_order))

    # B=b1+b2: e_i*s=2 for both branches.
    for left_ramification in range(1, 3):
        for right_ramification in range(1, 3):
            for base_order in range(2, 5):
                if (
                    left_ramification * base_order == 2
                    and right_ramification * base_order == 2
                ):
                    solutions.append(
                        (
                            (1, 1),
                            (left_ramification, right_ramification),
                            base_order,
                        )
                    )

    assert solutions == [
        ((2,), (1,), 4),
        ((2,), (2,), 2),
        ((1, 1), (1, 1), 2),
    ]
    assert all(order != 3 for _, _, order in solutions)

    collision_orders = [sum(indices) for _, indices, order in solutions if order == 2]
    assert collision_orders == [2, 2]
    print(
        "RATE_HALF_NONREDUCED_NORMALIZATION_COLLISION_PASS "
        "solutions=3 closed=1 collisions=2"
    )


if __name__ == "__main__":
    main()

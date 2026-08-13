#!/usr/bin/env python3
"""Replay all determinant-order-four Smith/jet routes."""


def partitions(total: int, minimum: int = 1):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def pairing_order(profile: tuple[int, ...], image_order: int) -> int:
    singular = min(
        exponent + 2 * max(0, image_order - exponent)
        for exponent in profile
    )
    regular = 2 * image_order
    return min(singular, regular)


def main() -> None:
    profiles = tuple(partitions(4))
    assert profiles == (
        (1, 1, 1, 1),
        (1, 1, 2),
        (1, 3),
        (2, 2),
        (4,),
    )

    table = {
        profile: (pairing_order(profile, 2), pairing_order(profile, 3))
        for profile in profiles
    }
    assert table == {
        (1, 1, 1, 1): (3, 5),
        (1, 1, 2): (2, 4),
        (1, 3): (3, 3),
        (2, 2): (2, 4),
        (4,): (4, 4),
    }

    survivors = {
        profile
        for profile, (order_two, order_three) in table.items()
        if len(profile) >= 2
        and not (order_two >= 3 and order_three >= 4)
    }
    assert survivors == {(1, 3), (2, 2), (1, 1, 2)}
    print(
        "RATE_HALF_NONREDUCED_HIGHER_CORANK_SMITH_ROUTER_PASS "
        "profiles=[1,3],[2,2],[1,1,2] collision=separate"
    )


if __name__ == "__main__":
    main()

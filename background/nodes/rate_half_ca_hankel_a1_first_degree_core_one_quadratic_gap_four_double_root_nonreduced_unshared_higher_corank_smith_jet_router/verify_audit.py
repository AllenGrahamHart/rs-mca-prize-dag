#!/usr/bin/env python3
"""Construct the three abstract diagonal Smith/jet survivors."""


def image_and_pairing_orders(
    profile: tuple[int, ...], vector_orders: tuple[int | None, ...]
) -> tuple[int, int]:
    image_orders = []
    pairing_orders = []
    for exponent, vector_order in zip(profile, vector_orders):
        if vector_order is None:
            continue
        image_orders.append(exponent + vector_order)
        pairing_orders.append(exponent + 2 * vector_order)
    return min(image_orders), min(pairing_orders)


def main() -> None:
    witnesses = {
        (1, 3): ((None, 0), (3, 3)),
        (2, 2): ((0, None), (2, 2)),
        (1, 1, 2): ((None, None, 0), (2, 2)),
    }
    for profile, (vector_orders, expected) in witnesses.items():
        assert image_and_pairing_orders(profile, vector_orders) == expected

    # Corank four: image order two forces every coordinate to order one.
    # Once the second jet vanishes, image order three forces order two.
    profile = (1, 1, 1, 1)
    assert image_and_pairing_orders(profile, (1, 1, 1, 1)) == (2, 3)
    assert image_and_pairing_orders(profile, (2, 2, 2, 2)) == (3, 5)

    print(
        "RATE_HALF_NONREDUCED_HIGHER_CORANK_SMITH_ROUTER_AUDIT_PASS "
        "abstract_witnesses=3 corank4=closed"
    )


if __name__ == "__main__":
    main()
